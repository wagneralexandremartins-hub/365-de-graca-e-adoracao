#!/usr/bin/env python3
"""
Script para gerar páginas HTML da Bíblia ACF
"""

import json
from pathlib import Path
import html

# Carregar JSON da Bíblia ACF
json_path = Path("/home/ubuntu/biblia-json/json/acf_clean.json")
with open(json_path, 'r', encoding='utf-8') as f:
    biblia = json.load(f)

# Criar diretório para a Bíblia
biblia_dir = Path("/home/ubuntu/365-de-graca-e-adoracao/biblia")
biblia_dir.mkdir(exist_ok=True)

print("📖 Gerando páginas da Bíblia ACF...")
print("="*60)

# Template HTML base
def create_html_page(book_name, book_abbrev, chapter_num, verses, total_chapters):
    prev_chapter = f"{book_abbrev}-{chapter_num-1:02d}.html" if chapter_num > 1 else None
    next_chapter = f"{book_abbrev}-{chapter_num+1:02d}.html" if chapter_num < total_chapters else None
    
    verses_html = ""
    for i, verse_text in enumerate(verses, 1):
        verses_html += f'        <div class="verse">\n'
        verses_html += f'          <span class="verse-number">{i}</span>\n'
        verses_html += f'          <span class="verse-text">{html.escape(verse_text)}</span>\n'
        verses_html += f'        </div>\n'
    
    html_content = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{book_name} {chapter_num} — 365 de Graça & Adoração</title>
  <meta name="description" content="Leia {book_name} capítulo {chapter_num} na versão Almeida Corrigida Fiel (ACF)">
  <link rel="stylesheet" href="/styles.css">
  <style>
    .bible-chapter {{
      max-width: 800px;
      margin: 2rem auto;
      padding: 2rem;
    }}
    .chapter-header {{
      text-align: center;
      margin-bottom: 2rem;
      padding-bottom: 1rem;
      border-bottom: 2px solid #4a90e2;
    }}
    .chapter-title {{
      font-size: 2rem;
      color: #4a90e2;
      margin-bottom: 0.5rem;
    }}
    .chapter-subtitle {{
      font-size: 1.2rem;
      color: #888;
    }}
    .verse {{
      margin: 1rem 0;
      line-height: 1.8;
      display: flex;
      gap: 1rem;
    }}
    .verse-number {{
      font-weight: bold;
      color: #4a90e2;
      min-width: 2rem;
      text-align: right;
    }}
    .verse-text {{
      flex: 1;
      color: #e0e0e0;
    }}
    .chapter-nav {{
      display: flex;
      justify-content: space-between;
      margin-top: 3rem;
      padding-top: 2rem;
      border-top: 1px solid #333;
    }}
    .nav-button {{
      padding: 0.75rem 1.5rem;
      background: #4a90e2;
      color: white;
      text-decoration: none;
      border-radius: 5px;
      transition: background 0.3s;
    }}
    .nav-button:hover {{
      background: #357abd;
    }}
    .nav-button.disabled {{
      background: #333;
      cursor: not-allowed;
      opacity: 0.5;
    }}
  </style>
</head>
<body>
  <nav>
    <div class="logo">📖 365 de Graça & Adoração</div>
    <ul>
      <li><a href="/index.html">Início</a></li>
      <li><a href="/sobre/index.html">Sobre</a></li>
      <li><a href="/sobre/fontes/index.html">Referências</a></li>
      <li><a href="/biblia/index.html">Bíblia</a></li>
    </ul>
  </nav>

  <div class="bible-chapter">
    <div class="chapter-header">
      <h1 class="chapter-title">{book_name} {chapter_num}</h1>
      <p class="chapter-subtitle">Almeida Corrigida Fiel (ACF)</p>
    </div>

    <div class="verses">
{verses_html}
    </div>

    <div class="chapter-nav">
      {'<a href="' + prev_chapter + '" class="nav-button">← Capítulo Anterior</a>' if prev_chapter else '<span class="nav-button disabled">← Capítulo Anterior</span>'}
      <a href="/biblia/index.html" class="nav-button">📑 Índice da Bíblia</a>
      {'<a href="' + next_chapter + '" class="nav-button">Próximo Capítulo →</a>' if next_chapter else '<span class="nav-button disabled">Próximo Capítulo →</span>'}
    </div>
  </div>
</body>
</html>'''
    
    return html_content

# Gerar páginas para cada livro e capítulo
total_books = len(biblia)
total_pages = 0

for book in biblia:
    book_name = book['name']
    book_abbrev = book['abbrev']
    chapters = book['chapters']
    
    # Criar diretório do livro
    book_dir = biblia_dir / book_abbrev
    book_dir.mkdir(exist_ok=True)
    
    total_chapters = len(chapters)
    
    for chapter_num, verses in enumerate(chapters, 1):
        filename = f"{book_abbrev}-{chapter_num:02d}.html"
        filepath = book_dir / filename
        
        html_content = create_html_page(book_name, book_abbrev, chapter_num, verses, total_chapters)
        filepath.write_text(html_content, encoding='utf-8')
        
        total_pages += 1
    
    print(f"✅ {book_name} - {total_chapters} capítulos")

print("="*60)
print(f"✅ Total: {total_books} livros, {total_pages} capítulos gerados!")
