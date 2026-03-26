#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

EXODO_DIR = "/home/ubuntu/365-de-graca-e-adoracao/02-pentateuco/exodo"

# Links a serem adicionados
LINKS_HTML = """
        <div class="complementary-links" style="margin-top: 3rem; padding: 2rem; background-color: #141824; border: 1px solid #2a3f5f; border-radius: 8px;">
            <h3 style="color: #5dade2; margin-bottom: 1.5rem;">📚 Recursos Complementares</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
                <a href="contexto-historico.html" style="display: block; padding: 1rem; background-color: #1a2332; border: 1px solid #2a3f5f; border-radius: 5px; text-decoration: none; color: #e8e8e8; transition: all 0.3s;">
                    <strong style="color: #4a90e2;">📜 Contexto Histórico</strong><br>
                    <span style="font-size: 0.9rem; color: #b0b0b0;">Situação do Egito e cronologia</span>
                </a>
                <a href="linha-do-tempo.html" style="display: block; padding: 1rem; background-color: #1a2332; border: 1px solid #2a3f5f; border-radius: 5px; text-decoration: none; color: #e8e8e8; transition: all 0.3s;">
                    <strong style="color: #4a90e2;">⏳ Linha do Tempo</strong><br>
                    <span style="font-size: 0.9rem; color: #b0b0b0;">Cronologia dos eventos</span>
                </a>
                <a href="bibliografia.html" style="display: block; padding: 1rem; background-color: #1a2332; border: 1px solid #2a3f5f; border-radius: 5px; text-decoration: none; color: #e8e8e8; transition: all 0.3s;">
                    <strong style="color: #4a90e2;">📖 Bibliografia</strong><br>
                    <span style="font-size: 0.9rem; color: #b0b0b0;">Referências específicas</span>
                </a>
            </div>
        </div>
"""

# Processar cada bloco
blocos = ['bloco-01', 'bloco-02', 'bloco-03', 'bloco-04', 'bloco-05', 'bloco-06']
updated = 0

for bloco in blocos:
    index_path = f"{EXODO_DIR}/{bloco}/index.html"
    
    if not os.path.exists(index_path):
        print(f"⚠️  Arquivo não encontrado: {index_path}")
        continue
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verificar se já tem os links
    if 'complementary-links' in content:
        print(f"ℹ️  {bloco}: Links já existem, pulando...")
        continue
    
    # Adicionar links antes da navegação
    if '<!-- NAVEGAÇÃO -->' in content:
        content = content.replace('<!-- NAVEGAÇÃO -->', f'{LINKS_HTML}\n    <!-- NAVEGAÇÃO -->')
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        updated += 1
        print(f"✅ {bloco}: Links adicionados!")
    else:
        print(f"⚠️  {bloco}: Tag </main> não encontrada")

print(f"\n🎉 Total de páginas atualizadas: {updated}")
