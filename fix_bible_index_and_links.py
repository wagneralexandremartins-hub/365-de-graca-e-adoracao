#!/usr/bin/env python3
"""
Script para:
1. Corrigir links da Bíblia no menu de todas as páginas
2. Escurecer e melhorar contraste da página índice da Bíblia
"""

import os
import re
from pathlib import Path

def fix_bible_links_in_file(filepath):
    """Corrige links duplicados e vazios da Bíblia no menu"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Remove link duplicado da Bíblia
        # Procura por dois links consecutivos da Bíblia e remove o segundo
        content = re.sub(
            r'(<li><a href="/biblia/">Bíblia</a></li>)\s*<li><a href="/biblia/index\.html">Bíblia</a></li>',
            r'\1',
            content
        )
        
        # Corrige links vazios da Bíblia
        content = re.sub(
            r'<a href="">Bíblia</a>',
            r'<a href="/biblia/">Bíblia</a>',
            content
        )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"   ⚠️  Erro em {filepath}: {e}")
        return False

def fix_bible_index_css():
    """Escurece e melhora contraste da página índice da Bíblia"""
    filepath = '/home/ubuntu/365-de-graca-e-adoracao/biblia/index.html'
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Adiciona CSS para fundo azul escuro e melhor contraste
        new_css = '''    <style>
        /* FUNDO AZUL ESCURO CONSISTENTE */
        body {
            background: #0a0e1a !important;
            color: #e8e8e8 !important;
        }
        
        .bible-index {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 2rem;
            background: #0a0e1a;
        }
        .bible-header {
            text-align: center;
            margin-bottom: 3rem;
        }
        .bible-title {
            font-size: 2.5rem;
            color: #4a90e2;
            margin-bottom: 0.5rem;
        }
        .bible-subtitle {
            font-size: 1.2rem;
            color: #b0b0b0;
        }
        .testament {
            margin-bottom: 3rem;
        }
        .testament-title {
            font-size: 1.8rem;
            color: #4a90e2;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #4a90e2;
        }
        .category-title {
            font-size: 1.3rem;
            color: #5dade2;
            margin: 2rem 0 1rem 0;
        }
        .book-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }
        .book-card {
            background: #141824;
            border: 1px solid #2a3f5f;
            border-radius: 8px;
            padding: 1.5rem;
            transition: all 0.3s;
        }
        .book-card:hover {
            border-color: #4a90e2;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(74, 144, 226, 0.3);
            background: #1a2332;
        }
        .book-name {
            font-size: 1.2rem;
            color: #4a90e2;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        .book-chapters {
            color: #a0a0a0;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        .chapter-links {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .chapter-link {
            display: inline-block;
            padding: 0.3rem 0.6rem;
            background: #1a2332;
            color: #e0e0e0;
            text-decoration: none;
            border-radius: 4px;
            font-size: 0.85rem;
            transition: all 0.2s;
            border: 1px solid #2a3f5f;
        }
        .chapter-link:hover {
            background: #4a90e2;
            color: white;
            border-color: #4a90e2;
        }
    </style>'''
        
        # Substitui o bloco <style> existente
        content = re.sub(
            r'<style>.*?</style>',
            new_css,
            content,
            flags=re.DOTALL
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Página índice da Bíblia atualizada com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao atualizar índice da Bíblia: {e}")
        return False

def main():
    base_dir = Path('/home/ubuntu/365-de-graca-e-adoracao')
    
    print("🔧 Corrigindo links da Bíblia no menu...")
    
    # Encontra todos os arquivos HTML
    html_files = list(base_dir.rglob('*.html'))
    print(f"📚 Encontrados {len(html_files)} arquivos HTML")
    
    fixed_count = 0
    for i, filepath in enumerate(html_files, 1):
        if fix_bible_links_in_file(filepath):
            fixed_count += 1
        
        if i % 100 == 0:
            print(f"   ✅ {i}/{len(html_files)} arquivos processados...")
    
    print(f"✅ {fixed_count} arquivos com links corrigidos!")
    
    print("\n🎨 Atualizando CSS da página índice da Bíblia...")
    fix_bible_index_css()
    
    print("\n✅ Concluído! Todas as correções aplicadas.")

if __name__ == '__main__':
    main()
