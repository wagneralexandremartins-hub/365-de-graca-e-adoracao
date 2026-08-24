#!/usr/bin/env python3
"""
Audita e corrige links internos sem extensão (href="/algo" sem .html e sem /
final) no site, para migração Vercel -> GitHub Pages.

- Se existir alvo/index.html: não precisa mexer (GitHub Pages redireciona
  /alvo -> /alvo/ automaticamente quando existe index.html na pasta).
- Se existir alvo.html: reescreve o href para incluir .html (GitHub Pages não
  tem "clean URLs" para arquivos, só para pastas).
- Se não existir nenhum dos dois: fica sem alterar e entra no relatório de
  "não resolvidos" para revisão manual.

Uso:
  python scripts/fix_clean_urls.py            # dry-run, só relatório
  python scripts/fix_clean_urls.py --apply    # aplica as correções de arquivo
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
HREF_RE = re.compile(r'href="(/[a-zA-Z0-9][a-zA-Z0-9\-/]*[a-zA-Z0-9])"')


def iter_html_files():
    for p in ROOT.rglob("*.html"):
        if "_backups" in p.parts:
            continue
        yield p


def resolve(target: str) -> str:
    """Retorna 'dir', 'file' ou 'missing' para o alvo (path começando com /)."""
    rel = target.lstrip("/")
    if (ROOT / rel / "index.html").is_file():
        return "dir"
    if (ROOT / f"{rel}.html").is_file():
        return "file"
    return "missing"


def main():
    apply_changes = "--apply" in sys.argv

    targets_to_files = defaultdict(set)
    for path in iter_html_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for m in HREF_RE.finditer(text):
            targets_to_files[m.group(1)].add(path)

    buckets = {"dir": [], "file": [], "missing": []}
    for target in sorted(targets_to_files):
        buckets[resolve(target)].append(target)

    print("=" * 70)
    print(f"Total de hrefs únicos sem extensão: {len(targets_to_files)}")
    print(f"  -> pasta com index.html (OK, GH Pages resolve sozinho): {len(buckets['dir'])}")
    print(f"  -> arquivo .html (precisa virar .html no href)        : {len(buckets['file'])}")
    print(f"  -> não resolvido (revisar manualmente)                : {len(buckets['missing'])}")
    print("=" * 70)

    if buckets["file"]:
        print("\n--- Alvos que precisam de .html ---")
        for t in buckets["file"]:
            print(f"  {t}  ({len(targets_to_files[t])} arquivo(s) referenciando)")

    if buckets["missing"]:
        print("\n--- NÃO RESOLVIDOS (revisar manualmente) ---")
        for t in buckets["missing"]:
            files = sorted(targets_to_files[t])[:3]
            sample = ", ".join(str(f.relative_to(ROOT)) for f in files)
            extra = "" if len(targets_to_files[t]) <= 3 else f" (+{len(targets_to_files[t]) - 3} outros)"
            print(f"  {t}  <- {sample}{extra}")

    if not apply_changes:
        print("\n(dry-run — nenhum arquivo foi alterado; rode com --apply para corrigir)")
        return

    changed_files = 0
    for target in buckets["file"]:
        old = f'href="{target}"'
        new = f'href="{target}.html"'
        for path in targets_to_files[target]:
            text = path.read_text(encoding="utf-8", errors="ignore")
            if old in text:
                path.write_text(text.replace(old, new), encoding="utf-8")
                changed_files += 1

    print(f"\nAplicado: {changed_files} escrita(s) de arquivo.")


if __name__ == "__main__":
    main()
