#!/usr/bin/env python3
"""
Renumeração dos blocos: 06b→07, 07→08, 08→09, 09→10, 10→11, 11→12, 12→13
Atualiza: links href, data-bloco, classes bloco-XX, textos visíveis de número,
          títulos e referências de caminho nos arquivos HTML.
"""
import os
import re
import glob

BASE = '/home/ubuntu/365-de-graca-e-adoracao'

# Mapeamento de substituições (ordem importa: do maior para o menor para evitar conflitos)
# Formato: (padrão_antigo, padrão_novo)
SUBSTITUICOES = [
    # Caminhos de diretório (href/src)
    ('/12-apocalipse/',          '/13-apocalipse/'),
    ('/11-cruzadas/',            '/12-conflitos-contemporaneos/'),   # não, cruzadas vira 11
    ('/10-concilios/',           '/10-concilios/'),                  # placeholder
    # Vamos fazer por número de bloco de forma mais precisa abaixo
]

# Mapeamento direto de caminhos antigos → novos
CAMINHOS = [
    ('12-apocalipse',            '13-apocalipse'),
    ('11-conflitos-contemporaneos', '12-conflitos-contemporaneos'),
    ('10-cruzadas',              '11-cruzadas'),
    ('09-concilios',             '10-concilios'),
    ('08-igreja-primitiva',      '09-igreja-primitiva'),
    ('07-novo-testamento',       '08-novo-testamento'),
    ('06-intertestamentario',    '07-intertestamentario'),
]

# Mapeamento de data-bloco e classes
BLOCOS = [
    ('data-bloco="12"',  'data-bloco="13"'),
    ('data-bloco="11"',  'data-bloco="12"'),
    ('data-bloco="10"',  'data-bloco="11"'),
    ('data-bloco="09"',  'data-bloco="10"'),
    ('data-bloco="08"',  'data-bloco="09"'),
    ('data-bloco="07"',  'data-bloco="08"'),
    ('data-bloco="06b"', 'data-bloco="07"'),
    # classes body
    ('class="bloco-12"', 'class="bloco-13"'),
    ('class="bloco-11"', 'class="bloco-12"'),
    ('class="bloco-10"', 'class="bloco-11"'),
    ('class="bloco-09"', 'class="bloco-10"'),
    ('class="bloco-08"', 'class="bloco-09"'),
    ('class="bloco-07"', 'class="bloco-08"'),
    ('class="bloco-06b"','class="bloco-07"'),
    # body class com espaço (ex: <body class="bloco-07 ...")
    ('bloco-12 ',  'bloco-13 '),
    ('bloco-11 ',  'bloco-12 '),
    ('bloco-10 ',  'bloco-11 '),
    ('bloco-09 ',  'bloco-10 '),
    ('bloco-08 ',  'bloco-09 '),
    ('bloco-07 ',  'bloco-08 '),
    ('bloco-06b ', 'bloco-07 '),
    # body class no final da string (sem espaço depois)
    ('"bloco-12"', '"bloco-13"'),
    ('"bloco-11"', '"bloco-12"'),
    ('"bloco-10"', '"bloco-11"'),
    ('"bloco-09"', '"bloco-10"'),
    ('"bloco-08"', '"bloco-09"'),
    ('"bloco-07"', '"bloco-08"'),
    ('"bloco-06b"','"bloco-07"'),
]

def processar_arquivo(fp):
    with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
        original = f.read()
    
    conteudo = original
    
    # 1. Substituir caminhos de diretório (href, src, etc.)
    for antigo, novo in CAMINHOS:
        conteudo = conteudo.replace(f'/{antigo}/', f'/{novo}/')
        conteudo = conteudo.replace(f'"{antigo}/', f'"{novo}/')
        conteudo = conteudo.replace(f"'{antigo}/", f"'{novo}/")
    
    # 2. Substituir data-bloco e classes
    for antigo, novo in BLOCOS:
        conteudo = conteudo.replace(antigo, novo)
    
    if conteudo != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        return True
    return False

# Coletar todos os arquivos HTML do projeto
todos_html = glob.glob(os.path.join(BASE, '**', '*.html'), recursive=True)
todos_html = [f for f in todos_html if '.git' not in f]

modificados = 0
for fp in sorted(todos_html):
    if processar_arquivo(fp):
        modificados += 1

print(f'✅ {modificados} arquivos HTML atualizados de {len(todos_html)} total')

# Verificar também o index.html principal
idx = os.path.join(BASE, 'index.html')
if processar_arquivo(idx):
    print('✅ index.html principal atualizado')
else:
    print('ℹ️  index.html principal — sem alterações necessárias (já atualizado)')
