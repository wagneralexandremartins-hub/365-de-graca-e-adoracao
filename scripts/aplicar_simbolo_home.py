"""Símbolo da Graça girando em 3D na home (aprovado pelo Wagner em 09/10/2026, a partir de
redesign/preview-simbolo-3d.html: 12 s por volta, 220 px no desktop, 140 px no celular, disco
escuro e halo atuais, acima do cartão "Continue de onde parou").

O que muda (só a home):
  1. NOVO assets/img/simbolo-365-anel.webp — cópia byte a byte de redesign/simbolo-365-anel.webp
     (anel "365" recortado de assets/img/logo-365-graca-adoracao.png, 440×440, WebP).
     O original logo-365-graca-adoracao.png NÃO é tocado (SHA-256 conferido antes e depois).
  2. NOVO assets/css/simbolo-3d.css — o CSS do símbolo (CSS puro, sem JavaScript), CRLF como site.css.
  3. index.html — SÓ inserções, nenhum byte existente muda:
     a) uma linha <link> para simbolo-3d.css logo abaixo da linha do site.css;
     b) antes de <aside class="resume">: abre <div class="hero-lado"> e insere o bloco do símbolo;
     c) depois do </aside> do cartão: fecha o </div>.
Nenhum texto editorial é tocado.

Uso:
  python scripts/aplicar_simbolo_home.py           # simulação (padrão)
  python scripts/aplicar_simbolo_home.py --apply   # grava, com backup zip em _backups/

Prova: removendo os 3 trechos inseridos, o index.html volta a ser idêntico ao original;
quebras de linha CRLF em tudo o que entra; arquivos novos não existiam (abertos com 'xb');
o .webp copiado tem o mesmo SHA-256 da prévia; o PNG original tem o mesmo SHA-256 antes e depois.
"""
import hashlib
import os
import sys
import time
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = 'index.html'
ORIGINAL = 'assets/img/logo-365-graca-adoracao.png'
ORIGEM_WEBP = 'redesign/simbolo-365-anel.webp'
DESTINO_WEBP = 'assets/img/simbolo-365-anel.webp'
CSS = 'assets/css/simbolo-3d.css'
NL = b'\r\n'

ANCORA_LINK = b'  <link rel="stylesheet" href="/assets/css/site.css">' + NL
LINK = b'  <link rel="stylesheet" href="/assets/css/simbolo-3d.css">' + NL
ANCORA_ASIDE = b'        <aside class="resume" aria-labelledby="resume-title">' + NL
FIM_ASIDE = b'        </aside>' + NL

_img = '              <img class="{c}" src="/assets/img/simbolo-365-anel.webp" width="440" height="440" alt="" decoding="async">'
ABRE = NL.join(l.encode() for l in [
    '        <div class="hero-lado">',
    '          <!-- Símbolo da Graça girando (assets/css/simbolo-3d.css); decorativo: o nome já está no menu -->',
    '          <div class="simbolo3d" aria-hidden="true">',
    '            <div class="moeda">',
    *[_img.format(c=c) for c in ('borda b7', 'borda b6', 'borda b5', 'borda b4', 'borda b3',
                                 'borda b2', 'borda b1', 'verso', 'frente')],
    '            </div>',
    '          </div>',
]) + NL
FECHA = b'        </div>' + NL

CSS_TXT = """/* ==========================================================================
   Símbolo da Graça girando em 3D — só na home (index.html), 09/10/2026
   CSS puro (perspective + rotateY), sem JavaScript. Prévia aprovada:
   redesign/preview-simbolo-3d.html. Imagem: /assets/img/simbolo-365-anel.webp
   (anel "365" recortado de logo-365-graca-adoracao.png, 440×440).
   ========================================================================== */

/* coluna da direita do hero: símbolo acima do cartão "Continue de onde parou" */
.hero-lado { display: flex; flex-direction: column; align-items: center; gap: 34px; min-width: 0; }
.hero-lado .resume { width: 100%; }

.simbolo3d {
  --tam: 220px;          /* tamanho no desktop */
  --volta: 12s;          /* duração de uma volta */
  --brilho: 0.38;        /* intensidade do halo âmbar */
  --espessura: 1.6px;    /* distância entre as camadas da borda da "moeda" */
  position: relative;
  width: var(--tam); height: var(--tam);   /* tamanho fixo: não desloca o layout */
  perspective: 900px;
  flex: none;
}
/* halo e sombra ficam FORA do elemento 3D (filter em preserve-3d achataria o giro) */
.simbolo3d::before {
  content: ""; position: absolute; inset: -18%;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(242, 169, 59, var(--brilho)) 0%, rgba(224, 144, 31, calc(var(--brilho) * 0.4)) 38%, transparent 68%);
  filter: blur(6px);
  pointer-events: none;
}
.simbolo3d::after {
  content: ""; position: absolute; left: 18%; right: 18%; bottom: -10%; height: 9%;
  border-radius: 50%;
  background: radial-gradient(ellipse, rgba(0, 0, 0, 0.55), transparent 70%);
  pointer-events: none;
}
.simbolo3d .moeda {
  position: absolute; inset: 0;
  transform-style: preserve-3d;
  animation: simbolo-gira var(--volta) linear infinite;
}
.simbolo3d img {
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  -webkit-mask-image: radial-gradient(closest-side, #000 80%, transparent 100%);
          mask-image: radial-gradient(closest-side, #000 80%, transparent 100%);
  user-select: none; -webkit-user-drag: none;
}
/* frente e verso: cada um só aparece do seu lado; o verso é girado 180° para o "365" não ficar espelhado */
.simbolo3d .frente { transform: translateZ(calc(var(--espessura) * 4)); backface-visibility: hidden; }
.simbolo3d .verso  { transform: rotateY(180deg) translateZ(calc(var(--espessura) * 4)); backface-visibility: hidden; }
/* camadas internas: formam a "borda" da moeda quando ela fica de perfil */
.simbolo3d .borda { filter: brightness(0.45) saturate(1.2); }
.simbolo3d .b1 { transform: translateZ(calc(var(--espessura) *  3)); }
.simbolo3d .b2 { transform: translateZ(calc(var(--espessura) *  2)); }
.simbolo3d .b3 { transform: translateZ(calc(var(--espessura) *  1)); }
.simbolo3d .b4 { transform: translateZ(0); }
.simbolo3d .b5 { transform: translateZ(calc(var(--espessura) * -1)); }
.simbolo3d .b6 { transform: translateZ(calc(var(--espessura) * -2)); }
.simbolo3d .b7 { transform: translateZ(calc(var(--espessura) * -3)); }

@keyframes simbolo-gira {
  from { transform: rotateY(0deg); }
  to   { transform: rotateY(360deg); }
}
@media (max-width: 600px) {
  .simbolo3d { --tam: 140px; --espessura: 1.1px; }
}
/* animação reduzida: parado, levemente de lado. "animation: none" é necessário porque a regra
   global do site.css só encurta a duração (0.001ms), o que num giro infinito não o pararia. */
@media (prefers-reduced-motion: reduce) {
  .simbolo3d .moeda { animation: none !important; transform: rotateY(-14deg); }
}
"""
CSS_BYTES = CSS_TXT.replace('\r\n', '\n').replace('\n', '\r\n').encode('utf-8')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def ler(rel):
    return open(os.path.join(ROOT, rel), 'rb').read()


def main():
    gravar = '--apply' in sys.argv
    print('Modo:', 'APLICAR' if gravar else 'SIMULAÇÃO (dry-run)')
    falhas = []
    sha_original = sha(ler(ORIGINAL))
    webp = ler(ORIGEM_WEBP)
    if webp[:4] != b'RIFF' or webp[8:12] != b'WEBP':
        falhas.append(f'{ORIGEM_WEBP}: não é WebP')
    for rel in (DESTINO_WEBP, CSS):
        if os.path.exists(os.path.join(ROOT, rel)):
            falhas.append(f'{rel}: já existe (não sobrescrevo)')

    v = ler(HOME)
    if v.count(b'\r\n') != v.count(b'\n'):
        falhas.append(f'{HOME}: não é 100% CRLF')
    for nome, a in (('link do site.css', ANCORA_LINK), ('<aside class="resume">', ANCORA_ASIDE)):
        if v.count(a) != 1:
            falhas.append(f'{HOME}: {nome} aparece {v.count(a)} vezes (esperado 1)')
    if b'simbolo3d' in v or b'simbolo-3d.css' in v:
        falhas.append(f'{HOME}: já tem o símbolo')
    if falhas:
        for f in falhas:
            print('FALHA:', f)
        print('\nNada gravado.')
        sys.exit(1)

    k1 = v.index(ANCORA_LINK) + len(ANCORA_LINK)
    k2 = v.index(ANCORA_ASIDE)
    k3 = v.index(FIM_ASIDE, k2) + len(FIM_ASIDE)
    novo = v[:k1] + LINK + v[k1:k2] + ABRE + v[k2:k3] + FECHA + v[k3:]

    # prova: tirando os 3 trechos, volta ao original
    j1 = k1
    j2 = k2 + len(LINK)
    j3 = k3 + len(LINK) + len(ABRE)
    assert novo[j1:j1 + len(LINK)] == LINK and novo[j2:j2 + len(ABRE)] == ABRE and novo[j3:j3 + len(FECHA)] == FECHA
    volta = novo[:j1] + novo[j1 + len(LINK):j2] + novo[j2 + len(ABRE):j3] + novo[j3 + len(FECHA):]
    inseridos = LINK + ABRE + FECHA
    ok = (volta == v and len(novo) - len(v) == len(inseridos)
          and novo.count(b'\r\n') == novo.count(b'\n')
          and novo.count(b'\n') - v.count(b'\n') == inseridos.count(b'\n')
          and novo.count(b'<div') - v.count(b'<div') == novo.count(b'</div>') - v.count(b'</div>')
          and CSS_BYTES.count(b'\r\n') == CSS_BYTES.count(b'\n'))

    print(f'\n{HOME}: {len(v)} -> {len(novo)} bytes (+{len(inseridos)}), {inseridos.count(NL)} linhas inseridas, 0 alteradas')
    for nome, pos, trecho in (('a) <head>', k1, LINK), ('b) antes do cartão', k2, ABRE), ('c) depois do cartão', k3, FECHA)):
        ln = v[:pos].count(b'\n') + 1
        print(f'\n  {nome} — antes da linha {ln}:')
        for l in trecho.decode().splitlines():
            print('    + ' + l[:118])
    print(f'\n{CSS}: novo, {len(CSS_BYTES)} bytes, {CSS_BYTES.count(NL)} linhas CRLF')
    print(f'{DESTINO_WEBP}: novo, cópia de {ORIGEM_WEBP} ({len(webp)} bytes, SHA-256 {sha(webp)[:16]}…)')
    print(f'{ORIGINAL}: SHA-256 {sha_original[:16]}… (não é tocado)')
    print('\n## Prova:', 'OK' if ok else 'FALHOU',
          '— index.html sem os 3 trechos = original byte a byte; CRLF; <div> abre e fecha em igual número')
    if not ok:
        print('Nada gravado.')
        sys.exit(1)
    if not gravar:
        print('\nDry-run: nada gravado. Rode com --apply para gravar.')
        return

    stamp = time.strftime('%Y%m%d-%H%M%S')
    zpath = os.path.join(ROOT, '_backups', f'simbolo-home-{stamp}.zip')
    os.makedirs(os.path.dirname(zpath), exist_ok=True)
    with zipfile.ZipFile(zpath, 'x', zipfile.ZIP_DEFLATED) as z:
        z.writestr(HOME, v)
        z.writestr('SHA256-originais.txt', f'{ORIGINAL} {sha_original}\n{HOME} {sha(v)}\n')
    print(f'\nBackup: {os.path.relpath(zpath, ROOT)}')
    with open(os.path.join(ROOT, DESTINO_WEBP), 'xb') as f:
        f.write(webp)
    with open(os.path.join(ROOT, CSS), 'xb') as f:
        f.write(CSS_BYTES)
    with open(os.path.join(ROOT, HOME), 'wb') as f:
        f.write(novo)
    # conferência depois de gravar
    with zipfile.ZipFile(zpath) as z:
        antigo = z.read(HOME)
    gravado = ler(HOME)
    ok2 = (gravado == novo and antigo == v
           and sha(ler(DESTINO_WEBP)) == sha(webp)
           and ler(CSS) == CSS_BYTES
           and sha(ler(ORIGINAL)) == sha_original)
    print('Conferência depois de gravar:', 'OK' if ok2 else 'FALHOU',
          f'— index.html, {DESTINO_WEBP} = prévia, {CSS}, {ORIGINAL} com o mesmo SHA-256')
    if not ok2:
        sys.exit(1)


if __name__ == '__main__':
    main()
