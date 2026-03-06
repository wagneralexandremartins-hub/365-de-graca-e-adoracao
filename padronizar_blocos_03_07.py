#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Padroniza as cores dos blocos 03–07 e adiciona o CSS global bloco.css.
Estes blocos usam style.css + CSS inline com cores variadas.
"""

import os
import re
import glob

BASE = "/home/ubuntu/365-de-graca-e-adoracao"

# Mapeamento: pasta → (classe_body, cor_hex, cor_rgb)
BLOCOS = {
    "03-historicos":        ("bloco-03", "#059669", "5, 150, 105"),
    "04-poeticos":          ("bloco-04", "#059669", "5, 150, 105"),
    "05-profetas":          ("bloco-05", "#059669", "5, 150, 105"),
    "06-apocrifos":         ("bloco-06", "#6366f1", "99, 102, 241"),
    "06-intertestamentario":("bloco-06b","#6366f1", "99, 102, 241"),
    "07-novo-testamento":   ("bloco-07", "#0ea5e9", "14, 165, 233"),
}

# Cores antigas que aparecem nos blocos 03-07 e precisam ser normalizadas
CORES_ANTIGAS = {
    # Bloco 03 — teal/verde
    "#5be7c4": "var(--accent)",
    "rgba(91,231,196,": "rgba(var(--accent-rgb),",
    "rgba(91, 231, 196,": "rgba(var(--accent-rgb),",
    # Bloco 04 — amarelo
    "#ffc850": "var(--accent)",
    "rgba(255,200,80,": "rgba(var(--accent-rgb),",
    # Bloco 05 — vermelho
    "#ef4444": "var(--accent)",
    "rgba(239,68,68,": "rgba(var(--accent-rgb),",
    # Bloco 06 — roxo
    "#c084fc": "var(--accent)",
    "#a78bfa": "var(--accent)",
    "rgba(192,132,252,": "rgba(var(--accent-rgb),",
    "rgba(167,139,250,": "rgba(var(--accent-rgb),",
    # Bloco 07 — âmbar/laranja
    "#f59e0b": "var(--accent)",
    "#f97316": "var(--accent)",
    "rgba(245,158,11,": "rgba(var(--accent-rgb),",
    "rgba(249,115,22,": "rgba(var(--accent-rgb),",
}


def injetar_css_global(html, classe, cor, rgb):
    """Injeta o link para o CSS global e as variáveis de cor."""
    # Verifica se já tem o bloco.css
    if '/assets/css/bloco.css' in html:
        # Apenas atualiza as variáveis
        html = re.sub(
            r'--accent:\s*[^;]+;',
            f'--accent: {cor};',
            html
        )
        html = re.sub(
            r'--accent-rgb:\s*[^;]+;',
            f'--accent-rgb: {rgb};',
            html
        )
        return html
    
    # Adiciona antes de </head>
    novo_link = f"""  <link rel="stylesheet" href="/assets/css/bloco.css">
  <style>
    :root {{
      --accent: {cor};
      --accent-rgb: {rgb};
    }}
  </style>"""
    
    html = html.replace('</head>', f'{novo_link}\n</head>', 1)
    return html


def normalizar_cores_no_css_inline(html, classe, cor, rgb):
    """Substitui cores hardcoded no CSS inline pelas variáveis CSS."""
    # Encontra blocos <style> e substitui as cores
    def substituir_no_style(match):
        css = match.group(0)
        for antiga, nova in CORES_ANTIGAS.items():
            css = css.replace(antiga, nova)
        return css
    
    html = re.sub(r'<style>.*?</style>', substituir_no_style, html, flags=re.DOTALL)
    return html


def adicionar_classe_body(html, classe):
    """Adiciona a classe de bloco ao elemento <body>."""
    # Remove classe anterior se existir
    html = re.sub(r'<body class="bloco-\w+"', '<body', html)
    # Adiciona nova classe
    if '<body class=' in html:
        # Já tem outra classe, adiciona junto
        html = re.sub(r'<body class="([^"]*)"', f'<body class="{classe} \\1"', html, count=1)
    else:
        html = re.sub(r'<body([^>]*)>', f'<body class="{classe}"\\1>', html, count=1)
    return html


def processar_arquivo(filepath, classe, cor, rgb):
    """Processa um único arquivo HTML."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    
    html = injetar_css_global(html, classe, cor, rgb)
    html = normalizar_cores_no_css_inline(html, classe, cor, rgb)
    html = adicionar_classe_body(html, classe)
    
    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False


def main():
    total = 0
    modificados = 0
    
    for pasta, (classe, cor, rgb) in BLOCOS.items():
        caminho = os.path.join(BASE, pasta)
        if not os.path.exists(caminho):
            print(f"⚠️  Pasta não encontrada: {pasta}")
            continue
        
        arquivos = glob.glob(os.path.join(caminho, "**/*.html"), recursive=True)
        arquivos += glob.glob(os.path.join(caminho, "*.html"))
        arquivos = list(set(arquivos))
        
        bloco_mod = 0
        for filepath in sorted(arquivos):
            total += 1
            if processar_arquivo(filepath, classe, cor, rgb):
                modificados += 1
                bloco_mod += 1
        
        print(f"✅ {pasta} ({cor}): {bloco_mod}/{len(arquivos)} arquivos atualizados")
    
    print(f"\n📊 Total: {modificados}/{total} arquivos modificados")
    print("🎉 Padronização dos Blocos 03–07 concluída!")


if __name__ == "__main__":
    main()
