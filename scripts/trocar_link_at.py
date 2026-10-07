#!/usr/bin/env python3
"""
Troca o link do item "Antigo Testamento" do protótipo para o endereço final:
    /redesign/antigo-testamento.html  →  /antigo-testamento/

Onde troca (e só ali):
  1. Dentro dos blocos <!-- site-nav:v1 --> … <!-- /site-nav:v1 --> das páginas
     .html (fora de en/, es/, _backups/, redesign/, scripts/, .claude/).
     Nada fora dos blocos é tocado.
  2. assets/js/site-nav.js: href e regra de item ativo do MENU; sai o aviso de piloto.
  3. scripts/aplicar_menu_central.py: lista MENU usada no fallback de páginas futuras.

Garantias:
  - Leitura e gravação em bytes: CRLF/LF preservados exatamente.
  - Prova por página: os trechos fora dos blocos são idênticos byte a byte;
    desfazer a troca devolve o arquivo original; o número de blocos não muda.
  - Prova nos arquivos de código: só mudam as linhas previstas; finais de linha iguais.
  - Idempotente: o que já está com /antigo-testamento/ conta como "já correto".
  - Qualquer falha de prova impede o --apply inteiro.

Uso:
  python scripts/trocar_link_at.py            # dry-run (padrão): só lê e imprime
  python scripts/trocar_link_at.py --apply    # grava (antes, backup zip em _backups/)
"""
import difflib
import re
import sys
import zipfile
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
APPLY = "--apply" in sys.argv

OLD, NEW = b"/redesign/antigo-testamento.html", b"/antigo-testamento/"
OLD_HREF, NEW_HREF = b'href="' + OLD + b'"', b'href="' + NEW + b'"'
BLOCK = re.compile(rb"<!-- site-nav:v1 -->[\s\S]*?<!-- /site-nav:v1 -->")
SKIP = {".git", "_backups", "redesign", "en", "es", "scripts", ".claude"}


def troca_blocos(data, de, para):
    return BLOCK.sub(lambda m: m.group(0).replace(de, para), data)


def fora_dos_blocos(data):
    return BLOCK.split(data)


def finais_de_linha(data):
    crlf = data.count(b"\r\n")
    return crlf, data.count(b"\n") - crlf


# ---------------------------------------------------------------- páginas
mudar, corretas, falhas, fora = [], [], [], []
for p in sorted(ROOT.rglob("*.html")):
    rel = p.relative_to(ROOT).as_posix()
    if p.relative_to(ROOT).parts[0] in SKIP:
        continue
    old = p.read_bytes()
    blocos = BLOCK.findall(old)
    if not blocos:
        continue
    if OLD in b"".join(fora_dos_blocos(old)):
        fora.append(rel)                       # cita o endereço fora dos blocos: não mexe
    dentro = b"".join(blocos)
    if OLD not in dentro:
        if NEW_HREF in dentro:
            corretas.append(rel)
        continue
    new = troca_blocos(old, OLD_HREF, NEW_HREF)
    motivos = []
    if fora_dos_blocos(new) != fora_dos_blocos(old):
        motivos.append("mudou fora dos blocos")
    if len(BLOCK.findall(new)) != len(blocos):
        motivos.append("número de blocos mudou")
    if troca_blocos(new, NEW_HREF, OLD_HREF) != old:
        motivos.append("troca não é reversível")
    if OLD in b"".join(BLOCK.findall(new)):
        motivos.append("endereço antigo sobrou no bloco (fora de href)")
    if finais_de_linha(new) != finais_de_linha(old):
        motivos.append("finais de linha mudaram")
    if motivos:
        falhas.append((rel, motivos))
    else:
        mudar.append((p, rel, old, new))

# ---------------------------------------------------------------- código
SN_OLD_HREF = b"href: '/redesign/antigo-testamento.html',  label: 'Antigo Testamento'"
SN_NEW_HREF = b"href: '/antigo-testamento/',              label: 'Antigo Testamento'"
SN_OLD_MATCH = rb"match: /^\/(redesign\/antigo-testamento|0[1-57]-|"
SN_NEW_MATCH = rb"match: /^\/(antigo-testamento\/|redesign\/antigo-testamento|0[1-57]-|"
SN_AVISO = re.compile(
    re.escape('  // ATENÇÃO (piloto): "Antigo Testamento" aponta para o protótipo até a etapa'.encode("utf-8"))
    + rb"\r?\n"
    + re.escape("  // dos hubs criar a página definitiva. Ver redesign/PLANO.md.".encode("utf-8"))
    + rb"\r?\n")
AP_OLD = b'("/redesign/antigo-testamento.html", "Antigo Testamento")'
AP_NEW = b'("/antigo-testamento/", "Antigo Testamento")'


def regra_site_nav(d):
    d = d.replace(SN_OLD_HREF, SN_NEW_HREF)
    if SN_NEW_MATCH not in d:
        d = d.replace(SN_OLD_MATCH, SN_NEW_MATCH)
    return SN_AVISO.sub(b"", d)


CODIGO = [
    ("assets/js/site-nav.js", regra_site_nav, SN_NEW_HREF, 3),
    ("scripts/aplicar_menu_central.py", lambda d: d.replace(AP_OLD, AP_NEW), AP_NEW, 1),
]
cod_mudar, cod_corretos = [], []
for rel, regra, marca_nova, linhas_previstas in CODIGO:
    path = ROOT / rel
    before = path.read_bytes()
    after = regra(before)
    if after == before:
        if marca_nova in before and OLD not in before:
            cod_corretos.append(rel)
        else:
            falhas.append((rel, ["padrão esperado não encontrado"]))
        continue
    a_lin, b_lin = before.splitlines(keepends=True), after.splitlines(keepends=True)
    diff = [l for l in difflib.diff_bytes(difflib.unified_diff, a_lin, b_lin, n=0) if l[:1] in (b"+", b"-") and l[:3] not in (b"+++", b"---")]
    motivos = []
    if sum(1 for l in diff if l[:1] == b"-") != linhas_previstas:
        motivos.append(f"linhas alteradas ≠ {linhas_previstas}")
    if any(not l.endswith(b"\r\n") for l in b_lin[:-1]) != any(not l.endswith(b"\r\n") for l in a_lin[:-1]):
        motivos.append("finais de linha mudaram")
    if motivos:
        falhas.append((rel, motivos))
    else:
        cod_mudar.append((path, rel, before, after, diff))

# ---------------------------------------------------------------- relatório
print(f"páginas a alterar (link antigo nos blocos site-nav:v1): {len(mudar)}")
print(f"páginas já corretas (link novo nos blocos): {len(corretas)}")
print(f"falhas de prova: {len(falhas)}")
for rel, motivos in falhas[:20]:
    print(f"   ✗ {rel}: {'; '.join(motivos)}")
print(f"páginas que citam o endereço antigo FORA dos blocos (não tocadas): {len(fora)}")
for rel in fora[:10]:
    print(f"   · {rel}")
por_pasta = {}
for _, rel, _, _ in mudar:
    k = rel.split("/")[0] if "/" in rel else "(raiz)"
    por_pasta[k] = por_pasta.get(k, 0) + 1
if por_pasta:
    print("por pasta:", ", ".join(f"{k} {v}" for k, v in sorted(por_pasta.items(), key=lambda x: -x[1])))
print(f"\narquivos de código a alterar: {len(cod_mudar)} · já corretos: {len(cod_corretos)}")
for _, rel, _, _, diff in cod_mudar:
    print(f"   {rel}:")
    for l in diff:
        print("     ", l.decode("utf-8").rstrip("\r\n")[:160])
if mudar:
    _, rel, old, new = mudar[0]
    i = old.find(OLD_HREF)
    print(f"\nexemplo ({rel}):")
    print("   antes :", old[i - 20:i + len(OLD_HREF) + 25].decode("utf-8"))
    j = new.find(NEW_HREF, i - 20)
    print("   depois:", new[j - 20:j + len(NEW_HREF) + 25].decode("utf-8"))

if not APPLY:
    print("\n(dry-run — nada gravado; use --apply para gravar)")
    sys.exit(1 if falhas else 0)
if falhas:
    print("\nNADA GRAVADO: há falhas de prova.")
    sys.exit(1)
if not mudar and not cod_mudar:
    print("\nNada a fazer: tudo já está correto.")
    sys.exit(0)

z = ROOT / "_backups" / f"trocar-link-at-{datetime.now():%Y%m%d-%H%M%S}.zip"
z.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
    for _, rel, old, _ in mudar:
        zf.writestr(rel, old)
    for _, rel, before, _, _ in cod_mudar:
        zf.writestr(rel, before)
for p, _, _, new in mudar:
    p.write_bytes(new)
for path, _, _, after, _ in cod_mudar:
    path.write_bytes(after)
print(f"\nAPLICADO: {len(mudar)} páginas + {len(cod_mudar)} arquivos de código. Backup: {z.relative_to(ROOT).as_posix()}")
