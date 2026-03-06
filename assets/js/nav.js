/**
 * nav.js — Menu principal, mega-menu, busca global
 * 365 de Graça & Adoração
 */

/* ── Índice de busca ──────────────────────────────────────────── */
const SEARCH_INDEX = [
  /* Blocos */
  { title: 'O Princípio de Tudo', sub: 'Bloco 01 — Criação, Queda, Caim e Abel', url: '/01-principio/index.html', tag: 'Bloco 01', color: '#d97706' },
  { title: 'Pentateuco', sub: 'Bloco 02 — Gênesis ao Deuteronômio', url: '/02-pentateuco/index.html', tag: 'Bloco 02', color: '#d97706' },
  { title: 'Livros Históricos', sub: 'Bloco 03 — Josué a Ester', url: '/03-historicos/index.html', tag: 'Bloco 03', color: '#059669' },
  { title: 'Livros Poéticos e Sapienciais', sub: 'Bloco 04 — Jó, Salmos, Provérbios, Eclesiastes, Cântico', url: '/04-poeticos/index.html', tag: 'Bloco 04', color: '#059669' },
  { title: 'Profetas', sub: 'Bloco 05 — 17 livros proféticos', url: '/05-profetas/index.html', tag: 'Bloco 05', color: '#059669' },
  { title: 'Livros Apócrifos', sub: 'Bloco 06 — 8 livros deuterocanônicos', url: '/06-apocrifos/index.html', tag: 'Bloco 06', color: '#6366f1' },
  { title: 'Período Intertestamentário', sub: 'Bloco 07 — Os 400 anos de silêncio', url: '/07-intertestamentario/index.html', tag: 'Bloco 07', color: '#6366f1' },
  { title: 'Novo Testamento', sub: 'Bloco 08 — Evangelhos, Atos, Epístolas, Apocalipse', url: '/08-novo-testamento/index.html', tag: 'Bloco 08', color: '#0ea5e9' },
  { title: 'Igreja Primitiva', sub: 'Bloco 09 — Pentecostes, Perseguições, Pais da Igreja', url: '/09-igreja-primitiva/index.html', tag: 'Bloco 09', color: '#0ea5e9' },
  { title: 'Concílios e História da Igreja', sub: 'Bloco 10 — Niceia, Calcedônia, Trento, Vaticano', url: '/10-concilios/index.html', tag: 'Bloco 10', color: '#8b5cf6' },
  { title: 'Cruzadas e Guerras Religiosas', sub: 'Bloco 11 — As 8 Cruzadas e suas consequências', url: '/11-cruzadas/index.html', tag: 'Bloco 11', color: '#8b5cf6' },
  { title: 'Conflitos Religiosos Contemporâneos', sub: 'Bloco 12 — Reforma, Cisma, Secularismo', url: '/12-conflitos-contemporaneos/index.html', tag: 'Bloco 12', color: '#e11d48' },
  { title: 'Apocalipse', sub: 'Bloco 13 — As 7 Igrejas, Selos, Trombetas, Nova Jerusalém', url: '/13-apocalipse/index.html', tag: 'Bloco 13', color: '#7c3aed' },

  /* Linha do tempo e mapas */
  { title: 'Linha do Tempo Bíblica', sub: 'Da Criação ao Apocalipse — cronologia completa', url: '/timeline/index.html', tag: 'Recurso', color: '#0ea5e9' },
  { title: 'Mapas Bíblicos', sub: 'Geografia bíblica, rotas de Paulo, Cruzadas', url: '/mapas/index.html', tag: 'Recurso', color: '#059669' },
  { title: 'Busca Global', sub: 'Pesquisar capítulos, temas e personagens', url: '/busca/index.html', tag: 'Recurso', color: '#d97706' },

  /* Livros do AT */
  { title: 'Gênesis', sub: 'Pentateuco — 50 capítulos', url: '/02-pentateuco/genesis/index.html', tag: 'AT', color: '#d97706' },
  { title: 'Êxodo', sub: 'Pentateuco — 40 capítulos', url: '/02-pentateuco/exodo/index.html', tag: 'AT', color: '#d97706' },
  { title: 'Levítico', sub: 'Pentateuco — 27 capítulos', url: '/02-pentateuco/levitico/index.html', tag: 'AT', color: '#d97706' },
  { title: 'Números', sub: 'Pentateuco — 36 capítulos', url: '/02-pentateuco/numeros/index.html', tag: 'AT', color: '#d97706' },
  { title: 'Deuteronômio', sub: 'Pentateuco — 34 capítulos', url: '/02-pentateuco/deuteronomio/index.html', tag: 'AT', color: '#d97706' },
  { title: 'Josué', sub: 'Livros Históricos — 24 capítulos', url: '/03-historicos/josue/index.html', tag: 'AT', color: '#059669' },
  { title: 'Juízes', sub: 'Livros Históricos — 21 capítulos', url: '/03-historicos/juizes/index.html', tag: 'AT', color: '#059669' },
  { title: 'Rute', sub: 'Livros Históricos — 4 capítulos', url: '/03-historicos/rute/index.html', tag: 'AT', color: '#059669' },
  { title: '1 Samuel', sub: 'Livros Históricos — 31 capítulos', url: '/03-historicos/1-samuel/index.html', tag: 'AT', color: '#059669' },
  { title: '2 Samuel', sub: 'Livros Históricos — 24 capítulos', url: '/03-historicos/2-samuel/index.html', tag: 'AT', color: '#059669' },
  { title: '1 Reis', sub: 'Livros Históricos — 22 capítulos', url: '/03-historicos/1-reis/index.html', tag: 'AT', color: '#059669' },
  { title: '2 Reis', sub: 'Livros Históricos — 25 capítulos', url: '/03-historicos/2-reis/index.html', tag: 'AT', color: '#059669' },
  { title: 'Salmos', sub: 'Livros Poéticos — 150 capítulos', url: '/04-poeticos/salmos/index.html', tag: 'AT', color: '#059669' },
  { title: 'Provérbios', sub: 'Livros Sapienciais — 31 capítulos', url: '/04-poeticos/proverbios/index.html', tag: 'AT', color: '#059669' },
  { title: 'Jó', sub: 'Livros Poéticos — 42 capítulos', url: '/04-poeticos/jo/index.html', tag: 'AT', color: '#059669' },
  { title: 'Eclesiastes', sub: 'Livros Sapienciais — 12 capítulos', url: '/04-poeticos/eclesiastes/index.html', tag: 'AT', color: '#059669' },
  { title: 'Isaías', sub: 'Profetas Maiores — 66 capítulos', url: '/05-profetas/isaias/index.html', tag: 'AT', color: '#059669' },
  { title: 'Jeremias', sub: 'Profetas Maiores — 52 capítulos', url: '/05-profetas/jeremias/index.html', tag: 'AT', color: '#059669' },
  { title: 'Ezequiel', sub: 'Profetas Maiores — 48 capítulos', url: '/05-profetas/ezequiel/index.html', tag: 'AT', color: '#059669' },
  { title: 'Daniel', sub: 'Profetas Maiores — 12 capítulos', url: '/05-profetas/daniel/index.html', tag: 'AT', color: '#059669' },

  /* Livros do NT */
  { title: 'Mateus', sub: 'Evangelhos — 28 capítulos', url: '/08-novo-testamento/mateus/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'Marcos', sub: 'Evangelhos — 16 capítulos', url: '/08-novo-testamento/marcos/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'Lucas', sub: 'Evangelhos — 24 capítulos', url: '/08-novo-testamento/lucas/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'João', sub: 'Evangelhos — 21 capítulos', url: '/08-novo-testamento/joao/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'Atos dos Apóstolos', sub: 'História — 28 capítulos', url: '/08-novo-testamento/atos/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'Romanos', sub: 'Epístolas Paulinas — 16 capítulos', url: '/08-novo-testamento/romanos/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: '1 Coríntios', sub: 'Epístolas Paulinas — 16 capítulos', url: '/08-novo-testamento/1-corintios/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: '2 Coríntios', sub: 'Epístolas Paulinas — 13 capítulos', url: '/08-novo-testamento/2-corintios/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'Gálatas', sub: 'Epístolas Paulinas — 6 capítulos', url: '/08-novo-testamento/galatas/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'Efésios', sub: 'Epístolas Paulinas — 6 capítulos', url: '/08-novo-testamento/efesios/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'Filipenses', sub: 'Epístolas Paulinas — 4 capítulos', url: '/08-novo-testamento/filipenses/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'Colossenses', sub: 'Epístolas Paulinas — 4 capítulos', url: '/08-novo-testamento/colossenses/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'Hebreus', sub: 'Epístolas Gerais — 13 capítulos', url: '/08-novo-testamento/hebreus/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'Tiago', sub: 'Epístolas Gerais — 5 capítulos', url: '/08-novo-testamento/tiago/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: '1 Pedro', sub: 'Epístolas Gerais — 5 capítulos', url: '/08-novo-testamento/1-pedro/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: '2 Pedro', sub: 'Epístolas Gerais — 3 capítulos', url: '/08-novo-testamento/2-pedro/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: '1 João', sub: 'Epístolas Gerais — 5 capítulos', url: '/08-novo-testamento/1-joao/index.html', tag: 'NT', color: '#0ea5e9' },
  { title: 'Apocalipse', sub: 'Profecia — 22 capítulos', url: '/08-novo-testamento/apocalipse/index.html', tag: 'NT', color: '#7c3aed' },

  /* Temas */
  { title: 'Graça', sub: 'Tema central — da Criação ao Apocalipse', url: '/busca/index.html?q=graca', tag: 'Tema', color: '#d97706' },
  { title: 'Adoração', sub: 'Tema central — formas e evolução da adoração', url: '/busca/index.html?q=adoracao', tag: 'Tema', color: '#d97706' },
  { title: 'Reino de Deus', sub: 'Tema central — manifestação ao longo da história', url: '/busca/index.html?q=reino', tag: 'Tema', color: '#059669' },
  { title: 'Aliança', sub: 'Tema teológico — Noé, Abraão, Moisés, Davi, Nova Aliança', url: '/busca/index.html?q=alianca', tag: 'Tema', color: '#059669' },
  { title: 'Profecia Messiânica', sub: 'Tema teológico — promessas cumpridas em Cristo', url: '/busca/index.html?q=messias', tag: 'Tema', color: '#0ea5e9' },
  { title: 'Fé e Obras', sub: 'Tema teológico — Tiago, Paulo, Hebreus', url: '/busca/index.html?q=fe-obras', tag: 'Tema', color: '#0ea5e9' },
  { title: 'Escatologia', sub: 'Tema teológico — fins últimos, Apocalipse, milênio', url: '/busca/index.html?q=escatologia', tag: 'Tema', color: '#7c3aed' },

  /* Personagens */
  { title: 'Abraão', sub: 'Personagem — pai da fé, Gênesis 12–25', url: '/busca/index.html?q=abraao', tag: 'Personagem', color: '#d97706' },
  { title: 'Moisés', sub: 'Personagem — libertador, Êxodo ao Deuteronômio', url: '/busca/index.html?q=moises', tag: 'Personagem', color: '#d97706' },
  { title: 'Davi', sub: 'Personagem — rei, salmista, 1-2 Samuel', url: '/busca/index.html?q=davi', tag: 'Personagem', color: '#059669' },
  { title: 'Paulo', sub: 'Personagem — apóstolo, Atos e Epístolas', url: '/busca/index.html?q=paulo', tag: 'Personagem', color: '#0ea5e9' },
  { title: 'João', sub: 'Personagem — discípulo amado, Evangelhos e Apocalipse', url: '/busca/index.html?q=joao', tag: 'Personagem', color: '#0ea5e9' },
];

/* ── Busca ─────────────────────────────────────────────────────── */
function initSearch() {
  const overlay = document.getElementById('search-overlay');
  const input = document.getElementById('search-input');
  const results = document.getElementById('search-results');
  if (!overlay || !input || !results) return;

  let selectedIndex = -1;

  function openSearch() {
    overlay.classList.add('open');
    input.focus();
    input.value = '';
    renderResults('');
    selectedIndex = -1;
  }

  function closeSearch() {
    overlay.classList.remove('open');
    input.blur();
  }

  function renderResults(query) {
    const q = query.toLowerCase().trim();
    const items = q.length === 0
      ? SEARCH_INDEX.slice(0, 8)
      : SEARCH_INDEX.filter(item =>
          item.title.toLowerCase().includes(q) ||
          item.sub.toLowerCase().includes(q) ||
          item.tag.toLowerCase().includes(q)
        ).slice(0, 12);

    if (items.length === 0) {
      results.innerHTML = `<div class="search-empty">Nenhum resultado para "<strong>${query}</strong>"</div>`;
      return;
    }

    results.innerHTML = items.map((item, i) => `
      <a href="${item.url}" class="search-result-item" data-index="${i}">
        <div class="search-result-icon" style="color:${item.color};background:${item.color}18">
          ${item.tag.slice(0,2)}
        </div>
        <div class="search-result-body">
          <div class="search-result-title">${highlight(item.title, q)}</div>
          <div class="search-result-sub">${item.sub}</div>
        </div>
        <span class="search-result-tag">${item.tag}</span>
      </a>
    `).join('');
    selectedIndex = -1;
  }

  function highlight(text, query) {
    if (!query) return text;
    const re = new RegExp(`(${query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    return text.replace(re, '<mark style="background:rgba(14,165,233,0.3);color:#fff;border-radius:2px;padding:0 2px">$1</mark>');
  }

  function moveSelection(dir) {
    const items = results.querySelectorAll('.search-result-item');
    if (!items.length) return;
    items[selectedIndex]?.classList.remove('selected');
    selectedIndex = (selectedIndex + dir + items.length) % items.length;
    items[selectedIndex]?.classList.add('selected');
    items[selectedIndex]?.scrollIntoView({ block: 'nearest' });
  }

  // Eventos
  input.addEventListener('input', () => renderResults(input.value));

  input.addEventListener('keydown', e => {
    if (e.key === 'ArrowDown') { e.preventDefault(); moveSelection(1); }
    if (e.key === 'ArrowUp') { e.preventDefault(); moveSelection(-1); }
    if (e.key === 'Enter') {
      const sel = results.querySelector('.search-result-item.selected');
      if (sel) { sel.click(); closeSearch(); }
    }
    if (e.key === 'Escape') closeSearch();
  });

  overlay.addEventListener('click', e => {
    if (e.target === overlay) closeSearch();
  });

  document.addEventListener('keydown', e => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      overlay.classList.contains('open') ? closeSearch() : openSearch();
    }
    if (e.key === 'Escape' && overlay.classList.contains('open')) closeSearch();
  });

  // Botões de abertura
  document.querySelectorAll('[data-search-open]').forEach(btn => {
    btn.addEventListener('click', e => { e.preventDefault(); openSearch(); });
  });

  // Pré-popular busca via URL ?q=
  const urlQ = new URLSearchParams(window.location.search).get('q');
  if (urlQ) {
    openSearch();
    input.value = urlQ;
    renderResults(urlQ);
  }
}

/* ── Menu mobile ───────────────────────────────────────────────── */
function initMobileMenu() {
  const toggle = document.getElementById('nav-toggle');
  const nav = document.getElementById('main-nav');
  if (!toggle || !nav) return;

  toggle.addEventListener('click', () => {
    nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', nav.classList.contains('open'));
  });

  // Fechar ao clicar fora
  document.addEventListener('click', e => {
    if (!toggle.contains(e.target) && !nav.contains(e.target)) {
      nav.classList.remove('open');
    }
  });

  // Dropdown mobile
  document.querySelectorAll('.nav-item > a').forEach(link => {
    link.addEventListener('click', e => {
      if (window.innerWidth <= 860) {
        e.preventDefault();
        link.closest('.nav-item').classList.toggle('open');
      }
    });
  });
}

/* ── Init ──────────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  initSearch();
  initMobileMenu();
});
