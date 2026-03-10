#!/usr/bin/env python3
"""
Script para adicionar SEO global (Open Graph, meta description, breadcrumb)
em todas as páginas internas do projeto 365 de Graça & Adoração.
"""

import os
import re
from pathlib import Path

BASE_URL = "https://365gracaeadoracao.com"
BASE_DIR = Path("/home/ubuntu/365-de-graca-e-adoracao")

# Mapeamento de diretórios para info de bloco
BLOCO_INFO = {
    "01-principio": {"nome": "O Princípio de Tudo", "cor": "#d97706", "num": "01"},
    "02-pentateuco": {"nome": "Pentateuco", "cor": "#d97706", "num": "02"},
    "03-historicos": {"nome": "Livros Históricos", "cor": "#059669", "num": "03"},
    "04-poeticos": {"nome": "Livros Poéticos", "cor": "#059669", "num": "04"},
    "05-profetas": {"nome": "Livros Proféticos", "cor": "#059669", "num": "05"},
    "06-apocrifos": {"nome": "Livros Apócrifos", "cor": "#6366f1", "num": "06"},
    "07-intertestamentario": {"nome": "Período Intertestamentário", "cor": "#6366f1", "num": "07"},
    "08-novo-testamento": {"nome": "Novo Testamento", "cor": "#0ea5e9", "num": "08"},
    "09-igreja-primitiva": {"nome": "Igreja Primitiva", "cor": "#0ea5e9", "num": "09"},
    "10-concilios": {"nome": "Concílios e História da Igreja", "cor": "#8b5cf6", "num": "10"},
    "11-cruzadas": {"nome": "Cruzadas e Guerras Religiosas", "cor": "#8b5cf6", "num": "11"},
    "12-conflitos-contemporaneos": {"nome": "Conflitos Religiosos Contemporâneos", "cor": "#e11d48", "num": "12"},
    "13-apocalipse": {"nome": "Apocalipse Aprofundado", "cor": "#7c3aed", "num": "13"},
}

# Pastas a ignorar
IGNORAR = {"assets", "node_modules", ".git", "biblia", "01_PENTATEUCO", "01_HISTORICOS"}

def extrair_titulo(html):
    """Extrai o título da página do HTML."""
    m = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    if m:
        return m.group(1).strip()
    # Tenta h1
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    return "365 de Graça & Adoração"

def extrair_descricao(html):
    """Extrai ou gera uma meta description."""
    # Verifica se já tem meta description
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # Tenta pegar do primeiro parágrafo
    m = re.search(r'<p[^>]*>(.*?)</p>', html, re.IGNORECASE | re.DOTALL)
    if m:
        texto = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        texto = re.sub(r'\s+', ' ', texto)
        return texto[:155] + "..." if len(texto) > 155 else texto
    return "Estudo bíblico aprofundado — 365 de Graça & Adoração, da Criação ao Apocalipse."

def gerar_og_tags(titulo, descricao, url_path, bloco_info):
    """Gera as meta tags Open Graph."""
    url_completa = f"{BASE_URL}{url_path}"
    og_image = f"{BASE_URL}/assets/img/og-image.png"
    
    return f"""
  <!-- Open Graph / Redes Sociais -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url_completa}">
  <meta property="og:title" content="{titulo}">
  <meta property="og:description" content="{descricao}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:site_name" content="365 de Graça &amp; Adoração">
  <meta property="og:locale" content="pt_BR">
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{titulo}">
  <meta name="twitter:description" content="{descricao}">
  <meta name="twitter:image" content="{og_image}">"""

def gerar_breadcrumb_json(partes):
    """Gera o JSON-LD de breadcrumb para SEO."""
    items = []
    for i, (nome, url) in enumerate(partes):
        items.append(f'''    {{
      "@type": "ListItem",
      "position": {i+1},
      "name": "{nome}",
      "item": "{BASE_URL}{url}"
    }}''')
    items_str = ",\n".join(items)
    return f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
{items_str}
    ]
  }}
  </script>"""

def processar_arquivo(filepath, bloco_dir, bloco_info):
    """Processa um arquivo HTML adicionando SEO."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception:
        return False

    # Pula se já tem Open Graph
    if 'og:title' in html:
        return False

    # Pula se não tem </head>
    if '</head>' not in html:
        return False

    titulo = extrair_titulo(html)
    descricao = extrair_descricao(html)
    
    # Gera URL relativa
    rel_path = str(filepath.relative_to(BASE_DIR))
    # Remove index.html do final
    url_path = "/" + rel_path.replace("\\", "/")
    if url_path.endswith("/index.html"):
        url_path = url_path[:-len("index.html")]
    elif url_path.endswith(".html"):
        url_path = url_path[:-5]

    # Gera breadcrumb
    partes_breadcrumb = [("Início", "/")]
    if bloco_info:
        partes_breadcrumb.append((f"Bloco {bloco_info['num']} — {bloco_info['nome']}", f"/{bloco_dir}/"))
    
    # Adiciona nível intermediário se for capítulo dentro de livro
    partes_url = url_path.strip("/").split("/")
    if len(partes_url) >= 3:
        livro_url = "/" + "/".join(partes_url[:2]) + "/"
        livro_nome = partes_url[1].replace("-", " ").title()
        partes_breadcrumb.append((livro_nome, livro_url))
    
    if url_path.strip("/") != bloco_dir:
        partes_breadcrumb.append((titulo.split("·")[0].strip(), url_path))

    og_tags = gerar_og_tags(titulo, descricao, url_path, bloco_info)
    breadcrumb_json = gerar_breadcrumb_json(partes_breadcrumb)
    
    # Adiciona meta description se não existir
    meta_desc = ""
    if 'name="description"' not in html and "name='description'" not in html:
        meta_desc = f'\n  <meta name="description" content="{descricao}">'

    # Insere antes de </head>
    insercao = meta_desc + og_tags + "\n" + breadcrumb_json + "\n"
    novo_html = html.replace("</head>", insercao + "</head>", 1)

    if novo_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(novo_html)
        return True
    return False

def main():
    total = 0
    modificados = 0

    for bloco_dir, bloco_info in BLOCO_INFO.items():
        bloco_path = BASE_DIR / bloco_dir
        if not bloco_path.exists():
            print(f"  [SKIP] {bloco_dir} não encontrado")
            continue
        
        count = 0
        for filepath in bloco_path.rglob("*.html"):
            # Ignora pastas de assets
            partes = filepath.parts
            if any(p in IGNORAR for p in partes):
                continue
            total += 1
            if processar_arquivo(filepath, bloco_dir, bloco_info):
                count += 1
                modificados += 1
        
        print(f"  [OK] {bloco_dir}: {count} arquivos com SEO adicionado")

    print(f"\nTotal: {modificados}/{total} arquivos modificados")

if __name__ == "__main__":
    main()
