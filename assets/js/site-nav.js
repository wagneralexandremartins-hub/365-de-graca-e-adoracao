/**
 * site-nav.js — menu principal central + progresso de leitura
 * 365 Graça & Adoração
 *
 * Cada página só precisa de:
 *   <header id="site-header" class="site-header" data-lang-en="…" data-lang-es="…">
 *     <noscript>…links principais…</noscript>
 *   </header>
 *   <script src="/assets/js/site-nav.js" defer></script>
 * (+ /assets/css/site-header.css no <head>)
 *
 * Mudou o menu? Edite só MENU abaixo.
 */
(function () {
  'use strict';

  /* ── Menu: fonte única ──────────────────────────────────────────── */
  // ATENÇÃO (piloto): "Antigo Testamento" aponta para o protótipo até a etapa
  // dos hubs criar a página definitiva. Ver redesign/PLANO.md.
  var MENU = [
    { href: '/',                                 label: 'Início',            match: /^\/(index\.html)?$/ },
    { href: '/redesign/antigo-testamento.html',  label: 'Antigo Testamento', match: /^\/(redesign\/antigo-testamento|0[1-57]-|genesis\/|biblia\/(?!(mt|mc|lc|jo|atos|rm|1co|2co|gl|ef|fp|cl|1ts|2ts|1tm|2tm|tt|fm|hb|tg|1pe|2pe|1jo|2jo|3jo|jd|ap)\/)[^\/]+\/)/ },
    { href: '/08-novo-testamento/',              label: 'Novo Testamento',   match: /^\/(redesign\/novo-testamento|08-|09-|13-|biblia\/(mt|mc|lc|jo|atos|rm|1co|2co|gl|ef|fp|cl|1ts|2ts|1tm|2tm|tt|fm|hb|tg|1pe|2pe|1jo|2jo|3jo|jd|ap)\/)/ },
    { href: '/personagens/index.html',           label: 'Personagens',       match: /^\/personagens\// },
    { href: '/mapas/index.html',                 label: 'Mapas',             match: /^\/mapas\// },
    { href: '/timeline/index.html',              label: 'Linha do Tempo',    match: /^\/timeline\// },
    // 06-apocrifos fica em Estudos › Fontes Históricas (decisão do Wagner, 05/10)
    { href: '/estudos/',                         label: 'Estudos',           match: /^\/(estudos\/|06-|1[0-2]-)/ },
    { href: '/loja-365/',                        label: 'Loja 365',          match: /^\/loja-365\//, cls: 'sh-loja' }
  ];

  /* ── Trilha do NT: 27 livros, 260 capítulos ─────────────────────── */
  var NT = [
    ['mateus', 'Mateus', 28], ['marcos', 'Marcos', 16], ['lucas', 'Lucas', 24], ['joao', 'João', 21],
    ['atos', 'Atos', 28], ['romanos', 'Romanos', 16], ['1corintios', '1 Coríntios', 16],
    ['2corintios', '2 Coríntios', 13], ['galatas', 'Gálatas', 6], ['efesios', 'Efésios', 6],
    ['filipenses', 'Filipenses', 4], ['colossenses', 'Colossenses', 4],
    ['1tessalonicenses', '1 Tessalonicenses', 5], ['2tessalonicenses', '2 Tessalonicenses', 3],
    ['1timoteo', '1 Timóteo', 6], ['2timoteo', '2 Timóteo', 4], ['tito', 'Tito', 3],
    ['filemom', 'Filemom', 1], ['hebreus', 'Hebreus', 13], ['tiago', 'Tiago', 5],
    ['1pedro', '1 Pedro', 5], ['2pedro', '2 Pedro', 3], ['1joao', '1 João', 5],
    ['2joao', '2 João', 1], ['3joao', '3 João', 1], ['judas', 'Judas', 1], ['apocalipse', 'Apocalipse', 22]
  ];
  var TOTAL = 0, OFFSET = {};
  NT.forEach(function (b) { OFFSET[b[0]] = TOTAL; TOTAL += b[2]; });

  function chapterUrl(slug, ch) {
    return '/08-novo-testamento/' + slug + '/capitulos/capitulo-' + (ch < 10 ? '0' : '') + ch + '.html';
  }
  function bookOf(slug) {
    for (var i = 0; i < NT.length; i++) if (NT[i][0] === slug) return NT[i];
    return null;
  }

  /* localStorage pode falhar (aba anônima, cookies bloqueados) */
  function store(key, val) { try { localStorage.setItem(key, val); } catch (e) {} }
  function load(key) { try { return localStorage.getItem(key); } catch (e) { return null; } }

  function record(slug, ch) {
    var b = bookOf(slug);
    if (!b || ch < 1 || ch > b[2]) return;
    var day = OFFSET[slug] + ch;
    store('365-progress', String(day));   // chave já lida pela home atual
    store('365-last', JSON.stringify({ slug: slug, ch: ch, day: day, t: Date.now() }));
  }

  function getProgress() {
    var last = null;
    try { last = JSON.parse(load('365-last') || 'null'); } catch (e) {}
    if (!last || !bookOf(last.slug)) return null;
    var b = bookOf(last.slug);
    return {
      slug: last.slug, book: b[1], ch: last.ch, day: last.day, total: TOTAL,
      pct: Math.round(last.day / TOTAL * 100), url: chapterUrl(last.slug, last.ch)
    };
  }

  var path = location.pathname;

  /* Grava o progresso quando a página é um capítulo do NT em português */
  var m = path.match(/^\/08-novo-testamento\/([^\/]+)\/capitulos\/capitulo-(\d+)\.html$/);
  if (m) record(m[1], parseInt(m[2], 10));

  /* Só no protótipo: ?simular=romanos/8 simula leitura para demonstrar a home */
  var sim = /[?&]simular=([a-z0-9]+)\/(\d+)/.exec(location.search);
  if (sim && /^\/redesign\//.test(path)) record(sim[1], parseInt(sim[2], 10));

  /* ── Montagem do cabeçalho ──────────────────────────────────────── */
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }

  // Ícone desenhado por máscara CSS (um <svg> embutido seria zerado pelo `all: revert`)
  var SEARCH_ICON = '<span class="sh-search-ico" aria-hidden="true"></span>';

  function buildHeader(el) {
    // Idiomas: a página pode informar a URL equivalente traduzida
    var langs = [
      { code: 'PT', lang: 'pt-BR', title: 'Português', href: el.getAttribute('data-lang-pt') || '/', cur: !/^\/(en|es)\//.test(path) },
      { code: 'EN', lang: 'en', title: 'English', href: el.getAttribute('data-lang-en') || '/en/', cur: /^\/en\//.test(path) },
      { code: 'ES', lang: 'es', title: 'Español', href: el.getAttribute('data-lang-es') || '/es/', cur: /^\/es\//.test(path) }
    ];

    var links = MENU.map(function (i) {
      return '<a href="' + i.href + '"' + (i.cls ? ' class="' + i.cls + '"' : '') +
        (i.match.test(path) ? ' aria-current="page"' : '') + '>' + esc(i.label) + '</a>';
    }).join('');

    var langLinks = langs.map(function (l) {
      return '<a href="' + esc(l.href) + '" lang="' + l.lang + '" hreflang="' + l.lang + '" title="' + l.title + '"' +
        (l.cur ? ' aria-current="true"' : '') + '>' + l.code + '</a>';
    }).join('');

    el.innerHTML = '<div class="sh-bar">' +
      '<a class="sh-brand" href="/" aria-label="365 Graça &amp; Adoração — início">' +
        '<img src="/assets/img/logo-header.png" alt="" width="36" height="36">' +
        '<span class="sh-brand-text">365 Graça &amp; Adoração<small>Da Criação ao Apocalipse</small></span>' +
      '</a>' +
      '<button type="button" class="sh-toggle" aria-expanded="false" aria-controls="sh-nav" aria-label="Abrir menu">' +
        '<span class="sh-bars" aria-hidden="true"></span></button>' +
      '<nav id="sh-nav" class="sh-nav" aria-label="Navegação principal">' + links +
        '<div class="sh-nav-lang" role="group" aria-label="Idioma">' + langLinks + '</div></nav>' +
      '<div class="sh-tools">' +
        '<a class="sh-search" href="/busca/" aria-label="Buscar" title="Buscar">' + SEARCH_ICON + '</a>' +
        '<div class="sh-lang" role="group" aria-label="Idioma">' + langLinks + '</div>' +
      '</div></div>';

    var btn = el.querySelector('.sh-toggle');
    var nav = el.querySelector('.sh-nav');
    function setOpen(open) {
      nav.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
    }
    btn.addEventListener('click', function () { setOpen(!nav.classList.contains('is-open')); });
    nav.addEventListener('click', function (e) { if (e.target.tagName === 'A') setOpen(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) { setOpen(false); btn.focus(); }
    });
  }

  function init() {
    var el = document.getElementById('site-header');
    if (el) buildHeader(el);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

  /* API usada pela home e pelos hubs */
  window.Site365 = { NT: NT, TOTAL: TOTAL, OFFSET: OFFSET, chapterUrl: chapterUrl, getProgress: getProgress };
})();
