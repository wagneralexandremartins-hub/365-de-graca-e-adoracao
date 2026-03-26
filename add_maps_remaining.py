#!/usr/bin/env python3
"""
Script para adicionar mapas nas páginas restantes de Gênesis
"""

import re
from pathlib import Path

# Páginas que precisam de mapas (Gênesis 3 = Era Pré-Diluviana)
files_to_update = [
    "Gênesis3—DaQuedaàPromessa.html",
    "Gênesis3_9_13_O_Confronto_Divino_e_as_Respostas_Humanas.html",
]

# HTML do contexto histórico para Gênesis 3 (Era Pré-Diluviana)
CONTEXT_HTML = """
    <section class="historical-context" style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border: 1px solid #333; border-radius: 8px; padding: 2rem; margin: 2rem auto; max-width: 1200px;">
        <div class="context-header" style="text-align: center; margin-bottom: 2rem;">
            <h2 style="color: #4a9eff; font-size: 1.8rem; margin-bottom: 0.5rem;">🗺️ Contexto Histórico & Geográfico</h2>
            <p style="color: #aaa; font-size: 0.95rem;">Situando este capítulo na linha do tempo bíblica</p>
        </div>
        
        <div class="timeline-map-container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem;">
            <div class="timeline-section">
                <h3 style="color: #4a9eff; margin-bottom: 1rem;">⏳ Linha do Tempo</h3>
                <span style="background: #2a4a7c; color: #fff; padding: 0.4rem 0.8rem; border-radius: 4px; font-size: 0.85rem; font-weight: 600;">ERA PRÉ-DILUVIANA (~4000-2400 a.C.)</span>
                
                <div style="margin: 1.5rem 0; padding: 1rem; background: rgba(255,255,255,0.03); border-left: 3px solid #4a9eff; border-radius: 4px;">
                    <div style="color: #4a9eff; font-weight: 600; font-size: 0.9rem; margin-bottom: 0.3rem;">Após a Criação</div>
                    <div style="color: #fff; font-weight: 600; margin-bottom: 0.5rem;">A Queda</div>
                    <div style="color: #bbb; font-size: 0.9rem;">Adão e Eva desobedecem a Deus e são expulsos do Éden. O pecado entra no mundo.</div>
                </div>
                
                <div style="margin: 1.5rem 0; padding: 1rem; background: rgba(255,255,255,0.03); border-left: 3px solid #4a9eff; border-radius: 4px;">
                    <div style="color: #4a9eff; font-weight: 600; font-size: 0.9rem; margin-bottom: 0.3rem;">Primeira Geração</div>
                    <div style="color: #fff; font-weight: 600; margin-bottom: 0.5rem;">Caim e Abel</div>
                    <div style="color: #bbb; font-size: 0.9rem;">Primeiro homicídio. Duas linhagens: Caim (mundana) e Sete (piedosa).</div>
                </div>
                
                <div style="margin: 1.5rem 0; padding: 1rem; background: rgba(255,255,255,0.03); border-left: 3px solid #4a9eff; border-radius: 4px;">
                    <div style="color: #4a9eff; font-weight: 600; font-size: 0.9rem; margin-bottom: 0.3rem;">Gerações 1-10</div>
                    <div style="color: #fff; font-weight: 600; margin-bottom: 0.5rem;">Expansão da Humanidade</div>
                    <div style="color: #bbb; font-size: 0.9rem;">Desenvolvimento de agricultura, pecuária, metalurgia e música. Crescente corrupção.</div>
                </div>
                
                <div style="background: rgba(74, 158, 255, 0.1); border: 1px solid rgba(74, 158, 255, 0.3); border-radius: 4px; padding: 1rem; margin-top: 1.5rem;">
                    <strong style="color: #4a9eff;">📍 Localização no Plano de Deus:</strong>
                    <p style="color: #ddd; font-size: 0.9rem; margin: 0.5rem 0 0 0;">A graça de Deus se manifesta mesmo após a Queda. A promessa de redenção (Gn 3:15) é o primeiro evangelho.</p>
                </div>
            </div>
            
            <div class="map-section">
                <h3 style="color: #4a9eff; margin-bottom: 1rem;">🗺️ Geografia Bíblica</h3>
                
                <div class="map-container" style="background: rgba(255,255,255,0.05); border-radius: 8px; overflow: hidden; margin-bottom: 1rem;">
                    <img src="/assets/img/mapa-eden.jpg" alt="Região do Éden e expansão inicial" style="width: 100%; height: auto; display: block;">
                    <p style="color: #aaa; font-size: 0.85rem; padding: 0.8rem; margin: 0; background: rgba(0,0,0,0.3); text-align: center;">Região do Éden e expansão da humanidade pré-diluviana</p>
                </div>
                
                <div style="background: rgba(74, 158, 255, 0.1); border: 1px solid rgba(74, 158, 255, 0.3); border-radius: 4px; padding: 1rem;">
                    <strong style="color: #4a9eff;">🌍 Contexto Geográfico:</strong>
                    <p style="color: #ddd; font-size: 0.9rem; margin: 0.5rem 0 0 0;">A humanidade se expande a partir do Éden. Caim constrói a primeira cidade a leste do Éden (terra de Node).</p>
                </div>
            </div>
        </div>
    </section>
"""

estudos_dir = Path("02-pentateuco/genesis/estudos")

for filename in files_to_update:
    filepath = estudos_dir / filename
    
    if not filepath.exists():
        print(f"⏭️  Arquivo não encontrado: {filename}")
        continue
    
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Verifica se já tem o contexto
        if 'Geografia Bíblica' in content:
            print(f"⏭️  Já possui mapa: {filename}")
            continue
        
        # Procura onde inserir (após o header, antes do conteúdo principal)
        # Tenta inserir após </header> ou após <body>
        if '</header>' in content:
            content = content.replace('</header>', f'</header>\n{CONTEXT_HTML}', 1)
        elif '<body>' in content:
            content = content.replace('<body>', f'<body>\n{CONTEXT_HTML}', 1)
        else:
            print(f"⚠️  Não encontrei onde inserir em: {filename}")
            continue
        
        filepath.write_text(content, encoding='utf-8')
        print(f"✅ Atualizado: {filename}")
        
    except Exception as e:
        print(f"❌ Erro em {filename}: {e}")

print("\n" + "="*60)
print("Concluído!")
print("="*60)
