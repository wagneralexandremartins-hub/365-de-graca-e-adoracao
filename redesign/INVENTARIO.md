# Inventário do site — 08/10/2026

Levantamento **somente leitura** feito na branch `redesign/navegacao-awexpress` (215e919b, igual à `main` no conteúdo publicado). Nenhuma página, CSS, JS ou sitemap foi alterado.

**Método.** Varredura de todos os `.html` publicáveis (fora de `_backups/`, `redesign/`, `scripts/`, `.claude/`, `.github/`), 5.652 arquivos. As contagens vêm da leitura de cada arquivo: title, H1, description, canonical, hreflang, og:image, JSON-LD, links `<a href>`, recursos (`img/script/link`) e texto do `<body>`. Os links foram resolvidos pelas regras do GitHub Pages (pasta com `index.html`, `/x` → `x.html`). Os scripts ficaram no scratchpad da sessão e não entram no repositório.

---

## 1. Mapa do site

5.652 arquivos HTML, dos quais **149 são stubs de redirect** (128 PT, 21 ES). Sobram **5.503 páginas reais**.

| Área | PT | EN | ES | Observação |
|---|---:|---:|---:|---|
| Bíblia AT — estudo por capítulo (blocos 01–05, `genesis/`, `antigo-testamento/`) | 1.106 | 957¹ | 957¹ | inclui 65 páginas de Tobias/Judite/1–2 Macabeus dentro de `03-historicos/` |
| Bíblia AT — texto ACF (`biblia/<sigla>/`) | 929 | — | — | |
| Bíblia NT — estudo (08 + 13-apocalipse) | 301 | 260 | 260 | 13-apocalipse tem 13 páginas |
| Bíblia NT — texto ACF (`biblia/`) | 260 | — | — | |
| Índice da Bíblia (`biblia/index.html`) | 1 | — | — | |
| Apócrifos/deuterocanônicos (`06-apocrifos/`) | 146 | 61 | 61 | |
| Estudos (`estudos/` 32 + `02-pentateuco/genesis/estudos/` 88) | 120 | 1 | 1 | 22 são placeholder (ver §6) |
| Fontes Históricas | 0 | — | — | não tem páginas próprias: é só o rótulo do 06-apocrifos dentro de `estudos/index.html` |
| História/contexto (07, 09, 10, 11, 12) | 43 | — | — | 8 + 8 + 9 + 9 + 9 |
| Personagens | 16 | — | — | 15 perfis + índice |
| Mapas | 1 | — | — | 11 mapas em SVG inline |
| Linha do Tempo | 3 | — | — | `timeline/` + 2 fragmentos na raiz |
| Busca | 2 | — | — | inclui `index_backup.html` |
| Loja (`loja-365/`, `ebook-4-passos/`) | 2 | — | — | |
| Institucionais (home, sobre ×3, privacidade, 404, blocos, como-estudar ×2, referências, sitemap-visual, autismo-e-fe) | 12 | 1 | 1 | |
| Outras (`contexto/index.html`) | 1 | — | — | |
| **Total** | **2.943** | **1.280** | **1.280** | |

¹ EN/ES AT: 930 capítulos + 27 páginas `*-block-N` (Pentateuco, de 53 a 71 palavras cada).

EN e ES só cobrem a Bíblia (capítulos), além de 1 índice e 1 página de estudos cada. Nenhuma área temática (estudos, história, personagens, mapas, linha do tempo) existe em EN/ES. Em ES há `john-N` (21 stubs) apontando para `juan-N`.

---

## 2. Temas

Contagem só nas páginas PT reais, **sem o texto ACF puro** (`biblia/`), para não inflar os números. Um tema conta como "título/H1" quando aparece no H1 ou no title (sem o nome do site).

| Tema | Págs com menção | ≥5 menções | Página dedicada (H1) | Situação |
|---|---:|---:|---|---|
| fé | 1.066 | 365 | Est.: *Fé em tempos de incerteza*, *Como viver a fé no mundo digital*; Personagem Abraão | só estudos placeholder; **lacuna** de página-tema |
| oração | 583 | 253 | *Oração que transforma a vida* (placeholder) | **lacuna** |
| jejum | 45 | 7 | só títulos de capítulo (Mt 6, Zc 7, Jdt 4) | **lacuna** |
| perdão | 180 | 54 | *Perdão e restauração* (placeholder) | **lacuna** |
| amor | 642 | 141 | nenhuma (Cânticos tem o maior volume) | **lacuna** |
| esperança | 724 | 93 | *Reconciliação e Esperança* (12), 2 estudos placeholder | **lacuna** |
| graça | 1.083 | 251 | `01-principio/adao-graca.html` | menções fortes; sem página-tema |
| misericórdia | 585 | 112 | só capítulos (Sl 51, 136, Tt 3, Eclo 18) | **lacuna** |
| justiça | 947 | 246 | só capítulos (Jó, Salmos, Amós) | **lacuna** |
| santidade | 413 | 158 | Lv bloco 5 *Santidade e Festas*; estudo placeholder | parcial |
| Reino de Deus | 282 | 90 | nenhuma | **lacuna** |
| Trindade | 45 | 4 | nenhuma (melhor: Constantinopla I, Pais da Igreja) | **lacuna** |
| Jesus/Messias | 465 | 77 | *O Messias Esperado* (07) | parcial |
| cruz | 498 | 41 | **`estudos/cruz-de-cristo/`** (4.244 palavras) | **dedicada** |
| ressurreição | 422 | 23 | só capítulos (1Co 15, Jo 11, Jo 20, Ez 37) | **lacuna** |
| parábolas | 72 | 9 | só capítulos (Mt 13, Mc 4, Lc 15) | **lacuna** |
| milagres | 140 | 26 | só capítulos | **lacuna** |
| Espírito Santo | 365 | 74 | só capítulos (Jo 16, Mt 12) + *Pentecostes* (09) | parcial |
| dons | 29 | 1 | só 1Co 12 | **lacuna** |
| fruto do Espírito | 11 | 0 | só Gl 5 | **lacuna** |
| cânon | 43 | 2 | nenhuma (`06-apocrifos/index` trata 14×) | **lacuna** |
| manuscritos | 18 | 1 | nenhuma | **lacuna** |
| Septuaginta | 148 | 6 | nenhuma (Período Helenístico 15×) | **lacuna** |
| Vulgata | 9 | 0 | nenhuma | **lacuna** |
| fariseus / saduceus / essênios | 31 / 9 / 14 | 5 / 2 / 1 | **`07-intertestamentario/grupos-judaicos/`** (os três no H1) | **dedicada** |
| Segundo Templo | 19 | 2 | *O mundo do Segundo Templo* (placeholder) + Período Persa | parcial |
| Roma | 532² | 98² | **`07-intertestamentario/periodo-romano/`**; estudo placeholder | **dedicada** |
| Babilônia | 510 | 35 | **`13-apocalipse/babilonia/`** (Babilônia do Apocalipse); o exílio está em 2Rs/2Cr/Período Persa | parcial: não há página do exílio |
| Pérsia | 111 | 44 | **`07-intertestamentario/periodo-persa/`** | **dedicada** |
| Grécia | 257 | 9 | **`07-intertestamentario/periodo-helenistico/`** | **dedicada** |

² "romanos" também casa com a carta aos Romanos; o número está inflado.

**Resumo:** 6 temas têm página dedicada de verdade (cruz, grupos judaicos, Roma, Pérsia, Grécia/helenismo e, em parte, Messias). Os temas de vida cristã (fé, oração, perdão, esperança, santidade) só têm estudos **placeholder** de cerca de 245 palavras. Os temas doutrinários (Trindade, Reino, Espírito Santo, dons, fruto) e os de transmissão do texto (cânon, manuscritos, Septuaginta, Vulgata) não têm página nenhuma, mas há muitas menções para listar.

---

## 3. Personagens, Mapas e Linha do Tempo

### Personagens
| Item | Número |
|---|---:|
| Perfis com página própria | 15 (Abraão, Moisés, José, Davi, Salomão, Josué, Elias, Isaías, Jeremias, Rute, Ester, Paulo, Pedro, João, Maria) |
| Perfis longos (1.200 palavras ou mais) | 4 (Abraão, Moisés, Davi, Paulo) |
| Perfis curtos (330–560 palavras) | 11 |
| Personagens só em lista ou busca, sem página | Daniel (a busca manda para o livro); Adão, Caim e Abel têm páginas em `01-principio/`, fora de Personagens |
| Links de capítulos para perfis | **0** de 1.106 capítulos do AT; 1 só no NT (o hub do NT, que liga 4 perfis) |

### Mapas
| Item | Número |
|---|---:|
| Mapas na página `/mapas/` | 11, todos em SVG inline (nenhuma imagem faltando ali) |
| Links de `/mapas/` para conteúdo | só índices de bloco (01, 02, 03, 08, 13) |
| Páginas de capítulo com imagem de mapa que existe | 247 (Gênesis 37, 1–2 Sm, 1–2 Rs, 1–2 Cr, Ed, Ne, Et, alguns profetas) |
| Páginas com **imagem de mapa faltando (404)** | **67**: Gênesis 45 (`mapa-oriente-proximo.jpg`), Josué 20 (20 nomes diferentes de `mapa-*.jpg`), Jonas 1, `timeline-component.html` 1 (`/CAMINHO_DO_MAPA`) |

### Linha do Tempo
- `timeline/index.html`: **10 eras** (Criação → Reforma e Escatologia), **39 eventos** (cartões `tl-event` com data, nome, descrição e tags) e filtro por era.
- Os eventos só levam a índices de bloco (02 e 03 com 8 links cada, os demais com 1 a 4). Nenhum leva a capítulo, personagem ou mapa.
- Nenhuma página do site liga para eventos específicos (a entrada vem só do menu).
- Há também linhas do tempo soltas: `genesis/linha-do-tempo.html` (lê um `.md`), a página em `01_PENTATEUCO/.../linha-do-tempo.html` (caminho duplicado) e a seção "Contexto Histórico & Geográfico" embutida em 86 páginas de Gênesis/Êxodo. Os fragmentos `timeline-component.html` e `timeline-genesis-1.html` estão na raiz sem `<head>`.

---

## 4. Busca atual

| Item | Situação |
|---|---|
| Onde está | **Dois índices separados, escritos à mão no código**: `BUSCA_INDEX` dentro de `busca/index.html` (array JS de cerca de 10 KB) e `SEARCH_INDEX` em `assets/js/nav.js` (15 KB no total) |
| Entradas | `busca/`: **76** (63 URLs distintas): 13 blocos, 25 livros AT, 16 NT, 11 personagens, 9 temas, 2 recursos. `nav.js`: **66** |
| Campos | `title`, `sub`, `url`, `tag`, `color` (sem texto, sem palavras-chave, sem capítulo) |
| Como busca | substring em `title + sub`; na `busca/` sem acento, no `nav.js` com acento |
| Cobertura | **76 de cerca de 5.500 páginas (1,4%)**. Não acha capítulos, versículos, estudos, páginas de história (07–12), Apócrifos nem EN/ES. Faltam livros: AT 25 de 46 canônicos + deutero, NT 16 de 27 |
| Temas | os 9 "temas" apontam para `/busca/?q=…`, ou seja, buscam a si mesmos e só acham o que já está no índice |
| **Links 404** | `busca/`: **12** (1-samuel, 2-samuel, 1-reis, 2-reis, cantico, 1-corintios, 2-corintios, 1-pedro + Davi, Salomão, Elias, Pedro, que usam esses mesmos caminhos). `nav.js`: **9** |
| Quem usa `nav.js` | 20 páginas (15 personagens, mapas, timeline, busca, como-estudar, índice de personagens); só 2 têm o overlay `#search-overlay` |

**Causa provável do bug:** os índices foram escritos à mão com slugs **hifenizados** (`1-samuel`, `1-reis`, `1-corintios`, `1-pedro`, `cantico`), mas as pastas reais não têm hífen (`1samuel`, `1reis`, `1corintios`, `1pedro`, `canticos`). O hífen só existe em `06-apocrifos/1-macabeus`, o que sugere cópia desse padrão. Como os dois índices são listas manuais, não acompanham o site.

---

## 5. Links internos

Sem contar o menu global, que liga todas as páginas aos 10 índices principais:

| Situação | Número |
|---|---:|
| Páginas órfãs (nenhum link de entrada) | **30**: 9 em `genesis/estudos` (inclui os 6 `pasted_*`/NUL), 8 em `genesis/` (rascunhos `00-…`/`04-…`, `_template`), 4 texto ACF NT, 1 ACF AT, 404, privacidade, `sitemap-visual`, `sobre/proposito`, `contexto/`, `busca/index_backup`, 2 fragmentos de timeline |
| Com 1–2 links de entrada | texto ACF AT 919 de 929 · ACF NT 256 de 260 · AT estudo 140 · Estudos 38 · Apócrifos 15 · História 15 |
| Mapas, Linha do Tempo | **0** links contextuais (só o menu) |
| Perfis de personagem | só o índice de personagens, os outros perfis e (4 deles) o hub do NT |

**Áreas que não se conectam** (páginas que têm pelo menos 1 link contextual para o destino):

| Origem ↓ / destino → | Personagem | Estudo | História 07–12 | Texto ACF | Mapa/Timeline específico |
|---|---:|---:|---:|---:|---:|
| Capítulos AT (1.106) | 0 | 0 | 1 | **0** | 8 |
| Capítulos NT (301) | 1 | 1 | 1 | **0** | 0 |
| Apócrifos (146) | 0 | 0 | 1 | 0 | 0 |
| Texto ACF (1.189) | 0 | 0 | 0 | (só entre si) | 0 |
| Estudos (120) | 0 | 31 (entre si) | 1 | 0 | 0 |
| História 07–12 (43) | 0 | 0 | 43 (entre si) | 0 | 0 |
| Personagens (16) | 16 (entre si) | 0 | 0 | 0 | 0 |

Ou seja, cada área só se liga a ela mesma. **Capítulo de estudo ↔ texto ACF do mesmo capítulo** (1.189 pares possíveis) não tem nenhum link.

**Links quebrados:** PT 46 pares (AT 39, Estudos 6, Busca 1; p.ex. `/01-antigo-testamento`, `/genesis/criacao.html`). **EN/ES 2.637 pares**: o link "ver em português" usa o formato antigo `/0N-…/livro/capitulo-NN/` (inexistente), e a navegação anterior/próximo do NT usa `capitulo-NN.html` relativo, que não existe em `/en/<livro>-N/`. Há também 40 links para `/08-nuevo-testamento/`.

---

## 6. SEO e idiomas

| Área | n | title | descr. | H1 = 1 | canonical | hreflang | trilha visível | BreadcrumbList |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AT estudo | 1.106 | 1.105 | 1.097 | 1.041 (62 com 2+, 3 sem) | 1.105 | 0 | 54 | 12 |
| AT texto ACF | 929 | 929 | 929 | 929 | 929 | 0 | 0 | 0 |
| NT estudo | 301 | 301 | 301 | 301 | 273 (28 sem) | 0 | 260 | 0 |
| NT texto ACF | 260 | 260 | 260 | 260 | 260 | 0 | 0 | 0 |
| Apócrifos | 146 | 146 | 146 | 146 | 146 | 0 | 0 | 0 |
| Estudos | 120 | 120 | 120 | 45 (55 com 2+, 20 sem) | 120 | 31 | 76 | 0 |
| História 07–12 | 43 | 43 | 43 | 43 | 43 | 0 | 0 | 0 |
| Personagens | 16 | 16 | 16 | 16 | 16 | 0 | 16 | 0 |
| Institucional | 12 | 12 | 8 | 12 | 11 | 1 | 1 | 0 |
| EN (1.280) / ES (1.280) | — | todas | todas | todas | 1.253 cada (27 `-block` sem) | 1.253 cada | 1.250 cada | 0 |

**Achados:**
- **Canonical × sitemap:** 4.038 páginas têm canonical **sem extensão** (`/…/capitulo-01`), enquanto o `sitemap.xml` lista a URL com `.html`. Só 31 coincidem. As duas formas abrem a página no GitHub Pages, mas o Google recebe sinais diferentes.
- **URLs duplicadas:** 223 pastas recebem links internos em 2 ou 3 formas (`/x/`, `/x/index.html`, `/x`). O sitemap usa uma forma por página (4.152 URLs, 0 em 404, 0 redirects).
- **Fora do sitemap:** 1.351 páginas reais: os 1.189 textos ACF de `biblia/`, os 88 `genesis/estudos`, 60 páginas de `genesis/`, `busca/`, `biblia/index` e outras. EN/ES estão todas dentro, mas o sitemap não declara hreflang.
- **hreflang:** só EN/ES e 31 estudos. O PT não declara nada, então falta reciprocidade. Dos alternates `pt-BR` declarados, **1.672 de 2.536 dão 404** (formato antigo de URL). `es`: 7 em 404. Nenhum `x-default`.
- **Títulos duplicados:** 367 grupos, 742 páginas. Capítulo de estudo × texto ACF com o mesmo title (p.ex. "Deuteronômio 1 — 365 de Graça & Adoração"); 1 Samuel com `cap-NN.html` (8) duplicando `capitulos/capitulo-NN.html`; 47 estudos de Gênesis.
- **"Bloco N" errado no title:** 52 páginas (13-apocalipse diz "Bloco 12", 10 diz "Bloco 09", 11 diz "Bloco 10", 12 diz "Bloco 11", 09 diz "Bloco 08", mais 9 no Pentateuco). *Decisão do Wagner: o title é rótulo, mas é texto.*
- **Descriptions repetidas:** "Situando este capítulo na linha do tempo bíblica" (37), "Oráculos contra as Nações" (26) e outras.
- **404 conhecidos (pares página→recurso):** `og-cover.jpg` **2.825** · `/styles.css` **1.196** · `mapa-oriente-proximo.jpg` 45 · outros mapas 22 · `favicon.png` 5 · `og-image.jpg` 2 (o arquivo real é `.png`) · `/home/ubuntu/upload/…jpg` 1. **2.663 páginas** (todas EN/ES e parte do PT) não têm `og:image`.
- **Placeholders:** `genesis/genesis-12` a `-50` (39 páginas com 12–17 palavras, AdSense, fora do sitemap); 22 estudos "Base introdutória para expansão futura" (cerca de 245 palavras, textos-chave sem referência); 27×2 páginas `*-block-N` em EN/ES; 1 Sm 13 e 1 Sm 29 com 0 palavras; Nm 24 com 29 palavras; rascunhos em `genesis/` (`00-…`, `_template`).
- **AdSense** está em praticamente todas as páginas, inclusive nos placeholders. Nenhuma página tem `noindex`.

---

## 7. Dados estruturados (schema)

| @type | Páginas | Onde |
|---|---:|---|
| Article + Organization + Person (autor) | 4.818 / 4.818 / 4.807 | quase todas: capítulos AT/NT, texto ACF, Apócrifos, História, Estudos, Personagens e EN AT/Apócrifos. **Ausente** em EN NT (254 de 260), em todo o ES NT e nos 28 capítulos de Mateus do NT PT sem canonical |
| BreadcrumbList | 12 | só AT (Gênesis) |
| ImageObject | 11 | AT |
| FAQPage (Question/Answer) | 2 | AT |
| WebSite | 2 | home + 1 AT |
| CollectionPage | 1 | AT |

Não existe `Person` para os personagens bíblicos (o `Person` atual é o autor), nem `Book`/`Chapter`, `Place` (mapas), `Event` (linha do tempo) ou `SearchAction`. O texto ACF (`biblia/`) está marcado como `Article`.

---

## Pronto para ligar

O que já existe e só precisa de links ou índice, sem texto editorial novo:

1. **Capítulo de estudo ↔ texto ACF**: 1.189 pares por tabela livro/capítulo (siglas do `biblia/` × pastas dos blocos). É hoje a maior desconexão do site.
2. **Busca com índice gerado**: extrair title/H1/description/URL das cerca de 4.150 páginas do sitemap para um JSON estático. Corrige os 12 + 9 links 404 e passa de 76 para milhares de entradas. Unificar `busca/` e `nav.js` num índice só.
3. **Perfis de personagem → capítulos**: os perfis já citam as referências (p.ex. Elias "1 Reis 17 – 2 Reis 2"), basta transformar em link. No sentido inverso, um bloco "Personagens deste capítulo" nos capítulos citados, usando só os 15 nomes existentes.
4. **Linha do Tempo → capítulos e páginas de história**: os 39 eventos já têm tag de livro/bloco; trocar os links de índice de bloco pelo capítulo ou página 07–12 correspondente.
5. **Mapas → capítulos**: os 11 mapas SVG já nomeiam lugares e blocos; ligar ao capítulo exato e, de volta, dos capítulos ao mapa.
6. **Temas com página dedicada que só precisam de entrada**: cruz, grupos judaicos, períodos persa/helenístico/romano, Messias esperado, Pentecostes. Ligar dos capítulos com 5 ou mais menções (as listas da varredura já existem).
7. **SEO técnico sem conteúdo**: canonical alinhado ao sitemap; uma forma única de URL nos links; `og:image`/`favicon` apontando para arquivos que existem (`og-image.png`, `favicon.ico`); `/styles.css` (1.196); hreflang `pt-BR` corrigido e PT recíproco; links EN/ES quebrados (2.637); BreadcrumbList a partir da trilha visível que já existe (EN/ES 2.500, NT 260, Estudos 76, Personagens 16).

## Lacunas reais (dependem de aprovação do Wagner)

1. **Páginas-tema**: só existem para cruz, grupos judaicos e períodos históricos. Fé, oração, jejum, perdão, amor, esperança, graça, misericórdia, justiça, santidade, Reino de Deus, Trindade, ressurreição, parábolas, milagres, Espírito Santo, dons, fruto do Espírito, cânon, manuscritos, Septuaginta, Vulgata, Segundo Templo e exílio babilônico não têm página. Mesmo uma página "índice de tema" precisa de pelo menos um parágrafo de abertura, que é texto editorial.
2. **22 estudos placeholder** com texto genérico: completar ou tirar da navegação é decisão editorial.
3. **Personagens**: 11 dos 15 perfis são curtos. Personagens novos (Daniel, Adão, Noé, Jacó, Samuel, Neemias, Esdras, Jesus etc.) exigem conteúdo.
4. **67 imagens de mapa faltando** (Gênesis 45, Josué 20, Jonas 1): exigem arte nova (Artlist/Nano Banana Pro) ou decisão de remover a referência.
5. **Fontes Históricas** não existe como área (é só o rótulo do 06-apocrifos). Decidir se vira seção com páginas próprias (cânon, manuscritos, Septuaginta, Vulgata, Josefo, Qumran) e o destino das 65 páginas de Tobias/Judite/Macabeus duplicadas em `03-historicos/`.
6. **Perguntas (FAQ)**: há seção de perguntas/reflexão em cerca de 223 páginas (87 Pentateuco, 116 NT, 12 `genesis/`, 4 bloco 01, 3 estudos, 1 Históricos) e FAQPage em 2. Gerar perguntas novas é editorial; marcar como FAQPage as que já existem também pede decisão (são perguntas de reflexão, não de "dúvida frequente").
7. **EN/ES temáticos**: nenhuma página de estudo, história, personagem, mapa ou linha do tempo traduzida.
8. **Textos de rótulo a decidir**: "Bloco N" errado em 52 titles; títulos duplicados estudo × ACF (diferenciar exige escolher o rótulo); placeholders `genesis-12..50` e `*-block-N` (manter, `noindex` ou tirar AdSense).

## Ordem sugerida

| # | Frente | O que entra | Risco | Esforço |
|---|---|---|---|---|
| 1 | **SEO técnico** | og/favicon, `/styles.css`, canonical = sitemap, forma única de URL, hreflang, links EN/ES, BreadcrumbList da trilha existente | baixo (só `<head>` e hrefs, em lote com prova byte a byte), mas toca cerca de 5.000 páginas | médio |
| 2 | **Busca** | índice JSON gerado das páginas reais + 1 script de busca; aposentar os 2 índices manuais | baixo (só `busca/` e 1 JS) | médio |
| 3 | **Links internos: estudo ↔ ACF** | 1.189 pares por tabela | baixo-médio (insere 1 bloco por página em 2.378 páginas) | baixo |
| 4 | **Personagens (ligar)** | perfis → capítulos; capítulos → perfis (só os 15) | baixo | baixo |
| 5 | **Linha do Tempo e Mapas (ligar)** | eventos e mapas → capítulos/história, e o caminho de volta | baixo | baixo-médio |
| 6 | **Temas (índices)** | páginas de tema que listam o que já existe | médio: precisa de texto de abertura aprovado e de rótulos novos | médio |
| 7 | **Perguntas** | decidir formato; FAQPage só depois | médio (editorial) | médio |
| 8 | **Conteúdo novo** | placeholders, perfis curtos, mapas faltando, Fontes Históricas, EN/ES temáticos | alto (editorial) | alto |

**Decisões pendentes do Wagner anotadas aqui, sem decidir:** "Bloco N" nos titles; o que fazer com os 22 placeholders, `genesis-12..50` e `*-block-N` (manter, `noindex` ou tirar AdSense); se Fontes Históricas vira área; destino das 65 páginas deutero em `03-historicos/`; se as perguntas de reflexão viram FAQPage; forma canônica de URL (`.html` como o sitemap ou sem extensão como os canonicals atuais).
