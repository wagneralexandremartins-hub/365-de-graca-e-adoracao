#!/usr/bin/env python3
"""
Corrige o trecho problemático do style.css — reescreve as linhas 609-635
com os seletores corretos para os blocos 10, 11, 12 e 13.
"""
import re

path = '/home/ubuntu/365-de-graca-e-adoracao/assets/css/style.css'

with open(path, 'r', encoding='utf-8') as f:
    linhas = f.readlines()

# Encontrar a linha do comentário "/* Bloco 10–11: Violeta */"
inicio = None
fim = None
for i, linha in enumerate(linhas):
    if '/* Bloco 10' in linha and 'Violeta' in linha:
        inicio = i
    if inicio and i > inicio and linha.strip().startswith('/*') and 'Bloco 1' in linha:
        # Próximo bloco — parar aqui
        fim = i
        break

if inicio is None:
    print('❌ Não encontrou o início do bloco 10')
    exit(1)

print(f'Início encontrado na linha {inicio+1}: {linhas[inicio].rstrip()}')
if fim:
    print(f'Fim encontrado na linha {fim+1}: {linhas[fim].rstrip()}')
else:
    # Procurar o fim pelo último seletor do bloco 13
    for i in range(inicio, len(linhas)):
        if '.card[data-bloco="13"]:hover' in linhas[i] and 'rgba(124' in linhas[i]:
            fim = i + 2  # +1 para a linha do }, +1 para a próxima
            break
    print(f'Fim calculado na linha {fim+1}')

# Novo conteúdo correto para os blocos 10-13
novo_trecho = '''/* Bloco 10–11: Violeta (Concílios + Cruzadas) */
.card[data-bloco="10"] .block-number,
.card[data-bloco="11"] .block-number { color: #8b5cf6; opacity: 0.6; }
.card[data-bloco="10"] .poster,
.card[data-bloco="11"] .poster {
  background: linear-gradient(135deg, #060010 0%, #0d0020 100%);
  border-bottom: 1px solid rgba(139,92,246,0.18);
}
.card[data-bloco="10"]:hover,
.card[data-bloco="11"]:hover { border-color: rgba(139,92,246,0.40); }
/* Bloco 12: Rubi (Conflitos Contemporâneos) */
.card[data-bloco="12"] .block-number { color: #e11d48; opacity: 0.6; }
.card[data-bloco="12"] .poster {
  background: linear-gradient(135deg, #0f0005 0%, #1a000a 100%);
  border-bottom: 1px solid rgba(225,29,72,0.18);
}
.card[data-bloco="12"]:hover { border-color: rgba(225,29,72,0.40); }
/* Bloco 13: Violeta Escuro (Apocalipse) */
.card[data-bloco="13"] .block-number { color: #7c3aed; opacity: 0.6; }
.card[data-bloco="13"] .poster {
  background: linear-gradient(135deg, #04001a 0%, #0a0030 100%);
  border-bottom: 1px solid rgba(124,58,237,0.18);
}
.card[data-bloco="13"]:hover { border-color: rgba(124,58,237,0.40); }
'''

# Substituir as linhas do trecho antigo pelo novo
novas_linhas = linhas[:inicio] + [novo_trecho] + linhas[fim:]

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(novas_linhas)

print(f'✅ style.css corrigido: substituídas linhas {inicio+1} a {fim}')

# Verificar resultado
with open(path, 'r', encoding='utf-8') as f:
    resultado = f.read()

# Confirmar que não há mais referências erradas
problemas = []
if 'data-bloco="06b"' in resultado:
    problemas.append('ainda tem 06b')
if '.card[data-bloco="11"] .block-number { color: #8b5cf6' not in resultado:
    problemas.append('bloco 11 violeta não encontrado')
if '.card[data-bloco="12"] .block-number { color: #e11d48' not in resultado:
    problemas.append('bloco 12 rubi não encontrado')
if '.card[data-bloco="13"] .block-number { color: #7c3aed' not in resultado:
    problemas.append('bloco 13 violeta escuro não encontrado')

if problemas:
    print(f'⚠️  Problemas encontrados: {", ".join(problemas)}')
else:
    print('✅ Todos os seletores estão corretos!')
