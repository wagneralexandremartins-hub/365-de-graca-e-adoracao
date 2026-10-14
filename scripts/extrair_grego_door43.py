"""Extrai do Door43 o grego dos versículos citados num Evangelho e grava scripts/dados/grego-tr-<livro>.json.

Fonte: Textus Receptus 1894 Scrivener, Door43 STR/el-x-koine_trs (CC BY-SA 4.0), commit fixado
4107626cbc0bd577a9024e66ff4614342e6b4238 (o mesmo do piloto de João 3). Conferência: byztxt
greektext-scrivener (Robinson, domínio público), commit fixado 6049a43b, pasta textonly/.
Adaptação: só as palavras e a pontuação (sem lema, Strong e morfologia), Unicode NFC — igual ao piloto.

Quais versículos: os das citações reais das páginas PT, EN e ES do livro (mesma varredura de
scripts/aplicar_grego_evangelhos.py; páginas de modelo ficam de fora — decisão do Wagner, 14/10/2026).

Provas (se qualquer uma falhar, nada é gravado):
  • SHA-256 dos arquivos-fonte = os fixados abaixo;
  • o USFM só tem os marcadores esperados; nenhum versículo extraído tem palavra vazia — exceto o
    "item vazio" de número composto (decisão do Wagner, 14/10/2026): o Door43 escreve o número inteiro
    numa palavra (ex.: εἰκοσιπέντε, Jo 6:19) e acrescenta logo depois uma linha sem texto só com o 2º
    lema (πέντε). É aceita apenas quando as duas linhas são numerais e a anterior tem a forma escrita;
    o texto não muda e o caso fica listado em "itens_vazios_aceitos";
  • o mesmo método reproduz byte a byte os 10 versículos de João 3 do piloto;
  • todo versículo em NFC (só troca por equivalente canônico, listada em "normalizados_nfc"), sem &, < ou >;
  • nos capítulos citados, os números de versículo são os mesmos no Door43, no byztxt e na ACF do site (biblia/);
  • cada versículo extraído = byztxt palavra a palavra (diferenças só de grafia são listadas: ν móvel,
    οὕτω/οὕτως, διατί/διὰ τί, ἱνατί/ἵνα τί, μήτι/μή τι);
  • rodar de novo gera o mesmo arquivo, byte a byte.

Uso:
  python scripts/extrair_grego_door43.py --livro mateus --baixar PASTA      # baixa as fontes fixadas (fora do repo)
  python scripts/extrair_grego_door43.py --livro mateus --fontes PASTA      # simulação: mostra o que gravaria
  python scripts/extrair_grego_door43.py --livro mateus --fontes PASTA --gravar
"""
import ast, hashlib, json, os, re, sys, unicodedata, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import aplicar_grego_evangelhos as ap

DOOR43_COMMIT = "4107626cbc0bd577a9024e66ff4614342e6b4238"
DOOR43_URL = "https://git.door43.org/STR/el-x-koine_trs/raw/commit/" + DOOR43_COMMIT + "/"
BYZ_COMMIT = "6049a43b135ed870f843b83eb6a04764fc796678"
BYZ_URL = "https://raw.githubusercontent.com/byztxt/greektext-scrivener/" + BYZ_COMMIT + "/textonly/"
SHA256 = {
    "41-MAT.usfm": "8eeb6a4344a3a4ab7f538e0f252508873e749272c820b373ebff5277728987bc",
    "42-MRK.usfm": "623f9f8c38ac5815d09948818a0206b4a4e0616e36eb44d876af5357cbc0cb4d",
    "43-LUK.usfm": "3553432dfa90fe5ec9f2fcb72517d2c0c0a18701972879813d08aceebae66be4",
    "44-JHN.usfm": "f93ebbc0404ed35effb898940ed179d79b10d7b24395179ec495231deb047cf9",
    "MT.SCV": "ac09657841358fe278cdc8e725b5f7301ca267f9427352a98ffd3f01c3091ace",
    "MR.SCV": "7fe8267676568ab61d1e97ae1e2cdcd605613fd5853b0e452473bb6bf3b19919",
    "LU.SCV": "98691cf08a155f742fed28e5e69b6bb92b1aa2c684f7b5c66cd2369d5ed8b00d",
    "JOH.SCV": "8eeaea1cc32b7559d68691b408d45f69780eeee782aa05eb49b0526107d601b8",
}
RX_W = re.compile(r'^\\w ([^|]*)\|[^\\]*\\w\*(.*)$')
RX_LEMA = re.compile(r'lemma="([^"]*)"')
RX_CABECALHO = re.compile(r"^\\(id|usfm|ide|h|toc\d|mt) ")
# numerais cardinais (lema), para reconhecer o "item vazio" de número composto
NUMERAIS = {"εἷς", "δύο", "τρεῖς", "τέσσαρες", "πέντε", "ἕξ", "ἑπτά", "ὀκτώ", "ἐννέα", "δέκα", "δώδεκα",
            "εἴκοσι", "τριάκοντα", "τεσσαράκοντα", "τεσσεράκοντα", "πεντήκοντα", "ἑξήκοντα", "ἑβδομήκοντα",
            "ὀγδοήκοντα", "ἐνενήκοντα", "ἑκατόν", "διακόσιοι", "τριακόσιοι", "χίλιοι"}


def le_usfm(path):
    """{(cap, v): texto}, {(cap, v)} com palavra vazia, [linhas desconhecidas], {(cap, v)} com item vazio
    de número composto aceito (a linha anterior, no mesmo versículo, é numeral com a forma escrita)."""
    vs, vazios, estranhas, compostos, c, v = {}, set(), [], set(), None, None
    anterior = None  # (forma, lema) da linha \w anterior no mesmo versículo
    for ln in open(path, encoding="utf-8").read().splitlines():
        if ln.startswith("\\c "): c, v, anterior = int(ln[3:]), None, None
        elif ln.startswith("\\v "): v = int(ln[3:]); vs[(c, v)] = []; anterior = None
        elif ln.startswith("\\w "):
            m = RX_W.match(ln)
            if not m or v is None: estranhas.append(ln); continue
            lema = RX_LEMA.search(ln)
            lema = unicodedata.normalize("NFC", lema.group(1)) if lema else ""
            if not m.group(1):
                if anterior and anterior[0] and anterior[1] in NUMERAIS and lema in NUMERAIS:
                    compostos.add((c, v))
                else:
                    vazios.add((c, v))
                anterior = ("", lema); continue
            vs[(c, v)].append(m.group(1) + m.group(2).strip())
            anterior = (m.group(1), lema)
        elif ln in ("\\p", "") or RX_CABECALHO.match(ln): pass
        else: estranhas.append(ln)
    return {k: " ".join(w) for k, w in vs.items()}, vazios, estranhas, compostos


TRANSLIT = dict(zip("αβγδεζηθικλμνξοπρστυφχψως", "abgdezhyiklmnxoprstufcqwv"))


def translit(t):
    t = "".join(ch for ch in unicodedata.normalize("NFD", t.lower()) if not unicodedata.combining(ch))
    return "".join(TRANSLIT.get(ch, ch if ch.isalnum() else " ") for ch in t.replace("’", "")).split()


def le_scv(path):
    txt = re.sub(r"\[[^\]]*\]", " ", open(path, encoding="latin-1").read())
    partes = re.split(r"(\d+:\d+)", txt)
    return {tuple(map(int, partes[i].split(":"))): re.sub(r"[^a-z ]", " ", partes[i + 1].lower()).split()
            for i in range(1, len(partes), 2)}


JUNTAS = {("dia", "ti"): "diati", ("ina", "ti"): "inati", ("mh", "ti"): "mhti"}


def grafia(ws):
    out, i = [], 0
    while i < len(ws):
        par = tuple(ws[i:i + 2])
        if par in JUNTAS: out.append(JUNTAS[par]); i += 2; continue
        w = ws[i]; i += 1
        out.append("outw" if w == "outwv" else w)
    return out


def compara(a, b):
    """'igual', 'grafia' (só ν móvel e afins) ou 'leitura'."""
    if a == b: return "igual"
    a, b = grafia(a), grafia(b)
    if len(a) == len(b) and all(x == y or x + "n" == y or y + "n" == x for x, y in zip(a, b)): return "grafia"
    return "leitura"


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    if "--livro" not in sys.argv or sys.argv[sys.argv.index("--livro") + 1] not in ap.LIVROS:
        print("uso: --livro " + "|".join(ap.LIVROS) + " (--baixar PASTA | --fontes PASTA [--gravar])"); return 2
    livro = sys.argv[sys.argv.index("--livro") + 1]
    cfg = ap.LIVROS[livro]
    arquivos = list(dict.fromkeys([cfg["usfm"], "44-JHN.usfm", cfg["byz"]]))  # em João, 44-JHN aparece uma vez só
    if "--baixar" in sys.argv:
        dest = os.path.abspath(sys.argv[sys.argv.index("--baixar") + 1])
        if dest.startswith(ROOT): print("--baixar precisa de pasta fora do repositório"); return 1
        os.makedirs(dest, exist_ok=True)
        for f in arquivos:
            url = (BYZ_URL if f.endswith(".SCV") else DOOR43_URL) + f
            urllib.request.urlretrieve(url, os.path.join(dest, f))
            print(f"{f}: {'ok' if sha(os.path.join(dest, f)) == SHA256[f] else 'SHA-256 DIFERENTE'}")
        return 0
    fontes = os.path.abspath(sys.argv[sys.argv.index("--fontes") + 1])
    provas = {f"SHA-256 de {f} = fixado": sha(os.path.join(fontes, f)) == SHA256[f] for f in arquivos}

    texto, vazios, estranhas, compostos = le_usfm(os.path.join(fontes, cfg["usfm"]))
    jhn, _, estr_jhn, _ = le_usfm(os.path.join(fontes, "44-JHN.usfm"))
    src = open(os.path.join(ROOT, "scripts", "aplicar_grego_jo3.py"), encoding="utf-8").read()
    piloto = ast.literal_eval(re.search(r"GREGO = (\{.*?\n\})", src, re.S).group(1))
    provas[f"USFM só com marcadores esperados ({len(estranhas)} linhas desconhecidas)"] = not estranhas and not estr_jhn
    provas["método reproduz byte a byte os 10 versículos de João 3 do piloto"] = all(jhn[(3, v)] == t for v, t in piloto.items())

    # versículos citados nas páginas (citações reais, 3 idiomas)
    citados, modelo = set(), 0
    for lang in ap.LANGS:
        tpl, nome = cfg[lang]
        for cap in range(1, cfg["caps"] + 1):
            info = ap.varre_pagina(open(os.path.join(ROOT, tpl.format(cap)), "rb").read(), nome, cap)
            modelo += info["tipo"] == "modelo"
            for _, a, z, _ in info["citacoes"]:
                citados |= {(cap, v) for v in range(a, z + 1)}
    citados = sorted(citados)
    provas["todos os versículos citados existem no Door43"] = all(k in texto for k in citados)
    provas["nenhum versículo citado tem palavra vazia no USFM"] = not (set(citados) & vazios)
    versos = {f"{c}:{v}": unicodedata.normalize("NFC", texto[(c, v)]) for c, v in citados if (c, v) in texto}
    # o Door43 às vezes usa formas pré-compostas que a NFC troca pela equivalente canônica (ex.: U+1FD3 ΐ -> U+0390)
    normalizados = [f"{c}:{v}" for c, v in citados if (c, v) in texto and unicodedata.normalize("NFC", texto[(c, v)]) != texto[(c, v)]]
    provas["NFC só troca por equivalentes canônicos (NFD igual)"] = all(
        unicodedata.normalize("NFD", versos[k]) == unicodedata.normalize("NFD", texto[tuple(map(int, k.split(":")))]) for k in versos)
    provas["sem &, < ou > no grego"] = all(not set(t) & set("&<>") for t in versos.values())

    # numeração: Door43 × byztxt × ACF nos capítulos citados
    byz = le_scv(os.path.join(fontes, cfg["byz"]))
    numeracao = []
    for cap in sorted({c for c, _ in citados}):
        b = open(os.path.join(ROOT, "biblia", cfg["acf"], f"{cfg['acf']}-{cap:02d}.html"), "rb").read().decode("utf-8")
        acf = {int(n) for n in re.findall(r'<span class="verse-number">(\d+)</span>', b)}
        d43 = {v for c, v in texto if c == cap}; bz = {v for c, v in byz if c == cap}
        if not (acf == d43 == bz): numeracao.append(cap)
    provas["numeração dos capítulos citados igual em Door43, byztxt e ACF"] = not numeracao

    # leitura: Door43 × byztxt
    cmp_cit = {k: compara(translit(texto[k]), byz.get(k, [])) for k in citados}
    cmp_livro = {k: compara(translit(t), byz.get(k, [])) for k, t in texto.items()}
    provas["versículos citados = byztxt (0 diferenças de leitura)"] = all(r != "leitura" for r in cmp_cit.values())

    dados = {
        "livro": livro,
        "fonte": {"texto": "Textus Receptus 1894 Scrivener", "edicao": "Door43 STR/el-x-koine_trs",
                  "licenca": "CC BY-SA 4.0", "url": "https://git.door43.org/STR/el-x-koine_trs",
                  "commit": DOOR43_COMMIT, "arquivo": cfg["usfm"], "sha256": SHA256[cfg["usfm"]]},
        "conferencia": {"texto": "byztxt greektext-scrivener (Robinson, domínio público)",
                        "commit": BYZ_COMMIT, "arquivo": "textonly/" + cfg["byz"], "sha256": SHA256[cfg["byz"]],
                        "versiculos_conferidos": len(cmp_cit),
                        "iguais": sum(r == "igual" for r in cmp_cit.values()),
                        "so_grafia": sorted(k for k, r in cmp_cit.items() if r == "grafia"),
                        "diferencas_de_leitura": sorted(k for k, r in cmp_cit.items() if r == "leitura")},
        "adaptacao": "só as palavras e a pontuação da fonte (sem lema, Strong e morfologia), Unicode NFC",
        "normalizados_nfc": normalizados,
        "versiculos": versos,
    }
    aceitos = [f"{c}:{v}" for c, v in citados if (c, v) in compostos]
    if aceitos:  # só aparece quando há caso citado (os JSON de Mateus, Marcos e Lucas não mudam)
        dados = {k: dados[k] for k in list(dados)[:-1]} | {"itens_vazios_aceitos": aceitos, "versiculos": versos}
    dados["conferencia"]["so_grafia"] = [f"{c}:{v}" for c, v in dados["conferencia"]["so_grafia"]]
    dados["conferencia"]["diferencas_de_leitura"] = [f"{c}:{v}" for c, v in dados["conferencia"]["diferencas_de_leitura"]]
    saida = (json.dumps(dados, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    provas["determinístico (2ª geração idêntica)"] = saida == (json.dumps(json.loads(saida), ensure_ascii=False, indent=1) + "\n").encode("utf-8")

    print(f"Livro: {livro} — {len(versos)} versículos citados em {len({c for c, _ in citados})} capítulos "
          f"({modelo} páginas de modelo ignoradas nos 3 idiomas)")
    for k, ok in provas.items():
        print(f"  [{'ok' if ok else 'FALHOU'}] {k}")
    if numeracao: print("  capítulos com numeração diferente:", numeracao)
    print(f"  byztxt (citados): {dados['conferencia']['iguais']} iguais, {len(dados['conferencia']['so_grafia'])} só grafia "
          f"{dados['conferencia']['so_grafia']}, {len(dados['conferencia']['diferencas_de_leitura'])} de leitura")
    lv = [k for k, r in cmp_livro.items() if r == "leitura"]
    print(f"  byztxt (livro inteiro, só informativo): {len(texto)} versículos, {sum(r == 'igual' for r in cmp_livro.values())} iguais, "
          f"{sum(r == 'grafia' for r in cmp_livro.values())} só grafia, {len(lv)} outros (divisão de versículo/variante): "
          f"{[f'{c}:{v}' for c, v in sorted(lv)]}")
    if compostos: print(f"  itens vazios de número composto (aceitos; texto completo na linha anterior): {sorted(compostos)}"
                        + (f" — citados: {aceitos}" if aceitos else ""))
    if vazios: print(f"  palavras vazias no USFM (fora das citações): {sorted(vazios)}")
    if not all(provas.values()):
        print("Prova falhou: nada gravado."); return 1
    destino = ap.caminho_dados(livro)
    # o git guarda LF; com core.autocrlf a cópia local pode estar em CRLF — compara sem o CR
    atual = open(destino, "rb").read().replace(b"\r\n", b"\n") if os.path.exists(destino) else None
    print(f"\n{os.path.relpath(destino, ROOT)}: {len(saida)} bytes, "
          + ("idêntico ao existente" if atual == saida else "NOVO" if atual is None else "DIFERENTE do existente"))
    if "--gravar" not in sys.argv:
        print("Simulação: nada gravado."); return 0
    if atual is not None:
        print("já existe: " + ("nada a fazer" if atual == saida else "não sobrescrevo")); return 0 if atual == saida else 1
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "xb") as f:
        f.write(saida)
    assert open(destino, "rb").read() == saida
    print("Gravado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
