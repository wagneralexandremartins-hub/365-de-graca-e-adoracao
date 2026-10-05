#!/usr/bin/env python3
"""
Aplica o menu central (assets/js/site-nav.js + assets/css/site-header.css)
nas páginas em português do 365 Graça & Adoração.

O que muda em cada página:
  <head>  → + fontes, site-header.css e site-nav.js (bloco marcado)
  <body>  → + link "Pular para o conteúdo", <header id="site-header"> com
            fallback <noscript>, e <nav class="context-nav"> com os links
            contextuais que a página já tinha (voltar, trilha do livro)
  remove  → o topo antigo (marca + menu), o seletor flutuante de idioma
            (#lang-selector) e a barra .lang-switcher. As URLs de tradução
            específicas da página passam para data-lang-* do novo header.

Nada mais é tocado. Para cada arquivo o script prova que:
  arquivo antigo − trechos removidos == arquivo novo − blocos inseridos
e que nenhum trecho removido contém conteúdo (títulos, parágrafos etc.).
Se a prova falhar, o arquivo não é gravado.

Uso:
  python scripts/aplicar_menu_central.py                  # dry-run (todas PT)
  python scripts/aplicar_menu_central.py --only a,b       # restringe
  python scripts/aplicar_menu_central.py --only-file lista.txt  # uma página por linha
  python scripts/aplicar_menu_central.py --diff-out f.diff
  python scripts/aplicar_menu_central.py --apply          # grava (com backup zip)
"""

import re
import sys
import zipfile
import difflib
import posixpath
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
MARK = "site-nav:v1"
EXCLUDE_TOP = {"_backups", ".git", ".github", "en", "es", "redesign", "scripts", "node_modules"}

# Itens do menu (fallback <noscript>). Manter igual ao MENU de site-nav.js.
MENU = [
    ("/", "Início"),
    ("/redesign/antigo-testamento.html", "Antigo Testamento"),
    ("/08-novo-testamento/", "Novo Testamento"),
    ("/personagens/index.html", "Personagens"),
    ("/mapas/index.html", "Mapas"),
    ("/timeline/index.html", "Linha do Tempo"),
    ("/estudos/", "Estudos"),
    ("/loja-365/", "Loja 365"),
]

# Links do topo antigo que o novo cabeçalho já cobre (são descartados).
# Comparação feita sobre o caminho absoluto normalizado (sem index.html).
COVERED = {"/", "/blocos/", "/personagens/", "/loja-365/", "/mapas/", "/timeline/",
           "/estudos/", "/busca/", "/08-novo-testamento/"}

CONTENT_TAGS = re.compile(r"<(h[1-6]|p|main|article|section|blockquote|table|form|iframe|video|figure)\b", re.I)
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param",
        "source", "track", "wbr"}
TOKEN = re.compile(r"<!--[\s\S]*?-->|<(script|style)\b[^>]*>[\s\S]*?</\1\s*>|<(/?)([a-zA-Z][a-zA-Z0-9-]*)\b([^>]*)>")


# ── Leitura de elementos (posições no texto) ──────────────────────────
class El:
    __slots__ = ("tag", "attrs", "start", "open_end", "end", "parent", "children")

    def __init__(self, tag, attrs, start, open_end, parent):
        self.tag, self.attrs, self.start, self.open_end = tag, attrs, start, open_end
        self.end, self.parent, self.children = None, parent, []

    def cls(self):
        m = re.search(r'\bclass\s*=\s*"([^"]*)"', self.attrs)
        return m.group(1).split() if m else []

    def id(self):
        m = re.search(r'\bid\s*=\s*"([^"]*)"', self.attrs)
        return m.group(1) if m else None


def parse(html):
    root = El("#root", "", 0, 0, None)
    root.end = len(html)
    stack = [root]
    for m in TOKEN.finditer(html):
        if m.group(0).startswith("<!--") or m.group(1):
            continue
        closing, tag, attrs = m.group(2) == "/", m.group(3).lower(), m.group(4)
        if not closing:
            el = El(tag, attrs, m.start(), m.end(), stack[-1])
            stack[-1].children.append(el)
            if tag in VOID or attrs.rstrip().endswith("/"):
                el.end = m.end()
            else:
                stack.append(el)
        else:
            for i in range(len(stack) - 1, 0, -1):
                if stack[i].tag == tag:
                    for el in stack[i:]:
                        el.end = m.end() if el is stack[i] else m.start()
                    del stack[i:]
                    break
    for el in stack[1:]:
        el.end = len(html)
    return root


def walk(el):
    for c in el.children:
        yield c
        yield from walk(c)


def find(root, pred):
    return next((e for e in walk(root) if pred(e)), None)


# ── Regras ────────────────────────────────────────────────────────────
def norm(href, page_url):
    if href.startswith(("http:", "https:", "mailto:", "tel:", "#")):
        return href
    path = href.split("#")[0].split("?")[0]
    if not path.startswith("/"):
        path = posixpath.normpath(posixpath.join(posixpath.dirname(page_url), path))
        if href.endswith("/"):
            path += "/"
    if path.endswith("/index.html"):
        path = path[: -len("index.html")]
    if path == "/index.html":
        path = "/"
    return path


def top_container(html, brand):
    """Maior ancestral (header/nav/div.topbar) da marca que não tem conteúdo."""
    best, el = None, brand.parent
    while el is not None and el.tag not in ("body", "#root"):
        inner = html[el.open_end:el.end]
        if CONTENT_TAGS.search(inner):
            break
        if el.tag in ("header", "nav") or (el.tag == "div" and "topbar" in el.cls()):
            best = el
        el = el.parent
    return best


def following_nav(html, el):
    """Irmão <nav> logo após o elemento (marca solta dentro do conteúdo)."""
    sibs = el.parent.children
    i = sibs.index(el)
    if i + 1 < len(sibs):
        nxt = sibs[i + 1]
        if nxt.tag == "nav" and not html[el.end:nxt.start].strip() and not CONTENT_TAGS.search(html[nxt.open_end:nxt.end]):
            return nxt
    return None


def links_in(html, start, end):
    out = []
    for m in re.finditer(r"<a\b([^>]*)>([\s\S]*?)</a>", html[start:end]):
        attrs, inner = m.group(1), m.group(2)
        href = re.search(r'href\s*=\s*"([^"]*)"', attrs)
        out.append({"attrs": attrs, "href": href.group(1) if href else "", "inner": inner.strip(),
                    "brand": "brand" in (re.search(r'class\s*=\s*"([^"]*)"', attrs) or [None, ""])[1].split(),
                    "active": bool(re.search(r'class\s*=\s*"[^"]*\bactive\b', attrs))})
    return out


def lang_hrefs(html, els):
    """URLs de tradução da página (prioriza .lang-switcher, que é específico)."""
    found = {}
    for el in els:
        for a in links_in(html, el.open_end, el.end):
            h, label = a["href"], re.sub(r"<[^>]+>", "", a["inner"]) + " " + a["attrs"]
            if h.startswith("/en/") or "English" in label:
                found.setdefault("en", h)
            elif h.startswith("/es/") or "Español" in label:
                found.setdefault("es", h)
            elif "Português" in label:
                found.setdefault("pt", h)
    return found


def expand(html, start, end):
    """Inclui indentação antes e a quebra de linha depois, se o trecho ocupa a linha toda."""
    ls = html.rfind("\n", 0, start) + 1
    if html[ls:start].strip() == "":
        start = ls
    if html[end:end + 2] == "\r\n":
        end += 2
    elif html[end:end + 1] == "\n":
        end += 1
    return start, end


# ── Transformação ─────────────────────────────────────────────────────
def transform(rel, html):
    nl = "\r\n" if "\r\n" in html else "\n"
    page_url = "/" + rel.replace("\\", "/")
    root = parse(html)
    body = find(root, lambda e: e.tag == "body")
    head_close = html.lower().find("</head>")
    if body is None or head_close < 0:
        return None, "sem <head>/<body>"
    if MARK in html:
        return None, "já aplicado"

    removals, report = [], {"removido": [], "mantidos": [], "descartados": []}

    # 1) seletores de idioma
    lang_els = [e for e in walk(body) if e.tag == "div" and (e.id() == "lang-selector" or "lang-switcher" in e.cls())]
    langs = lang_hrefs(html, sorted(lang_els, key=lambda e: "lang-switcher" not in e.cls()))
    for e in lang_els:
        s = e.start
        cm = re.search(r"<!--\s*Seletor de Idioma Flutuante\s*-->\s*$", html[:s])
        if cm:
            s = cm.start()
        removals.append((s, e.end))
        report["removido"].append("#lang-selector" if e.id() == "lang-selector" else ".lang-switcher")

    # 2) topo antigo
    brand = find(body, lambda e: e.tag == "a" and "brand" in e.cls())
    if brand is None:
        return None, "marca (a.brand) não encontrada — variante não reconhecida"
    top = top_container(html, brand)
    if top is not None:
        parts = [top]
    else:
        nav = following_nav(html, brand)
        parts = [brand] + ([nav] if nav else [])
    for el in parts:
        if CONTENT_TAGS.search(html[el.open_end:el.end]):
            return None, f"topo <{el.tag}> contém conteúdo — não tocado"
        removals.append((el.start, el.end))
        report["removido"].append(f"<{el.tag}{(' class=' + '.'.join(el.cls())) if el.cls() else ''}>")

    # 3) links contextuais do topo antigo
    kept, seen = [], set()
    for el in parts:
        for a in links_in(html, el.start, el.end):
            if a["brand"]:
                continue
            n = norm(a["href"], page_url)
            label = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", a["inner"])).strip()
            if n in COVERED or n.startswith("/#") or n in seen:
                report["descartados"].append(f"{label} ({a['href']})")
                continue
            seen.add(n)
            kept.append(a)
            report["mantidos"].append(f"{label} ({a['href']})")

    # 4) novo bloco do body
    data = "".join(f' data-lang-{k}="{v}"' for k, v in sorted(langs.items())
                   if v not in {"pt": ("/",), "en": ("/en/",), "es": ("/es/",)}[k])
    fallback = "".join(f'<a href="{h}">{t}</a>' for h, t in MENU)
    ctx = ""
    if kept:
        items = '<span class="sh-sep" aria-hidden="true">·</span>'.join(
            f'<a href="{a["href"]}"{" aria-current=\"page\"" if a["active"] else ""}>{a["inner"]}</a>' for a in kept)
        ctx = f'<nav class="context-nav" aria-label="Navegação desta seção">{items}</nav>{nl}'
    body_block = (f"<!-- {MARK} -->{nl}"
                  f'<a class="sh-skip" href="#conteudo">Pular para o conteúdo</a>{nl}'
                  f'<header id="site-header" class="site-header"{data}>'
                  f'<noscript><nav class="sh-fallback" aria-label="Navegação principal">{fallback}</nav></noscript>'
                  f"</header>{nl}{ctx}"
                  f'<span id="conteudo"></span>{nl}'
                  f"<!-- /{MARK} -->{nl}")
    head_block = (f"<!-- {MARK} -->{nl}"
                  f'<link rel="preconnect" href="https://fonts.googleapis.com">{nl}'
                  f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>{nl}'
                  f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=JetBrains+Mono:wght@400;500&amp;family=Sora:wght@600;700;800&amp;display=swap">{nl}'
                  f'<link rel="stylesheet" href="/assets/css/site-header.css">{nl}'
                  f'<script src="/assets/js/site-nav.js" defer></script>{nl}'
                  f"<!-- /{MARK} -->{nl}")

    # 5) aplica (de trás para frente)
    removals = sorted(expand(html, s, e) for s, e in removals)
    merged = []
    for s, e in removals:
        if merged and s <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(e, merged[-1][1]))
        else:
            merged.append((s, e))
    # insere logo após "<body …>" e a quebra de linha que o segue
    m_nl = re.match(r"\r?\n", html[body.open_end:])
    body_at = body.open_end + (m_nl.end() if m_nl else 0)
    if not m_nl:
        body_block = nl + body_block
    if any(s < body_at < e for s, e in merged):
        return None, "trecho removido cruza o início do <body> — não tocado"
    edits = [(s, e, "") for s, e in merged] + [(body_at, body_at, body_block),
                                                (head_close, head_close, head_block)]
    new = html
    for s, e, txt in sorted(edits, key=lambda x: (x[0], x[1]), reverse=True):
        new = new[:s] + txt + new[e:]

    # 6) prova
    old_kept = "".join(html[a:b] for a, b in zip([0] + [e for _, e in merged], [s for s, _ in merged] + [len(html)]))
    new_kept, nb = re.subn(rf'(<body\b[^>]*>(?:\r?\n)?)(?:\r?\n)?<!-- {MARK} -->\r?\n<a class="sh-skip"[\s\S]*?<!-- /{MARK} -->\r?\n',
                           r"\1", new, count=1)
    new_kept, nh = re.subn(rf'<!-- {MARK} -->\r?\n<link rel="preconnect"[\s\S]*?<!-- /{MARK} -->\r?\n', "", new_kept, count=1)
    if (nb, nh) != (1, 1):
        return None, "PROVA FALHOU: blocos inseridos não localizados — não gravado"
    if new_kept != old_kept:
        return None, "PROVA FALHOU: algo fora dos trechos declarados mudou — não gravado"
    imgs_removed = sum(len(re.findall(r"<img\b", html[s:e])) for s, e in merged)
    if len(re.findall(r"<img\b", html)) - imgs_removed != len(re.findall(r"<img\b", new)):
        return None, "PROVA FALHOU: contagem de <img> — não gravado"
    report["idiomas"] = langs
    return new, report


# ── CLI ───────────────────────────────────────────────────────────────
def targets(only):
    if only:
        for rel in only:
            yield ROOT / rel
        return
    for p in sorted(ROOT.rglob("*.html")):
        if p.relative_to(ROOT).parts[0] in EXCLUDE_TOP:
            continue
        yield p


def main():
    args = sys.argv[1:]
    apply = "--apply" in args
    only = None
    diff_out = None
    if "--only" in args:
        only = [x.strip() for x in args[args.index("--only") + 1].split(",") if x.strip()]
    if "--only-file" in args:  # uma página por linha (listas longas não cabem na linha de comando)
        lst = Path(args[args.index("--only-file") + 1]).read_text(encoding="utf-8").splitlines()
        only = (only or []) + [x.strip().replace("\\", "/") for x in lst if x.strip()]
    if "--diff-out" in args:
        diff_out = Path(args[args.index("--diff-out") + 1])

    changes, skipped, diffs = [], [], []
    for p in targets(only):
        rel = p.relative_to(ROOT).as_posix()
        with open(p, encoding="utf-8", newline="") as fh:
            html = fh.read()
        if 'http-equiv="refresh"' in html:
            continue
        new, info = transform(rel, html)
        if new is None:
            skipped.append((rel, info))
            continue
        changes.append((p, rel, html, new, info))
        diffs.extend(difflib.unified_diff(html.splitlines(), new.splitlines(),
                                          f"a/{rel}", f"b/{rel}", n=2, lineterm=""))

    for _, rel, _, _, info in changes:
        print(f"\n● {rel}")
        print(f"   removido:    {', '.join(info['removido'])}")
        print(f"   descartados: {'; '.join(info['descartados']) or '—'}")
        print(f"   mantidos:    {'; '.join(info['mantidos']) or '—'}")
        if info["idiomas"]:
            print(f"   idiomas:     {info['idiomas']}")
    if skipped:
        print("\nNão tocados:")
        for rel, why in skipped:
            print(f"   ○ {rel}: {why}")
    print(f"\n{len(changes)} a alterar · {len(skipped)} não tocados")

    if diff_out:
        diff_out.write_text("\n".join(diffs) + "\n", encoding="utf-8")
        print(f"diff salvo em {diff_out}")

    if apply and changes:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        bdir = ROOT / "_backups"
        bdir.mkdir(exist_ok=True)
        zpath = bdir / f"menu-central-{stamp}.zip"
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
            for p, rel, html, _, _ in changes:
                z.writestr(rel, html.encode("utf-8"))
        for p, _, _, new, _ in changes:
            with open(p, "w", encoding="utf-8", newline="") as fh:
                fh.write(new)
        print(f"APLICADO. Backup: {zpath.relative_to(ROOT)}")
    elif not apply:
        print("(dry-run — nada gravado; use --apply)")


if __name__ == "__main__":
    main()
