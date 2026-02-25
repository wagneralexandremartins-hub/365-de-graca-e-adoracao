#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import markdown

# Diretórios
BASE_DIR = "/home/ubuntu/365-de-graca-e-adoracao"
EXODO_DIR = f"{BASE_DIR}/02-pentateuco/exodo"

# Template HTML
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — 365 de Graça & Adoração</title>
    <link rel="stylesheet" href="/assets/css/style.css">
    <style>
        body {{
            background-color: #0a0e1a;
            color: #e8e8e8;
            font-family: 'Georgia', serif;
            line-height: 1.8;
            margin: 0;
            padding: 0;
        }}
        
        header {{
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            padding: 1.5rem 2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }}
        
        header h1 {{
            margin: 0;
            color: #4a90e2;
            font-size: 1.8rem;
        }}
        
        nav {{
            margin-top: 1rem;
        }}
        
        nav a {{
            color: #ffffff;
            text-decoration: none;
            margin-right: 1.5rem;
            font-weight: 500;
            transition: color 0.3s;
        }}
        
        nav a:hover {{
            color: #4a90e2;
        }}
        
        main {{
            max-width: 900px;
            margin: 3rem auto;
            padding: 0 2rem;
        }}
        
        .page-title {{
            color: #4a90e2;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            border-bottom: 3px solid #2a3f5f;
            padding-bottom: 1rem;
        }}
        
        .page-subtitle {{
            color: #5dade2;
            font-size: 1.3rem;
            margin-bottom: 2rem;
        }}
        
        .content h2 {{
            color: #5dade2;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
            font-size: 1.8rem;
        }}
        
        .content h3 {{
            color: #7ec8f3;
            margin-top: 2rem;
            margin-bottom: 0.8rem;
            font-size: 1.4rem;
        }}
        
        .content p {{
            margin-bottom: 1.2rem;
            text-align: justify;
        }}
        
        .content ul, .content ol {{
            margin-left: 2rem;
            margin-bottom: 1.5rem;
        }}
        
        .content li {{
            margin-bottom: 0.8rem;
        }}
        
        .content blockquote {{
            background-color: #1a2332;
            border-left: 4px solid #4a90e2;
            padding: 1rem 1.5rem;
            margin: 1.5rem 0;
            font-style: italic;
            color: #d0d0d0;
        }}
        
        .back-button {{
            display: inline-block;
            background-color: #4a90e2;
            color: white;
            padding: 0.8rem 1.5rem;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 2rem;
            transition: background-color 0.3s;
        }}
        
        .back-button:hover {{
            background-color: #357abd;
        }}
        
        footer {{
            background-color: #0d1117;
            color: #8b949e;
            text-align: center;
            padding: 2rem;
            margin-top: 4rem;
        }}
    </style>
</head>
<body>
    <header>
        <h1>📖 365 de Graça & Adoração</h1>
        <nav>
            <a href="/">Início</a>
            <a href="/sobre">Sobre</a>
            <a href="/sobre/fontes">Referências</a>
            <a href="/biblia">Bíblia</a>
        </nav>
    </header>
    
    <main>
        <h1 class="page-title">{page_title}</h1>
        <p class="page-subtitle">{page_subtitle}</p>
        
        <div class="content">
            {content}
        </div>
        
        <a href="{back_url}" class="back-button">← Voltar para {back_text}</a>
    </main>
    
    <footer>
        <p>&copy; 2026 365 de Graça & Adoração. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
"""

# Mapear arquivos por bloco
def get_files_by_block():
    files = {}
    for i in range(6):
        bloco = f"bloco-0{i+1}"
        files[bloco] = {
            'contexto': None,
            'linha': None,
            'biblio': None
        }
    
    # Contexto histórico
    for f in os.listdir("/home/ubuntu/contexto_historico"):
        if f.endswith(".md"):
            match = re.search(r'^(\d+)_', f)
            if match:
                idx = int(match.group(1))
                bloco = f"bloco-0{idx+1}"
                files[bloco]['contexto'] = f"/home/ubuntu/contexto_historico/{f}"
    
    # Linha do tempo
    for f in os.listdir("/home/ubuntu/linha_do_tempo"):
        if f.endswith(".md"):
            match = re.search(r'^(\d+)_', f)
            if match:
                idx = int(match.group(1))
                bloco = f"bloco-0{idx+1}"
                files[bloco]['linha'] = f"/home/ubuntu/linha_do_tempo/{f}"
    
    # Bibliografia
    for f in os.listdir("/home/ubuntu/bibliografia"):
        if f.endswith(".md"):
            match = re.search(r'^(\d+)_', f)
            if match:
                idx = int(match.group(1))
                bloco = f"bloco-0{idx+1}"
                files[bloco]['biblio'] = f"/home/ubuntu/bibliografia/{f}"
    
    return files

# Títulos dos blocos
BLOCOS_TITULOS = {
    'bloco-01': 'O Chamado e a Missão (Êxodo 1-4)',
    'bloco-02': 'As Pragas e o Confronto (Êxodo 5-11)',
    'bloco-03': 'A Libertação e o Mar (Êxodo 12-15)',
    'bloco-04': 'Provações no Deserto (Êxodo 16-18)',
    'bloco-05': 'A Aliança no Sinai (Êxodo 19-24)',
    'bloco-06': 'O Tabernáculo e a Presença (Êxodo 25-40)'
}

# Criar páginas
files_by_block = get_files_by_block()
pages_created = 0

for bloco, files in files_by_block.items():
    bloco_dir = f"{EXODO_DIR}/{bloco}"
    os.makedirs(bloco_dir, exist_ok=True)
    
    bloco_titulo = BLOCOS_TITULOS[bloco]
    
    # 1. Contexto Histórico
    if files['contexto']:
        with open(files['contexto'], 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        html_content = markdown.markdown(md_content)
        
        html = HTML_TEMPLATE.format(
            title=f"Contexto Histórico - {bloco_titulo}",
            page_title="Contexto Histórico",
            page_subtitle=bloco_titulo,
            content=html_content,
            back_url=f"/02-pentateuco/exodo/{bloco}/",
            back_text=bloco_titulo
        )
        
        output_path = f"{bloco_dir}/contexto-historico.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        pages_created += 1
        print(f"✅ Criado: {output_path}")
    
    # 2. Linha do Tempo
    if files['linha']:
        with open(files['linha'], 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        html_content = markdown.markdown(md_content)
        
        html = HTML_TEMPLATE.format(
            title=f"Linha do Tempo - {bloco_titulo}",
            page_title="Linha do Tempo",
            page_subtitle=bloco_titulo,
            content=html_content,
            back_url=f"/02-pentateuco/exodo/{bloco}/",
            back_text=bloco_titulo
        )
        
        output_path = f"{bloco_dir}/linha-do-tempo.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        pages_created += 1
        print(f"✅ Criado: {output_path}")
    
    # 3. Bibliografia
    if files['biblio']:
        with open(files['biblio'], 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        html_content = markdown.markdown(md_content)
        
        html = HTML_TEMPLATE.format(
            title=f"Bibliografia - {bloco_titulo}",
            page_title="Bibliografia",
            page_subtitle=bloco_titulo,
            content=html_content,
            back_url=f"/02-pentateuco/exodo/{bloco}/",
            back_text=bloco_titulo
        )
        
        output_path = f"{bloco_dir}/bibliografia.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        pages_created += 1
        print(f"✅ Criado: {output_path}")

print(f"\n🎉 Total de páginas criadas: {pages_created}")
