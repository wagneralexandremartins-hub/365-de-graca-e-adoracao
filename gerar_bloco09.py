#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os 8 módulos aprofundados do Bloco 09 — Concílios e História da Igreja."""

import os

BASE = "/home/ubuntu/365-de-graca-e-adoracao/09-concilios"

CSS_COMUM = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: #0f172a; color: #e2e8f0; font-family: 'Georgia', serif; line-height: 1.7; }
    a { color: inherit; text-decoration: none; }
    .topbar { background: rgba(15,23,42,0.97); border-bottom: 1px solid rgba(255,255,255,0.07); padding: 14px 0; position: sticky; top: 0; z-index: 100; }
    .topbar .inner { max-width: 900px; margin: 0 auto; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
    .topbar a { font-size: 0.85rem; color: #94a3b8; font-weight: 600; }
    .hero { padding: 64px 24px 48px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.07); }
    .tag { display: inline-block; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 999px; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 1px; }
    .hero h1 { font-size: 2.4rem; font-weight: 900; color: #f1f5f9; margin-bottom: 12px; line-height: 1.2; }
    .hero .ref { font-size: 0.88rem; color: #64748b; margin-bottom: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .hero blockquote { font-style: italic; color: #cbd5e1; font-size: 1rem; padding-left: 20px; max-width: 620px; margin: 0 auto; text-align: left; }
    .wrap { max-width: 900px; margin: 0 auto; padding: 40px 24px 80px; }
    .sb { margin-bottom: 40px; }
    .sb h2 { font-size: 1.3rem; font-weight: 800; color: #f1f5f9; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.07); }
    .sb p { color: #94a3b8; font-size: 0.95rem; line-height: 1.85; margin-bottom: 16px; }
    .bloco { border-left-width: 3px; border-left-style: solid; border-radius: 0 12px 12px 0; padding: 18px 20px; margin-bottom: 16px; background: rgba(255,255,255,0.02); border-top: 1px solid rgba(255,255,255,0.07); border-right: 1px solid rgba(255,255,255,0.07); border-bottom: 1px solid rgba(255,255,255,0.07); }
    .bt { font-size: 0.85rem; font-weight: 800; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
    .bx { color: #94a3b8; font-size: 0.92rem; line-height: 1.82; }
    table { width: 100%; border-collapse: collapse; font-size: 0.87rem; margin: 20px 0 32px; }
    td { padding: 10px 14px; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; }
    tr:hover td { background: rgba(255,255,255,0.02); }
    .nav-mod { display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.07); flex-wrap: wrap; gap: 10px; }
    .nav-mod a { padding: 10px 20px; border-radius: 8px; font-size: 0.88rem; font-weight: 700; transition: all 0.2s; }
    .reflexao { border-radius: 12px; padding: 22px 26px; margin-top: 32px; background: rgba(34,197,94,0.05); border: 1px solid rgba(34,197,94,0.15); }
    .reflexao h3 { color: #22c55e; font-size: 0.95rem; font-weight: 800; margin-bottom: 10px; }
    .reflexao p { color: #94a3b8; font-size: 0.9rem; line-height: 1.8; margin-bottom: 10px; }
    .reflexao p:last-child { margin-bottom: 0; }
    .pers-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; margin: 20px 0 32px; }
    .pers-card { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; padding: 16px; }
    .pers-nome { font-size: 0.95rem; font-weight: 800; margin-bottom: 4px; }
    .pers-datas { font-size: 0.72rem; color: #64748b; margin-bottom: 8px; font-weight: 600; }
    .pers-desc { font-size: 0.83rem; color: #94a3b8; line-height: 1.6; }
    .credo-box { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 24px 28px; margin: 20px 0 32px; font-style: italic; color: #cbd5e1; font-size: 0.92rem; line-height: 1.9; }
    .credo-box .credo-titulo { font-style: normal; font-weight: 800; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 14px; }
"""


def pagina(pasta, cor, hero_bg, titulo, subtitulo, ref, citacao, autor_cit, corpo, nav_prev, nav_prev_lbl, nav_next, nav_next_lbl):
    css_extra = f"""
    .topbar a:hover {{ color: {cor}; }}
    .hero {{ background: linear-gradient(135deg, #0f172a 0%, {hero_bg} 50%, #0f172a 100%); }}
    .tag {{ background: {cor}18; border: 1px solid {cor}40; color: {cor}; }}
    .hero blockquote {{ border-left: 3px solid {cor}; }}
    .bloco {{ border-left-color: {cor}; }}
    .bt {{ color: {cor}; }}
    table th {{ background: {cor}18; color: {cor}; border-bottom: 1px solid {cor}30; }}
    .nav-mod a {{ background: {cor}18; border: 1px solid {cor}30; color: {cor}; }}
    .nav-mod a:hover {{ background: {cor}30; }}
    .pers-nome {{ color: {cor}; }}
    .credo-box .credo-titulo {{ color: {cor}; }}
    """
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titulo} | Bloco 09 — 365 de Graça & Adoração</title>
  <link rel="icon" href="/favicon.ico">
  <style>{CSS_COMUM}{css_extra}</style>
</head>
<body>
  <div class="topbar"><div class="inner">
    <a href="/09-concilios/index.html">← Bloco 09</a>
    <a href="/">365 de Graça & Adoração</a>
  </div></div>
  <div class="hero">
    <span class="tag">{subtitulo}</span>
    <h1>{titulo}</h1>
    <div class="ref">{ref}</div>
    <blockquote>{citacao}<br><small style="color:#64748b;font-size:0.8rem;font-style:normal;">— {autor_cit}</small></blockquote>
  </div>
  <div class="wrap">
    {corpo}
    <div class="nav-mod">
      <a href="{nav_prev}">{nav_prev_lbl}</a>
      <a href="/09-concilios/index.html">📋 Índice</a>
      <a href="{nav_next}">{nav_next_lbl}</a>
    </div>
  </div>
</body>
</html>"""


# ============================================================
# MÓDULO 1: OS 21 CONCÍLIOS ECUMÊNICOS
# ============================================================
concilios_corpo = """
<div class="sb">
  <h2>📜 O Que é um Concílio Ecumênico?</h2>
  <p>Um Concílio Ecumênico (do grego <em>oikoumenē</em> — "o mundo habitado") é uma assembleia representativa de bispos de toda a Igreja convocada para definir doutrina, disciplina ou organização eclesiástica. A palavra "ecumênico" não significa que todos os bispos do mundo estavam presentes — significa que o Concílio representa a Igreja universal, não apenas uma região. Os critérios de ecumenicidade variam entre as tradições: para a Igreja Católica, um Concílio é ecumênico quando é convocado e confirmado pelo Papa; para a Igreja Ortodoxa, os únicos Concílios verdadeiramente ecumênicos são os sete primeiros (325–787 d.C.), aceitos por toda a Igreja antes do Cisma de 1054.</p>
  <p>Os Concílios não criam a fé cristã — eles a articulam, defendem e transmitem. A doutrina trinitária e cristológica não foi inventada em Niceia ou Calcedônia: ela estava implícita nas Escrituras e na tradição apostólica desde o início. O que os Concílios fizeram foi tornar explícito o que estava implícito, usando a linguagem filosófica grega para expressar verdades bíblicas com precisão suficiente para excluir as heresias. Esta tarefa foi necessária — mas também arriscada: a linguagem filosófica pode distorcer tanto quanto clarificar.</p>
</div>
<div class="sb">
  <h2>📊 Os 21 Concílios Ecumênicos Católicos</h2>
  <table>
    <tr><th>#</th><th>Concílio</th><th>Ano</th><th>Tema Principal</th></tr>
    <tr><td>1</td><td>Niceia I</td><td>325</td><td>Divindade de Cristo — contra o Arianismo</td></tr>
    <tr><td>2</td><td>Constantinopla I</td><td>381</td><td>Divindade do Espírito Santo — Trindade completa</td></tr>
    <tr><td>3</td><td>Éfeso</td><td>431</td><td>Maria como <em>Theotokos</em> — contra o Nestorianismo</td></tr>
    <tr><td>4</td><td>Calcedônia</td><td>451</td><td>Duas naturezas de Cristo — contra o Monofisismo</td></tr>
    <tr><td>5</td><td>Constantinopla II</td><td>553</td><td>Os Três Capítulos — questões cristológicas</td></tr>
    <tr><td>6</td><td>Constantinopla III</td><td>680–681</td><td>Duas vontades de Cristo — contra o Monotelismo</td></tr>
    <tr><td>7</td><td>Niceia II</td><td>787</td><td>Veneração de ícones — contra o Iconoclasmo</td></tr>
    <tr><td>8</td><td>Constantinopla IV</td><td>869–870</td><td>Deposição do Patriarca Fócio</td></tr>
    <tr><td>9</td><td>Latrão I</td><td>1123</td><td>Concordata de Worms — investidura clerical</td></tr>
    <tr><td>10</td><td>Latrão II</td><td>1139</td><td>Cisma de Anacleto II — reforma clerical</td></tr>
    <tr><td>11</td><td>Latrão III</td><td>1179</td><td>Eleição papal — combate ao Catarismo</td></tr>
    <tr><td>12</td><td>Latrão IV</td><td>1215</td><td>Transubstanciação — confissão anual — Cruzada</td></tr>
    <tr><td>13</td><td>Lyon I</td><td>1245</td><td>Deposição do Imperador Frederico II</td></tr>
    <tr><td>14</td><td>Lyon II</td><td>1274</td><td>União com os Gregos — eleição papal</td></tr>
    <tr><td>15</td><td>Viena</td><td>1311–1312</td><td>Dissolução dos Templários</td></tr>
    <tr><td>16</td><td>Constança</td><td>1414–1418</td><td>Fim do Grande Cisma Ocidental — condenação de Hus</td></tr>
    <tr><td>17</td><td>Basileia/Ferrara/Florença</td><td>1431–1445</td><td>União com os Gregos — Conciliarismo vs. Papado</td></tr>
    <tr><td>18</td><td>Latrão V</td><td>1512–1517</td><td>Reforma da Igreja — véspera da Reforma Protestante</td></tr>
    <tr><td>19</td><td>Trento</td><td>1545–1563</td><td>Resposta à Reforma — doutrina e disciplina católica</td></tr>
    <tr><td>20</td><td>Vaticano I</td><td>1869–1870</td><td>Infalibilidade papal — primado de jurisdição</td></tr>
    <tr><td>21</td><td>Vaticano II</td><td>1962–1965</td><td>Igreja no mundo moderno — ecumenismo — liturgia</td></tr>
  </table>
</div>
<div class="sb">
  <h2>⚖️ Autoridade dos Concílios — Perspectivas Diferentes</h2>
  <div class="bloco">
    <div class="bt">Perspectiva Católica</div>
    <div class="bx">Os 21 Concílios listados acima são ecumênicos e seus ensinamentos dogmáticos são infalíveis quando confirmados pelo Papa. A autoridade dos Concílios deriva da assistência do Espírito Santo prometida por Cristo à Igreja. O Papa tem autoridade para convocar, presidir e confirmar os Concílios — sem confirmação papal, um Concílio não é ecumênico.</div>
  </div>
  <div class="bloco">
    <div class="bt">Perspectiva Ortodoxa</div>
    <div class="bx">Apenas os sete primeiros Concílios (325–787) são verdadeiramente ecumênicos, pois foram aceitos por toda a Igreja antes do Cisma de 1054. Os Concílios posteriores são concílios ocidentais, não ecumênicos. A autoridade de um Concílio é confirmada pela sua recepção pela Igreja toda — não pela aprovação papal.</div>
  </div>
  <div class="bloco">
    <div class="bt">Perspectiva Protestante</div>
    <div class="bx">Os Concílios têm autoridade derivada — eles são válidos na medida em que articulam fielmente o ensinamento das Escrituras. As definições trinitárias e cristológicas dos primeiros quatro Concílios são amplamente aceitas. Os Concílios podem errar — a <em>Sola Scriptura</em> significa que a Escritura é a autoridade suprema à qual os Concílios devem ser submetidos.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: O Espírito Santo e os Concílios</h3>
    <p>O Concílio de Jerusalém (Atos 15) é o modelo bíblico de deliberação eclesial. Os apóstolos e presbíteros se reuniram, debateram, ouviram testemunhos e chegaram a uma decisão que expressaram com as palavras: "Pareceu bem ao Espírito Santo e a nós" (At 15:28). Esta fórmula revela a convicção de que a deliberação humana, quando conduzida com oração e fidelidade às Escrituras, pode ser guiada pelo Espírito Santo. Os grandes Concílios da história da Igreja foram momentos em que a Igreja, diante de crises teológicas graves, buscou articular a fé apostólica com precisão e fidelidade — e, apesar de todas as suas limitações humanas, produziu definições que têm guiado a Igreja por séculos.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 2: NICEIA
# ============================================================
niceia_corpo = """
<div class="sb">
  <h2>⭐ O Contexto de Niceia</h2>
  <p>O Concílio de Niceia (325 d.C.) foi o primeiro Concílio Ecumênico da história da Igreja e um dos eventos mais importantes do Cristianismo. Ele foi convocado pelo Imperador Constantino I — o primeiro imperador romano a abraçar o Cristianismo — para resolver a crise teológica provocada pelo Arianismo. O Concílio reuniu aproximadamente 318 bispos de todo o Império Romano, a maioria do Oriente grego, em Niceia (atual Iznik, na Turquia).</p>
  <p>O contexto histórico é crucial: Constantino havia acabado de unificar o Império Romano após décadas de guerra civil. Para ele, a unidade religiosa era essencial para a unidade política. A disputa entre Ário e Alexandre de Alexandria ameaçava dividir a Igreja — e, por extensão, o Império. Constantino convocou o Concílio não como teólogo, mas como estadista: ele queria paz religiosa, não necessariamente verdade teológica. Esta ambiguidade entre fé e política marcará todos os Concílios subsequentes.</p>
</div>
<div class="sb">
  <h2>⚡ O Arianismo — A Heresia que Provocou Niceia</h2>
  <div class="bloco">
    <div class="bt">Quem foi Ário?</div>
    <div class="bx">Ário (c. 256–336 d.C.) era um presbítero de Alexandria, Egito, discípulo do teólogo Luciano de Antioquia. Era um pregador carismático e popular, conhecido por sua piedade pessoal e por compor hinos teológicos que tornavam suas ideias acessíveis ao povo. Sua heresia não era motivada por má-fé, mas por uma tentativa sincera de proteger a unicidade de Deus contra o que ele percebia como politeísmo disfarçado.</div>
  </div>
  <div class="bloco">
    <div class="bt">O Que Ário Ensinava</div>
    <div class="bx">Ário ensinava que o Filho de Deus era uma criatura — a mais elevada de todas as criaturas, mas ainda assim criatura. Sua frase mais famosa era: <em>"Houve um tempo em que o Filho não existia"</em> (<em>ēn pote hote ouk ēn</em>). Para Ário, o Filho foi criado pelo Pai antes de toda a criação — ele é o instrumento pelo qual Deus criou o mundo, mas não é eterno nem da mesma substância que o Pai. O Filho é divino em um sentido derivado e subordinado — não no sentido pleno e essencial. Esta visão era atraente porque parecia preservar a unicidade de Deus e explicar as passagens bíblicas que descrevem o Filho como subordinado ao Pai (Jo 14:28; 1 Co 15:28).</div>
  </div>
  <div class="bloco">
    <div class="bt">Por Que o Arianismo é Heresia</div>
    <div class="bx">A Igreja rejeitou o Arianismo porque ele esvazia o Evangelho. Se Cristo é uma criatura — mesmo a mais elevada — então ele não pode salvar. Apenas Deus pode salvar; uma criatura não pode ser o mediador entre Deus e a humanidade. Atanásio de Alexandria, o grande defensor da ortodoxia nicena, argumentou: "Deus se fez homem para que o homem se tornasse Deus" — a salvação como participação na natureza divina (<em>theosis</em>) pressupõe que Cristo seja verdadeiramente Deus. Além disso, se adoramos Cristo (como a Igreja sempre fez), e Cristo é uma criatura, então somos idólatras. A divindade de Cristo não é um luxo teológico — é o fundamento da adoração e da salvação cristã.</div>
  </div>
</div>
<div class="sb">
  <h2>🏛️ O Concílio e o <em>Homoousios</em></h2>
  <p>O debate central em Niceia foi sobre o termo <em>homoousios</em> (grego: "da mesma substância" ou "consubstancial"). Os defensores da ortodoxia, liderados por Alexandre de Alexandria e seu jovem diácono Atanásio, propuseram que o Credo afirmasse que o Filho é <em>homoousios</em> com o Pai — da mesma substância, da mesma essência divina. Os arianos propuseram <em>homoiousios</em> ("de substância semelhante") — uma diferença de apenas uma letra (iota) que, no entanto, fazia toda a diferença teológica.</p>
  <p>O Concílio adotou o <em>homoousios</em> por uma maioria esmagadora — apenas dois bispos recusaram assinar o Credo. Constantino exilou os recalcitrantes. A vitória nicena, porém, foi temporária: nas décadas seguintes, o Arianismo ressurgiu com força, apoiado por imperadores arianos. Atanásio foi exilado cinco vezes por imperadores arianos — daí o dito <em>Athanasius contra mundum</em> ("Atanásio contra o mundo"). Apenas com o Concílio de Constantinopla (381) o Arianismo foi definitivamente derrotado no Império Romano.</p>
</div>
<div class="sb">
  <h2>📜 O Credo Niceno</h2>
  <div class="credo-box">
    <div class="credo-titulo">Credo de Niceia (325 d.C.) — versão original</div>
    Cremos em um só Deus, Pai todo-poderoso, criador de todas as coisas visíveis e invisíveis.<br><br>
    E em um só Senhor Jesus Cristo, Filho de Deus, gerado unigênito do Pai, isto é, da substância do Pai, Deus de Deus, Luz de Luz, Deus verdadeiro de Deus verdadeiro, gerado, não criado, <strong>consubstancial ao Pai</strong> (<em>homoousios tō Patri</em>), por quem todas as coisas foram feitas, tanto as do céu como as da terra; que por nós homens e por nossa salvação desceu e se encarnou, se fez homem, sofreu e ressuscitou ao terceiro dia, subiu aos céus, e virá para julgar os vivos e os mortos.<br><br>
    E no Espírito Santo.<br><br>
    <em>Mas os que dizem: "Houve um tempo em que ele não existia", e "Antes de ser gerado não existia", e "Ele foi feito do nada" ou "é de outra substância ou essência", ou "o Filho de Deus é criado, mutável ou variável" — esses a Igreja Católica anatematiza.</em>
  </div>
</div>
<div class="sb">
  <h2>🌍 Consequências de Niceia</h2>
  <div class="bloco">
    <div class="bt">Para a Doutrina</div>
    <div class="bx">Niceia estabeleceu o vocabulário trinitário que a Igreja usa até hoje: <em>homoousios</em>, substância, essência, pessoa. Ela tornou claro que a fé cristã não é monoteísmo simples (um Deus solitário), nem politeísmo (três deuses), mas Trindade — um Deus em três pessoas. Esta definição foi completada pelo Concílio de Constantinopla (381), que afirmou a divindade do Espírito Santo e produziu o Credo Niceno-Constantinopolitano que usamos até hoje.</div>
  </div>
  <div class="bloco">
    <div class="bt">Para a Relação Igreja-Estado</div>
    <div class="bx">Niceia estabeleceu um precedente perigoso: o Imperador convocando e presidindo um Concílio da Igreja. Esta fusão de poder imperial e autoridade eclesiástica — o Cesaropapismo — tornou-se um problema recorrente na história da Igreja, especialmente no Oriente. O Imperador usava a Igreja para fins políticos; a Igreja usava o Imperador para fins eclesiásticos. Esta relação ambígua gerou tanto proteção quanto corrupção para a Igreja.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: Por Que a Divindade de Cristo Importa?</h3>
    <p>A batalha de Niceia não foi uma disputa acadêmica sobre filosofia grega — foi uma batalha pelo coração do Evangelho. Se Cristo é uma criatura, então a salvação é obra de uma criatura, não de Deus. Se Cristo é Deus, então quando ele morreu na cruz, foi Deus mesmo que pagou o preço do nosso pecado. "Deus estava em Cristo reconciliando consigo o mundo" (2 Co 5:19) — esta afirmação de Paulo pressupõe a divindade de Cristo. Niceia não adicionou nada ao Evangelho — ela protegeu o Evangelho contra uma distorção que o teria esvaziado.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 3: CONSTANTINOPLA
# ============================================================
const_corpo = """
<div class="sb">
  <h2>🕊️ O Contexto de Constantinopla I (381)</h2>
  <p>O Concílio de Constantinopla I (381 d.C.) foi convocado pelo Imperador Teodósio I para completar a obra de Niceia. Embora menor que Niceia em número de participantes (cerca de 150 bispos, todos do Oriente), foi de importância teológica igual. Seu principal resultado foi a completação do Credo Niceno com a afirmação da divindade do Espírito Santo e a condenação do Macedonianismo (também chamado de Pneumatômaco — "lutadores contra o Espírito").</p>
  <p>O contexto histórico é o de uma Igreja que havia passado por décadas de turbulência ariana. O Imperador Constâncio II (filho de Constantino) era ariano e havia perseguido os defensores de Niceia. Atanásio de Alexandria foi exilado cinco vezes. Apenas com a morte de Constâncio e a ascensão de Teodósio I — um cristão niceno convicto — a ortodoxia trinitária foi restaurada como posição oficial do Império.</p>
</div>
<div class="sb">
  <h2>⚡ O Macedonianismo — A Heresia do Espírito</h2>
  <div class="bloco">
    <div class="bt">A Posição Macedoniana</div>
    <div class="bx">Os Macedonianos (seguidores do Bispo Macedônio de Constantinopla, deposto em 360) aceitavam a divindade do Filho conforme definida em Niceia, mas negavam a divindade do Espírito Santo. Para eles, o Espírito era uma criatura — inferior ao Pai e ao Filho, um ministro ou servo divino, mas não Deus. Esta posição era atraente para quem havia aceitado Niceia mas resistia ao que parecia ser uma "trindade de deuses." Se o Filho é Deus, e o Espírito é Deus, não teríamos três deuses?</div>
  </div>
  <div class="bloco">
    <div class="bt">A Resposta dos Capadócios</div>
    <div class="bx">A resposta teológica ao Macedonianismo foi desenvolvida pelos três grandes teólogos capadócios: Basílio de Cesareia, Gregório de Nissa (seu irmão) e Gregório de Nazianzo. Eles desenvolveram a distinção crucial entre <em>ousia</em> (essência ou substância — o que Deus é) e <em>hypostasis</em> (pessoa — quem Deus é). Há uma única <em>ousia</em> divina (Deus é um), mas três <em>hypostaseis</em> (o Pai, o Filho e o Espírito Santo são três pessoas distintas). Esta distinção permitiu afirmar tanto a unidade de Deus quanto a distinção real das três pessoas — sem cair no triteísmo (três deuses) nem no modalismo (um Deus que se manifesta de três formas).</div>
  </div>
</div>
<div class="sb">
  <h2>👤 Gregório de Nazianzo — O Teólogo da Trindade</h2>
  <div class="pers-grid">
    <div class="pers-card">
      <div class="pers-nome">Basílio de Cesareia</div>
      <div class="pers-datas">330–379 d.C. · Capadócia</div>
      <div class="pers-desc">Bispo de Cesareia, organizador do monaquismo oriental. Seu tratado <em>Sobre o Espírito Santo</em> (375) foi a defesa mais rigorosa da divindade do Espírito antes do Concílio. Morreu antes de ver a vitória em Constantinopla.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Gregório de Nazianzo</div>
      <div class="pers-datas">329–390 d.C. · Capadócia</div>
      <div class="pers-desc">Chamado "o Teólogo" pela tradição ortodoxa — título dado apenas a João Evangelista e a ele. Presidiu o início do Concílio de Constantinopla. Seus cinco Discursos Teológicos são a exposição mais brilhante da doutrina trinitária da Antiguidade.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Gregório de Nissa</div>
      <div class="pers-datas">335–395 d.C. · Capadócia</div>
      <div class="pers-desc">Irmão de Basílio, o mais especulativo dos três Capadócios. Desenvolveu a distinção <em>ousia/hypostasis</em> com maior rigor filosófico. Sua obra <em>Contra Eunômio</em> é a refutação mais completa do Arianismo radical.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Atanásio de Alexandria</div>
      <div class="pers-datas">296–373 d.C. · Egito</div>
      <div class="pers-desc">O grande herói de Niceia. Exilado cinco vezes por imperadores arianos. Sua frase <em>Athanasius contra mundum</em> ("Atanásio contra o mundo") resume sua resistência solitária. Não viveu para ver Constantinopla, mas sua obra preparou o caminho.</div>
    </div>
  </div>
</div>
<div class="sb">
  <h2>📜 O Credo Niceno-Constantinopolitano</h2>
  <div class="credo-box">
    <div class="credo-titulo">Credo Niceno-Constantinopolitano (381 d.C.) — usado até hoje</div>
    Creio em um só Deus, Pai todo-poderoso, criador do céu e da terra, de todas as coisas visíveis e invisíveis.<br><br>
    Creio em um só Senhor, Jesus Cristo, Filho Unigênito de Deus, nascido do Pai antes de todos os séculos: Deus de Deus, Luz da Luz, Deus verdadeiro de Deus verdadeiro; gerado, não criado, <strong>consubstancial ao Pai</strong>. Por ele todas as coisas foram feitas. E por nós, homens, e para nossa salvação, desceu dos céus: e se encarnou pelo Espírito Santo, no seio da Virgem Maria, e se fez homem. Também por nós foi crucificado sob Pôncio Pilatos; padeceu e foi sepultado. Ressuscitou ao terceiro dia, conforme as Escrituras; subiu aos céus, está sentado à direita do Pai. E de novo há de vir, em sua glória, para julgar os vivos e os mortos; e o seu reino não terá fim.<br><br>
    <strong>Creio no Espírito Santo, Senhor que dá a vida, e procede do Pai [e do Filho*]; com o Pai e o Filho é adorado e glorificado conjuntamente; ele que falou pelos profetas.</strong><br><br>
    Creio na Igreja una, santa, católica e apostólica. Professo um só batismo para a remissão dos pecados. Espero a ressurreição dos mortos e a vida do século vindouro. Amém.<br><br>
    <em>* O "e do Filho" (Filioque) foi adicionado pelo Ocidente no séc. VI — causa do Cisma de 1054.</em>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: O Espírito Santo é Deus</h3>
    <p>A afirmação de que o Espírito Santo é "Senhor que dá a vida" e deve ser "adorado e glorificado conjuntamente" com o Pai e o Filho é uma das mais importantes da fé cristã. Ela significa que quando o Espírito age em nós — convencendo-nos do pecado, regenerando-nos, habitando em nós, guiando-nos — é o próprio Deus que age. A vida cristã não é apenas imitação de Cristo (o que uma criatura poderia fazer); é participação na vida trinitária de Deus pelo Espírito Santo. "Não sabeis que sois templo de Deus e que o Espírito de Deus habita em vós?" (1 Co 3:16) — esta afirmação de Paulo só faz sentido pleno se o Espírito é Deus.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 4: ÉFESO E CALCEDÔNIA
# ============================================================
efeso_corpo = """
<div class="sb">
  <h2>✝️ A Questão Cristológica</h2>
  <p>Após Niceia e Constantinopla definirem que Cristo é verdadeiramente Deus e que o Espírito Santo é verdadeiramente Deus, a questão seguinte era inevitável: como o Filho de Deus eterno se relaciona com o homem Jesus de Nazaré? Como a divindade e a humanidade coexistem em uma única pessoa? Esta questão cristológica dominou o século V e produziu dois Concílios fundamentais: Éfeso (431) e Calcedônia (451).</p>
  <p>As heresias cristológicas do século V não eram invenções maliciosas — eram tentativas sinceras de resolver um paradoxo genuíno. Como pode o eterno ser temporal? Como pode o imutável sofrer? Como pode o onipresente estar localizado em um corpo? As respostas heréticas simplificavam o paradoxo: ou separando as duas naturezas em duas pessoas (Nestorianismo), ou fundindo-as em uma única natureza (Monofisismo). A resposta ortodoxa de Calcedônia manteve o paradoxo — e foi acusada de ser incoerente por isso.</p>
</div>
<div class="sb">
  <h2>⚡ O Nestorianismo e o Concílio de Éfeso (431)</h2>
  <div class="bloco">
    <div class="bt">Nestório e o Problema de Maria</div>
    <div class="bx">Nestório (c. 386–451), Patriarca de Constantinopla, recusou o título de <em>Theotokos</em> ("Mãe de Deus") para Maria, preferindo <em>Christotokos</em> ("Mãe de Cristo"). Para Nestório, Maria deu à luz o homem Jesus — não o Deus eterno. Ele temia que chamar Maria de "Mãe de Deus" fosse confundir as duas naturezas de Cristo. Sua posição implicava que havia dois sujeitos em Cristo: o Filho de Deus eterno e o homem Jesus — unidos moralmente, mas não ontologicamente.</div>
  </div>
  <div class="bloco">
    <div class="bt">Cirilo de Alexandria e a Resposta Ortodoxa</div>
    <div class="bx">Cirilo de Alexandria (376–444) foi o grande adversário de Nestório. Para Cirilo, a unidade de Cristo é real e ontológica — não apenas moral. O sujeito que nasceu de Maria, que cresceu, que sofreu, que morreu e ressuscitou é o mesmo sujeito: o Filho eterno de Deus. Por isso, Maria é legitimamente chamada de <em>Theotokos</em> — não porque ela seja a origem da divindade de Cristo, mas porque o filho que ela gerou é o Filho de Deus encarnado. A comunicação de idiomas (<em>communicatio idiomatum</em>) — a atribuição das propriedades de uma natureza ao sujeito único — é a consequência lógica desta unidade.</div>
  </div>
  <div class="bloco">
    <div class="bt">O Concílio de Éfeso (431)</div>
    <div class="bx">O Concílio de Éfeso foi marcado por intrigas políticas e até violência. Cirilo chegou com seus bispos egípcios antes da delegação de Nestório e abriu o Concílio sem esperar pelos orientais. Nestório foi condenado e exilado. Quando os bispos orientais chegaram, abriram seu próprio concílio e condenaram Cirilo. O Imperador Teodósio II prendeu ambos os líderes. Eventualmente, um compromisso foi alcançado: o "Símbolo de União" (433) afirmou que Cristo é "perfeito em divindade e perfeito em humanidade" e que Maria é legitimamente chamada de <em>Theotokos</em>.</div>
  </div>
</div>
<div class="sb">
  <h2>⚡ O Monofisismo e o Concílio de Calcedônia (451)</h2>
  <div class="bloco">
    <div class="bt">Eutiques e o Monofisismo</div>
    <div class="bx">Eutiques (c. 380–456), arquimandrita de Constantinopla, foi ao extremo oposto de Nestório. Para ele, após a encarnação, Cristo tinha apenas uma natureza — a divina havia absorvido a humana "como uma gota de mel no oceano." Esta posição — o Monofisismo (do grego <em>monos</em> = um, <em>physis</em> = natureza) — preservava a unidade de Cristo, mas ao custo de sua humanidade real. Se Cristo não é verdadeiramente humano, ele não pode ser nosso representante e substituto; sua morte não seria a morte de um ser humano.</div>
  </div>
  <div class="bloco">
    <div class="bt">A Definição de Calcedônia</div>
    <div class="bx">O Concílio de Calcedônia (451), com cerca de 600 bispos, produziu a definição cristológica mais precisa da história: Cristo é "uma e a mesma pessoa em duas naturezas, sem confusão, sem mudança, sem divisão, sem separação." Os quatro advérbios negativos são o coração da definição: <em>sem confusão</em> (contra o Monofisismo — as naturezas não se fundem); <em>sem mudança</em> (contra o Monofisismo — a natureza humana não é transformada em divina); <em>sem divisão</em> (contra o Nestorianismo — não há dois sujeitos); <em>sem separação</em> (contra o Nestorianismo — as naturezas não são independentes). A definição é apofática — diz o que Cristo não é, mais do que o que ele é.</div>
  </div>
</div>
<div class="sb">
  <h2>📊 As Divisões Cristológicas e Suas Consequências</h2>
  <table>
    <tr><th>Posição</th><th>Naturezas</th><th>Pessoas</th><th>Heresia</th><th>Igrejas Hoje</th></tr>
    <tr><td>Nestorianismo</td><td>Duas separadas</td><td>Duas</td><td>Sim — Éfeso 431</td><td>Igreja Assíria do Oriente</td></tr>
    <tr><td>Monofisismo</td><td>Uma (divina)</td><td>Uma</td><td>Sim — Calcedônia 451</td><td>Copta, Etíope, Armênia, Síria Ocidental</td></tr>
    <tr><td>Calcedônia (Ortodoxia)</td><td>Duas unidas</td><td>Uma</td><td>Não</td><td>Católica, Ortodoxa, Protestante</td></tr>
  </table>
  <div class="reflexao">
    <h3>🙏 Reflexão: Por Que a Humanidade de Cristo Importa?</h3>
    <p>A definição de Calcedônia afirma que Cristo é "perfeito em humanidade, verdadeiramente homem, composto de alma racional e corpo." Esta afirmação não é apenas teológica — é pastoral. Hebreus 4:15 diz: "Não temos um sumo sacerdote que não possa compadecer-se das nossas fraquezas; pelo contrário, temos um que foi tentado em tudo como nós, mas sem pecado." Cristo não apenas sabe sobre o sofrimento humano — ele o viveu. Ele chorou diante do túmulo de Lázaro (Jo 11:35). Ele sentiu fome, cansaço, solidão, abandono. Quando oramos a Cristo em nosso sofrimento, oramos a alguém que sabe por experiência própria o que é sofrer. Calcedônia protegeu esta verdade consoladora.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 5: TRENTO
# ============================================================
trento_corpo = """
<div class="sb">
  <h2>🏰 O Contexto de Trento</h2>
  <p>O Concílio de Trento (1545–1563) foi a resposta da Igreja Católica à Reforma Protestante — o maior desafio que a Igreja havia enfrentado desde as heresias cristológicas do século V. Convocado pelo Papa Paulo III, o Concílio se reuniu em três períodos distintos ao longo de 18 anos na cidade de Trento (atual Trento, norte da Itália). Foi o Concílio mais longo da história e o que produziu o maior volume de definições dogmáticas e reformas disciplinares.</p>
  <p>O Concílio de Trento foi ao mesmo tempo uma resposta à Reforma e uma reforma genuína da Igreja Católica. Ele reafirmou as doutrinas contestadas pelos protestantes — mas também reconheceu os abusos que haviam provocado a Reforma e promoveu reformas disciplinares significativas. Trento não foi apenas uma reação defensiva — foi uma renovação que transformou o Catolicismo para os séculos seguintes.</p>
</div>
<div class="sb">
  <h2>⚖️ As Grandes Definições Dogmáticas de Trento</h2>
  <div class="bloco">
    <div class="bt">Escritura e Tradição</div>
    <div class="bx">Contra a <em>Sola Scriptura</em> protestante, Trento afirmou que a revelação divina está contida tanto nas Escrituras quanto na Tradição apostólica não escrita, e que ambas devem ser recebidas "com igual afeto de piedade e reverência." A Vulgata latina foi declarada a versão oficial da Bíblia para uso litúrgico e teológico. O Cânon bíblico católico (incluindo os deuterocanônicos/apócrifos) foi definido. Esta decisão aprofundou o fosso com os protestantes, que aceitam apenas o Cânon hebraico (sem os deuterocanônicos).</div>
  </div>
  <div class="bloco">
    <div class="bt">Justificação — A Questão Central</div>
    <div class="bx">O decreto sobre a justificação (Sessão VI, 1547) foi o mais elaborado e teologicamente rico de Trento. Contra a <em>Sola Fide</em> protestante, Trento afirmou que a justificação envolve tanto a fé quanto as obras — não como mérito independente, mas como cooperação com a graça. A justificação não é apenas a declaração forense de que o pecador é justo (posição protestante), mas a renovação interior do pecador pela graça. A graça é necessária e suficiente para a salvação — mas o ser humano coopera com ela livremente. Esta posição rejeita tanto o Pelagianismo (salvação pelas obras sem graça) quanto o que Trento entendia ser o determinismo protestante (salvação sem cooperação humana).</div>
  </div>
  <div class="bloco">
    <div class="bt">Os Sete Sacramentos</div>
    <div class="bx">Contra a redução protestante a dois sacramentos (Batismo e Ceia do Senhor), Trento reafirmou os sete sacramentos: Batismo, Confirmação, Eucaristia, Penitência, Unção dos Enfermos, Ordem e Matrimônio. A transubstanciação — a doutrina de que o pão e o vinho se tornam o corpo e o sangue de Cristo na Eucaristia — foi reafirmada com precisão filosófica. A Missa foi definida como sacrifício propiciatório — não uma repetição do sacrifício da cruz, mas uma representação sacramental do único sacrifício de Cristo.</div>
  </div>
  <div class="bloco">
    <div class="bt">Purgatório, Indulgências e Invocação dos Santos</div>
    <div class="bx">Trento reafirmou a doutrina do purgatório e a legitimidade das indulgências — mas proibiu o comércio de indulgências que havia provocado a ira de Lutero. A invocação dos santos e a veneração de relíquias e imagens foram reafirmadas como práticas legítimas, mas com advertências contra os abusos. Estas definições aprofundaram as divisões com os protestantes, que rejeitam o purgatório e a invocação dos santos como sem fundamento bíblico.</div>
  </div>
</div>
<div class="sb">
  <h2>🔧 As Reformas Disciplinares de Trento</h2>
  <p>Além das definições dogmáticas, Trento promoveu reformas disciplinares que transformaram a Igreja Católica. A criação de seminários diocesanos para a formação do clero foi talvez a reforma mais importante: antes de Trento, muitos padres eram ignorantes e mal formados; depois de Trento, a formação clerical tornou-se sistemática e rigorosa. O absenteísmo episcopal foi combatido: bispos foram obrigados a residir em suas dioceses. O nepotismo e a simonia foram proibidos. O casamento foi regulamentado: passou a exigir a presença de um padre e duas testemunhas para ser válido.</p>
  <p>O Catecismo Romano (1566), o Missal Romano (1570) e o Breviário Romano (1568) — todos produzidos após Trento — padronizaram a liturgia e o ensino católico em todo o mundo. Esta padronização foi tanto uma força (unidade e clareza) quanto uma fraqueza (rigidez e uniformidade que sufocou a diversidade legítima). O Missal de Trento permaneceu em uso por quase 400 anos, até ser reformado pelo Concílio Vaticano II.</p>
  <div class="reflexao">
    <h3>🙏 Reflexão: Reforma e Contra-Reforma</h3>
    <p>O Concílio de Trento é um exemplo de como a crise pode ser um catalisador de renovação. A Reforma Protestante foi um choque para a Igreja Católica — mas também foi um espelho que revelou seus pecados e fraquezas. Trento não teria acontecido sem Lutero. A renovação que Trento promoveu — seminários, residência episcopal, fim do comércio de indulgências — era necessária e legítima. O paradoxo é que muitas das reformas que Lutero pediu foram implementadas por Trento — mas tarde demais para evitar a divisão. Esta lição histórica é relevante para qualquer instituição: a reforma interna é sempre preferível à ruptura — mas só é possível quando há humildade suficiente para reconhecer os próprios erros.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 6: VATICANO I
# ============================================================
vat1_corpo = """
<div class="sb">
  <h2>👑 O Contexto do Vaticano I</h2>
  <p>O Primeiro Concílio do Vaticano (1869–1870) foi convocado pelo Papa Pio IX em um momento de crise profunda para a Igreja Católica. O Risorgimento italiano — o movimento de unificação da Itália — ameaçava os Estados Pontifícios, o território que a Igreja governava há mais de mil anos. O liberalismo político e o racionalismo filosófico desafiavam a autoridade da Igreja na esfera pública. O Modernismo teológico questionava a historicidade dos Evangelhos e a autoridade do magistério eclesiástico. Pio IX respondeu com o Syllabus Errorum (1864) — uma lista de 80 "erros modernos" condenados — e com a convocação do Vaticano I.</p>
  <p>O Vaticano I reuniu cerca de 700 bispos de todo o mundo. Foi o primeiro Concílio a incluir bispos de todos os continentes — um reflexo da expansão missionária católica do século XIX. O Concílio foi interrompido em julho de 1870 quando as tropas do Reino da Itália invadiram Roma e completaram a unificação italiana, pondo fim aos Estados Pontifícios. O Papa Pio IX se declarou "prisioneiro do Vaticano" e recusou-se a reconhecer o novo Estado italiano. Esta situação durou até 1929, quando os Tratados de Latrão criaram o Estado da Cidade do Vaticano.</p>
</div>
<div class="sb">
  <h2>📜 A Definição da Infalibilidade Papal</h2>
  <div class="bloco">
    <div class="bt">O Que é a Infalibilidade Papal?</div>
    <div class="bx">A constituição dogmática <em>Pastor Aeternus</em> (1870) definiu que o Papa, quando fala <em>ex cathedra</em> — "da cátedra" — sobre questões de fé e moral, com a intenção de vincular toda a Igreja, é preservado pelo Espírito Santo do erro. Esta infalibilidade não é pessoal (o Papa pode errar em questões científicas, históricas ou políticas) nem contínua (aplica-se apenas a definições dogmáticas formais). Ela é uma assistência do Espírito Santo que preserva a Igreja do erro em questões essenciais da fé.</div>
  </div>
  <div class="bloco">
    <div class="bt">As Condições da Infalibilidade</div>
    <div class="bx">Para que uma declaração papal seja infalível, ela deve satisfazer quatro condições: (1) deve ser feita pelo Papa como pastor supremo de toda a Igreja; (2) deve ser sobre questões de fé ou moral; (3) deve ser feita com a intenção explícita de vincular toda a Igreja; (4) deve ser uma definição final e definitiva. Estas condições são muito restritas: desde 1870, apenas duas definições papais foram feitas <em>ex cathedra</em>: a Imaculada Conceição (1854, antes do Concílio) e a Assunção de Maria (1950). Todas as demais declarações papais — encíclicas, exortações, discursos — não são infalíveis, embora mereçam respeito e obediência.</div>
  </div>
  <div class="bloco">
    <div class="bt">O Primado de Jurisdição</div>
    <div class="bx">Além da infalibilidade, o Vaticano I definiu o primado de jurisdição do Papa sobre toda a Igreja — não apenas uma primazia de honra, mas de governo real. O Papa tem "poder pleno e supremo de jurisdição sobre a Igreja universal, não apenas em questões de fé e moral, mas também em questões de disciplina e governo." Esta definição foi o ponto mais controverso do Concílio: ela foi rejeitada pelos Velhos Católicos (que se separaram da Igreja Católica em 1870) e permanece o principal obstáculo ao diálogo com as igrejas ortodoxas.</div>
  </div>
</div>
<div class="sb">
  <h2>⚖️ A Oposição ao Vaticano I</h2>
  <p>A definição da infalibilidade papal não foi unânime. Cerca de 55 bispos votaram contra e outros 70 se abstiveram ou abandonaram o Concílio antes da votação final. O cardeal John Henry Newman, embora não fosse bispo e não participasse do Concílio, expressou reservas sobre a oportunidade da definição — não sobre sua substância. O bispo alemão Joseph Georg Strossmayer fez um discurso eloquente contra a definição, argumentando que ela não tinha fundamento na tradição da Igreja primitiva.</p>
  <p>Os Velhos Católicos — um grupo de bispos e leigos alemães, suíços e austríacos — recusaram aceitar as definições do Vaticano I e formaram igrejas independentes. Eles mantêm a sucessão apostólica e os sacramentos católicos, mas rejeitam a infalibilidade papal e o primado de jurisdição. Hoje, as Igrejas Velhas Católicas fazem parte da União de Utrecht e têm plena comunhão com a Igreja Anglicana.</p>
  <div class="reflexao">
    <h3>🙏 Reflexão: Autoridade e Humildade</h3>
    <p>A doutrina da infalibilidade papal é um dos maiores obstáculos ao diálogo ecumênico. Para os protestantes, ela contradiz a <em>Sola Scriptura</em> — a Escritura é a única autoridade infalível. Para os ortodoxos, ela contradiz a autoridade dos Concílios Ecumênicos como expressão da fé da Igreja toda. Para os católicos, ela é a garantia de que a Igreja não pode errar em questões essenciais da fé. O debate sobre a infalibilidade toca em uma questão fundamental: onde está a autoridade última na Igreja? Esta questão não pode ser resolvida sem uma eclesiologia — uma teologia da Igreja — que leve a sério tanto a promessa de Cristo de guiar sua Igreja pelo Espírito Santo quanto a falibilidade humana de todos os seus líderes.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 7: VATICANO II
# ============================================================
vat2_corpo = """
<div class="sb">
  <h2>🌍 O Vaticano II — A Igreja se Abre ao Mundo</h2>
  <p>O Segundo Concílio do Vaticano (1962–1965) foi o maior Concílio da história da Igreja e um dos eventos mais importantes do século XX. Convocado pelo Papa João XXIII com a palavra de ordem <em>aggiornamento</em> ("atualização"), reuniu cerca de 2.500 bispos de todo o mundo em quatro sessões ao longo de três anos. Produziu 16 documentos — quatro constituições, nove decretos e três declarações — que transformaram a Igreja Católica de maneira profunda e duradoura.</p>
  <p>João XXIII surpreendeu o mundo ao convocar o Concílio em 1959 — apenas três meses após sua eleição. Ele era um Papa idoso (77 anos) que muitos esperavam que fosse um "papa de transição." Em vez disso, ele lançou a maior renovação da Igreja Católica desde Trento. Sua visão era a de uma Igreja que se abrisse ao mundo moderno não para capitular a ele, mas para dialogar com ele — para encontrar "os sinais dos tempos" e responder ao Evangelho às necessidades do mundo contemporâneo.</p>
</div>
<div class="sb">
  <h2>📜 Os Quatro Documentos Fundamentais</h2>
  <div class="bloco">
    <div class="bt">Sacrosanctum Concilium — A Constituição sobre a Liturgia</div>
    <div class="bx">A reforma litúrgica foi a mudança mais visível do Vaticano II. A Missa passou a ser celebrada em vernáculo (a língua do povo) em vez do latim. O altar foi virado para o povo. A participação ativa dos fiéis foi enfatizada. As leituras bíblicas foram ampliadas (o Lecionário trienal). Estas reformas foram recebidas com entusiasmo por muitos e com resistência por outros — incluindo o Arcebispo Marcel Lefebvre, que fundou a Fraternidade São Pio X em oposição à nova liturgia. O debate sobre a reforma litúrgica continua até hoje.</div>
  </div>
  <div class="bloco">
    <div class="bt">Lumen Gentium — A Constituição sobre a Igreja</div>
    <div class="bx">A <em>Lumen Gentium</em> foi a mais importante renovação eclesiológica desde o Vaticano I. Ela apresentou a Igreja como "Povo de Deus" — antes de ser hierarquia, a Igreja é a comunidade de todos os batizados. Ela afirmou a colegialidade episcopal — os bispos governam a Igreja em colégio com o Papa, não apenas como delegados papais. Ela reconheceu que a Igreja de Cristo "subsiste" na Igreja Católica — mas não se identifica exclusivamente com ela, deixando espaço para reconhecer elementos da Igreja de Cristo em outras comunidades cristãs.</div>
  </div>
  <div class="bloco">
    <div class="bt">Dei Verbum — A Constituição sobre a Revelação</div>
    <div class="bx">A <em>Dei Verbum</em> foi um avanço significativo na teologia bíblica católica. Ela afirmou que a Escritura e a Tradição formam "um único depósito sagrado da Palavra de Deus." Ela encorajou o estudo bíblico usando os métodos histórico-críticos — uma abertura que havia sido resistida desde a crise modernista do início do século XX. Ela afirmou que os hagiógrafos (autores humanos da Bíblia) são "verdadeiros autores" — não meros secretários do Espírito Santo — o que implica que seus escritos devem ser interpretados levando em conta seu contexto histórico e literário.</div>
  </div>
  <div class="bloco">
    <div class="bt">Gaudium et Spes — A Igreja no Mundo Moderno</div>
    <div class="bx">A <em>Gaudium et Spes</em> foi o documento mais inovador do Vaticano II — e o mais controverso. Ela abriu a Igreja ao diálogo com o mundo moderno: com a ciência, a cultura, a política, a economia. Ela afirmou a dignidade da pessoa humana, o valor da família, a importância do trabalho, a responsabilidade da Igreja pela paz e pela justiça social. Ela reconheceu que a Igreja aprende com o mundo, não apenas ensina. Esta abertura foi recebida como libertadora por muitos e como perigosa por outros — o debate sobre a hermenêutica do Vaticano II (continuidade ou ruptura com a tradição?) continua até hoje.</div>
  </div>
</div>
<div class="sb">
  <h2>🕊️ Ecumenismo e Liberdade Religiosa</h2>
  <p>O decreto <em>Unitatis Redintegratio</em> sobre o ecumenismo foi uma revolução na posição católica em relação às outras igrejas cristãs. Antes do Vaticano II, a posição oficial era que as igrejas separadas de Roma eram simplesmente "seitas" sem salvação. Após o Vaticano II, a Igreja reconheceu que as comunidades cristãs separadas "não estão de modo algum desprovidas de significado e de importância no mistério da salvação" e que há "elementos de santificação e de verdade" fora dos limites visíveis da Igreja Católica.</p>
  <p>A declaração <em>Dignitatis Humanae</em> sobre a liberdade religiosa foi talvez a mais controversa do Vaticano II. Ela afirmou que toda pessoa tem o direito de seguir sua consciência em matéria religiosa e que o Estado não pode coagir ninguém em questões de fé. Esta declaração foi uma reversão da posição tradicional da Igreja, que havia defendido a confessionalidade do Estado católico. Ela foi atacada pelos tradicionalistas como contradição da tradição e celebrada pelos progressistas como reconhecimento tardio de um direito humano fundamental.</p>
  <div class="reflexao">
    <h3>🙏 Reflexão: O Vaticano II e os Evangélicos</h3>
    <p>O Vaticano II é frequentemente ignorado ou mal compreendido pelos cristãos evangélicos. Mas ele contém afirmações que deveriam interessar a qualquer cristão comprometido com as Escrituras: a centralidade da Palavra de Deus na vida da Igreja, a importância da participação ativa dos fiéis na liturgia, o reconhecimento da dignidade de todas as pessoas criadas à imagem de Deus, o compromisso com a paz e a justiça social. O Vaticano II não resolveu todas as diferenças entre católicos e protestantes — mas abriu um espaço de diálogo que não existia antes. Para o cristão evangélico, estudar o Vaticano II é entender melhor o maior parceiro de diálogo ecumênico do mundo.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 8: PATRÍSTICA
# ============================================================
patrist_corpo = """
<div class="sb">
  <h2>📖 O Que é a Patrística?</h2>
  <p>A Patrística (do latim <em>pater</em> — pai) é o estudo dos escritos e do pensamento dos Pais da Igreja — os teólogos e líderes cristãos dos primeiros séculos que desenvolveram a teologia cristã e defenderam a fé contra as heresias. O período patrístico se estende aproximadamente do século I ao século VIII — dos escritos apostólicos até João Damasceno no Oriente e Isidoro de Sevilha no Ocidente. Os Pais da Igreja não são infalíveis — eles erraram em questões individuais — mas representam a tradição teológica mais próxima dos apóstolos e são testemunhas preciosas da fé da Igreja primitiva.</p>
  <p>A Patrística é dividida em períodos: os Pais Apostólicos (discípulos diretos dos apóstolos, séc. I–II), os Apologistas (séc. II), os Pais Antenicenos (séc. II–III), os Pais Nicenos (séc. IV) e os Pais Pós-Nicenos (séc. V–VIII). Ela também é dividida geograficamente: os Pais Gregos (Oriente) e os Pais Latinos (Ocidente) — uma divisão que reflete as diferenças culturais e linguísticas que eventualmente contribuiriam para o Cisma de 1054.</p>
</div>
<div class="sb">
  <h2>👤 Os Grandes Pais da Igreja</h2>
  <div class="pers-grid">
    <div class="pers-card">
      <div class="pers-nome">Inácio de Antioquia</div>
      <div class="pers-datas">c. 35–108 d.C. · Síria</div>
      <div class="pers-desc">Discípulo do apóstolo João. Bispo de Antioquia. Escreveu sete cartas às igrejas durante sua viagem a Roma para ser martirizado. Primeiro a usar o termo "Igreja Católica." Defensor da autoridade episcopal e da Eucaristia como "remédio da imortalidade."</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Justino Mártir</div>
      <div class="pers-datas">c. 100–165 d.C. · Palestina/Roma</div>
      <div class="pers-desc">Filósofo convertido ao Cristianismo. Primeiro grande Apologista — defensor intelectual da fé cristã diante dos imperadores romanos. Desenvolveu a doutrina do <em>Logos</em> como semente de verdade em toda a humanidade. Martirizado em Roma.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Ireneu de Lyon</div>
      <div class="pers-datas">c. 130–202 d.C. · Ásia Menor/França</div>
      <div class="pers-desc">Bispo de Lyon. Seu <em>Contra as Heresias</em> é a primeira grande obra de teologia sistemática cristã — uma refutação do Gnosticismo. Desenvolveu a doutrina da <em>recapitulação</em>: Cristo recapitula (resume e restaura) toda a história humana.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Tertuliano</div>
      <div class="pers-datas">c. 155–220 d.C. · Cartago</div>
      <div class="pers-desc">Primeiro grande teólogo latino. Criou o vocabulário trinitário latino: <em>trinitas</em>, <em>persona</em>, <em>substantia</em>. Sua frase "O sangue dos mártires é a semente da Igreja" é célebre. Converteu-se ao Montanismo no final da vida.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Orígenes</div>
      <div class="pers-datas">c. 185–254 d.C. · Alexandria</div>
      <div class="pers-desc">O maior erudito bíblico da Antiguidade. Produziu a <em>Hexapla</em> — seis versões paralelas do AT. Desenvolveu a exegese alegórica. Algumas de suas posições foram condenadas postumamente (pré-existência das almas, apocatástase). Influência enorme na teologia posterior.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Atanásio de Alexandria</div>
      <div class="pers-datas">296–373 d.C. · Egito</div>
      <div class="pers-desc">O grande defensor de Niceia. Exilado cinco vezes por imperadores arianos. Seu tratado <em>Sobre a Encarnação</em> é um dos mais belos da teologia patrística. Atribuiu-se a ele o Cânon do NT que usamos hoje.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">João Crisóstomo</div>
      <div class="pers-datas">347–407 d.C. · Antioquia/Constantinopla</div>
      <div class="pers-desc">O maior pregador da Antiguidade — <em>Crisóstomo</em> significa "boca de ouro." Patriarca de Constantinopla. Seus comentários bíblicos são modelos de exegese histórico-gramatical. Exilado por criticar a Imperatriz Eudóxia.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Agostinho de Hipona</div>
      <div class="pers-datas">354–430 d.C. · Norte da África</div>
      <div class="pers-desc">O maior teólogo do Ocidente. Suas <em>Confissões</em> são o primeiro grande texto autobiográfico da literatura ocidental. <em>A Cidade de Deus</em> é a primeira filosofia da história cristã. Sua teologia da graça, do pecado original e da predestinação moldou o
 Ocidente cristão até hoje.</div>
    </div>
  </div>
</div>
<div class="sb">
  <h2>📚 As Grandes Contribuições da Patrística</h2>
  <div class="bloco">
    <div class="bt">O Cânon Bíblico</div>
    <div class="bx">Os Pais da Igreja foram os responsáveis pela formação do Cânon do Novo Testamento. Não houve um único Concílio que "criou" o Cânon — foi um processo gradual de discernimento em que a Igreja reconheceu quais escritos eram apostólicos, usados universalmente e conformes à regra de fé. Atanásio, em sua Carta Pascal de 367 d.C., foi o primeiro a listar os 27 livros do NT exatamente como os temos hoje. Os Concílios de Hipona (393) e Cartago (397) confirmaram este Cânon.</div>
  </div>
  <div class="bloco">
    <div class="bt">A Regra de Fé</div>
    <div class="bx">Os Pais desenvolveram a <em>regula fidei</em> — a regra de fé — como critério para distinguir o ensinamento apostólico das heresias. A regra de fé era um resumo dos pontos centrais da fé cristã (criação, encarnação, morte, ressurreição, juízo) que servia como chave hermenêutica para a interpretação das Escrituras. Ireneu e Tertuliano foram os principais desenvolvedores desta doutrina. A regra de fé não é uma alternativa às Escrituras — é o resumo do seu ensinamento central, transmitido pela tradição apostólica.</div>
  </div>
  <div class="bloco">
    <div class="bt">A Teologia Trinitária e Cristológica</div>
    <div class="bx">A maior contribuição dos Pais foi o desenvolvimento da teologia trinitária e cristológica que culminou nos Concílios de Niceia e Calcedônia. Eles usaram a filosofia grega — não para helenizar o Evangelho, mas para expressar com precisão verdades bíblicas que a linguagem cotidiana não conseguia articular com suficiente clareza. O vocabulário que eles criaram — <em>ousia</em>, <em>hypostasis</em>, <em>persona</em>, <em>natura</em>, <em>homoousios</em> — tornou-se o instrumento pelo qual a Igreja articulou sua fé por séculos.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: Os Pais da Igreja e Nós</h3>
    <p>Os Pais da Igreja não são autoridades infalíveis — eles erraram em questões individuais e foram condicionados por seu contexto histórico e cultural. Mas eles são testemunhas preciosas da fé da Igreja primitiva — a Igreja mais próxima dos apóstolos. Estudar os Pais é ouvir vozes que beberam diretamente da fonte apostólica e que enfrentaram desafios teológicos que, em formas diferentes, ainda enfrentamos hoje. Calvino chamava os Pais de "testemunhas aprovadas" — não árbitros supremos, mas guias confiáveis na interpretação das Escrituras. Esta é uma posição sábia: nem ignorar os Pais (como faz o fundamentalismo que rejeita toda tradição) nem idolatrá-los (como faz o catolicismo que os equipara à Escritura), mas aprender com eles com discernimento e gratidão.</p>
  </div>
</div>
"""

MODULOS_09 = [
    {
        "pasta": "concilios-ecumenicos",
        "cor": "#818cf8",
        "hero_bg": "#0a0a1f",
        "titulo": "Os 21 Concílios Ecumênicos",
        "subtitulo": "📜 Visão Geral · 325–1965 d.C.",
        "ref": "Da Igreja Primitiva ao Século XX",
        "citacao": "Pareceu bem ao Espírito Santo e a nós não vos impor nenhum outro encargo além destas coisas necessárias.",
        "autor_cit": "Concílio de Jerusalém, Atos 15:28 — o modelo bíblico de deliberação conciliar",
        "corpo": concilios_corpo,
        "nav_prev": "/09-concilios/index.html",
        "nav_prev_lbl": "← Índice Bloco 09",
        "nav_next": "/09-concilios/niceia",
        "nav_next_lbl": "Concílio de Niceia →",
    },
    {
        "pasta": "niceia",
        "cor": "#f59e0b",
        "hero_bg": "#1a0e00",
        "titulo": "Concílio de Niceia (325)",
        "subtitulo": "⭐ Niceia · 325 d.C.",
        "ref": "A Divindade de Cristo · Contra o Arianismo · Homoousios",
        "citacao": "Houve um tempo em que o Filho não existia.",
        "autor_cit": "Ário — a frase que provocou o Concílio de Niceia e foi condenada por ele",
        "corpo": niceia_corpo,
        "nav_prev": "/09-concilios/concilios-ecumenicos",
        "nav_prev_lbl": "← Os 21 Concílios",
        "nav_next": "/09-concilios/constantinopla",
        "nav_next_lbl": "Constantinopla I →",
    },
    {
        "pasta": "constantinopla",
        "cor": "#22c55e",
        "hero_bg": "#001a08",
        "titulo": "Constantinopla I (381)",
        "subtitulo": "🕊️ Constantinopla · 381 d.C.",
        "ref": "A Divindade do Espírito Santo · Os Capadócios · Credo Niceno-Constantinopolitano",
        "citacao": "O Espírito Santo é Senhor e dá a vida; com o Pai e o Filho é adorado e glorificado conjuntamente.",
        "autor_cit": "Credo Niceno-Constantinopolitano (381 d.C.)",
        "corpo": const_corpo,
        "nav_prev": "/09-concilios/niceia",
        "nav_prev_lbl": "← Niceia",
        "nav_next": "/09-concilios/efeso-calcedonia",
        "nav_next_lbl": "Éfeso e Calcedônia →",
    },
    {
        "pasta": "efeso-calcedonia",
        "cor": "#ef4444",
        "hero_bg": "#1a0000",
        "titulo": "Éfeso (431) e Calcedônia (451)",
        "subtitulo": "✝️ Éfeso · Calcedônia · Séc. V",
        "ref": "As Duas Naturezas de Cristo · Theotokos · Definição Calcedoniana",
        "citacao": "Um e o mesmo Cristo, Filho, Senhor, Unigênito, em duas naturezas, sem confusão, sem mudança, sem divisão, sem separação.",
        "autor_cit": "Definição do Concílio de Calcedônia (451 d.C.)",
        "corpo": efeso_corpo,
        "nav_prev": "/09-concilios/constantinopla",
        "nav_prev_lbl": "← Constantinopla I",
        "nav_next": "/09-concilios/trento",
        "nav_next_lbl": "Concílio de Trento →",
    },
    {
        "pasta": "trento",
        "cor": "#a855f7",
        "hero_bg": "#0d001a",
        "titulo": "Concílio de Trento (1545–1563)",
        "subtitulo": "🏰 Trento · 1545–1563",
        "ref": "Resposta à Reforma · Justificação · Sacramentos · Reforma Disciplinar",
        "citacao": "Se alguém disser que o homem é justificado pela fé somente, de modo que se entenda que nada mais é requerido para cooperar para a obtenção da graça da justificação — seja anátema.",
        "autor_cit": "Cânon IX do Decreto sobre a Justificação, Concílio de Trento (1547)",
        "corpo": trento_corpo,
        "nav_prev": "/09-concilios/efeso-calcedonia",
        "nav_prev_lbl": "← Éfeso e Calcedônia",
        "nav_next": "/09-concilios/vaticano-i",
        "nav_next_lbl": "Vaticano I →",
    },
    {
        "pasta": "vaticano-i",
        "cor": "#22d3ee",
        "hero_bg": "#001a1f",
        "titulo": "Concílio Vaticano I (1869–1870)",
        "subtitulo": "👑 Vaticano I · 1869–1870",
        "ref": "Infalibilidade Papal · Pastor Aeternus · Primado de Jurisdição",
        "citacao": "O Romano Pontífice, quando fala ex cathedra... goza, em virtude da assistência divina prometida a ele na pessoa do bem-aventurado Pedro, da infalibilidade.",
        "autor_cit": "Pastor Aeternus, Concílio Vaticano I (1870)",
        "corpo": vat1_corpo,
        "nav_prev": "/09-concilios/trento",
        "nav_prev_lbl": "← Trento",
        "nav_next": "/09-concilios/vaticano-ii",
        "nav_next_lbl": "Vaticano II →",
    },
    {
        "pasta": "vaticano-ii",
        "cor": "#f97316",
        "hero_bg": "#1a0800",
        "titulo": "Concílio Vaticano II (1962–1965)",
        "subtitulo": "🌍 Vaticano II · 1962–1965",
        "ref": "Aggiornamento · Lumen Gentium · Gaudium et Spes · Ecumenismo",
        "citacao": "As alegrias e as esperanças, as tristezas e as angústias dos homens de hoje, sobretudo dos pobres e de todos os que sofrem, são também as alegrias e as esperanças, as tristezas e as angústias dos discípulos de Cristo.",
        "autor_cit": "Gaudium et Spes, §1 — Concílio Vaticano II (1965)",
        "corpo": vat2_corpo,
        "nav_prev": "/09-concilios/vaticano-i",
        "nav_prev_lbl": "← Vaticano I",
        "nav_next": "/09-concilios/patristica",
        "nav_next_lbl": "Patrística →",
    },
    {
        "pasta": "patristica",
        "cor": "#10b981",
        "hero_bg": "#001a0e",
        "titulo": "Os Pais da Igreja e a Patrística",
        "subtitulo": "📖 Patrística · Séc. I–VIII",
        "ref": "Inácio · Justino · Ireneu · Tertuliano · Orígenes · Atanásio · Agostinho",
        "citacao": "Aquele que lê muito e compreende muito, esse é o homem culto. Aquele que lê pouco e compreende muito, esse é o homem sábio.",
        "autor_cit": "Agostinho de Hipona",
        "corpo": patrist_corpo,
        "nav_prev": "/09-concilios/vaticano-ii",
        "nav_prev_lbl": "← Vaticano II",
        "nav_next": "/09-concilios/index.html",
        "nav_next_lbl": "Índice Bloco 09 →",
    },
]


def main():
    for m in MODULOS_09:
        html = pagina(
            m["pasta"], m["cor"], m["hero_bg"],
            m["titulo"], m["subtitulo"], m["ref"],
            m["citacao"], m["autor_cit"], m["corpo"],
            m["nav_prev"], m["nav_prev_lbl"],
            m["nav_next"], m["nav_next_lbl"]
        )
        path = os.path.join(BASE, m["pasta"], "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {m['pasta']}/index.html")
    print("\n🎉 Bloco 09 completo!")


if __name__ == "__main__":
    main()
