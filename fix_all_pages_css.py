#!/usr/bin/env python3
"""
Script para corrigir CSS e legibilidade de todas as páginas do projeto
"""
import os
import re
from pathlib import Path

# Diretório base
BASE_DIR = Path("/home/ubuntu/365-de-graca-e-adoracao")

# CSS otimizado para legibilidade
OPTIMIZED_CSS = """
<style>
/* Reset e Base */
body {
  background: #0a0e1a !important;
  color: #e8e8e8 !important;
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif;
  line-height: 1.7;
  margin: 0;
  padding: 0;
}

/* Container principal */
.container, .wrap {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  background: #0a0e1a;
}

/* Títulos */
h1, h2, h3, h4, h5, h6 {
  color: #5dade2 !important;
  font-weight: 700;
  margin-top: 2rem;
  margin-bottom: 1rem;
}

h1 { font-size: 2.5rem; color: #4a90e2 !important; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }

/* Parágrafos */
p {
  color: #e8e8e8 !important;
  margin-bottom: 1.2rem;
  line-height: 1.8;
}

/* Links */
a {
  color: #5dade2 !important;
  text-decoration: none;
  transition: color 0.3s;
}

a:hover {
  color: #7ec8f3 !important;
  text-decoration: underline;
}

/* Blockquotes */
blockquote {
  background: #1a2332 !important;
  border-left: 4px solid #4a90e2;
  padding: 1.5rem;
  margin: 1.5rem 0;
  border-radius: 8px;
  color: #d0d0d0 !important;
  font-style: italic;
}

/* Listas */
ul, ol {
  color: #e8e8e8 !important;
  margin-bottom: 1.5rem;
  padding-left: 2rem;
}

li {
  margin-bottom: 0.8rem;
  line-height: 1.7;
}

/* Seções especiais */
.historical-context, .timeline, .geography {
  background: linear-gradient(135deg, #1a2332 0%, #0f1922 100%);
  border: 2px solid #2a4a6a;
  border-radius: 12px;
  padding: 2rem;
  margin: 2rem 0;
}

.historical-context h2, .timeline h2, .geography h2 {
  color: #5dade2 !important;
  margin-top: 0;
}

/* Tabelas */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 2rem 0;
  background: #1a2332;
  border-radius: 8px;
  overflow: hidden;
}

th {
  background: #2a4a6a;
  color: #ffffff !important;
  padding: 1rem;
  text-align: left;
  font-weight: 700;
}

td {
  padding: 1rem;
  border-top: 1px solid #2a4a6a;
  color: #e8e8e8 !important;
}

/* Código */
code {
  background: #1a2332;
  color: #5dade2;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
}

pre {
  background: #1a2332;
  padding: 1.5rem;
  border-radius: 8px;
  overflow-x: auto;
  border: 1px solid #2a4a6a;
}

pre code {
  background: none;
  padding: 0;
}

/* Botões */
.btn, button {
  background: #4a90e2;
  color: #ffffff !important;
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  border: none;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s;
}

.btn:hover, button:hover {
  background: #5dade2;
  text-decoration: none;
}

/* Imagens */
img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 1.5rem 0;
}

/* Responsivo */
@media (max-width: 768px) {
  body {
    font-size: 16px;
  }
  
  h1 { font-size: 2rem; }
  h2 { font-size: 1.75rem; }
  h3 { font-size: 1.5rem; }
  
  .container, .wrap {
    padding: 1rem;
  }
}
</style>
"""

def fix_html_file(file_path):
    """Corrige CSS de um arquivo HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove <style> tags antigos (exceto o do menu/topbar)
        content = re.sub(
            r'<style>(?:(?!</style>).)*?</style>',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Adiciona novo CSS otimizado após o <head>
        if '<head>' in content:
            content = content.replace('<head>', f'<head>\n{OPTIMIZED_CSS}')
        
        # Salva arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Erro em {file_path}: {e}")
        return False

def main():
    """Processa todas as páginas HTML"""
    count = 0
    
    # Gênesis
    genesis_dir = BASE_DIR / "02-pentateuco" / "genesis" / "estudos"
    if genesis_dir.exists():
        for html_file in genesis_dir.glob("*.html"):
            if fix_html_file(html_file):
                count += 1
                print(f"✅ {html_file.name}")
    
    # Êxodo
    exodo_dir = BASE_DIR / "02-pentateuco" / "exodo"
    if exodo_dir.exists():
        # Índice
        index_file = exodo_dir / "index.html"
        if index_file.exists():
            if fix_html_file(index_file):
                count += 1
                print(f"✅ {index_file.name}")
        
        # Blocos
        for i in range(1, 7):
            bloco_dir = exodo_dir / f"bloco-{i:02d}"
            if bloco_dir.exists():
                index_file = bloco_dir / "index.html"
                if index_file.exists():
                    if fix_html_file(index_file):
                        count += 1
                        print(f"✅ bloco-{i:02d}/index.html")
    
    print(f"\n✅ Total: {count} páginas corrigidas")

if __name__ == "__main__":
    main()
