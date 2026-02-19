#!/usr/bin/env python3
"""
Script para gerar sitemap.xml automaticamente
para o projeto 365 de Graça & Adoração
"""

import os
from datetime import datetime
from pathlib import Path
import html

# Configurações
BASE_URL = "https://365-de-graca-e-adoracao.vercel.app"
OUTPUT_FILE = "sitemap.xml"
ROOT_DIR = Path(__file__).parent

# Prioridades por tipo de página
PRIORITIES = {
    'index': '1.0',
    'sobre': '0.9',
    'contexto': '0.9',
    'genesis_index': '0.8',
    'estudos': '0.7',
    'templates': '0.5',
}

# Frequência de atualização
CHANGEFREQ = {
    'index': 'weekly',
    'sobre': 'monthly',
    'contexto': 'monthly',
    'genesis_index': 'weekly',
    'estudos': 'monthly',
    'templates': 'yearly',
}

def get_page_info(filepath):
    """Determina prioridade e changefreq baseado no caminho"""
    path_str = str(filepath)
    
    if path_str == 'index.html':
        return PRIORITIES['index'], CHANGEFREQ['index']
    elif '/sobre/' in path_str:
        return PRIORITIES['sobre'], CHANGEFREQ['sobre']
    elif '/contexto/' in path_str:
        return PRIORITIES['contexto'], CHANGEFREQ['contexto']
    elif 'genesis/index.html' in path_str:
        return PRIORITIES['genesis_index'], CHANGEFREQ['genesis_index']
    elif '/estudos/' in path_str and not path_str.endswith('genesis-'):
        return PRIORITIES['estudos'], CHANGEFREQ['estudos']
    else:
        return PRIORITIES['templates'], CHANGEFREQ['templates']

def find_html_files():
    """Encontra todos os arquivos HTML relevantes"""
    html_files = []
    
    # Diretórios para incluir
    include_dirs = [
        '.',
        'sobre',
        'contexto',
        '01-principio',
        '02-pentateuco/genesis',
        '02-pentateuco/genesis/estudos',
    ]
    
    for dir_path in include_dirs:
        full_path = ROOT_DIR / dir_path
        if full_path.exists():
            for html_file in full_path.glob('*.html'):
                # Ignorar arquivos temporários e templates
                if not html_file.name.startswith('_') and html_file.name != 'template.html':
                    rel_path = html_file.relative_to(ROOT_DIR)
                    html_files.append(rel_path)
    
    return sorted(html_files)

def generate_sitemap():
    """Gera o arquivo sitemap.xml"""
    html_files = find_html_files()
    lastmod = datetime.now().strftime('%Y-%m-%d')
    
    # Início do XML
    xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    # Adicionar cada URL
    for filepath in html_files:
        # Converter caminho do arquivo para URL
        url_path = str(filepath).replace('\\', '/')
        if url_path == 'index.html':
            url = BASE_URL + '/'
        elif url_path.endswith('/index.html'):
            url = BASE_URL + '/' + url_path.replace('/index.html', '/')
        else:
            url = BASE_URL + '/' + url_path
        
        # Escapar caracteres especiais XML
        url = html.escape(url, quote=True)
        
        priority, changefreq = get_page_info(filepath)
        
        xml_content.append('  <url>')
        xml_content.append(f'    <loc>{url}</loc>')
        xml_content.append(f'    <lastmod>{lastmod}</lastmod>')
        xml_content.append(f'    <changefreq>{changefreq}</changefreq>')
        xml_content.append(f'    <priority>{priority}</priority>')
        xml_content.append('  </url>')
    
    # Fim do XML
    xml_content.append('</urlset>')
    
    # Escrever arquivo
    output_path = ROOT_DIR / OUTPUT_FILE
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_content))
    
    print(f"✅ Sitemap gerado com sucesso!")
    print(f"📄 Arquivo: {output_path}")
    print(f"🔗 {len(html_files)} páginas incluídas")
    
    return len(html_files)

if __name__ == '__main__':
    generate_sitemap()
