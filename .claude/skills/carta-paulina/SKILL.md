---
name: carta-paulina
description: Esqueleto da página de contexto de uma carta paulina no 365. Use quando o Wagner pedir a página de introdução/contexto de uma carta de Paulo (piloto sugerido: 1 Tessalonicenses ou Filemom).
---

# Página de contexto de carta paulina

Esta skill monta **só a estrutura**. Todo campo de conteúdo fica como marcador `[[A PREENCHER: …]]` até o Wagner fornecer ou aprovar o texto. **Não escreva texto bíblico, teológico ou histórico por conta própria** — nem datas, nem cidades, nem citações. Proponha o modelo, mostre, espere aprovação.

## Onde fica
- Uma página por carta, dentro da pasta do livro: `08-novo-testamento/<livro>/contexto.html` (ex.: `filemom/contexto.html`). Não renomeie nem mova o `index.html` existente; o índice do livro ganha um link para o contexto só depois da aprovação.
- Use o menu central (skill `menu-central`) e o visual do protótipo (`redesign/redesign.css`). Nada de CSS inline novo.
- Citações bíblicas, quando aprovadas, na ACF (skill `regras-365`).

## Classe `ficha` (lista de dados rápidos)
Não existe em outra página do site. Entra em `redesign/redesign.css` quando a primeira página for criada (na etapa dos hubs, migra para o CSS definitivo):
```css
.ficha{ display:grid; grid-template-columns:max-content 1fr; gap:10px 24px; margin:0; padding:22px 24px;
  background:var(--panel); border:1px solid var(--line); border-radius:14px; }
.ficha dt{ font-family:var(--font-mono); font-size:12px; letter-spacing:1px; text-transform:uppercase;
  color:var(--amber-glow); padding-top:2px; }
.ficha dd{ margin:0; color:var(--ink); }
@media (max-width:600px){ .ficha{ grid-template-columns:1fr; gap:4px; } .ficha dd{ margin-bottom:12px; } }
```

## Campos (nesta ordem)
| Campo | Marcador |
|---|---|
| Carta | `[[A PREENCHER: nome da carta]]` |
| Autor | `[[A PREENCHER: autor e coautores citados na saudação]]` |
| Data aproximada | `[[A PREENCHER: faixa de data e justificativa curta]]` |
| Local de escrita | `[[A PREENCHER: cidade/situação de Paulo ao escrever]]` |
| Cidade e igreja destinatária | `[[A PREENCHER: cidade, região, perfil da igreja]]` |
| Ocasião | `[[A PREENCHER: o que motivou a carta]]` |
| Relação com Atos | `[[A PREENCHER: capítulos de Atos relacionados, com links]]` |
| Tema central | `[[A PREENCHER: tema em uma frase]]` |
| Mapa | `[[A PREENCHER: imagem do mapa — origem e destino]]` |
| Personagens ligados | `[[A PREENCHER: lista; link só para páginas de personagem que existem]]` |
| Capítulos | Links para `capitulos/capitulo-NN.html` (estrutural, pode ser gerado) |

## Esqueleto HTML
```html
<main id="conteudo" class="wrap">
  <section class="page-hero">
    <span class="kicker">Carta de Paulo · Contexto</span>
    <h1>[[A PREENCHER: nome da carta]]</h1>
  </section>
  <section class="section">
    <dl class="ficha">
      <dt>Autor</dt><dd>[[A PREENCHER: …]]</dd>
      <dt>Data aproximada</dt><dd>[[A PREENCHER: …]]</dd>
      <dt>Local de escrita</dt><dd>[[A PREENCHER: …]]</dd>
      <dt>Destinatários</dt><dd>[[A PREENCHER: …]]</dd>
    </dl>
  </section>
  <section class="section"><span class="kicker">Ocasião</span><p>[[A PREENCHER: …]]</p></section>
  <section class="section"><span class="kicker">Relação com Atos</span><p>[[A PREENCHER: …]]</p></section>
  <section class="section"><span class="kicker">Tema central</span><p>[[A PREENCHER: …]]</p></section>
  <section class="section"><span class="kicker">Mapa</span><figure>[[A PREENCHER: mapa]]</figure></section>
  <section class="section"><span class="kicker">Personagens</span><ul>[[A PREENCHER: …]]</ul></section>
  <section class="section"><span class="kicker">Capítulos</span><div class="books"><!-- links gerados --></div></section>
</main>
```

## Antes de publicar
- Nenhum `[[A PREENCHER` pode restar no arquivo (`Select-String -Pattern '\[\[A PREENCHER'`).
- O Wagner aprova o conteúdo de cada carta antes do commit.
- Valide com a skill `validacao-visual`.
- Commit de conteúdo separado do commit de navegação (skill `regras-365`).
