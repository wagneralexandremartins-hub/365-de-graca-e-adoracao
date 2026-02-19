#!/usr/bin/env python3
"""
Script para adicionar CSS de legibilidade em todas as páginas
"""
import os
import re
from pathlib import Path

BASE_DIR = Path("/home/ubuntu/365-de-graca-e-adoracao")

# CSS adicional para legibilidade (não remove o existente)
LEGIBILITY_CSS = """
  /* === CORREÇÕES DE LEGIBILIDADE === */
  body {
    background: #0a0e1a !important;
    color: #e8e8e8 !important;
  }
  
  p, li, td, div {
    color: #e8e8e8 !important;
  }
  
  h1, h2, h3, h4, h5, h6 {
    color: #5dade2 !important;
  }
  
  a {
    color: #5dade2 !important;
  }
  
  a:hover {
    color: #7ec8f3 !important;
  }
  
  blockquote {
    background: #1a2332 !important;
    color: #d0d0d0 !important;
    border-left: 4px solid #4a90e2;
  }
  
  .container, .wrap, main, article {
    background: #0a0e1a !important;
  }
"""

def add_legibility_css(file_path):
    """Adiciona CSS de legibilidade ao arquivo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verifica se já tem o CSS de legibilidade
        if "CORREÇÕES DE LEGIBILIDADE" in content:
            return False
        
        # Adiciona antes do </head>
        if '</head>' in content:
            content = content.replace('</head>', f'<style>{LEGIBILITY_CSS}</style>\n</head>')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    except Exception as e:
        print(f"Erro em {file_path}: {e}")
        return False

def main():
    """Processa todas as páginas"""
    count = 0
    
    # Gênesis
    genesis_dir = BASE_DIR / "02-pentateuco" / "genesis" / "estudos"
    if genesis_dir.exists():
        for html_file in genesis_dir.glob("*.html"):
            if add_legibility_css(html_file):
                count += 1
                print(f"✅ {html_file.name}")
    
    # Êxodo
    exodo_dir = BASE_DIR / "02-pentateuco" / "exodo"
    if exodo_dir.exists():
        index_file = exodo_dir / "index.html"
        if index_file.exists() and add_legibility_css(index_file):
            count += 1
            print(f"✅ exodo/index.html")
        
        for i in range(1, 7):
            bloco_dir = exodo_dir / f"bloco-{i:02d}"
            if bloco_dir.exists():
                index_file = bloco_dir / "index.html"
                if index_file.exists() and add_legibility_css(index_file):
                    count += 1
                    print(f"✅ bloco-{i:02d}/index.html")
    
    print(f"\n✅ Total: {count} páginas corrigidas")

if __name__ == "__main__":
    main()
