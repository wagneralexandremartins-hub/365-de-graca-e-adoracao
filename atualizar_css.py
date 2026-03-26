#!/usr/bin/env python3
"""
Atualiza os seletores CSS no style.css e bloco.css para a nova numeração:
06b → 07, 07 → 08, 08 → 09, 09 → 10, 10 → 11, 11 → 12, 12 → 13
"""
import os

BASE = '/home/ubuntu/365-de-graca-e-adoracao'

# ── style.css ──────────────────────────────────────────────────────────────
style_path = os.path.join(BASE, 'assets/css/style.css')
with open(style_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Substituir o bloco inteiro de CSS dos blocos 06b ao 12
# Encontrar e substituir o trecho completo
antigo = '''/* Bloco 06\u201306b: \u00cdndigo */
.card[data-bloco="06"] .block-number,
.card[data-bloco="06b"] .block-number { color: #6366f1 !important; opacity: 0.6; }
.card[data-bloco="06"] .poster,
.card[data-bloco="06b"] .poster {
  background: linear-gradient(135deg, #06060f 0%, #0a0a1a 100%) !important;
  border-bottom: 1px solid rgba(99,102,241,0.18) !important;
}
.card[data-bloco="06"]:hover,
.card[data-bloco="06b"]:hover { border-color: rgba(99,102,241,0.40) !important; }
/* Seletor extra para garantir 06b em todos os navegadores */
article[data-bloco="06b"] .poster {
  background: linear-gradient(135deg, #06060f 0%, #0a0a1a 100%) !important;
  border-bottom: 1px solid rgba(99,102,241,0.18) !important;
}
article[data-bloco="06b"] .block-number { color: #6366f1 !important; opacity: 0.6; }
/* Bloco 07\u201308: Azul Celeste */
.card[data-bloco="07"] .block-number,
.card[data-bloco="08"] .block-number { color: #0ea5e9; opacity: 0.6; }
.card[data-bloco="07"] .poster,
.card[data-bloco="08"] .poster {
  background: linear-gradient(135deg, #00080f 0%, #001020 100%);
  border-bottom: 1px solid rgba(14,165,233,0.18);
}
.card[data-bloco="07"]:hover,
.card[data-bloco="08"]:hover { border-color: rgba(14,165,233,0.40); }
/* Bloco 09\u201310: Violeta */
.card[data-bloco="09"] .block-number,
.card[data-bloco="10"] .block-number { color: #8b5cf6; opacity: 0.6; }
.card[data-bloco="09"] .poster,
.card[data-bloco="10"] .poster {
  background: linear-gradient(135deg, #060010 0%, #0d0020 100%);
  border-bottom: 1px solid rgba(139,92,246,0.18);
}
.card[data-bloco="09"]:hover,
.card[data-bloco="10"]:hover { border-color: rgba(139,92,246,0.40); }
/* Bloco 11: Rubi */
.card[data-bloco="11"] .block-number { color: #e11d48; opacity: 0.6; }
.card[data-bloco="11"] .poster {
  background: linear-gradient(135deg, #0f0005 0%, #1a000a 100%);
  border-bottom: 1px solid rgba(225,29,72,0.18);
}
.card[data-bloco="11"]:hover { border-color: rgba(225,29,72,0.40); }
/* Bloco 12: Violeta Escuro */
.card[data-bloco="12"] .block-number { color: #7c3aed; opacity: 0.6; }
.card[data-bloco="12"] .poster {
  background: linear-gradient(135deg, #04001a 0%, #0a0030 100%);
  border-bottom: 1px solid rgba(124,58,237,0.18);
}
.card[data-bloco="12"]:hover { border-color: rgba(124,58,237,0.40); }'''

novo = '''/* Bloco 06\u201307: \u00cdndigo (Ap\u00f3crifos + Intertestament\u00e1rio) */
.card[data-bloco="06"] .block-number,
.card[data-bloco="07"] .block-number { color: #6366f1; opacity: 0.6; }
.card[data-bloco="06"] .poster,
.card[data-bloco="07"] .poster {
  background: linear-gradient(135deg, #06060f 0%, #0a0a1a 100%);
  border-bottom: 1px solid rgba(99,102,241,0.18);
}
.card[data-bloco="06"]:hover,
.card[data-bloco="07"]:hover { border-color: rgba(99,102,241,0.40); }
/* Bloco 08\u201309: Azul Celeste (NT + Igreja Primitiva) */
.card[data-bloco="08"] .block-number,
.card[data-bloco="09"] .block-number { color: #0ea5e9; opacity: 0.6; }
.card[data-bloco="08"] .poster,
.card[data-bloco="09"] .poster {
  background: linear-gradient(135deg, #00080f 0%, #001020 100%);
  border-bottom: 1px solid rgba(14,165,233,0.18);
}
.card[data-bloco="08"]:hover,
.card[data-bloco="09"]:hover { border-color: rgba(14,165,233,0.40); }
/* Bloco 10\u201311: Violeta (Conc\u00edlios + Cruzadas) */
.card[data-bloco="10"] .block-number,
.card[data-bloco="11"] .block-number { color: #8b5cf6; opacity: 0.6; }
.card[data-bloco="10"] .poster,
.card[data-bloco="11"] .poster {
  background: linear-gradient(135deg, #060010 0%, #0d0020 100%);
  border-bottom: 1px solid rgba(139,92,246,0.18);
}
.card[data-bloco="10"]:hover,
.card[data-bloco="11"]:hover { border-color: rgba(139,92,246,0.40); }
/* Bloco 12: Rubi (Conflitos Contempor\u00e2neos) */
.card[data-bloco="12"] .block-number { color: #e11d48; opacity: 0.6; }
.card[data-bloco="12"] .poster {
  background: linear-gradient(135deg, #0f0005 0%, #1a000a 100%);
  border-bottom: 1px solid rgba(225,29,72,0.18);
}
.card[data-bloco="12"]:hover { border-color: rgba(225,29,72,0.40); }
/* Bloco 13: Violeta Escuro (Apocalipse) */
.card[data-bloco="13"] .block-number { color: #7c3aed; opacity: 0.6; }
.card[data-bloco="13"] .poster {
  background: linear-gradient(135deg, #04001a 0%, #0a0030 100%);
  border-bottom: 1px solid rgba(124,58,237,0.18);
}
.card[data-bloco="13"]:hover { border-color: rgba(124,58,237,0.40); }'''

if antigo in css:
    css = css.replace(antigo, novo)
    with open(style_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print('✅ style.css atualizado com nova numeração')
else:
    print('⚠️  Trecho não encontrado no style.css — verificar manualmente')
    # Tentar substituição linha a linha
    css = css.replace('data-bloco="06b"', 'data-bloco="07"')
    css = css.replace('bloco-06b', 'bloco-07')
    css = css.replace('/* Bloco 06–06b: Índigo */', '/* Bloco 06–07: Índigo */')
    css = css.replace('/* Bloco 07–08: Azul Celeste */', '/* Bloco 08–09: Azul Celeste */')
    css = css.replace('.card[data-bloco="07"] .block-number,\n.card[data-bloco="08"]', '.card[data-bloco="08"] .block-number,\n.card[data-bloco="09"]')
    css = css.replace('.card[data-bloco="07"] .poster,\n.card[data-bloco="08"]', '.card[data-bloco="08"] .poster,\n.card[data-bloco="09"]')
    css = css.replace('.card[data-bloco="07"]:hover,\n.card[data-bloco="08"]', '.card[data-bloco="08"]:hover,\n.card[data-bloco="09"]')
    css = css.replace('/* Bloco 09–10: Violeta */', '/* Bloco 10–11: Violeta */')
    css = css.replace('.card[data-bloco="09"] .block-number,\n.card[data-bloco="10"]', '.card[data-bloco="10"] .block-number,\n.card[data-bloco="11"]')
    css = css.replace('.card[data-bloco="09"] .poster,\n.card[data-bloco="10"]', '.card[data-bloco="10"] .poster,\n.card[data-bloco="11"]')
    css = css.replace('.card[data-bloco="09"]:hover,\n.card[data-bloco="10"]', '.card[data-bloco="10"]:hover,\n.card[data-bloco="11"]')
    css = css.replace('/* Bloco 11: Rubi */', '/* Bloco 12: Rubi */')
    css = css.replace('.card[data-bloco="11"]', '.card[data-bloco="12"]')
    css = css.replace('/* Bloco 12: Violeta Escuro */', '/* Bloco 13: Violeta Escuro (Apocalipse) */')
    css = css.replace('.card[data-bloco="12"]', '.card[data-bloco="13"]')
    with open(style_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print('✅ style.css atualizado via substituição linha a linha')

# ── bloco.css ──────────────────────────────────────────────────────────────
bloco_path = os.path.join(BASE, 'assets/css/bloco.css')
with open(bloco_path, 'r', encoding='utf-8') as f:
    bcss = f.read()

# Substituições no bloco.css (de trás para frente para evitar conflitos)
subs = [
    ('body.bloco-12 {', 'body.bloco-13 {'),
    ('body.bloco-11 {', 'body.bloco-12 {'),
    ('body.bloco-09, body.bloco-10 {', 'body.bloco-10, body.bloco-11 {'),
    ('body.bloco-07, body.bloco-08 {', 'body.bloco-08, body.bloco-09 {'),
    ('body.bloco-06, body.bloco-06b {', 'body.bloco-06, body.bloco-07 {'),
    ('bloco-06b', 'bloco-07'),
    ('/* Bloco 12 — Violeta Escuro */', '/* Bloco 13 — Violeta Escuro (Apocalipse) */'),
    ('/* Bloco 11 — Rubi */', '/* Bloco 12 — Rubi */'),
    ('/* Bloco 09 e 10 — Violeta */', '/* Bloco 10 e 11 — Violeta */'),
    ('/* Bloco 07 e 08 — Azul Celeste */', '/* Bloco 08 e 09 — Azul Celeste */'),
    ('/* Bloco 06 e 06b — Índigo */', '/* Bloco 06 e 07 — Índigo */'),
    ('Bloco 06b— Intertestamentário', 'Bloco 07 — Intertestamentário'),
]

for antigo_s, novo_s in subs:
    bcss = bcss.replace(antigo_s, novo_s)

with open(bloco_path, 'w', encoding='utf-8') as f:
    f.write(bcss)
print('✅ bloco.css atualizado com nova numeração')
