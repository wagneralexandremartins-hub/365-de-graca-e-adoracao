#!/usr/bin/env python3
"""
Script para converter arquivos Markdown em páginas HTML
para o projeto 365 de Graça & Adoração
"""

import os
import re
from pathlib import Path

def clean_filename(filename):
    """Remove caracteres especiais e normaliza o nome do arquivo"""
    # Remove extensão se existir
    name = filename.replace('.md', '').replace('.html', '')
    # Remove ## e # do início
    name = re.sub(r'^#+', '', name)
    return name

def read_markdown(filepath):
    """Lê o conteúdo do arquivo Markdown"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        try:
            with open(filepath, 'r', encoding='latin-1') as f:
                return f.read()
        except Exception as e:
            print(f"Erro ao ler {filepath}: {e}")
            return None

def markdown_to_html(md_content):
    """Converte Markdown básico para HTML"""
    if not md_content:
        return ""
    
    html = md_content
    
    # Headers
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    
    # Italic
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Links
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)
    
    # Blockquotes
    html = re.sub(r'^> (.*?)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    
    # Lists
    lines = html.split('\n')
    in_list = False
    result = []
    
    for line in lines:
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            if not in_list:
                result.append('<ul>')
                in_list = True
            item = line.strip()[2:]
            result.append(f'<li>{item}</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(line)
    
    if in_list:
        result.append('</ul>')
    
    html = '\n'.join(result)
    
    # Paragraphs
    paragraphs = html.split('\n\n')
    formatted = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<') and not p.endswith('>'):
            formatted.append(f'<p>{p}</p>')
        else:
            formatted.append(p)
    
    return '\n'.join(formatted)

def create_html_page(title, content, breadcrumb=""):
    """Cria uma página HTML completa"""
    template = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 365 de Graça & Adoração</title>
    <link rel="stylesheet" href="/assets/css/style.css">
    <style>
        .study-content {{
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            line-height: 1.8;
        }}
        .study-content h1 {{
            color: #e50914;
            margin-bottom: 1rem;
        }}
        .study-content h2 {{
            color: #fff;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #333;
            padding-bottom: 0.5rem;
        }}
        .study-content h3 {{
            color: #ccc;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
        }}
        .study-content p {{
            margin-bottom: 1rem;
            color: #ddd;
        }}
        .study-content blockquote {{
            border-left: 4px solid #e50914;
            padding-left: 1rem;
            margin: 1.5rem 0;
            font-style: italic;
            color: #bbb;
        }}
        .study-content ul {{
            margin: 1rem 0;
            padding-left: 2rem;
        }}
        .study-content li {{
            margin-bottom: 0.5rem;
            color: #ddd;
        }}
        .study-content strong {{
            color: #fff;
            font-weight: 600;
        }}
        .breadcrumb {{
            padding: 1rem 2rem;
            background: #1a1a1a;
            border-bottom: 1px solid #333;
        }}
        .breadcrumb a {{
            color: #e50914;
            text-decoration: none;
            margin-right: 0.5rem;
        }}
        .breadcrumb a:hover {{
            text-decoration: underline;
        }}
        .navigation {{
            display: flex;
            justify-content: space-between;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #333;
        }}
        .navigation a {{
            color: #e50914;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border: 1px solid #e50914;
            border-radius: 4px;
            transition: all 0.3s;
        }}
        .navigation a:hover {{
            background: #e50914;
            color: #fff;
        }}
    </style>
</head>
<body>
    <header>
        <nav>
            <a href="/" class="logo">365 de Graça & Adoração</a>
            <div class="nav-links">
                <a href="/02-pentateuco/genesis/index.html">← Voltar ao Gênesis</a>
                <a href="/">Início</a>
            </div>
        </nav>
    </header>

    {breadcrumb}

    <main class="study-content">
        {content}
        
        <div class="navigation">
            <a href="/02-pentateuco/genesis/index.html">← Voltar aos Estudos</a>
            <a href="/">Início</a>
        </div>
    </main>

    <footer>
        <p>&copy; 2025 365 de Graça & Adoração. Todos os direitos reservados.</p>
    </footer>

    <script src="/assets/js/script.js"></script>
</body>
</html>"""
    return template

def convert_file(input_path, output_path):
    """Converte um arquivo Markdown para HTML"""
    md_content = read_markdown(input_path)
    if not md_content:
        return False
    
    # Extrai o título (primeiro h1 ou nome do arquivo)
    title_match = re.search(r'^#\s+(.*?)$', md_content, re.MULTILINE)
    if title_match:
        title = title_match.group(1)
    else:
        title = clean_filename(input_path.stem)
    
    html_content = markdown_to_html(md_content)
    full_html = create_html_page(title, html_content)
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
        return True
    except Exception as e:
        print(f"Erro ao escrever {output_path}: {e}")
        return False

def main():
    """Função principal"""
    base_dir = Path(__file__).parent
    estudos_dir = base_dir / '02-pentateuco' / 'genesis' / 'estudos'
    
    if not estudos_dir.exists():
        print(f"Diretório não encontrado: {estudos_dir}")
        return
    
    converted = 0
    errors = 0
    
    # Processa todos os arquivos
    for file_path in estudos_dir.iterdir():
        if file_path.is_file():
            # Define o nome do arquivo de saída
            output_name = clean_filename(file_path.stem) + '.html'
            output_path = estudos_dir / output_name
            
            print(f"Convertendo: {file_path.name} → {output_name}")
            
            if convert_file(file_path, output_path):
                converted += 1
            else:
                errors += 1
    
    print(f"\n✅ Conversão concluída!")
    print(f"   Arquivos convertidos: {converted}")
    print(f"   Erros: {errors}")

if __name__ == '__main__':
    main()
