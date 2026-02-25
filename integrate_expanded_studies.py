#!/usr/bin/env python3
"""
Script para integrar os estudos expandidos nos arquivos HTML de Gênesis
"""

import csv
import re
from pathlib import Path
import markdown

# Ler o CSV com o mapeamento
csv_path = Path("/home/ubuntu/expandir_estudos_genesis.csv")
estudos_dir = Path("02-pentateuco/genesis/estudos")

# Mapeamento de capítulo para arquivo HTML
chapter_to_html = {
    1: ["01_Criacao.html"],
    2: ["02_Genesis_1_1_2.html"],
    3: ["03_Genesis_1_3_5.html", "03_Genesis_3_14_19_O_Juizo_Divino_e_Suas_Consequencias.html", "03_Genesis_3_Queda_e_Promessa.html"],
    4: ["01_Genesis_4_1_5_Caim_e_Abel_Adoracao_e_Aceitacao.html", "02_Genesis_4_6_8_Pecado_a_Porta_e_o_Homicidio.html"],
    5: ["01_Genesis_5_1_32_Genealogia_de_Adao.html", "01_Genesis_5_1_4_Introducao_e_Imagem_de_Deus.html", "02_Genesis_5_5_8_Adao_a_Sete_Continuidade.html"],
}

# Para capítulos 6-50, usar genesis-XX.html
for i in range(6, 51):
    chapter_to_html[i] = [f"genesis-{i:02d}.html"]

print("🔄 Integrando estudos expandidos nos arquivos HTML...")
print("="*60)

# Ler CSV
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        capitulo = int(row['Capítulo'])
        md_file = Path(row['Conteúdo em Markdown'])
        titulo = row['Título do Capítulo']
        
        if not md_file.exists():
            print(f"⚠️  Arquivo MD não encontrado: {md_file.name}")
            continue
        
        # Ler conteúdo Markdown
        md_content = md_file.read_text(encoding='utf-8')
        
        # Converter Markdown para HTML
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
        
        # Pegar os arquivos HTML correspondentes
        html_files = chapter_to_html.get(capitulo, [])
        
        for html_filename in html_files:
            html_path = estudos_dir / html_filename
            
            if not html_path.exists():
                print(f"⏭️  HTML não encontrado: {html_filename}")
                continue
            
            try:
                content = html_path.read_text(encoding='utf-8')
                
                # Procurar onde inserir o conteúdo expandido
                # Inserir após a seção historical-context
                if 'historical-context' in content:
                    # Encontrar o final da seção historical-context
                    match = re.search(r'</section>(\s*<!--.*?-->)?(\s*<div class="study-content">)?', content, re.DOTALL)
                    if match:
                        insert_pos = match.end()
                        # Inserir o conteúdo expandido
                        new_content = (
                            content[:insert_pos] +
                            f'\n<div class="study-content">\n{html_content}\n</div>\n' +
                            content[insert_pos:]
                        )
                        html_path.write_text(new_content, encoding='utf-8')
                        print(f"✅ Gênesis {capitulo:02d} → {html_filename}")
                    else:
                        print(f"⚠️  Não encontrei onde inserir em: {html_filename}")
                else:
                    print(f"⚠️  Sem historical-context em: {html_filename}")
                    
            except Exception as e:
                print(f"❌ Erro em {html_filename}: {e}")

print("="*60)
print("✅ Integração concluída!")
