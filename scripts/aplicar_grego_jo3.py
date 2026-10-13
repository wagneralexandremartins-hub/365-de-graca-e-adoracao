"""Piloto do grego koiné em João 3 (PT, EN e ES): camada nova, recolhida, abaixo de cada citação.

O que muda (só acréscimos; nenhum texto bíblico ou de estudo existente é alterado):
  • 08-novo-testamento/joao/capitulos/capitulo-03.html, en/john-3/index.html, es/juan-3/index.html
      – no <head>, antes de </head>: fonte Gentium Plus (Google Fonts) + /assets/css/grego.css;
      – em cada um dos 4 blocos de versículo (3:1-3, 3:5-8, 3:16, 3:17-18), logo depois do
        </blockquote>: um <details class="grego-tr"> fechado, com o grego dos versículos da faixa
        e o crédito da licença. Tudo entre <!-- grego-tr:v1 --> e <!-- /grego-tr:v1 -->.
  • assets/css/grego.css (arquivo novo).

Texto grego: Textus Receptus 1894 Scrivener, edição digital Door43 (STR/el-x-koine_trs),
CC BY-SA 4.0 — https://git.door43.org/STR/el-x-koine_trs — arquivo 44-JHN.usfm do commit
4107626cbc0bd577a9024e66ff4614342e6b4238 (SHA-256 f93ebbc0404ed35effb898940ed179d79b10d7b24395179ec495231deb047cf9).
Adaptação: só as palavras e a pontuação da fonte (sem lema, Strong e morfologia), Unicode NFC.

Decisões do Wagner (13/10/2026): fonte Door43 aprovada; proposta A (grego recolhido em PT, EN e ES,
fonte Gentium Plus); rótulos aprovados; textos do crédito em PT, EN e ES aprovados como estão,
em cada um dos 4 blocos (CREDITO_APROVADO = True).

Uso:
  python scripts/aplicar_grego_jo3.py                     # simulação (não grava nada)
  python scripts/aplicar_grego_jo3.py --sim-dir PASTA     # simulação + cópia dos arquivos novos fora do repo
  python scripts/aplicar_grego_jo3.py --apply             # grava, com backup zip em _backups/

Prova, por página: novo menos os trechos inseridos == antigo, byte a byte; os trechos só usam CRLF;
as 4 citações (<blockquote class="verse-text">) e o resto da página ficam idênticos; contagem de <img> igual.
"""
import datetime, os, re, sys, unicodedata, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDITO_APROVADO = True  # crédito aprovado pelo Wagner em 13/10/2026 (PT, EN e ES, em cada bloco)
MARCA_INI, MARCA_FIM = "<!-- grego-tr:v1 -->", "<!-- /grego-tr:v1 -->"

# Door43 STR/el-x-koine_trs, 44-JHN.usfm (commit 4107626c), João 3 — só os versículos citados nas páginas
GREGO = {
    1: "Ἦν δὲ ἄνθρωπος ἐκ τῶν Φαρισαίων, Νικόδημος ὄνομα αὐτῷ, ἄρχων τῶν Ἰουδαίων·",
    2: "οὗτος ἦλθε πρὸς τὸν Ἰησοῦν νυκτός, καὶ εἶπεν αὐτῷ, Ῥαββί, οἴδαμεν ὅτι ἀπὸ Θεοῦ ἐλήλυθας διδάσκαλος· οὐδεὶς γὰρ ταῦτα τὰ σημεῖα δύναται ποιεῖν ἃ σὺ ποιεῖς, ἐὰν μὴ ᾖ ὁ Θεὸς μετ’ αὐτοῦ.",
    3: "Ἀπεκρίθη ὁ Ἰησοῦς καὶ εἶπεν αὐτῷ, Ἀμὴν ἀμὴν λέγω σοι, ἐὰν μή τις γεννηθῇ ἄνωθεν, οὐ δύναται ἰδεῖν τὴν βασιλείαν τοῦ Θεοῦ.",
    5: "ἀπεκρίθη ὁ Ἰησοῦς, Ἀμὴν ἀμὴν λέγω σοι, ἐὰν μή τις γεννηθῇ ἐξ ὕδατος καὶ Πνεύματος, οὐ δύναται εἰσελθεῖν εἰς τὴν βασιλείαν τοῦ Θεοῦ.",
    6: "τὸ γεγεννημένον ἐκ τῆς σαρκὸς σάρξ ἐστι· καὶ τὸ γεγεννημένον ἐκ τοῦ πνεύματος πνεῦμά ἐστι.",
    7: "μὴ θαυμάσῃς ὅτι εἶπόν σοι, Δεῖ ὑμᾶς γεννηθῆναι ἄνωθεν.",
    8: "τὸ πνεῦμα ὅπου θέλει πνεῖ, καὶ τὴν φωνὴν αὐτοῦ ἀκούεις, ἀλλ’ οὐκ οἶδας πόθεν ἔρχεται καὶ ποῦ ὑπάγει· οὕτως ἐστὶ πᾶς ὁ γεγεννημένος ἐκ τοῦ πνεύματος.",
    16: "Οὕτω γὰρ ἠγάπησεν ὁ Θεὸς τὸν κόσμον, ὥστε τὸν υἱὸν αὐτοῦ τὸν μονογενῆ ἔδωκεν, ἵνα πᾶς ὁ πιστεύων εἰς αὐτὸν μὴ ἀπόληται, ἀλλ’ ἔχῃ ζωὴν αἰώνιον.",
    17: "οὐ γὰρ ἀπέστειλεν ὁ Θεὸς τὸν υἱὸν αὐτοῦ εἰς τὸν κόσμον ἵνα κρίνῃ τὸν κόσμον, ἀλλ’ ἵνα σωθῇ ὁ κόσμος δι’ αὐτοῦ.",
    18: "ὁ πιστεύων εἰς αὐτὸν οὐ κρίνεται· ὁ δὲ μὴ πιστεύων ἤδη κέκριται, ὅτι μὴ πεπίστευκεν εἰς τὸ ὄνομα τοῦ μονογενοῦς υἱοῦ τοῦ Θεοῦ.",
}
FAIXAS = [(1, 3), (5, 8), (16, 16), (17, 18)]

FONTE_URL = "https://git.door43.org/STR/el-x-koine_trs"
PAGINAS = {
    "pt": dict(arq="08-novo-testamento/joao/capitulos/capitulo-03.html", livro="João",
               rotulo="Ver o texto grego (koiné)",
               credito=(f'Texto grego: <a href="{FONTE_URL}" rel="noopener">Textus Receptus 1894 Scrivener</a>, '
                        'Door43 World Missions Community, com Scriptorium e Dr. Maurice A. Robinson, sob a licença '
                        '<a href="https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br" rel="license noopener">CC BY-SA 4.0</a>. '
                        'Adaptado: só o texto, sem as marcações de morfologia, Strong e lema. Esta camada grega segue a mesma licença.')),
    "en": dict(arq="en/john-3/index.html", livro="John",
               rotulo="View the Greek text (Koine)",
               credito=(f'Greek text: <a href="{FONTE_URL}" rel="noopener">Textus Receptus 1894 Scrivener</a>, '
                        'Door43 World Missions Community, with Scriptorium and Dr. Maurice A. Robinson, under the '
                        '<a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en" rel="license noopener">CC BY-SA 4.0</a> license. '
                        "Adapted: text only, without the morphology, Strong's and lemma tags. This Greek layer is shared under the same license.")),
    "es": dict(arq="es/juan-3/index.html", livro="Juan",
               rotulo="Ver el texto griego (koiné)",
               credito=(f'Texto griego: <a href="{FONTE_URL}" rel="noopener">Textus Receptus 1894 Scrivener</a>, '
                        'Door43 World Missions Community, con Scriptorium y el Dr. Maurice A. Robinson, bajo la licencia '
                        '<a href="https://creativecommons.org/licenses/by-sa/4.0/deed.es" rel="license noopener">CC BY-SA 4.0</a>. '
                        'Adaptado: solo el texto, sin las marcas de morfología, Strong y lema. Esta capa griega se comparte bajo la misma licencia.')),
}

HEAD = [
    MARCA_INI,
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gentium+Plus&amp;display=swap">',
    '<link rel="stylesheet" href="/assets/css/grego.css">',
    MARCA_FIM,
]

CSS_GREGO = """/* Camada do grego koiné (piloto: João 3 em PT, EN e ES) — inserida por scripts/aplicar_grego_jo3.py.
   Bloco recolhido abaixo da citação; sem cores claras próprias (o modo claro inverte a página inteira). */
.grego-tr { margin: 0.2rem 0 0.9rem; border: 1px solid var(--line, rgba(255,255,255,0.08)); border-radius: 8px; background: rgba(255,255,255,0.02); }
.grego-tr > summary { cursor: pointer; padding: 0.5rem 0.9rem; font-family: var(--font-ui, system-ui, sans-serif); font-size: 0.85rem; font-weight: 600; color: var(--accent, #0ea5e9); }
.grego-tr > summary:focus-visible { outline: 2px solid var(--accent, #0ea5e9); outline-offset: 2px; border-radius: 6px; }
.grego-tr[open] > summary { border-bottom: 1px solid var(--line, rgba(255,255,255,0.08)); }
.grego-texto { padding: 0.7rem 1rem 0.3rem; font-family: "Gentium Plus", "Noto Serif", "Times New Roman", serif; font-size: 1.18rem; font-style: normal; line-height: 1.8; color: #e2e8f0; }
.grego-texto p { margin: 0 0 0.5rem; }
.grego-texto sup { font-family: var(--font-ui, system-ui, sans-serif); font-size: 0.65em; font-weight: 700; color: var(--accent, #0ea5e9); margin-right: 0.3em; }
.grego-credito { margin: 0; padding: 0 1rem 0.75rem; font-family: var(--font-ui, system-ui, sans-serif); font-size: 0.72rem; line-height: 1.5; color: #64748b; }
.grego-credito a { color: inherit; text-decoration: underline; }
"""


def bloco_versos(lang, ini, fim, nl):
    p = PAGINAS[lang]
    linhas = ["  " + MARCA_INI, '  <details class="grego-tr">', f"    <summary>{p['rotulo']}</summary>",
              '    <div class="grego-texto" lang="grc">']
    for v in range(ini, fim + 1):
        linhas.append(f"      <p><sup>{v}</sup>{GREGO[v]}</p>")
    linhas += ["    </div>", f'    <p class="grego-credito">{p["credito"]}</p>', "  </details>", "  " + MARCA_FIM]
    return (nl.join(linhas) + nl).encode("utf-8")


def processa(lang):
    p = PAGINAS[lang]
    caminho = os.path.join(ROOT, p["arq"])
    antigo = open(caminho, "rb").read()
    if MARCA_INI.encode() in antigo:
        return antigo, antigo, [], "já tem a camada grega"
    nl = b"\r\n" if antigo.count(b"\r\n") == antigo.count(b"\n") else (b"\n" if b"\r\n" not in antigo else None)
    if nl is None:
        return antigo, None, [], "quebra de linha mista"
    nl_s = nl.decode()
    rx = re.compile(rb'<div class="verse-ref">' + re.escape(p["livro"].encode()) +
                    rb' 3:(\d+)(?:-(\d+))?</div>' + re.escape(nl) + rb'  <blockquote class="verse-text">.*?</blockquote>' + re.escape(nl))
    achados = list(rx.finditer(antigo))
    faixas = [(int(m.group(1)), int(m.group(2) or m.group(1))) for m in achados]
    if faixas != FAIXAS:
        return antigo, None, [], f"faixas diferentes do esperado: {faixas}"
    if antigo.count(b"</head>") != 1 or antigo.count(nl + b"</head>" + nl) != 1:
        return antigo, None, [], "</head> fora do padrão"
    insercoes = [(antigo.index(nl + b"</head>") + len(nl), (nl_s.join(HEAD) + nl_s).encode("utf-8"))]
    for m, (a, b) in zip(achados, faixas):
        insercoes.append((m.end(), bloco_versos(lang, a, b, nl_s)))
    insercoes.sort()
    novo, pos = b"", 0
    for i, txt in insercoes:
        novo += antigo[pos:i] + txt
        pos = i
    novo += antigo[pos:]
    return antigo, novo, insercoes, None


def prova(antigo, novo, insercoes):
    volta, pos, desloc = b"", 0, 0
    for i, txt in insercoes:
        j = i + desloc
        assert novo[j:j + len(txt)] == txt
        volta += novo[pos:j]
        pos = j + len(txt)
        desloc += len(txt)
    volta += novo[pos:]
    trechos = b"".join(t for _, t in insercoes)
    citacoes = lambda b: re.findall(rb'<blockquote class="verse-text">.*?</blockquote>', b)
    return {
        "novo menos inserções == antigo (byte a byte)": volta == antigo,
        "trechos só com CRLF": trechos.count(b"\n") == trechos.count(b"\r\n"),
        "arquivo segue só CRLF": novo.count(b"\n") == novo.count(b"\r\n"),
        "4 citações idênticas": citacoes(antigo) == citacoes(novo) and len(citacoes(antigo)) == 4,
        "<img> igual": antigo.count(b"<img") == novo.count(b"<img"),
        "5 inserções (head + 4 blocos)": len(insercoes) == 5,
    }


def main():
    provas_dados = {
        "10 versículos, todos em NFC": len(GREGO) == 10 and all(unicodedata.normalize("NFC", t) == t for t in GREGO.values()),
        "faixas cobertas pelos dados": all(v in GREGO for a, b in FAIXAS for v in range(a, b + 1)),
        "sem &, < ou > no grego": not any(c in t for t in GREGO.values() for c in "&<>"),
    }
    resultados, ok_geral = {}, all(provas_dados.values())
    print("Dados do grego:")
    for k, ok in provas_dados.items():
        print(f"  [{'ok' if ok else 'FALHOU'}] {k}")
    for lang in PAGINAS:
        antigo, novo, ins, motivo = processa(lang)
        print(f"\n== {lang}: {PAGINAS[lang]['arq']}")
        if motivo:
            print(f"  pulada: {motivo}")
            ok_geral = ok_geral and motivo == "já tem a camada grega"
            continue
        pv = prova(antigo, novo, ins)
        print(f"  {len(antigo)} -> {len(novo)} bytes (+{len(novo) - len(antigo)}); linhas +{novo.count(b'\n') - antigo.count(b'\n')}")
        for k, ok in pv.items():
            print(f"  [{'ok' if ok else 'FALHOU'}] {k}")
        ok_geral = ok_geral and all(pv.values())
        resultados[lang] = (antigo, novo, ins)
    css_path = os.path.join(ROOT, "assets", "css", "grego.css")
    css_novo = CSS_GREGO.replace("\n", "\r\n").encode("utf-8")
    print(f"\nassets/css/grego.css: {'JÁ EXISTE (não sobrescreve)' if os.path.exists(css_path) else f'novo, {len(css_novo)} bytes, CRLF'}")
    if resultados:
        lang0 = next(iter(resultados))
        a, n, ins = resultados[lang0]
        print(f"\nExemplo de trecho inserido ({lang0}, bloco 3:16):\n" + ins[3][1].decode("utf-8"))
    if not ok_geral:
        print("Prova falhou: nada gravado.")
        return 1
    if "--sim-dir" in sys.argv:
        dest = os.path.abspath(sys.argv[sys.argv.index("--sim-dir") + 1])
        if dest.startswith(ROOT):
            print("--sim-dir precisa ficar fora do repositório"); return 1
        for lang, (a, n, ins) in resultados.items():
            alvo = os.path.join(dest, PAGINAS[lang]["arq"]); os.makedirs(os.path.dirname(alvo), exist_ok=True)
            open(alvo, "wb").write(n)
        os.makedirs(os.path.join(dest, "assets", "css"), exist_ok=True)
        open(os.path.join(dest, "assets", "css", "grego.css"), "wb").write(css_novo)
        print(f"\nArquivos simulados gravados em {dest} (fora do repositório)")
    if "--apply" not in sys.argv:
        print("\nSimulação: nada foi gravado no repositório.")
        return 0
    if not CREDITO_APROVADO:
        print("\n--apply recusado: o texto do crédito ainda não foi aprovado (CREDITO_APROVADO = False).")
        return 1
    if os.path.exists(css_path):
        print("assets/css/grego.css já existe: nada gravado."); return 1
    os.makedirs(os.path.join(ROOT, "_backups"), exist_ok=True)
    zp = os.path.join(ROOT, "_backups", "grego-jo3-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".zip")
    with zipfile.ZipFile(zp, "x", zipfile.ZIP_DEFLATED) as z:
        for lang, (a, n, ins) in resultados.items():
            z.writestr(PAGINAS[lang]["arq"], a)
    for lang, (a, n, ins) in resultados.items():
        open(os.path.join(ROOT, PAGINAS[lang]["arq"]), "wb").write(n)
    with open(css_path, "xb") as f:
        f.write(css_novo)
    z = zipfile.ZipFile(zp)
    for lang, (a, n, ins) in resultados.items():
        assert open(os.path.join(ROOT, PAGINAS[lang]["arq"]), "rb").read() == n and z.read(PAGINAS[lang]["arq"]) == a
    print(f"\nGravado: {len(resultados)} páginas + assets/css/grego.css; backup em {os.path.relpath(zp, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
