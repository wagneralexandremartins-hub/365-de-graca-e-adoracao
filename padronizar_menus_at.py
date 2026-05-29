#!/usr/bin/env python3
"""
Padroniza o menu das páginas de livros do AT pendentes.
Trata 3 padrões distintos:
  A) <div class="topbar"> → substitui o bloco inteiro (06-apocrifos, 07-intertestamentario)
  B) <header>...</header> → substitui o bloco header (02-pentateuco/genesis, exodo)
  C) bare <nav> dentro de container → substitui só o <nav>...</nav> (levitico, numeros, deuteronomio)
"""

import re
from pathlib import Path

ROOT = Path("C:/365graca")

# Arquivos alvo — apenas os pendentes
TARGETS = [
    "02-pentateuco/genesis/index.html",
    "02-pentateuco/exodo/index.html",
    "02-pentateuco/levitico/index.html",
    "02-pentateuco/numeros/index.html",
    "02-pentateuco/deuteronomio/index.html",
    "06-apocrifos/index.html",
    "06-apocrifos/acrescimos/index.html",
    "06-apocrifos/1-macabeus/index.html",
    "06-apocrifos/2-macabeus/index.html",
    "06-apocrifos/baruque/index.html",
    "06-apocrifos/eclesiastico/index.html",
    "06-apocrifos/judite/index.html",
    "06-apocrifos/sabedoria/index.html",
    "06-apocrifos/tobias/index.html",
    "07-intertestamentario/index.html",
    "07-intertestamentario/expectativa-messianica/index.html",
    "07-intertestamentario/grupos-judaicos/index.html",
    "07-intertestamentario/periodo-helenistico/index.html",
    "07-intertestamentario/periodo-macabeu/index.html",
    "07-intertestamentario/periodo-persa/index.html",
    "07-intertestamentario/periodo-romano/index.html",
    "07-intertestamentario/sintese-teologica/index.html",
]

BRAND = (
    '<a href="/" class="brand" aria-label="365 Graça e Adoração">'
    '<img src="/assets/img/logo-header.png" alt="365 Graça e Adoração" '
    'class="brand-logo-img" style="height:42px;width:auto;display:block;">'
    '<div class="brand-text">365 Graça &amp; Adoração'
    '<small>Da Criação ao Apocalipse</small></div></a>'
)

TOPBAR_NEW = (
    '<div class="topbar">\n'
    '  <div class="inner">\n'
    '    ' + BRAND + '\n'
    '    <nav class="nav" aria-label="Menu principal">\n'
    '      <a href="/">Início</a>\n'
    '      <a href="/#jornada">Jornada</a>\n'
    '      <a href="/blocos/">13 Blocos</a>\n'
    '      <a href="/#idiomas">Idiomas</a>\n'
    '      <a href="/personagens/index.html">Personagens</a>\n'
    '      <a href="/loja-365/">Loja 365</a>\n'
    '      <a href="/sobre/index.html">Sobre</a>\n'
    '    </nav>\n'
    '  </div>\n'
    '</div>'
)

NAV_STANDARD = (
    '<nav class="nav" aria-label="Menu principal">\n'
    '      <a href="/">Início</a>\n'
    '      <a href="/#jornada">Jornada</a>\n'
    '      <a href="/blocos/">13 Blocos</a>\n'
    '      <a href="/#idiomas">Idiomas</a>\n'
    '      <a href="/personagens/index.html">Personagens</a>\n'
    '      <a href="/loja-365/">Loja 365</a>\n'
    '      <a href="/sobre/index.html">Sobre</a>\n'
    '    </nav>'
)

# Regex para <nav> bare (sem classe) com ou sem atributos
BARE_NAV_RE = re.compile(r'<nav(?:\s[^>]*)?>.*?</nav>', re.DOTALL)


def already_standard(content):
    return (
        'href="/#jornada"' in content
        and 'href="/blocos/"' in content
        and 'href="/loja-365/"' in content
    )


def find_div_end(content, start):
    """Retorna o índice logo após o </div> de fechamento do div em `start`."""
    i = start
    depth = 0
    while i < len(content):
        if content[i] == '<':
            if content[i:i+4] == '<div':
                depth += 1
                i += 4
                continue
            if content[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    return i + 6
                i += 6
                continue
        i += 1
    return -1


def find_tag_end(content, start, open_tag, close_tag):
    """Encontra o fim de uma tag aninhável (ex: <header> / </header>)."""
    i = start
    depth = 0
    while i < len(content):
        if content[i:i+len(open_tag)] == open_tag:
            depth += 1
            i += len(open_tag)
            continue
        if content[i:i+len(close_tag)] == close_tag:
            depth -= 1
            if depth == 0:
                return i + len(close_tag)
            i += len(close_tag)
            continue
        i += 1
    return -1


def fix_topbar(content):
    """Padrão A: substitui <div class="topbar">...</div>."""
    start = content.find('<div class="topbar"')
    if start == -1:
        return content, False
    end = find_div_end(content, start)
    if end == -1:
        return content, False
    return content[:start] + TOPBAR_NEW + content[end:], True


def fix_header(content):
    """Padrão B: substitui <header>...</header>."""
    start = content.find('<header>')
    if start == -1:
        return content, False
    end = find_tag_end(content, start, '<header', '</header>')
    if end == -1:
        return content, False
    return content[:start] + TOPBAR_NEW + content[end:], True


def fix_bare_nav(content):
    """Padrão C: substitui <nav>...</nav> (sem classe) pelo nav padrão."""
    # Garantir que é um nav bare (sem class=)
    match = BARE_NAV_RE.search(content)
    if not match:
        return content, False
    new_content = content[:match.start()] + NAV_STANDARD + content[match.end():]
    return new_content, True


def fix_file(path):
    content = path.read_text(encoding='utf-8')

    if already_standard(content):
        return 'ok'

    # Padrão A: div.topbar
    if '<div class="topbar"' in content:
        new_content, changed = fix_topbar(content)
        if changed:
            path.write_text(new_content, encoding='utf-8')
            return 'updated-topbar'
        return 'parse-error'

    # Padrão B: <header>
    if '<header>' in content:
        new_content, changed = fix_header(content)
        if changed:
            path.write_text(new_content, encoding='utf-8')
            return 'updated-header'
        return 'parse-error'

    # Padrão C: bare <nav>
    new_content, changed = fix_bare_nav(content)
    if changed:
        path.write_text(new_content, encoding='utf-8')
        return 'updated-nav'

    return 'no-match'


def main():
    results = {}
    for rel in TARGETS:
        path = ROOT / rel
        if not path.exists():
            results[rel] = 'not-found'
            continue
        results[rel] = fix_file(path)

    counts = {}
    for status in results.values():
        counts[status] = counts.get(status, 0) + 1

    print(f"\n{'='*56}")
    for k, v in counts.items():
        print(f"  {k:20s}: {v}")
    print(f"{'='*56}\n")

    for rel, status in results.items():
        icon = 'OK' if 'updated' in status else ('JA' if status == 'ok' else 'ERR')
        print(f"  [{icon}] {status:20s} {rel}")


if __name__ == '__main__':
    main()
