// assets/js/md-viewer.js
// Renderiza um arquivo .md dentro da página usando marked (CDN).

async function renderMarkdown({ mdPath, title }) {
  const elTitle = document.querySelector("[data-title]");
  const elContent = document.querySelector("[data-content]");
  const elMeta = document.querySelector("[data-meta]");

  if (title && elTitle) elTitle.textContent = title;

  try {
    const res = await fetch(mdPath, { cache: "no-store" });
    if (!res.ok) throw new Error(`Não consegui carregar: ${mdPath} (${res.status})`);
    const md = await res.text();

    // marked vem do CDN no HTML
    elContent.innerHTML = marked.parse(md);

    if (elMeta) elMeta.textContent = mdPath;
  } catch (err) {
    elContent.innerHTML = `
      <div style="padding:14px;border:1px solid rgba(255,255,255,.12);border-radius:14px;">
        <h3 style="margin:0 0 8px;">Erro ao carregar conteúdo</h3>
        <p style="margin:0;opacity:.8;">${String(err.message || err)}</p>
        <p style="margin:10px 0 0;opacity:.8;">
          Confira se o arquivo existe e se o caminho está correto.
        </p>
      </div>
    `;
  }
}

// Lê atributos do HTML
document.addEventListener("DOMContentLoaded", () => {
  const root = document.documentElement;
  const mdPath = root.getAttribute("data-md");
  const title = root.getAttribute("data-page-title") || "Leitura";

  if (!mdPath) {
    console.error("Faltou data-md no <html>.");
    return;
  }
  renderMarkdown({ mdPath, title });
});
