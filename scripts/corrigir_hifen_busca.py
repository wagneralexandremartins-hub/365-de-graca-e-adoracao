"""Corrige os links quebrados (slugs com hífen) dos índices de busca.

Alvos: assets/js/nav.js (SEARCH_INDEX) e busca/index.html (BUSCA_INDEX).
Livros: tira o hífen do slug (pastas reais: 1samuel, 1reis, 1corintios...).
Personagens Davi, Salomão, Elias e Pedro: apontam para o perfil em /personagens/
(decisão do Wagner, 08/10/2026); se o perfil não existir, a entrada é removida.

Uso:
  python scripts/corrigir_hifen_busca.py           # dry-run (padrão)
  python scripts/corrigir_hifen_busca.py --apply   # grava, com backup zip em _backups/

Trabalha em bytes e preserva as quebras de linha. Prova: o resultado é
comparado com uma reconstrução independente a partir do original; só as
linhas previstas mudam, e só na url.
"""
import os
import sys
import time
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (título da entrada, url antiga, url nova)
LIVROS_NAV = [
    ("'1 Samuel'", '/03-historicos/1-samuel/index.html', '/03-historicos/1samuel/index.html'),
    ("'2 Samuel'", '/03-historicos/2-samuel/index.html', '/03-historicos/2samuel/index.html'),
    ("'1 Reis'", '/03-historicos/1-reis/index.html', '/03-historicos/1reis/index.html'),
    ("'2 Reis'", '/03-historicos/2-reis/index.html', '/03-historicos/2reis/index.html'),
    ("'1 Coríntios'", '/08-novo-testamento/1-corintios/index.html', '/08-novo-testamento/1corintios/index.html'),
    ("'2 Coríntios'", '/08-novo-testamento/2-corintios/index.html', '/08-novo-testamento/2corintios/index.html'),
    ("'1 Pedro'", '/08-novo-testamento/1-pedro/index.html', '/08-novo-testamento/1pedro/index.html'),
    ("'2 Pedro'", '/08-novo-testamento/2-pedro/index.html', '/08-novo-testamento/2pedro/index.html'),
    ("'1 João'", '/08-novo-testamento/1-joao/index.html', '/08-novo-testamento/1joao/index.html'),
]
LIVROS_BUSCA = [
    ("'1 Samuel'", '/03-historicos/1-samuel/index.html', '/03-historicos/1samuel/index.html'),
    ("'2 Samuel'", '/03-historicos/2-samuel/index.html', '/03-historicos/2samuel/index.html'),
    ("'1 Reis'", '/03-historicos/1-reis/index.html', '/03-historicos/1reis/index.html'),
    ("'2 Reis'", '/03-historicos/2-reis/index.html', '/03-historicos/2reis/index.html'),
    ("'Cântico dos Cânticos'", '/04-poeticos/cantico/index.html', '/04-poeticos/canticos/index.html'),
    ("'1 Coríntios'", '/08-novo-testamento/1-corintios/index.html', '/08-novo-testamento/1corintios/index.html'),
    ("'2 Coríntios'", '/08-novo-testamento/2-corintios/index.html', '/08-novo-testamento/2corintios/index.html'),
    ("'1 Pedro'", '/08-novo-testamento/1-pedro/index.html', '/08-novo-testamento/1pedro/index.html'),
]
PERSONAGENS_BUSCA = [
    ("'Davi'", '/03-historicos/1-samuel/index.html', '/personagens/davi.html'),
    ("'Salomão'", '/03-historicos/1-reis/index.html', '/personagens/salomao.html'),
    ("'Elias'", '/03-historicos/1-reis/index.html', '/personagens/elias.html'),
    ("'Pedro'", '/08-novo-testamento/1-pedro/index.html', '/personagens/pedro.html'),
]

# arquivo -> [(itens, separador depois de "title:", remover se o destino não existir)]
ALVOS = {
    'assets/js/nav.js': [(LIVROS_NAV, ' ', False)],
    'busca/index.html': [(LIVROS_BUSCA, '', False), (PERSONAGENS_BUSCA, '', True)],
}


def destino_existe(url):
    """Existe como arquivo e não é página de redirecionamento."""
    p = os.path.join(ROOT, url.lstrip('/'))
    if not os.path.isfile(p):
        return False
    return b'http-equiv="refresh"' not in open(p, 'rb').read().lower()


def planejar(arquivo, dados):
    """Devolve (trocas {linha: (velha, nova, título)}, remoções {linha: título}, falhas)."""
    linhas = dados.split(b'\n')
    trocas, remocoes, falhas = {}, {}, []
    for itens, sep, remover in ALVOS[arquivo]:
        for titulo, velha, nova in itens:
            chave = f'title:{sep}{titulo}'.encode('utf-8')
            vb = velha.encode('utf-8')
            achadas = [i for i, ln in enumerate(linhas, 1) if chave in ln and vb in ln]
            if len(achadas) != 1:
                falhas.append(f'{arquivo}: {titulo} — esperada 1 linha, achadas {len(achadas)}')
                continue
            n = achadas[0]
            if linhas[n - 1].count(vb) != 1:
                falhas.append(f'{arquivo}:{n}: url antiga aparece mais de 1× na linha')
            elif n in trocas or n in remocoes:
                falhas.append(f'{arquivo}:{n}: linha atingida por duas regras')
            elif destino_existe(nova):
                trocas[n] = (velha, nova, titulo)
            elif remover:
                remocoes[n] = titulo
            else:
                falhas.append(f'{arquivo}:{n}: destino não existe: {nova}')
    return trocas, remocoes, falhas


def aplicar_plano(dados, trocas, remocoes):
    saida = []
    for i, ln in enumerate(dados.split(b'\n'), 1):
        if i in remocoes:
            continue
        if i in trocas:
            velha, nova, _ = trocas[i]
            ln = ln.replace(velha.encode('utf-8'), nova.encode('utf-8'))
        saida.append(ln)
    return b'\n'.join(saida)


def provar(velho, novo, trocas, remocoes):
    """Reconstrução independente (por posição de byte) + checagens de contagem."""
    erros = []
    esperado = velho
    # aplica de trás para frente, por offset, para não deslocar as posições
    offsets, pos = {}, 0
    for i, ln in enumerate(velho.split(b'\n'), 1):
        offsets[i] = (pos, pos + len(ln))
        pos += len(ln) + 1
    for i in sorted(set(trocas) | set(remocoes), reverse=True):
        a, b = offsets[i]
        if i in remocoes:
            esperado = esperado[:a] + esperado[b + 1:]
        else:
            velha, nova, _ = trocas[i]
            k = esperado.index(velha.encode('utf-8'), a, b)
            esperado = esperado[:k] + nova.encode('utf-8') + esperado[k + len(velha.encode('utf-8')):]
    if esperado != novo:
        erros.append('resultado difere da reconstrução independente')
    if not remocoes:
        lv, ln_ = velho.split(b'\n'), novo.split(b'\n')
        mudadas = sorted(i for i, (x, y) in enumerate(zip(lv, ln_), 1) if x != y)
        if mudadas != sorted(trocas):
            erros.append(f'linhas alteradas {mudadas} ≠ previstas {sorted(trocas)}')
    if novo.count(b'\n') != velho.count(b'\n') - len(remocoes):
        erros.append('contagem de LF mudou além do previsto')
    rem_crlf = sum(1 for i in remocoes if velho.split(b'\n')[i - 1].endswith(b'\r'))
    if novo.count(b'\r\n') != velho.count(b'\r\n') - rem_crlf:
        erros.append('contagem de CRLF mudou além do previsto')
    return erros


def main():
    gravar = '--apply' in sys.argv
    print('Modo:', 'APLICAR' if gravar else 'SIMULAÇÃO (dry-run)')
    print()
    resultados, falhas = {}, []
    for arquivo in ALVOS:
        velho = open(os.path.join(ROOT, arquivo), 'rb').read()
        trocas, remocoes, f = planejar(arquivo, velho)
        falhas += f
        novo = aplicar_plano(velho, trocas, remocoes)
        resultados[arquivo] = (velho, novo, trocas, remocoes)
        for n in sorted(set(trocas) | set(remocoes)):
            if n in trocas:
                velha, nova, titulo = trocas[n]
                print(f'{arquivo:18s} linha {n:4d}  {titulo:24s} {velha:44s} -> {nova}  [destino existe]')
            else:
                print(f'{arquivo:18s} linha {n:4d}  {remocoes[n]:24s} REMOVER entrada (perfil não existe)')
    print()
    for arquivo, (velho, novo, trocas, remocoes) in resultados.items():
        erros = provar(velho, novo, trocas, remocoes)
        falhas += [f'{arquivo}: {e}' for e in erros]
        crlf_v, crlf_n = velho.count(b'\r\n'), novo.count(b'\r\n')
        print(f'Prova {arquivo}: {len(trocas)} trocas, {len(remocoes)} remoções, '
              f'bytes {len(velho)} -> {len(novo)} ({len(novo) - len(velho):+d}), '
              f'CRLF {crlf_v} -> {crlf_n}: {"OK" if not erros else "FALHOU"}')
    if falhas:
        for f in falhas:
            print('FALHA:', f)
        print('\nNada gravado.')
        sys.exit(1)
    if not gravar:
        print('\nDry-run: nada gravado. Rode com --apply para gravar.')
        return
    stamp = time.strftime('%Y%m%d-%H%M%S')
    zpath = os.path.join(ROOT, '_backups', f'hifen-busca-{stamp}.zip')
    os.makedirs(os.path.dirname(zpath), exist_ok=True)
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for arquivo, (velho, _, _, _) in resultados.items():
            z.writestr(arquivo, velho)
    for arquivo, (_, novo, _, _) in resultados.items():
        open(os.path.join(ROOT, arquivo), 'wb').write(novo)
    print(f'\nGravado. Backup: {os.path.relpath(zpath, ROOT)}')


if __name__ == '__main__':
    main()
