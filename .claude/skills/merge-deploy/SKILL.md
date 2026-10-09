---
name: merge-deploy
description: Merge da branch do redesign na main e deploy do 365 no GitHub Pages, com conferência do que está no ar e plano de reversão. Use quando o Wagner falar em PR, merge, publicar, deploy, Settings do GitHub ou "o que está no ar".
---

# Merge e deploy

## Regras fixas do projeto
- Nunca alterar texto editorial (estudos, exegese, versículos, títulos) sem autorização explícita do Wagner.
- Trabalhar só em branch; nunca na `main`. Perguntar antes de cada commit e de cada push. **Nada de merge na `main` sem ordem explícita do Wagner.**
- Site 100% estático (HTML, CSS e JS puros), mudanças incrementais, preservar todas as URLs.
- Responder em português do Brasil.

## Como o site é publicado
- `.github/workflows/pages.yml`: deploy a cada push na `main` (ou manual). Monta `_site` com `rsync`, excluindo `_backups/`, `scripts/`, `.github/`, `.claude/`, `redesign/`, `*.md`, `*.py` e arquivos de build antigos; gera `.nojekyll` e `CNAME`.
- O ambiente `github-pages` só aceita deploy da `main`. Push em outra branch não publica nada.
- Branches: `main` (site), `redesign/navegacao-awexpress` (trabalho), a antiga `(root)` (linha de backups automáticos, hoje exibida como `(main)`, `501c8730`; renomear ou apagar depende do Wagner). Branch padrão: `main`.

## Configuração do Pages (resolvida em 07/10/2026)
Até 07/10 o Pages estava em "Deploy from a branch → `(root)`" (legacy), e a `(root)` era a branch padrão. O Wagner trocou em Settings, antes do PR #1:
1. Pages → Source: **"GitHub Actions"**.
2. General → Default branch: **`main`**.
Hoje só o workflow publica, a partir da `main`. Se essas configurações voltarem ao estado antigo, parar e avisar o Wagner antes de qualquer merge.

## Conferir o que está no ar (só leitura)
- `gh api repos/<dono>/<repo>/pages` (build_type, source), `.../pages/builds` (builds legacy) e `.../deployments?environment=github-pages` (deploys pelo workflow, com sha e data).
- Baixe algumas páginas do site e compare com `git hash-object --path=<arquivo>` contra `git rev-parse <branch>:<arquivo>` de cada branch.

## Checklist (seções C, D e E do `redesign/PLANO.md`)
1. Bloco B feito (links, amostra visual, git limpo, `redesign/` fora do deploy).
2. Wagner confirma as duas trocas de Settings.
3. Tag do estado atual da `main`: `git tag pre-redesign <sha da main>` e push da tag — com OK.
4. Push da branch e PR **para a `main`** (o GitHub sugere `(root)` enquanto ela for padrão: trocar). Corpo do PR com o resumo de commits e arquivos para o Wagner revisar.
5. Merge com **merge commit** (não squash), só com ordem explícita.
6. Acompanhar o workflow "Deploy GitHub Pages" até "success".
7. Depois do deploy: abrir home, hubs AT/NT, um capítulo do NT e um do AT, Bíblia, Estudos, no desktop e no celular, escuro e claro; testar "Continue de onde parou"; conferir `/antigo-testamento/` e o canonical. Nos dias seguintes: Search Console e AdSense.

## Exemplos
- **PR #1** (redesign): merge commit `6101ab89` em 07/10/2026 (pais `ec2c3181` + `d721e79f`); tag `pre-redesign` = `ec2c3181`.
- **PR #2** (SEO técnico): merge commit `7ce48cd2` em 08/10/2026 (pais `6101ab89` + `8e3df475`; 20 commits, 4.379 arquivos). Workflow run `37843120886`, build e deploy success às 20:56 UTC. Conferido no ar com `curl` (skill `lote-seguro`, seção 7); sitemap reenviado no Search Console. Reversão, só com ordem do Wagner: `git revert -m 1 7ce48cd2`.

## Reversão
- Pelo GitHub: PR mesclado → "Revert" → mesclar o PR de reversão na `main`.
- Pela linha de comando (com ordem do Wagner): `git checkout main && git pull`, `git revert -m 1 <sha do merge>`, `git push origin main`.
- Nunca `git push --force` na `main` nem deploy manual de outra branch.
- Os zips de `_backups/` (só locais) guardam cada página como estava antes de cada etapa.
