---
name: hub-testamento
description: Hubs do Antigo e do Novo Testamento (e a home) no layout novo do 365. Use ao criar ou alterar /antigo-testamento/, 08-novo-testamento/index.html ou index.html, ou ao montar outra página-índice no mesmo modelo.
---

# Hubs AT/NT e home

## Regras fixas do projeto
- Nunca alterar texto editorial (estudos, exegese, versículos, títulos) sem autorização explícita do Wagner.
- Trabalhar só em branch; nunca na `main`. Perguntar antes de cada commit e de cada push. Nada de merge na `main` sem ordem explícita.
- Site 100% estático (HTML, CSS e JS puros), mudanças incrementais, preservar todas as URLs.
- Responder em português do Brasil.

## Onde ficam
- Hub do AT: `/antigo-testamento/index.html` (pasta criada no redesign; é a referência de estrutura).
- Hub do NT: `/08-novo-testamento/index.html`. `/novo-testamento/` continua só como redirecionamento.
- Home: `/index.html`. Não existe `index-anterior.html` (decisão do Wagner; a versão antiga fica no histórico do git).
- Protótipos de referência em `redesign/` (fora do deploy): nunca linkar `/redesign/…` nas páginas publicadas.

## Peças
- `assets/css/site.css` — layout dos hubs e da home (cópia definitiva de `redesign/redesign.css`).
- `assets/js/hub.js` — filtro (`.filter [data-filter]` × `.group[data-group]`) e destaque do livro em leitura (`.book[data-book]`, via `window.Site365` do `site-nav.js`; sem progresso, destaca Mateus).
- `assets/js/header-cta.js` — botão "Começar Dia 1 ›" no cabeçalho. Fica só na home e nos hubs.

## Estrutura (igual nos dois hubs)
Topo (caminho "Início › …", título, subtítulo, botões) → filtro por grupo → grupos com cards (nome, nº de capítulos, linha de dias e link; no NT também o tema já existente) → apoio ao estudo → visão geral com o restante do texto da página → rodapé.
- Linha de dias do NT: soma acumulada dos capítulos dos 27 livros (Dias 1–28 … 239–260).
- Cards de apoio: título copiado do `<h1>` da página de destino. Card sem texto existente fica sem descrição; não invente.
- Rótulos de interface novos (filtro, "Dias X–Y", "Ver livro →") são permitidos, mas passam pela aprovação do Wagner.

## O que preservar
- `<head>`: título, description, canonical, Open Graph, Twitter, JSON-LD, hreflang, robots e AdSense **idênticos**. Só sai o `<style>`/CSS do layout antigo, trocado por `site.css`, e entram o bloco do menu e `header-cta.js`/`hub.js`.
- Blocos `<!-- site-nav:v1 -->`: os mesmos do hub do AT. A faixa `context-nav` sai **só** nos hubs e na home (exceção pontual aprovada).
- Final da página (modo claro e WhatsApp) idêntico.
- Todo texto editorial: extraído do arquivo atual por script, nunca redigitado. Trocas de texto só com decisão registrada do Wagner (ex.: home com "A Jornada" e "+2.900 Páginas em português").

## Procedimento
1. Monte a página nova com um script no scratchpad que lê o arquivo do commit e o protótipo.
2. Prova de integridade: `<head>` byte a byte (menos as linhas trocadas), cada metadado conferido, blocos do menu e final idênticos, todos os trechos de texto da página atual presentes no novo (mesma quantidade), links e âncoras mantidos, quebras de linha preservadas.
3. Links: 0 erros (seguindo redirecionamentos de pasta). Rolagem horizontal: nenhuma em 1280/768/390/360, escuro e claro. Item do menu aceso correto.
4. Prints lado a lado (atual × nova, ou hub × hub de referência) em 1280/768/390, escuro e claro. **Pare para revisão.**
5. Commit só da página, depois commit separado marcando o item no `redesign/PLANO.md`. Sem push.
