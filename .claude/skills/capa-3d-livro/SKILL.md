---
name: capa-3d-livro
description: Capa 3D de livro (só CSS) nas páginas de abertura dos livros bíblicos do 365. Use ao levar a capa para novos livros, ajustar nome/cor/capítulos de uma capa ou mexer em scripts/aplicar_capa3d.py e assets/css/capa-livro.css.
---

# Capa 3D de livro

## Regras fixas do projeto
- Nunca alterar texto editorial (estudos, exegese, versículos, títulos) sem autorização explícita do Wagner.
- Trabalhar só em branch; nunca na `main`. Perguntar antes de cada commit e de cada push. Nada de merge na `main` sem ordem explícita.
- Site 100% estático (HTML, CSS e JS puros), mudanças incrementais, preservar todas as URLs.
- Responder em português do Brasil.

## Peças
- `assets/css/capa-livro.css` — a capa e as poucas regras de encaixe, todas presas à capa (`.capa3d-faixa ~ …`), para não afetar páginas sem capa. Cor por grupo: `data-grupo="at"` (âmbar), `"nt"` (azul), `"deutero"` (roxo). A animação usa `fill: backwards` (com `both` a lombada some).
- `scripts/aplicar_capa3d.py` — insere a capa. Tabela `LIVROS`: pasta, nome, grupo, capítulos (cânon), texto da lombada, `--capa-nome` (None = 15cqi) e topo esperado.

Em cada página o script acrescenta só duas coisas: a linha `<link rel="stylesheet" href="/assets/css/capa-livro.css">` antes de `</head>` e o bloco `<!-- capa3d:v1 --> … <!-- /capa3d:v1 -->` logo depois do fim do menu central no `<body>`. Nada mais é tocado.

## Onde aplicar
- **Só na página de abertura do livro:** `<bloco>/<livro>/index.html`. Nunca em capítulos.
- Se um livro tiver mais de uma página candidata, liste as candidatas e **não escolha sozinho**.
- Ficaram fora por decisão do Wagner: `biblia/<sigla>/index.html` (índice do texto bíblico), `13-apocalipse/index.html` (bloco "Apocalipse Aprofundado") e Tobias, Judite, 1–2 Macabeus (duplicados em `03-historicos` e `06-apocrifos`, decisão pendente).
- Estado em 07/10/2026: 44 livros com capa (17 do AT: Pentateuco + Históricos canônicos; 27 do NT).

## Dados da capa
- Nome, grupo e capítulos vêm **da tabela**, nunca do texto da página. Capítulos = cânon; o script confere com as páginas de capítulo no disco e recusa se não bater.
- Nome igual ao `<h1>` da página (ex.: "Atos dos Apóstolos", em 2 linhas).
- "1 capítulo" no singular (Filemom, 2 e 3 João, Judas).
- Nomes longos: meça no navegador o maior tamanho em que nenhuma palavra estoura a capa. Valores aprovados: Deuteronômio e Colossenses 13cqi; 1 e 2 Tessalonicenses 11.5cqi (o número fica na primeira linha, como no protótipo).

## Procedimento (uma aprovação por etapa)
1. Mapeamento só leitura das páginas pedidas: topo logo depois do menu (`div.wrap`, `div.hero`, `main.container`…), estrutura da página e capítulos no disco. Agrupe as páginas por estrutura.
2. `python scripts/aplicar_capa3d.py` (dry-run, padrão; `--only livro,livro`, `--diff-out arquivo`). Mostre: a alterar, não tocadas e motivo (topo diferente, capítulos que não batem). Página com topo diferente é pulada e listada.
3. Piloto em um livro, só na prévia (servidor local), com prints 1280 e 390, escuro e claro, e uma página de cada estrutura medida. **Pare para revisão.**
4. Depois do OK: `--apply` (backup zip em `_backups/capa3d-AAAAMMDD-HHMMSS.zip`, nunca em commit).
5. Prova independente contra o zip: arquivo novo menos o bloco da capa e a linha do `<head>` == original, byte a byte. Segunda execução deve dar "0 a alterar".
6. Rolagem horizontal em 1280/768/390/360, escuro e claro, em todas as páginas do lote (e nenhum nome estourando a capa). Folha com todas as capas lado a lado para conferência.
7. Commit separado (páginas + script), mensagem por arquivo (`git commit -F`), sem push.

## Dicas de validação
- O Chrome headless não abre janela abaixo de ~500px: para 390/360, carregue a página num `<iframe>` da largura exata.
- No Windows, rode o Chrome pelo PowerShell (`Start-Process`) e ponha entre aspas argumentos com espaço (`--host-resolver-rules=…`).
- Bloqueie o AdSense nos testes (`--host-resolver-rules="MAP pagead2.googlesyndication.com 127.0.0.1"`).
