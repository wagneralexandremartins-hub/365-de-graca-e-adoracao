# Redesign da navegação — plano de aplicação

Branch: `redesign/navegacao-awexpress` · Escopo desta rodada: **somente páginas em português**.
EN/ES só depois da aprovação do protótipo.

## O que existe no protótipo (`/redesign/`)

| Arquivo | Papel |
|---|---|
| `site-nav.js` | Menu central (fonte única dos 8 itens), recolhimento no mobile, seletor PT/EN/ES, gravação do progresso no NT (`365-progress` e `365-last`) |
| `redesign.css` | Tokens AWEXPRESS, Sora/Inter/JetBrains Mono, cabeçalho, componentes |
| `index.html` | Nova home (todos os textos copiados da home atual) |
| `antigo-testamento.html` | Hub do AT. Os blocos 01 a 07 funcionam como filtro |
| `novo-testamento.html` | Hub do NT: 27 livros por gênero, com os dias da trilha de 260; blocos 08, 09 e 13 e "História da Igreja" (10 a 12) como seção secundária |
| `hub.js` | Filtro dos hubs e destaque do livro em leitura |

`?simular=romanos/8` funciona só em `/redesign/`, para demonstrar o progresso. Sai na versão definitiva.

## Como cada página vai ficar

```html
<head>
  …
  <!-- site-nav:v1 -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Sora:wght@600;700;800&display=swap">
  <link rel="stylesheet" href="/assets/css/site-header.css">
  <script src="/assets/js/site-nav.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
  <header id="site-header" class="site-header">
    <noscript><nav class="nav-fallback">…8 links principais…</nav></noscript>
  </header>
  <nav class="context-nav">…links contextuais que já existiam (← Voltar, breadcrumb)…</nav>
  …conteúdo intocado…
```

- `site-header.css` = só os tokens e o cabeçalho (extraídos de `redesign.css`). Fica com escopo em `.site-header`, para não interferir no `style.css`/`bloco.css` das páginas antigas. Nas páginas legadas o cabeçalho usa `position: sticky` em vez de `fixed`, o que dispensa mexer no `padding` de cada layout.
- Nas páginas em português, o seletor flutuante de idioma (`#lang-selector`, presente em 5.381 páginas) sai, porque o cabeçalho novo já tem PT/EN/ES.

## Script: `scripts/aplicar_menu_central.py`

Segue o modelo de `padronizar_menus.py`:

1. **Simulação (dry-run) por padrão**: mostra o diff e um resumo por variante de menu. Aplicar exige `--apply`. `--only a,b` restringe o escopo.
2. **Alvo**: `*.html` fora de `en/`, `es/`, `_backups/` e `redesign/`, e fora das 149 páginas de redirecionamento (`http-equiv="refresh"`). São cerca de 2.940 páginas.
3. **Classificação**: o script reconhece cada uma das 57 variantes de cabeçalho/menu levantadas na Fase 1. Página com variante **desconhecida não é tocada**; ela vai para o relatório.
4. **Links contextuais preservados**: os links que não são do menu global ("← Voltar ao Pentateuco", "Início › Livros Históricos › 1 Samuel") vão para `<nav class="context-nav">`, com os mesmos textos e destinos.
5. **Idempotente**: o marcador `<!-- site-nav:v1 -->` evita aplicar duas vezes.
6. **Backup**: antes de `--apply`, gera um zip em `_backups/menu-central-AAAAMMDD-HHMM.zip` com os arquivos que serão alterados. A pasta `_backups/` já fica fora do deploy.

## Garantia de que o conteúdo editorial não muda

Para cada arquivo, o script compara **antes e depois**, excluindo só os trechos que ele mesmo substitui (`<head>`, cabeçalho, `#lang-selector`):

- o restante do HTML precisa ser **idêntico byte a byte**;
- o texto visível (`innerText` sem o cabeçalho) também precisa ser idêntico, e a contagem de `<img>` precisa bater.

Se qualquer verificação falhar, o arquivo é revertido e listado. Nenhum texto de estudo passa pelo script.

## Etapas (uma aprovação e um commit por etapa)

1. **Piloto**: 10 páginas, uma de cada variante principal (capítulo do NT, capítulo do AT, índice de livro, índice de bloco, Bíblia ACF, personagens, estudos, mapas, timeline, sobre). Validação visual em desktop e mobile, mais a varredura de overflow pelo DOM.
2. NT em português (cerca de 290 páginas).
3. AT: blocos 01 a 07 (cerca de 1.290 páginas).
4. `biblia/` (1.190 páginas).
5. Demais páginas (blocos 09 a 13, personagens, estudos, raiz).
6. Home e hubs: `/redesign/index.html` → `/index.html`, com a home atual preservada como `/index-anterior.html`. Hubs em `/antigo-testamento/` (pasta nova) e `/novo-testamento/` (hoje é só um redirecionamento para `/08-novo-testamento/`; **decisão pendente**).
7. EN/ES, só após aprovação.

**Para desfazer**: `git revert` do commit da etapa, ou restaurar o zip da etapa.

## Decisões do Wagner (05/10/2026)

- Textos de navegação aprovados. Card Gênesis → `/02-pentateuco/genesis/`. Stats: "+2.900 páginas em português" (2.942 contadas pelo script).
- Blocos 10 a 12 vão para Estudos, no grupo "História da Igreja" (`/estudos/#historia-da-igreja`). O hub do NT fica só com os 27 livros, mais o link "Depois do NT".
- `/novo-testamento/` continua como redirecionamento. O hub do NT fica em `/08-novo-testamento/`, com a tabela dos 27 livros e o parágrafo "Estrutura do NT" com texto idêntico, só estilizados.
- O modo claro (`#dark-toggle`, inversão por `filter`) é mantido. O cabeçalho não define cores claras próprias.
- Rótulos "Bloco NN" dos índices 08 a 13 corrigidos para a numeração das pastas. Parágrafos de estudo que citam "Bloco 08" e "Bloco 11" **não** foram alterados.

## Piloto (10 páginas): aplicado, sem commit

Backup: `_backups/menu-central-20261005-140700.zip`. A prova passou nas 10 páginas, e uma segunda execução não altera nada.
Validação: 66 combinações (11 páginas × 6 larguras: 1440, 1366, 1321, 1280, 768 e 390). Sem overflow causado pelo cabeçalho. A barra fica no topo após a rolagem. Modo claro funcionando.
Mudança técnica: `sticky` falhava em layouts antigos. Agora `#site-header` reserva a altura e `.sh-bar` é `position: fixed`.

Problemas **anteriores** ao piloto (o site no ar é igual):
- `08-novo-testamento/mateus/capitulos/*` e `03-historicos/1samuel/cap-*`: conteúdo sem estilo (classes sem CSS).
- Overflow a 390px: URLs longas nas referências de Números 1 e a tabela do hub do NT.

## Decisão editorial pendente: texto-base em NVI ou ARA (41 páginas)

A tradução padrão do site é a **ACF** (decisão de 05/10/2026). Estas 41 páginas mostram o texto bíblico em outra tradução. **Ficam como estão** até o Wagner decidir: trocar o texto é mudança editorial.

**NVI (36 páginas)**
- `02-pentateuco/genesis/estudos/` (34): `01_Genesis_4_1_5_Caim_e_Abel_Adoracao_e_Aceitacao.html`, `01_Genesis_5_1_32_Genealogia_de_Adao.html`, `01_Genesis_5_1_4_Introducao_e_Imagem_de_Deus.html`, `02_Genesis_4_6_8_Pecado_a_Porta_e_o_Homicidio.html`, `02_Genesis_5_5_8_Adao_a_Sete_Continuidade.html`, `genesis-07`, `08`, `09`, `13`, `15`, `17`, `18`, `19`, `21`, `22`, `23`, `24`, `26`, `28`, `30`, `33`, `34`, `36`, `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44`, `48`, `49`, `50` (todos `.html`)
- `02-pentateuco/exodo/bloco-01/index.html`
- `02-pentateuco/levitico/bloco-01/index.html`

**ARA (5 páginas)**
- `02-pentateuco/genesis/estudos/genesis-06.html`, `genesis-12.html`, `genesis-16.html`, `genesis-47.html`
- `genesis/genesis-1.html`

Observação: `02-pentateuco/genesis/estudos/genesis-20.html` cita "(Gênesis 20:1-18, NVI)" numa citação, sem declarar texto-base. Fora da lista: 26 páginas que citam NVI/ARA só como fonte, bibliografia, comparação ou descrição das traduções (corretas como estão).

## Limpeza prioritária (registrada em 05/10/2026; nada alterado ainda)

Estas páginas **não devem ser alteradas** até decisão do Wagner. Todas ficaram fora do menu central.

| Página(s) | Problema |
|---|---|
| `genesis/genesis-12.html` a `genesis/genesis-50.html` (39) | Conteúdo mínimo (~700 bytes: título + "Conteúdo completo do capítulo N…") com `canonical` e anúncio do AdSense. Conteúdo raso indexado: risco de SEO e de política do AdSense. |
| `busca/index_backup.html` | Cópia de backup da busca, **publicada no site** (o deploy não exclui `*_backup.html`). |
| `02-pentateuco/genesis/estudos/pasted_content.html` | Nome de arquivo colado por engano; dois `<title>` ("pasted_content" e "Projeto 365"). |
| `timeline-component.html`, `timeline-genesis-1.html` (raiz) | Fragmentos sem `<html>`/`<body>`, publicados como páginas. |

## Pendências para a Fase 2 (anotadas a pedido do Wagner)

- **Bug no índice de busca** (`assets/js/nav.js`): as URLs usam `1-corintios`, mas a pasta é `1corintios`. Revisar todos os livros com número (1/2 Coríntios, 1/2 Tessalonicenses, 1/2 Timóteo, 1/2 Pedro, 1/2/3 João, 1/2 Samuel, 1/2 Reis, 1/2 Crônicas, 1/2 Macabeus) e testar cada URL do índice contra o disco.
- **Revisão das páginas com estilos inline** (2.933 com `<style>` próprio): checar visualmente, por amostragem, o conflito com Sora/Inter e com os tokens novos.
- Itens já listados no briefing: modelo de introdução das cartas paulinas (piloto 1 Tessalonicenses ou Filemom), títulos "Capítulo N" em Romanos, "1 capitulos" em Filemom, menu do NT com 8 livros, "próximo" de Filemom → Hebreus 1, faixa de data de Gálatas, personagens que faltam (Timóteo, Tito, Onésimo, Barnabé, Silas, Priscila e Áquila).
