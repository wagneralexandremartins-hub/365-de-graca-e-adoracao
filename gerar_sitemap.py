#!/usr/bin/env python3
"""
Gera o sitemap.xml completo para 365gracaeadoracao.com
Percorre todos os arquivos HTML do projeto e gera as URLs com prioridades corretas.
"""

import os
import glob
from datetime import datetime

BASE_URL = "https://365gracaeadoracao.com"
PROJECT_DIR = "/home/ubuntu/365-de-graca-e-adoracao"
OUTPUT_FILE = os.path.join(PROJECT_DIR, "sitemap.xml")

# Data de hoje para lastmod
TODAY = datetime.now().strftime("%Y-%m-%d")

# Prioridades por tipo de página
def get_priority(path):
    # Homepage
    if path == "/":
        return "1.0", "daily"
    # Index de bloco principal
    if path.count("/") == 2 and path.endswith("/index.html"):
        return "0.9", "weekly"
    # Páginas especiais
    if any(x in path for x in ["/timeline/", "/mapas/", "/busca/", "/sobre/"]):
        return "0.8", "weekly"
    # Index de sub-seção (livro dentro de bloco)
    if path.count("/") == 3 and path.endswith("/index.html"):
        return "0.7", "monthly"
    # Capítulos individuais
    if "capitulo" in path or "capitulos" in path:
        return "0.6", "monthly"
    # Módulos temáticos
    return "0.5", "monthly"

# Coletar todos os arquivos HTML
urls = []

# Percorrer todos os arquivos HTML
for root, dirs, files in os.walk(PROJECT_DIR):
    # Ignorar pastas ocultas, node_modules, .git, scripts e pastas legadas
    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in [
        'node_modules', '__pycache__', 'biblia', 'genesis', '01_PENTATEUCO'
    ]]
    
    for fname in files:
        if not fname.endswith('.html'):
            continue
        
        full_path = os.path.join(root, fname)
        
        # Converter para URL relativa
        rel_path = full_path.replace(PROJECT_DIR, "")
        
        # Ignorar arquivos de backup, scripts e arquivos soltos na raiz
        # NOTA: 'test' removido pois bloqueava '08-novo-testamento'
        if any(x in rel_path for x in ['_backup', 'backup', 'gerar_', 'padronizar_', 'renumerar_', 'atualizar_', 'corrigir_', '_template', '01_PENTATEUCO']):
            continue
        
        # Ignorar arquivos HTML soltos na raiz (exceto index.html)
        if rel_path.count('/') == 1 and fname != 'index.html':
            continue
        
        # Normalizar index.html na raiz
        if rel_path == "/index.html":
            url = "/"
        else:
            url = rel_path
        
        priority, changefreq = get_priority(url)
        urls.append((url, priority, changefreq))

# Ordenar: homepage primeiro, depois por prioridade decrescente, depois alfabético
def sort_key(item):
    url, priority, _ = item
    if url == "/":
        return (0, "")
    return (1 - float(priority), url)

urls.sort(key=sort_key)

print(f"Total de URLs encontradas: {len(urls)}")

# Gerar XML
xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
    '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9',
    '        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">',
    '',
    '  <!-- Sitemap gerado automaticamente para 365gracaeadoracao.com -->',
    f'  <!-- Gerado em: {TODAY} | Total de páginas: {len(urls)} -->',
    '',
]

for url, priority, changefreq in urls:
    if url == "/":
        full_url = BASE_URL + "/"
    else:
        full_url = BASE_URL + url
    
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{full_url}</loc>')
    xml_lines.append(f'    <lastmod>{TODAY}</lastmod>')
    xml_lines.append(f'    <changefreq>{changefreq}</changefreq>')
    xml_lines.append(f'    <priority>{priority}</priority>')
    xml_lines.append('  </url>')
    xml_lines.append('')

xml_lines.append('</urlset>')

# Escrever arquivo
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(xml_lines))

print(f"Sitemap gerado: {OUTPUT_FILE}")
print(f"Tamanho: {os.path.getsize(OUTPUT_FILE):,} bytes")

# Estatísticas por bloco
print("\nEstatísticas por seção:")
sections = {}
for url, priority, _ in urls:
    parts = url.strip('/').split('/')
    section = parts[0] if parts[0] else 'raiz'
    sections[section] = sections.get(section, 0) + 1

for section, count in sorted(sections.items()):
    print(f"  {section}: {count} páginas")
