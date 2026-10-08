"""SEO técnico 4: hreflang entre PT, EN e ES (skill seo-limpeza, regra de 08/10/2026).

Regra: um alternate só fica se aponta para página que existe, sem redirect,
equivalente (mesmo livro e capítulo), com a URL IGUAL ao canonical do alvo,
e se o alvo declara a volta. Na dúvida, o alternate sai.

Sub-etapas (todas no mesmo passe, contadas em separado):
  H1  corrige o href de alternates de EN/ES para a URL canônica do equivalente
      (pt-BR com forma antiga ou nome de livro em inglês; es/en trocados).
  H2  remove de EN/ES os alternates sem equivalente seguro (linha inteira).
  H3  insere nas páginas PT o bloco de volta (pt-BR, en, es), logo abaixo do
      <link rel="canonical">, com a mesma indentação e a mesma quebra de linha.

Uso:
  python scripts/hreflang_item4.py           # simulação (padrão)
  python scripts/hreflang_item4.py --apply   # grava, com backup zip em _backups/

Prova, por arquivo: tirando todas as linhas de hreflang, antigo e novo são
idênticos byte a byte; CRLF/LF de cada linha nova igual à do canonical; e o
estado final inteiro (todas as páginas) é revalidado pela regra acima.
"""
import collections
import os
import re
import sys
import time
import zipfile

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sitemap_canonical import ROOT, DOMINIO, arquivo_de, canonical_de, forma  # noqa: E402

EXCLUIR = {'_backups', 'redesign', 'scripts', '.claude', '.github', '.git', '_site', 'node_modules'}
ALT_RE = re.compile(rb'^([ \t]*)<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"\s*/?>[ \t]*(\r?\n)', re.M)
CANON_LINHA_RE = re.compile(rb'^([ \t]*)<link rel="canonical" href="([^"]+)">[ \t]*(\r?\n)', re.M)
CAP_RE = re.compile(r'^/(0\d-[^/]+)/([^/]+)/capitulo-(\d+)/?$')
NT_RE = re.compile(r'^/08-novo-testamento/([^/]+)/capitulos/capitulo-(\d+)$')
LIVRO_NT_EN = {'matthew': 'mateus', 'romans': 'romanos', 'revelation': 'apocalipse'}
ORDEM = ['pt-BR', 'en', 'es']
# Escopo: páginas de capítulo EN/ES (en/<livro>-N/, es/<libro>-N/). Home, estudos e
# índices EN/ES com hreflang ficam como estão e só entram na revalidação.
ESCOPO_RE = re.compile(r'^(en|es)/[a-z0-9]+-\d+/index\.html$')


def lingua(rel):
    return {'en': 'en', 'es': 'es'}.get(rel.split('/')[0], 'pt-BR')


def paginas():
    for dp, dns, fns in os.walk(ROOT):
        rel = os.path.relpath(dp, ROOT).replace(os.sep, '/')
        if rel.split('/')[0] in EXCLUIR:
            dns[:] = []
            continue
        for fn in fns:
            if fn.endswith('.html'):
                yield ('' if rel == '.' else rel + '/') + fn


_dados, _canon = {}, {}


def ler(rel):
    if rel not in _dados:
        _dados[rel] = open(os.path.join(ROOT, rel), 'rb').read()
    return _dados[rel]


def redirect(rel):
    return b'http-equiv="refresh"' in ler(rel).lower()


def canon_ok(rel):
    """URL canônica utilizável da página, ou None."""
    if rel not in _canon:
        can, erro = canonical_de(rel)
        ok = (not erro and can.startswith(DOMINIO + '/') and not can.endswith('.html')
              and arquivo_de(can) == rel and forma(can) != 'pasta (sem barra)')
        _canon[rel] = can if ok else None
    return _canon[rel]


def real(url):
    rel = arquivo_de(url)
    return rel if rel and not redirect(rel) else None


def numero_no_titulo(rel, n):
    m = re.search(rb'<title>([^<]*)</title>', ler(rel))
    return bool(m and re.search(rb'(?<!\d)0*%d(?!\d)' % n, m.group(1)))


def candidato_pt(href):
    """(arquivo PT equivalente, motivo) para um pt-BR que hoje não serve."""
    p = '/' + href.split('://', 1)[-1].split('/', 1)[-1]
    m = NT_RE.match(p)
    if m and m[1] in LIVRO_NT_EN:
        cands, n = [f'08-novo-testamento/{LIVRO_NT_EN[m[1]]}/capitulos/capitulo-{m[2]}.html'], int(m[2])
        motivo = 'nome de livro em inglês'
    else:
        m = CAP_RE.match(p)
        if not m:
            return None, 'formato sem regra'
        n = int(m[3])
        cands = [f'{m[1]}/{m[2]}/capitulos/capitulo-{n:02d}.html',
                 f'{m[1]}/{m[2]}/capitulos/salmo-{n:03d}.html']
        motivo = 'forma antiga /livro/capitulo-N/'
    for c in cands:
        if os.path.isfile(os.path.join(ROOT, c)) and not redirect(c):
            if not numero_no_titulo(c, n):
                return None, f'candidato {c} sem o capítulo {n} no título'
            return c, motivo
    return None, 'sem página PT equivalente: ' + '/'.join(p.split('/')[1:3])


def main():
    gravar = '--apply' in sys.argv
    print('Modo:', 'APLICAR' if gravar else 'SIMULAÇÃO (dry-run)')
    todas = [p for p in paginas() if not redirect(p)]
    alts = {}                                    # rel -> [match]
    for p in todas:
        d = ler(p)
        ms = list(ALT_RE.finditer(d))
        if d.count(b'hreflang') != len(ms):
            print(f'FALHA: {p}: hreflang fora do formato de linha esperado')
            sys.exit(1)
        if ms:
            alts[p] = ms

    # ---- Decisão por alternate de EN/ES --------------------------------------
    acao = {}                                    # (rel, idx) -> ('ok'|'h1'|'h2', novo_href, motivo)
    pend = collections.defaultdict(list)
    alvo_pt = collections.defaultdict(list)      # arquivo PT -> [rel EN/ES]
    for p, ms in alts.items():
        lp = lingua(p)
        if not ESCOPO_RE.match(p):
            continue
        cp = canon_ok(p)
        for i, m in enumerate(ms):
            lg, href = m.group(2).decode(), m.group(3).decode()
            if cp is None:
                acao[(p, i)] = ('h2', None, 'página de origem sem canonical utilizável')
                continue
            if lg == lp:
                acao[(p, i)] = ('ok', href, '') if href == cp else ('h1', cp, 'auto-referência ≠ canonical')
                continue
            t = real(href)
            if lg == 'pt-BR':
                motivo = ''
                if t is None:
                    t, motivo = candidato_pt(href)
                if t is None:
                    acao[(p, i)] = ('h2', None, motivo)
                elif canon_ok(t) is None:
                    acao[(p, i)] = ('h2', None, f'alvo PT sem canonical: {t}')
                else:
                    alvo_pt[t].append(p)
                    acao[(p, i)] = ('ok', href, '') if href == canon_ok(t) else ('h1', canon_ok(t), motivo or 'href ≠ canonical do alvo')
            else:                                # en <-> es
                if t is None or canon_ok(t) is None or lingua(t) != lg:
                    # procura a página que aponta de volta para esta
                    volta = [q for q, qms in alts.items() if lingua(q) == lg and canon_ok(q)
                             and any(x.group(2).decode() == lp and x.group(3).decode() == cp for x in qms)]
                    if len(volta) == 1:
                        acao[(p, i)] = ('h1', canon_ok(volta[0]), 'nome de livro em inglês (EN→ES)')
                    else:
                        acao[(p, i)] = ('h2', None, f'{lg} inexistente e sem página recíproca única')
                else:
                    acao[(p, i)] = ('ok', href, '') if href == canon_ok(t) else ('h1', canon_ok(t), 'href ≠ canonical do alvo')

    # Equivalência 1:1 — um PT por EN e um por ES
    for t, ps in alvo_pt.items():
        por_l = collections.Counter(lingua(x) for x in ps)
        if any(n > 1 for n in por_l.values()):
            for x in ps:
                for i, m in enumerate(alts[x]):
                    if m.group(2) == b'pt-BR':
                        acao[(x, i)] = ('h2', None, f'{t} disputado por {sorted(ps)}')
            alvo_pt[t] = []

    # ---- Estado final desejado por página ------------------------------------
    final = {}                                   # rel -> {lang: url}
    for p, ms in alts.items():
        if not ESCOPO_RE.match(p):
            continue
        final[p] = {}
        for i, m in enumerate(ms):
            tipo, novo, _ = acao[(p, i)]
            if tipo != 'h2':
                final[p][m.group(2).decode()] = novo
    # en<->es só fica se o outro lado declara a volta
    for p in list(final):
        for lg in ('en', 'es'):
            if lg == lingua(p) or lg not in final[p]:
                continue
            q = arquivo_de(final[p][lg])
            if final.get(q, {}).get(lingua(p)) != canon_ok(p):
                del final[p][lg]
                for i, m in enumerate(alts[p]):
                    if m.group(2).decode() == lg:
                        acao[(p, i)] = ('h2', None, 'en/es sem reciprocidade')
    # H3: bloco de volta nas páginas PT
    h3 = {}
    for t, ps in alvo_pt.items():
        ps = [x for x in ps if final.get(x, {}).get('pt-BR') == canon_ok(t)]
        if not ps:
            continue
        bloco = {'pt-BR': canon_ok(t)}
        for x in ps:
            bloco[lingua(x)] = canon_ok(x)
        if t in alts:                            # já tem hreflang
            atual = {m.group(2).decode(): m.group(3).decode() for m in alts[t]}
            if atual != bloco:
                pend['página PT já tem hreflang diferente do desejado'].append(t)
                for x in ps:
                    for i, m in enumerate(alts[x]):
                        if m.group(2) == b'pt-BR':
                            acao[(x, i)] = ('h2', None, f'{t} já tem hreflang diferente')
                            final[x].pop('pt-BR', None)
            continue
        h3[t] = bloco
    for p in final:                              # se só sobrou a auto-referência, ela sai também
        if set(final[p]) <= {lingua(p)}:
            for i, m in enumerate(alts[p]):
                if acao[(p, i)][0] != 'h2':
                    acao[(p, i)] = ('h2', None, 'sobrou só a auto-referência')
            final[p] = {}

    # ---- Monta os arquivos novos ---------------------------------------------
    novos = {}
    for p, ms in alts.items():
        if not ESCOPO_RE.match(p):
            continue
        d, partes, pos, mudou = ler(p), [], 0, False
        for i, m in enumerate(ms):
            tipo, novo, _ = acao[(p, i)]
            if tipo == 'ok':
                continue
            mudou = True
            partes.append(d[pos:m.start()])
            if tipo == 'h1':
                partes.append(d[m.start():m.start(3)] + novo.encode() + d[m.end(3):m.end()])
            pos = m.end()
        if mudou:
            partes.append(d[pos:])
            novos[p] = b''.join(partes)
    falhas = []
    for t, bloco in h3.items():
        d = ler(t)
        cs = list(CANON_LINHA_RE.finditer(d))
        if len(cs) != 1:
            falhas.append(f'{t}: {len(cs)} linhas de canonical no formato esperado')
            continue
        ind, nl = cs[0].group(1), cs[0].group(3)
        linhas = b''.join(ind + b'<link rel="alternate" hreflang="%s" href="%s">' % (lg.encode(), bloco[lg].encode()) + nl
                          for lg in ORDEM if lg in bloco)
        novos[t] = d[:cs[0].end()] + linhas + d[cs[0].end():]

    # ---- Prova ----------------------------------------------------------------
    sem_alt = lambda b: ALT_RE.sub(b'', b)
    for p, n in novos.items():
        v = ler(p)
        if sem_alt(v) != sem_alt(n):
            falhas.append(f'{p}: mudou algo além das linhas de hreflang')
        nl_v = len(ALT_RE.findall(v)) - len(ALT_RE.findall(n))
        if v.count(b'\n') - n.count(b'\n') != nl_v:
            falhas.append(f'{p}: contagem de linhas inconsistente')
        crlf = v.count(b'\r\n') > 0
        if any((m.group(4) == b'\r\n') != crlf for m in ALT_RE.finditer(n)) and p in h3:
            falhas.append(f'{p}: quebra de linha das linhas novas ≠ do arquivo')
    # Revalida o estado final inteiro
    estado = {p: {m.group(2).decode(): m.group(3).decode() for m in ALT_RE.finditer(novos.get(p, ler(p)))}
              for p in set(alts) | set(novos)}
    erros_fim = collections.Counter()
    exemplos_fim = {}
    for p, mp in estado.items():
        for lg, url in mp.items():
            t = real(url)
            if t is None:
                e = 'alvo 404/redirect'
            elif canon_ok(t) != url:
                e = 'URL ≠ canonical do alvo'
            elif lingua(t) != lg:
                e = 'idioma do alvo ≠ hreflang'
            elif t != p and estado.get(t, {}).get(lingua(p)) != canon_ok(p):
                e = 'sem reciprocidade'
            elif t == p and url != canon_ok(p):
                e = 'auto-referência ≠ canonical'
            else:
                continue
            grupo = 'no escopo' if ESCOPO_RE.match(p) or p in h3 else 'fora do escopo (não editada)'
            erros_fim[(grupo, e)] += 1
            exemplos_fim.setdefault((grupo, e), (p, lg, url))

    # ---- Relatório ------------------------------------------------------------
    cont = collections.Counter()
    exs = {}
    for (p, i), (tipo, novo, motivo) in acao.items():
        m = alts[p][i]
        k = (tipo, lingua(p), m.group(2).decode(), motivo)
        cont[k] += 1
        exs.setdefault(k, (p, m.group(3).decode(), novo))
    tot = collections.Counter(k[0] for k in cont.elements())
    origem = [p for p in alts if ESCOPO_RE.match(p)]
    print(f'\nPáginas EN/ES com hreflang: {len(origem)}  |  alternates: {sum(len(alts[p]) for p in origem)}'
          f'  |  já corretos: {tot["ok"]}  H1: {tot["h1"]}  H2: {tot["h2"]}')
    fora = sorted(p for p in alts if not ESCOPO_RE.match(p))
    print(f'Fora do escopo (não editadas, só revalidadas): {len(fora)} páginas com hreflang '
          f'{dict(collections.Counter(lingua(p) for p in fora))}')
    for etapa, titulo in (('h1', 'H1 — corrigir href'), ('h2', 'H2 — remover linha')):
        print(f'\n## {titulo}: {tot[etapa]} alternates em '
              f'{len({p for (p, i), a in acao.items() if a[0] == etapa})} páginas')
        for k, n in sorted(((k, n) for k, n in cont.items() if k[0] == etapa), key=lambda x: -x[1]):
            p, a, b = exs[k]
            print(f'  {n:5d}  {k[1]}→{k[2]}  {k[3]}\n         {p}\n         antes:  {a}' + (f'\n         depois: {b}' if b else ''))
    print(f'\n## H3 — bloco de volta em {len(h3)} páginas PT')
    por = collections.Counter(tuple(lg for lg in ORDEM if lg in b) for b in h3.values())
    for k, n in por.most_common():
        print(f'  {n:5d}  com {", ".join(k)}')
    pastas = collections.Counter('/'.join(t.split('/')[:2]) for t in h3)
    print('  por livro (primeiros 12):', dict(pastas.most_common(12)))
    if h3:
        t = sorted(h3)[0]
        cs = CANON_LINHA_RE.search(novos[t])
        trecho = novos[t][cs.start():cs.start() + 700].split(b'\n')[:5]
        print(f'  ex.: {t}')
        for l in trecho:
            print('     | ' + l.decode().rstrip('\r'))
    for motivo, itens in pend.items():
        print(f'\nPendente — {motivo}: {len(itens)}  ex.: {itens[:5]}')
    alteradas = collections.Counter(lingua(p) for p in novos)
    print(f'\nArquivos alterados: {len(novos)}  {dict(alteradas)}')
    print('\n## Prova')
    print(f'  byte a byte (fora das linhas de hreflang idêntico; quebras preservadas): '
          f'{len(novos) - len([f for f in falhas if ".html" in f])}/{len(novos)} OK')
    print(f'  estado final revalidado ({sum(len(v) for v in estado.values())} alternates em {len(estado)} páginas): '
          + ('0 violações da regra' if not erros_fim else str(dict(erros_fim))))
    for k, v in exemplos_fim.items():
        print(f'     ex. {k}: {v}')
    if falhas:
        for f in falhas[:30]:
            print('FALHA:', f)
        print('\nNada gravado.')
        sys.exit(1)
    if not gravar:
        print('\nDry-run: nada gravado. Rode com --apply para gravar.')
        return
    stamp = time.strftime('%Y%m%d-%H%M%S')
    zpath = os.path.join(ROOT, '_backups', f'hreflang-{stamp}.zip')
    os.makedirs(os.path.dirname(zpath), exist_ok=True)
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in novos:
            z.writestr(p, ler(p))
    for p, n in novos.items():
        open(os.path.join(ROOT, p), 'wb').write(n)
    print(f'\nGravado: {len(novos)} arquivos. Backup: {os.path.relpath(zpath, ROOT)}')


if __name__ == '__main__':
    main()
