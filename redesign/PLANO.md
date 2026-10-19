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
- [x] Decidir: botão "Começar Dia 1 ›" só na home e nos hubs (como está) ou em todas as páginas. Resolvido pelo Wagner: fica só na home e nos hubs.

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

## Estado em 07/10 (fim do dia)

**Redesign no ar.** PR #1 (`redesign/navegacao-awexpress` → `main`) mesclado com merge commit **`6101ab89`** em 07/10/2026 às 18h26; workflow "Deploy GitHub Pages" com sucesso, site publicado às 18h27.
- `main` (GitHub): `6101ab89`.
- Branch `redesign/navegacao-awexpress`: `d32764b3` no GitHub ao fim de 07/10 (antes deste registro).
- Tag `pre-redesign`: `ec2c3181` (a `main` anterior ao redesign; ponto de volta).
- No ar: menu central em ~2.940 páginas PT, hubs `/antigo-testamento/` e `/08-novo-testamento/`, nova home, capa 3D em 44 livros (17 AT + 27 NT), `sitemap.xml` com `/antigo-testamento/`.

## Estado em 08/10

Inventário somente leitura em `redesign/INVENTARIO.md` (commit `45c8381c`). Frente 1 (SEO técnico) iniciada, um item por vez, sempre com dry-run e OK do Wagner antes do `--apply`.

| Commit | Conteúdo |
|---|---|
| `82c14da1` | `scripts/corrigir_hifen_busca.py` (dry-run padrão, `--apply` com backup) |
| `bac53d98` | **Item 1 — bug do hífen:** 9 links em `assets/js/nav.js` e 12 em `busca/index.html` (1–2 Samuel, 1–2 Reis, 1–2 Coríntios, 1–2 Pedro, 1 João, Cântico → `canticos`); Davi, Salomão, Elias e Pedro (personagens) apontam para `/personagens/*.html`. Backup `_backups/hifen-busca-20261008-125328.zip`. |
| `ba066ba0` | `scripts/seo_arquivos_ausentes.py` (2a + 2b numa passada) |
| `bd34f8e1` | **Item 2b — `/styles.css`:** linha removida de 1.196 páginas (1.190 `biblia/` + 6 blocos de Êxodo); o arquivo nunca existiu (404). Prova byte a byte 1.196/1.196. Backup `_backups/seo-2a2b-20261008-130812.zip`. |
| `5716d119` | **Item 2a — imagens:** `assets/img/og-cover.jpg` e `og-image.jpg` (JPEG do `og-image.png`, mesma arte, 1200×630; enquadramento aprovado) e `favicon.png` (cópia do `apple-touch-icon.png`). Nenhuma página editada. |

- Push feito: `origin/redesign/navegacao-awexpress` = `5716d119`. `main` segue `6101ab89`, ou seja, **essas correções ainda não estão no ar** (exigem novo PR e merge, só com ordem do Wagner).
- Validação: busca testada no navegador (`?q=` Samuel, Reis, Coríntios, Cântico, Davi, Salomão, Elias, Pedro); 14 destinos e 3 imagens com 200. Prints antes/depois (escuro e claro) de `biblia/gn/gn-01`, `sl/sl-23`, `1co/1co-13` e `exodo/bloco-01`: 7 de 8 idênticos pixel a pixel; o bloco de Êxodo no escuro difere só no anti-aliasing do texto do cabeçalho (487 px, sem mudança de layout).
- **Decisão provisória do Wagner (08/10): formato oficial das URLs sem `.html`**, como os canonicals atuais. Nenhuma página alterada por isso.
- **Item 3 — sitemap alinhado ao canonical:** ✅ feito, sem push. Commits `fc10aa21` (`scripts/sitemap_canonical.py`) e `07cee8bc` (`sitemap.xml`). Backup `_backups/sitemap-canonical-20261008-163709.zip`. 4.034 de 4.152 `<loc>` passaram à URL do canonical: EN/ES `/pasta/` (2.506), PT capítulos sem extensão (1.216), PT índices `/pasta/index` (299) e `/pasta/` (13). Fora de `<loc>` o arquivo é idêntico byte a byte (`lastmod`, `priority`, ordem e CRLF intactos). Amostra no ar: 24 URLs novas com 200, sem redirect.
  - **116 URLs ficaram com `.html` no sitemap** (decisão pendente):
    - **83 páginas sem canonical:** 27 EN `*-block-N`, 27 ES `*-bloque-N`, `03-historicos/1samuel/capitulos/capitulo-29.html` e, em destaque, **os 28 capítulos de Mateus** (`08-novo-testamento/mateus/capitulos/capitulo-01` a `28`): o primeiro livro do NT inteiro sem canonical.
    - 29 páginas de `estudos/` (índice, 6 categorias, 22 estudos) com canonical `.../index.html`.
    - 4 com canonical de pasta sem barra (`autismo-e-fe`, `como-estudar-a-biblia`, `ebook-4-passos`, `loja-365`), que no ar respondem 301 para `/pasta/`; ficaram de fora para não pôr redirect no sitemap.
  - **Formato `/pasta/index` em 299 índices PT:** é o canonical atual e responde 200, mas é atípico. O limpo seria `/pasta/`, o que exige editar o canonical dessas páginas e rodar o script do sitemap de novo. Decisão do Wagner.
- Skill nova `lote-seguro` com o ritual dos lotes; `seo-limpeza` atualizada com as decisões de 08/10 (commit `b94f8e93`).
- **Canonical de Mateus:** ✅ concluído. Commits `df0235e6` (`scripts/canonical_mateus.py`) e `443900a1` (28 páginas). Uma linha `<link rel="canonical" href=".../08-novo-testamento/mateus/capitulos/capitulo-NN">` abaixo do `<meta name="description">` em `capitulo-01` a `28` (109 bytes, CRLF). Prova byte a byte 28/28; prints dos capítulos 1, 15 e 28 (escuro e claro) idênticos pixel a pixel. Backup `_backups/canonical-mateus-20261008-170320.zip`.
- **Sitemap × Mateus:** ✅ commit `da33334b`. As 28 URLs de Mateus passaram para a forma sem `.html`; fora de `<loc>` idêntico byte a byte. Backup `_backups/sitemap-canonical-20261008-171146.zip`. **Restam 88 URLs com `.html`:** 55 sem canonical (27 EN `*-block-N`, 27 ES `*-bloque-N`, 1 Samuel 29), 29 de `estudos/` e 4 de pasta sem barra.
- **Item 4 — hreflang:** ✅ feito. Commits `9da75802` (`scripts/hreflang_item4.py`) e `e7158fff` (3.168 arquivos: 1.000 EN, 1.000 ES, 1.168 PT). Backup `_backups/hreflang-20261008-171332.zip`.
  - H1: 1.843 hrefs corrigidos para o canonical do equivalente (pt-BR na forma antiga `/livro/capitulo-N/` 1.494; Pentateuco `/capitulo-NN/index` 328; nome de livro em inglês no NT 14; EN→ES `matthew/romans/revelation` → `mateo/romanos/apocalipsis` 7). Os capítulos 4–28 de Mateus já ficaram certos com o canonical novo.
  - H2: 164 alternates pt-BR removidos: Gênesis 100 (o PT não tem página por capítulo), 1–2 Macabeus 62 (apontavam para `06-apocrifos/1macabeus/`, inexistente; usar as cópias de `03-historicos` depende da decisão das duplicatas) e 1 Samuel 29 2 (página truncada).
  - H3: 1.168 páginas PT ganharam pt-BR/en/es logo abaixo do canonical.
  - Prova: 3.168/3.168 idênticos ao backup fora das linhas de hreflang, CRLF preservado; nova simulação dá 0 mudanças; estado final com 0 violações da regra no escopo. Prints de Salmo 23 PT/EN/ES (escuro e claro) idênticos.
  - Fora do escopo, não editado: `estudos/` e home (31 pt-BR com canonical `.html` e 64 sem reciprocidade com `en/estudos` e `es/estudios`).
  - Se o formato `/pasta/index` mudar, rodar de novo `sitemap_canonical.py` e `hreflang_item4.py`.
- **1 Samuel 29 PT truncada** (`03-historicos/1samuel/capitulos/capitulo-29.html`; relatório só de leitura, nada alterado): 4.139 bytes contra ~22–23 KB dos capítulos 28 e 30. Começa no byte 0 no meio de uma frase (" (1 Sm 29:5) ressoava na mente dos filisteus…"); não tem `<!DOCTYPE>`, `<html>`, `<head>` nem abertura de `<body>`, portanto não tem título, description, canonical, CSS, AdSense nem menu central. Restam os 2 últimos parágrafos da dissertação (1.227 caracteres), os botões 28 · livro · 30, o rodapé e os scripts (modo escuro, WhatsApp); o fechamento está íntegro. Faltam o cabeçalho do capítulo, o Texto Bíblico (ACF), o Contexto Histórico e Geográfico, os mapas e o início da Dissertação. Já nasceu truncada no primeiro commit (`c0c808c7`, 26/03/2026); não há versão completa no git. **A reconstrução é decisão editorial do Wagner**; material de apoio: `biblia/1sm/1sm-29.html` (texto ACF).
- Push: branch enviada em 08/10 (`origin/redesign/navegacao-awexpress` = `0732def8`), sem PR e sem merge; `main` segue `6101ab89`. Nada disso está no ar até PR e merge na `main`.
- **Pendência — Gênesis EN/ES sem link pt-BR:** as 100 páginas `en/genesis-1` a `50` e `es/genesis-1` a `50` perderam o hreflang pt-BR (H2) porque o PT de Gênesis só tem páginas por bloco (`02-pentateuco/genesis/bloco-01` a `06`), não por capítulo. Decisão do Wagner: criar páginas PT por capítulo, apontar para o bloco (não é equivalente 1:1, a regra não permite) ou deixar sem pt-BR.
- **Pendência — 61 arquivos versionados em `_backups/`** (commits de 09/04/2026, anteriores ao redesign). Não vão ao ar: o `pages.yml` exclui `_backups/` do deploy, e `https://365gracaeadoracao.com/_backups/2026-04-15_10-51-26_blocos_index.html` responde 404 (checado em 08/10). O `.gitignore` só ignora `_backups/*.zip`, não a pasta inteira. Decisão do Wagner: tirar do repositório (`git rm --cached`, mantendo a cópia local) e ignorar `_backups/`, ou deixar como está.

## Estado em 08/10 (fim do dia)

**Entregue**
- PR #2 mesclado na `main` com merge commit `7ce48cd2` (pais `6101ab89` + `8e3df475`; 20 commits, 4.379 arquivos). Workflow "Deploy GitHub Pages" (run 37843120886): build e deploy **success** às 20:56 UTC.
- Conferência no ar, só com curl: hreflang do Salmo 23 em PT/EN/ES correto e recíproco; `sitemap.xml` com 4.152 URLs (88 ainda com `.html`), igual ao do repositório; canonical de Mateus 1 presente; `og-cover.jpg`, `og-image.jpg` e `favicon.png` com 200; 1 Samuel 29 continua abrindo (truncada, como estava).
- Rollback: tag `pre-redesign` (`ec2c3181`) ou `git revert -m 1 7ce48cd2`, só com ordem do Wagner.

**Search Console**
- Domínio verificado via TXT na Hostinger: **manter os dois registros TXT**.
- Sitemap `https://365gracaeadoracao.com/sitemap.xml` reenviado em 08/10.
- Existe uma linha antiga com defeito (`sitemap.xml.`, com ponto no fim, de 23/02/2026): remover no Search Console.

**Linha de base (08/10/2026)**
- 1.483 cliques desde julho.
- Últimos 28 dias: 585 cliques (+19%) e 48,3 mil impressões (+27%).
- 3.693 páginas indexadas e 9.319 não indexadas.
- Cliques por país: EUA 14%, Brasil 12%, México 12%, Venezuela 9%, Colômbia 8%.
- Páginas mais clicadas são ES: 1 Crónicas 18, Ezequiel 16, Jeremías 6, Deuteronomio 3.

**Novas pendências**
- (a) Acentos faltando nos títulos ES (ex.: "Cronicas", "Dias de Gracia y Adoracion"): contar quantos títulos ES e EN são afetados, sem alterar nada, e propor simulação.
- (b) Símbolo da Graça girando em CSS (`rotateY`) no hero da home, com `prefers-reduced-motion`, primeiro numa página de teste.
- (c) Tirar os 61 arquivos de `_backups/` do git e pôr `_backups/` no `.gitignore` (via PR).
- (d) Revisar a qualidade dos textos ES, começando pelas páginas mais clicadas.
- (e) Ler a aba Indexação > Páginas do Search Console e classificar os motivos de não indexação.

**Decisões do Wagner (não alterar texto sem OK)**
- Macabeus, Tobias e Judite duplicados (`03-historicos` × `06-apocrifos`).
- Reconstrução da 1 Samuel 29.
- Gênesis EN/ES: 100 páginas sem pt-BR.
- `/pasta/index` (299 índices PT) contra `/pasta/`.
- 55 páginas sem canonical (27 EN `*-block-N`, 27 ES `*-bloque-N`, 1 Samuel 29).

**Próximo passo de amanhã:** ler Indexação > Páginas no Search Console e escolher a próxima frente: símbolo girando, acentos ES ou busca com índice gerado.

## Próximos passos

1. Acompanhar Search Console (erros de cobertura) e AdSense (anúncios aparecendo) a partir de 08/10; depois do próximo merge, reenviar o sitemap.
2. Limpeza de SEO: decisões sobre os 55 sem canonical (blocos EN/ES e 1 Samuel 29), `/pasta/index` (299) e os 88 URLs com `.html`; hreflang de `estudos/`; Gênesis EN/ES sem pt-BR (100 páginas); 61 arquivos de `_backups/` versionados; reconstrução da 1 Samuel 29 (editorial); `lastmod` do sitemap e páginas `genesis/genesis-NN` (ver Limpeza prioritária). Favicon, og-image/og-cover, `/styles.css`, sitemap × canonical, canonical de Mateus e hreflang dos capítulos resolvidos em 08/10.
3. **Próxima frente sugerida: busca com índice gerado** (frente 2 do `INVENTARIO.md`): índice JSON estático gerado a partir das páginas reais (title/H1/description/URL), um script de busca só, aposentando os índices manuais de `busca/index.html` e `assets/js/nav.js` (hoje 76 e 66 entradas, 1,4% do site).
4. Capas 3D dos Poéticos, Profetas e deuterocanônicos (mesmo procedimento da skill `capa-3d-livro`).
5. CSS: faixa de números dos livros `main.wrap`; Apócrifos e Busca no celular (rolagem a 390px); o botão verde flutuante (WhatsApp, canto inferior direito) pode cobrir o botão "próximo capítulo" da barra fixa (visto em Mateus 15 a 1280px).
6. Ideias visuais futuras (não implementar agora):
   - og-cover melhorado, com arte nova (hoje é o `og-image.png` convertido para JPEG).
   - Símbolo da Graça girando sobre o eixo no hero da home, ao lado do cartão "Continue de onde parou", inspirado no cubo do site da AWEXPRESS: `rotateY` em CSS, SVG/PNG leve, parado com `prefers-reduced-motion`. Só depois do merge do SEO, como lote visual separado.
7. Textos para decisão do Wagner: "1.627+ Páginas no projeto" na busca e "compatíveis com Vercel" no rodapé dos estudos.
8. Duplicatas Tobias, Judite e 1–2 Macabeus (`03-historicos` × `06-apocrifos`).
9. Branches `(main)` e `(root)`: a antiga `(root)` aparece no GitHub como `(main)` (`501c8730`); decidir renomear ou apagar.
10. EN/ES (etapa 7), só após aprovação.

## Botões anterior/próximo EN/ES (09/10/2026, branch `fix/botoes-en-es`)

**Descoberta.** No Search Console, a exportação de 404 (`Coverage-Drilldown-2026-10-09.xlsx`, 1.000 URLs de exemplo) mostrou **548 endereços** `/en|es/<livro>-<N>/capitulo-NN.html` (ex.: `/en/luke-14/capitulo-13.html`). Origem: no bloco `<nav class="chapter-nav">` do fim do artigo das páginas EN/ES do NT, os botões anterior/próximo usavam o link relativo `capitulo-NN.html`, que não existe em nenhuma pasta. Outros 32 endereços na raiz (`/en/capitulo-NN.html`, `/es/capitulo-NN.html`, 404 no ar) vêm, provavelmente, do mesmo botão na época do Vercel (`trailingSlash: false`, página servida sem barra final). Os links de baixo da página (`/en/luke-13/`) já estavam certos.

**Correção.** `scripts/corrigir_botoes_en_es.py` (simulação por padrão, `--apply` com OK do Wagner em 09/10): **504 páginas** (EN 249, ES 255) e **918 botões**. Só o valor do href muda, para o capítulo vizinho no formato dos links de baixo (`capitulo-13.html` → `/en/luke-13/`), e só quando a pasta de destino existe. Em 500 páginas o novo href é igual ao link de baixo; as outras 4 (`en/romans-1` a `3`, `en/revelation-1`) não têm link embaixo. Prova byte a byte: 504/504 contra o backup `_backups/botoes-en-es-20261009-123925.zip`, CRLF preservado, nova simulação com 0 mudanças. Servidor local: botões de `en/luke-14`, `es/mateo-20`, `en/romans-2`, `en/luke-1` e `es/mateo-28` abrem com 200. Fora do lote, sem mudança: 106 botões de borda (52 `←` no capítulo 1 e 54 `→` no último) que apontam para `../index.html`; páginas EN/ES do AT (não têm esse bloco).

**Decisão futura do Wagner.** Nas páginas EN/ES, o botão central ("Luke Index", "Índice de Mateo") e os botões de borda usam `../index.html`, que abre o **índice geral** (`/en/index.html`, `/es/index.html`), não o do livro. Não é 404, mas o rótulo promete outra coisa. Opções: manter, trocar o rótulo ou apontar para um índice do livro (hoje não existe página por livro em `en/` e `es/`).

Depois do merge: reenviar o sitemap no Search Console e pedir "Validar correção" no relatório de 404.

## CSS de leitura nos capítulos EN/ES (09/10/2026, branch `feat/css-capitulos-en-es`)

**Diagnóstico.** As páginas de capítulo EN/ES nunca tiveram estilo no conteúdo (desde a criação, `896fb47e`, 26/03/2026): o HTML usa `chapter-main`, `chapter-header`, `verse-block` etc., que só ganharam CSS em `55c00f92` (05/10), restrito a `:root[lang|="pt"]`. Não foi regressão.

**O que mudou (só `assets/css/bloco.css`, nenhuma página editada).**
- As 21 regras `:root[lang|="pt"] .chapter-main …` passaram a valer também para `:root[lang|="en"]` e `:root[lang|="es"]` (lista de seletores; declarações iguais). Atinge as 2.212 páginas EN/ES com `<main class="chapter-main">` (1.106 por idioma).
- Nova regra `:root[lang|="en"] body.bloco-ot, :root[lang|="es"] body.bloco-ot { --accent: #f5c542; --accent-rgb: 245, 197, 66; }`: os capítulos EN/ES do AT (1.980 com `bloco-ot`) não tinham `--accent`/`--accent-rgb`; o âmbar é o mesmo dos títulos inline dessas páginas.
- Sem `?v=` no link: o GitHub Pages serve com `Cache-Control: max-age=600` e ETag.

**Prova de que PT e o resto não mudaram.**
- 4.153 páginas carregam `bloco.css` (pt-BR 1.647, en 1.252, es 1.252, 2 sem `lang`); nenhuma com outro idioma.
- Declarações do `bloco.css` aplicadas a cada elemento (medida determinística, antes = `71506aca`, depois = branch): **iguais** em `lucas/capitulos/capitulo-14` (PT), `salmos/capitulos/salmo-023` (PT) e `en/old-testament` (página com `<style>` próprio), a 1280 e 390 px. HTML do Lucas 14 PT no ar = git, byte a byte.
- As 58 páginas EN/ES com `<style>` próprio não usam `chapter-main` (56 nem carregam `bloco.css`); as 79 com `<body>` sem classe também não (stubs `es/john-N` e blocos do Pentateuco).
- `en/luke-14`, `es/mateo-20`, `en/isaiah-53`: sem rolagem horizontal a 1280, 390 e 360 px, antes e depois.

**Pendências.**
- Trocar o cabeçalho antigo (`topbar`) das páginas EN/ES pelo menu central (`site-nav.js`), como no PT; hoje o seletor de idioma fica sobreposto no canto.
- Modo claro: as páginas EN/ES não têm (o botão 🌙 das páginas do AT grava `data-theme` sem CSS correspondente).
- Ajuste de tamanho/contraste do texto de leitura (`.verse-analysis` em `--muted`, 0,92rem), se o Wagner quiser, valendo para os três idiomas.

## Padrão EN/ES do NT — lote 1: cartas e Apocalipse (13/10/2026, branch `feat/css-cartas-en-es`)

**Decisões do Wagner (13/10).** Ordem dos lotes aprovada: 1) CSS das cartas EN/ES; 2) `site-nav.js` em três idiomas; 3) menu central nos 520 capítulos + homes + estudos EN/ES; 4) barra inferior, modo claro e WhatsApp; 5) homes EN/ES no layout novo (a home EN/ES continua sendo o hub do NT; nenhuma página nova de hub); 6) aberturas de livro EN/ES com capa 3D — fica para depois.

**Diagnóstico.** As 143 páginas PT de capítulo das cartas e do Apocalipse (`.wrap` + `.chapter-hero` + `.versiculo-bloco`) recebem o visual de um `<style>` dentro de cada página; os equivalentes `en/<livro>-N/` e `es/<libro>-N/` não têm esse bloco e apareciam sem estilo (blocos de versículo, cabeçalho do capítulo e breadcrumb crus).

**O que mudou (só `assets/css/bloco.css`, nenhuma página editada).** 15 regras acrescentadas no fim do arquivo (+23 linhas, 0 removidas), com as declarações do `<style>` do PT (sem a parte `.brand` do cabeçalho antigo). Escopo: `:root:is([lang|="en"], [lang|="es"]) body.bloco-08:has(.chapter-hero):has(.versiculo-bloco)`. Script: `scripts/css_cartas_en_es.py` (simulação por padrão; `--apply` com backup `_backups/css-cartas-en-es-20261013-154840.zip`).

**Prova de que PT e o resto não mudaram.**
- Só acréscimo: o arquivo antigo é prefixo exato do novo; só CRLF; o gravado é idêntico, byte a byte, à simulação aprovada; nova simulação depois do apply = 0 mudanças.
- 4.153 páginas carregam `bloco.css` (pt-BR 1.647, en 1.252, es 1.252, 2 com `lang` malformado: Josué 16 e Juízes 9). Varredura do HTML e verificação no Chrome de **todas** as 4.153 (cada página carregada com o CSS novo, perguntando ao navegador quais elementos casam com as regras novas): casam 286 (143 EN + 143 ES), **0 PT**.
- Estilo calculado EN/ES × PT nos elementos de leitura (Rm 8, Ap 1, Ap 22, 1 Jo 1, Hb 11, Fm 1, 2 Tm 4): idêntico; a única diferença é o próprio idioma (`-webkit-locale`).
- Sem rolagem horizontal a 390 px em 6 cartas EN/ES, em João 3 EN e em Romanos 8 PT.

**Fora deste lote (decisão do Wagner, 13/10).** Atos 26 EN/ES (o PT tem CSS próprio de página inteira); navegação e rodapé duplicados no fim das cartas EN/ES (ver no lote 3); Josué 16 e Juízes 9 com `lang` malformado.

**No ar.** PR #10, merge `a2c025b8`, deploy run `38452157647` (success, 13/10 19:06 UTC). Conferido com curl: `bloco.css` no ar = `main` byte a byte (marca `cartas-en-es:v1`, 15 regras); HTML de `en/romans-8`, `es/romanos-8`, `en/revelation-1`, `es/hebreos-11` e Romanos 8 PT no ar = `main`. Rollback: `git revert -m 1 a2c025b8`.

## Piloto do grego koiné em João 3 (13/10/2026, branch `feat/grego-jo3`)

**Decisões do Wagner (13/10).** Texto-base: Textus Receptus de Scrivener (1894). Fonte digital: Door43 `STR/el-x-koine_trs` (CC BY-SA 4.0), a única politônica fiel ao Scrivener 1894 com licença clara (byztxt é domínio público mas ASCII sem acentos; eBible `grctr` é colação St1550/Elz1624/Scr1881; CrossWire TR é Stephanus 1550 com CC BY-NC-SA). Proposta A: grego recolhido abaixo de cada citação, em PT, EN e ES, fonte Gentium Plus. Rótulos e crédito aprovados.

**O que mudou.** `08-novo-testamento/joao/capitulos/capitulo-03.html`, `en/john-3/index.html`, `es/juan-3/index.html` (+46 linhas cada, 0 removidas) e `assets/css/grego.css` (novo). Em cada página: 2 linhas no `<head>` (Gentium Plus + `grego.css`) e, logo depois de cada uma das 4 citações (3:1-3, 3:5-8, 3:16, 3:17-18), um `<details class="grego-tr">` fechado com o grego numerado (`lang="grc"`) e o crédito da licença; tudo entre `<!-- grego-tr:v1 -->`. Script: `scripts/aplicar_grego_jo3.py` (backup `_backups/grego-jo3-20261013-161828.zip`).

**Fonte fixada.** `44-JHN.usfm` do commit `4107626c` do Door43 (SHA-256 `f93ebbc0…`). João 3 completo na fonte (36 versículos), UTF-8 NFC, politônico; comparado palavra a palavra com o byztxt (Robinson, domínio público): 0 diferenças de leitura (só grafia impressa: ἐστί/ἐστίν, οὕτω/οὕτως).

**Prova.** Por página: novo menos os 5 trechos inseridos = original, byte a byte; só CRLF; as 4 citações e as imagens idênticas; arquivos gravados = simulação aprovada; nova simulação = 0 mudanças. No navegador (3 idiomas × 1280/768/390, aberto e fechado): 4 blocos por página, sem rolagem horizontal, Gentium Plus carregada quando o bloco abre (fechado, a fonte nem é baixada); modo claro do PT correto.

**Próximos passos possíveis (só com decisão do Wagner).** Estender a outros capítulos; versão completa dos 36 versículos em `biblia/jo/jo-03.html` (proposta B).

**No ar.** PR #11, merge `c48d4204`, deploy run `38463079906` (success, 13/10 20:28 UTC). Conferido com curl: as três páginas de João 3 no ar = `main` byte a byte; em cada idioma, 4 de 4 `<details class="grego-tr">` logo depois das citações, 10 de 10 versículos idênticos à Door43, rótulo, `lang="grc"` e crédito presentes; `grego.css` no ar = `main`; Gentium Plus (subconjuntos greek e greek-ext) respondendo 200. Rollback: `git revert -m 1 c48d4204`.

## Grego koiné em Mateus (14/10/2026, branch `feat/grego-mateus`)

**Decisões do Wagner (14/10).** Estender a camada do piloto de João 3 a Mateus, Marcos e Lucas, em PT, EN e ES, um PR por Evangelho, começando por Mateus. (a) Páginas de modelo ficam de fora: "N:1" com "Contexto e introdução ao capítulo N" e "N — Teologia Central" (em Marcos "O Servo Sofredor", em Lucas "O Salvador Universal"). (b) O grego mostra a faixa inteira do rótulo, mesmo quando a citação está resumida com reticências. Rótulos, crédito, `<head>` e marca `grego-tr:v1` são os do piloto.

**Diagnóstico (só leitura).** Por idioma: Mateus 28 págs. (12 com citação real, 39 blocos), Marcos 16 (8, 18), Lucas 24 (8, 21); as outras 40 por idioma são de modelo. Rótulos só `C:V` e `C:V-W`; nenhum cruza capítulos. Nenhuma anomalia de estrutura (1 `</head>`, git em LF, cópia local em CRLF). Numeração idêntica no Door43, no byztxt e na ACF do site (`biblia/`) nos 68 capítulos; 0 diferenças de leitura Door43 × byztxt nos três livros. Acréscimo estimado: ~150 KB (Mateus), ~68 KB (Marcos), ~125 KB (Lucas), em LF.

**O que mudou.** Commit `9724a50f`: `scripts/extrair_grego_door43.py` (gera os dados, com SHA-256 das fontes fixado, reprodução byte a byte dos 10 versículos do piloto e conferência contra o byztxt `6049a43b`), `scripts/aplicar_grego_evangelhos.py` (`--livro mateus|marcos|lucas`, simulação por padrão) e `scripts/dados/grego-tr-mateus.json` (94 versículos; 65 iguais ao byztxt, 29 só de grafia, 0 de leitura; Mt 3:3 normalizado em NFC, U+1FD3 → U+0390). Commit `b4777bd9`: 36 páginas (caps. 1–7, 13, 16, 26, 27, 28 × PT/EN/ES), 117 blocos, +1.362 linhas, 0 removidas. Backup `_backups/grego-mateus-20261014-130434.zip`. As 48 páginas de modelo (caps. 8–12, 14, 15, 17–25) ficaram de fora.

**Prova.** Por página: novo menos os trechos inseridos = original, byte a byte; citações e `<img>` idênticas; quebra de linha preservada; grego lido da página = JSON. Gravado = simulação aprovada (36/36); backup = HEAD (36/36); nova simulação = 0 mudanças. Chrome: prints de Mateus 5 (PT/EN/ES, 1280 e 390 px, aberto e fechado) aprovados; 36 páginas a 390 e 360 px com todos os blocos abertos, sem rolagem horizontal, Gentium Plus carregada.

**Próximos passos (só com OK do Wagner).** Push e PR de Mateus; depois Marcos e Lucas, cada um com `extrair_grego_door43.py --livro <livro>` e o mesmo ritual. As páginas de modelo dos três Evangelhos são assunto editorial (ver "frente 0" do plano das Perguntas).

**No ar.** PR #15 mesclado pelo Wagner, merge `418dea75` (14/10 16:12 UTC), deploy run `38596061047` (success, 16:14 UTC). Conferido com curl: Mateus 1, 5 e 26 em PT, EN e ES no ar = `main` byte a byte (200); 6/5/1 blocos `grego-tr` com crédito em cada um e `lang="grc"`; 1 link de `grego.css` e 1 da Gentium Plus no `<head>`; versículos = JSON (10/13/3); `grego.css` no ar = `main`; Gentium Plus respondendo 200 com os subconjuntos greek e greek-ext. Rollback: `git revert -m 1 418dea75`.

## Grego koiné em Marcos (14/10/2026, branch `feat/grego-marcos`)

**Decisões.** As mesmas de Mateus (14/10): páginas de modelo fora, grego da faixa inteira do rótulo, um PR por Evangelho. Scripts sem mudança (`extrair_grego_door43.py` e `aplicar_grego_evangelhos.py --livro marcos`).

**O que mudou.** Commit `3aefc599`: `scripts/dados/grego-tr-marcos.json` (38 versículos de 8 capítulos; contra o byztxt, 23 iguais, 15 só de grafia, 0 de leitura; nenhum normalizado em NFC; o token vazio do USFM em Mc 13:9 fica fora das citações). Commit `5d090daf`: 24 páginas (caps. 1, 2, 4, 8, 10, 14, 15, 16 × PT/EN/ES), 54 blocos, +642 linhas, 0 removidas (+68.058 B em LF, igual ao previsto no diagnóstico). Backup `_backups/grego-marcos-20261014-135407.zip`. As 24 páginas de modelo (caps. 3, 5, 6, 7, 9, 11, 12, 13: "N:1 — Contexto e introdução" + "O Servo Sofredor") ficaram de fora; rótulos fora dos formatos: 0.

**Prova.** Por página: novo menos os trechos inseridos = original, byte a byte; citações e `<img>` idênticas; quebra de linha preservada; grego lido da página = JSON. Gravado = simulação aprovada (24/24); backup = HEAD (24/24); nova simulação = 0 mudanças. Chrome: prints de Marcos 8 (bloco 8:29-33; PT/EN/ES, 1280 e 390 px, aberto e fechado) aprovados; 24 páginas a 390 e 360 px com todos os blocos abertos, sem rolagem horizontal, Gentium Plus carregada. Observação: em EN/ES a 390 px o seletor de idioma flutuante cobre o fim de alguns títulos; já era assim antes do grego.

**Próximos passos (só com OK do Wagner).** Push e PR de Marcos; depois Lucas, com o mesmo ritual.

**No ar.** PR #16 mesclado pelo Wagner, merge `364f54a9` (14/10 17:00 UTC). A 1ª tentativa do deploy (run `38602880121`) falhou no passo "Upload do artefato do Pages" por timeout do serviço de artefatos do GitHub (não do conteúdo); relançada com `gh run rerun 38602880121 --failed` (OK do Wagner), a 2ª tentativa deu success (17:21 UTC). Conferido com curl: Marcos 1, 8 e 16 em PT, EN e ES no ar = `main` byte a byte (200); 3/2/1 blocos `grego-tr` com crédito e `lang="grc"`; 1 link de `grego.css` e 1 da Gentium Plus no `<head>`; versículos = JSON (3/7/3); `grego.css` no ar = `main`; Gentium Plus (greek e greek-ext) 200. Rollback: `git revert -m 1 364f54a9`.

## Grego koiné em Lucas (14/10/2026, branch `feat/grego-lucas`)

**Decisões.** As mesmas de Mateus e Marcos (14/10): páginas de modelo fora, grego da faixa inteira do rótulo, um PR por Evangelho. Scripts sem mudança (`--livro lucas`).

**O que mudou.** Commit `d0edaaad`: `scripts/dados/grego-tr-lucas.json` (121 versículos de 8 capítulos; contra o byztxt, 75 iguais, 46 só de grafia, 0 de leitura; Lc 10:32 normalizado em NFC, U+1FD3 → U+0390; o token vazio do USFM em Lc 2:37 fica fora das citações). Commit `321c4385`: 24 páginas (caps. 1, 2, 4, 10, 15, 19, 22, 24 × PT/EN/ES), 63 blocos, +963 linhas, 0 removidas (+124.995 B em LF; o diagnóstico previa 124.998, a diferença de 3 B é a normalização de Lc 10:32 nos 3 idiomas). Maiores blocos: Lc 24:13-27 (15 versículos) e Lc 15:11-24 (14). Backup `_backups/grego-lucas-20261014-142602.zip`. As 48 páginas de modelo (caps. 3, 5–9, 11–14, 16–18, 20, 21, 23: "N:1 — Contexto e introdução" + "O Salvador Universal") ficaram de fora; rótulos fora dos formatos: 0.

**Prova.** Por página: novo menos os trechos inseridos = original, byte a byte; citações e `<img>` idênticas; quebra de linha preservada; grego lido da página = JSON. Gravado = simulação aprovada (24/24); backup = HEAD (24/24); nova simulação = 0 mudanças. Chrome: prints de Lc 15 e Lc 24 (PT/EN/ES, 1280 e 390 px, aberto e fechado; aberto em tela alta); a 390 px o bloco de Lc 24:13-27 aberto tem ~2.700 px de altura, sem cortes. 24 páginas a 390 e 360 px com todos os blocos abertos, sem rolagem horizontal, Gentium Plus carregada.

**Próximos passos (só com OK do Wagner).** Push e PR de Lucas; depois do merge, conferir no ar (Lucas 1, 15 e 24). Com Lucas, os três sinóticos ficam completos nas páginas com citação real (84 páginas, 234 blocos). Em aberto: as 120 páginas de modelo dos três Evangelhos (40 por idioma) (editorial, "frente 0") e, se desejado, um "ver mais" para blocos longos (CSS novo).

**No ar.** PR #17 mesclado pelo Wagner, merge `21af4857` (14/10 17:33 UTC), deploy run `38607723760` (success na 1ª tentativa, 17:35 UTC). Conferido com curl: Lucas 1, 15 e 24 em PT, EN e ES no ar = `main` byte a byte (200); 4/3/3 blocos `grego-tr` com crédito e `lang="grc"`; 1 link de `grego.css` e 1 da Gentium Plus no `<head>`; versículos = JSON (21/29/23); `grego.css` no ar = `main`; Gentium Plus (greek e greek-ext) 200. Rollback: `git revert -m 1 21af4857`.

## Grego koiné em João (14/10/2026, branch `feat/grego-joao`)

**Decisões do Wagner (14/10).** Estender a camada a João com o mesmo ritual; João 3 (piloto, PR #11) não é tocado. Aprovada a regra do "item vazio" de número composto (Jo 6:19, "εἰκοσιπέντε": o Door43 escreve o número inteiro numa palavra e acrescenta uma linha sem texto só com o lema πέντε). As junções οὐκέτι/μήτις na regra de grafia do extrator ficaram de fora por ora.

**O que mudou.** Commit `5cb7c320`: scripts aceitam `--livro joao` (entrada `joao` em `aplicar_grego_evangelhos.py`; no extrator, SHA-256 do `JOH.SCV`, regra do item vazio — só quando as duas linhas são numerais e a anterior tem a forma escrita; os casos citados vão para `"itens_vazios_aceitos"` — e comparação do JSON sem o CR da cópia local). Regressão: os JSON de Mateus, Marcos e Lucas saem idênticos byte a byte. Commit `03a1e0fd`: `scripts/dados/grego-tr-joao.json` (103 versículos: 93 novos e os 10 de João 3, idênticos aos do piloto e não reaplicados; contra o byztxt, 76 iguais, 27 só de grafia, 0 de leitura; `"itens_vazios_aceitos": ["6:19"]`). Commit `873ca0bb`: 36 páginas (caps. 1, 4, 6, 10, 11, 13, 14, 15, 17, 19, 20, 21 × PT/EN/ES), 108 blocos, +1.287 linhas, 0 removidas (+144.159 B em LF, igual ao previsto). Backup `_backups/grego-joao-20261014-152259.zip`. As 24 páginas de modelo (caps. 2, 5, 7, 8, 9, 12, 16, 18: "N:1 — Contexto e introdução" + "A Teologia Joanina") ficaram de fora; João 3 aparece como "já tem" e segue idêntico; rótulos fora dos formatos: 0. Em João 6 os blocos estão na ordem 35 · 51-56 · 19-20 (fora da ordem dos versículos; o script lida com isso).

**Prova.** Por página: novo menos os trechos inseridos = original, byte a byte; citações e `<img>` idênticas; quebra de linha preservada; grego lido da página = JSON. Gravado = simulação aprovada (36/36); backup = HEAD (36/36); nova simulação = 0 mudanças; João 3 sem nenhum diff. Chrome: prints de Jo 6:19-20 (simulado) e Jo 3:16 (controle, piloto) em PT/EN/ES, 1280 e 390 px, aberto e fechado; 36 páginas a 390 e 360 px com todos os blocos abertos, sem rolagem horizontal, Gentium Plus carregada.

**Próximos passos (só com OK do Wagner).** Push e PR de João; depois do merge, conferir no ar (João 1, 6 e 21, e João 3 inalterado). Com João, os quatro Evangelhos ficam completos nas páginas com citação real (120 páginas novas + 3 do piloto). Em aberto: as 144 páginas de modelo dos Evangelhos (48 por idioma; editorial, "frente 0"), um "ver mais" para blocos longos (CSS novo) e, se desejado, as junções οὐκέτι/μήτις na regra de grafia do extrator.

**No ar.** PR #18 mesclado pelo Wagner, merge `476eede0` (14/10 18:31 UTC), deploy run `38615945866` (success na 1ª tentativa, 18:33 UTC). Conferido com curl: João 1, 6 e 21 em PT, EN e ES no ar = `main` byte a byte (200); 4/3/2 blocos `grego-tr` com crédito e `lang="grc"`; 1 link de `grego.css` e 1 da Gentium Plus no `<head>`; versículos = JSON (6/9/5, inclusive Jo 6:19); João 3 inalterado: nos 3 idiomas, 4 blocos e 10 versículos, no ar = `main`, e as 3 páginas no git idênticas à versão do piloto (`c48d4204`); `grego.css` no ar = `main`; Gentium Plus (greek e greek-ext) 200. Com isso, os quatro Evangelhos estão no ar nas páginas com citação real (120 páginas novas + 3 do piloto). Rollback: `git revert -m 1 476eede0`.

## Grego em todos os versículos do NT (decisões de 14/10/2026; nada aplicado)

**Objetivo (Wagner, 14/10, por sugestão dos professores).** Levar o grego koiné (Textus Receptus 1894 Scrivener, Door43, mesma versão fixada `4107626c`, conferida contra o byztxt `6049a43b`) a todos os versículos do Novo Testamento, e não só aos citados nos estudos, livro por livro, em PT, EN e ES.

**Diagnóstico (somente leitura, 14/10).** 260 páginas da Bíblia ACF em `biblia/<sigla>/<sigla>-NN.html`, estrutura uniforme nas 260 (`<div class="verse">` com `verse-number` e `verse-text`, versículos em sequência); CSS próprio embutido, sem hreflang, fora do sitemap, sem links com os estudos. EN e ES não têm Bíblia completa, só os estudos. Numeração: ACF = Door43 em 7.958 versículos; única diferença Ap 12:18 (o Door43 tem 12:18; a ACF e o byztxt põem o texto no início de 13:1); o byztxt não tem 3 Jo 1:15 (junto com o 14). As 92 diferenças contra o byztxt não são variantes de texto: 18 pares de fronteira de versículo, junções (μή πως, οὐκ ἔτι, ἐκ περισσοῦ…), numerais com keraia no Apocalipse e as subscrições paulinas, que o Door43 põe dentro do último versículo (15 livros, de Romanos a Hebreus). Linhas sem texto ainda sem regra: Mc 13:9, Hb 3:6, 3:14, 6:3 e Ap 7:4. Peso nas 260 páginas: +2,25 MB sem compressão, gzip de 1,19 para 1,89 MB (+59%); de 4 a 13 KB por capítulo (maior: Mt 26, +19,8 KB); Gentium greek + greek-ext 26 KB, uma vez.

**Decisões do Wagner (14/10).**
1. Subscrições paulinas: nota discreta fora da numeração dos versículos.
2. Ap 12:18 segue a ACF (o grego entra no versículo em que a ACF põe o texto), com nota sobre a numeração do Scrivener.
3. Layout: uma linha de grego abaixo de cada versículo, visível por padrão, com um botão por capítulo para ocultar/mostrar; crédito da licença uma vez por capítulo, no fim dos versículos (mesmo texto do piloto).
4. EN e ES: KJV e Reina-Valera 1909 (domínio público) aprovadas em princípio para a segunda frente, com conferência de numeração por livro. As citações atuais dos estudos (EN aparentemente ESV, ES RVR1960) têm copyright e não servem para capítulos inteiros.
5. As páginas `biblia/` ficam fora do sitemap até o piloto de João 3 ser avaliado.

**Plano em fases (cada fase e cada livro só com OK do Wagner, no ritual dos Evangelhos: simulação, prints, `--apply` com backup, um PR por livro).**
- **Fase 1 — piloto em PT: `biblia/jo/jo-03.html`** (36 versículos). Prova: os 10 versículos do piloto saem idênticos ao JSON publicado; regras novas no `grego.css` (linha do versículo, botão, nota); avaliação no ar antes de seguir.
- **Fase 2 — Proposta B em PT, livro por livro, do menor risco ao maior:** 2 Jo, Jd, Tg, 1 Pe, 2 Pe, 1 Jo; 3 Jo; cartas paulinas com a nota de subscrição (Fp, Cl, 2 Ts, Tt, Fm, 1 Ts, 1 Tm, 2 Tm, Gl, Ef, 1 Co, 2 Co, Rm); Hebreus (resolver as linhas sem texto); Jo, Mt, Lc, At, Mc (13:9); Apocalipse por último (12:18, numerais, 7:4). Dados num JSON por livro com todos os versículos (`scripts/dados/grego-nt/<livro>.json`); os JSON dos estudos não mudam.
- **Fase 3 — segunda frente, EN e ES (só depois da Fase 2 avaliada):** 260 páginas novas em cada idioma com KJV e RV1909 de fonte fixada e o grego embaixo; links "Estudo deste capítulo" / "Ler o capítulo inteiro" (só marcação), hreflang entre as três versões, canonical próprio; sitemap decidido depois do piloto.

## Grego em todos os versículos do NT — Fase 1: piloto em `biblia/jo/jo-03.html` (15/10/2026, branch `feat/grego-biblia-jo3`)

**Decisões do Wagner (15/10).** Rótulos do botão aprovados: "Ocultar o grego" / "Mostrar o grego". O botão não lembra a escolha entre capítulos (pode entrar depois, se desejado).

**O que mudou.** Commit `89cc1ae6`: `scripts/aplicar_grego_biblia.py` (simulação por padrão; `--apply` com backup; por ora só autoriza João 3). Commit `419ee8b7`: `scripts/dados/grego-nt/joao.json`, João inteiro (879 versículos; contra o byztxt 633 iguais, 237 só grafia, 9 de fronteira/variante, nenhum em João 3; itens vazios de número composto aceitos: 6:19 e 21:11); `grego-tr-joao.json` dos estudos não muda. Commit `b0c000dc`: `biblia/jo/jo-03.html` (bloco `grego-biblia:v1` no `<head>` com Gentium Plus, `grego.css` e `grego-biblia.js`; botão antes dos versículos; uma linha `<span class="verso-grego" lang="grc">` em cada um dos 36 versículos; crédito CC BY-SA 4.0 uma vez no fim, texto do piloto), `assets/css/grego.css` (+9 linhas no fim, classes que nenhuma das 123 páginas de estudo usa) e `assets/js/grego-biblia.js` (novo; sem JS o botão fica escondido e o grego visível). A classe da nota (subscrições, Ap 12:18) fica para a Fase 2, quando houver caso real. Backup `_backups/grego-biblia-joao-20261015-141909.zip`.

**Prova.** SHA-256 das fontes = fixados; numeração ACF = Door43 = byztxt (36 versículos); 0 diferenças de leitura no capítulo; os 103 versículos publicados nos estudos (inclusive os 10 do piloto de João 3) saem idênticos no JSON novo; novo menos os trechos inseridos = original, byte a byte (texto ACF intacto); grego lido da página = JSON, 36/36 na ordem; gravado = simulação aprovada; nova simulação = 0 mudanças. Chrome: 1280, 390 e 360 px, escuro e claro, sem rolagem horizontal, Gentium Plus carregada, botão alterna e `aria-pressed` acompanha.

**Achado antigo (não alterado).** A barra "← Capítulo Anterior / Índice da Bíblia / Próximo Capítulo →" (`.chapter-nav`, `.nav-button`) não tem CSS nas 1.189 páginas de `biblia/` e aparece como links azuis crus. Já era assim antes do piloto; tratar à parte, só com ordem do Wagner.

**Próximos passos (só com OK do Wagner).** Push e PR; depois do merge, conferir no ar (João 3 com 36 linhas de grego, `grego.css` e `grego-biblia.js` = `main`, Gentium 200) e avaliar o piloto antes da Fase 2.

## Grego em todos os versículos do NT: andamento (registrado em 15/10/2026)

Script único `scripts/aplicar_grego_biblia.py` (simulação por padrão, `--apply` com backup zip em `_backups/`), dados em `scripts/dados/grego-nt/<livro>.json`. Fonte fixada: Door43 `4107626c` (SHA-256 de cada arquivo no script, hash git conferido no Door43 e no GitHub), conferência no byztxt `6049a43b`. Em cada livro: diagnóstico, lista de correções aprovada pelo Wagner, dry-run com prova byte a byte, regressão dos livros já no ar (0 mudanças), prints a 1280/390/360 px no escuro e no claro, `--apply`, nova simulação com 0 mudanças, PR e conferência no ar com curl.

| Etapa | Livros (PT) | PR | Merge | Deploy | Reversão |
|---|---|---|---|---|---|
| Fase 1 (piloto) | João 3 | #20 | `f00e0f3c` (15/10 17:40 UTC) | run `38779262665` ok | `git revert -m 1 f00e0f3c` |
| Fase 2, lote 1 | 2 João, 3 João, Judas | #21 | `6847fa81` (15/10 18:41 UTC) | run `38787656179` ok | `git revert -m 1 6847fa81` |
| Fase 2, lote 2 | Tiago (5 caps., 108 vers.) | #22 | `0598dd64` (15/10 19:33 UTC) | run `38794863761` ok | `git revert -m 1 0598dd64` |
| Fase 2, lote 3 | 1 Pedro (5 caps., 105 vers.) | #23 | `a2395647` (15/10 20:49 UTC) | run `38805014793` ok | `git revert -m 1 a2395647` |
| Fase 2, lote 4 | 2 Pedro (3 caps., 61 vers.) | #25 | `ecb64b70` (16/10 13:35 UTC) | run `38908996391` ok | `git revert -m 1 ecb64b70` |
| Fase 2, lote 5 | 1 João (5 caps., 105 vers.) | #26 | `2596d9e9` (16/10 14:38 UTC) | run `38917342360` ok | `git revert -m 1 2596d9e9` |
| Fase 3, Apocalipse lote 1 | Apocalipse 1 a 7 (130 vers.) | #28 | `5f43bbf5` (16/10 20:07 UTC) | run `38959961702` ok | `git revert -m 1 5f43bbf5` |
| Fase 3, Apocalipse lote 2 | Apocalipse 8 a 14 (119 vers.) | #29 | `983dc74f` (19/10 17:58 UTC) | run `39298667028` ok | `git revert -m 1 983dc74f` |
| Fase 3, Apocalipse lote 3 | Apocalipse 15 a 22 (155 vers.) | #31 | `5986d29b` (19/10 19:24 UTC) | run `39310762661` ok | `git revert -m 1 5986d29b` |

**Marco (16/10/2026): cartas gerais completas em PT.** Grego em todos os versículos de `biblia/` em Tiago, 1 e 2 Pedro, 1, 2 e 3 João e Judas, mais o piloto de João 3. Ainda **sem** grego em todos os versículos: Evangelhos (Mateus, Marcos, Lucas e João, exceto João 3), Atos, cartas paulinas, Hebreus e Apocalipse. Nos Evangelhos existe só o grego dos versículos citados nos estudos (`scripts/dados/grego-tr-*.json`, 14/10), que é outra coisa.

Conferido no ar (curl, página no ar = `main` byte a byte): jo-03; 2jo, 3jo e jd; Tiago 1, 3 e 4; 1 Pedro 1, 3 e 4; 2 Pedro 1, 2 e 3; 1 João 1 a 5. Correções de acentuação no ar: 2 Jo 7; 3 Jo 9 e 15; Jd 20 e 22; Tg 1:12, 1:26, 2:2, 2:18, 3:5, 3:12 e 4:13; 1 Pe 1:4, 1:7, 1:16, 2:6, 3:1, 3:12, 3:13, 3:15, 3:16, 4:1 e 4:8; 2 Pe 1:12, 1:17, 1:21, 2:2, 2:7, 2:22, 3:3, 3:7, 3:10, 3:11 e 3:16 (13 trocas); 1 Jo 1:5, 1:10, 2:7, 2:11, 2:14, 2:16, 2:24, 2:28, 3:3, 3:6, 3:14, 3:16, 3:17, 4:6, 4:12, 4:19, 4:21, 5:7, 5:9, 5:12, 5:13, 5:18 e 5:20 (24 trocas).

Apocalipse (frente nº 2 da FILA, 3 lotes, 22 capítulos): lote 1 (1 a 7) e lote 2 (8 a 14) no ar. Conferido no ar: ap-01 a ap-07 = `main` (20/29/22/11/14/17/17 linhas de grego); ap-08 a ap-14 = `main` (13/21/11/19/17/18/20 linhas; nota só no 13:1), com 1 botão e 1 crédito por página; controles 1jo-01, 2 Pedro e Tiago inalterados. Correções no Apocalipse: lote 1, 67 trocas registradas (68 palavras) em 49 versículos, mais a troca de letra de 5:8 (D3); lote 2, 41 trocas em 31 versículos (lista A 37, lista B 4). O `ap.json` cresce lote a lote (só os capítulos autorizados): 130 versículos e 75.577 B no lote 1, 249 versículos e 135.818 B no lote 2; o script prova que os versículos e as correções já publicados ficam idênticos. Backups: `_backups/grego-biblia-ap-20261016-162754.zip` e `_backups/grego-biblia-ap-20261019-142001.zip`.

Apocalipse, lote 3 (15 a 22) no ar em 19/10 (#31): com ele, os 22 capítulos do Apocalipse têm grego em todos os versículos. Conferido no ar (Python, urllib com anti-cache): ap-15 a ap-22 = `main` (8/21/18/24/21/15/27/21 linhas de grego; sem notas), com 1 botão e 1 crédito por página; 22:18 com `ταῦτα` e nenhum `ταὐτά` nas páginas ap-01 a ap-22; controles ap-01, ap-08, ap-14, 1jo-01, 2 Pedro e Tiago inalterados. Correções no lote 3: 63 trocas em 45 versículos (67 palavras; lista A 61, lista B 2). O `ap.json` passa de 249 para 404 versículos (135.818 → 212.924 B), com os 249 já publicados idênticos. Backups: `_backups/grego-biblia-ap-20261019-152814.zip` (8 páginas e JSON) e `_backups/grego-biblia-ap-20261019-160748.zip` (ap-22 e JSON, reaplicação com o 22:18).

**Decisões do Wagner (15/10).**
1. Correções de acentuação, opção B: só acentos e pontuação, com as letras iguais às do byztxt (prova no script); cada correção fica registrada no JSON do livro (`correcoes_de_acentuacao`: forma do Door43, forma publicada e motivo); a lista de cada livro passa pelo Wagner antes do `--apply`. O grave antes de vírgula é convenção da fonte e fica como está.
2. A ACF manda na numeração; quando a fonte numera diferente, o grego segue a ACF, com nota discreta abaixo do grego (caso real: 3 Jo 15, texto aprovado; classe `.verso-nota`, bloco `grego-biblia-nota:v1` no `grego.css`).
3. Rótulos do botão: "Ocultar o grego" / "Mostrar o grego".
4. Um livro por PR, ou livros curtos juntos (como 2 Jo, 3 Jo e Jd).

**Decisões do Wagner (16/10).**
5. 2 Pe 1:17: só o grave (`ἀγαπητὸς εἰς`), sem acrescentar vírgula. 2 Pe 2:7: sem pontuação no fim, como na fonte.
6. 1 Jo 1:1 (sem pontuação no fim) e 1 Jo 3:13 (sem vírgula antes do vocativo) ficam como na fonte.
7. Propostas de pontuação, maiúscula ou grafia só entram se o byztxt confirmar a forma exata; o byztxt fixado (`textonly`) é transliterado, sem acentos, pontuação nem maiúsculas, então nesses casos fica a forma da fonte.
8. 1 Jo 5:7 (Comma Johanneum): está no Door43, no byztxt (`greektext-scrivener`, o próprio Scrivener 1894) e na ACF; numeração igual nas três fontes, sem nota. Única correção no trecho: `εν` → `ἐν`.

**Decisões do Wagner (16/10, Apocalipse, lote 1).**
9. D1: a keraia dos números (`ιβʹ`) sai só da comparação com o byztxt; o texto publicado fica como na fonte.
10. D2: Ap 7:4, as duas linhas vazias do numeral `ρμδʹ` (144) no USFM são aceitas; o texto não muda (`vazios_aceitos_por_decisao` no JSON).
11. D3: Ap 5:8, troca de letra `εἴκοσιιτέσσαρες` → `εἴκοσιτέσσαρες` (ι a mais; forma de 5:14; letras = byztxt), em seção própria (`correcoes_de_letra`), separada das de acento.
12. O `ap.json` cresce lote a lote (só os capítulos autorizados); o script prova que o que já está publicado fica idêntico.

**Decisões do Wagner (19/10, Apocalipse, lote 2).**
13. D4: Ap 13:18, o Door43 escreve 666 com estigma (`χξϛʹ`) e o byztxt `cxv`; o estigma vira sigma final só na comparação. O texto publicado mantém `χξϛʹ`.
14. D5: Ap 14:1 e 14:3, `τεσσαράκοντατέσσαρες` fica junto, como no Door43 (o byztxt separa); o par é juntado só na comparação.
15. D6: Ap 14:13, `ἀπ’ ἄρτι` fica separado, como no Door43 (o byztxt junta); o par é juntado só na comparação.
16. Ap 12:18 → 13:1 (decidido em 14/10, nota aprovada em 19/10): o grego segue a numeração da ACF. As palavras que o Door43 numera como 12:18 (`καὶ ἐστάθην ἐπὶ τὴν ἄμμον τῆς θαλάσσης.`) abrem o 13:1; o byztxt também não tem 12:18, e o 13:1 juntado = byztxt 13:1. Nota no 13:1: "Nota: no Textus Receptus de Scrivener (1894), as primeiras palavras deste versículo formam o v. 18 do capítulo 12; aqui o grego segue a numeração da ACF."
17. Ap 12:15: `εκ’` → `ἐκ` (sem apóstrofo), mesmo precedente de 2:21. Lista B (acento que muda a palavra): 10:4 `ταῦτα`, 12:15 `ταύτην`, 14:4 `οὗτοί εἰσιν`, 14:15 `ἦλθέ σοι`.
18. O que fica "para revisão futura" é registrado no script e no PLANO (pendência i), não no JSON.

**Decisões do Wagner (19/10, Apocalipse, lote 3).**
19. Numeração ACF = Door43 = byztxt nos capítulos 15 a 22 (8, 21, 18, 24, 21, 15, 27 e 21 versículos): sem movimento e sem nota.
20. D7: Ap 21:17, `τεσσαράκοντατεσσάρων` fica junto, como no Door43 (o byztxt separa); o par é juntado só na comparação, como na D5. A linha vazia do numeral composto já era aceita pela regra de Jo 6:19.
21. Lista B: 20:14 `οὗτος ἐστιν` → `οὗτός ἐστιν` (como 14:4) e 22:18 `ταὐτά,` → `ταῦτα,` ("estas coisas", não "as mesmas coisas"; como 10:4). O 22:18 foi achado na conferência dos prints, depois do primeiro `--apply`: `ap-22.html` e `ap.json` foram restaurados do backup, a entrada foi acrescentada e o `--apply` refeito.
22. Ap 17:9 `εἰσίν ἑπτὰ` fica como na fonte (pendência i). Aprovados: 19:7 `ἀγαλλιώμεθα`, 19:20 `τούτου`, 17:7 `Διατί` (junto), 22:17 `Ἐλθέ` (oxítono) e as correções de acento junto de enclítica (17:7, 19:8, 19:9, 19:10, 21:5, 21:9, 21:12, 22:9, 22:13).

**Pendências.**
- (a) Lote de correção das páginas já publicadas, em PR separado: Jd 1 `ἠγίασμένοις` → `ἡγιασμένοις`; Jd 17 `δέ ἀγαπητοί` → `δὲ ἀγαπητοί`; 2 Jo 12 `ᾗ` → `ᾖ` (subjuntivo); Jo 3:13 `ὁ ὤν ἐν` → `ὁ ὢν ἐν` e pontuação final (afeta também o estudo de João 3, que publica o mesmo versículo); dúvida em Jd 14 (`Ἑνὼχ` no Door43, com espírito áspero; `Ἐνώχ` no Robinson-Pierpont).
- (b) Os botões flutuantes (modo claro e WhatsApp) cobrem parte do texto e do crédito no celular nas páginas de `biblia/`.
- (c) `.chapter-nav` sem estilo nas 1.189 páginas de `biblia/` (ver o achado da Fase 1).
- (d) Prévias do símbolo (`redesign/preview-simbolo-3d.html` e `redesign/simbolo-365-anel.webp`) fora do git, aguardando decisão.
- (e) 61 arquivos de `_backups/` ainda versionados no git (o `.gitignore` só cobre `*.zip`), a resolver por PR.
- (f) Cartas gerais concluídas (16/10). Apocalipse em PT é a frente nº 2 da FILA (aberta, 3 lotes, 22 capítulos): lote 1 (1 a 7) no ar em 16/10 (#28), lote 2 (8 a 14) no ar em 19/10 (#29), lote 3 (15 a 22) no ar em 19/10 (#31); os 3 lotes estão no ar e a frente aguarda a conferência e o "Pronto" do Wagner. Depois, a frente nº 3 (lote de correção, pendência a). Evangelhos, Atos, cartas paulinas e Hebreus ficam em "Frentes futuras", sem prioridade; depois EN/ES (KJV/RV1909), conferindo a numeração livro a livro.
- (g) A frente 0 das páginas de modelo EN/ES e o plano das Perguntas (`redesign/plano-perguntas-biblia.md`, na branch `docs/plano-perguntas`) seguem pendentes do export do Search Console.
- (h) Para revisão futura em 1 João, deixados como na fonte porque o byztxt não confirma a forma proposta (PR #26): **A** 2:13 sem vírgulas no vocativo nem pontuação no fim; **B** 2:14 sem pontuação interna nem final; **C** 2:14 `τοῦ θεοῦ` em minúscula (único caso no livro); **D** 2:15 vírgula solta em `τοῦ πατρὸς, ἐν αὐτῷ`; **E** 4:20 `ἀγαπᾷν` (grafia antiga), enquanto 4:11 tem `ἀγαπᾶν`.
- (i) Para revisão futura no Apocalipse, deixados como na fonte porque o byztxt fixado não tem acentos nem pontuação e não confirma a forma. Lote 1 (PR #28): 3:3 `ἐπὶ σε` (2 vezes); pontuação de 1:3 (ponto em `προφητείας. καὶ`), 1:20 (`ἑπτὰ· ἀστέρων`), 2:13 (`πίστιν, μου`), 2:27 e 2:28 (sem pontuação no fim), 3:12 (ponto antes de `τῆς καινῆς Ἰερουσαλήμ`) e 7:7 (vírgula a mais em `χιλιάδες, ἐσφραγισμένοι`). Lote 2 (PR #29): 9:4 `θεοῦ` minúsculo; 9:19 falta pontuação antes de `αἱ γὰρ`; 13:4 `τίς` minúsculo; 13:13 ponto em `γῆν. ἐνώπιον`; 14:8 pontuação; 14:13 pontuação entre `ἄρτι` e `ναί`; 14:3 `ζώων` sem iota subscrito. Lote 3 (PR #31): 15:3 `θεοῦ`, `κύριε`, `θεὸς` minúsculos e sem pontuação; 15:4 `τίς` minúsculo; 15:7 `ζώων` sem iota subscrito; 17:1 e 17:10 sem pontuação; 17:9 `εἰσίν ἑπτὰ`; 18:23 `φάνῃ` (o Robinson-Pierpont traz `φανῇ`); 19:4 `θεῷ` minúsculo e sem pontuação entre `Ἀμήν` e `Ἁλληλουϊά` e no fim; 19:5 falta vírgula depois de `αὐτόν`; 19:10 falta pontuação entre `Ἰησοῦ` e `τῷ Θεῷ`; 20:12 `θεοῦ` minúsculo e falta vírgula depois de `νεκρούς`; 21:6 `Ὦ` acentuado (1:8, 1:11 e 22:13 têm `Ω`); 21:25 falta pontuação entre `ἡμέρας` e `νὺξ`; 22:6 ponto alto em `προφητῶν·`; 22:20 falta vírgula em `Ναί ἔρχου`.

**Melhorias futuras do script.**
- Tornar `CORRECOES_CONFERIDAS` por livro (hoje é uma chave única, já `True`, em `scripts/aplicar_grego_biblia.py`; com uma chave por livro em `LIVROS`, a lista de correções de um livro novo não passa no `--apply` sem a conferência do Wagner).

A fila de frentes, com critério de pronto, está em `redesign/FILA.md`.

## Estado em 13/10 (fim do dia)

**No ar (merge commit e deploy "Deploy GitHub Pages" com sucesso, conferidos com curl)**
| PR | O quê | Merge | Rollback (só com ordem do Wagner) |
|---|---|---|---|
| #10 | Lote 1 EN/ES: coluna de leitura nas cartas e no Apocalipse (só `bloco.css`) | `a2c025b8` | `git revert -m 1 a2c025b8` |
| #11 | Piloto do grego koiné em João 3 (PT, EN e ES) | `c48d4204` | `git revert -m 1 c48d4204` |
| #12 | Docs: diagnóstico do lote 3.5 (WhatsApp) | `15175bf4` | `git revert -m 1 15175bf4` |
| #13 | Lote 3.5 parte A: WhatsApp e claro/escuro acima da barra inferior (só `bloco.css`) | `5bdf8d7b` | `git revert -m 1 5bdf8d7b` |

**Pendências abertas**
- *Lote 3.5 parte B* (botão "próximo" cortado no celular): simulada, aguardando aprovação do Wagner; se aprovada, vai em PR separado.
- *Próximo lote da ordem:* 2 — `site-nav.js` em três idiomas (rótulos do menu em EN/ES dependem de aprovação).
- *PRs de docs abertos:* #8 (hashes de rollback de 09/10) e #9 (ideias futuras: idioma original e versões HE/AR).
- *Fora do lote 1 (decisão do Wagner):* Atos 26 EN/ES; navegação e rodapé duplicados no fim das cartas EN/ES; Josué 16 e Juízes 9 com `lang` malformado.

## Estado em 09/10 (fim do dia)

**No ar (todos com merge commit e deploy "Deploy GitHub Pages" com sucesso, conferidos com curl)**
| PR | O quê | Merge | Rollback (só com ordem do Wagner) |
|---|---|---|---|
| #2 | SEO técnico: busca, og-cover/og-image/favicon, `/styles.css`, sitemap = canonical, canonical de Mateus, hreflang (item 4) | `7ce48cd2` (08/10) | `git revert -m 1 7ce48cd2` |
| #3 | Botões anterior/próximo EN/ES: 504 páginas, 918 botões | `71506aca` | `git revert -m 1 71506aca` |
| #4 | CSS de leitura nos capítulos EN/ES (só `bloco.css`) | `760336d2` | `git revert -m 1 760336d2` |
| #5 | Símbolo da Graça girando em 3D na home | `be928fb0` | `git revert -m 1 be928fb0` |

**Símbolo 3D na home (PR #5).** Commits `ca31ba29` (`scripts/aplicar_simbolo_home.py`), `6b9aa161` (`assets/img/simbolo-365-anel.webp`, anel "365" recortado de `logo-365-graca-adoracao.png`, 440×440, 29.780 bytes) e `09c2ab40` (`assets/css/simbolo-3d.css` + 17 linhas inseridas no `index.html`). CSS puro: `perspective` + `rotateY`, 12 s por volta; 220 px no desktop, acima do cartão "Continue de onde parou"; 112 px no celular (até 600 px), no topo do hero, acima do título (`display: contents` + `order: -1`, sem mexer no HTML). `prefers-reduced-motion`: `animation: none`, parado (a regra global do `site.css` só encurta a duração). Sem deslocamento de layout; decorativo (`aria-hidden`). Original `logo-365-graca-adoracao.png` intacto (2.388 KB, SHA-256 `e515ad3b…`, conferido no ar). Backup local `_backups/simbolo-home-20261009-155720.zip`. Deploy run `37980063522`, 19:25 UTC. Observação: o CSS embutido no script do commit 1 é a versão anterior ao ajuste do celular; vale o `assets/css/simbolo-3d.css`.

**Search Console.** Domínio verificado por TXT na Hostinger (manter os dois registros TXT) e sitemap `https://365gracaeadoracao.com/sitemap.xml` reenviado. Exportação de 404 de 09/10 analisada: 548 URLs eram os botões EN/ES (corrigidos no #3), 32 `/en|es/capitulo-NN.html` vêm da época do Vercel (mesma correção), 392 PT `/<bloco>/<livro>/capitulo-NN/` vêm do hreflang antigo (já corrigido no #2).

**Pendências abertas**
- *Search Console:* pedir "Validar correção" no relatório de 404; reenviar o sitemap depois de cada merge de SEO; remover a linha antiga `sitemap.xml.` (23/02/2026); ler Indexação > Páginas e classificar os demais motivos de não indexação.
- *Branch `docs/plano-09-10`* (estado de 08/10 + skills `seo-limpeza`, `lote-seguro`, `merge-deploy`): no GitHub, ainda fora da `main`. Teste de merge com a `main` em 09/10: sem conflito.
- *EN/ES:* botão central e de borda abrem o índice geral (`../index.html`), não o do livro (decisão do Wagner); trocar o cabeçalho `topbar` pelo menu central; modo claro (não existe); tamanho/contraste do texto de leitura nos três idiomas, se o Wagner quiser.
- *Textos:* acentos faltando nos títulos ES/EN (contar e simular, sem alterar); revisar a qualidade dos textos ES, começando pelas páginas mais clicadas.
- *SEO (decisões do Wagner):* 55 páginas sem canonical (27 EN `*-block-N`, 27 ES `*-bloque-N`, 1 Samuel 29); `/pasta/index` (299) × `/pasta/`; 88 URLs com `.html` no sitemap; Gênesis EN/ES sem pt-BR (100); hreflang de `estudos/` e home.
- *Editorial (decisões do Wagner):* duplicatas Tobias, Judite e 1–2 Macabeus (`03-historicos` × `06-apocrifos`); reconstrução da 1 Samuel 29.
- *Limpeza:* tirar os 61 arquivos de `_backups/` do git e pôr a pasta no `.gitignore` (via PR); branch antiga `(main)` (`501c8730`): renomear ou apagar.
- *Prévia do símbolo:* `redesign/preview-simbolo-3d.html` e `redesign/simbolo-365-anel.webp` estão só no disco (fora do git); decidir se entram no repositório.
- *Próxima frente sugerida:* busca com índice gerado (frente 2 do `INVENTARIO.md`).
- *CSS antigo:* o botão verde flutuante (WhatsApp) pode cobrir o "próximo capítulo" da barra fixa.

## Ponto de partida para terça (13/10/2026)

**Atualização 09/10, 20h38 UTC — PRs #7 e #6 mesclados (merge commit, com ordem do Wagner)**
| PR | O quê | Merge | Deploy | Rollback (só com ordem do Wagner) |
|---|---|---|---|---|
| #7 | Símbolo 3D nos 6 índices de testamento (PT, EN, ES) | `35e48613` (pais `be928fb0` + `b212e3fa`) | run `37988188742`, success 20:37 UTC | `git revert -m 1 35e48613` |
| #6 | Docs: `PLANO.md` (08/10, 09/10, terça) + skills | `a9d911b7` (pais `35e48613` + `a48a6be6`) | run `37988317423`, success 20:38 UTC | `git revert -m 1 a9d911b7` |
- Conferido no ar com `curl ?v=` depois do #7: as 6 páginas de índice respondem 200, têm o `<link>` do `simbolo-3d.css` e as 9 imagens, e são iguais à `main`; `simbolo-3d.css` 200 com o bloco AT/NT (5.004 bytes, igual à `main`); capítulos `lucas/capitulos/capitulo-14` e `en/luke-14/` iguais antes e depois do merge, sem o símbolo; home 200.
- O #6 não muda o site: `redesign/` e `.claude/` seguem fora do deploy (404 no ar).
- Com isso, os passos 1 e 2 abaixo estão feitos; terça começa pelo passo 3.

**Onde paramos (09/10, noite — antes dos merges acima)**
- `main` no GitHub = `be928fb0` (merge do PR #5, símbolo 3D na home). Site no ar = `main`.
- **PR #6 aberto, sem merge:** `docs/estado-09-10` → `main` (este `PLANO.md` com os estados de 08/10 e 09/10 + skills `seo-limpeza`, `lote-seguro`, `merge-deploy`). Só documentação; não muda o site.
- **`feat/simbolo-at-nt`, só local (sem push, sem PR):** símbolo 3D nos 6 índices de testamento (PT `antigo-testamento/` e `08-novo-testamento/`; EN `old-testament/` e `en/`; ES `antiguo-testamento/` e `es/`). Commits `0f6c4495` (script `scripts/aplicar_simbolo_at_nt.py`) e `b212e3fa` (+21 linhas no fim do `simbolo-3d.css` e +15 linhas em cada página, 0 alteradas). Backup `_backups/simbolo-at-nt-20261009-170509.zip`. Testes feitos a 1280/1024/390/360 px: giro, movimento reduzido, sem rolagem horizontal, sem sobreposição com o texto, título na mesma posição da `main`, home inalterada. Desktop: 220 px (PT) e 180 px (EN/ES) à direita do hero; até 1100 px: canto superior direito, 60 px (PT) e 48 px (EN/ES). Índices de livro (79) e capítulos ficaram de fora por decisão do Wagner.

**Primeiros passos de terça, nesta ordem (cada um só com OK do Wagner)**
1. ✅ (09/10) Revisar e mesclar o PR #6 (docs).
2. ✅ (09/10, PR #7) Push da `feat/simbolo-at-nt` e PR para a `main`; depois do merge: acompanhar o deploy e conferir no ar com `curl ?v=` (6 páginas com o `<link>` e as 9 imagens; `simbolo-3d.css` com o bloco novo; home sem mudança).
3. Search Console: pedir "Validar correção" no relatório de 404 (botões EN/ES); remover a linha `sitemap.xml.`; ler Indexação > Páginas e classificar os motivos restantes.
4. Escolher a próxima frente: busca com índice gerado; acentos nos títulos ES/EN (contar e simular); cabeçalho `topbar` → menu central nas páginas EN/ES; modo claro em EN/ES.

**Pendência registrada em 09/10 — deslocamento de 8 px no cabeçalho antigo EN/ES**
- Nas páginas EN/ES, no celular (390/360 px), o conteúdo desce 8 px quando o logo do cabeçalho ainda não carregou: `<img class="brand-logo-img" style="height:42px;width:auto">` não reserva a largura, e sem a imagem o cabeçalho muda de altura.
- **Já existe na `main`, sem o símbolo** (medido em `es/` e `en/old-testament/`: título em y 119 → 127 e 155 → 163, iguais na `main` e na `feat/simbolo-at-nt`). O símbolo não acrescenta deslocamento.
- Será tratado na troca do cabeçalho `topbar` pelo menu central nas páginas EN/ES; não corrigir à parte antes disso.

**Lembretes**
- `redesign/preview-simbolo-3d.html` e `redesign/simbolo-365-anel.webp` continuam só no disco (fora do git).
- O CSS embutido em `scripts/aplicar_simbolo_home.py` é a versão anterior ao ajuste do celular; vale o `assets/css/simbolo-3d.css`.
- Rollbacks no ar: #2 `7ce48cd2`, #3 `71506aca`, #4 `760336d2`, #5 `be928fb0`, #7 `35e48613`, #6 (docs) `a9d911b7` (`git revert -m 1 <hash>`, só com ordem do Wagner).

## Tarefa de amanhã (06/10/2026): capa 3D de livro

Criar uma **capa 3D de livro, só em CSS**, no topo das **páginas de abertura de cada livro** da Bíblia (não nos capítulos).

- **Antes de qualquer alteração**, fazer apenas o mapeamento somente leitura das páginas de abertura que o Wagner pedir, e parar no relatório.
- Mapeamento já feito em 05/10 (só leitura): o padrão recomendado é `<bloco>/<livro>/index.html` (`02-` a `06-` e `08-novo-testamento/`), que cobre os 66 livros canônicos uma vez cada. A confirmar com o Wagner:
  - Gênesis: `02-pentateuco/genesis/index.html` (o `genesis/index.html` da raiz é um estudo temático).
  - Deuterocanônicos: `06-apocrifos/` (as cópias em `03-historicos/` ficariam sem capa).
- Nome, testamento e número de capítulos da capa devem vir de uma tabela única de livros, não do texto de cada página (Deuteronômio cita "187" antes da contagem real; Gênesis e Salmos não mostram a contagem no formato padrão).
- Sem criar páginas novas. Mesmo procedimento das etapas anteriores: dry-run, confirmação, validação e commit separado.

## Lote 3.5 — corrigir sobreposição do WhatsApp antes do lote 4 (13/10/2026: parte A no ar; parte B simulada, aguardando aprovação)

**Problema.** Nas páginas PT de capítulo do NT, o botão flutuante do WhatsApp (`#whatsapp-cta`, estilo inline `bottom: 20px`, 50 px) fica sobre o botão "próximo" da barra inferior fixa (`.chapter-nav-fixed`, 59 px de altura): em Atos 8, "Atos 9 →" aparece só como "Atos".

**Onde acontece (medido no navegador, as 260 páginas, 1280/768/390/360 px).**
- A barra inferior só existe nos **260 capítulos PT do NT** (`08-novo-testamento/*/capitulos/`), todos com o mesmo código de botão, barra e claro/escuro. EN/ES não têm a barra: **0 páginas** afetadas.
- WhatsApp sobre o "próximo": **260 de 260** em todas as larguras.
- No celular, com nomes longos (1–2 Co, 1–2 Ts, 1 Tm, Fp, Cl, Ap), a barra quebra em várias linhas (até 104 px) e o botão claro/escuro (`#dark-toggle`, `bottom: 80px`) também encosta nela: 35 páginas a 390 px, 95 a 360 px.
- As outras 4.575 páginas com WhatsApp (PT 2.592, EN 991, ES 991) não têm barra inferior; varredura estática e amostra no navegador: nenhuma sobreposição.

**Correção proposta (só CSS, sem tocar em texto nem estrutura).** Em `assets/css/bloco.css` (as 260 páginas o carregam), restrita às páginas com a barra:
```css
body:has(.chapter-nav-fixed) #whatsapp-cta { bottom: 72px !important; }
body:has(.chapter-nav-fixed) #dark-toggle { bottom: 132px; }
@media (max-width: 600px) {
  body:has(.chapter-nav-fixed) #whatsapp-cta { bottom: 116px !important; }
  body:has(.chapter-nav-fixed) #dark-toggle { bottom: 176px; }
}
```
`!important` só no WhatsApp, porque a posição dele vem do atributo `style` do próprio botão.

**Simulação (CSS injetado só no navegador, 260 páginas × 4 larguras).** Depois: WhatsApp × "próximo" = 0; claro/escuro × barra/WhatsApp = 0, em 1280, 768, 390 e 360 px. Amostra sem barra (PT AT, estudos, EN, ES): sem mudança. Prints antes/depois de Atos 8 e 1 Tessalonicenses 4 (1280 e 390).

**Problema à parte, já existente (não incluído).** No celular, o próprio botão "próximo" com nome longo passa da borda direita da tela: 8 páginas a 390 px (1–2 Ts, Cl) e 13 a 360 px (+ 1 Tm, Ap). Corrigir junto só com decisão do Wagner.

**Parte A aplicada (13/10/2026, branch `fix/lote-3-5-whatsapp`, aprovada pelo Wagner).** As 4 regras acima foram acrescentadas no fim do `assets/css/bloco.css` (+11 linhas, 0 removidas), com `scripts/css_lote_3_5.py` (backup `_backups/lote-3-5a-20261013-175722.zip`). Gravado = simulação; nova simulação = 0 mudanças. Com o arquivo real: WhatsApp × "próximo" e claro/escuro × barra = 0 nas 260 páginas, em 1280, 768, 390 e 360 px. Verificação no Chrome das 4.153 páginas que carregam `bloco.css`: as regras novas casam com exatamente as 260 que têm a barra, nenhuma outra.

**Parte A no ar.** PR #13, merge `5bdf8d7b`, deploy run `38471609374` (success, 13/10 21:36 UTC). Conferido com curl: `bloco.css` no ar = `main` byte a byte (marca `lote-3-5a:v1`, sem a parte B); HTML de Atos 8 e 1 Tessalonicenses 4 no ar = `main`; print da página real de Atos 8 a 1280 px com "Atos 9 →" inteiro e os botões flutuantes acima da barra. O registro do diagnóstico entrou antes, no PR #12 (merge `15175bf4`). Rollback: `git revert -m 1 5bdf8d7b`.

**Parte B (botão "próximo" cortado no celular) — só simulada, aguardando aprovação do Wagner.** Até 600 px, a barra passa a ter duas linhas: "Capítulo X de 260 do NT" em cima; anterior/próximo embaixo, metade da largura cada, com quebra de linha; espaço reservado embaixo da página de 60 para 120 px. Simulação sobre a parte A real (260 páginas): botão fora da tela 8 → 0 a 390 px e 13 → 0 a 360 px; texto cortado 0; sobreposições 0; barra com 86 px (110 px quando o nome quebra em duas linhas); 1280/768 px sem mudança. Atenção para testes: os botões da barra têm `transition: all 0.15s`, então CSS injetado depois do carregamento precisa de espera antes de medir ou fotografar.

## Limpeza prioritária (registrada em 05/10/2026; nada alterado ainda)

Estas páginas **não devem ser alteradas** até decisão do Wagner. Todas ficaram fora do menu central.

| Página(s) | Problema |
|---|---|
| `genesis/genesis-12.html` a `genesis/genesis-50.html` (39) | Conteúdo mínimo (~700 bytes: título + "Conteúdo completo do capítulo N…") com `canonical` e anúncio do AdSense. Conteúdo raso indexado: risco de SEO e de política do AdSense. |
| `busca/index_backup.html` | Cópia de backup da busca, **publicada no site** (o deploy não exclui `*_backup.html`). |
| `02-pentateuco/genesis/estudos/pasted_content.html` | Nome de arquivo colado por engano; dois `<title>` ("pasted_content" e "Projeto 365"). |
| `02-pentateuco/genesis/estudos/pasted_file_FffSUA_image.html`, `pasted_file_V6Gujv_image.html`, `pasted_file_aNGcVD_image.html`, `pasted_file_llU4dO_image.html`, `pasted_file_roMaD4_image.html` (5) | Arquivos de imagem colados por engano e embrulhados no modelo de página: cabeçalho HTML normal (com `canonical` e AdSense) seguido de dados binários com 1.054 a 1.185 bytes nulos cada. Título = nome do arquivo (o de `roMaD4` saiu ilegível). O git as trata como binárias (diff não aparece). Publicadas no site, fora do `sitemap.xml`. Receberam o menu central e a troca do link do AT com prova byte a byte (registrado em 07/10/2026). |
| ~~`08-novo-testamento/index.html` (canonical)~~ | ✅ **Resolvido em 08/10/2026** (commit `07cee8bc`): o sitemap agora usa o canonical. Registro original: o canonical é `https://365gracaeadoracao.com/08-novo-testamento/index` (sem `.html`), mas o `sitemap.xml` lista `/08-novo-testamento/index.html`. Alinhar os dois na etapa de SEO (registrado em 07/10/2026). |
| `sitemap.xml` (`lastmod` e cabeçalho) | Os `lastmod` das páginas alteradas no redesign continuam em 2026-05-26, e o comentário do topo diz "Gerado em 2026-05-26 · Total de páginas: 4151" (são 4.152 desde 07/10). Atualizar na etapa de SEO (registrado em 07/10/2026). |
| `06-apocrifos/index.html`, `busca/index.html` | Rolagem horizontal a 390px: Apócrifos passa 6px; Busca passa 31px (grade `.indice-item` com 2 colunas de 180px). Iguais na `main` (não causadas pelo redesign). Corrigir por CSS depois (registrado em 07/10/2026). |
| `estudos/` e subpáginas | Sem o botão de modo claro (`#dark-toggle`): o modo claro escolhido no resto do site não se aplica nessas páginas (registrado em 07/10/2026). |
| Textos para decisão do Wagner (**não alterar**) | `busca/index.html` mostra "1.627+ Páginas no projeto", enquanto a home diz "+2.900 Páginas em português". O rodapé dos estudos diz "compatíveis com Vercel" (o site está no GitHub Pages). Registrado em 07/10/2026. |
| ~~`assets/img/favicon.png`~~ | ✅ **Resolvido em 08/10/2026** (commit `5716d119`). Criado como cópia do `apple-touch-icon.png`; as 5 páginas que o citam (inclui `en/estudos` e `es/estudios`) não foram editadas. |
| `timeline-component.html`, `timeline-genesis-1.html` (raiz) | Fragmentos sem `<html>`/`<body>`, publicados como páginas. |
| ~~`og:image`/`twitter:image` em 2.825 páginas~~ | ✅ **Resolvido em 08/10/2026** (commit `5716d119`). `assets/img/og-cover.jpg` (e `og-image.jpg`, citado pela home e `blocos/`) criados como JPEG do `og-image.png`, mesma arte; nenhuma página editada. Só vale no ar depois do próximo merge na `main`. |
| `03-historicos/juizes/index.html` (e provavelmente os outros 9 livros com `main.wrap`: 1–2 Samuel, 1–2 Reis, 1–2 Crônicas, Esdras, Neemias, Ester) | Faixa de números ("21 Capítulos · 618 Versículos · ~1380–1050 a.C. · 12 Juízes Principais") sem estilo, um item por linha; selo, título e subtítulo deslocados para a esquerda no cartão de abertura. Já existia antes da capa 3D (registrado em 06/10/2026). Tratar numa etapa própria, depois do lote da capa. |
| `03-historicos/rute/index.html`, `03-historicos/josue/index.html` | No modo claro, o cartão de introdução de Rute fica escuro e as faixas coloridas de Josué (e de Rute) mudam de tom, por causa da inversão global do site (`filter: invert` no `<html>`) sobre cores fixas da página. Não afeta a capa 3D (registrado em 06/10/2026). |
| ~~`02-pentateuco/deuteronomio/index.html`~~ | ✅ **Resolvido em 06/10/2026** (commit `23969271`). Rolagem horizontal a 390px: o título da página ("📜 DEUTERONÔMIO", 3em) não cabia na coluna. Corrigido no `assets/css/capa-livro.css`, preso à capa: `clamp(1.4rem, 6.5vw, 3em)` — só reduz no celular; no desktop continua 3em. |
| ~~`02-pentateuco/exodo/index.html`~~ | ✅ **Resolvido em 06/10/2026** (commit `83713f7d`). Rolagem horizontal no celular: as grades da página (`.study-options` 400px, `.blocks-grid` 350px) não cabiam na tela. Corrigido no `assets/css/capa-livro.css`, preso à capa: mínimo da grade limitado à largura da coluna. |

## Pendências para a Fase 2 (anotadas a pedido do Wagner)

- ~~**Bug no índice de busca** (`assets/js/nav.js`)~~: ✅ **Resolvido em 08/10/2026** (commit `bac53d98`). Todas as URLs dos dois índices (`nav.js` e `busca/index.html`) testadas contra o disco: 21 corrigidas, 0 quebradas restantes. A substituição dos índices manuais por um índice gerado é a próxima frente sugerida.
- **Revisão das páginas com estilos inline** (2.933 com `<style>` próprio): checar visualmente, por amostragem, o conflito com Sora/Inter e com os tokens novos.
- Itens já listados no briefing: modelo de introdução das cartas paulinas (piloto 1 Tessalonicenses ou Filemom), títulos "Capítulo N" em Romanos, "1 capitulos" em Filemom, menu do NT com 8 livros, "próximo" de Filemom → Hebreus 1, faixa de data de Gálatas, personagens que faltam (Timóteo, Tito, Onésimo, Barnabé, Silas, Priscila e Áquila).

## Ideias futuras (registradas em 09/10/2026; não implementar sem decisão do Wagner)

1. **Camada do idioma original:** hebraico no Antigo Testamento e grego koiné no Novo Testamento.
   - Começar por um **piloto de poucas páginas** (ex.: Salmo 23 e João 3).
   - Em cada página do piloto: o texto original, a transliteração e o significado das palavras-chave.
2. **Versões completas em hebraico e/ou árabe:** possibilidade, **só depois** de haver revisores nativos e dados de demanda que justifiquem.
