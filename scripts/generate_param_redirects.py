#!/usr/bin/env python3
"""
Gera os stubs de redirect para as rotas parametrizadas do vercel.json que
têm alcance conhecido e pequeno (capítulos de Josué, João/John, es/juan).
Complementa scripts/generate_redirect_stubs.py, que só trata rotas fixas.

Uso:
  python scripts/generate_param_redirects.py            # dry-run
  python scripts/generate_param_redirects.py --apply
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STUB_TEMPLATE = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Redirecionando… | 365 Graça & Adoração</title>
<link rel="canonical" href="https://365gracaeadoracao.com{dest}">
<meta http-equiv="refresh" content="0; url={dest}">
<meta name="robots" content="noindex,follow">
</head>
<body>
<p>Esta página foi movida para <a href="{dest}">{dest}</a>.</p>
</body>
</html>
"""


def build_jobs():
    jobs = []

    # /03-historicos/josue/capitulo-N(/) -> /03-historicos/josue/capitulos/capitulo-N.html
    for n in range(1, 25):
        num = f"{n:02d}"
        dest = f"/03-historicos/josue/capitulos/capitulo-{num}.html"
        jobs.append((f"03-historicos/josue/capitulo-{n}", dest))

    # /08-novo-testamento/john/capitulos/capitulo-NN(.html) -> .../joao/capitulos/capitulo-NN.html
    for n in range(1, 22):
        num = f"{n:02d}"
        dest = f"/08-novo-testamento/joao/capitulos/capitulo-{num}.html"
        jobs.append((f"08-novo-testamento/john/capitulos/capitulo-{num}", dest))
        jobs.append((f"08-novo-testamento/john/capitulos/capitulo-{num}.html", dest))

    # /es/john-N(/) -> /es/juan-N/
    for n in range(1, 22):
        dest = f"/es/juan-{n}/"
        jobs.append((f"es/john-{n}", dest))

    # legacy catch-all, caso genérico (sem sub-caminho)
    jobs.append(("06-apocrifos/capitulos", "/06-apocrifos/"))

    return jobs


def main():
    apply_changes = "--apply" in sys.argv
    jobs = build_jobs()

    collisions = []
    to_create = []
    for source, dest in jobs:
        if source.endswith(".html"):
            stub_path = ROOT / source
        else:
            stub_path = ROOT / source / "index.html"
        if stub_path.exists():
            collisions.append((source, dest, stub_path))
        else:
            to_create.append((source, dest, stub_path))

    print(f"Stubs a criar: {len(to_create)}")
    if collisions:
        print(f"\n--- JA EXISTEM (não serão sobrescritos) ---")
        for source, dest, path in collisions:
            print(f"  /{source}")

    if not apply_changes:
        print("\n(dry-run — nenhum arquivo foi criado; rode com --apply para gerar)")
        return

    for source, dest, stub_path in to_create:
        stub_path.parent.mkdir(parents=True, exist_ok=True)
        stub_path.write_text(STUB_TEMPLATE.format(dest=dest), encoding="utf-8")

    print(f"\nCriado(s): {len(to_create)} arquivo(s) de redirect.")


if __name__ == "__main__":
    main()
