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
- Branches: `main` (site), `redesign/navegacao-awexpress` (trabalho), `(root)` (linha antiga de backups automáticos, ainda a branch padrão).

## Atenção: configuração antiga do Pages
Em 07/10/2026 o site no ar era a `main` (`ec2c3181`, deploy de 24/08), mas o Pages ainda estava em **"Deploy from a branch → `(root)`" (legacy)**. Um push na `(root)` reconstruiria o site com o conteúdo antigo dela. Antes do merge, o Wagner troca em Settings:
1. Pages → Source: **"GitHub Actions"**.
2. General → Default branch: `(root)` → **`main`**.
Nenhuma das duas muda o que está no ar na hora; só o próximo deploy da `main` muda.

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

## Reversão
- Pelo GitHub: PR mesclado → "Revert" → mesclar o PR de reversão na `main`.
- Pela linha de comando (com ordem do Wagner): `git checkout main && git pull`, `git revert -m 1 <sha do merge>`, `git push origin main`.
- Nunca `git push --force` na `main` nem deploy manual de outra branch.
- Os zips de `_backups/` (só locais) guardam cada página como estava antes de cada etapa.
