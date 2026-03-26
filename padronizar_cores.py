#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Padroniza as cores de todos os blocos 08–12 do projeto 365 de Graça & Adoração.
Substitui o CSS inline por referência ao CSS global /assets/css/bloco.css
e adiciona a classe de bloco ao <body>.
"""

import os
import re
import glob

BASE = "/home/ubuntu/365-de-graca-e-adoracao"

# Mapeamento: pasta → (classe_body, cor_hex, cor_rgb, nome_bloco)
BLOCOS = {
    "08-igreja-primitiva": ("bloco-08", "#0ea5e9", "14, 165, 233", "Bloco 08 — Igreja Primitiva"),
    "09-concilios":        ("bloco-09", "#8b5cf6", "139, 92, 246",  "Bloco 09 — Concílios"),
    "10-cruzadas":         ("bloco-10", "#8b5cf6", "139, 92, 246",  "Bloco 10 — Cruzadas"),
    "11-conflitos-contemporaneos": ("bloco-11", "#e11d48", "225, 29, 72", "Bloco 11 — Conflitos"),
    "12-apocalipse":       ("bloco-12", "#7c3aed", "124, 58, 237",  "Bloco 12 — Apocalipse"),
}

# CSS padrão a ser injetado no <head> de cada arquivo
# (variáveis de cor + link para o CSS global)
def gerar_head_css(classe, cor, rgb):
    return f"""  <link rel="stylesheet" href="/assets/css/bloco.css">
  <style>
    :root {{
      --accent: {cor};
      --accent-rgb: {rgb};
    }}
  </style>"""


def substituir_style_inline(html, classe, cor, rgb):
    """Remove o bloco <style>...</style> inline e substitui pelo CSS global."""
    # Remove o bloco <style> inline completo
    html = re.sub(r'\s*<style>.*?</style>', '', html, flags=re.DOTALL)
    
    # Remove qualquer link para bloco.css já existente (evitar duplicação)
    html = re.sub(r'\s*<link[^>]*bloco\.css[^>]*>', '', html)
    
    # Injeta o novo CSS antes de </head>
    novo_head = gerar_head_css(classe, cor, rgb)
    html = html.replace('</head>', f'{novo_head}\n</head>')
    
    return html


def adicionar_classe_body(html, classe):
    """Adiciona a classe de bloco ao elemento <body>."""
    # Remove classe de bloco anterior se existir
    html = re.sub(r'<body class="bloco-\d+[a-z]*"', '<body', html)
    # Adiciona a nova classe
    html = re.sub(r'<body([^>]*)>', f'<body class="{classe}"\\1>', html, count=1)
    return html


def padronizar_cores_inline(html, cor, rgb):
    """Substitui cores hardcoded pela variável --accent."""
    # Cores que eram usadas nos blocos 08-12 (mapeamento antigo → novo)
    substituicoes_cor = {
        # Bloco 08 — laranja
        "#f97316": "var(--accent)",
        "rgba(249,115,22,": f"rgba(var(--accent-rgb),",
        "rgba(249, 115, 22,": f"rgba(var(--accent-rgb),",
        # Bloco 09 — índigo/violeta
        "#818cf8": "var(--accent)",
        "rgba(129,140,248,": f"rgba(var(--accent-rgb),",
        "rgba(129, 140, 248,": f"rgba(var(--accent-rgb),",
        # Bloco 10 — vermelho escuro
        "#dc2626": "var(--accent)",
        "rgba(220,38,38,": f"rgba(var(--accent-rgb),",
        # Bloco 11 — vermelho
        "#ef4444": "var(--accent)",
        "rgba(239,68,68,": f"rgba(var(--accent-rgb),",
        # Bloco 12 — roxo
        "#c084fc": "var(--accent)",
        "#a855f7": "var(--accent)",
        "rgba(192,132,252,": f"rgba(var(--accent-rgb),",
        "rgba(168,85,247,": f"rgba(var(--accent-rgb),",
    }
    # Não substituímos no corpo HTML — apenas no CSS inline (já removido)
    return html


def processar_arquivo(filepath, classe, cor, rgb):
    """Processa um único arquivo HTML."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    
    # 1. Substituir CSS inline pelo CSS global
    html = substituir_style_inline(html, classe, cor, rgb)
    
    # 2. Adicionar classe ao body
    html = adicionar_classe_body(html, classe)
    
    # 3. Corrigir background do body se ainda hardcoded
    html = re.sub(
        r"body\s*\{[^}]*background:\s*#0[fa]172a[^}]*\}",
        "",
        html
    )
    
    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False


def main():
    total = 0
    modificados = 0
    
    for pasta, (classe, cor, rgb, nome) in BLOCOS.items():
        caminho = os.path.join(BASE, pasta)
        if not os.path.exists(caminho):
            print(f"⚠️  Pasta não encontrada: {pasta}")
            continue
        
        arquivos = glob.glob(os.path.join(caminho, "**/*.html"), recursive=True)
        arquivos += glob.glob(os.path.join(caminho, "*.html"))
        arquivos = list(set(arquivos))  # remover duplicatas
        
        bloco_mod = 0
        for filepath in sorted(arquivos):
            total += 1
            if processar_arquivo(filepath, classe, cor, rgb):
                modificados += 1
                bloco_mod += 1
        
        print(f"✅ {nome}: {bloco_mod}/{len(arquivos)} arquivos atualizados")
    
    print(f"\n📊 Total: {modificados}/{total} arquivos modificados")
    print("🎉 Padronização de cores concluída!")


if __name__ == "__main__":
    main()
