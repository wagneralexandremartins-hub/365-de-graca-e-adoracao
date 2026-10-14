"""Camada do grego koiné nos Evangelhos sinóticos (PT, EN e ES) — generalização do piloto de João 3.

O que muda (só acréscimos; nenhum texto bíblico ou de estudo existente é alterado), por livro (--livro):
  • nas páginas de capítulo PT, EN e ES que têm citações reais:
      – no <head>, antes de </head>: as mesmas 2 linhas do piloto (Gentium Plus + /assets/css/grego.css);
      – logo depois de cada </blockquote> de citação: um <details class="grego-tr"> fechado com o grego
        de TODOS os versículos da faixa do rótulo (mesmo quando a citação traz reticências) e o crédito;
        tudo entre <!-- grego-tr:v1 --> e <!-- /grego-tr:v1 -->, no formato exato do piloto.
  • assets/css/grego.css não muda (já existe desde o piloto).

Texto grego: scripts/dados/grego-tr-<livro>.json, gerado por scripts/extrair_grego_door43.py a partir do
Door43 STR/el-x-koine_trs (Scrivener 1894, CC BY-SA 4.0), commit 4107626c, conferido contra o byztxt.

Decisões do Wagner (14/10/2026): (a) páginas de modelo ("<Livro> N:1" = "Contexto e introdução ao
capítulo N" + "<Livro> N — Teologia Central"/"O Servo Sofredor"/"O Salvador Universal") ficam de fora;
(b) grego da faixa inteira do rótulo, mesmo com citação resumida; (c) um PR por Evangelho, começando
por Mateus. Rótulos e crédito: os aprovados no piloto (13/10/2026), importados de aplicar_grego_jo3.py.

Fora do padrão, sem palpite (página pulada e listada como "decisão pendente"): rótulo fora dos formatos
"<Livro> C:V" e "<Livro> C:V-W" do próprio capítulo, página mista (modelo + citação), faixas diferentes
entre PT, EN e ES, </head> fora do padrão, quebra de linha mista.

Uso:
  python scripts/aplicar_grego_evangelhos.py --livro mateus                   # simulação (não grava nada)
  python scripts/aplicar_grego_evangelhos.py --livro mateus --sim-dir PASTA   # + cópia das páginas simuladas fora do repo
  python scripts/aplicar_grego_evangelhos.py --livro mateus --apply           # grava, com backup zip em _backups/

Prova, por página: novo menos os trechos inseridos == antigo, byte a byte; trechos com a mesma quebra de
linha do arquivo; citações (<blockquote>) e <img> idênticas; 1 inserção no head + 1 por citação; o grego
lido de volta da página == JSON. Prova de formato: o mesmo gerador reproduz byte a byte os 4 blocos de
João 3 já publicados (PT, EN e ES).
"""
import datetime, json, os, re, sys, unicodedata, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import aplicar_grego_jo3 as piloto  # rótulos, crédito, HEAD e marcas aprovados no piloto

MARCA_INI, MARCA_FIM, HEAD, PAGINAS_PILOTO = piloto.MARCA_INI, piloto.MARCA_FIM, piloto.HEAD, piloto.PAGINAS
LANGS = ("pt", "en", "es")

LIVROS = {
    "mateus": dict(sigla="MAT", usfm="41-MAT.usfm", byz="MT.SCV", acf="mt", caps=28,
                   pt=("08-novo-testamento/mateus/capitulos/capitulo-{:02d}.html", "Mateus"),
                   en=("en/matthew-{}/index.html", "Matthew"), es=("es/mateo-{}/index.html", "Mateo")),
    "marcos": dict(sigla="MRK", usfm="42-MRK.usfm", byz="MR.SCV", acf="mc", caps=16,
                   pt=("08-novo-testamento/marcos/capitulos/capitulo-{:02d}.html", "Marcos"),
                   en=("en/mark-{}/index.html", "Mark"), es=("es/marcos-{}/index.html", "Marcos")),
    "lucas": dict(sigla="LUK", usfm="43-LUK.usfm", byz="LU.SCV", acf="lc", caps=24,
                  pt=("08-novo-testamento/lucas/capitulos/capitulo-{:02d}.html", "Lucas"),
                  en=("en/luke-{}/index.html", "Luke"), es=("es/lucas-{}/index.html", "Lucas")),
}

RX_REF = re.compile(rb'<div class="verse-ref">(.*?)</div>', re.S)
RX_MODELO_CIT = re.compile(r'^"(Contexto e introdução ao capítulo|Context and introduction to chapter|'
                           r'Contexto e introducción al capítulo) \d+"$', re.I)


def caminho_dados(livro):
    return os.path.join(ROOT, "scripts", "dados", f"grego-tr-{livro}.json")


def quebra(b):
    crlf, n = b.count(b"\r\n"), b.count(b"\n")
    return b"\r\n" if crlf == n else (b"\n" if crlf == 0 else None)


def varre_pagina(b, nome, cap):
    """Classifica a página. Devolve dict(tipo=alvo|modelo|pendente, motivo, citacoes=[(fim, ini, fim_v, rotulo)], fora=[...])."""
    nl = quebra(b)
    if nl is None:
        return dict(tipo="pendente", motivo="quebra de linha mista", citacoes=[], fora=[], modelo=[])
    citacoes, fora, modelo = [], [], []
    rx_cit = re.compile(re.escape(f"{nome} {cap}:".encode()) + rb"(\d+)(?:-(\d+))?$")
    rx_tema = re.compile(re.escape(f"{nome} {cap} — ".encode()) + rb".+$")
    for m in RX_REF.finditer(b):
        rot = m.group(1)
        bq = re.match(re.escape(nl) + rb'  <blockquote class="verse-text">([^\r\n]*?)</blockquote>' + re.escape(nl),
                      b[m.end():m.end() + 30000])
        rot_s = rot.decode("utf-8")
        if rx_tema.match(rot):
            modelo.append(rot_s); continue
        c = rx_cit.match(rot)
        if not c or not bq:
            fora.append(rot_s + ("" if bq else "  [citação fora do padrão do piloto]")); continue
        if RX_MODELO_CIT.match(bq.group(1).decode("utf-8")):
            modelo.append(rot_s + ' = "' + bq.group(1).decode("utf-8").strip('"') + '"'); continue
        a, z = int(c.group(1)), int(c.group(2) or c.group(1))
        if z < a:
            fora.append(rot_s + "  [intervalo invertido]"); continue
        citacoes.append((m.end() + bq.end(), a, z, rot_s))
    if fora:
        return dict(tipo="pendente", motivo="rótulo fora dos formatos", citacoes=citacoes, fora=fora, modelo=modelo)
    if modelo and citacoes:
        return dict(tipo="pendente", motivo="página mista (modelo + citação)", citacoes=citacoes, fora=fora, modelo=modelo)
    if modelo:
        return dict(tipo="modelo", motivo="página de modelo", citacoes=[], fora=[], modelo=modelo)
    if not citacoes:
        return dict(tipo="pendente", motivo="sem citações", citacoes=[], fora=[], modelo=[])
    if b.count(b"</head>") != 1 or b.count(nl + b"</head>" + nl) != 1:
        return dict(tipo="pendente", motivo="</head> fora do padrão", citacoes=citacoes, fora=[], modelo=[])
    return dict(tipo="alvo", motivo="", citacoes=citacoes, fora=[], modelo=[])


def bloco(lang, cap, ini, fim, versos, nl):
    """Mesmo formato de piloto.bloco_versos, com os versículos vindos do JSON."""
    p = PAGINAS_PILOTO[lang]
    linhas = ["  " + MARCA_INI, '  <details class="grego-tr">', f"    <summary>{p['rotulo']}</summary>",
              '    <div class="grego-texto" lang="grc">']
    for v in range(ini, fim + 1):
        linhas.append(f"      <p><sup>{v}</sup>{versos[f'{cap}:{v}']}</p>")
    linhas += ["    </div>", f'    <p class="grego-credito">{p["credito"]}</p>', "  </details>", "  " + MARCA_FIM]
    return (nl.join(linhas) + nl).encode("utf-8")


def prova_formato():
    """O gerador reproduz byte a byte os 4 blocos de João 3 já publicados nas 3 páginas do piloto."""
    versos = {f"3:{v}": t for v, t in piloto.GREGO.items()}
    for lang, p in PAGINAS_PILOTO.items():
        b = open(os.path.join(ROOT, p["arq"]), "rb").read()
        nl = quebra(b).decode()
        publicados = re.findall(rb"  " + re.escape(MARCA_INI.encode()) + rb"\r?\n  <details.*?" +
                                re.escape(MARCA_FIM.encode()) + rb"\r?\n", b, re.S)
        gerados = [bloco(lang, 3, a, z, versos, nl) for a, z in piloto.FAIXAS]
        if publicados != gerados:
            return False
    return True


def processa(rel, nome, cap, lang, versos):
    antigo = open(os.path.join(ROOT, rel), "rb").read()
    if MARCA_INI.encode() in antigo:
        return antigo, None, [], dict(tipo="feito", motivo="já tem a camada grega", citacoes=[], fora=[], modelo=[])
    info = varre_pagina(antigo, nome, cap)
    if info["tipo"] != "alvo":
        return antigo, None, [], info
    nl = quebra(antigo).decode()
    falta = [f"{cap}:{v}" for _, a, z, _ in info["citacoes"] for v in range(a, z + 1) if f"{cap}:{v}" not in versos]
    if falta:
        info.update(tipo="pendente", motivo=f"versículos ausentes no JSON: {falta}")
        return antigo, None, [], info
    insercoes = [(antigo.index(nl.encode() + b"</head>") + len(nl), (nl.join(HEAD) + nl).encode("utf-8"))]
    for fim, a, z, _ in info["citacoes"]:
        insercoes.append((fim, bloco(lang, cap, a, z, versos, nl)))
    insercoes.sort()
    novo, pos = b"", 0
    for i, txt in insercoes:
        novo += antigo[pos:i] + txt
        pos = i
    novo += antigo[pos:]
    return antigo, novo, insercoes, info


def prova(antigo, novo, insercoes, info, cap, versos):
    volta, pos, desloc = b"", 0, 0
    for i, txt in insercoes:
        j = i + desloc
        assert novo[j:j + len(txt)] == txt
        volta += novo[pos:j]
        pos = j + len(txt)
        desloc += len(txt)
    volta += novo[pos:]
    nl = quebra(antigo)
    trechos = b"".join(t for _, t in insercoes)
    citacoes = lambda b: re.findall(rb'<blockquote class="verse-text">.*?</blockquote>', b, re.S)
    lidos = re.findall(rb'<p><sup>(\d+)</sup>(.*?)</p>', novo)
    esperados = [(str(v).encode(), versos[f"{cap}:{v}"].encode("utf-8"))
                 for _, a, z, _ in info["citacoes"] for v in range(a, z + 1)]
    return {
        "novo menos inserções == antigo (byte a byte)": volta == antigo,
        "trechos com a quebra do arquivo": (trechos.count(b"\n") == trechos.count(b"\r\n")) if nl == b"\r\n" else (b"\r" not in trechos),
        "quebra do arquivo preservada": quebra(novo) == nl,
        "citações idênticas": citacoes(antigo) == citacoes(novo),
        "<img> igual": antigo.count(b"<img") == novo.count(b"<img"),
        f"{1 + len(info['citacoes'])} inserções (head + {len(info['citacoes'])} blocos)": len(insercoes) == 1 + len(info["citacoes"]),
        "grego lido da página == JSON": lidos == esperados,
        "</head> único e um bloco depois de cada </blockquote>": novo.count(b"</head>") == 1 and
            novo.count(b"</blockquote>" + nl + b"  " + MARCA_INI.encode()) == len(info["citacoes"]),
    }


def main():
    if "--livro" not in sys.argv or sys.argv[sys.argv.index("--livro") + 1] not in LIVROS:
        print("uso: --livro " + "|".join(LIVROS)); return 2
    livro = sys.argv[sys.argv.index("--livro") + 1]
    cfg = LIVROS[livro]
    dados = json.load(open(caminho_dados(livro), encoding="utf-8"))
    versos = dados["versiculos"]
    provas_dados = {
        f"JSON de {livro}: {len(versos)} versículos, todos em NFC": all(unicodedata.normalize("NFC", t) == t for t in versos.values()),
        "sem &, < ou > no grego": not any(c in t for t in versos.values() for c in "&<>"),
        "JSON aponta para o commit fixado do Door43": dados["fonte"]["commit"].startswith("4107626c"),
        "gerador reproduz byte a byte os blocos de João 3 publicados": prova_formato(),
        "assets/css/grego.css existe (não muda)": os.path.exists(os.path.join(ROOT, "assets", "css", "grego.css")),
    }
    ok_geral = all(provas_dados.values())
    print("Provas gerais:")
    for k, ok in provas_dados.items():
        print(f"  [{'ok' if ok else 'FALHOU'}] {k}")

    resultados, pulados, faixas_por_cap = {}, [], {}
    for lang in LANGS:
        tpl, nome = cfg[lang]
        for cap in range(1, cfg["caps"] + 1):
            rel = tpl.format(cap)
            antigo, novo, ins, info = processa(rel, nome, cap, lang, versos)
            faixas_por_cap.setdefault(cap, {})[lang] = [(a, z) for _, a, z, _ in info["citacoes"]] if info["tipo"] == "alvo" else info["tipo"]
            if info["tipo"] != "alvo":
                pulados.append((lang, cap, rel, info)); continue
            pv = prova(antigo, novo, ins, info, cap, versos)
            resultados[rel] = (lang, cap, antigo, novo, ins, info, pv)

    divergentes = [cap for cap, d in faixas_por_cap.items() if not (d["pt"] == d["en"] == d["es"])]
    for rel in [r for r, v in resultados.items() if v[1] in divergentes]:
        lang, cap, a, n, ins, info, pv = resultados.pop(rel)
        info.update(tipo="pendente", motivo=f"faixas diferentes entre idiomas: {faixas_por_cap[cap]}")
        pulados.append((lang, cap, rel, info))

    print(f"\n== Páginas que recebem o grego: {len(resultados)}")
    tot = 0
    for rel, (lang, cap, a, n, ins, info, pv) in resultados.items():
        tot += len(n) - len(a)
        ok = all(pv.values()); ok_geral = ok_geral and ok
        rot = ", ".join(f"{x}" if x == y else f"{x}-{y}" for _, x, y, _ in info["citacoes"])
        print(f"  [{'ok' if ok else 'FALHOU'}] {rel}: {len(info['citacoes'])} bloco{'s' if len(info['citacoes']) > 1 else ''} ({rot}); "
              f"{len(a)} -> {len(n)} B (+{len(n) - len(a)}); linhas +{n.count(b'\n') - a.count(b'\n')}")
        if not ok:
            for k, v in pv.items():
                if not v: print(f"        FALHOU: {k}")
    print(f"  total: +{tot} B (bytes da cópia local; no git/no ar, em LF, 1 B a menos por linha inserida)")
    nomes_provas = next(iter(resultados.values()))[6].keys() if resultados else []
    for k in nomes_provas:
        if not k[0].isdigit():
            print(f"  [{'ok' if all(v[6][k] for v in resultados.values()) else 'FALHOU'}] {k} — em todas")
    ok_ins = all(ok for r in resultados.values() for k, ok in r[6].items() if k[0].isdigit())
    print(f"  [{'ok' if ok_ins else 'FALHOU'}] nº de inserções = 1 (head) + nº de citações — em todas")
    print(f"  faixas iguais em PT, EN e ES: {'ok' if not divergentes else 'divergem nos caps ' + str(divergentes)}")

    print(f"\n== Puladas: {len(pulados)}")
    por_tipo = {}
    for lang, cap, rel, info in pulados:
        por_tipo.setdefault(info["motivo"], []).append((lang, cap, rel, info))
    for motivo, itens in por_tipo.items():
        print(f"  -- {motivo}: {len(itens)}")
        for lang, cap, rel, info in itens:
            det = info["fora"] or info["modelo"]
            print(f"     {rel}" + (f"  | {' / '.join(det)}" if det else ""))
    fora_total = [x for _, _, _, i in pulados for x in i["fora"]]
    print(f"\n== Rótulos fora dos formatos: {len(fora_total)}" + ("" if not fora_total else ": " + "; ".join(fora_total)))

    if resultados:
        rel0 = next(iter(resultados))
        lang, cap, a, n, ins, info, pv = resultados[rel0]
        print(f"\nExemplo de trecho inserido ({rel0}, 1º bloco):\n" + ins[1][1].decode("utf-8"))
    if not ok_geral:
        print("Prova falhou: nada gravado.")
        return 1
    if "--sim-dir" in sys.argv:
        dest = os.path.abspath(sys.argv[sys.argv.index("--sim-dir") + 1])
        if dest.startswith(ROOT):
            print("--sim-dir precisa ficar fora do repositório"); return 1
        for rel, v in resultados.items():
            alvo = os.path.join(dest, rel); os.makedirs(os.path.dirname(alvo), exist_ok=True)
            open(alvo, "wb").write(v[3])
        print(f"\nPáginas simuladas gravadas em {dest} (fora do repositório)")
    if "--apply" not in sys.argv:
        print("\nSimulação: nada foi gravado no repositório.")
        return 0
    os.makedirs(os.path.join(ROOT, "_backups"), exist_ok=True)
    zp = os.path.join(ROOT, "_backups", f"grego-{livro}-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".zip")
    with zipfile.ZipFile(zp, "x", zipfile.ZIP_DEFLATED) as z:
        for rel, v in resultados.items():
            z.writestr(rel, v[2])
    for rel, v in resultados.items():
        open(os.path.join(ROOT, rel), "wb").write(v[3])
    z = zipfile.ZipFile(zp)
    for rel, v in resultados.items():
        assert open(os.path.join(ROOT, rel), "rb").read() == v[3] and z.read(rel) == v[2]
    print(f"\nGravado: {len(resultados)} páginas; backup em {os.path.relpath(zp, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
