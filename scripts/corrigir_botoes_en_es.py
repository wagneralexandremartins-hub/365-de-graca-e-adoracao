"""Botões anterior/próximo do topo das páginas EN/ES (pedido do Wagner, 09/10/2026).

Nas páginas en/<livro>-<N>/index.html e es/<livro>-<N>/index.html, o bloco
<nav class="chapter-nav"> do fim do artigo tem links relativos
"capitulo-NN.html" que não existem (o Search Console mostra 548 desses 404,
mais 32 /en|es/capitulo-NN.html herdados da época do Vercel, com
trailingSlash: false). O script troca SÓ o valor do href pelo endereço do
capítulo vizinho no mesmo livro, no formato dos links de baixo da página:
  en/luke-14:  href="capitulo-13.html"  ->  href="/en/luke-13/"
Só troca se: a pasta é <livro>-<N>; NN é N-1 ou N+1; en|es/<livro>-<NN>/index.html
existe. O resto (capítulo 1, último capítulo, alvo inexistente, NN fora da
sequência, href relativo fora do nav do topo) é listado como caso de borda e
não muda. Nenhum texto é tocado.

Uso:
  python scripts/corrigir_botoes_en_es.py           # simulação (padrão)
  python scripts/corrigir_botoes_en_es.py --apply   # grava, com backup zip em _backups/

Prova, por página: com os hrefs trocados mascarados, antigo e novo são
idênticos; a diferença de tamanho é a soma das diferenças dos hrefs; contagem
de \\r\\n e de \\n preservada.
"""
import os
import re
import sys
import time
import zipfile
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_RE = re.compile(r'^(.+)-(\d+)$')
NAV_RE = re.compile(rb'<nav class="chapter-nav">(.*?)</nav>', re.S)
HREF_RE = re.compile(rb'href="capitulo-(\d+)\.html"')
A_RE = re.compile(rb'<a href="([^"]*)"[^>]*>(.*?)</a>', re.S)
EXEMPLOS = ('en/luke-14/index.html', 'es/mateo-20/index.html', 'en/romans-2/index.html')


def alvo_existe(lang, livro, n):
    return os.path.isfile(os.path.join(ROOT, lang, f'{livro}-{n}', 'index.html'))


def analisar(lang, pasta, v):
    """Retorna (trocas [(ini, fim, antigo, novo)], bordas [motivo], links_baixo_ok)."""
    trocas, bordas = [], []
    m = PASTA_RE.match(pasta)
    hrefs_todos = [x for x in HREF_RE.finditer(v)]
    if not hrefs_todos and not NAV_RE.search(v):
        return trocas, bordas, None
    if not m:
        bordas.append(f'pasta fora do padrão <livro>-<N>: {len(hrefs_todos)} href(s)')
        return [], bordas, None
    livro, n = m.group(1), int(m.group(2))
    nav = NAV_RE.search(v)
    dentro = set()
    if nav:
        for h in HREF_RE.finditer(v, nav.start(1), nav.end(1)):
            dentro.add(h.start())
            nn = int(h.group(1))
            if nn not in (n - 1, n + 1):
                bordas.append(f'capitulo-{h.group(1).decode()}.html não é vizinho de {n}')
                continue
            if not alvo_existe(lang, livro, nn):
                bordas.append(f'capitulo-{h.group(1).decode()}.html -> /{lang}/{livro}-{nn}/ não existe')
                continue
            trocas.append((h.start(), h.end(), h.group(0), f'href="/{lang}/{livro}-{nn}/"'.encode()))
        for a in A_RE.finditer(v, nav.start(1), nav.end(1)):
            href, rotulo = a.group(1), a.group(2)
            if HREF_RE.match(b'href="' + href + b'"'):
                continue
            seta = '←' if '←'.encode() in rotulo else '→' if '→'.encode() in rotulo else None
            if seta:
                bordas.append(f'botão {seta} aponta para "{href.decode()}" (sem capítulo '
                              f'{"anterior" if seta == "←" else "seguinte"}), não muda')
    for h in hrefs_todos:
        if h.start() not in dentro:
            bordas.append(f'capitulo-{h.group(1).decode()}.html fora do <nav class="chapter-nav"> do topo')
    # os links de baixo da página já apontam para o mesmo endereço?
    resto = v[:nav.start()] + v[nav.end():] if nav else v
    baixo_ok = all(t[3] in resto for t in trocas) if trocas else None
    return trocas, bordas, baixo_ok


def aplicar(v, trocas):
    partes, pos = [], 0
    for ini, fim, _, novo in trocas:
        partes += [v[pos:ini], novo]
        pos = fim
    partes.append(v[pos:])
    return b''.join(partes)


def provar(v, novo, trocas):
    mask = b'\x00HREF\x00'
    a = aplicar(v, [(i, f, o, mask) for i, f, o, _ in trocas])
    b = novo
    # mascarar no novo nas posições deslocadas
    partes, pos, desloc = [], 0, 0
    for ini, fim, o, n in trocas:
        i2 = ini + desloc
        partes += [b[pos:i2], mask]
        pos = i2 + len(n)
        desloc += len(n) - len(o)
    partes.append(b[pos:])
    ok = a == b''.join(partes)
    ok &= len(novo) - len(v) == sum(len(n) - len(o) for _, _, o, n in trocas)
    ok &= v.count(b'\r\n') == novo.count(b'\r\n') and v.count(b'\n') == novo.count(b'\n')
    ok &= aplicar(v, trocas) == novo
    return ok


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    gravar = '--apply' in sys.argv
    print('Modo:', 'APLICAR' if gravar else 'SIMULAÇÃO (dry-run)')
    novos, bordas, falhas, exemplos, avisos = {}, [], [], [], []
    stats = Counter()
    for lang in ('en', 'es'):
        base = os.path.join(ROOT, lang)
        for pasta in sorted(os.listdir(base)):
            p = os.path.join(base, pasta, 'index.html')
            if not os.path.isfile(p):
                continue
            rel = f'{lang}/{pasta}/index.html'
            v = open(p, 'rb').read()
            trocas, bs, baixo_ok = analisar(lang, pasta, v)
            for b in bs:
                bordas.append((rel, b))
            if not trocas:
                continue
            novo = aplicar(v, trocas)
            if not provar(v, novo, trocas):
                falhas.append(rel)
                continue
            novos[rel] = novo
            stats[lang] += 1
            stats['botoes'] += len(trocas)
            stats['botoes_' + lang] += len(trocas)
            stats['quebra_' + ('CRLF' if b'\r\n' in v else 'LF')] += 1
            stats['baixo_igual' if baixo_ok else 'baixo_diferente'] += 1
            if baixo_ok is False:
                avisos.append(rel)
            if rel in EXEMPLOS:
                exemplos.append((rel, trocas))

    print(f'\nPáginas que mudam: {len(novos)} (en {stats["en"]}, es {stats["es"]})')
    print(f'Botões trocados: {stats["botoes"]} (en {stats["botoes_en"]}, es {stats["botoes_es"]})')
    print(f'Quebra de linha das páginas: LF {stats["quebra_LF"]}, CRLF {stats["quebra_CRLF"]}')
    print(f'Links de baixo da página iguais ao novo href: {stats["baixo_igual"]} páginas; diferentes: {stats["baixo_diferente"]}')
    print(f'Prova byte a byte: {len(novos)}/{len(novos) + len(falhas)} ok')
    for f in falhas:
        print('  FALHOU:', f)

    print('\nExemplos (antes -> depois):')
    for rel, trocas in exemplos:
        print(' ', rel)
        for _, _, o, n in trocas:
            print('     ', o.decode(), '->', n.decode())

    print(f'\nTrocadas, mas sem link de baixo igual para comparar: {len(avisos)}')
    for rel in avisos:
        print('   ', rel)

    print(f'\nCasos de borda, NÃO alterados: {len(bordas)}')
    tipos = Counter(re.sub(r'capitulo-\d+|/[a-z0-9-]+-\d+/|\d+', '#', b) for _, b in bordas)
    for t, c in tipos.most_common():
        print(f'  {c:4d}  {t}')
    for rel, b in bordas:
        print('   ', rel, '|', b)

    if falhas:
        print('\nProva falhou: nada gravado.')
        sys.exit(1)
    if not gravar:
        print('\nDry-run: nada gravado. Rode com --apply para gravar.')
        return

    stamp = time.strftime('%Y%m%d-%H%M%S')
    zpath = os.path.join(ROOT, '_backups', f'botoes-en-es-{stamp}.zip')
    os.makedirs(os.path.dirname(zpath), exist_ok=True)
    with zipfile.ZipFile(zpath, 'x', zipfile.ZIP_DEFLATED) as z:
        for rel in novos:
            z.write(os.path.join(ROOT, rel), rel)
    print('\nBackup:', zpath)
    for rel, novo in novos.items():
        with open(os.path.join(ROOT, rel), 'wb') as f:
            f.write(novo)
    with zipfile.ZipFile(zpath) as z:
        for rel, novo in novos.items():
            antigo = z.read(rel)
            if aplicar(antigo, analisar(rel[:2], rel.split('/')[1], antigo)[0]) != novo:
                print('Conferência contra o backup FALHOU:', rel)
                sys.exit(1)
    print(f'Gravado: {len(novos)} páginas; conferido contra o backup.')


if __name__ == '__main__':
    main()
