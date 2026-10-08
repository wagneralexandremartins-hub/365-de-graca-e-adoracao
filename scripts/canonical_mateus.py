"""SEO técnico 4, pré-requisito: canonical nas 28 páginas de capítulo de Mateus
(autorização do Wagner, 08/10/2026; formato sem .html, como os demais livros do NT).

Em cada 08-novo-testamento/mateus/capitulos/capitulo-NN.html (01 a 28), insere
UMA linha no <head>, logo abaixo do <meta name="description">, sem indentação
(como as demais linhas do <head> dessas páginas) e com a mesma quebra de linha:
  <link rel="canonical" href="https://365gracaeadoracao.com/08-novo-testamento/mateus/capitulos/capitulo-NN">
Nenhum texto editorial é tocado.

Uso:
  python scripts/canonical_mateus.py           # simulação (padrão)
  python scripts/canonical_mateus.py --apply   # grava, com backup zip em _backups/

Prova, por página: o novo é o antigo mais exatamente essa linha, no ponto
previsto; nenhum outro byte muda; CRLF/LF da linha igual ao do arquivo.
"""
import os
import re
import sys
import time
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA = '08-novo-testamento/mateus/capitulos'
URL = 'https://365gracaeadoracao.com/08-novo-testamento/mateus/capitulos/capitulo-%02d'
DESC_RE = re.compile(rb'^<meta name="description" content="[^"\r\n]*">[ \t]*(\r?\n)', re.M)


def quebra(linha):
    return 'CRLF' if linha.endswith(b'\r\n') else 'LF'


def main():
    gravar = '--apply' in sys.argv
    print('Modo:', 'APLICAR' if gravar else 'SIMULAÇÃO (dry-run)')
    novos, falhas = {}, []
    for n in range(1, 29):
        rel = f'{PASTA}/capitulo-{n:02d}.html'
        v = open(os.path.join(ROOT, rel), 'rb').read()
        if b'rel="canonical"' in v:
            falhas.append(f'{rel}: já tem canonical')
            continue
        if b'http-equiv="refresh"' in v.lower():
            falhas.append(f'{rel}: é redirect')
            continue
        head = v[:v.find(b'</head>')]
        ms = list(DESC_RE.finditer(head))
        if len(ms) != 1:
            falhas.append(f'{rel}: {len(ms)} linhas <meta name="description"> no formato esperado')
            continue
        m = re.search(rb'<title>([^<]*)</title>', head)
        if not m or not re.search(rb'Mateus %d(?!\d)' % n, m.group(1)):
            falhas.append(f'{rel}: título não confere com Mateus {n}')
            continue
        nl = ms[0].group(1)
        crlf_arq = v.count(b'\r\n') == v.count(b'\n')
        if (nl == b'\r\n') != crlf_arq:
            falhas.append(f'{rel}: quebra da linha de description ≠ do arquivo')
            continue
        linha = b'<link rel="canonical" href="' + (URL % n).encode() + b'">' + nl
        k = ms[0].end()
        novo = v[:k] + linha + v[k:]
        # prova
        if novo[:k] != v[:k] or novo[k + len(linha):] != v[k:] or len(novo) - len(v) != len(linha):
            falhas.append(f'{rel}: prova byte a byte falhou')
            continue
        if novo.count(b'\r\n') - v.count(b'\r\n') != (1 if nl == b'\r\n' else 0) or novo.count(b'\n') - v.count(b'\n') != 1:
            falhas.append(f'{rel}: quebras de linha mudaram além da linha nova')
            continue
        if novo.count(b'rel="canonical"') != 1:
            falhas.append(f'{rel}: canonical não é único')
            continue
        novos[rel] = (v, novo, linha, k)

    print(f'\nPáginas: {len(novos)} de 28 recebem 1 linha de canonical')
    tam = sorted({len(x[2]) for x in novos.values()})
    print(f'  bytes acrescentados por página: {tam}  |  quebra de linha: '
          f'{sorted({quebra(x[2]) for x in novos.values()})}')
    for rel in sorted(novos)[:1] + sorted(novos)[-1:]:
        v, novo, linha, k = novos[rel]
        ini = v.rfind(b'\n', 0, k - 1) + 1
        fim = novo.find(b'\n', k + len(linha)) + 1
        print(f'\n  {rel}  ({len(v)} -> {len(novo)} bytes)')
        print('    antes:')
        for l in v[ini:v.find(b'\n', k) + 1].splitlines():
            print('     | ' + l.decode()[:110])
        print('    depois:')
        for l in novo[ini:fim].splitlines():
            print('     ' + ('+' if l + b'\r\n' == linha or l + b'\n' == linha else '|') + ' ' + l.decode()[:110])
    print('\n## Prova')
    print(f'  {len(novos)}/28 OK: novo = antigo + exatamente a linha do canonical, após o <meta name="description">; '
          f'nenhum outro byte muda; CRLF preservado; 1 canonical por página; título confere com o capítulo')
    if falhas:
        for f in falhas:
            print('FALHA:', f)
        print('\nNada gravado.')
        sys.exit(1)
    if not gravar:
        print('\nDry-run: nada gravado. Rode com --apply para gravar.')
        return
    stamp = time.strftime('%Y%m%d-%H%M%S')
    zpath = os.path.join(ROOT, '_backups', f'canonical-mateus-{stamp}.zip')
    os.makedirs(os.path.dirname(zpath), exist_ok=True)
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for rel, (v, _, _, _) in novos.items():
            z.writestr(rel, v)
    for rel, (_, novo, _, _) in novos.items():
        open(os.path.join(ROOT, rel), 'wb').write(novo)
    print(f'\nGravado: {len(novos)} páginas. Backup: {os.path.relpath(zpath, ROOT)}')


if __name__ == '__main__':
    main()
