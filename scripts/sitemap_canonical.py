"""SEO técnico 3: alinhar o sitemap.xml aos canonicals (decisão provisória do
Wagner, 08/10/2026: URL oficial sem .html, como os canonicals atuais).

Nenhuma página é alterada. Só o texto dentro de cada <loc> do sitemap.xml muda,
e só quando a página correspondente declara um canonical "aproveitável":
  - existe exatamente um <link rel="canonical"> no arquivo;
  - aponta para https://365gracaeadoracao.com (sem www, sem http);
  - não termina em .html;
  - resolve para o MESMO arquivo que o <loc> atual;
  - não é pasta sem barra final (o GitHub Pages responde 301 nesse caso).
Nos demais casos o <loc> fica como está e a página é listada para decisão.
lastmod, changefreq, priority, comentários, ordem e quebras de linha (CRLF)
ficam intactos.

Uso:
  python scripts/sitemap_canonical.py           # simulação (padrão)
  python scripts/sitemap_canonical.py --apply   # grava, com backup zip em _backups/
"""
import collections
import os
import re
import sys
import time
import zipfile
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(ROOT, 'sitemap.xml')
DOMINIO = 'https://365gracaeadoracao.com'
LOC_RE = re.compile(rb'<loc>([^<]*)</loc>')
CANON_RE = re.compile(rb'<link\b[^>]*\brel=["\']canonical["\'][^>]*>', re.I)
HREF_RE = re.compile(rb'\bhref=["\']([^"\']*)["\']', re.I)


def arquivo_de(url):
    """Caminho relativo do arquivo que a URL serve no GitHub Pages, ou None."""
    p = urlparse(url).path.lstrip('/')
    if p == '' or p.endswith('/'):
        cands = [p + 'index.html']
    elif p.endswith('.html'):
        cands = [p]
    else:
        cands = [p + '.html', p + '/index.html']
    for c in cands:
        if os.path.isfile(os.path.join(ROOT, c)):
            return c
    return None


def forma(url):
    p = urlparse(url).path
    if p.endswith('/index.html'):
        return 'pasta/index.html'
    if p.endswith('.html'):
        return 'arquivo.html'
    if p.endswith('/'):
        return 'pasta/'
    if p.endswith('/index'):
        return 'pasta/index'
    if os.path.isdir(os.path.join(ROOT, p.lstrip('/'))):
        return 'pasta (sem barra)'
    return 'arquivo sem extensão'


def canonical_de(rel):
    dados = open(os.path.join(ROOT, rel), 'rb').read()
    tags = CANON_RE.findall(dados)
    if not tags:
        return None, 'sem canonical'
    hrefs = {m.group(1).decode('utf-8') for t in tags for m in [HREF_RE.search(t)] if m}
    if len(hrefs) != 1:
        return None, f'{len(tags)} tags canonical com hrefs {sorted(hrefs)}'
    return hrefs.pop(), None


def idioma(rel):
    return {'en': 'EN', 'es': 'ES'}.get(rel.split('/')[0], 'PT')


def main():
    gravar = '--apply' in sys.argv
    print('Modo:', 'APLICAR' if gravar else 'SIMULAÇÃO (dry-run)')
    velho = open(SITEMAP, 'rb').read()
    locs = list(LOC_RE.finditer(velho))

    novos, mudam, iguais = [], [], 0
    pend = collections.defaultdict(list)          # motivo -> [(loc, canonical, arquivo)]
    transicoes = collections.Counter()           # (idioma, forma antes, forma depois)
    exemplos = {}
    for m in locs:
        loc = m.group(1).decode('utf-8')
        rel = arquivo_de(loc)
        novo = loc
        pendente = True
        if rel is None:
            pend['loc do sitemap não resolve para arquivo'].append((loc, '', ''))
        else:
            can, erro = canonical_de(rel)
            if erro:
                pend[erro if erro == 'sem canonical' else 'canonical ambíguo'].append((loc, erro, rel))
            elif not can.startswith(DOMINIO + '/'):
                pend['canonical fora de https://365gracaeadoracao.com'].append((loc, can, rel))
            elif can.endswith('.html'):
                pend['canonical com .html'].append((loc, can, rel))
            elif arquivo_de(can) != rel:
                pend['canonical aponta para outra página (ou 404)'].append((loc, can, rel))
            elif forma(can) == 'pasta (sem barra)':
                # GitHub Pages responde 301 para /pasta/; não pôr URL com redirect no sitemap
                pend['canonical de pasta sem barra final (301 no GitHub Pages)'].append((loc, can, rel))
            else:
                novo = can
                pendente = False
        if novo != loc:
            k = (idioma(rel), forma(loc), forma(novo))
            transicoes[k] += 1
            exemplos.setdefault(k, (loc, novo))
            mudam.append((loc, novo))
        elif not pendente:
            iguais += 1
        novos.append(novo.encode('utf-8'))

    # Reconstrói trocando só o conteúdo de cada <loc>
    partes, pos = [], 0
    for m, n in zip(locs, novos):
        a, b = m.span(1)
        partes += [velho[pos:a], n]
        pos = b
    partes.append(velho[pos:])
    novo_xml = b''.join(partes)

    # Prova: fora dos <loc>, o arquivo é idêntico byte a byte
    falhas = []
    mascara = lambda d: LOC_RE.sub(b'<loc></loc>', d)
    if mascara(velho) != mascara(novo_xml):
        falhas.append('texto fora de <loc> mudou')
    if [x.group(1) for x in LOC_RE.finditer(novo_xml)] != novos:
        falhas.append('ordem/quantidade de <loc> mudou')
    for tag in (b'<url>', b'</url>', b'<lastmod>', b'<priority>', b'<changefreq>', b'\r\n', b'\n'):
        if velho.count(tag) != novo_xml.count(tag):
            falhas.append(f'contagem de {tag!r} mudou')
    for padrao in (rb'<lastmod>[^<]*</lastmod>', rb'<priority>[^<]*</priority>', rb'<changefreq>[^<]*</changefreq>'):
        if re.findall(padrao, velho) != re.findall(padrao, novo_xml):
            falhas.append(f'sequência {padrao!r} mudou')
    finais = [n.decode() for n in novos]
    dup = [u for u, c in collections.Counter(finais).items() if c > 1]
    if dup:
        falhas.append(f'{len(dup)} <loc> duplicados após a troca, ex.: {dup[:3]}')

    print(f'\nsitemap.xml: {len(locs)} <loc>  |  {len(velho)} -> {len(novo_xml)} bytes '
          f'({len(novo_xml) - len(velho):+d})')
    print(f'  mudam: {len(mudam)}   já iguais ao canonical: {iguais}   '
          f'ficam como estão por pendência: {sum(len(v) for v in pend.values())}')
    print('\n## Transições (idioma | forma no sitemap -> forma do canonical | qtd | exemplo)')
    for k, n in sorted(transicoes.items(), key=lambda x: -x[1]):
        a, b = exemplos[k]
        print(f'  {k[0]} | {k[1]} -> {k[2]} | {n}\n      {a}\n   -> {b}')
    print('\n## Ficam como estão (decisão pendente)')
    for motivo, itens in sorted(pend.items(), key=lambda x: -len(x[1])):
        print(f'  {motivo}: {len(itens)}')
        for loc, can, rel in itens:
            print(f'     {rel or loc}' + (f'  canonical={can}' if can and can != motivo else ''))
    print('\n## Prova')
    print('  ' + ('OK: fora de <loc> o arquivo é idêntico byte a byte; ordem, '
                  'lastmod, changefreq, priority e CRLF preservados; sem duplicados'
                  if not falhas else 'FALHAS: ' + '; '.join(falhas)))

    if falhas:
        print('\nNada gravado.')
        sys.exit(1)
    if not gravar:
        print('\nDry-run: nada gravado. Rode com --apply para gravar.')
        return
    stamp = time.strftime('%Y%m%d-%H%M%S')
    zpath = os.path.join(ROOT, '_backups', f'sitemap-canonical-{stamp}.zip')
    os.makedirs(os.path.dirname(zpath), exist_ok=True)
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('sitemap.xml', velho)
    open(SITEMAP, 'wb').write(novo_xml)
    print(f'\nGravado: sitemap.xml ({len(mudam)} <loc> alterados). Backup: {os.path.relpath(zpath, ROOT)}')


if __name__ == '__main__':
    main()
