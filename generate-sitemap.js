/**
 * generate-sitemap.js
 * Gera sitemap.xml automaticamente para 365gracaeadoracao.com
 * Execute: node generate-sitemap.js
 * Roda automaticamente no build da Vercel via package.json "build" script
 */

const fs   = require('fs');
const path = require('path');

const BASE_URL  = 'https://365gracaeadoracao.com';
const TODAY     = new Date().toISOString().split('T')[0]; // YYYY-MM-DD
const OUT_FILE  = path.join(__dirname, 'sitemap.xml');

// Diretórios e arquivos a ignorar
const IGNORE_DIRS  = new Set(['.git', 'node_modules', 'assets', '__pycache__']);
const IGNORE_FILES = new Set(['sitemap.xml', 'sitemap-visual.html', '404.html']);

// ── Regras de prioridade e frequência ────────────────────────────────────────
function getUrlMeta(relPath) {
  const p = relPath.replace(/\\/g, '/');

  // Home
  if (p === 'index.html' || p === '') {
    return { priority: '1.0', changefreq: 'weekly' };
  }

  // Índices de seção (index.html dentro de pastas)
  if (p.endsWith('/index.html') || p.endsWith('\\index.html')) {
    return { priority: '0.9', changefreq: 'weekly' };
  }

  // Capítulos do NT aprofundados (08-novo-testamento/.../capitulos/capitulo-XX.html)
  if (p.includes('08-novo-testamento') && p.includes('/capitulos/capitulo-')) {
    return { priority: '0.9', changefreq: 'monthly' };
  }

  // Salmos
  if (p.includes('/salmos/capitulos/salmo-')) {
    return { priority: '0.9', changefreq: 'monthly' };
  }

  // Capítulos do AT
  if (p.includes('/capitulos/capitulo-')) {
    return { priority: '0.8', changefreq: 'monthly' };
  }

  // Personagens, estudos, artigos estratégicos
  if (p.includes('/personagens/') || p.includes('/estudos/') || p.includes('/como-estudar/')) {
    return { priority: '0.8', changefreq: 'monthly' };
  }

  // Mapas, timeline, linha do tempo
  if (p.includes('/mapas/') || p.includes('/timeline/') || p.includes('/linha-do-tempo/')) {
    return { priority: '0.7', changefreq: 'monthly' };
  }

  // Demais páginas
  return { priority: '0.6', changefreq: 'monthly' };
}

// ── Coletar todos os arquivos HTML ────────────────────────────────────────────
function getAllHtmlFiles(dir, base, results = []) {
  let entries;
  try { entries = fs.readdirSync(dir); } catch { return results; }

  for (const entry of entries) {
    if (IGNORE_DIRS.has(entry)) continue;

    const fullPath = path.join(dir, entry);
    const stat     = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      getAllHtmlFiles(fullPath, base, results);
    } else if (entry.endsWith('.html') && !IGNORE_FILES.has(entry)) {
      results.push(path.relative(base, fullPath));
    }
  }
  return results;
}

// ── Converter caminho em URL ──────────────────────────────────────────────────
function toUrl(relPath) {
  let url = relPath.replace(/\\/g, '/');

  // Remover index.html final (URL limpa)
  url = url.replace(/\/index\.html$/, '/').replace(/^index\.html$/, '');

  // Remover extensão .html
  url = url.replace(/\.html$/, '');

  // Codificar caracteres especiais (acentos, espaços)
  url = url.split('/').map(segment => encodeURIComponent(decodeURIComponent(segment))).join('/');

  return BASE_URL + '/' + url;
}

// ── Gerar XML ─────────────────────────────────────────────────────────────────
function buildXml(files) {
  const urlEntries = files.map(relPath => {
    const url  = toUrl(relPath);
    const meta = getUrlMeta(relPath);
    return `  <url>
    <loc>${url}</loc>
    <lastmod>${TODAY}</lastmod>
    <changefreq>${meta.changefreq}</changefreq>
    <priority>${meta.priority}</priority>
  </url>`;
  });

  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
${urlEntries.join('\n')}
</urlset>`;
}

// ── Validação básica de XML ───────────────────────────────────────────────────
function validateXml(xml) {
  // Checar & não escapado
  const badAmpersand = /&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[\da-fA-F]+;)/g;
  const matches = xml.match(badAmpersand);
  if (matches) {
    console.warn(`⚠️  Encontrados ${matches.length} & não escapados — corrija os nomes de arquivo.`);
  }
  return !matches;
}

// ── Main ──────────────────────────────────────────────────────────────────────
(function main() {
  const base  = __dirname;
  const files = getAllHtmlFiles(base, base);

  // Ordenar: home primeiro, depois índices, depois capítulos
  files.sort((a, b) => {
    const pa = getUrlMeta(a).priority;
    const pb = getUrlMeta(b).priority;
    if (pa !== pb) return parseFloat(pb) - parseFloat(pa); // maior prioridade primeiro
    return a.localeCompare(b);
  });

  const xml = buildXml(files);

  if (!validateXml(xml)) {
    console.error('❌ sitemap.xml contém erros de XML. Verifique os nomes de arquivo.');
    process.exit(1);
  }

  fs.writeFileSync(OUT_FILE, xml, 'utf8');

  // Estatísticas
  const byPriority = {};
  files.forEach(f => {
    const p = getUrlMeta(f).priority;
    byPriority[p] = (byPriority[p] || 0) + 1;
  });

  console.log('✅ sitemap.xml gerado com sucesso!');
  console.log(`   Total de URLs: ${files.length}`);
  console.log(`   Data: ${TODAY}`);
  console.log(`   Arquivo: ${OUT_FILE}`);
  Object.entries(byPriority).sort((a,b) => b[0]-a[0]).forEach(([p, n]) => {
    console.log(`   Prioridade ${p}: ${n} URLs`);
  });
})();
