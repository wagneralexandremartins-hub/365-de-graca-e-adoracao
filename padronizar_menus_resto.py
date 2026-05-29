#!/usr/bin/env python3
"""
Padroniza o menu nas páginas restantes do site 365 Graça & Adoração.
Lista explícita de diretórios-alvo para evitar atingir EN/ES e capítulos.
"""

import re
from pathlib import Path

ROOT = Path("C:/365graca")

# Diretórios-alvo (apenas estes — sem rglob aberto)
TARGET_DIRS = [
    "09-igreja-primitiva",
    "10-concilios",
    "11-cruzadas",
    "12-conflitos-contemporaneos",
    "13-apocalipse",
    "autismo-e-fe",
    "biblia",
    "como-estudar-a-biblia",
    "ebook-4-passos",
    "estudos/contexto-historico/cultura-cotidiano-mundo-biblico",
    "estudos/contexto-historico/geografia-terra-santa",
    "estudos/cruz-de-cristo",
    "genesis",
    "loja-365",
    "referencias",
]

# Páginas únicas restantes (fora dos diretórios acima)
EXTRA_FILES = [
    # nenhuma — index.html raiz está OK com âncoras locais
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

# Apenas <nav> SEM atributos (bare nav) — não toca <nav class="topbar"> etc.
BARE_NAV_RE = re.compile(r'<nav\s*>.*?</nav>', re.DOTALL)


def already_standard(content):
    return (
        'href="/#jornada"' in content
        and 'href="/blocos/"' in content
        and 'href="/loja-365/"' in content
    )


def find_div_end(content, start):
    i, depth = start, 0
    while i < len(content):
        if content[i:i+4] == '<div':
            depth += 1; i += 4; continue
        if content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                return i + 6
            i += 6; continue
        i += 1
    return -1


def find_header_end(content, start):
    i, depth = start, 0
    while i < len(content):
        if content[i:i+7] == '<header':
            depth += 1; i += 7; continue
        if content[i:i+9] == '</header>':
            depth -= 1
            if depth == 0:
                return i + 9
            i += 9; continue
        i += 1
    return -1


def fix_file(path):
    content = path.read_text(encoding='utf-8')

    if already_standard(content):
        return 'ok'

    # Padrão 1: div.topbar
    if '<div class="topbar"' in content:
        start = content.find('<div class="topbar"')
        end = find_div_end(content, start)
        if end == -1:
            return 'parse-error'
        content = content[:start] + TOPBAR_NEW + content[end:]
        path.write_text(content, encoding='utf-8')
        return 'updated-topbar'

    # Padrão 2: <header class="topbar"> ou <header>
    for header_tag in ('<header class="topbar">', '<header>'):
        if header_tag in content:
            start = content.find(header_tag)
            end = find_header_end(content, start)
            if end == -1:
                return 'parse-error'
            content = content[:start] + TOPBAR_NEW + content[end:]
            path.write_text(content, encoding='utf-8')
            return 'updated-header'

    # Padrão 3: bare <nav> (SEM atributos)
    m = BARE_NAV_RE.search(content)
    if m:
        content = content[:m.start()] + NAV_STANDARD + content[m.end():]
        path.write_text(content, encoding='utf-8')
        return 'updated-nav'

    return 'no-match'


def collect_targets():
    targets = []
    for d in TARGET_DIRS:
        dir_path = ROOT / d
        if dir_path.is_file():
            targets.append(dir_path)
        elif dir_path.is_dir():
            targets.extend(sorted(dir_path.rglob('index.html')))
    for f in EXTRA_FILES:
        targets.append(ROOT / f)
    return targets


def main():
    targets = collect_targets()
    results = {}

    for path in targets:
        rel = str(path.relative_to(ROOT))
        results[rel] = fix_file(path)

    counts = {}
    for s in results.values():
        counts[s] = counts.get(s, 0) + 1

    print(f"\n{'='*60}")
    for k, v in sorted(counts.items()):
        print(f"  {k:22s}: {v}")
    print(f"{'='*60}\n")

    for rel, status in sorted(results.items()):
        tag = 'OK ' if 'updated' in status else ('---' if status == 'ok' else 'ERR')
        print(f"  [{tag}] {status:20s} {rel}")


if __name__ == '__main__':
    main()
