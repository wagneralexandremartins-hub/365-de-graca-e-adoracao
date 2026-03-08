#!/usr/bin/env python3
"""
Corrige todos os links quebrados (404) encontrados no projeto.
Categorias:
  1. Links com hífen onde o diretório não tem (1-samuel -> 1samuel, etc.)
  2. Link antigo /07-novo-testamento -> /08-novo-testamento
  3. Links para sub-páginas inexistentes no Bloco 09 -> redireciona para index.html do módulo
"""

import os
import re

PROJECT_DIR = '/home/ubuntu/365-de-graca-e-adoracao'

# Mapa de substituições de href: (padrão_antigo, novo_valor)
# Ordem importa: mais específicos primeiro
REPLACEMENTS = [
    # === Bloco 03 — Históricos: remover hífen nos nomes de livros ===
    ('href="/03-historicos/1-samuel/', 'href="/03-historicos/1samuel/'),
    ('href="/03-historicos/2-samuel/', 'href="/03-historicos/2samuel/'),
    ('href="/03-historicos/1-reis/', 'href="/03-historicos/1reis/'),
    ('href="/03-historicos/2-reis/', 'href="/03-historicos/2reis/'),
    ('href="/03-historicos/1-cronicas/', 'href="/03-historicos/1cronicas/'),
    ('href="/03-historicos/2-cronicas/', 'href="/03-historicos/2cronicas/'),
    
    # === Bloco 04 — Poéticos: cantico -> canticos ===
    ('href="/04-poeticos/cantico/', 'href="/04-poeticos/canticos/'),
    
    # === Bloco 05 — Profetas: miqueas -> miqueias ===
    ('href="/05-profetas/miqueas/', 'href="/05-profetas/miqueias/'),
    
    # === Bloco 08 — NT: remover hífen nos nomes de livros ===
    ('href="/08-novo-testamento/1-corintios/', 'href="/08-novo-testamento/1corintios/'),
    ('href="/08-novo-testamento/2-corintios/', 'href="/08-novo-testamento/2corintios/'),
    ('href="/08-novo-testamento/1-joao/', 'href="/08-novo-testamento/1joao/'),
    ('href="/08-novo-testamento/2-joao/', 'href="/08-novo-testamento/2joao/'),
    ('href="/08-novo-testamento/3-joao/', 'href="/08-novo-testamento/3joao/'),
    ('href="/08-novo-testamento/1-pedro/', 'href="/08-novo-testamento/1pedro/'),
    ('href="/08-novo-testamento/2-pedro/', 'href="/08-novo-testamento/2pedro/'),
    ('href="/08-novo-testamento/1-tessalonicenses/', 'href="/08-novo-testamento/1tessalonicenses/'),
    ('href="/08-novo-testamento/2-tessalonicenses/', 'href="/08-novo-testamento/2tessalonicenses/'),
    ('href="/08-novo-testamento/1-timoteo/', 'href="/08-novo-testamento/1timoteo/'),
    ('href="/08-novo-testamento/2-timoteo/', 'href="/08-novo-testamento/2timoteo/'),
    ('href="/08-novo-testamento/filemon/', 'href="/08-novo-testamento/filemom/'),
    
    # === Link antigo do NT (antes da renumeração) ===
    ('href="/07-novo-testamento"', 'href="/08-novo-testamento"'),
    ('href="/07-novo-testamento/', 'href="/08-novo-testamento/'),
    
    # === Bloco 09 — Igreja Primitiva: sub-páginas inexistentes -> index.html do módulo ===
    ('href="/09-igreja-primitiva/pentecostes/comunidade-primitiva.html"', 'href="/09-igreja-primitiva/pentecostes/index.html"'),
    ('href="/09-igreja-primitiva/pentecostes/estefano.html"', 'href="/09-igreja-primitiva/pentecostes/index.html"'),
    ('href="/09-igreja-primitiva/perseguicoes/nero.html"', 'href="/09-igreja-primitiva/perseguicoes/index.html"'),
    ('href="/09-igreja-primitiva/perseguicoes/domiciano.html"', 'href="/09-igreja-primitiva/perseguicoes/index.html"'),
    ('href="/09-igreja-primitiva/perseguicoes/dioclesiano.html"', 'href="/09-igreja-primitiva/perseguicoes/index.html"'),
    ('href="/09-igreja-primitiva/martires/policarpo.html"', 'href="/09-igreja-primitiva/martires/index.html"'),
    ('href="/09-igreja-primitiva/martires/perpetua.html"', 'href="/09-igreja-primitiva/martires/index.html"'),
    ('href="/09-igreja-primitiva/martires/inacio.html"', 'href="/09-igreja-primitiva/martires/index.html"'),
    ('href="/09-igreja-primitiva/pais-da-igreja/agostinho.html"', 'href="/09-igreja-primitiva/pais-da-igreja/index.html"'),
    ('href="/09-igreja-primitiva/pais-da-igreja/atanasio.html"', 'href="/09-igreja-primitiva/pais-da-igreja/index.html"'),
    ('href="/09-igreja-primitiva/pais-da-igreja/crisostomo.html"', 'href="/09-igreja-primitiva/pais-da-igreja/index.html"'),
    ('href="/09-igreja-primitiva/expansao-missionaria/antioqua.html"', 'href="/09-igreja-primitiva/expansao-missionaria/index.html"'),
    ('href="/09-igreja-primitiva/expansao-missionaria/roma.html"', 'href="/09-igreja-primitiva/expansao-missionaria/index.html"'),
    ('href="/09-igreja-primitiva/heresias-e-concilios/niceia.html"', 'href="/09-igreja-primitiva/heresias-e-concilios/index.html"'),
    ('href="/09-igreja-primitiva/heresias-e-concilios/calcedonia.html"', 'href="/09-igreja-primitiva/heresias-e-concilios/index.html"'),
    ('href="/09-igreja-primitiva/vida-comunitaria/agape.html"', 'href="/09-igreja-primitiva/vida-comunitaria/index.html"'),
    ('href="/09-igreja-primitiva/vida-comunitaria/batismo.html"', 'href="/09-igreja-primitiva/vida-comunitaria/index.html"'),
    
    # === Links para páginas de topo sem .html ===
    ('href="/referencias.html"', 'href="/referencias/"'),
    ('href="/sobre.html"', 'href="/sobre/index.html"'),
]

# Contar arquivos modificados
files_modified = 0
replacements_total = 0

for root, dirs, files in os.walk(PROJECT_DIR):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__']]
    
    for fname in files:
        if not fname.endswith('.html'):
            continue
        
        full_path = os.path.join(root, fname)
        
        try:
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            original = content
            count = 0
            
            for old, new in REPLACEMENTS:
                if old in content:
                    content = content.replace(old, new)
                    count += content.count(new) - original.count(new) if new in original else content.count(new)
            
            if content != original:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                files_modified += 1
                replacements_total += 1
                rel = full_path.replace(PROJECT_DIR, '')
                print(f'  Corrigido: {rel}')
        
        except Exception as e:
            print(f'  ERRO em {full_path}: {e}')

print(f'\nTotal de arquivos corrigidos: {files_modified}')
print(f'Script concluído!')
