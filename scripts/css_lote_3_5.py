"""Lote 3.5: botões flutuantes e barra inferior dos capítulos PT do NT (só CSS, em assets/css/bloco.css).

Parte A (aprovada pelo Wagner em 13/10/2026): o botão do WhatsApp (#whatsapp-cta) ficava sobre o botão
"próximo" da barra inferior fixa (.chapter-nav-fixed) nas 260 páginas de capítulo do NT em PT; no celular,
com nomes longos, a barra chega a 104 px e o botão claro/escuro (#dark-toggle) também encostava nela.
As regras sobem os dois botões para cima da barra. `!important` só no WhatsApp, porque a posição dele vem
do atributo style do próprio botão.

Parte B (só em simulação até o OK do Wagner): no celular, o botão "próximo" com nome de livro longo passava
da borda direita da tela (8 páginas a 390 px, 13 a 360 px). Até 600 px, a barra passa a ter duas linhas:
o texto "Capítulo X de 260 do NT" em cima e os botões anterior/próximo embaixo, cada um com metade da
largura e quebra de linha permitida; o espaço reservado embaixo da página (60 px hoje, menor que a barra
no celular) passa para 120 px, para o fim do texto não ficar escondido atrás dela.

Escopo: body:has(.chapter-nav-fixed) — só as páginas que têm a barra inferior (os 260 capítulos PT do NT).
As regras ganham das do <style> de cada página por especificidade (o <style> vem depois do bloco.css).

Uso:
  python scripts/css_lote_3_5.py                          # simulação da parte A (não grava nada)
  python scripts/css_lote_3_5.py --parte-b                # simulação da parte B (sobre o arquivo atual)
  python scripts/css_lote_3_5.py [--parte-b] --sim-out ARQ.css   # + cópia do CSS resultante fora do repo
  python scripts/css_lote_3_5.py [--parte-b] --apply      # grava, com backup zip em _backups/

Prova: o arquivo antigo é prefixo exato do novo (só acréscimo no fim); só CRLF; todo seletor do bloco começa
pelo escopo; varredura das páginas que carregam bloco.css: só as 260 com a barra podem casar.
"""
import datetime, os, re, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = os.path.join(ROOT, "assets", "css", "bloco.css")
ESCOPO = "body:has(.chapter-nav-fixed)"

PARTES = {
    "a": dict(marca="/* lote-3-5a:v1 */", linhas=[
        "/* ─── Lote 3.5 A: WhatsApp e claro/escuro acima da barra inferior (13/10/2026) ───",
        "   Só nas páginas com .chapter-nav-fixed (260 capítulos PT do NT). A barra tem 59 px no desktop",
        "   e até 104 px no celular (nomes longos quebram em várias linhas). Gerado por scripts/css_lote_3_5.py. */",
        f"{ESCOPO} #whatsapp-cta {{ bottom: 72px !important; }}",
        f"{ESCOPO} #dark-toggle {{ bottom: 132px; }}",
        "@media (max-width: 600px) {",
        f"  {ESCOPO} #whatsapp-cta {{ bottom: 116px !important; }}",
        f"  {ESCOPO} #dark-toggle {{ bottom: 176px; }}",
        "}",
    ]),
    "b": dict(marca="/* lote-3-5b:v1 */", linhas=[
        "/* ─── Lote 3.5 B: barra inferior em duas linhas no celular (13/10/2026) ───",
        "   Até 600 px: \"Capítulo X de 260 do NT\" em cima; anterior/próximo embaixo, metade da largura cada,",
        "   com quebra de linha, para o nome longo não passar da borda. A barra fica com 86 a 110 px, então o",
        "   espaço reservado embaixo da página sobe de 60 para 120 px. Gerado por scripts/css_lote_3_5.py. */",
        "@media (max-width: 600px) {",
        f"  {ESCOPO} .chapter-nav-fixed {{ flex-wrap: wrap; row-gap: 0.4rem; }}",
        f"  {ESCOPO} .chapter-nav-fixed .progress-text {{ order: -1; flex: 1 0 100%; }}",
        f"  {ESCOPO} .chapter-nav-fixed a {{ flex: 1 1 0; min-width: 0; white-space: normal; text-align: center; }}",
        f"  {ESCOPO} {{ padding-bottom: 120px; }}",
        "}",
    ]),
}


def bloco(parte):
    p = PARTES[parte]
    return ("\r\n".join(["", p["marca"]] + p["linhas"]) + "\r\n").encode("utf-8")


def seletores(add):
    sem_coment = re.sub(rb"/\*.*?\*/", b"", add, flags=re.S)
    return [s.strip() for s in re.findall(rb"([^{}]+)\{", sem_coment) if not s.strip().startswith(b"@media")]


RX_BLOCO_CSS = re.compile(rb'<link[^>]+href="[^"]*/assets/css/bloco\.css"')


def varredura():
    """Páginas que carregam bloco.css e quantas têm a barra inferior (únicas que o escopo pode casar)."""
    total, com_barra = 0, []
    for d, ds, fs in os.walk(ROOT):
        ds[:] = [x for x in ds if x not in (".git", "_backups", "node_modules", ".claude", "redesign")]
        for f in fs:
            if f.endswith(".html"):
                b = open(os.path.join(d, f), "rb").read()
                if RX_BLOCO_CSS.search(b):
                    total += 1
                    if b'class="chapter-nav-fixed"' in b:
                        com_barra.append(os.path.relpath(os.path.join(d, f), ROOT).replace(os.sep, "/"))
    return total, com_barra


def main():
    parte = "b" if "--parte-b" in sys.argv else "a"
    antigo = open(CSS, "rb").read()
    if PARTES[parte]["marca"].encode() in antigo:
        print(f"bloco.css já tem a parte {parte.upper()} ({PARTES[parte]['marca']}): 0 mudanças.")
        return 0
    if parte == "b" and PARTES["a"]["marca"].encode() not in antigo:
        print("A parte B pressupõe a parte A já aplicada: nada feito."); return 1
    add = bloco(parte)
    novo = antigo + add
    sel = seletores(add)
    provas = {
        "antigo é prefixo exato do novo": novo[: len(antigo)] == antigo,
        "antigo termina em CRLF": antigo.endswith(b"\r\n"),
        "bloco e arquivo só com CRLF": add.count(b"\n") == add.count(b"\r\n") and novo.count(b"\n") == novo.count(b"\r\n"),
        f"{len(sel)} regras, todas com o escopo {ESCOPO}": bool(sel) and all(s.startswith(ESCOPO.encode()) for s in sel),
    }
    print(f"Parte {parte.upper()} — bloco.css: {len(antigo)} -> {len(novo)} bytes (+{len(add)}); linhas +{add.count(b'\n')}")
    print("\nBloco acrescentado no fim:\n" + add.decode("utf-8"))
    total, com_barra = varredura()
    pt = all(not (p.startswith("en/") or p.startswith("es/")) for p in com_barra)
    nt = all(p.startswith("08-novo-testamento/") and "/capitulos/" in p for p in com_barra)
    print(f"Páginas que carregam bloco.css: {total}; com a barra inferior (únicas que o escopo pode casar): {len(com_barra)}")
    provas["260 páginas com a barra, todas capítulos PT do NT"] = len(com_barra) == 260 and pt and nt
    print("\nProvas:")
    for k, ok in provas.items():
        print(f"  [{'ok' if ok else 'FALHOU'}] {k}")
    if not all(provas.values()):
        print("Prova falhou: nada gravado."); return 1
    if "--sim-out" in sys.argv:
        dest = sys.argv[sys.argv.index("--sim-out") + 1]
        if os.path.abspath(dest).startswith(ROOT):
            print("--sim-out precisa ficar fora do repositório"); return 1
        open(dest, "wb").write(novo); print(f"\nCSS simulado gravado em {dest} (fora do repositório)")
    if "--apply" not in sys.argv:
        print("\nSimulação: nada foi gravado no repositório."); return 0
    os.makedirs(os.path.join(ROOT, "_backups"), exist_ok=True)
    zp = os.path.join(ROOT, "_backups", f"lote-3-5{parte}-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".zip")
    with zipfile.ZipFile(zp, "x", zipfile.ZIP_DEFLATED) as z:
        z.writestr("assets/css/bloco.css", antigo)
    open(CSS, "wb").write(novo)
    assert open(CSS, "rb").read() == novo and zipfile.ZipFile(zp).read("assets/css/bloco.css") == antigo
    print(f"\nGravado assets/css/bloco.css (parte {parte.upper()}); backup em {os.path.relpath(zp, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
