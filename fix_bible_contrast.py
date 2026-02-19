#!/usr/bin/env python3
"""
Script para corrigir contraste e legibilidade das páginas da Bíblia
"""

import os
import re
from pathlib import Path

def fix_bible_page_css(file_path):
    """Corrige CSS de uma página da Bíblia para melhor legibilidade"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # CSS melhorado para legibilidade
    new_css = """
    <style>
        body {
            background-color: #0a0e1a !important;
            color: #e8e8e8 !important;
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.8;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }
        
        h1 {
            color: #4a90e2 !important;
            text-align: center;
            margin-bottom: 10px;
        }
        
        .version {
            text-align: center;
            color: #a0a0a0 !important;
            font-size: 0.9em;
            margin-bottom: 30px;
        }
        
        .verse {
            margin-bottom: 15px;
            padding-left: 40px;
            text-indent: -40px;
        }
        
        .verse-number {
            color: #4a90e2 !important;
            font-weight: bold;
            margin-right: 8px;
            font-size: 0.9em;
        }
        
        .verse-text {
            color: #e8e8e8 !important;
        }
        
        .navigation {
            display: flex;
            justify-content: space-between;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #2a3f5f;
        }
        
        .navigation a {
            color: #5dade2 !important;
            text-decoration: none;
            padding: 10px 20px;
            border: 1px solid #5dade2;
            border-radius: 5px;
            transition: all 0.3s;
        }
        
        .navigation a:hover {
            background-color: #5dade2;
            color: #0a0e1a !important;
        }
        
        hr {
            border: none;
            border-top: 1px solid #2a3f5f;
            margin: 30px 0;
        }
    </style>
    """
    
    # Remove CSS antigo se existir
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    
    # Adiciona novo CSS antes do </head>
    if '</head>' in content:
        content = content.replace('</head>', f'{new_css}\n</head>')
    else:
        # Se não tiver </head>, adiciona após <head>
        content = content.replace('<head>', f'<head>\n{new_css}')
    
    # Salva arquivo atualizado
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Processa todas as páginas da Bíblia"""
    
    bible_dir = Path('/home/ubuntu/365-de-graca-e-adoracao/biblia')
    
    if not bible_dir.exists():
        print(f"❌ Diretório não encontrado: {bible_dir}")
        return
    
    # Encontra todos os arquivos HTML
    html_files = list(bible_dir.rglob('*.html'))
    
    print(f"📚 Encontrados {len(html_files)} arquivos HTML da Bíblia")
    print("🔧 Corrigindo CSS para melhor legibilidade...")
    
    success_count = 0
    
    for html_file in html_files:
        try:
            fix_bible_page_css(html_file)
            success_count += 1
            if success_count % 100 == 0:
                print(f"   ✅ {success_count}/{len(html_files)} arquivos processados...")
        except Exception as e:
            print(f"   ❌ Erro em {html_file}: {e}")
    
    print(f"\n✅ Concluído! {success_count}/{len(html_files)} páginas atualizadas com sucesso!")

if __name__ == '__main__':
    main()
