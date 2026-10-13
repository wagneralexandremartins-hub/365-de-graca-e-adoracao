# Plano — Perguntas sobre a Bíblia, páginas-mestre de temas e busca

**Data:** 13/10/2026 · **Situação:** análise somente leitura, nada executado; aguarda avaliação do Wagner.

A análise foi feita só lendo arquivos, contando páginas e comparando textos; nada no site foi alterado.

## 0. O achado que muda a prioridade

As cinco consultas com demanda não são perguntas. São pedidos de **explicação de capítulo** em espanhol ("isaías 29 explicación", "daniel 10 estudio bíblico"). Quem responde a essas buscas são as páginas de capítulo ES, e muitas delas não têm conteúdo próprio:

| | Capítulos AT/deuterocanônicos | Páginas com texto de modelo (iguais, trocando só nome e número) |
|---|---|---|
| ES | 1.038 | **908** |
| EN | 1.017 | **887** |
| PT | 940 | **183** (quase todas em Profetas) |

| Consulta com demanda | Página ES | Página PT |
|---|---|---|
| 1 crónicas 18 explicación | modelo (96% igual a outras) | texto próprio (cerca de 4.160 palavras) |
| isaías 29 estudio/explicación | modelo (100%) | **modelo** (igual a Isaías 30) |
| lamentaciones 2 explicación | modelo (100%) | texto próprio |
| daniel 10 estudio bíblico | modelo (100%) | **modelo** (igual a Daniel 11) |

Além disso, os títulos ES saem sem acento ("Isaias", "Cronicas", "Capitulo", "Adoracion"), e as descrições são genéricas.

**Consequência:** a demanda comprovada hoje pede capítulos AT em espanhol com conteúdo real, e não uma área nova de perguntas. Cerca de 2.000 páginas de modelo também são um risco de SEO, porque o Google trata texto repetido em grande escala como sinal de baixa qualidade. Recomendo uma **frente 0**, decisão editorial do Wagner, a resolver antes de qualquer página nova:
- refazer as páginas ES com tradução revisada do PT, onde o PT tem texto próprio;
- marcar as demais como "não indexar" até haver texto;
- ou manter como está, sabendo do risco.

Uma área de Perguntas feita no mesmo molde agravaria o problema.

## 1. O que já existe

| Função pedida | O que o site já tem | Situação |
|---|---|---|
| Perguntas | seções "perguntas para reflexão" em cerca de 223 páginas; marcação de FAQ em 2 | são perguntas de reflexão, não de dúvida |
| "Quem eram os fariseus?" | `07-intertestamentario/grupos-judaicos/` | já responde |
| "O que aconteceu entre Malaquias e Mateus?" | `07-intertestamentario/` + 6 subpáginas (períodos, expectativa messiânica) | já responde |
| "Quem era Melquisedeque?" | Hebreus 5 e 7 (34 páginas citam) | coberto dentro de capítulos |
| "O que é nascer de novo?" | João 3 (agora com o grego) | coberto dentro de capítulo |
| "Por que Jesus chorou?" | 1 menção, em João 11 | fraco |
| "O que significa Emanuel?" / "Quantos livros tem a Bíblia?" | 18 menções / cânon tratado só em `06-apocrifos` | sem página |
| Páginas-tema | dedicadas: cruz, grupos judaicos, períodos persa, helenístico e romano, Messias esperado, Pentecostes | as outras não existem |
| Graça, fé, oração, Reino, aliança, redenção, ressurreição | de 247 a 1.083 páginas citam cada tema; nenhum tem página própria | maior lacuna de navegação |
| Estudos | 8 categorias, 22 com texto provisório de cerca de 245 palavras | precisam de decisão editorial |
| Personagens / mapas / linha do tempo | 15 perfis / 11 mapas / 39 eventos | não se ligam aos capítulos |
| Busca | 76 entradas escritas à mão, só PT; o ícone do menu sempre abre a busca em português | muito limitada |

## 2. Reaproveitar, melhorar ou criar

- **Reaproveitar sem texto novo:** as páginas dedicadas acima, que viram destino de perguntas e temas; as listas de capítulos que mais citam cada tema (a contagem já existe); personagens, mapas e linha do tempo como links.
- **Melhorar:** a busca (seção 4); as ligações entre perfis, mapas, linha do tempo e capítulos (já propostas no inventário); os 22 estudos provisórios e as páginas de modelo (editorial).
- **Realmente novo:** páginas-mestre de temas sem página hoje (precisam de texto de abertura) e páginas de pergunta sem página equivalente, só as que tiverem demanda comprovada.
- **Regra contra duplicação:** uma intenção de busca, uma URL. Se uma página existente já responde (fariseus, período intertestamentário), a pergunta só aparece no índice apontando para ela, sem página nova. Se a resposta está dentro de um capítulo (Melquisedeque, nascer de novo), a página de pergunta só se justifica se acrescentar visão de conjunto. Caso contrário, compete com o capítulo.

## 3. Estrutura proposta

**URLs** (minúsculas, sem acento, hífens, barra no fim, uma forma só):
- PT: `/perguntas/`, `/perguntas/quem-era-melquisedeque/`, `/temas/`, `/temas/graca/`
- ES: `/es/preguntas/quien-era-melquisedec/`, `/es/temas/gracia/`
- EN: `/en/questions/who-was-melchizedek/`, `/en/themes/grace/`

**Página de pergunta**, adaptada à natureza de cada pergunta:
1. resposta direta em 2 a 3 frases;
2. explicação bíblica com referências em ACF;
3. contexto histórico, cultural e linguístico, quando couber;
4. interpretações divergentes, nomeadas como tais e não apresentadas como consenso;
5. relação com livros, personagens e acontecimentos;
6. links para capítulos, estudos, mapas e linha do tempo;
7. perguntas relacionadas;
8. bibliografia.

**Página-mestre de tema** (ex.: Graça):
- abertura curta;
- o tema no AT, nos Evangelhos e nas cartas de Paulo, cada parte com um parágrafo e links para os capítulos que mais tratam dele;
- relações com outros temas (graça e obras, graça e Reino);
- personagens, estudos e perguntas do tema;
- fontes.

A página-mestre organiza e aponta; não repete o que os capítulos já explicam.

**Dados estruturados:** `Article` + `BreadcrumbList`. A marcação de FAQ pode existir, mas desde 2023 o Google só exibe esse destaque para sites governamentais e de saúde, então não vale contar com ele.

**Plano incremental:**
1. Dados do Search Console (seção 6).
2. Busca melhorada (independe de conteúdo).
3. Piloto PT: 1 página-mestre e 3 a 5 perguntas com demanda comprovada.
4. Medir por 6 a 8 semanas.
5. Expandir pela demanda.
6. EN/ES.

## 4. Busca e descoberta (separada das páginas novas)

- **Índice gerado das páginas reais:** título, H1, descrição e URL num arquivo de dados estático, no lugar dos dois índices escritos à mão. Passa de 76 entradas para milhares.
- **Linguagem cotidiana:** ignorar acentos; tirar começos como "o que é", "quem foi", "qué es", "who was"; um dicionário pequeno de sinônimos, revisado pelo Wagner (salvação/salvo/salvar; fariseu/fariseus; Melquisedeque/Melquisedec/Melchizedek).
- **Um índice por idioma:** a lupa do menu abriria a busca do idioma da página.
- **Descoberta:** sugerir perguntas relacionadas a partir dos temas, personagens e capítulos ligados. As páginas de resultado (`?q=`) não seriam indexadas.
- **Risco:** baixo; mexe só na busca e em um script. O índice PT pode ser feito antes dos lotes EN/ES.

## 5. SEO: benefícios e riscos

- **Benefícios:** captar buscas longas com pergunta; concentrar links internos nos temas; mostrar profundidade temática.
- **Riscos e como evitar:**
  - *Concorrência com os capítulos* (ex.: "nascer de novo" × João 3): seguir a regra de uma intenção por URL.
  - *Páginas rasas ou geradas em massa:* só páginas revisadas, poucas por vez.
  - *Título e descrição:* próprios em cada página.
  - *Sitemap:* só páginas aprovadas.
  - *Canonical e idiomas:* canonical para a própria página; hreflang só entre páginas realmente equivalentes.
  - *Peso do que já existe:* o risco maior hoje são as cerca de 2.000 páginas de modelo; ver a seção 0.

## 6. As considerações A a D

**A. Idiomas.** Recomendação: começar só em PT. É a língua em que o Wagner revisa, e o hreflang só deve ligar páginas equivalentes. Página sem equivalente fica sem hreflang. As versões ES e EN entram depois, como traduções revisadas, cada uma com hreflang de ida e volta e entrada no sitemap. O sitemap atual (4.152 URLs) não declara hreflang; os cabeçalhos das páginas já declaram desde o PR #2. Como o tráfego é sobretudo ES, a prioridade ES é a frente 0, antes das perguntas.

**B. Demanda.** As cinco consultas pedem capítulos, não perguntas, então nenhuma justifica página de pergunta. Nada de perguntas inventadas. Para planejar com dados, é preciso este export do Search Console, em planilha como o de 09/10:
- *Desempenho, últimos 16 meses:* abas Consultas, Páginas, Países e Dispositivos, com cliques, impressões, CTR e posição;
- *a mesma visão filtrada* por páginas `/es/`, `/en/` e PT, e por país (México, EUA, Brasil, Venezuela, Colômbia);
- *filtros por expressão regular nas consultas:* palavras de pergunta nos 3 idiomas (o que, quem, qual, por que, como, quantos; qué, quién, cuál, por qué, cómo, cuántos; what, who, why, how, which) e termos de explicação (explicación, estudio, significado, explicação, meaning);
- *Indexação > Páginas:* motivos de não indexação, principalmente "rastreada, mas não indexada" e cópias.

**C. Autoria.**
- Nenhum texto existente é tocado sem autorização do Wagner.
- Fluxo proposto para página nova:
  1. pauta com prova de demanda;
  2. roteiro (Claude propõe: intenção, páginas existentes a ligar, referências);
  3. rascunho do texto teológico, feito pelo Wagner ou pelo Claude a pedido dele;
  4. revisão teológica do Wagner (divergências, citações ACF);
  5. revisão técnica do Claude (links, título, dados estruturados, acessibilidade);
  6. aprovação final explícita do Wagner;
  7. publicação pelo ritual de lote seguro.
- Traduções: mesmo fluxo, com aprovação do Wagner e, se possível, de um revisor nativo.
- Uma planilha de controle registra a situação de cada página.

**D. Dependência dos lotes EN/ES.**
- *Depende do lote 2:* incluir "Perguntas" e "Temas" no menu, com rótulos em três idiomas aprovados pelo Wagner, e a lupa abrindo a busca do idioma certo.
- *Depende do lote 3:* páginas EN/ES novas já nascerem com o menu central, e não com o cabeçalho antigo.
- *Depende do lote 5:* entradas a partir das homes EN/ES.
- *Lote 4 (barra inferior):* não afeta as páginas novas. Só evita mexer nos capítulos ao mesmo tempo, se depois forem acrescentados blocos de "perguntas relacionadas".
- *Pode andar antes dos lotes:* análise do Search Console, a decisão da frente 0, o índice de busca PT e os modelos de página.

---

## Decisões pendentes do Wagner

1. Se a frente 0 (páginas de modelo, sobretudo ES) entra antes desta área, e de que forma: tradução revisada, não indexar ou manter.
2. O export do Search Console descrito em 6.B.
3. Se aprova a estrutura de URLs e os modelos de página para um piloto PT futuro.

Nada será executado até essas decisões.
