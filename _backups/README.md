# Backups — 365 Graça e Adoração

Esta pasta contém backups dos arquivos principais do site para restauração em caso de emergência.

## Arquivos

| Arquivo | Data | Descrição |
|---|---|---|
| `index.html.backup-2026-04-09` | 09/04/2026 | Página inicial original — 505 linhas, versão estável com nav de 13 blocos, seção de estudos e hero completo |

## Como restaurar

Para restaurar o `index.html` da raiz a partir de um backup:

```bash
cp _backups/index.html.backup-2026-04-09 index.html
git add index.html
git commit -m "fix: restaurar index.html a partir do backup"
git push origin main
```

## Importante

- Nunca aplique diffs completos que substituam o arquivo inteiro
- Sempre aplique apenas as alterações específicas (linhas adicionadas/removidas)
- Em caso de dúvida, compare com o backup antes de fazer push
