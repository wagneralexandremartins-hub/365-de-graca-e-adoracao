---
name: seo-limpeza
description: Etapa de SEO e limpeza do 365 — sitemap, canonical, hreflang, imagens de compartilhamento, favicon, links quebrados antigos, páginas ralas ou publicadas por engano e ajustes de CSS pendentes. Use quando o Wagner pedir para tratar itens da "Limpeza prioritária" do redesign/PLANO.md ou fazer varredura de links.
---

# SEO e limpeza

## Regras fixas do projeto
- Nunca alterar texto editorial (estudos, exegese, versículos, títulos) sem autorização explícita do Wagner.
- Trabalhar só em branch; nunca na `main`. Perguntar antes de cada commit e de cada push. Nada de merge na `main` sem ordem explícita.
- Site 100% estático (HTML, CSS e JS puros), mudanças incrementais, preservar todas as URLs (não apagar nem mover páginas sem ordem).
- Responder em português do Brasil.

## Fonte da verdade
A lista atualizada fica em `redesign/PLANO.md`, seção "Limpeza prioritária". **Nada ali é alterado sem decisão do Wagner**, um item (ou grupo de itens iguais) por etapa. Itens registrados até 07/10/2026:
- ~~Imagens de compartilhamento (`og-cover.jpg`, `og-image.jpg`)~~ e ~~`assets/img/favicon.png`~~: resolvidos em 08/10 (commit `5716d119`).
- ~~Canonical do hub do NT diferente do `sitemap.xml`~~: resolvido em 08/10 com o sitemap alinhado ao canonical (commit `07cee8bc`).
- `sitemap.xml`: `lastmod` antigos e cabeçalho "Total de páginas" desatualizado (4.152 URLs desde 07/10).
- Páginas ralas com AdSense (`genesis/genesis-12.html` a `-50`), `busca/index_backup.html` publicada, `pasted_content.html`, 5 `pasted_file_*_image.html` com bytes nulos, fragmentos `timeline-*.html` na raiz.
- Rolagem horizontal a 390px em `06-apocrifos/` (6px) e `busca/` (31px, grade `.indice-item`), iguais na `main`: corrigir por CSS.
- `/estudos/` sem botão de modo claro; modo claro de Rute e Josué; faixa de números dos livros `main.wrap`.
- Textos para decisão do Wagner (não alterar sozinho): "1.627+ Páginas no projeto" na busca × "+2.900" na home; "compatíveis com Vercel" no rodapé dos estudos.
- Fase 2: índice de busca do `assets/js/nav.js` com `1-corintios` × pasta `1corintios` (e livros numerados semelhantes).

## Decisões de 08/10/2026
Todo lote segue a skill `lote-seguro`.
- **Formato oficial das URLs: sem `.html`** (decisão provisória do Wagner), como os canonicals atuais: capítulos PT sem extensão (`.../capitulo-01`), pastas com barra (`/en/genesis/`). As URLs antigas com `.html` continuam no ar (200); nada é apagado nem redirecionado.
- **Sitemap alinhado ao canonical** (commit `07cee8bc`, script `scripts/sitemap_canonical.py`): cada `<loc>` usa exatamente o canonical lido do próprio arquivo, só quando há um canonical único, do domínio, sem `.html`, que resolve para a mesma página e não é pasta sem barra. 4.034 de 4.152 trocados; `lastmod`, `priority`, ordem e CRLF intactos. Para rodar de novo depois de mudar canonicals: simulação, OK, `--apply`.
- ~~**Canonical de Mateus**~~: resolvido em 08/10 (commits `df0235e6` script `scripts/canonical_mateus.py`, `443900a1` 28 páginas; sitemap alinhado em `da33334b`).
- ~~**Regra do hreflang** (item 4)~~: aplicado em 08/10 (commits `9da75802` script `scripts/hreflang_item4.py`, `e7158fff` 3.168 arquivos): H1 1.843 hrefs corrigidos, H2 164 alternates pt-BR removidos, H3 1.168 páginas PT com pt-BR/en/es. A regra continua valendo: só entre páginas que existem, sem redirect, realmente equivalentes (mesmo livro e capítulo/bloco), com a URL **igual ao canonical do alvo** e **recíprocas** (PT ↔ EN ↔ ES, cada uma declara as outras e a si mesma). Na dúvida, remover em vez de chutar.
- **GitHub Pages:** `/pasta` sem barra final responde **301** para `/pasta/`. Esse formato não vai para sitemap, canonical nem hreflang.

### Pendências (decisão do Wagner; não corrigir sozinho)
- **55 páginas sem canonical:** 27 EN `*-block-N`, 27 ES `*-bloque-N` e `03-historicos/1samuel/capitulos/capitulo-29.html`. No sitemap seguem com `.html`.
- **`/pasta/index` em 299 índices PT:** é o canonical atual (200 no ar), mas atípico; o limpo seria `/pasta/`, o que exige editar o canonical das páginas. **Se `/pasta/index` mudar, rodar de novo `scripts/sitemap_canonical.py` e `scripts/hreflang_item4.py`** (simulação, OK, `--apply`).
- **29 páginas de `estudos/`** com canonical `.../index.html` e **4 com canonical de pasta sem barra** (`autismo-e-fe`, `como-estudar-a-biblia`, `ebook-4-passos`, `loja-365`; 301 no ar). Somadas aos 55, são os **88 URLs que ficaram com `.html`** no sitemap.
- **Gênesis EN/ES sem pt-BR:** as 100 páginas `en/genesis-1` a `50` e `es/genesis-1` a `50` perderam o hreflang pt-BR (H2), porque o PT de Gênesis só tem páginas por bloco (`02-pentateuco/genesis/bloco-01` a `06`). Opções: criar páginas PT por capítulo, apontar para o bloco (não é 1:1, a regra não permite) ou deixar sem pt-BR.
- **hreflang de `estudos/` e home:** fora do item 4, não editados: 31 pt-BR com canonical `.html` e 64 sem reciprocidade com `en/estudos` e `es/estudios`.

## Rotina do Search Console
- Domínio verificado por TXT na Hostinger: **manter os dois registros TXT**.
- **Depois de cada merge de SEO na `main`**, reenviar `https://365gracaeadoracao.com/sitemap.xml` (último envio: 08/10/2026).
- Remover a linha antiga com defeito `sitemap.xml.` (com ponto no fim, de 23/02/2026).
- Ler Indexação > Páginas e classificar os motivos de não indexação (linha de base de 08/10: 3.693 indexadas, 9.319 não indexadas). Só leitura; correções viram itens desta skill.

## Varredura de links (como foi feita no bloco B)
- Escopo: todas as `*.html` fora de `en/`, `es/`, `_backups/`, `redesign/`, `scripts/`, `.claude/`, `.github/`, sem as páginas de redirecionamento (`http-equiv="refresh"`).
- Links: `a[href]`, `img/script/iframe/source[src]`, `link[rel=stylesheet|icon|apple-touch-icon]`, `form[action]`; URLs absolutas do próprio domínio contam como internas.
- Regras do GitHub Pages: pasta com `index.html` responde; `/pasta` sem barra redireciona; endereço sem extensão serve o `.html`. Tudo o que o `pages.yml` exclui conta como 404.
- Compare com a `main` extraída por `git archive <sha> | tar -x` (só leitura) e reporte só os pares página → destino **novos**. Em 07/10: 1.325 pares quebrados antigos (1.196 são `/styles.css`), 0 novos.
- Confira também os links gerados por JS: itens do `MENU` e a trilha de 260 capítulos do `site-nav.js`, e o botão do `header-cta.js`.

## Procedimento por item
1. Levante o escopo (quantas páginas, quais) e mostre em dry-run, com prova de que só a linha/trecho previsto muda (byte a byte, quebras de linha preservadas).
2. **Espere o OK do Wagner.** Para trocas em lote, backup zip em `_backups/` (nunca em commit).
3. Aplique, valide (links e, se mexer em CSS, rolagem horizontal em 1280/768/390/360, escuro e claro) e mostre o relatório.
4. Commit separado por assunto, mensagem por arquivo, sem push. Atualize o item no `PLANO.md` em commit próprio.
