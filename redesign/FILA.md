# Fila de frentes — 365 Graça & Adoração

Uma frente aberta por vez; a próxima só começa depois do "Pronto" do Wagner. Só o Wagner marca "Pronto".
Situação: **na fila**, **aberta** ou **pronta**. Detalhes de cada frente em `redesign/PLANO.md`.

Criada em 15/10/2026. Atualizada em 16/10/2026 (frente 1 pronta).

| Nº | Frente | Critério de pronto | Situação | Dependência | PR |
|---|---|---|---|---|---|
| 1 | Grego em todos os versículos do NT em PT: 2 Pedro e 1 João | 2 Pedro e 1 João no ar, com a lista de correções aprovada, prova byte a byte, regressão com 0 mudanças, prints aprovados e conferência no ar com curl | **pronta** (Wagner, 16/10/2026) | — | #25 (2 Pedro), #26 (1 João); anteriores: #20, #21, #22, #23 |
| 2 | Grego em todos os versículos do Apocalipse em PT (3 lotes, 22 capítulos) | Os 3 lotes no ar, com os 22 capítulos, a lista de acentos aprovada pelo Wagner, provas byte a byte, regressão com 0 mudanças, prints aprovados e conferência no ar | aberta | — | — |
| 3 | Lote de correção das páginas já publicadas (Jd 1, Jd 17, 2 Jo 12, Jo 3:13; dúvida em Jd 14) | Lista aprovada pelo Wagner, correções no ar (JSON e páginas, inclusive o estudo de João 3), prova de letras iguais às do byztxt e conferência no ar | na fila | 1 | — |
| 4 | Export do Search Console (16 meses: consultas, páginas, países, filtros de perguntas, Indexação > Páginas) | Arquivos exportados pelo Wagner e lidos, com resumo registrado no PLANO | na fila | Wagner | — |
| 5 | Decisão da frente 0 (páginas de modelo EN/ES: tradução revisada, noindex ou manter) | Decisão do Wagner registrada no PLANO | na fila | 4 | — |
| 6 | Botões flutuantes e `.chapter-nav` nas páginas de `biblia/` | Botões sem cobrir texto e crédito no celular (390 e 360 px), `.chapter-nav` com estilo, prints aprovados e conferência no ar | na fila | — | — |
| 7 | Lote 3.5, parte B (botão "próximo" cortado no celular) | Prints aprovados pelo Wagner e correção no ar | na fila | aprovação do Wagner | — |
| 8 | Lote 2: menu central EN/ES (`site-nav.js` trilíngue) | Rótulos EN/ES aprovados, menu central no ar em EN/ES, prints aprovados | na fila | rótulos EN/ES | — |
| 9 | Busca em PT (índice gerado) | Busca com índice gerado no ar em PT, sem links 404, testada no navegador | na fila | — | — |
| 10 | Piloto de Perguntas sobre a Bíblia | Piloto aprovado pelo Wagner e no ar | na fila | 4 e 5; plano em `redesign/plano-perguntas-biblia.md` (branch `docs/plano-perguntas`) | — |

## Frentes futuras (sem número de prioridade)

Entram na fila só quando o Wagner der número e critério de pronto.

- Grego no restante do NT: Evangelhos, Atos, cartas paulinas e Hebreus (o Apocalipse virou a frente nº 2).
