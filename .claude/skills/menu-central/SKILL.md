---
name: menu-central
description: Como aplicar e manter o menu central (site-nav.js + site-header.css) nas páginas do 365. Use ao levar o menu novo para uma pasta, mudar itens do menu ou mexer no cabeçalho.
---

# Menu central do 365

## Peças
- `assets/js/site-nav.js` — fonte única do menu (array `MENU`), busca, idiomas, menu mobile e gravação do progresso do NT (`365-progress`, `365-last`). Mudou o menu? Edite só aqui.
- `assets/css/site-header.css` — estilos do cabeçalho, isolados das folhas antigas com `all: revert` sob `#site-header`.
- `scripts/aplicar_menu_central.py` — insere o cabeçalho nas páginas.

Cada página recebe dois blocos marcados com `<!-- site-nav:v1 -->` … `<!-- /site-nav:v1 -->`: um no `<head>` (fontes, CSS, JS) e um logo após `<body>` (link "Pular para o conteúdo", `<header id="site-header">` com fallback `<noscript>` dos 8 links, `<nav class="context-nav">` com os links contextuais que a página já tinha). O script remove só o topo antigo (marca + menu), o `#lang-selector` e a `.lang-switcher`; URLs de tradução específicas viram `data-lang-*` no header.

## Uso do script
```
python scripts/aplicar_menu_central.py                       # dry-run de todas as páginas PT
python scripts/aplicar_menu_central.py --only a.html,b.html  # restringe
python scripts/aplicar_menu_central.py --only … --diff-out C:\caminho\etapa.diff
python scripts/aplicar_menu_central.py --only … --apply      # grava, com backup zip
```
- Dry-run é o padrão; nada é gravado sem `--apply`.
- No PowerShell, monte a lista com `Get-ChildItem … | ForEach-Object { caminho relativo com / }` e junte com `-join ','`.
- O script pula páginas de redirecionamento e as que já têm o marcador (rodar de novo não muda nada).
- Variante de topo não reconhecida, ou topo que contém conteúdo, não é tocada e aparece em "Não tocados".

## Procedimento de cada etapa
1. Escopo: liste pastas e contagem. Separe páginas só AT, só NT e mistas quando a etapa for por testamento.
2. Dry-run com `--only`. Mostre: a alterar, puladas e motivo, falhas de prova, e o resumo do que é removido e mantido.
3. **Espere a confirmação do Wagner.**
4. `--apply`: o backup vai para `_backups/menu-central-AAAAMMDD-HHMMSS.zip`. Esse zip **nunca** entra em commit (`_backups/*.zip` está no `.gitignore`).
5. Prova de integridade (feita pelo script, por arquivo): antigo − trechos removidos == novo − blocos inseridos, **byte a byte**, mais contagem de `<img>`. Se falhar, o arquivo não é gravado.
6. Checagem independente no `git diff -U0`: nenhuma linha removida com `<h1-6|p|blockquote|article|section|main|table>`, e nenhuma linha adicionada fora dos blocos marcados.
7. Validação visual (skill `validacao-visual`).
8. Commit separado, por arquivo de mensagem, sem push.

## Cuidados técnicos
- **CRLF**: leia e grave com `newline=""` em Python (`open(p, encoding="utf-8", newline="")`). `read_text()` converte CRLF e estraga o diff.
- **Modo claro**: o site inverte a página inteira com `filter: invert(1) hue-rotate(180deg)` no `<html>` (botão `#dark-toggle`). O cabeçalho **não define cores claras próprias**; se definir, a inversão as escurece de novo.
- **Cabeçalho fixo**: `#site-header` fica no fluxo (`position: relative`) e reserva a altura; a barra interna `.sh-bar` é `position: fixed`. `position: sticky` falhava em vários layouts antigos.
- O menu recolhe abaixo de 1320px; abaixo de 440px os idiomas vão para dentro do menu aberto (o nome do site precisa continuar visível).
- Ícones: não use `<svg>` embutido dentro de `#site-header` (o `all: revert` zera traço e geometria); use máscara CSS.
- **CSS novo para páginas antigas**: enquanto EN/ES não forem tratados, prefixe as regras com `:root[lang|="pt"]` (o `|=` casa `pt` e `pt-BR`; `[lang="pt"]` sozinho **não** casa com `pt-BR`). Quando EN/ES entrarem, remova o prefixo.
- Antes de pôr uma regra num CSS compartilhado (`bloco.css` é carregado por ~4.150 páginas), restrinja-a a um ancestral exclusivo das páginas-alvo e prove onde ela encaixa.

## Pendências conhecidas
- O item "Antigo Testamento" do `MENU` aponta para `/redesign/antigo-testamento.html` até a etapa dos hubs. A branch não vai para a `main` antes disso.
- Páginas mistas (`biblia/index.html`, `personagens/index.html`, `estudos/cruz-de-cristo/`) ficam para a etapa dos hubs e de Estudos.
