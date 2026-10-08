"""SEO técnico 2a + 2b: arquivos ausentes, numa só passada.

2a (sem arte nova, nenhuma página editada):
  - assets/img/og-cover.jpg  = og-image.png convertido para JPEG (mesma arte, 1200x630)
  - assets/img/og-image.jpg  = cópia byte a byte do og-cover.jpg acima
  - assets/img/favicon.png   = cópia byte a byte do apple-touch-icon.png
2b (decisão do Wagner, 08/10/2026: opção A):
  - remove a linha '<link rel="stylesheet" href="/styles.css">' das páginas
    (arquivo nunca existiu no repositório; hoje é 404).

Uso:
  python scripts/seo_arquivos_ausentes.py           # dry-run (padrão)
  python scripts/seo_arquivos_ausentes.py --apply   # grava, com backup zip em _backups/

Prova 2b, por página: a tag ocorre uma vez, sozinha na linha; o arquivo novo é
o antigo menos exatamente essa linha (com sua quebra CRLF/LF); nenhum outro byte muda.
Prova 2a: os arquivos de destino não existem antes; JPEG com 1200x630 e
assinatura FF D8; cópias com SHA-256 igual à origem.
"""
import hashlib
import io
import os
import re
import sys
import time
import zipfile

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUIR = {'_backups', 'redesign', 'scripts', '.claude', '.github', '.git', '_site', 'node_modules'}
LINHA_RE = re.compile(rb'^[ \t]*<link rel="stylesheet" href="/styles\.css">[ \t]*\r?\n', re.M)
TAG = b'href="/styles.css"'
JPEG_QUALIDADE = 90


def sha(b):
    return hashlib.sha256(b).hexdigest()[:16]


def gerar_imagens():
    """Devolve {destino: bytes} e a lista de checagens."""
    erros, saida = [], {}
    png = os.path.join(ROOT, 'assets/img/og-image.png')
    ico = os.path.join(ROOT, 'apple-touch-icon.png')
    with Image.open(png) as im:
        origem_tam = im.size
        buf = io.BytesIO()
        im.convert('RGB').save(buf, 'JPEG', quality=JPEG_QUALIDADE, optimize=True)
    jpg = buf.getvalue()
    with Image.open(io.BytesIO(jpg)) as chk:
        if chk.format != 'JPEG' or chk.size != origem_tam or chk.size != (1200, 630):
            erros.append(f'JPEG gerado inválido: {chk.format} {chk.size}')
    if not jpg.startswith(b'\xff\xd8'):
        erros.append('JPEG sem assinatura FF D8')
    fav = open(ico, 'rb').read()
    saida['assets/img/og-cover.jpg'] = jpg
    saida['assets/img/og-image.jpg'] = jpg
    saida['assets/img/favicon.png'] = fav
    for destino in saida:
        if os.path.exists(os.path.join(ROOT, destino)):
            erros.append(f'{destino} já existe; não sobrescrevo')
    if sha(saida['assets/img/favicon.png']) != sha(fav):
        erros.append('favicon.png diferente do apple-touch-icon.png')
    return saida, erros


def paginas():
    for dp, dns, fns in os.walk(ROOT):
        rel = os.path.relpath(dp, ROOT).replace(os.sep, '/')
        if rel.split('/')[0] in EXCLUIR:
            dns[:] = []
            continue
        for fn in fns:
            if fn.endswith('.html'):
                yield ('' if rel == '.' else rel + '/') + fn


def processar_pagina(dados):
    """Devolve (novo, linha_removida) ou (None, motivo) se não se aplica/falha."""
    if TAG not in dados:
        return None, None
    ms = list(LINHA_RE.finditer(dados))
    if len(ms) != 1 or dados.count(TAG) != 1:
        return None, f'esperada 1 linha só com a tag; achadas {len(ms)} linhas e {dados.count(TAG)} tags'
    a, b = ms[0].span()
    return dados[:a] + dados[b:], dados[a:b]


def provar_pagina(velho, novo, linha):
    erros = []
    k = velho.find(linha)
    if k < 0 or velho.count(linha) != 1:
        erros.append('linha não única no original')
    elif velho[:k] + velho[k + len(linha):] != novo:
        erros.append('resultado ≠ original sem a linha')
    if len(velho) - len(novo) != len(linha):
        erros.append('diferença de tamanho inesperada')
    crlf = 1 if linha.endswith(b'\r\n') else 0
    if velho.count(b'\r\n') - novo.count(b'\r\n') != crlf or velho.count(b'\n') - novo.count(b'\n') != 1:
        erros.append('quebras de linha mudaram além da linha removida')
    if TAG in novo:
        erros.append('tag ainda presente')
    return erros


def main():
    gravar = '--apply' in sys.argv
    print('Modo:', 'APLICAR' if gravar else 'SIMULAÇÃO (dry-run)')
    falhas = []

    # 2a
    imagens, e = gerar_imagens()
    falhas += e
    print('\n## 2a — arquivos novos (nenhuma página editada)')
    for destino, dados in imagens.items():
        print(f'  {destino:26s} {len(dados):7d} bytes  sha256 {sha(dados)}')
    print(f'  origem og-image.png sha256 {sha(open(os.path.join(ROOT, "assets/img/og-image.png"), "rb").read())}'
          f' · apple-touch-icon.png sha256 {sha(open(os.path.join(ROOT, "apple-touch-icon.png"), "rb").read())}')

    # 2b (e contagem de quem passa a resolver com o 2a)
    alteradas, por_pasta, deltas, refs = {}, {}, {}, {'og-cover.jpg': 0, 'og-image.jpg': 0, 'favicon.png': 0}
    for p in paginas():
        dados = open(os.path.join(ROOT, p), 'rb').read()
        for nome in refs:
            if ('/assets/img/' + nome).encode() in dados:
                refs[nome] += 1
        novo, info = processar_pagina(dados)
        if novo is None:
            if info:
                falhas.append(f'{p}: {info}')
            continue
        e = provar_pagina(dados, novo, info)
        if e:
            falhas += [f'{p}: {x}' for x in e]
            continue
        alteradas[p] = (dados, novo)
        por_pasta[p.split('/')[0]] = por_pasta.get(p.split('/')[0], 0) + 1
        deltas[len(info)] = deltas.get(len(info), 0) + 1
    print('\n## 2a — páginas cujas referências passam a resolver')
    for nome, n in refs.items():
        print(f'  /assets/img/{nome}: {n} páginas')
    print('\n## 2b — remoção da linha /styles.css')
    print(f'  páginas alteradas: {len(alteradas)}  por pasta: {dict(sorted(por_pasta.items()))}')
    print(f'  bytes removidos por página: {dict(sorted(deltas.items()))}  (linha + CRLF)')
    print(f'  prova byte a byte: {len(alteradas)} OK, {len([f for f in falhas if ".html" in f])} falhas')
    amostras = [x for x in sorted(alteradas) if x.startswith('biblia/')][:2] + \
               [x for x in sorted(alteradas) if not x.startswith('biblia/')][:1]
    for amostra in amostras:
        v, n = alteradas[amostra]
        print(f'  ex.: {amostra}: {len(v)} -> {len(n)} bytes')

    if falhas:
        print()
        for f in falhas:
            print('FALHA:', f)
        print('\nNada gravado.')
        sys.exit(1)
    if not gravar:
        print('\nDry-run: nada gravado. Rode com --apply para gravar.')
        return
    stamp = time.strftime('%Y%m%d-%H%M%S')
    zpath = os.path.join(ROOT, '_backups', f'seo-2a2b-{stamp}.zip')
    os.makedirs(os.path.dirname(zpath), exist_ok=True)
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for p, (velho, _) in alteradas.items():
            z.writestr(p, velho)
    for destino, dados in imagens.items():
        open(os.path.join(ROOT, destino), 'xb').write(dados)
    for p, (_, novo) in alteradas.items():
        open(os.path.join(ROOT, p), 'wb').write(novo)
    print(f'\nGravado: {len(imagens)} arquivos novos e {len(alteradas)} páginas. Backup: {os.path.relpath(zpath, ROOT)}')


if __name__ == '__main__':
    main()
