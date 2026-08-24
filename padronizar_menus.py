#!/usr/bin/env python3
"""
Padroniza o menu de navegação em todos os index.html do projeto 365.
Alvo: apenas arquivos index.html (exclui capitulo-*.html e backups).
Menu padrão: Início | Jornada | 13 Blocos | Idiomas | Personagens | Loja 365 | Sobre

Duas estruturas de header existem no site:
  1. <nav class="nav">...</nav> com a logo FORA do <nav> (padrão da maioria
     das páginas) — o script substitui o <nav> inteiro.
  2. <nav class="navbar"><div class="container"><a class="brand">logo</a>
     <ul class="nav-links">...</ul></div></nav>, onde a logo fica DENTRO do
     <nav> (hoje só em /sobre e /sobre/fontes) — substituir o <nav> inteiro
     apagaria a logo. Nesse caso o script troca só o <ul class="nav-links">.

Uso:
  python padronizar_menus.py                 # dry-run: só mostra o diff
  python padronizar_menus.py --apply         # aplica as mudanças
  python padronizar_menus.py --only a,b      # restringe às paths dadas
                                              # (relativas à raiz do repo,
                                              # separadas por vírgula)
"""

import re
import sys
import difflib
from pathlib import Path

# Console do Windows costuma usar cp1252, que não cobre emoji/símbolos que
# aparecem no HTML (usados no diff do dry-run); força UTF-8 na saída.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent

# Arquivo raiz — já tem o menu correto com âncoras locais; pular.
SKIP_FILES = {ROOT / "index.html"}

# Fonte única dos 7 itens do menu padrão.
MENU_LINKS = [
    ("/", "Início"),
    ("/#jornada", "Jornada"),
    ("/blocos/", "13 Blocos"),
    ("/#idiomas", "Idiomas"),
    ("/personagens/index.html", "Personagens"),
    ("/loja-365/", "Loja 365"),
    ("/sobre/index.html", "Sobre"),
]

# Variante 1: <nav class="nav"> com a logo fora do <nav>.
MENU_STANDARD = (
    '<nav class="nav" aria-label="Menu principal">\n'
    + "".join(f'        <a href="{href}">{label}</a>\n' for href, label in MENU_LINKS)
    + '      </nav>'
)

# Variante 2: <ul class="nav-links"> dentro de <nav class="navbar">, com a
# logo (a.brand) como irmã do <ul>, dentro do mesmo <nav>.
MENU_LINKS_LIST = (
    '<ul class="nav-links">\n'
    + "".join(f'                <li><a href="{href}">{label}</a></li>\n' for href, label in MENU_LINKS)
    + '            </ul>'
)

NAV_PATTERN = re.compile(r'<nav\s+class="nav"[^>]*>.*?</nav>', re.DOTALL)
NAVBAR_TAG_PATTERN = re.compile(r'<nav\s+class="navbar"[^>]*>')
NAVBAR_LIST_PATTERN = re.compile(r'<ul\s+class="nav-links"[^>]*>.*?</ul>', re.DOTALL)

REQUIRED_HREFS = [f'href="{href}"' for href, _ in MENU_LINKS]


def already_standard(content: str) -> bool:
    """Retorna True se o menu já contém todos os 7 itens padrão."""
    return all(r in content for r in REQUIRED_HREFS)


def _reindent(menu: str, content: str, start: int) -> str:
    """Ajusta a indentação do menu para bater com a linha onde ele entra."""
    line_start = content.rfind('\n', 0, start) + 1
    indent = ''
    for ch in content[line_start:start]:
        if ch in (' ', '\t'):
            indent += ch
        else:
            break
    last_line = menu.splitlines()[-1]  # última linha = tag de fechamento
    base_indent = last_line[:len(last_line) - len(last_line.lstrip())]
    if indent and indent != base_indent:
        menu = menu.replace(base_indent, indent)
    return menu


def fix_menu(content: str) -> tuple[str, bool]:
    """
    Substitui o menu de navegação pelo padrão, preservando a logo/marca
    nas páginas onde ela vive dentro do <nav> (estrutura "navbar").
    Retorna (novo_conteúdo, foi_alterado).
    """
    if NAVBAR_TAG_PATTERN.search(content):
        match = NAVBAR_LIST_PATTERN.search(content)
        if not match:
            return content, False
        menu = _reindent(MENU_LINKS_LIST, content, match.start())
        new_content = content[:match.start()] + menu + content[match.end():]
        return new_content, True

    match = NAV_PATTERN.search(content)
    if not match:
        return content, False
    menu = _reindent(MENU_STANDARD, content, match.start())
    new_content = content[:match.start()] + menu + content[match.end():]
    return new_content, True


def process_all(root: Path, apply_changes: bool, only: set[Path] | None = None):
    files = [
        p for p in root.rglob("index.html")
        if "_backups" not in str(p)
        and ".git" not in str(p)
        and p not in SKIP_FILES
    ]
    if only is not None:
        files = [p for p in files if p in only]

    updated = []
    skipped_already_ok = 0
    skipped_no_nav = 0
    errors = []

    for path in sorted(files):
        try:
            content = path.read_text(encoding="utf-8")

            if already_standard(content):
                skipped_already_ok += 1
                continue

            new_content, changed = fix_menu(content)

            if not changed:
                skipped_no_nav += 1
                continue

            updated.append(path.relative_to(root))

            if apply_changes:
                path.write_text(new_content, encoding="utf-8")
            else:
                diff = difflib.unified_diff(
                    content.splitlines(keepends=True),
                    new_content.splitlines(keepends=True),
                    fromfile=f"a/{path.relative_to(root)}",
                    tofile=f"b/{path.relative_to(root)}",
                )
                print("".join(diff))

        except Exception as e:
            errors.append(f"{path}: {e}")

    print(f"\n{'='*60}")
    print(f"{'Atualizados' if apply_changes else 'Seriam atualizados'}: {len(updated)}")
    print(f"Já corretos  : {skipped_already_ok}")
    print(f"Sem nav alvo : {skipped_no_nav}")
    print(f"Erros        : {len(errors)}")
    if errors:
        print("\nErros:")
        for e in errors:
            print(f"  {e}")
    print("=" * 60)

    for p in updated:
        print(f"  {'[OK]' if apply_changes else '~'} {p}")

    if not apply_changes and updated:
        print("\n(dry-run — nenhum arquivo foi alterado; rode com --apply para aplicar)")


if __name__ == "__main__":
    apply_flag = "--apply" in sys.argv
    only_arg = next((a for a in sys.argv if a.startswith("--only=")), None)
    if not only_arg:
        for i, a in enumerate(sys.argv):
            if a == "--only" and i + 1 < len(sys.argv):
                only_arg = "--only=" + sys.argv[i + 1]
                break

    only_paths = None
    if only_arg:
        raw = only_arg.split("=", 1)[1]
        only_paths = {(ROOT / p.strip()).resolve() for p in raw.split(",") if p.strip()}

    process_all(ROOT, apply_changes=apply_flag, only=only_paths)
