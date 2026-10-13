"""Lote 1 do padrão EN/ES do NT: coluna de leitura das cartas e do Apocalipse em inglês e espanhol.

O que muda: só assets/css/bloco.css, com um bloco de regras acrescentado NO FIM do arquivo
(nenhuma linha existente é alterada). Nenhuma página HTML é editada.

Por quê: em PT, as 143 páginas de capítulo das cartas e do Apocalipse (estrutura .wrap +
.chapter-hero + .versiculo-bloco) recebem o visual de um <style> escrito dentro de cada página.
Os equivalentes en/<livro>-N/ e es/<libro>-N/ não têm esse bloco e aparecem sem estilo.
As regras abaixo repetem as declarações desse <style> do PT (sem a parte .brand do cabeçalho
antigo, que sai no lote do menu central).

Escopo: :root:is([lang|="en"], [lang|="es"]) body.bloco-08:has(.chapter-hero):has(.versiculo-bloco)
  • só páginas em inglês ou espanhol — nenhuma página em português pode casar;
  • só capítulos com .chapter-hero e .versiculo-bloco — ficam de fora os Evangelhos e Atos
    (.chapter-main, já tratados no PR #4) e Atos 26 (CSS próprio de página inteira, decisão pendente).

Decisão do Wagner (13/10/2026): ordem dos lotes aprovada; executar só o lote 1, em simulação,
com a prova de que as páginas PT não mudam, e aguardar aprovação antes de aplicar.

Uso:
  python scripts/css_cartas_en_es.py                      # simulação (não grava nada)
  python scripts/css_cartas_en_es.py --sim-out ARQ.css    # simulação + cópia do CSS novo fora do repo
  python scripts/css_cartas_en_es.py --apply              # grava bloco.css, com backup zip em _backups/

Prova: novo == antigo + bloco (o antigo é prefixo exato do novo); o bloco só usa CRLF, como o
arquivo; todo seletor do bloco começa pelo escopo; varredura de todas as páginas que carregam
bloco.css mostra quais casam com o escopo (esperado: 143 EN + 143 ES, 0 PT).
"""
import datetime, os, re, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = os.path.join(ROOT, "assets", "css", "bloco.css")
MARCA = "/* cartas-en-es:v1 */"
ESCOPO = ':root:is([lang|="en"], [lang|="es"]) body.bloco-08:has(.chapter-hero):has(.versiculo-bloco)'

REGRAS = [
    (".section-block", "background: var(--panel2,#1a1a2e); border-radius:12px; padding:1.5rem; margin:1.5rem 0;"),
    (".section-block h2", "color: var(--accent,#0ea5e9); margin-bottom:1rem; font-size:1.2rem;"),
    (".versiculo-bloco", "border-left: 3px solid var(--accent,#0ea5e9); padding: 1rem 1.2rem; margin:1rem 0; background: rgba(255,255,255,0.03); border-radius:0 8px 8px 0;"),
    (".ref-v", "font-size:0.8rem; color: var(--accent,#0ea5e9); font-weight:700; margin-bottom:0.4rem; text-transform:uppercase; letter-spacing:0.05em;"),
    (".texto-v", "font-style:italic; color:#e2e8f0; margin-bottom:0.6rem; line-height:1.7;"),
    (".analise-v", "color:#94a3b8; font-size:0.92rem; line-height:1.7;"),
    (".chapter-hero", "text-align:center; padding:3rem 1rem 2rem; background:linear-gradient(135deg,rgba(14,165,233,0.15),rgba(99,102,241,0.1));"),
    (".chapter-number", "font-size:0.85rem; color:var(--accent,#0ea5e9); font-weight:700; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.5rem;"),
    (".chapter-subtitle", "color:#94a3b8; font-style:italic; margin-top:0.5rem;"),
    (".chapter-ref", "color:var(--accent,#0ea5e9); font-size:0.85rem;"),
    (".chapter-nav", "display:flex; justify-content:space-between; padding:1.5rem; gap:1rem; flex-wrap:wrap;"),
    (".chapter-nav a", "color:var(--accent,#0ea5e9); text-decoration:none; padding:0.5rem 1rem; border:1px solid var(--accent,#0ea5e9); border-radius:6px;"),
    (".breadcrumb", "padding:0.75rem 1.5rem; font-size:0.85rem; color:#64748b;"),
    (".breadcrumb a", "color:var(--accent,#0ea5e9); text-decoration:none;"),
    (".wrap", "max-width:860px; margin:0 auto; padding:0 1.5rem 3rem;"),
]

CABECALHO = [
    "",
    MARCA,
    "/* ─── Cartas e Apocalipse em EN/ES (13/10/2026) ───",
    "   Em PT estas regras vêm de um <style> dentro de cada uma das 143 páginas de capítulo",
    "   das cartas e do Apocalipse; os equivalentes en/ e es/ não têm esse bloco.",
    "   Escopo: só inglês/espanhol e só páginas com .chapter-hero e .versiculo-bloco",
    "   (Evangelhos/Atos usam .chapter-main, acima; Atos 26 tem CSS próprio e fica fora).",
    "   Gerado por scripts/css_cartas_en_es.py. */",
]


def bloco():
    linhas = list(CABECALHO)
    for sel, decl in REGRAS:
        linhas.append(f"{ESCOPO} {sel} {{ {decl} }}")
    return ("\r\n".join(linhas) + "\r\n").encode("utf-8")


RX_CLASSE = lambda c: re.compile(rb'class="[^"]*\b' + re.escape(c.encode()) + rb'\b')
RX_BLOCO_CSS = re.compile(rb'<link[^>]+href="[^"]*/assets/css/bloco\.css"')
RX_LANG = re.compile(rb'<html[^>]*\blang="([^"]*)"', re.I)
RX_BODY = re.compile(rb"<body([^>]*)>", re.I)
TEM_HERO, TEM_VERS = RX_CLASSE("chapter-hero"), RX_CLASSE("versiculo-bloco")


def varredura():
    """Todas as páginas que carregam bloco.css, por idioma, e quais casam com o escopo."""
    por_lang, casam, sem_lang = {}, [], []
    for d, ds, fs in os.walk(ROOT):
        ds[:] = [x for x in ds if x not in (".git", "_backups", "node_modules", ".claude")]
        for f in fs:
            if not f.endswith(".html"):
                continue
            p = os.path.join(d, f)
            b = open(p, "rb").read()
            if not RX_BLOCO_CSS.search(b):
                continue
            rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
            m = RX_LANG.search(b)
            lang = m.group(1).decode().lower() if m else ""
            grupo = "pt" if lang.startswith("pt") else "en" if lang.startswith("en") else "es" if lang.startswith("es") else (lang or "(sem lang)")
            por_lang[grupo] = por_lang.get(grupo, 0) + 1
            if not lang:
                sem_lang.append(rel)
            body = RX_BODY.search(b)
            bloco08 = bool(body and re.search(rb'class="[^"]*\bbloco-08\b', body.group(1)))
            if grupo in ("en", "es") and bloco08 and TEM_HERO.search(b) and TEM_VERS.search(b):
                casam.append((grupo, rel))
            # páginas PT/sem lang nunca casam (o escopo exige lang en/es); registramos as que teriam a estrutura
    return por_lang, casam, sem_lang


def main():
    antigo = open(CSS, "rb").read()
    if MARCA.encode() in antigo:
        print("bloco.css já tem o bloco (cartas-en-es:v1): 0 mudanças.")
        return 0
    novo = antigo + bloco()
    add = novo[len(antigo):]
    seletores = re.findall(rb"([^{}]+)\{", re.sub(rb"/\*.*?\*/", b"", add, flags=re.S))
    provas = {
        "antigo é prefixo exato do novo": novo[: len(antigo)] == antigo,
        "antigo termina em CRLF": antigo.endswith(b"\r\n"),
        "bloco só usa CRLF": add.count(b"\n") == add.count(b"\r\n"),
        "arquivo inteiro segue só CRLF": novo.count(b"\n") == novo.count(b"\r\n"),
        f"{len(REGRAS)} regras, todas com o escopo": len(seletores) == len(REGRAS)
        and all(s.strip().startswith(ESCOPO.encode()) for s in seletores),
    }
    print(f"bloco.css: {len(antigo)} -> {len(novo)} bytes (+{len(add)}); linhas {antigo.count(b'\n')} -> {novo.count(b'\n')} (+{add.count(b'\n')})")
    print("\nBloco acrescentado no fim:\n" + add.decode("utf-8"))
    por_lang, casam, sem_lang = varredura()
    total = sum(por_lang.values())
    print(f"Páginas que carregam bloco.css: {total} — " + ", ".join(f"{k}: {v}" for k, v in sorted(por_lang.items())))
    if sem_lang:
        print(f"  sem atributo lang (não casam com [lang|=…]): {len(sem_lang)} — ex.: {sem_lang[:3]}")
    n_en = sum(1 for g, _ in casam if g == "en"); n_es = sum(1 for g, _ in casam if g == "es")
    print(f"Casam com o escopo: {len(casam)} (EN {n_en}, ES {n_es}); PT: 0 por construção (o escopo exige lang en/es)")
    provas["casam 143 EN + 143 ES"] = (n_en, n_es) == (143, 143)
    provas["nenhuma página PT/sem lang casa"] = all(g in ("en", "es") for g, _ in casam)
    print("\nProvas:")
    for k, ok in provas.items():
        print(f"  [{'ok' if ok else 'FALHOU'}] {k}")
    if not all(provas.values()):
        print("Prova falhou: nada gravado.")
        return 1
    if "--sim-out" in sys.argv:
        dest = sys.argv[sys.argv.index("--sim-out") + 1]
        if os.path.abspath(dest).startswith(ROOT):
            print("--sim-out precisa ficar fora do repositório"); return 1
        open(dest, "wb").write(novo); print(f"\nCSS simulado gravado em {dest} (fora do repositório)")
    if "--apply" not in sys.argv:
        print("\nSimulação: nada foi gravado no repositório. Use --apply depois do OK do Wagner.")
        return 0
    os.makedirs(os.path.join(ROOT, "_backups"), exist_ok=True)
    zp = os.path.join(ROOT, "_backups", "css-cartas-en-es-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".zip")
    with zipfile.ZipFile(zp, "x", zipfile.ZIP_DEFLATED) as z:
        z.writestr("assets/css/bloco.css", antigo)
    open(CSS, "wb").write(novo)
    assert open(CSS, "rb").read() == novo and zipfile.ZipFile(zp).read("assets/css/bloco.css") == antigo
    print(f"\nGravado assets/css/bloco.css; backup em {os.path.relpath(zp, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
