#!/usr/bin/env python3
"""
Script para adicionar link 'Bíblia' no menu e corrigir cores em todas as páginas HTML
"""

import os
import re
from pathlib import Path

def fix_menu_and_colors(html_content):
    """Adiciona link Bíblia e corrige cores do menu"""
    
    # 1. Adicionar link "Bíblia" no menu se não existir
    if '<a href="/biblia">Bíblia</a>' not in html_content and '<a href="/biblia/">Bíblia</a>' not in html_content:
        # Procurar pelo menu nav e adicionar link Bíblia após Referências
        menu_pattern = r'(<a href="/sobre/fontes[^>]*>Referências</a>)'
        if re.search(menu_pattern, html_content):
            html_content = re.sub(
                menu_pattern,
                r'\1\n                <a href="/biblia/">Bíblia</a>',
                html_content
            )
    
    # 2. Corrigir cores do menu para melhor legibilidade
    # Substituir cor verde claro (#4ade80) por branco (#ffffff)
    html_content = html_content.replace('color: #4ade80', 'color: #ffffff')
    html_content = html_content.replace('color:#4ade80', 'color:#ffffff')
    
    # Adicionar CSS para links do menu se não existir
    if 'header nav a' in html_content and 'color: #ffffff' not in html_content:
        # Procurar por estilos do header nav a e atualizar
        header_nav_pattern = r'(header nav a\s*{[^}]*color:\s*)[^;]+(;[^}]*})'
        if re.search(header_nav_pattern, html_content):
            html_content = re.sub(header_nav_pattern, r'\1#ffffff\2', html_content)
    
    return html_content

def process_html_files(root_dir):
    """Processa todos os arquivos HTML no diretório"""
    count = 0
    
    # Processar arquivos HTML em todas as subpastas
    for html_file in Path(root_dir).rglob('*.html'):
        # Ignorar arquivos temporários e de backup
        if 'pasted_' in str(html_file) or '.git' in str(html_file):
            continue
            
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Aplicar correções
            new_content = fix_menu_and_colors(content)
            
            # Salvar se houver mudanças
            if new_content != content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ {html_file.relative_to(root_dir)}")
                count += 1
                
        except Exception as e:
            print(f"❌ Erro em {html_file}: {e}")
    
    return count

if __name__ == '__main__':
    root = '/home/ubuntu/365-de-graca-e-adoracao'
    
    print("🔧 Adicionando link 'Bíblia' e corrigindo cores do menu...")
    print()
    
    total = process_html_files(root)
    
    print()
    print(f"✅ Total: {total} páginas atualizadas")
