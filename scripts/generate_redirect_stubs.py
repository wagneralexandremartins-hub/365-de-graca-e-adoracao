#!/usr/bin/env python3
"""
Gera páginas estáticas de redirect (meta refresh) a partir do array
"redirects" do vercel.json, para GitHub Pages (que não tem redirects
server-side).

Rotas com parâmetro (contêm ":") são puladas e listadas no relatório --
tratadas manualmente com um pequeno catch-all JS.

Uso:
  python scripts/generate_redirect_stubs.py            # dry-run, só relatório
  python scripts/generate_redirect_stubs.py --apply    # cria os arquivos
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERCEL_JSON = ROOT / "vercel.json"

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


def main():
    apply_changes = "--apply" in sys.argv

    data = json.loads(VERCEL_JSON.read_text(encoding="utf-8"))
    redirects = data["redirects"]

    fixed = []
    parametrized = []
    for r in redirects:
        if ":" in r["source"]:
            parametrized.append(r)
        else:
            fixed.append(r)

    print(f"Redirects com origem fixa (viram stub estático): {len(fixed)}")
    print(f"Redirects com parâmetro (precisam de solução manual): {len(parametrized)}")

    missing_dest = []
    created = []
    for r in fixed:
        source = r["source"].strip("/")
        dest = r["destination"]
        if not dest.endswith("/"):
            dest += "/"
        dest_dir = ROOT / dest.strip("/")
        if not (dest_dir / "index.html").is_file():
            missing_dest.append((r["source"], dest))
            continue

        stub_path = ROOT / source / "index.html"
        created.append((source, dest, stub_path))

    if missing_dest:
        print("\n--- ATENÇÃO: destino não existe, stub não será criado ---")
        for src, dest in missing_dest:
            print(f"  {src} -> {dest}  (pasta/index.html não encontrada)")

    print(f"\nStubs a criar: {len(created)}")
    for source, dest, stub_path in created:
        print(f"  /{source}  ->  {dest}")

    if parametrized:
        print("\n--- Rotas parametrizadas (fora do lote automático) ---")
        for r in parametrized:
            print(f"  {r['source']}  ->  {r['destination']}")

    if not apply_changes:
        print("\n(dry-run — nenhum arquivo foi criado; rode com --apply para gerar)")
        return

    for source, dest, stub_path in created:
        stub_path.parent.mkdir(parents=True, exist_ok=True)
        stub_path.write_text(STUB_TEMPLATE.format(dest=dest), encoding="utf-8")

    print(f"\nCriado(s): {len(created)} arquivo(s) de redirect.")


if __name__ == "__main__":
    main()
