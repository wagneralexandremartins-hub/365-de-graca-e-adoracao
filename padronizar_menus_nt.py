#!/usr/bin/env python3
"""
Padroniza o menu das 28 páginas de livros do NT (08-novo-testamento/**/index.html).
Essas páginas usam <div class="topbar"> com nav inconsistente ou quebrada.
Substitui o bloco topbar inteiro pela versão padronizada com o menu de 7 itens.
"""

from pathlib import Path
import re

ROOT = Path("C:/365graca/08-novo-testamento")

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

# CSS mínimo necessário para .topbar .inner
TOPBAR_CSS = (
    '.topbar { background:rgba(15,23,42,0.97); border-bottom:1px solid rgba(255,255,255,0.08); '
    'padding:0 24px; position:sticky; top:0; z-index:100; }\n'
    '    .topbar .inner { max-width:1100px; margin:0 auto; display:flex; align-items:center; '
    'justify-content:space-between; height:60px; }\n'
    '    .topbar a { color:#94a3b8; text-decoration:none; font-size:0.9rem; transition:color 0.2s; }\n'
    '    .topbar a:hover { color:#f5c542; }\n'
    '    .nav { display:flex; gap:18px; align-items:center; }'
)


def find_topbar_end(content, start):
    """Retorna o índice logo após o </div> de fechamento do div.topbar."""
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


def already_standard(content):
    return (
        'href="/#jornada"' in content
        and 'href="/blocos/"' in content
        and 'href="/loja-365/"' in content
    )


def ensure_inner_css(content):
    """Garante que o CSS do .topbar .inner existe no <style> da página."""
    if '.topbar .inner' in content:
        return content  # já tem

    # Procurar o bloco .topbar { ... } e substituir por versão completa
    topbar_css_re = re.compile(
        r'\.topbar\s*\{[^}]+\}(\s*\.topbar\s+a\s*\{[^}]+\})?(\s*\.topbar\s+a:hover\s*\{[^}]+\})?',
        re.DOTALL
    )
    if topbar_css_re.search(content):
        content = topbar_css_re.sub(TOPBAR_CSS, content, count=1)
    return content


def fix_file(path):
    content = path.read_text(encoding='utf-8')

    if already_standard(content):
        return 'ok'

    start = content.find('<div class="topbar"')
    if start == -1:
        return 'no-topbar'

    end = find_topbar_end(content, start)
    if end == -1:
        return 'parse-error'

    content = content[:start] + TOPBAR_NEW + content[end:]
    content = ensure_inner_css(content)
    path.write_text(content, encoding='utf-8')
    return 'updated'


def main():
    files = sorted(ROOT.rglob('index.html'))
    results = {'updated': [], 'ok': [], 'no-topbar': [], 'parse-error': []}

    for path in files:
        rel = str(path.relative_to(ROOT.parent))
        status = fix_file(path)
        results[status].append(rel)

    print(f"\n{'='*56}")
    print(f"  Atualizados  : {len(results['updated'])}")
    print(f"  Ja corretos  : {len(results['ok'])}")
    print(f"  Sem topbar   : {len(results['no-topbar'])}")
    print(f"  Erro parse   : {len(results['parse-error'])}")
    print(f"{'='*56}\n")
    for r in results['updated']:
        print(f"  [OK] {r}")
    for r in results['parse-error']:
        print(f"  [ERRO] {r}")
    for r in results['no-topbar']:
        print(f"  [SEM NAV] {r}")


if __name__ == '__main__':
    main()
