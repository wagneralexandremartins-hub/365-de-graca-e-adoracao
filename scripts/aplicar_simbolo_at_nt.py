"""Símbolo da Graça girando em 3D no topo dos índices do Antigo e do Novo Testamento
(pedido do Wagner em 09/10/2026), reaproveitando o que já está no ar na home:
assets/css/simbolo-3d.css e assets/img/simbolo-365-anel.webp. Nenhum arquivo novo.

Páginas (6): os índices de testamento em PT, EN e ES.
  PT: antigo-testamento/index.html, 08-novo-testamento/index.html   (hero .page-hero.hub-hero, alinhado à esquerda)
  EN: en/old-testament/index.html, en/index.html (NT)                 (hero .lang-hero, centralizado)
  ES: es/antiguo-testamento/index.html, es/index.html (NT)
Índices de livro e páginas de capítulo NÃO entram.

O que muda — SÓ inserções, nenhum byte existente muda:
  1. assets/css/simbolo-3d.css: um bloco de regras acrescentado NO FIM (as regras da home ficam iguais).
  2. Em cada página:
     a) uma linha <link> para simbolo-3d.css logo abaixo do link do site.css (PT) ou do bloco.css (EN/ES);
     b) o bloco do símbolo (o mesmo da home: 9 <img> da mesma imagem, aria-hidden) logo depois de
        <div class="wrap"> do hero (PT) ou de <div class="lang-hero"> (EN/ES).
Posição: no desktop, à direita do hero, centrado na altura, em position: absolute (não empurra nada);
até 1100 px, vai para o canto superior direito do hero, pequeno, também absolute.

Uso:
  python scripts/aplicar_simbolo_at_nt.py           # simulação (padrão)
  python scripts/aplicar_simbolo_at_nt.py --apply   # grava, com backup zip em _backups/

Prova: em cada arquivo, removendo os trechos inseridos, volta ao original byte a byte; CRLF.
"""
import hashlib
import os
import sys
import time
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = b'\r\n'
CSS = 'assets/css/simbolo-3d.css'
IMG = 'assets/img/simbolo-365-anel.webp'

PT_LINK = b'  <link rel="stylesheet" href="/assets/css/site.css">' + NL
PT_HERO = b'    <section class="section page-hero hub-hero">' + NL + b'      <div class="wrap">' + NL
EX_LINK = b'<link rel="stylesheet" href="/assets/css/bloco.css">' + NL
EX_HERO = b'<div class="lang-hero">' + NL

PAGINAS = [
    # (arquivo, âncora do link, linha nova do link, âncora do hero, recuo do bloco)
    ('antigo-testamento/index.html', PT_LINK, b'  <link rel="stylesheet" href="/assets/css/simbolo-3d.css">' + NL, PT_HERO, '        '),
    ('08-novo-testamento/index.html', PT_LINK, b'  <link rel="stylesheet" href="/assets/css/simbolo-3d.css">' + NL, PT_HERO, '        '),
    ('en/old-testament/index.html', EX_LINK, b'<link rel="stylesheet" href="/assets/css/simbolo-3d.css">' + NL, EX_HERO, '  '),
    ('en/index.html', EX_LINK, b'<link rel="stylesheet" href="/assets/css/simbolo-3d.css">' + NL, EX_HERO, '  '),
    ('es/antiguo-testamento/index.html', EX_LINK, b'<link rel="stylesheet" href="/assets/css/simbolo-3d.css">' + NL, EX_HERO, '  '),
    ('es/index.html', EX_LINK, b'<link rel="stylesheet" href="/assets/css/simbolo-3d.css">' + NL, EX_HERO, '  '),
]


def bloco(r):
    img = r + '    <img class="{c}" src="/assets/img/simbolo-365-anel.webp" width="440" height="440" alt="" decoding="async">'
    linhas = [r + '<!-- Símbolo da Graça girando (assets/css/simbolo-3d.css); decorativo -->',
              r + '<div class="simbolo3d" aria-hidden="true">',
              r + '  <div class="moeda">',
              *[img.format(c=c) for c in ('borda b7', 'borda b6', 'borda b5', 'borda b4', 'borda b3',
                                          'borda b2', 'borda b1', 'verso', 'frente')],
              r + '  </div>',
              r + '</div>']
    return NL.join(l.encode('utf-8') for l in linhas) + NL


CSS_NOVO = """
/* ==========================================================================
   Índices do Antigo e do Novo Testamento (09/10/2026)
   PT: hero .page-hero.hub-hero (alinhado à esquerda); EN/ES: hero .lang-hero (centralizado).
   O símbolo fica em position: absolute — não empurra o conteúdo em nenhuma largura.
   ========================================================================== */
.page-hero.hub-hero > .wrap,
.lang-hero { position: relative; }
.page-hero.hub-hero > .wrap > .simbolo3d,
.lang-hero > .simbolo3d {
  position: absolute; top: 50%; right: 4%;
  margin: calc(var(--tam) / -2) 0 0;
}
.page-hero.hub-hero > .wrap > .simbolo3d { --tam: 220px; }
.lang-hero > .simbolo3d { --tam: 180px; --espessura: 1.3px; }
/* até 1100 px o texto ocupa a largura: o símbolo vai pequeno para o canto superior direito do hero */
@media (max-width: 1100px) {
  .page-hero.hub-hero > .wrap > .simbolo3d,
  .lang-hero > .simbolo3d { --tam: 60px; --espessura: 0.5px; --brilho: 0.3; top: 0; right: 0; margin: 0; }
  .lang-hero > .simbolo3d { right: 1rem; --tam: 48px; }
}
"""
CSS_BLOCO = CSS_NOVO.replace('\n', '\r\n').encode('utf-8')


def ler(rel):
    return open(os.path.join(ROOT, rel), 'rb').read()


def main():
    gravar = '--apply' in sys.argv
    print('Modo:', 'APLICAR' if gravar else 'SIMULAÇÃO (dry-run)')
    falhas, novos = [], {}
    sha_img = hashlib.sha256(ler(IMG)).hexdigest()

    # CSS: acrescentar no fim
    css = ler(CSS)
    if b'Antigo e do Novo Testamento' in css:
        falhas.append(f'{CSS}: já tem o bloco dos testamentos')
    elif not css.endswith(b'}' + NL):
        falhas.append(f'{CSS}: não termina em "}}" + CRLF')
    else:
        novo = css + CSS_BLOCO
        ok = (novo[:len(css)] == css and novo.count(b'\r\n') == novo.count(b'\n'))
        if ok:
            novos[CSS] = (css, novo, [(len(css), CSS_BLOCO)])
        else:
            falhas.append(f'{CSS}: prova falhou')

    for rel, ancora_link, link, ancora_hero, recuo in PAGINAS:
        v = ler(rel)
        if v.count(b'\r\n') != v.count(b'\n'):
            falhas.append(f'{rel}: não é 100% CRLF'); continue
        if b'simbolo3d' in v or b'simbolo-3d.css' in v:
            falhas.append(f'{rel}: já tem o símbolo'); continue
        if b'http-equiv="refresh"' in v.lower():
            falhas.append(f'{rel}: é redirect'); continue
        if v.count(ancora_link) != 1 or v.count(ancora_hero) != 1:
            falhas.append(f'{rel}: âncoras encontradas link={v.count(ancora_link)} hero={v.count(ancora_hero)} (esperado 1 e 1)'); continue
        k1 = v.index(ancora_link) + len(ancora_link)
        k2 = v.index(ancora_hero) + len(ancora_hero)
        if not k1 < k2:
            falhas.append(f'{rel}: link do CSS depois do hero'); continue
        b = bloco(recuo)
        novo = v[:k1] + link + v[k1:k2] + b + v[k2:]
        volta = novo[:k1] + novo[k1 + len(link):k2 + len(link)] + novo[k2 + len(link) + len(b):]
        ok = (volta == v and len(novo) - len(v) == len(link) + len(b)
              and novo.count(b'\r\n') == novo.count(b'\n')
              and novo.count(b'<div') - v.count(b'<div') == novo.count(b'</div>') - v.count(b'</div>') == 2)
        if not ok:
            falhas.append(f'{rel}: prova falhou'); continue
        novos[rel] = (v, novo, [(k1, link), (k2, b)])

    print(f'\nArquivos que mudam: {len(novos)} (1 CSS + {len(novos) - 1 if CSS in novos else len(novos)} páginas); nenhum arquivo novo')
    for rel, (v, novo, ins) in novos.items():
        n_lin = sum(t.count(NL) for _, t in ins)
        print(f'  {rel}: {len(v)} -> {len(novo)} bytes, +{n_lin} linhas, 0 alteradas')
    exemplo = next((r for r in novos if r != CSS), None)
    if exemplo:
        v, novo, ins = novos[exemplo]
        print(f'\nExemplo — {exemplo}:')
        for pos, t in ins:
            print(f'  antes da linha {v[:pos].count(b"\n") + 1}:')
            for l in t.decode().splitlines()[:4] + (['    …'] if t.count(NL) > 4 else []):
                print('    + ' + l[:116])
    print(f'\n{CSS} — bloco acrescentado no fim ({CSS_BLOCO.count(NL)} linhas):')
    for l in CSS_NOVO.strip('\n').splitlines():
        print('    + ' + l)
    print(f'\n{IMG}: reaproveitada, não muda (SHA-256 {sha_img[:16]}…)')
    if falhas:
        for f in falhas:
            print('FALHA:', f)
        print('\nNada gravado.')
        sys.exit(1)
    print('\n## Prova: OK — cada arquivo sem os trechos inseridos = original byte a byte; CRLF; <div> 2 abertos e 2 fechados por página')
    if not gravar:
        # --saida PASTA: grava as versões simuladas numa pasta FORA do repositório (para prévia visual)
        if '--saida' in sys.argv:
            saida = os.path.abspath(sys.argv[sys.argv.index('--saida') + 1])
            if os.path.commonpath([saida, ROOT]) == ROOT:
                print('FALHA: --saida não pode ficar dentro do repositório'); sys.exit(1)
            for rel, (_, novo, _) in novos.items():
                os.makedirs(os.path.dirname(os.path.join(saida, rel)), exist_ok=True)
                with open(os.path.join(saida, rel), 'wb') as f:
                    f.write(novo)
            print(f'\nPrévia simulada gravada fora do repositório: {saida}')
        print('\nDry-run: nada gravado no repositório. Rode com --apply para gravar.')
        return

    stamp = time.strftime('%Y%m%d-%H%M%S')
    zpath = os.path.join(ROOT, '_backups', f'simbolo-at-nt-{stamp}.zip')
    os.makedirs(os.path.dirname(zpath), exist_ok=True)
    with zipfile.ZipFile(zpath, 'x', zipfile.ZIP_DEFLATED) as z:
        for rel, (v, _, _) in novos.items():
            z.writestr(rel, v)
    print(f'\nBackup: {os.path.relpath(zpath, ROOT)}')
    for rel, (_, novo, _) in novos.items():
        with open(os.path.join(ROOT, rel), 'wb') as f:
            f.write(novo)
    with zipfile.ZipFile(zpath) as z:
        ok2 = all(z.read(rel) == v and ler(rel) == novo for rel, (v, novo, _) in novos.items())
    ok2 = ok2 and hashlib.sha256(ler(IMG)).hexdigest() == sha_img
    print('Conferência depois de gravar:', 'OK' if ok2 else 'FALHOU', f'— {len(novos)} arquivos contra o backup; imagem inalterada')
    if not ok2:
        sys.exit(1)


if __name__ == '__main__':
    main()
