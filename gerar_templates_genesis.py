#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar páginas template de Gênesis capítulos 6-50
"""

import os

# Template HTML para cada capítulo
TEMPLATE_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Gênesis {capitulo} — 365 de Graça & Adoração</title>
  <meta name="description" content="Estudo de Gênesis capítulo {capitulo} — {titulo}">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>

<body>
  <!-- Topbar -->
  <div class="topbar">
    <div class="inner">
      <div class="brand">
        <span class="dot"></span>
        <span>365 de Graça & Adoração</span>
      </div>

      <nav class="nav" aria-label="Navegação principal">
        <a href="/">Início</a>
        <a href="/sobre/index.html">Sobre</a>
        <a href="/referencias/">Referências</a>
        <a href="/02-pentateuco/genesis/">Gênesis</a>
      </nav>
    </div>
  </div>

  <main class="wrap">
    <!-- Breadcrumb -->
    <nav class="breadcrumb" aria-label="Navegação estrutural">
      <a href="/">Início</a>
      <span>›</span>
      <a href="/02-pentateuco/">Pentateuco</a>
      <span>›</span>
      <a href="/02-pentateuco/genesis/">Gênesis</a>
      <span>›</span>
      <span>Capítulo {capitulo}</span>
    </nav>

    <!-- Conteúdo Principal -->
    <article class="content-article">
      <header class="article-header">
        <h1>📖 Gênesis {capitulo}</h1>
        <p class="subtitle">{titulo}</p>
      </header>

      <section class="article-section">
        <h2>📜 Texto-base</h2>
        <blockquote class="scripture">
          <p><em>Gênesis {capitulo} — [Texto a ser adicionado]</em></p>
        </blockquote>
      </section>

      <section class="article-section">
        <h2>🎯 Visão Geral do Capítulo</h2>
        <p>[Conteúdo a ser desenvolvido]</p>
      </section>

      <section class="article-section">
        <h2>📖 Contexto Histórico e Cultural</h2>
        <p>[Conteúdo a ser desenvolvido]</p>
      </section>

      <section class="article-section">
        <h2>🔍 Exposição do Texto</h2>
        <p>[Conteúdo a ser desenvolvido]</p>
      </section>

      <section class="article-section">
        <h2>💭 As Três Perguntas</h2>
        
        <h3>1️⃣ Onde estava a graça?</h3>
        <p>[Conteúdo a ser desenvolvido]</p>

        <h3>2️⃣ Como era a adoração?</h3>
        <p>[Conteúdo a ser desenvolvido]</p>

        <h3>3️⃣ O que foi revelado sobre o Reino de Deus?</h3>
        <p>[Conteúdo a ser desenvolvido]</p>
      </section>

      <section class="article-section">
        <h2>🧠 Reflexão Teológica</h2>
        <p>[Conteúdo a ser desenvolvido]</p>
      </section>

      <section class="article-section">
        <h2>💡 Aplicação Prática</h2>
        <p>[Conteúdo a ser desenvolvido]</p>
      </section>

      <section class="article-section">
        <h2>📚 Para Aprofundar</h2>
        <ul>
          <li>Consulte a <a href="/referencias/">página de Referências</a> para recursos adicionais</li>
        </ul>
      </section>
    </article>

    <!-- Navegação entre capítulos -->
    <nav class="study-nav" aria-label="Navegação entre estudos">
      {nav_anterior}
      <a href="/02-pentateuco/genesis/" class="btn-secondary">📑 Índice de Gênesis</a>
      {nav_proximo}
    </nav>
  </main>

  <footer class="footer">
    <p>&copy; 2026 365 de Graça & Adoração — Todos os direitos reservados</p>
  </footer>
</body>
</html>
"""

# Títulos dos capítulos de Gênesis
TITULOS_CAPITULOS = {
    6: "A Corrupção da Humanidade e Noé",
    7: "O Dilúvio",
    8: "O Fim do Dilúvio",
    9: "A Aliança com Noé",
    10: "A Tabela das Nações",
    11: "A Torre de Babel e a Genealogia de Sem",
    12: "O Chamado de Abraão",
    13: "Abraão e Ló se Separam",
    14: "Abraão Resgata Ló",
    15: "A Aliança com Abraão",
    16: "Agar e Ismael",
    17: "A Aliança da Circuncisão",
    18: "A Visita dos Três Anjos",
    19: "A Destruição de Sodoma e Gomorra",
    20: "Abraão e Abimeleque",
    21: "O Nascimento de Isaque",
    22: "O Sacrifício de Isaque",
    23: "A Morte de Sara",
    24: "Isaque e Rebeca",
    25: "A Morte de Abraão e os Descendentes de Ismael",
    26: "Isaque e Abimeleque",
    27: "Jacó Recebe a Bênção",
    28: "O Sonho de Jacó em Betel",
    29: "Jacó, Raquel e Lia",
    30: "Os Filhos de Jacó",
    31: "Jacó Foge de Labão",
    32: "Jacó se Prepara para Encontrar Esaú",
    33: "O Encontro de Jacó e Esaú",
    34: "Diná e os Siquemitas",
    35: "Jacó em Betel",
    36: "Os Descendentes de Esaú",
    37: "José e Seus Irmãos",
    38: "Judá e Tamar",
    39: "José e a Mulher de Potifar",
    40: "José Interpreta Sonhos na Prisão",
    41: "José Interpreta os Sonhos de Faraó",
    42: "Os Irmãos de José Vão ao Egito",
    43: "A Segunda Viagem ao Egito",
    44: "A Taça de José",
    45: "José se Revela aos Seus Irmãos",
    46: "Jacó Vai para o Egito",
    47: "José e a Fome no Egito",
    48: "Jacó Abençoa Efraim e Manassés",
    49: "As Bênçãos de Jacó",
    50: "A Morte de Jacó e José"
}

def gerar_paginas():
    """Gera páginas HTML template para Gênesis 6-50"""
    
    base_dir = "/home/ubuntu/365-de-graca-e-adoracao/02-pentateuco/genesis/estudos"
    
    # Criar diretório se não existir
    os.makedirs(base_dir, exist_ok=True)
    
    paginas_criadas = 0
    
    for capitulo in range(6, 51):
        titulo = TITULOS_CAPITULOS.get(capitulo, f"Capítulo {capitulo}")
        
        # Navegação anterior
        if capitulo > 6:
            nav_anterior = f'<a href="genesis-{capitulo-1:02d}.html" class="btn-secondary">← Gênesis {capitulo-1}</a>'
        else:
            nav_anterior = '<span></span>'
        
        # Navegação próxima
        if capitulo < 50:
            nav_proximo = f'<a href="genesis-{capitulo+1:02d}.html" class="btn-primary">Gênesis {capitulo+1} →</a>'
        else:
            nav_proximo = '<span></span>'
        
        # Gerar HTML
        html_content = TEMPLATE_HTML.format(
            capitulo=capitulo,
            titulo=titulo,
            nav_anterior=nav_anterior,
            nav_proximo=nav_proximo
        )
        
        # Nome do arquivo
        filename = f"genesis-{capitulo:02d}.html"
        filepath = os.path.join(base_dir, filename)
        
        # Escrever arquivo
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        paginas_criadas += 1
        print(f"✅ Criado: {filename} — {titulo}")
    
    print(f"\n🎉 Total de páginas criadas: {paginas_criadas}")
    print(f"📁 Localização: {base_dir}")

if __name__ == "__main__":
    print("🚀 Gerando páginas template de Gênesis 6-50...\n")
    gerar_paginas()
    print("\n✅ Processo concluído!")
