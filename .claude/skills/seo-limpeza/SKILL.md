---
name: seo-limpeza
description: Etapa de SEO e limpeza do 365 — sitemap, canonical, imagens de compartilhamento, favicon, links quebrados antigos, páginas ralas ou publicadas por engano e ajustes de CSS pendentes. Use quando o Wagner pedir para tratar itens da "Limpeza prioritária" do redesign/PLANO.md ou fazer varredura de links.
---

# SEO e limpeza

## Regras fixas do projeto
- Nunca alterar texto editorial (estudos, exegese, versículos, títulos) sem autorização explícita do Wagner.
- Trabalhar só em branch; nunca na `main`. Perguntar antes de cada commit e de cada push. Nada de merge na `main` sem ordem explícita.
- Site 100% estático (HTML, CSS e JS puros), mudanças incrementais, preservar todas as URLs (não apagar nem mover páginas sem ordem).
- Responder em português do Brasil.

## Fonte da verdade
A lista atualizada fica em `redesign/PLANO.md`, seção "Limpeza prioritária". **Nada ali é alterado sem decisão do Wagner**, um item (ou grupo de itens iguais) por etapa. Itens registrados até 07/10/2026:
- Imagens de compartilhamento: `og:image`/`twitter:image` de ~2.825 páginas apontam para `assets/img/og-cover.jpg`, que não existe; a home aponta para `og-image.jpg`, mas o arquivo existente é `assets/img/og-image.png`.
- `assets/img/favicon.png` referenciado (home e outras) e inexistente.
- Canonical do hub do NT (`/08-novo-testamento/index`) diferente do `sitemap.xml` (`/08-novo-testamento/index.html`).
- `sitemap.xml`: `lastmod` antigos e cabeçalho "Total de páginas" desatualizado (4.152 URLs desde 07/10).
- Páginas ralas com AdSense (`genesis/genesis-12.html` a `-50`), `busca/index_backup.html` publicada, `pasted_content.html`, 5 `pasted_file_*_image.html` com bytes nulos, fragmentos `timeline-*.html` na raiz.
- Rolagem horizontal a 390px em `06-apocrifos/` (6px) e `busca/` (31px, grade `.indice-item`), iguais na `main`: corrigir por CSS.
- `/estudos/` sem botão de modo claro; modo claro de Rute e Josué; faixa de números dos livros `main.wrap`.
- Textos para decisão do Wagner (não alterar sozinho): "1.627+ Páginas no projeto" na busca × "+2.900" na home; "compatíveis com Vercel" no rodapé dos estudos.
- Fase 2: índice de busca do `assets/js/nav.js` com `1-corintios` × pasta `1corintios` (e livros numerados semelhantes).

## Varredura de links (como foi feita no bloco B)
- Escopo: todas as `*.html` fora de `en/`, `es/`, `_backups/`, `redesign/`, `scripts/`, `.claude/`, `.github/`, sem as páginas de redirecionamento (`http-equiv="refresh"`).
- Links: `a[href]`, `img/script/iframe/source[src]`, `link[rel=stylesheet|icon|apple-touch-icon]`, `form[action]`; URLs absolutas do próprio domínio contam como internas.
- Regras do GitHub Pages: pasta com `index.html` responde; `/pasta` sem barra redireciona; endereço sem extensão serve o `.html`. Tudo o que o `pages.yml` exclui conta como 404.
- Compare com a `main` extraída por `git archive <sha> | tar -x` (só leitura) e reporte só os pares página → destino **novos**. Em 07/10: 1.325 pares quebrados antigos (1.196 são `/styles.css`), 0 novos.
- Confira também os links gerados por JS: itens do `MENU` e a trilha de 260 capítulos do `site-nav.js`, e o botão do `header-cta.js`.

## Procedimento por item
1. Levante o escopo (quantas páginas, quais) e mostre em dry-run, com prova de que só a linha/trecho previsto muda (byte a byte, quebras de linha preservadas).
2. **Espere o OK do Wagner.** Para trocas em lote, backup zip em `_backups/` (nunca em commit).
3. Aplique, valide (links e, se mexer em CSS, rolagem horizontal em 1280/768/390/360, escuro e claro) e mostre o relatório.
4. Commit separado por assunto, mensagem por arquivo, sem push. Atualize o item no `PLANO.md` em commit próprio.
