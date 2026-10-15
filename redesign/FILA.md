# Fila de frentes — 365 Graça & Adoração

Uma frente aberta por vez; a próxima só começa depois do "Pronto" do Wagner. Só o Wagner marca "Pronto".
Situação: **na fila**, **aberta** ou **pronta**. Detalhes de cada frente em `redesign/PLANO.md`.

Criada em 15/10/2026.

| Nº | Frente | Critério de pronto | Situação | Dependência | PR |
|---|---|---|---|---|---|
| 1 | Grego em todos os versículos do NT em PT: 2 Pedro e 1 João | 2 Pedro e 1 João no ar, com a lista de correções aprovada, prova byte a byte, regressão com 0 mudanças, prints aprovados e conferência no ar com curl | aberta | — | anteriores: #20, #21, #22, #23 |
| 2 | Lote de correção das páginas já publicadas (Jd 1, Jd 17, 2 Jo 12, Jo 3:13; dúvida em Jd 14) | Lista aprovada pelo Wagner, correções no ar (JSON e páginas, inclusive o estudo de João 3), prova de letras iguais às do byztxt e conferência no ar | na fila | 1 | — |
| 3 | Export do Search Console (16 meses: consultas, páginas, países, filtros de perguntas, Indexação > Páginas) | Arquivos exportados pelo Wagner e lidos, com resumo registrado no PLANO | na fila | Wagner | — |
| 4 | Decisão da frente 0 (páginas de modelo EN/ES: tradução revisada, noindex ou manter) | Decisão do Wagner registrada no PLANO | na fila | 3 | — |
| 5 | Botões flutuantes e `.chapter-nav` nas páginas de `biblia/` | Botões sem cobrir texto e crédito no celular (390 e 360 px), `.chapter-nav` com estilo, prints aprovados e conferência no ar | na fila | — | — |
| 6 | Lote 3.5, parte B (botão "próximo" cortado no celular) | Prints aprovados pelo Wagner e correção no ar | na fila | aprovação do Wagner | — |
| 7 | Lote 2: menu central EN/ES (`site-nav.js` trilíngue) | Rótulos EN/ES aprovados, menu central no ar em EN/ES, prints aprovados | na fila | rótulos EN/ES | — |
| 8 | Busca em PT (índice gerado) | Busca com índice gerado no ar em PT, sem links 404, testada no navegador | na fila | — | — |
| 9 | Piloto de Perguntas sobre a Bíblia | Piloto aprovado pelo Wagner e no ar | na fila | 3 e 4; plano em `redesign/plano-perguntas-biblia.md` (branch `docs/plano-perguntas`) | — |
