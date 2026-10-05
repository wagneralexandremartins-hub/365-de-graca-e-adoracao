---
name: validacao-visual
description: Checklist de validação visual (desktop, tablet, mobile, modo claro/escuro) para qualquer mudança de layout, menu ou CSS no 365. Use antes de propor commit de mudanças visuais.
---

# Validação visual do 365

Valide **antes de propor commit**. Screenshot sozinho não basta: confira também a geometria pelo DOM.

## Como testar localmente
- Sirva a raiz do repositório: `python -m http.server 8365 --bind 127.0.0.1` (o servidor em segundo plano expira em até 2 h; se cair no meio de um teste, descarte o resultado daquela rodada).
- A janela do Chrome pode não redimensionar; para larguras menores, carregue a página num `<iframe>` da mesma origem com a largura desejada e meça dentro dele.
- Para comparar CSS antes/depois sem mexer no repositório, sirva a versão antiga de outra porta e troque o `href` do `<link>` só no navegador.
- Limpe o `localStorage` de teste no fim (`365-theme`, `365-progress`, `365-last`).

## Checklist por página
- **Larguras**: 1280px, 768px e 390px.
- **Modo escuro e claro**: clique em `#dark-toggle`; a página inverte e a barra do menu continua no topo (`.sh-bar` com `top = 0` após rolar).
- **Overflow horizontal**: `document.documentElement.scrollWidth > clientWidth` deve ser falso. Se houver, identifique o elemento e diga se é do cabeçalho novo ou de conteúdo antigo.
- **Menu**: 8 itens, item ativo correto (`aria-current="page"`); no mobile, o botão abre o menu e os 8 links (mais PT/EN/ES abaixo de 440px) ficam visíveis.
- **Barra contextual** (`.context-nav`) com os links que a página já tinha.
- **Hubs**: todos os links levam a arquivos que existem.
- **Console** sem erros.

## Amostra mínima por etapa
Pelo menos 12 páginas cobrindo: hub da seção, índices de livro, capítulo curto, capítulo mais longo, uma página de cada variante de topo encontrada no dry-run e páginas com problema conhecido. Para mudanças de CSS compartilhado, inclua páginas que **já funcionavam** e compare o estilo calculado de todos os elementos antes e depois (ignore anúncios e scripts carregados dinamicamente).

## Problemas antigos conhecidos — só registrar, não corrigir
Estes já existiam (ou existem no site no ar) e não são causados pelo menu. Liste-os no relatório quando aparecerem; não corrija sem pedido do Wagner.
- `/estudos/` e subpáginas sem o botão de modo claro.
- Hero do índice de `13-apocalipse` "cru" no site no ar (corrigido na branch pelo commit de `bloco.css`; confira se continua bom).
- 12 subpáginas de `13-apocalipse/` com "Bloco 12" no `<title>` (não alterar sem ordem).
- Botões flutuantes (modo claro e WhatsApp) cobrindo o botão "Próximo" da barra inferior dos capítulos no mobile.
- Overflow a 390px: URLs longas nas referências de Números 1 e a tabela dos 27 livros no hub do NT.
- Índice de busca (`assets/js/nav.js`) com `1-corintios`, mas a pasta é `1corintios` (e livros numerados semelhantes).
- Estilos escritos direto no HTML que prevalecem sobre o CSS (ex.: "Perguntas para Reflexão" em Mateus).
- Capítulos EN/ES sem estilo: 2.212 páginas (`en/` e `es/`, 1.106 cada) usam `.chapter-main` sem regras para o idioma delas.
