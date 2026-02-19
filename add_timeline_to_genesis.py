#!/usr/bin/env python3
"""
Script para adicionar linha do tempo e mapas históricos nas páginas de Gênesis
"""

import os
import re
from pathlib import Path

# Diretório dos estudos
ESTUDOS_DIR = Path("02-pentateuco/genesis/estudos")

# CSS para linha do tempo e mapas
TIMELINE_CSS = """
    .historical-context {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 1px solid #333;
        border-radius: 8px;
        padding: 2rem;
        margin: 2rem auto;
        max-width: 1200px;
    }
    
    .context-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .context-header h2 {
        color: #4a9eff;
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }
    
    .context-header p {
        color: #aaa;
        font-size: 0.95rem;
    }
    
    .timeline-map-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
        margin-top: 2rem;
    }
    
    @media (max-width: 768px) {
        .timeline-map-container {
            grid-template-columns: 1fr;
        }
    }
    
    .timeline-section, .map-section {
        background: rgba(0, 0, 0, 0.3);
        border-radius: 8px;
        padding: 1.5rem;
    }
    
    .timeline-section h3, .map-section h3 {
        color: #4a9eff;
        font-size: 1.2rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .timeline-item {
        position: relative;
        padding-left: 2rem;
        margin-bottom: 1.5rem;
        border-left: 2px solid #4a9eff;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -6px;
        top: 0;
        width: 10px;
        height: 10px;
        background: #4a9eff;
        border-radius: 50%;
    }
    
    .timeline-date {
        color: #4a9eff;
        font-weight: bold;
        font-size: 0.9rem;
        margin-bottom: 0.3rem;
    }
    
    .timeline-event {
        color: #fff;
        font-weight: 500;
        margin-bottom: 0.3rem;
    }
    
    .timeline-description {
        color: #aaa;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    
    .map-container {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
    }
    
    .map-container img {
        width: 100%;
        height: auto;
        border-radius: 4px;
        border: 1px solid #333;
    }
    
    .map-caption {
        color: #aaa;
        font-size: 0.85rem;
        margin-top: 0.5rem;
        text-align: center;
        font-style: italic;
    }
    
    .context-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    .key-info {
        background: rgba(74, 158, 255, 0.1);
        border-left: 3px solid #4a9eff;
        padding: 1rem;
        margin-top: 1rem;
        border-radius: 4px;
    }
    
    .key-info strong {
        color: #4a9eff;
        display: block;
        margin-bottom: 0.5rem;
    }
    
    .key-info p {
        color: #ddd;
        font-size: 0.9rem;
        margin: 0;
    }
"""

def get_timeline_for_chapter(chapter_num):
    """Retorna o HTML da linha do tempo apropriada para cada capítulo"""
    
    # Capítulos 1-2: Criação
    if chapter_num in [1, 2]:
        return """
    <section class="historical-context">
        <div class="context-header">
            <h2>🗺️ Contexto Histórico & Geográfico</h2>
            <p>Situando este capítulo na linha do tempo bíblica</p>
        </div>
        
        <div class="timeline-map-container">
            <div class="timeline-section">
                <h3>⏳ Linha do Tempo</h3>
                <span class="context-badge">CRIAÇÃO (~4000 a.C.)</span>
                
                <div class="timeline-item">
                    <div class="timeline-date">Eternidade Passada</div>
                    <div class="timeline-event">Antes da Criação</div>
                    <div class="timeline-description">Deus existe em perfeita comunhão trinitária. O plano da redenção é estabelecido.</div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">Dias 1-7</div>
                    <div class="timeline-event">Semana da Criação</div>
                    <div class="timeline-description">Deus cria o universo, a terra e a humanidade em seis dias, descansando no sétimo.</div>
                </div>
                
                <div class="key-info">
                    <strong>📍 Localização no Plano de Deus:</strong>
                    <p>O início de tudo - fundamento da história da redenção. A criação revela o caráter de Deus: ordenado, generoso e relacional.</p>
                </div>
            </div>
            
            <div class="map-section">
                <h3>🗺️ Geografia Bíblica</h3>
                
                <div class="map-container">
                    <img src="/assets/img/mapa-eden.jpg" alt="Localização do Jardim do Éden">
                    <p class="map-caption">Localização provável do Jardim do Éden na Mesopotâmia (rios Tigre e Eufrates)</p>
                </div>
                
                <div class="key-info">
                    <strong>🌍 Contexto Geográfico:</strong>
                    <p>O Éden estava localizado na região da Mesopotâmia, onde os rios Tigre e Eufrates se encontram (atual Iraque).</p>
                </div>
            </div>
        </div>
    </section>
"""
    
    # Capítulos 3-5: Queda e Era Pré-Diluviana
    elif chapter_num in [3, 4, 5]:
        return """
    <section class="historical-context">
        <div class="context-header">
            <h2>🗺️ Contexto Histórico & Geográfico</h2>
            <p>Situando este capítulo na linha do tempo bíblica</p>
        </div>
        
        <div class="timeline-map-container">
            <div class="timeline-section">
                <h3>⏳ Linha do Tempo</h3>
                <span class="context-badge">ERA PRÉ-DILUVIANA (~4000-2400 a.C.)</span>
                
                <div class="timeline-item">
                    <div class="timeline-date">Após a Criação</div>
                    <div class="timeline-event">A Queda</div>
                    <div class="timeline-description">Adão e Eva desobedecem a Deus e são expulsos do Éden. O pecado entra no mundo.</div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">Primeira Geração</div>
                    <div class="timeline-event">Caim e Abel</div>
                    <div class="timeline-description">Primeiro homicídio. Duas linhagens: Caim (mundana) e Sete (piedosa).</div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">Gerações 1-10</div>
                    <div class="timeline-event">Expansão da Humanidade</div>
                    <div class="timeline-description">Desenvolvimento de agricultura, pecuária, metalurgia e música. Crescente corrupção.</div>
                </div>
                
                <div class="key-info">
                    <strong>📍 Localização no Plano de Deus:</strong>
                    <p>A graça de Deus se manifesta mesmo após a Queda. A promessa de redenção (Gn 3:15) é o primeiro evangelho.</p>
                </div>
            </div>
            
            <div class="map-section">
                <h3>🗺️ Geografia Bíblica</h3>
                
                <div class="map-container">
                    <img src="/assets/img/mapa-eden.jpg" alt="Região do Éden e expansão inicial">
                    <p class="map-caption">Região do Éden e expansão da humanidade pré-diluviana</p>
                </div>
                
                <div class="key-info">
                    <strong>🌍 Contexto Geográfico:</strong>
                    <p>A humanidade se expande a partir do Éden. Caim constrói a primeira cidade a leste do Éden (terra de Node).</p>
                </div>
            </div>
        </div>
    </section>
"""
    
    # Capítulos 6-9: Dilúvio
    elif chapter_num in [6, 7, 8, 9]:
        return """
    <section class="historical-context">
        <div class="context-header">
            <h2>🗺️ Contexto Histórico & Geográfico</h2>
            <p>Situando este capítulo na linha do tempo bíblica</p>
        </div>
        
        <div class="timeline-map-container">
            <div class="timeline-section">
                <h3>⏳ Linha do Tempo</h3>
                <span class="context-badge">O DILÚVIO (~2400 a.C.)</span>
                
                <div class="timeline-item">
                    <div class="timeline-date">120 anos antes</div>
                    <div class="timeline-event">Construção da Arca</div>
                    <div class="timeline-description">Noé recebe ordem de construir a arca. Pregação da justiça por 120 anos.</div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">Ano 600 de Noé</div>
                    <div class="timeline-event">O Dilúvio</div>
                    <div class="timeline-description">40 dias e 40 noites de chuva. Juízo global sobre a humanidade corrupta.</div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">Após o Dilúvio</div>
                    <div class="timeline-event">Aliança Noética</div>
                    <div class="timeline-description">Deus estabelece aliança com Noé. Arco-íris como sinal. Recomeço da civilização.</div>
                </div>
                
                <div class="key-info">
                    <strong>📍 Localização no Plano de Deus:</strong>
                    <p>O Dilúvio demonstra a justiça de Deus contra o pecado, mas também Sua graça em preservar um remanescente fiel.</p>
                </div>
            </div>
            
            <div class="map-section">
                <h3>🗺️ Geografia Bíblica</h3>
                
                <div class="map-container">
                    <img src="/assets/img/mapa-eden.jpg" alt="Monte Ararate">
                    <p class="map-caption">Monte Ararate (atual Turquia) onde a arca repousou</p>
                </div>
                
                <div class="key-info">
                    <strong>🌍 Contexto Geográfico:</strong>
                    <p>A arca repousa no Monte Ararate. Mudanças geológicas massivas transformam a geografia mundial.</p>
                </div>
            </div>
        </div>
    </section>
"""
    
    # Capítulos 10-11: Dispersão das Nações
    elif chapter_num in [10, 11]:
        return """
    <section class="historical-context">
        <div class="context-header">
            <h2>🗺️ Contexto Histórico & Geográfico</h2>
            <p>Situando este capítulo na linha do tempo bíblica</p>
        </div>
        
        <div class="timeline-map-container">
            <div class="timeline-section">
                <h3>⏳ Linha do Tempo</h3>
                <span class="context-badge">DISPERSÃO (~2400-2100 a.C.)</span>
                
                <div class="timeline-item">
                    <div class="timeline-date">Após o Dilúvio</div>
                    <div class="timeline-event">Tábua das Nações</div>
                    <div class="timeline-description">Descendentes de Noé (Sem, Cam, Jafé) se multiplicam e formam nações.</div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">Planície de Sinear</div>
                    <div class="timeline-event">Torre de Babel</div>
                    <div class="timeline-description">Rebelião humana. Deus confunde as línguas e dispersa as nações.</div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">Genealogia</div>
                    <div class="timeline-event">De Sem a Abraão</div>
                    <div class="timeline-description">Linhagem preservada de Sem até Abraão (10 gerações).</div>
                </div>
                
                <div class="key-info">
                    <strong>📍 Localização no Plano de Deus:</strong>
                    <p>A dispersão prepara o cenário para o chamado de Abraão e a formação do povo de Deus.</p>
                </div>
            </div>
            
            <div class="map-section">
                <h3>🗺️ Geografia Bíblica</h3>
                
                <div class="map-container">
                    <img src="/assets/img/mapa-dispersao-nacoes.jpg" alt="Planície de Sinear e dispersão">
                    <p class="map-caption">Planície de Sinear (Babilônia) e dispersão das nações</p>
                </div>
                
                <div class="key-info">
                    <strong>🌍 Contexto Geográfico:</strong>
                    <p>Torre de Babel na planície de Sinear (Babilônia). Dispersão para África, Europa e Ásia.</p>
                </div>
            </div>
        </div>
    </section>
"""
    
    # Capítulos 12-50: Era Patriarcal
    else:
        return """
    <section class="historical-context">
        <div class="context-header">
            <h2>🗺️ Contexto Histórico & Geográfico</h2>
            <p>Situando este capítulo na linha do tempo bíblica</p>
        </div>
        
        <div class="timeline-map-container">
            <div class="timeline-section">
                <h3>⏳ Linha do Tempo</h3>
                <span class="context-badge">ERA PATRIARCAL (~2100-1800 a.C.)</span>
                
                <div class="timeline-item">
                    <div class="timeline-date">~2100 a.C.</div>
                    <div class="timeline-event">Chamado de Abraão</div>
                    <div class="timeline-description">Deus chama Abrão de Ur dos Caldeus. Promessa de terra, descendência e bênção.</div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">~2066 a.C.</div>
                    <div class="timeline-event">Nascimento de Isaque</div>
                    <div class="timeline-description">Filho da promessa nasce. Aliança Abraâmica confirmada.</div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">~2006 a.C.</div>
                    <div class="timeline-event">Jacó e as 12 Tribos</div>
                    <div class="timeline-description">Jacó (Israel) gera os 12 filhos que formarão as tribos de Israel.</div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">~1915 a.C.</div>
                    <div class="timeline-event">José no Egito</div>
                    <div class="timeline-description">José é vendido, torna-se governador e preserva sua família da fome.</div>
                </div>
                
                <div class="key-info">
                    <strong>📍 Localização no Plano de Deus:</strong>
                    <p>Deus forma um povo através do qual todas as nações serão abençoadas. A aliança com Abraão é central.</p>
                </div>
            </div>
            
            <div class="map-section">
                <h3>🗺️ Geografia Bíblica</h3>
                
                <div class="map-container">
                    <img src="/assets/img/mapa-patriarcas.jpg" alt="Jornada dos Patriarcas">
                    <p class="map-caption">Rota: Ur → Harã → Canaã → Egito (Crescente Fértil)</p>
                </div>
                
                <div class="key-info">
                    <strong>🌍 Contexto Geográfico:</strong>
                    <p>Os patriarcas transitam pelo Crescente Fértil: Mesopotâmia, Canaã e Egito. Impérios da época: Egito, Babilônia, Assíria.</p>
                </div>
            </div>
        </div>
    </section>
"""

def extract_chapter_number(filename):
    """Extrai o número do capítulo do nome do arquivo"""
    # Tenta vários padrões
    patterns = [
        r'genesis-(\d+)\.html',  # genesis-06.html
        r'Genesis[_\s](\d+)',
        r'genesis[_\s](\d+)',
        r'(\d+)_Genesis',
        r'(\d+)_genesis',
        r'^(\d+)_',  # 01_Criacao.html, 02_Genesis_1_1_2.html
    ]
    
    for pattern in patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            return int(match.group(1))
    
    return None

def add_timeline_to_file(filepath):
    """Adiciona linha do tempo e mapas a um arquivo HTML"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verifica se já tem linha do tempo
        if 'historical-context' in content:
            print(f"  ⏭️  Já possui linha do tempo: {filepath.name}")
            return False
        
        # Extrai número do capítulo
        chapter_num = extract_chapter_number(filepath.name)
        if not chapter_num:
            print(f"  ⚠️  Não foi possível identificar capítulo: {filepath.name}")
            return False
        
        # Adiciona CSS no <style> existente ou cria novo <style> no <head>
        style_pattern = r'(</style>)'
        if re.search(style_pattern, content):
            content = re.sub(style_pattern, TIMELINE_CSS + r'\1', content, count=1)
        else:
            # Se não tem <style>, adiciona antes do </head>
            head_pattern = r'(</head>)'
            if re.search(head_pattern, content):
                new_style = '  <style>\n' + TIMELINE_CSS + '  </style>\n'
                content = re.sub(head_pattern, new_style + r'\1', content, count=1)
            else:
                print(f"  ⚠️  Não encontrou tag </head>: {filepath.name}")
                return False
        
        # Adiciona HTML da linha do tempo após </header>
        timeline_html = get_timeline_for_chapter(chapter_num)
        header_pattern = r'(</header>\s*)'
        if re.search(header_pattern, content):
            content = re.sub(header_pattern, r'\1\n' + timeline_html + '\n', content, count=1)
        else:
            print(f"  ⚠️  Não encontrou tag </header>: {filepath.name}")
            return False
        
        # Salva arquivo atualizado
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ Atualizado: {filepath.name} (Cap. {chapter_num})")
        return True
        
    except Exception as e:
        print(f"  ❌ Erro ao processar {filepath.name}: {e}")
        return False

def main():
    """Processa todos os arquivos HTML de Gênesis"""
    print("\n🔄 Adicionando linha do tempo e mapas nas páginas de Gênesis...\n")
    
    html_files = list(ESTUDOS_DIR.glob("*.html"))
    
    if not html_files:
        print("❌ Nenhum arquivo HTML encontrado!")
        return
    
    print(f"📁 Encontrados {len(html_files)} arquivos HTML\n")
    
    updated = 0
    skipped = 0
    errors = 0
    
    for filepath in sorted(html_files):
        result = add_timeline_to_file(filepath)
        if result:
            updated += 1
        elif result is False:
            skipped += 1
        else:
            errors += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Atualizados: {updated}")
    print(f"⏭️  Ignorados: {skipped}")
    print(f"❌ Erros: {errors}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
