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
