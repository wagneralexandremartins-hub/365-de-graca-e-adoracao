#!/usr/bin/env python3
"""
Script para gerar páginas HTML dos blocos de Êxodo
"""

import json
import markdown
from pathlib import Path

# Mapear arquivos MD
md_files = {
    1: "0_h0Tggy9g4AYNy83CY39sHQ_1771517386219_na1fn_L2hvbWUvdWJ1bnR1L2VzdHVkb19leG9kb18xLTQ.md",
    2: "1_5Moc7O74h5HQmZaIRdttbi_1771517194557_na1fn_L2hvbWUvdWJ1bnR1L2VzdHVkb19leG9kb19ibG9jb18wMg.md",
    3: "2_2nQvOvPlvmxYT4eayNG38B_1771517237620_na1fn_L2hvbWUvdWJ1bnR1L2VzdHVkb19leG9kb18xMi0xNQ.md",
    4: "3_97YnOdIxHGd3RxTAAcARQx_1771517409538_na1fn_L2hvbWUvdWJ1bnR1L2VzdHVkb19leG9kb18xNi0xOA.md",
    5: "4_xZp8McBHUnKUQpfx2qQchV_1771517487655_na1fn_L2hvbWUvdWJ1bnR1L2VzdHVkb19leG9kb19ibG9jb18wNQ.md",
    6: "5_cZMdEUTYxHC0MdPshqQcXW_1771517947894_na1fn_L2hvbWUvdWJ1bnR1L2VzdHVkb19leG9kb18yNS00MA.md"
}

# Informações dos blocos
blocos_info = [
    {
        "numero": 1,
        "titulo": "O Chamado e a Missão",
        "capitulos": "Êxodo 1-4",
        "mapa": "/assets/img/mapa-rota-exodo.jpg",
        "periodo": "~1526-1446 a.C.",
        "eventos": ["Opressão no Egito", "Nascimento de Moisés", "Sarça Ardente", "Comissão Divina"]
    },
    {
        "numero": 2,
        "titulo": "As Pragas e o Confronto",
        "capitulos": "Êxodo 5-11",
        "mapa": "/assets/img/mapa-exodo-detalhado.gif",
        "periodo": "~1446 a.C.",
        "eventos": ["10 Pragas", "Confronto com Faraó", "Juízo sobre deuses egípcios", "Endurecimento do coração"]
    },
    {
        "numero": 3,
        "titulo": "A Libertação e o Mar",
        "capitulos": "Êxodo 12-15",
        "mapa": "/assets/img/mapa-rota-exodo.jpg",
        "periodo": "~1446 a.C. (Nisã 14-15)",
        "eventos": ["Páscoa", "Saída do Egito", "Mar Vermelho", "Cântico de Vitória"]
    },
    {
        "numero": 4,
        "titulo": "Provações no Deserto",
        "capitulos": "Êxodo 16-18",
        "mapa": "/assets/img/mapa-sinai.jpg",
        "periodo": "~1446 a.C. (meses 2-3)",
        "eventos": ["Maná e Codornizes", "Água da Rocha", "Batalha contra Amaleque", "Conselho de Jetro"]
    },
    {
        "numero": 5,
        "titulo": "A Aliança no Sinai",
        "capitulos": "Êxodo 19-24",
        "mapa": "/assets/img/mapa-sinai.jpg",
        "periodo": "~1446 a.C. (mês 3)",
        "eventos": ["Teofania no Sinai", "Dez Mandamentos", "Livro da Aliança", "Ratificação com Sangue"]
    },
    {
        "numero": 6,
        "titulo": "O Tabernáculo e a Presença",
        "capitulos": "Êxodo 25-40",
        "mapa": "/assets/img/mapa-sinai.jpg",
        "periodo": "~1446-1445 a.C.",
        "eventos": ["Instruções do Tabernáculo", "Bezerro de Ouro", "Intercessão de Moisés", "Glória de Deus"]
    }
]

print("📖 Gerando páginas dos blocos de Êxodo...")
print("="*60)

for bloco in blocos_info:
    num = bloco["numero"]
    md_file = Path(f"/home/ubuntu/conteudo_exodo_md/{md_files[num]}")
    
    # Ler conteúdo Markdown
    md_content = md_file.read_text(encoding='utf-8')
    html_content = markdown.markdown(md_content, extensions=['extra', 'nl2br'])
    
    # Criar HTML completo
    html_page = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bloco {num:02d}: {bloco["titulo"]} — 365 de Graça & Adoração</title>
  <meta name="description" content="Estudo profundo de {bloco["capitulos"]}: {bloco["titulo"]}">
  <link rel="stylesheet" href="/styles.css">
  <style>
    .study-container {{
      max-width: 900px;
      margin: 2rem auto;
      padding: 2rem;
    }}
    .study-header {{
      text-align: center;
      margin-bottom: 3rem;
      padding: 2rem;
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
      border-radius: 12px;
    }}
    .block-number {{
      font-size: 1.2rem;
      color: #4a90e2;
      margin-bottom: 0.5rem;
    }}
    .study-title {{
      font-size: 2.5rem;
      color: #4a90e2;
      margin-bottom: 0.5rem;
    }}
    .study-subtitle {{
      font-size: 1.2rem;
      color: #888;
    }}
    .historical-context {{
      background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%);
      border-left: 4px solid #4a90e2;
      padding: 2rem;
      margin: 2rem 0;
      border-radius: 8px;
    }}
    .timeline {{
      margin: 2rem 0;
    }}
    .timeline-item {{
      padding: 1rem;
      border-left: 3px solid #4a90e2;
      margin-left: 1rem;
      margin-bottom: 1rem;
    }}
    .map-section {{
      margin: 2rem 0;
      text-align: center;
    }}
    .map-section img {{
      max-width: 100%;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}
    .study-content {{
      line-height: 1.8;
      color: #e0e0e0;
    }}
    .study-content h2 {{
      color: #4a90e2;
      margin-top: 2rem;
      margin-bottom: 1rem;
      font-size: 1.8rem;
    }}
    .study-content h3 {{
      color: #5aa3f0;
      margin-top: 1.5rem;
      margin-bottom: 0.75rem;
      font-size: 1.4rem;
    }}
    .study-content p {{
      margin-bottom: 1rem;
    }}
    .nav-buttons {{
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
      border-radius: 8px;
      transition: background 0.3s;
    }}
    .nav-button:hover {{
      background: #357abd;
    }}
    .nav-button.disabled {{
      background: #333;
      opacity: 0.5;
      cursor: not-allowed;
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

  <div class="study-container">
    <div class="study-header">
      <div class="block-number">BLOCO {num:02d}</div>
      <h1 class="study-title">{bloco["titulo"]}</h1>
      <p class="study-subtitle">{bloco["capitulos"]}</p>
    </div>

    <!-- CONTEXTO HISTÓRICO -->
    <div class="historical-context">
      <h2 style="color: #4a90e2; margin-top: 0;">⏳ Contexto Histórico</h2>
      <p><strong>Período:</strong> {bloco["periodo"]}</p>
      <div class="timeline">
        <h3 style="color: #5aa3f0;">Eventos Principais:</h3>
        {"".join([f'<div class="timeline-item"><strong>{evento}</strong></div>' for evento in bloco["eventos"]])}
      </div>
    </div>

    <!-- MAPA -->
    <div class="map-section">
      <h2 style="color: #4a90e2;">🗺️ Geografia Bíblica</h2>
      <img src="{bloco["mapa"]}" alt="Mapa de {bloco["titulo"]}">
    </div>

    <!-- CONTEÚDO DO ESTUDO -->
    <div class="study-content">
      {html_content}
    </div>

    <!-- NAVEGAÇÃO -->
    <div class="nav-buttons">
      {'<a href="/02-pentateuco/exodo/bloco-' + f'{num-1:02d}' + '/index.html" class="nav-button">← Bloco Anterior</a>' if num > 1 else '<span class="nav-button disabled">← Bloco Anterior</span>'}
      <a href="/02-pentateuco/exodo/index.html" class="nav-button">📑 Índice de Êxodo</a>
      {'<a href="/02-pentateuco/exodo/bloco-' + f'{num+1:02d}' + '/index.html" class="nav-button">Próximo Bloco →</a>' if num < 6 else '<span class="nav-button disabled">Próximo Bloco →</span>'}
    </div>
  </div>
</body>
</html>'''
    
    # Salvar arquivo
    output_dir = Path(f"/home/ubuntu/365-de-graca-e-adoracao/02-pentateuco/exodo/bloco-{num:02d}")
    output_file = output_dir / "index.html"
    output_file.write_text(html_page, encoding='utf-8')
    
    print(f"✅ Bloco {num:02d}: {bloco['titulo']} - {len(html_content)} chars")

print("="*60)
print("✅ Todos os 6 blocos de Êxodo gerados!")
