---
name: lote-seguro
description: Ritual obrigatório para qualquer alteração em lote no 365 (script que mexe em várias páginas, no sitemap ou em assets) — simulação por padrão, --apply só com OK do Wagner, backup zip, prova byte a byte, CRLF preservado, teste no navegador e commits separados sem push. Use sempre que uma etapa for tocar mais de um arquivo por script.
---

# Lote seguro

## Regras fixas do projeto
- Nunca alterar texto editorial (estudos, exegese, versículos, títulos) sem autorização explícita do Wagner.
- Trabalhar só em branch (a branch da etapa); **nunca na `main`**. Confira `git branch --show-current` antes de gravar e antes de cada commit.
- Perguntar antes de cada commit e de cada push. Nada de merge na `main` sem ordem explícita.
- Site 100% estático (HTML, CSS e JS puros), preservar todas as URLs; não apagar nem mover páginas.
- Responder em português do Brasil. Na dúvida, parar e perguntar; o que exigir decisão do Wagner é anotado, não decidido.

## 1. Script em `scripts/`
- Um script por assunto, com docstring dizendo o que muda, a decisão do Wagner (com data) e a prova.
- **Simulação por padrão.** Só grava com `--apply`. Modelos: `scripts/seo_arquivos_ausentes.py`, `scripts/sitemap_canonical.py`, `scripts/corrigir_hifen_busca.py`, `scripts/canonical_mateus.py` (inserir uma linha em várias páginas) e `scripts/hreflang_item4.py` (trocas, remoções e inserções em sub-etapas, milhares de arquivos).
- Ler e gravar em bytes (`rb`/`wb`), nunca reabrir em texto: assim CRLF, BOM e acentos ficam como estão.
- Casos fora do padrão **não são corrigidos por palpite**: o script os pula e lista com o motivo ("decisão pendente").
- Se qualquer prova falhar, o script sai com erro e não grava nada.

## 2. Simulação na tela (antes do OK)
Mostrar ao Wagner:
- quantos arquivos mudam, por pasta/idioma/tipo de troca, com exemplos antes → depois;
- o que fica de fora e por quê;
- a prova (item 4) rodada sobre o resultado simulado;
- os riscos (SEO, redirects, dependência do GitHub Pages, o que só vale depois do merge).
Depois **parar** e esperar o OK explícito do `--apply`.

## 3. Aplicar (só com OK)
- Backup zip em `_backups/<assunto>-AAAAMMDD-HHMMSS.zip` com cada arquivo como estava, gravado **antes** de escrever. `_backups/` nunca entra em commit.
- Arquivo novo: abrir com `'xb'` (falha se já existir; não sobrescreve).
- Rodar o script de novo depois de gravar: a nova simulação deve dar 0 mudanças.

## 4. Prova byte a byte
Por arquivo, conforme o tipo de troca:
- **Remoção de linha:** o novo é o antigo menos exatamente aquela linha (com sua quebra); a diferença de tamanho é o tamanho da linha; contagem de `\r\n` e `\n` cai só 1.
- **Troca dentro de um trecho** (ex.: `<loc>`): com o trecho mascarado, antigo e novo são idênticos; ordem e quantidade de trechos iguais; demais campos (ex.: `lastmod`, `priority`) idênticos em sequência.
- **Cópia/conversão de asset:** SHA-256 igual à origem (cópia) ou formato e dimensões conferidos (conversão).
- Em todos: contagem de `\r\n` preservada (o tipo de quebra de cada arquivo não muda), nenhum outro byte alterado, conferido de novo contra o zip de backup depois de gravar.
- `git diff --stat` deve mostrar só os arquivos previstos, com inserções = remoções nas trocas 1:1.

## 5. Teste no navegador
- Servidor local: `python -m http.server` ou o `srv.py` do scratchpad (rota `/__tema?modo=light|dark&u=/caminho` para o modo claro).
- Chrome headless (`/c/Program Files/Google/Chrome/Application/chrome.exe --headless=new`), bloqueando `pagead2.googlesyndication.com` com `--host-resolver-rules`.
- Prints antes e depois de páginas-amostra (AT, NT, Salmos e uma página de bloco), escuro e claro, a 1280 px (e 390 px se mexer em CSS); comparar pixel a pixel e explicar qualquer diferença.
- JS (busca, menu): `--dump-dom` com `?q=` e conferir os links gerados.
- URLs: testar uma amostra no disco e, se o formato depender do GitHub Pages, no ar com `curl -s -o /dev/null -w '%{http_code} %{redirect_url}'` (só leitura). URL com 301 não vai para sitemap, canonical nem hreflang.

## 6. Commits
- **`git add` em milhares de arquivos demora** (ex.: 3.168 no item 4): esperar o comando terminar e conferir `git status` antes de editar ou gravar qualquer outro arquivo.
- Separados por assunto: primeiro o script, depois o resultado do lote, e o `redesign/PLANO.md` em commit próprio.
- Mensagem em arquivo no scratchpad e `git commit -F arquivo.txt`, com números no corpo e a linha `Co-Authored-By`.
- Mostrar as mensagens e **perguntar antes de commitar**. **Sem push**, a menos que o Wagner peça; push e PR para a `main` são passos separados (skill `merge-deploy`).
- Nada no ar até PR e merge na `main`; dizer isso no relatório.

## 7. Conferência no ar (depois do deploy, só leitura)
- Só com `curl`, acrescentando `?v=<algo novo>` em cada URL para evitar cache (ex.: `curl -s "https://365gracaeadoracao.com/sitemap.xml?v=$(date +%s)"`).
- Conferir uma amostra das páginas do lote (ex.: hreflang do Salmo 23 em PT/EN/ES, canonical de Mateus 1) e os assets tocados (status 200).
- Baixar o `sitemap.xml` no ar e comparar com o do repositório (`cmp` ou SHA-256, mais contagem de `<loc>` e de URLs com `.html`); devem ser iguais.
