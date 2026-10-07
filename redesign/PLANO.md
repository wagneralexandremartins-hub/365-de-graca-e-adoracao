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

## Checklist final do merge na `main`

Nada vai à `main` sem ordem explícita do Wagner. Marcar cada item antes de abrir o PR.

**A. Pendências de conteúdo e navegação (na branch)**
- [x] Trocar o link do AT para `/antigo-testamento/` nas 2.888 páginas, no `site-nav.js` e no `aplicar_menu_central.py` (`scripts/trocar_link_at.py`; commits `a1592ef9` e `32f4e237`, push em 07/10; prova byte a byte 2.888/2.888).
- [x] Hub do NT real (`08-novo-testamento/index.html`): mesma estrutura do hub do AT, `<head>` mantido (só os estilos antigos trocados por `site.css`), faixa `context-nav` removida só nesta página; prova de textos idênticos (commit `36cdb569`, 07/10).
- [x] Home real (`index.html`): `<head>` mantido (só o `<style>` antigo trocado por `site.css`), corpo no layout do protótipo, links finais `/antigo-testamento/` e `/08-novo-testamento/`; "A Jornada" e "+2.900 Páginas em português" por decisão do Wagner (commit `7ee6ed59`, 07/10). Sem `index-anterior.html`. favicon, og-image e og-cover ficam para uma etapa própria no site inteiro.
- [x] `sitemap.xml`: incluir `/antigo-testamento/` (commit `064bb6f7`, 07/10; o hub do NT já constava como `/08-novo-testamento/index.html`).
- [ ] Decidir: botão "Começar Dia 1 ›" só na home e nos hubs (como está) ou em todas as páginas.

**B. Validação final (na branch, servidor local)**
- [x] Varredura de links internos de todas as páginas PT (nenhum 404 novo): 2.943 páginas, 57.119 links; 0 quebrados novos em relação à `main` (os 1.325 pares quebrados são todos antigos, 1.196 deles `/styles.css`). Menu, trilha de 260 capítulos e "Começar Dia 1" conferidos (07/10).
- [x] Amostra visual (skill `validacao-visual`): home, hubs, 1 página de cada etapa, 1280/768/390px, claro e escuro. Feita em 07/10 (home, hubs AT/NT, Gênesis, Romanos, estudo, Apócrifos, busca); só problemas antigos (ver Limpeza prioritária).
- [x] `git status` limpo; nenhum `_backups/*.zip` em commit; `redesign/` fora do deploy (`pages.yml`). Conferido em 07/10; nenhuma página publicada referencia `/redesign/`.

**C. GitHub (Settings, feito pelo Wagner)**
- [x] Branch padrão do repositório: `(root)` → `main`. Feito pelo Wagner; conferido em 07/10 (`default_branch = main`). A antiga `(root)` aparece agora como `(main)` (mesmo commit `501c8730`).
- [x] Pages › Source: "Deploy from a branch" (`(root)`) → **"GitHub Actions"**. Conferido em 07/10 (`build_type = workflow`).
- [x] Conferir que o ambiente `github-pages` continua aceitando deploy só da `main`. Conferido em 07/10 (política de branch: só `main`).

**D. Merge**
- [x] Antes do merge: marcar o estado atual da `main` com uma tag (`git tag pre-redesign ec2c3181` e `git push origin pre-redesign`). Tag no GitHub em `ec2c3181` (07/10).
- [x] Push da branch e PR **para a `main`** (o GitHub vai sugerir `(root)` enquanto ela for a padrão: trocar). PR #1, de `redesign/navegacao-awexpress` (`d721e79f`) para `main`: 45 commits, 2.919 arquivos (2.892 modificados, 27 novos, 0 removidos).
- [x] Revisar o resumo do PR (arquivos e commits) com o Wagner. Sem conflitos; lista de arquivos igual ao diff local, nada fora do esperado.
- [x] Merge com **merge commit** (não squash), para a reversão ser um único `revert`. **Merge `6101ab89`** (PR #1, pais `ec2c3181` + `d721e79f`), em 07/10/2026 às 18h26, com ordem do Wagner. Branches mantidas.
- [x] Acompanhar o workflow "Deploy GitHub Pages" até "success". Build e deploy com sucesso; site no ar = `6101ab89` às 18h27 de 07/10 (home, hubs, Mateus, `site-nav.js` e `sitemap.xml` conferidos byte a byte; `/redesign/` e `/CLAUDE.md` dão 404).

**E. Depois do deploy (site no ar)**
- [x] Abrir home, hubs AT/NT, um capítulo do NT, um do AT, Bíblia, Estudos; desktop e celular; modo claro. Conferido pelo Wagner no ar em 07/10: home, hubs AT e NT, capas de Juízes, Mateus, Marcos, Lucas, João e Romanos, celular e modo claro.
- [x] Testar "Continue de onde parou" (abrir um capítulo do NT e voltar à home). Conferido pelo Wagner no ar em 07/10.
- [x] Conferir `https://365gracaeadoracao.com/antigo-testamento/` e o canonical. Página no ar idêntica à da `main` (canonical `/antigo-testamento/`), 07/10.
- [ ] Nos dias seguintes: Search Console (erros de cobertura) e AdSense (anúncios aparecendo). Em aberto: acompanhar a partir de 08/10.

## Plano de reversão (se algo der errado depois do merge)

O site é estático e o deploy publica a `main`. Reverter = devolver a `main` ao estado anterior e deixar o workflow publicar de novo (~1 minuto). Nenhum dado externo é afetado.

1. **Pelo GitHub (mais simples):** abrir o PR mesclado → botão **"Revert"** → cria um PR de reversão → mesclar na `main`. O deploy roda sozinho.
2. **Pela linha de comando (com ordem do Wagner):**
   ```
   git checkout main && git pull
   git revert -m 1 <sha-do-merge>        # desfaz o merge inteiro num commit novo
   git push origin main                  # dispara o deploy do site anterior
   ```
3. **Conferir:** workflow em "success" e o site com a home antiga. A tag `pre-redesign` marca o ponto de volta para comparação (`git diff pre-redesign main` deve ficar vazio, salvo commits posteriores).
4. **Não usar** `git push --force` na `main` nem deploy manual de outra branch (o ambiente só aceita a `main`).
5. A branch `redesign/navegacao-awexpress` continua existindo: corrige-se nela e repete-se o checklist.
6. Se a fonte do Pages tiver sido trocada para "GitHub Actions" e isso for a causa do problema, voltar em Settings › Pages (isso independe do revert do código).
7. Correção pontual de página: os zips em `_backups/` (só na máquina local) guardam cada página como estava antes de cada etapa.

## Estado em 06/10 (fim do dia)

**Feito**
- Capa 3D aplicada nas páginas de abertura de **17 livros**: Pentateuco (5) + Históricos canônicos (12: Josué, Juízes, Rute, 1–2 Samuel, 1–2 Reis, 1–2 Crônicas, Esdras, Neemias, Ester). Capítulos da capa vindos do cânon. Tobias, Judite e 1–2 Macabeus ficaram fora (duplicados em `03-historicos` e `06-apocrifos`, decisão pendente).
- CSS em `assets/css/capa-livro.css` (tudo preso à capa: coluna de leitura, grades do Êxodo, título do Deuteronômio no celular); script `scripts/aplicar_capa3d.py` (dry-run, `--apply`, `--only`, bloco `<!-- capa3d:v1 -->`, prova byte a byte).
- Validação: 17/17 sem rolagem horizontal em 1280/768/390/360, escuro e claro; desktop inalterado.
- Commits: `3e602f64` (protótipo + CSS), `f63a6912` (piloto Gênesis + script), `c8bcca86` (notas de limpeza), `83713f7d` (lote de 16), `23969271` (Deuteronômio), `66685bd5` (Êxodo/Deuteronômio resolvidos).
- **Push da branch** `redesign/navegacao-awexpress` em `66685bd5`. **`main` intacta em `ec2c3181`**; `(root)` não tocada; nenhum deploy disparado.

**Pendências**
1. Opcional: capa em mais 2 livros (sugestão: Salmos e um Evangelho), com o mesmo procedimento (dry-run, confirmação, validação, commit separado).
2. Faixa de números desalinhada em Juízes e provavelmente nos outros 9 livros `main.wrap` (ver Limpeza prioritária).
3. Modo claro de Rute e Josué (cartão de introdução e faixas coloridas mudam de tom pela inversão global).
4. Checklist do merge (seção "Checklist final do merge na `main`"):
   - **Wagner, no GitHub:** trocar a branch padrão para `main` e o Pages para "GitHub Actions". Conferido em 06/10: a branch padrão ainda é `(root)` e o Pages ainda é *legacy* apontando para `(root)`.
   - Troca do link do AT em 2.888 páginas (script `trocar_link_at.py`, dry-run OK, não aplicado).
   - Hub do NT e home reais.
   - PR da branch para `main` (não para `(root)`).
   - Merge **só com OK explícito do Wagner**.

## Tarefa de amanhã (06/10/2026): capa 3D de livro

Criar uma **capa 3D de livro, só em CSS**, no topo das **páginas de abertura de cada livro** da Bíblia (não nos capítulos).

- **Antes de qualquer alteração**, fazer apenas o mapeamento somente leitura das páginas de abertura que o Wagner pedir, e parar no relatório.
- Mapeamento já feito em 05/10 (só leitura): o padrão recomendado é `<bloco>/<livro>/index.html` (`02-` a `06-` e `08-novo-testamento/`), que cobre os 66 livros canônicos uma vez cada. A confirmar com o Wagner:
  - Gênesis: `02-pentateuco/genesis/index.html` (o `genesis/index.html` da raiz é um estudo temático).
  - Deuterocanônicos: `06-apocrifos/` (as cópias em `03-historicos/` ficariam sem capa).
- Nome, testamento e número de capítulos da capa devem vir de uma tabela única de livros, não do texto de cada página (Deuteronômio cita "187" antes da contagem real; Gênesis e Salmos não mostram a contagem no formato padrão).
- Sem criar páginas novas. Mesmo procedimento das etapas anteriores: dry-run, confirmação, validação e commit separado.

## Limpeza prioritária (registrada em 05/10/2026; nada alterado ainda)

Estas páginas **não devem ser alteradas** até decisão do Wagner. Todas ficaram fora do menu central.

| Página(s) | Problema |
|---|---|
| `genesis/genesis-12.html` a `genesis/genesis-50.html` (39) | Conteúdo mínimo (~700 bytes: título + "Conteúdo completo do capítulo N…") com `canonical` e anúncio do AdSense. Conteúdo raso indexado: risco de SEO e de política do AdSense. |
| `busca/index_backup.html` | Cópia de backup da busca, **publicada no site** (o deploy não exclui `*_backup.html`). |
| `02-pentateuco/genesis/estudos/pasted_content.html` | Nome de arquivo colado por engano; dois `<title>` ("pasted_content" e "Projeto 365"). |
| `02-pentateuco/genesis/estudos/pasted_file_FffSUA_image.html`, `pasted_file_V6Gujv_image.html`, `pasted_file_aNGcVD_image.html`, `pasted_file_llU4dO_image.html`, `pasted_file_roMaD4_image.html` (5) | Arquivos de imagem colados por engano e embrulhados no modelo de página: cabeçalho HTML normal (com `canonical` e AdSense) seguido de dados binários com 1.054 a 1.185 bytes nulos cada. Título = nome do arquivo (o de `roMaD4` saiu ilegível). O git as trata como binárias (diff não aparece). Publicadas no site, fora do `sitemap.xml`. Receberam o menu central e a troca do link do AT com prova byte a byte (registrado em 07/10/2026). |
| `08-novo-testamento/index.html` (canonical) | O canonical é `https://365gracaeadoracao.com/08-novo-testamento/index` (sem `.html`), mas o `sitemap.xml` lista `/08-novo-testamento/index.html`. Alinhar os dois na etapa de SEO (registrado em 07/10/2026). |
| `sitemap.xml` (`lastmod` e cabeçalho) | Os `lastmod` das páginas alteradas no redesign continuam em 2026-05-26, e o comentário do topo diz "Gerado em 2026-05-26 · Total de páginas: 4151" (são 4.152 desde 07/10). Atualizar na etapa de SEO (registrado em 07/10/2026). |
| `06-apocrifos/index.html`, `busca/index.html` | Rolagem horizontal a 390px: Apócrifos passa 6px; Busca passa 31px (grade `.indice-item` com 2 colunas de 180px). Iguais na `main` (não causadas pelo redesign). Corrigir por CSS depois (registrado em 07/10/2026). |
| `estudos/` e subpáginas | Sem o botão de modo claro (`#dark-toggle`): o modo claro escolhido no resto do site não se aplica nessas páginas (registrado em 07/10/2026). |
| Textos para decisão do Wagner (**não alterar**) | `busca/index.html` mostra "1.627+ Páginas no projeto", enquanto a home diz "+2.900 Páginas em português". O rodapé dos estudos diz "compatíveis com Vercel" (o site está no GitHub Pages). Registrado em 07/10/2026. |
| `timeline-component.html`, `timeline-genesis-1.html` (raiz) | Fragmentos sem `<html>`/`<body>`, publicados como páginas. |
| `og:image`/`twitter:image` em 2.825 páginas | Apontam para `assets/img/og-cover.jpg`, que **não existe** (404 no site no ar): compartilhamentos saem sem imagem. O arquivo existente é `assets/img/og-image.png`. |
| `03-historicos/juizes/index.html` (e provavelmente os outros 9 livros com `main.wrap`: 1–2 Samuel, 1–2 Reis, 1–2 Crônicas, Esdras, Neemias, Ester) | Faixa de números ("21 Capítulos · 618 Versículos · ~1380–1050 a.C. · 12 Juízes Principais") sem estilo, um item por linha; selo, título e subtítulo deslocados para a esquerda no cartão de abertura. Já existia antes da capa 3D (registrado em 06/10/2026). Tratar numa etapa própria, depois do lote da capa. |
| `03-historicos/rute/index.html`, `03-historicos/josue/index.html` | No modo claro, o cartão de introdução de Rute fica escuro e as faixas coloridas de Josué (e de Rute) mudam de tom, por causa da inversão global do site (`filter: invert` no `<html>`) sobre cores fixas da página. Não afeta a capa 3D (registrado em 06/10/2026). |
| ~~`02-pentateuco/deuteronomio/index.html`~~ | ✅ **Resolvido em 06/10/2026** (commit `23969271`). Rolagem horizontal a 390px: o título da página ("📜 DEUTERONÔMIO", 3em) não cabia na coluna. Corrigido no `assets/css/capa-livro.css`, preso à capa: `clamp(1.4rem, 6.5vw, 3em)` — só reduz no celular; no desktop continua 3em. |
| ~~`02-pentateuco/exodo/index.html`~~ | ✅ **Resolvido em 06/10/2026** (commit `83713f7d`). Rolagem horizontal no celular: as grades da página (`.study-options` 400px, `.blocks-grid` 350px) não cabiam na tela. Corrigido no `assets/css/capa-livro.css`, preso à capa: mínimo da grade limitado à largura da coluna. |

## Pendências para a Fase 2 (anotadas a pedido do Wagner)

- **Bug no índice de busca** (`assets/js/nav.js`): as URLs usam `1-corintios`, mas a pasta é `1corintios`. Revisar todos os livros com número (1/2 Coríntios, 1/2 Tessalonicenses, 1/2 Timóteo, 1/2 Pedro, 1/2/3 João, 1/2 Samuel, 1/2 Reis, 1/2 Crônicas, 1/2 Macabeus) e testar cada URL do índice contra o disco.
- **Revisão das páginas com estilos inline** (2.933 com `<style>` próprio): checar visualmente, por amostragem, o conflito com Sora/Inter e com os tokens novos.
- Itens já listados no briefing: modelo de introdução das cartas paulinas (piloto 1 Tessalonicenses ou Filemom), títulos "Capítulo N" em Romanos, "1 capitulos" em Filemom, menu do NT com 8 livros, "próximo" de Filemom → Hebreus 1, faixa de data de Gálatas, personagens que faltam (Timóteo, Tito, Onésimo, Barnabé, Silas, Priscila e Áquila).
