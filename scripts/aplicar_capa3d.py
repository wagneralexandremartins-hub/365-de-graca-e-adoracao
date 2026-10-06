#!/usr/bin/env python3
"""
Aplica a capa 3D de livro (assets/css/capa-livro.css) nas páginas de abertura
dos livros (<bloco>/<livro>/index.html), nunca nos capítulos.

O que muda em cada página:
  <head>  → + UMA linha: <link rel="stylesheet" href="/assets/css/capa-livro.css">
            (logo antes de </head>)
  <body>  → + bloco marcado <!-- capa3d:v1 --> … <!-- /capa3d:v1 --> logo depois
            do fim do menu central (<!-- /site-nav:v1 --> do <body>), acima do
            topo que a página já tem.
Nada mais é tocado: nenhum texto, título, introdução ou URL.

Nome, grupo, capítulos (cânon), texto da lombada e tamanho do nome vêm da
tabela LIVROS abaixo, não do texto da página.

Antes de alterar, cada página é conferida. Ela NÃO é tocada (e é listada) se:
  - não tiver exatamente um <!-- /site-nav:v1 --> no <body> (modo "sem topo antigo");
  - o primeiro elemento depois do menu não for o topo esperado da tabela;
  - não houver <h1> depois do menu;
  - os capítulos encontrados no disco não baterem com o cânon
    (sem páginas de capítulo no disco = "não verificável", só avisado).
Depois de montar a versão nova, o script prova, byte a byte, que
  arquivo novo − bloco da capa − link do <head> == arquivo antigo.
Se a prova falhar, o arquivo não é gravado. Rodar de novo não duplica nada.

Uso:
  python scripts/aplicar_capa3d.py                     # dry-run (as 17 páginas)
  python scripts/aplicar_capa3d.py --only genesis,rute # restringe (pasta do livro)
  python scripts/aplicar_capa3d.py --diff-out f.diff
  python scripts/aplicar_capa3d.py --apply             # grava (com backup zip)
"""

import re
import sys
import zipfile
import difflib
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
MARK = "capa3d:v1"
CSS_LINK = '<link rel="stylesheet" href="/assets/css/capa-livro.css">'
GRUPOS = {"at": "Antigo Testamento", "nt": "Novo Testamento", "deutero": "Deuterocanônico"}

# pasta, nome, grupo, capítulos (cânon), lombada, --capa-nome (None = padrão 15cqi), topo esperado
LIVROS = [
    ("02-pentateuco/genesis",      "Gênesis",      "at", 50, "Gênesis",      None,    "main.container"),
    ("02-pentateuco/exodo",        "Êxodo",        "at", 40, "Êxodo",        None,    "div.exodus-index"),
    ("02-pentateuco/levitico",     "Levítico",     "at", 27, "Levítico",     None,    "div.container"),
    ("02-pentateuco/numeros",      "Números",      "at", 36, "Números",      None,    "div.container"),
    ("02-pentateuco/deuteronomio", "Deuteronômio", "at", 34, "Deuteronômio", "13cqi", "div.container"),
    ("03-historicos/josue",        "Josué",        "at", 24, "Josué",        None,    "div.hero-josue"),
    ("03-historicos/juizes",       "Juízes",       "at", 21, "Juízes",       None,    "main.wrap"),
    ("03-historicos/rute",         "Rute",         "at",  4, "Rute",         None,    "div.hero-rute"),
    ("03-historicos/1samuel",      "1 Samuel",     "at", 31, "1 Samuel",     None,    "main.wrap"),
    ("03-historicos/2samuel",      "2 Samuel",     "at", 24, "2 Samuel",     None,    "main.wrap"),
    ("03-historicos/1reis",        "1 Reis",       "at", 22, "1 Reis",       None,    "main.wrap"),
    ("03-historicos/2reis",        "2 Reis",       "at", 25, "2 Reis",       None,    "main.wrap"),
    ("03-historicos/1cronicas",    "1 Crônicas",   "at", 29, "1 Crônicas",   None,    "main.wrap"),
    ("03-historicos/2cronicas",    "2 Crônicas",   "at", 36, "2 Crônicas",   None,    "main.wrap"),
    ("03-historicos/esdras",       "Esdras",       "at", 10, "Esdras",       None,    "main.wrap"),
    ("03-historicos/neemias",      "Neemias",      "at", 13, "Neemias",      None,    "main.wrap"),
    ("03-historicos/ester",        "Ester",        "at", 10, "Ester",        None,    "main.wrap"),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def bloco(livro, nl):
    _, nome, grupo, caps, lombada, tam, _ = livro
    g = GRUPOS[grupo]
    st = f' style="--capa-nome:{tam}"' if tam else ""
    linhas = [
        f"<!-- {MARK} -->",
        f'<div class="capa3d-faixa" data-grupo="{grupo}"{st}>',
        f'  <div class="capa3d-cena" role="img" aria-label="Capa do livro {esc(nome)} — {g}, {caps} capítulos">',
        '    <div class="capa3d-livro" aria-hidden="true">',
        '      <div class="capa3d-face capa3d-verso"></div>',
        '      <div class="capa3d-face capa3d-topo"></div>',
        '      <div class="capa3d-face capa3d-paginas"></div>',
        f'      <div class="capa3d-face capa3d-lombada"><span>{esc(lombada)}</span></div>',
        '      <div class="capa3d-face capa3d-frente">',
        f'        <span class="capa3d-grupo">{g}</span>',
        '        <span class="capa3d-titulo">',
        f'          <span class="capa3d-nome">{esc(nome)}</span>',
        '          <span class="capa3d-filete"></span>',
        f'          <span class="capa3d-caps">{caps} capítulos</span>',
        '        </span>',
        '        <span class="capa3d-marca">365 Graça &amp; Adoração</span>',
        '      </div>',
        '    </div>',
        '    <div class="capa3d-sombra"></div>',
        '  </div>',
        '</div>',
        f"<!-- /{MARK} -->",
    ]
    return nl.join(linhas) + nl


def capitulos_no_disco(pasta):
    """Números de capítulo distintos (capitulo-XX.html, capitulo-XX/, cap-XX.html), sem en/ e es/."""
    nums = set()
    for p in pasta.rglob("*"):
        partes = p.relative_to(pasta).parts
        if partes and partes[0] in ("en", "es"):
            continue
        m = re.fullmatch(r"(?:capitulo|cap)[-_]?(\d+)(?:\.html)?", p.name, re.I)
        if m and (p.is_dir() or p.suffix.lower() == ".html"):
            nums.add(int(m.group(1)))
    return nums


def transform(livro, html):
    pasta, nome, _, caps, _, _, topo = livro
    if f"<!-- {MARK} -->" in html:
        if CSS_LINK not in html:
            return None, "capa já aplicada, mas sem o link do CSS no <head> — conferir à mão"
        return None, "já aplicada (nada a fazer)"
    nl = "\r\n" if "\r\n" in html else "\n"
    if html.count("\r\n") and html.replace("\r\n", "").count("\n"):
        return None, "quebras de linha mistas (CRLF e LF)"
    hb = html.lower().find("</head>")
    bi = html.lower().find("<body")
    if hb < 0 or bi < 0 or hb > bi or html.lower().count("</head>") != 1:
        return None, "estrutura <head>/<body> inesperada"
    marcas = [m.end() for m in re.finditer(r"<!-- /site-nav:v1 -->", html) if m.start() > bi]
    if len(marcas) != 1:
        return None, f'modo "sem topo antigo": {len(marcas)} fim(ns) de menu no <body> (esperado 1)'
    ins = marcas[0]
    if not html.startswith(nl, ins):
        return None, "fim do menu não é seguido de quebra de linha"
    ins += len(nl)
    m = re.search(r"<(\w+)([^>]*)>", html[ins:])
    achado = "—"
    if m:
        c = re.search(r'class="([^"]*)"', m.group(2))
        achado = m.group(1).lower() + ("." + c.group(1).split()[0] if c and c.group(1).split() else "")
    if achado != topo:
        return None, f"topo diferente do esperado: achado <{achado}>, esperado <{topo}>"
    if not re.search(r"<h1[\s>]", html[ins:], re.I):
        return None, "sem <h1> depois do menu"
    if CSS_LINK in html:
        return None, "link do CSS da capa já está no <head> sem o bloco — conferir à mão"

    # head: uma linha nova logo antes de </head>; se </head> não começar a linha, quebra antes
    ini_linha = html.rfind(nl, 0, hb) + len(nl)
    if html[ini_linha:hb].strip() == "":
        head_ins, head_txt = ini_linha, CSS_LINK + nl
    else:
        head_ins, head_txt = hb, nl + CSS_LINK + nl
    body_txt = bloco(livro, nl)

    new = html[:head_ins] + head_txt + html[head_ins:ins] + body_txt + html[ins:]

    # prova: retirar exatamente os dois trechos inseridos devolve o original, byte a byte
    a = head_ins
    b = ins + len(head_txt)
    volta = new[:a] + new[a + len(head_txt):b] + new[b + len(body_txt):]
    if volta.encode("utf-8") != html.encode("utf-8"):
        return None, "PROVA FALHOU (não gravado)"
    if new.count(f"<!-- {MARK} -->") != 1 or new.count(CSS_LINK) != 1:
        return None, "PROVA FALHOU: bloco ou link duplicado"

    nums = capitulos_no_disco(ROOT / pasta)
    if not nums:
        cap_info = f"cânon {caps} · disco: sem páginas de capítulo (não verificável)"
    elif len(nums) != caps or max(nums) != caps:
        return None, f"capítulos não batem: cânon {caps}, disco {len(nums)} (maior nº {max(nums)})"
    else:
        cap_info = f"cânon {caps} · disco {len(nums)} ✓"
    info = dict(topo=achado, caps=cap_info, crlf="CRLF" if nl == "\r\n" else "LF",
                head="nova linha antes de </head>" if head_txt == CSS_LINK + nl else "</head> na mesma linha: link com quebra antes")
    return new, info


def main():
    args = sys.argv[1:]
    apply = "--apply" in args
    only = None
    diff_out = None
    if "--only" in args:
        only = [x.strip().strip("/") for x in args[args.index("--only") + 1].split(",") if x.strip()]
    if "--diff-out" in args:
        diff_out = Path(args[args.index("--diff-out") + 1])

    livros = LIVROS
    if only:
        livros = [l for l in LIVROS if l[0] in only or l[0].split("/")[-1] in only]
        faltam = [o for o in only if not any(o in (l[0], l[0].split("/")[-1]) for l in LIVROS)]
        if faltam:
            print(f"Fora da tabela (ignorados): {', '.join(faltam)}")

    changes, skipped, diffs = [], [], []
    for livro in livros:
        rel = f"{livro[0]}/index.html"
        p = ROOT / rel
        if not p.exists():
            skipped.append((rel, "arquivo não existe"))
            continue
        raw = p.read_bytes()
        html = raw.decode("utf-8")
        if html.encode("utf-8") != raw:
            skipped.append((rel, "não é UTF-8 reversível"))
            continue
        new, info = transform(livro, html)
        if new is None:
            skipped.append((rel, info))
            continue
        changes.append((p, rel, html, new, info, livro))
        diffs.extend(difflib.unified_diff(html.splitlines(), new.splitlines(),
                                          f"a/{rel}", f"b/{rel}", n=2, lineterm=""))

    for _, rel, _, _, info, livro in changes:
        print(f"● {rel}  —  {livro[1]} ({GRUPOS[livro[2]]})")
        print(f"   topo: <{info['topo']}> · {info['caps']} · {info['crlf']} · head: {info['head']}")
    if skipped:
        print("\nNão tocadas:")
        for rel, why in skipped:
            print(f"   ○ {rel}: {why}")
    print(f"\n{len(changes)} a alterar · {len(skipped)} não tocadas")

    if diff_out:
        diff_out.write_text("\n".join(diffs) + "\n", encoding="utf-8")
        print(f"diff salvo em {diff_out}")

    if apply and changes:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        bdir = ROOT / "_backups"
        bdir.mkdir(exist_ok=True)
        zpath = bdir / f"capa3d-{stamp}.zip"
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
            for p, rel, html, _, _, _ in changes:
                z.writestr(rel, html.encode("utf-8"))
        for p, _, _, new, _, _ in changes:
            p.write_bytes(new.encode("utf-8"))
        print(f"APLICADO. Backup: {zpath.relative_to(ROOT).as_posix()}")
    elif not apply:
        print("(dry-run — nada gravado; use --apply)")


if __name__ == "__main__":
    main()
