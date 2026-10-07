---
name: regras-365
description: Regras invioláveis de trabalho no repositório do 365 Graça & Adoração. Use antes de qualquer alteração no site — edição de páginas, scripts, CSS/JS, commits, push ou deploy.
---

# Regras do projeto 365 Graça & Adoração

Valem para qualquer tarefa neste repositório. Em caso de dúvida, pergunte ao Wagner antes de agir.

## Conteúdo
- **Nunca altere texto editorial** (estudos, exegese, comentários, versículos, títulos de capítulos, notas) sem autorização explícita do Wagner. O conteúdo foi desenvolvido no ChatGPT e é responsabilidade editorial dele. Mexa só em estrutura, navegação e visual.
- Se uma mudança técnica deixar um texto incoerente (ex.: "os livros abaixo" sem livros abaixo), não corrija o texto: aponte e pergunte.
- Quando um conteúdo editorial aprovado citar dados de saúde ou população, use fontes oficiais (OMS, Ministério da Saúde, IBGE).
- Tradução bíblica padrão em português: **ACF (Almeida Corrigida Fiel)**, a mesma do texto em `biblia/`. Conteúdo novo usa ACF. Páginas existentes que citam outra tradução (NVI em parte do Pentateuco, ARA em poucas páginas, NT sem tradução declarada) não são alteradas sem ordem do Wagner.
- Rótulos de navegação novos (botões, títulos de seção da interface) também passam pela aprovação do Wagner antes de serem gravados.

## Git
- Trabalhe sempre numa branch, nunca na `main`.
- **Pergunte antes de cada commit e de cada push.** Nunca faça merge na `main` sem ordem explícita.
- Mensagens de commit sempre por arquivo: escreva a mensagem num `.txt` e rode `git commit -F arquivo.txt`. No PowerShell, passar a mensagem como argumento quebra o comando (o texto vira nome de arquivo).
- Separe commits de navegação/estrutura dos commits de conteúdo. Um assunto por commit.
- Confira o stage antes de commitar (`git diff --cached --name-only`): nenhum `.zip`, nada de `_backups/`, nada fora do escopo da etapa.

## Técnica
- Site 100% estático: HTML, CSS e JS puros. Nada de frameworks, bundlers ou build tools novos.
- Mudanças incrementais. Nunca reconstruir o site do zero.
- Preserve todas as URLs e páginas existentes. Não apague nem mova páginas; o que sai da navegação continua acessível. Redirecionamentos existentes (`http-equiv="refresh"`) ficam como estão.
- Preserve o tipo de quebra de linha de cada arquivo (muitos são CRLF).
- Hospedagem: GitHub Pages via `.github/workflows/pages.yml` (deploy a cada push na `main`). Não usar Vercel.

## Procedimento por etapa
1. Defina o escopo e liste as pastas e quantas páginas entram.
2. Rode em **dry-run** e mostre o resultado (páginas alteradas, puladas e motivo, falhas).
3. **Espere a confirmação do Wagner** antes de aplicar.
4. Aplique, valide (ver skill `validacao-visual`) e mostre o relatório.
5. Pergunte se pode commitar.

## Comunicação
- Responda em português do Brasil, de forma direta. Evite listas excessivas; prefira frases curtas e uma tabela quando houver números.
- Relate falhas com franqueza: o que deu errado, o que foi descartado, o que ficou pendente.
