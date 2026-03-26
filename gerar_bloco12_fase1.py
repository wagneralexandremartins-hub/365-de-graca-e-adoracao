#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os módulos da fase 1 do Bloco 12 — Introdução, João em Patmos, 7 Igrejas, Visão do Trono, Hermenêutica."""

import os

BASE = "/home/ubuntu/365-de-graca-e-adoracao/12-apocalipse"

CSS_COMUM = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: #0a0a14; color: #e2e8f0; font-family: 'Georgia', serif; line-height: 1.7; }
    a { color: inherit; text-decoration: none; }
    .topbar { background: rgba(10,10,20,0.97); border-bottom: 1px solid rgba(255,255,255,0.07); padding: 14px 0; position: sticky; top: 0; z-index: 100; }
    .topbar .inner { max-width: 900px; margin: 0 auto; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
    .topbar a { font-size: 0.85rem; color: #94a3b8; font-weight: 600; }
    .hero { padding: 64px 24px 48px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.07); }
    .tag { display: inline-block; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 999px; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 1px; }
    .hero h1 { font-size: 2.4rem; font-weight: 900; color: #f1f5f9; margin-bottom: 12px; line-height: 1.2; }
    .hero .ref { font-size: 0.88rem; color: #64748b; margin-bottom: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .hero blockquote { font-style: italic; color: #cbd5e1; font-size: 1rem; padding-left: 20px; max-width: 620px; margin: 0 auto; text-align: left; }
    .wrap { max-width: 900px; margin: 0 auto; padding: 40px 24px 80px; }
    .sb { margin-bottom: 44px; }
    .sb h2 { font-size: 1.3rem; font-weight: 800; color: #f1f5f9; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.07); }
    .sb p { color: #94a3b8; font-size: 0.95rem; line-height: 1.88; margin-bottom: 16px; }
    .bloco { border-left-width: 3px; border-left-style: solid; border-radius: 0 12px 12px 0; padding: 18px 22px; margin-bottom: 16px; background: rgba(255,255,255,0.02); border-top: 1px solid rgba(255,255,255,0.07); border-right: 1px solid rgba(255,255,255,0.07); border-bottom: 1px solid rgba(255,255,255,0.07); }
    .bt { font-size: 0.85rem; font-weight: 800; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
    .bx { color: #94a3b8; font-size: 0.93rem; line-height: 1.85; }
    .versiculo { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 16px 20px; margin-bottom: 20px; }
    .v-ref { font-size: 0.78rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }
    .v-texto { font-style: italic; color: #e2e8f0; font-size: 0.95rem; line-height: 1.75; margin-bottom: 10px; border-left: 2px solid; padding-left: 14px; }
    .v-analise { color: #94a3b8; font-size: 0.9rem; line-height: 1.82; }
    table { width: 100%; border-collapse: collapse; font-size: 0.87rem; margin: 20px 0 32px; }
    td { padding: 10px 14px; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; }
    tr:hover td { background: rgba(255,255,255,0.02); }
    .nav-mod { display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.07); flex-wrap: wrap; gap: 10px; }
    .nav-mod a { padding: 10px 20px; border-radius: 8px; font-size: 0.88rem; font-weight: 700; transition: all 0.2s; }
    .reflexao { border-radius: 12px; padding: 22px 26px; margin-top: 32px; background: rgba(34,197,94,0.05); border: 1px solid rgba(34,197,94,0.15); }
    .reflexao h3 { color: #22c55e; font-size: 0.95rem; font-weight: 800; margin-bottom: 10px; }
    .reflexao p { color: #94a3b8; font-size: 0.9rem; line-height: 1.82; margin-bottom: 10px; }
    .reflexao p:last-child { margin-bottom: 0; }
    .igreja-card { border-radius: 14px; padding: 22px 24px; margin-bottom: 24px; border: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.02); }
    .ic-header { display: flex; align-items: center; gap: 12px; margin-bottom: 14px; }
    .ic-num { font-size: 1.4rem; font-weight: 900; }
    .ic-nome { font-size: 1.1rem; font-weight: 800; color: #f1f5f9; }
    .ic-local { font-size: 0.78rem; color: #64748b; font-weight: 600; }
    .ic-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 10px; margin-bottom: 12px; }
    .ic-item { background: rgba(255,255,255,0.03); border-radius: 8px; padding: 10px 12px; }
    .ic-label { font-size: 0.7rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }
    .ic-valor { font-size: 0.85rem; color: #94a3b8; line-height: 1.5; }
    .ic-analise { font-size: 0.9rem; color: #94a3b8; line-height: 1.82; }
    .escola-card { border-radius: 12px; padding: 20px 22px; margin-bottom: 16px; border: 1px solid rgba(255,255,255,0.07); background: rgba(255,255,255,0.02); }
    .ec-titulo { font-size: 1rem; font-weight: 800; margin-bottom: 6px; }
    .ec-desc { font-size: 0.9rem; color: #94a3b8; line-height: 1.8; }
"""


def pagina(pasta, cor, hero_bg, titulo, subtitulo, ref, citacao, autor_cit, corpo, nav_prev, nav_prev_lbl, nav_next, nav_next_lbl):
    css_extra = f"""
    .topbar a:hover {{ color: {cor}; }}
    .hero {{ background: linear-gradient(135deg, #0a0a14 0%, {hero_bg} 50%, #0a0a14 100%); }}
    .tag {{ background: {cor}18; border: 1px solid {cor}40; color: {cor}; }}
    .hero blockquote {{ border-left: 3px solid {cor}; }}
    .bloco {{ border-left-color: {cor}; }}
    .bt {{ color: {cor}; }}
    .v-ref {{ color: {cor}; }}
    .v-texto {{ border-left-color: {cor}; }}
    table th {{ background: {cor}18; color: {cor}; border-bottom: 1px solid {cor}30; }}
    .nav-mod a {{ background: {cor}18; border: 1px solid {cor}30; color: {cor}; }}
    .nav-mod a:hover {{ background: {cor}30; }}
    .ic-num {{ color: {cor}; }}
    .ic-label {{ color: {cor}; }}
    .ec-titulo {{ color: {cor}; }}
    """
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titulo} | Bloco 12 — Apocalipse | 365 de Graça & Adoração</title>
  <link rel="icon" href="/favicon.ico">
  <style>{CSS_COMUM}{css_extra}</style>
</head>
<body>
  <div class="topbar"><div class="inner">
    <a href="/12-apocalipse/index.html">← Bloco 12</a>
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
      <a href="/12-apocalipse/index.html">📋 Índice</a>
      <a href="{nav_next}">{nav_next_lbl}</a>
    </div>
  </div>
</body>
</html>"""


# ============================================================
# MÓDULO: INTRODUÇÃO
# ============================================================
intro_corpo = """
<div class="sb">
  <h2>📜 O Que é o Apocalipse?</h2>
  <p>O Apocalipse de João é o último livro da Bíblia e um dos mais fascinantes e mal compreendidos de toda a Escritura. Seu título vem do grego <em>apokalypsis</em> — "revelação", "desvelamento" — e esta palavra define seu propósito: não esconder o futuro em mistério impenetrável, mas revelar realidades espirituais que estão ocultas aos olhos humanos comuns. O Apocalipse não é um livro de terror — é um livro de esperança, escrito para cristãos perseguidos que precisavam ver além das aparências e compreender que o Senhor da história estava no controle, mesmo quando tudo parecia indicar o contrário.</p>
  <p>O livro foi escrito pelo apóstolo João durante seu exílio na ilha de Patmos, no Mar Egeu, provavelmente durante o reinado do Imperador Domiciano (81–96 d.C.), que havia lançado uma perseguição aos cristãos por se recusarem a adorar o Imperador como deus. As sete igrejas da Ásia Menor às quais o livro é dirigido — Éfeso, Esmirna, Pérgamo, Tiatira, Sardes, Filadélfia e Laodiceia — eram comunidades reais que enfrentavam pressões reais: perseguição imperial, heresias internas, compromisso com a cultura pagã e o risco de apostasia. O Apocalipse foi escrito para elas — e, através delas, para toda a Igreja em toda a história.</p>
</div>
<div class="sb">
  <h2>📚 O Gênero Apocalíptico</h2>
  <p>O Apocalipse pertence ao gênero literário da <strong>apocalíptica</strong> — um gênero literário judaico e cristão que floresceu entre 200 a.C. e 200 d.C. Outros exemplos incluem Daniel (caps. 7–12), 1 Enoque, 4 Esdras e o Apocalipse de Baruc. As características do gênero apocalíptico incluem: visões mediadas por um anjo; uso extensivo de símbolos e imagens (animais, números, cores); perspectiva dualista (Deus vs. Satanás, bem vs. mal, céu vs. terra); urgência escatológica (o fim está próximo); e propósito pastoral (consolar e fortalecer os perseguidos).</p>
  <p>Compreender o gênero apocalíptico é essencial para interpretar o Apocalipse corretamente. Os símbolos do Apocalipse não são enigmas arbitrários — eles têm raízes profundas no Antigo Testamento e na tradição judaica. O Dragão vermelho de Apocalipse 12 evoca o Leviatã do Salmo 74 e o Egito de Ezequiel 29. A Besta do mar de Apocalipse 13 é uma combinação das quatro bestas de Daniel 7. A Mulher vestida de sol evoca Israel de Gênesis 37. Para um leitor judeu do século I, estas imagens eram imediatamente reconhecíveis — como um código que os perseguidores romanos não conseguiam decifrar, mas que os cristãos entendiam perfeitamente.</p>
</div>
<div class="sb">
  <h2>🏗️ A Estrutura do Apocalipse</h2>
  <div class="bloco">
    <div class="bt">Estrutura em Sete Partes</div>
    <div class="bx">O Apocalipse é organizado em torno do número 7 — o número da perfeição e completude. Há 7 cartas às igrejas (caps. 2–3), 7 selos (caps. 6–8), 7 trombetas (caps. 8–11), 7 visões centrais (caps. 12–14), 7 taças (caps. 15–16), 7 visões de julgamento (caps. 17–20) e 7 visões da Nova Criação (caps. 21–22). Esta estrutura heptádica não é acidental — ela reflete a convicção de que a história humana está se movendo em direção a um fim perfeito e completo ordenado por Deus.</div>
  </div>
  <div class="bloco">
    <div class="bt">Recapitulação — Não Cronologia Linear</div>
    <div class="bx">Uma das chaves para interpretar o Apocalipse é reconhecer que ele não segue uma cronologia linear — ele usa a técnica literária da <em>recapitulação</em>: as séries de 7 selos, 7 trombetas e 7 taças não são eventos sequenciais, mas visões paralelas do mesmo período histórico, cada uma com um ângulo diferente e uma intensidade crescente. Os selos descrevem o período da história da Igreja de forma geral; as trombetas focam nos julgamentos de advertência; as taças representam os julgamentos finais. Esta interpretação — defendida por Agostinho, Lutero e a maioria dos reformadores — evita a armadilha de tentar criar um "calendário profético" detalhado a partir do Apocalipse.</div>
  </div>
</div>
<div class="sb">
  <h2>📅 Data e Autoria</h2>
  <div class="bloco">
    <div class="bt">O Autor — João de Patmos</div>
    <div class="bx">O autor se identifica como "João" (Ap 1:1, 4, 9; 22:8) — um nome que não precisa de qualificação adicional para os destinatários, o que sugere que era bem conhecido pelas igrejas da Ásia Menor. A tradição da Igreja desde o século II (Justino Mártir, Ireneu, Clemente de Alexandria) identifica este João com o apóstolo João, filho de Zebedeu, o autor do Quarto Evangelho e das três Epístolas Joaninas. Esta identificação é contestada por alguns estudiosos modernos — o estilo grego do Apocalipse é mais rude e semítico do que o do Evangelho de João — mas a maioria dos estudiosos conservadores mantém a autoria apostólica.</div>
  </div>
  <div class="bloco">
    <div class="bt">A Data — c. 95–96 d.C.</div>
    <div class="bx">A maioria dos estudiosos data o Apocalipse no final do reinado de Domiciano (81–96 d.C.), com base no testemunho de Ireneu (c. 180 d.C.), que afirma que a visão foi recebida "quase em nossa própria geração, no final do reinado de Domiciano." Esta data tardia (c. 95–96 d.C.) é consistente com as evidências internas do livro: as sete igrejas mostram sinais de desenvolvimento institucional que sugere um período posterior ao da Primeira Epístola de Paulo; a perseguição imperial descrita é consistente com a de Domiciano; e a referência à "besta que era, e não é, e está para subir" (Ap 17:8) pode aludir ao mito de Nero redivivus — a crença popular de que Nero havia ressuscitado ou retornado.</div>
  </div>
</div>
<div class="sb">
  <h2>🔍 As Quatro Escolas de Interpretação</h2>
  <div class="escola-card">
    <div class="ec-titulo">1. Preterismo — "Já se Cumpriu"</div>
    <div class="ec-desc">O Preterismo (do latim <em>praeter</em> — "passado") interpreta a maior parte do Apocalipse como tendo se cumprido no século I — especialmente na destruição de Jerusalém em 70 d.C. (Preterismo Parcial) ou em sua totalidade (Preterismo Total). Para os preteristas, a "besta" é Nero, "Babilônia" é Roma, e os julgamentos do Apocalipse são a destruição do Templo e do Estado judeu. Esta interpretação tem o mérito de levar a sério o contexto histórico do livro e a afirmação de João de que os eventos "devem acontecer em breve" (Ap 1:1). Seus principais defensores modernos incluem R.C. Sproul e Kenneth Gentry.</div>
  </div>
  <div class="escola-card">
    <div class="ec-titulo">2. Historicismo — "A História da Igreja"</div>
    <div class="ec-desc">O Historicismo interpreta o Apocalipse como uma profecia panorâmica de toda a história da Igreja, desde o século I até o retorno de Cristo. Os selos, trombetas e taças representam eventos históricos específicos — as invasões bárbaras, o surgimento do Islã, a Reforma Protestante, etc. Esta foi a interpretação dominante dos Reformadores (Lutero, Calvino, Knox) e dos puritanos. Ela identificava o Papa com o Anticristo e o Papado com a Besta. Hoje, o Historicismo tem poucos defensores acadêmicos, mas ainda é influente em algumas tradições protestantes.</div>
  </div>
  <div class="escola-card">
    <div class="ec-titulo">3. Futurismo — "Ainda Está por Vir"</div>
    <div class="ec-desc">O Futurismo interpreta a maior parte do Apocalipse (caps. 4–22) como descrevendo eventos que ainda estão por acontecer — especialmente os eventos do "fim dos tempos." O Futurismo Dispensacionalista (a forma mais popular nos EUA) divide o Futurismo em Pré-Tribulacionismo (o Arrebatamento precede a Grande Tribulação), Pós-Tribulacionismo (a Igreja passa pela Tribulação) e Meio-Tribulacionismo. Esta interpretação foi sistematizada por John Nelson Darby no século XIX e popularizada pelo Scofield Reference Bible e, mais recentemente, pela série Left Behind. Seus defensores incluem John MacArthur, Tim LaHaye e Hal Lindsey.</div>
  </div>
  <div class="escola-card">
    <div class="ec-titulo">4. Idealismo — "Princípios Atemporais"</div>
    <div class="ec-desc">O Idealismo (ou Simbolismo) interpreta o Apocalipse não como profecia de eventos históricos específicos, mas como uma representação simbólica do conflito eterno entre o bem e o mal, que se repete em cada geração. Os símbolos do Apocalipse não têm referentes históricos específicos — eles representam princípios espirituais atemporais: a Besta representa qualquer poder opressor, Babilônia representa qualquer cultura que se oponha a Deus, a Nova Jerusalém representa a comunhão com Deus que os fiéis experimentam agora e plenamente no fim. Seus defensores incluem William Hendriksen e Vern Poythress.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: Como Ler o Apocalipse com Sabedoria</h3>
    <p>Cada uma das quatro escolas de interpretação captura aspectos importantes do Apocalipse. O Preterismo tem razão em levar a sério o contexto histórico do século I. O Historicismo tem razão em ver o Apocalipse como relevante para toda a história da Igreja. O Futurismo tem razão em esperar um cumprimento escatológico final das promessas de Deus. O Idealismo tem razão em reconhecer os princípios espirituais atemporais que o Apocalipse comunica. Uma interpretação sábia do Apocalipse provavelmente incorpora elementos de todas as quatro escolas — lendo o livro como uma palavra dirigida às igrejas do século I, relevante para toda a história da Igreja, apontando para um cumprimento escatológico final, e comunicando verdades espirituais atemporais sobre o conflito entre Deus e o mal. O que o Apocalipse não é: um calendário profético detalhado que nos permite prever datas e eventos específicos. Aqueles que tentam usar o Apocalipse desta forma invariavelmente se enganam — e enganam outros.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO: JOÃO EM PATMOS (Cap. 1)
# ============================================================
joao_corpo = """
<div class="sb">
  <h2>🏝️ Patmos — O Lugar do Exílio</h2>
  <p>Patmos é uma pequena ilha rochosa no Mar Egeu, a cerca de 60 km da costa da Ásia Menor (atual Turquia). Com apenas 34 km², ela era usada pelos romanos como local de exílio para criminosos e dissidentes políticos. João foi exilado ali "por causa da palavra de Deus e do testemunho de Jesus" (Ap 1:9) — provavelmente durante a perseguição de Domiciano (81–96 d.C.), que exigia que seus súditos o adorassem como "Senhor e Deus" (<em>Dominus et Deus</em>). Para um cristão que confessava que "Jesus é Senhor" (<em>Kyrios Iēsous</em>), esta exigência era uma apostasia inaceitável.</p>
  <p>O exílio de João em Patmos não foi uma derrota — foi o contexto em que ele recebeu a maior visão profética do Novo Testamento. Isto é característico da espiritualidade bíblica: os momentos de maior sofrimento e isolamento frequentemente são os momentos de maior revelação divina. Moisés recebeu a revelação do nome de Deus no deserto do Sinai. Elias recebeu a voz suave e delicada no deserto de Horebe. Paulo recebeu suas revelações durante seus encarceramento. João recebeu o Apocalipse em Patmos. O sofrimento não impede a revelação — ele a prepara.</p>
</div>
<div class="sb">
  <h2>📖 Apocalipse 1:1–8 — O Prólogo</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 1:1–3</div>
    <div class="v-texto">"Revelação de Jesus Cristo, que Deus lhe deu para mostrar aos seus servos as coisas que em breve devem acontecer; e as quais ele comunicou, enviando-as pelo seu anjo ao seu servo João, que testificou da palavra de Deus e do testemunho de Jesus Cristo, tudo o que viu. Bem-aventurado aquele que lê, e os que ouvem as palavras desta profecia e guardam as coisas nela escritas; porque o tempo está próximo."</div>
    <div class="v-analise">O prólogo estabelece a cadeia de revelação: Deus → Cristo → Anjo → João → Igreja. O Apocalipse não é uma visão de João sobre o futuro — é uma revelação que Deus deu a Cristo, que a comunicou por meio de um anjo a João. A primeira bem-aventurança do Apocalipse (há sete no total) é dada àqueles que leem, ouvem e guardam as palavras do livro — sugerindo que ele era lido em voz alta nas reuniões das igrejas. "O tempo está próximo" — esta urgência escatológica é central para entender o livro: ele foi escrito para pessoas que precisavam de esperança imediata, não para especuladores do futuro distante.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 1:4–6</div>
    <div class="v-texto">"João, às sete igrejas que estão na Ásia: Graça e paz da parte daquele que é, e que era, e que há de vir, e dos sete Espíritos que estão diante do seu trono, e da parte de Jesus Cristo, a testemunha fiel, o primogênito dos mortos e o soberano dos reis da terra."</div>
    <div class="v-analise">A saudação trinitária: o Pai ("aquele que é, e que era, e que há de vir" — uma expansão do nome divino YHWH de Êxodo 3:14), o Espírito Santo ("os sete Espíritos" — a plenitude do Espírito, baseado em Isaías 11:2) e o Filho (Jesus Cristo — com três títulos messiânicos: "testemunha fiel" evoca o Servo Sofredor de Isaías; "primogênito dos mortos" afirma a ressurreição; "soberano dos reis da terra" afirma a soberania universal de Cristo sobre todos os poderes, incluindo Roma). Para cristãos perseguidos pelo Imperador romano, esta afirmação de que Jesus é "soberano dos reis da terra" era ao mesmo tempo um conforto e uma provocação.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 1:7–8</div>
    <div class="v-texto">"Eis que vem com as nuvens, e todo olho o verá, até mesmo os que o traspassaram; e todos os povos da terra se lamentarão sobre ele. Sim, amém. Eu sou o Alfa e o Ômega, diz o Senhor Deus, aquele que é, e que era, e que há de vir, o Todo-Poderoso."</div>
    <div class="v-analise">"Vem com as nuvens" combina Daniel 7:13 (o Filho do Homem vindo nas nuvens) com Zacarias 12:10 ("olharão para aquele a quem traspassaram"). O retorno de Cristo será universal e inegável — "todo olho o verá." O lamento dos povos pode ser de arrependimento (como em Zacarias 12) ou de terror (como em Mateus 24:30). "Alfa e Ômega" — a primeira e a última letra do alfabeto grego — afirma que Deus é o começo e o fim de toda a história. Esta afirmação será repetida pelo Cristo ressurreto em Apocalipse 22:13, identificando Cristo com o Deus do AT.</div>
  </div>
</div>
<div class="sb">
  <h2>👁️ Apocalipse 1:9–20 — A Visão do Cristo Glorificado</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 1:9–11</div>
    <div class="v-texto">"Eu, João, irmão de vós todos e companheiro na tribulação, no reino e na perseverança em Jesus, estava na ilha chamada Patmos, por causa da palavra de Deus e do testemunho de Jesus. Fiquei em êxtase no dia do Senhor, e ouvi detrás de mim uma grande voz, como de trombeta, que dizia: O que vês, escreve num livro e manda às sete igrejas."</div>
    <div class="v-analise">João se apresenta como "irmão" e "companheiro na tribulação" — não como autoridade distante, mas como co-participante no sofrimento. "No dia do Senhor" — o domingo, o dia da ressurreição, quando as igrejas se reuniam para adorar. A voz "como de trombeta" evoca a teofania do Sinai (Êxodo 19:16–19) — a revelação divina sempre é acompanhada de sons poderosos no AT. O mandato de "escrever num livro" é fundamental: o Apocalipse não é apenas uma experiência mística privada — é uma revelação destinada à Igreja.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 1:12–16</div>
    <div class="v-texto">"Voltei-me para ver a voz que falava comigo; e, voltando-me, vi sete candeeiros de ouro; e no meio dos candeeiros, um semelhante ao Filho do Homem, vestido com uma roupa que chegava até os pés e cingido, na altura do peito, com um cinto de ouro. Sua cabeça e seus cabelos eram brancos como lã branca, como neve; seus olhos, como chama de fogo; seus pés, semelhantes ao bronze polido, como que refinado numa fornalha; e sua voz, como o ruído de muitas águas. Tinha na mão direita sete estrelas; e da sua boca saía uma espada aguda de dois gumes; e o seu rosto era como o sol quando brilha na sua força."</div>
    <div class="v-analise">Esta visão é uma das mais ricas em alusões ao AT de todo o Apocalipse. "Filho do Homem" evoca Daniel 7:13 — o ser celestial que recebe o domínio eterno. "Cabelos brancos como lã" evoca o "Ancião de Dias" de Daniel 7:9 — João aplica ao Cristo ressurreto atributos que Daniel aplica ao Pai, afirmando implicitamente a divindade de Cristo. "Olhos como chama de fogo" — visão penetrante que nada escapa. "Pés como bronze polido" — força e estabilidade inabaláveis. "Voz como muitas águas" evoca a voz de Deus em Ezequiel 43:2. "Espada de dois gumes" — a palavra de Deus que julga (Hb 4:12). "Rosto como o sol" evoca a Transfiguração (Mt 17:2). O Cristo do Apocalipse não é o Jesus manso e humilde dos Evangelhos — é o Senhor glorificado, o Juiz soberano, o Rei dos reis.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 1:17–20</div>
    <div class="v-texto">"Quando o vi, caí a seus pés como morto. Mas ele pôs sobre mim a sua mão direita, dizendo: Não temas; eu sou o Primeiro e o Último, e o que vive; estive morto, mas eis que estou vivo pelos séculos dos séculos, e tenho as chaves da morte e do Hades."</div>
    <div class="v-analise">A reação de João — cair "como morto" — é a reação típica diante de uma teofania no AT (Ezequiel 1:28; Daniel 10:9). O gesto de Cristo — "pôs sobre mim a sua mão direita" — é um gesto de conforto e comissionamento. "Não temas" — as mesmas palavras com que os anjos saúdam os humanos em momentos de revelação divina. "Eu sou o Primeiro e o Último" — o mesmo título dado a YHWH em Isaías 44:6 e 48:12, aplicado aqui a Cristo. "Tenho as chaves da morte e do Hades" — Cristo tem autoridade soberana sobre a morte — a maior ameaça que os perseguidores podiam fazer. Para cristãos que enfrentavam o martírio, esta afirmação era de imenso conforto: o pior que Roma podia fazer — matar — estava sob o controle de Cristo.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: O Cristo do Apocalipse e Nós</h3>
    <p>A visão do Cristo glorificado em Apocalipse 1 é um antídoto poderoso contra uma visão sentimental e domesticada de Jesus. O Cristo do Apocalipse não é apenas um amigo gentil ou um conselheiro espiritual — ele é o Senhor soberano do universo, cujos olhos são como chama de fogo e cuja voz é como o ruído de muitas águas. Diante dele, o apóstolo mais amado caiu como morto. Esta visão não nos deve afastar de Cristo — deve nos aproximar com reverência e maravilha. O mesmo Cristo que é o Senhor glorificado é aquele que pôs sua mão direita sobre João e disse "Não temas." A soberania e a ternura de Cristo não são contraditórias — elas são complementares. Ele é simultaneamente o Leão de Judá e o Cordeiro imolado (Ap 5:5–6).</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO: AS 7 IGREJAS
# ============================================================
igrejas_corpo = """
<div class="sb">
  <h2>⛪ As 7 Igrejas — Contexto e Estrutura</h2>
  <p>As cartas às sete igrejas (Apocalipse 2–3) são a parte mais imediatamente pastoral do Apocalipse — e, paradoxalmente, a mais frequentemente negligenciada em favor das visões mais dramáticas dos capítulos seguintes. Mas estas cartas são a chave para entender todo o livro: elas revelam o propósito pastoral do Apocalipse, identificam os problemas que as igrejas enfrentavam, e estabelecem o padrão de diagnóstico espiritual que percorre todo o livro.</p>
  <p>As sete igrejas eram comunidades reais em cidades reais da Ásia Menor (atual Turquia ocidental), todas situadas em uma rota circular que um mensageiro poderia percorrer partindo de Éfeso, o principal porto da região. Cada cidade tinha características geográficas, históricas e culturais específicas que João usa para comunicar sua mensagem — os ouvintes originais reconheceriam imediatamente as alusões locais. Mas as sete igrejas também representam tipologicamente toda a Igreja em toda a história — cada uma representa um tipo de situação espiritual que se repete em todas as épocas.</p>
  <p>Cada carta segue um padrão estrutural consistente: (1) endereço à igreja; (2) descrição de Cristo usando elementos da visão do cap. 1; (3) elogio ("conheço as tuas obras"); (4) repreensão (ausente em Esmirna e Filadélfia); (5) exortação e chamado ao arrependimento; (6) promessa ao "vencedor"; (7) chamado a ouvir o Espírito. Este padrão revela que Cristo conhece cada igreja intimamente — seus pontos fortes e suas fraquezas — e que ele se dirige a cada uma com precisão pastoral.</p>
</div>

<div class="sb">
  <h2>📍 As 7 Igrejas em Detalhe</h2>

  <div class="igreja-card">
    <div class="ic-header">
      <div class="ic-num">1</div>
      <div>
        <div class="ic-nome">Éfeso — A Igreja que Perdeu o Primeiro Amor</div>
        <div class="ic-local">Ap 2:1–7 · Principal cidade da Ásia Menor · Centro do culto a Ártemis</div>
      </div>
    </div>
    <div class="ic-grid">
      <div class="ic-item"><div class="ic-label">Elogio</div><div class="ic-valor">Trabalho, perseverança, intolerância ao mal, testou os falsos apóstolos, odeia os nicolaítas</div></div>
      <div class="ic-item"><div class="ic-label">Repreensão</div><div class="ic-valor">Abandonou o primeiro amor — a devoção fervorosa e a alegria do relacionamento com Cristo</div></div>
      <div class="ic-item"><div class="ic-label">Exortação</div><div class="ic-valor">Lembra de onde caíste, arrepende-te e faz as primeiras obras</div></div>
      <div class="ic-item"><div class="ic-label">Ameaça</div><div class="ic-valor">Removerei o teu candeeiro do seu lugar</div></div>
      <div class="ic-item"><div class="ic-label">Promessa</div><div class="ic-valor">Comer da árvore da vida no paraíso de Deus</div></div>
    </div>
    <div class="ic-analise">Éfeso era a maior e mais importante cidade da Ásia Menor — um centro comercial, cultural e religioso de primeira grandeza. A igreja de Éfeso havia sido fundada por Paulo (At 19) e pastoreada por Timóteo e, posteriormente, pelo próprio João. Era uma igreja ortodoxa e trabalhadora — mas havia perdido o que mais importava: o amor ardente por Cristo que havia caracterizado sua fundação. A ortodoxia sem amor é um cadáver teológico. A ameaça de remover o candeeiro é uma ameaça de extinção — uma igreja sem amor não é mais uma igreja no sentido pleno. A promessa da "árvore da vida" evoca o Éden (Gn 2–3) e antecipa a Nova Jerusalém (Ap 22:2) — o amor restaurado é o retorno ao Paraíso.</div>
  </div>

  <div class="igreja-card">
    <div class="ic-header">
      <div class="ic-num">2</div>
      <div>
        <div class="ic-nome">Esmirna — A Igreja Perseguida e Pobre-Rica</div>
        <div class="ic-local">Ap 2:8–11 · Porto importante · Rival de Éfeso · Forte culto imperial</div>
      </div>
    </div>
    <div class="ic-grid">
      <div class="ic-item"><div class="ic-label">Elogio</div><div class="ic-valor">Tribulação, pobreza (mas és rico!), blasfêmia dos que dizem ser judeus e não são</div></div>
      <div class="ic-item"><div class="ic-label">Repreensão</div><div class="ic-valor">Nenhuma — Esmirna é uma das duas igrejas sem repreensão</div></div>
      <div class="ic-item"><div class="ic-label">Exortação</div><div class="ic-valor">Não temas o que estás para sofrer; sê fiel até a morte</div></div>
      <div class="ic-item"><div class="ic-label">Promessa</div><div class="ic-valor">A coroa da vida; não será prejudicado pela segunda morte</div></div>
    </div>
    <div class="ic-analise">Esmirna era uma cidade rica e bela — mas a igreja cristã era pobre e perseguida. O paradoxo "és pobre, mas és rico" é um dos mais profundos do Apocalipse: a riqueza espiritual e a pobreza material coexistem, e Cristo vê a riqueza que o mundo não vê. A referência à "sinagoga de Satanás" é controversa — provavelmente se refere a judeus que denunciavam os cristãos às autoridades romanas, usando sua posição de <em>religio licita</em> (religião legalmente reconhecida) para perseguir os cristãos. "Sê fiel até a morte" — não "até o fim de tua vida", mas "até o ponto de morrer" — um chamado ao martírio. A "coroa da vida" (<em>stephanos</em> — a coroa do atleta vitorioso, não a coroa do rei) é a recompensa do fiel que persevera até o fim.</div>
  </div>

  <div class="igreja-card">
    <div class="ic-header">
      <div class="ic-num">3</div>
      <div>
        <div class="ic-nome">Pérgamo — A Igreja que Mora onde Satanás Tem o Seu Trono</div>
        <div class="ic-local">Ap 2:12–17 · Capital da Ásia Romana · Centro do culto imperial · Biblioteca famosa</div>
      </div>
    </div>
    <div class="ic-grid">
      <div class="ic-item"><div class="ic-label">Elogio</div><div class="ic-valor">Retém o nome de Cristo, não negou a fé mesmo onde Satanás habita, fiel no tempo de Antipas</div></div>
      <div class="ic-item"><div class="ic-label">Repreensão</div><div class="ic-valor">Tolera os que seguem o ensino de Balaão e os nicolaítas — compromisso com a idolatria</div></div>
      <div class="ic-item"><div class="ic-label">Exortação</div><div class="ic-valor">Arrepende-te; caso contrário, virei a ti e guerrearás com a espada da minha boca</div></div>
      <div class="ic-item"><div class="ic-label">Promessa</div><div class="ic-valor">Maná escondido e uma pedra branca com nome novo</div></div>
    </div>
    <div class="ic-analise">Pérgamo era a capital administrativa da província romana da Ásia — a sede do poder imperial na região. O "trono de Satanás" provavelmente se refere ao grande altar de Zeus em Pérgamo (hoje no Museu de Pérgamo em Berlim) ou ao templo do culto imperial. A igreja havia resistido à pressão do culto imperial — mas havia tolerado o ensino de Balaão (compromisso com a idolatria e a imoralidade sexual) e os nicolaítas (um grupo que ensinava que os cristãos podiam participar dos banquetes idolátricos). O "maná escondido" evoca o maná do deserto — o sustento sobrenatural de Deus para seu povo. A "pedra branca com nome novo" é um símbolo de vitória e identidade nova em Cristo.</div>
  </div>

  <div class="igreja-card">
    <div class="ic-header">
      <div class="ic-num">4</div>
      <div>
        <div class="ic-nome">Tiatira — A Igreja Tolerante com Jezabel</div>
        <div class="ic-local">Ap 2:18–29 · Cidade comercial · Famosa pelas corporações de artesãos · Lídia era de lá</div>
      </div>
    </div>
    <div class="ic-grid">
      <div class="ic-item"><div class="ic-label">Elogio</div><div class="ic-valor">Obras, amor, fé, serviço, perseverança — e as últimas obras maiores que as primeiras</div></div>
      <div class="ic-item"><div class="ic-label">Repreensão</div><div class="ic-valor">Tolera Jezabel — uma profetisa que ensina imoralidade e idolatria</div></div>
      <div class="ic-item"><div class="ic-label">Exortação</div><div class="ic-valor">Guardar o que têm até que Cristo venha</div></div>
      <div class="ic-item"><div class="ic-label">Promessa</div><div class="ic-valor">Autoridade sobre as nações; a estrela da manhã</div></div>
    </div>
    <div class="ic-analise">Tiatira era uma cidade de comerciantes e artesãos, organizada em corporações profissionais — cada uma com seu deus patrono e seus banquetes religiosos. Para um cristão em Tiatira, participar de uma corporação significava participar de banquetes idolátricos — uma pressão enorme de conformidade social e econômica. "Jezabel" (nome simbólico, evocando a rainha idólatra de 1 Rs 16–21) era uma profetisa que ensinava que os cristãos podiam participar destes banquetes sem comprometer sua fé. A repreensão de Cristo é severa: ele dará a Jezabel e seus seguidores grande tribulação, a menos que se arrependam. A promessa da "estrela da manhã" é identificada em Ap 22:16 com o próprio Cristo — a recompensa suprema é Cristo mesmo.</div>
  </div>

  <div class="igreja-card">
    <div class="ic-header">
      <div class="ic-num">5</div>
      <div>
        <div class="ic-nome">Sardes — A Igreja que Tem Nome de Viva, mas Está Morta</div>
        <div class="ic-local">Ap 3:1–6 · Antiga capital da Lídia · Famosa por sua riqueza passada · Conquistada de surpresa duas vezes</div>
      </div>
    </div>
    <div class="ic-grid">
      <div class="ic-item"><div class="ic-label">Elogio</div><div class="ic-valor">Alguns poucos que não mancharam suas vestes</div></div>
      <div class="ic-item"><div class="ic-label">Repreensão</div><div class="ic-valor">Tens nome de que vives, mas estás morta; obras incompletas diante de Deus</div></div>
      <div class="ic-item"><div class="ic-label">Exortação</div><div class="ic-valor">Sê vigilante, confirma o que resta, lembra do que recebeste, arrepende-te</div></div>
      <div class="ic-item"><div class="ic-label">Promessa</div><div class="ic-valor">Vestes brancas; nome não apagado do livro da vida; confissão diante do Pai</div></div>
    </div>
    <div class="ic-analise">Sardes havia sido a capital do reino de Creso — o homem mais rico do mundo antigo. Mas sua glória era passada: a cidade havia sido conquistada de surpresa duas vezes (por Ciro em 547 a.C. e por Antíoco em 218 a.C.) porque seus guardas não vigiavam. A igreja de Sardes era espiritualmente análoga à cidade: tinha uma reputação gloriosa, mas estava morta por dentro. A repreensão é a mais severa de todas as cartas — não há elogio substancial, apenas a menção de "alguns poucos" que permaneceram fiéis. "Sê vigilante" — a mesma palavra usada por Jesus em Mateus 24:42 — evoca a história de Sardes: a cidade que não vigiou foi conquistada. A promessa das "vestes brancas" evoca a pureza e a vitória; o "livro da vida" é o registro dos que pertencem a Deus (Ex 32:32; Dn 12:1).</div>
  </div>

  <div class="igreja-card">
    <div class="ic-header">
      <div class="ic-num">6</div>
      <div>
        <div class="ic-nome">Filadélfia — A Igreja da Porta Aberta</div>
        <div class="ic-local">Ap 3:7–13 · Cidade de fronteira · "Pequena Atenas" · Porta para a Ásia interior</div>
      </div>
    </div>
    <div class="ic-grid">
      <div class="ic-item"><div class="ic-label">Elogio</div><div class="ic-valor">Pouca força, mas guardou a palavra de Cristo e não negou o seu nome</div></div>
      <div class="ic-item"><div class="ic-label">Repreensão</div><div class="ic-valor">Nenhuma — Filadélfia é a segunda igreja sem repreensão</div></div>
      <div class="ic-item"><div class="ic-label">Promessa</div><div class="ic-valor">Porta aberta que ninguém pode fechar; proteção na hora da provação; nome de Deus, da Nova Jerusalém e de Cristo</div></div>
    </div>
    <div class="ic-analise">Filadélfia ("amor fraternal") era uma cidade de fronteira — fundada para ser uma "porta" para a helenização da Ásia interior. Cristo usa esta imagem geográfica: "ponho diante de ti uma porta aberta, que ninguém pode fechar." A "porta aberta" provavelmente se refere a oportunidades missionárias — a mesma expressão que Paulo usa em 1 Co 16:9 e 2 Co 2:12. A "sinagoga de Satanás" (como em Esmirna) se refere a judeus que perseguiam os cristãos. A promessa de que eles "virão e se prostrarão a teus pés" evoca Isaías 60:14 — a conversão das nações. A promessa de "guardar da hora da provação" é usada pelos pré-tribulacionistas como argumento para o Arrebatamento pré-tribulacional — mas o contexto sugere proteção na tribulação, não remoção dela.</div>
  </div>

  <div class="igreja-card">
    <div class="ic-header">
      <div class="ic-num">7</div>
      <div>
        <div class="ic-nome">Laodiceia — A Igreja Morna</div>
        <div class="ic-local">Ap 3:14–22 · Cidade bancária e comercial · Famosa por lã negra, colírio e termas</div>
      </div>
    </div>
    <div class="ic-grid">
      <div class="ic-item"><div class="ic-label">Elogio</div><div class="ic-valor">Nenhum — Laodiceia é a única igreja sem elogio</div></div>
      <div class="ic-item"><div class="ic-label">Repreensão</div><div class="ic-valor">Morna — nem fria nem quente; diz "sou rico" mas é miserável, pobre, cega e nua</div></div>
      <div class="ic-item"><div class="ic-label">Exortação</div><div class="ic-valor">Compra ouro refinado, vestes brancas, colírio; sê zeloso e arrepende-te</div></div>
      <div class="ic-item"><div class="ic-label">Promessa</div><div class="ic-valor">Cear com Cristo; sentar no trono com Cristo</div></div>
    </div>
    <div class="ic-analise">Laodiceia era uma das cidades mais ricas da Ásia Menor — um centro bancário, produtor de lã negra famosa e de um colírio medicinal. Quando um terremoto destruiu a cidade em 60 d.C., ela recusou a ajuda imperial e se reconstruiu com seus próprios recursos — um símbolo de autossuficiência orgulhosa. A imagem da água morna é geograficamente precisa: Laodiceia não tinha fonte própria de água — ela recebia água por aqueduto de Hierápolis (água quente, medicinal) ou de Colossos (água fria, refrescante). Quando chegava a Laodiceia, estava morna — inútil. A autossuficiência espiritual de Laodiceia — "sou rico, enriqueci e não preciso de coisa alguma" — é o diagnóstico mais grave de todas as cartas. Cristo está fora da porta, batendo — uma imagem de ternura surpreendente diante da dureza da repreensão: mesmo a pior das igrejas pode ser restaurada se abrir a porta para Cristo.</div>
  </div>

  <div class="reflexao">
    <h3>🙏 Reflexão: Qual Igreja Somos Nós?</h3>
    <p>As sete igrejas do Apocalipse são um espelho para a Igreja em toda época. Cada congregação cristã pode se reconhecer em uma ou mais destas igrejas: a ortodoxia sem amor de Éfeso, a fidelidade sofrida de Esmirna, o compromisso com a cultura de Pérgamo e Tiatira, a reputação sem vida de Sardes, a fidelidade humilde de Filadélfia, a autossuficiência morna de Laodiceia. A pergunta que as cartas nos fazem não é "qual dessas igrejas é a melhor?" — é "qual dessas igrejas somos nós, e o que Cristo nos diz?" O Cristo que conhece as obras de cada igreja também conhece as nossas. Ele elogia, repreende, exorta e promete — com a mesma precisão pastoral que demonstrou às igrejas da Ásia. "Quem tem ouvidos, ouça o que o Espírito diz às igrejas" (Ap 2:7).</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO: VISÃO DO TRONO (Caps. 4–5)
# ============================================================
trono_corpo = """
<div class="sb">
  <h2>👑 A Porta Aberta no Céu</h2>
  <p>Após as sete cartas às igrejas (caps. 2–3), o Apocalipse faz uma transição dramática: "Depois destas coisas, olhei, e eis que havia uma porta aberta no céu" (Ap 4:1). Esta transição não é apenas geográfica (da terra para o céu) — é hermenêutica: ela revela a perspectiva a partir da qual todo o restante do Apocalipse deve ser lido. Antes de ver os julgamentos e tribulações dos capítulos seguintes, João é levado ao céu para ver o que está no centro da realidade: o Trono de Deus. Tudo o que acontece na terra — perseguição, sofrimento, julgamento — deve ser visto à luz deste Trono.</p>
  <p>Os capítulos 4 e 5 formam uma unidade literária — a "cena do trono" — que é o coração teológico do Apocalipse. O capítulo 4 revela quem está no Trono (o Pai); o capítulo 5 revela quem é digno de abrir o livro selado (o Filho, o Cordeiro). Juntos, eles estabelecem a base para todos os julgamentos e promessas que se seguem: Deus está no controle da história, e Cristo — o Cordeiro imolado e ressurreto — é o executor do plano de Deus para a redenção e o julgamento do mundo.</p>
</div>
<div class="sb">
  <h2>📖 Apocalipse 4 — O Trono e o Que Está Sentado Nele</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 4:1–3</div>
    <div class="v-texto">"Logo fiquei em êxtase no Espírito; e eis que havia um trono posto no céu, e alguém assentado no trono. E o que estava assentado era semelhante, na aparência, a uma pedra de jaspe e de sárdio; e havia um arco-íris em volta do trono, semelhante, na aparência, a uma esmeralda."</div>
    <div class="v-analise">João não descreve o que está sentado no Trono com formas humanas — apenas com pedras preciosas (jaspe = brilho cristalino; sárdio = vermelho-sangue) e com um arco-íris esmeralda. Esta reticência é teológica: Deus transcende qualquer imagem humana. O arco-íris evoca Gênesis 9 (o pacto de Noé) e Ezequiel 1:28 (a visão da glória de Deus) — ele é um símbolo da fidelidade de Deus ao seu pacto. O Trono é o centro do universo — tudo o mais orbita em torno dele.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 4:4–8</div>
    <div class="v-texto">"Em volta do trono havia vinte e quatro tronos; e nos tronos estavam assentados vinte e quatro anciãos, vestidos de vestes brancas, e sobre as suas cabeças havia coroas de ouro. Do trono saíam relâmpagos, vozes e trovões. Diante do trono ardiam sete tochas de fogo, que são os sete Espíritos de Deus. Diante do trono havia como um mar de vidro, semelhante ao cristal. No meio do trono e em volta dele havia quatro seres viventes, cheios de olhos por diante e por detrás."</div>
    <div class="v-analise">Os 24 anciãos são interpretados de várias formas: os 12 patriarcas + 12 apóstolos (o povo de Deus do AT e do NT); anjos com funções sacerdotais; ou representantes da Igreja glorificada. Suas coroas (<em>stephanoi</em> — coroas de vitória) e vestes brancas indicam que são vencedores. Os "relâmpagos, vozes e trovões" evocam a teofania do Sinai — a presença de Deus é sempre acompanhada de poder e majestade. Os quatro seres viventes (leão, boi, homem, águia) evocam Ezequiel 1 e representam a criação em sua plenitude — o mais nobre dos animais selvagens, o mais nobre dos animais domésticos, o mais nobre dos seres humanos, o mais nobre das aves. Toda a criação está em adoração diante do Trono.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 4:8–11</div>
    <div class="v-texto">"E os quatro seres viventes, cada um deles com seis asas, estavam cheios de olhos em volta e por dentro; e não cessavam, nem de dia nem de noite, de dizer: Santo, santo, santo é o Senhor Deus, o Todo-Poderoso, aquele que era, e que é, e que há de vir. E quando os seres viventes davam glória, honra e ações de graças ao que estava assentado no trono, ao que vive pelos séculos dos séculos, os vinte e quatro anciãos prostravam-se diante do que estava assentado no trono, e adoravam o que vive pelos séculos dos séculos, e lançavam as suas coroas diante do trono, dizendo: Digno és, Senhor e Deus nosso, de receber a glória, a honra e o poder, porque tu criaste todas as coisas, e por tua vontade existiam e foram criadas."</div>
    <div class="v-analise">O "Santo, santo, santo" (<em>Trisagion</em>) evoca Isaías 6:3 — a visão do Trono que transformou Isaías em profeta. A santidade de Deus — sua alteridade absoluta, sua pureza perfeita, sua glória incomparável — é o fundamento de toda adoração. Os anciãos lançam suas coroas diante do Trono — reconhecendo que qualquer vitória que tenham alcançado é, em última análise, dom de Deus. O hino de adoração do v. 11 é uma confissão de que Deus é digno de toda glória porque ele é o Criador — a existência de todas as coisas depende de sua vontade soberana.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 Apocalipse 5 — O Cordeiro Digno</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 5:1–5</div>
    <div class="v-texto">"Vi na mão direita do que estava assentado no trono um livro escrito por dentro e por fora, selado com sete selos. E vi um anjo poderoso proclamando em grande voz: Quem é digno de abrir o livro e de desatar os seus selos? E ninguém no céu, nem na terra, nem debaixo da terra, podia abrir o livro, nem olhar para ele. E eu chorava muito, porque não havia ninguém digno de abrir o livro, nem de olhar para ele. Mas um dos anciãos me disse: Não chores; eis que o Leão da tribo de Judá, a Raiz de Davi, venceu para abrir o livro e os seus sete selos."</div>
    <div class="v-analise">O livro selado com sete selos representa o plano de Deus para a história — o decreto divino que determina o curso dos eventos até o fim. Ninguém é digno de abrir este livro — nenhum anjo, nenhum ser humano, nenhum poder cósmico. O choro de João é o choro da humanidade diante da aparente ausência de um redentor capaz de executar o plano de Deus. O "Leão da tribo de Judá" evoca Gênesis 49:9–10 (a promessa messiânica a Judá) e Isaías 11:1–10 (o Ramo de Jessé). Mas quando João olha para ver o Leão...</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 5:6–7</div>
    <div class="v-texto">"E vi, no meio do trono e dos quatro seres viventes e no meio dos anciãos, um Cordeiro em pé, como se tivesse sido morto, tendo sete chifres e sete olhos, que são os sete Espíritos de Deus enviados a toda a terra. E ele veio e tomou o livro da mão direita do que estava assentado no trono."</div>
    <div class="v-analise">Este é um dos momentos mais poderosos de toda a Bíblia. João ouve "Leão" — e vê "Cordeiro." Esta inversão é o coração da cristologia do Apocalipse: Cristo venceu não como um leão feroz que devora seus inimigos, mas como um cordeiro que foi imolado. O poder de Deus se manifesta na fraqueza; a vitória divina se realiza pelo sacrifício. "Como se tivesse sido morto" — o Cordeiro carrega as marcas do sacrifício mesmo em sua glória. "Sete chifres" — poder perfeito e completo. "Sete olhos" — onisciência perfeita. O Cordeiro toma o livro — um gesto de autoridade soberana que desencadeia a adoração universal.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 5:9–14</div>
    <div class="v-texto">"E cantavam um novo cântico, dizendo: Digno és de tomar o livro e de abrir os seus selos, porque foste morto e com o teu sangue compraste para Deus homens de toda tribo, língua, povo e nação, e os fizeste para o nosso Deus um reino e sacerdotes; e eles reinarão sobre a terra... Digno é o Cordeiro que foi morto de receber o poder, e riquezas, e sabedoria, e força, e honra, e glória, e louvor."</div>
    <div class="v-analise">O "novo cântico" é o cântico da redenção — o cântico que só pode ser cantado por aqueles que foram redimidos pelo sangue do Cordeiro. A redenção é universal em seu alcance: "de toda tribo, língua, povo e nação" — não apenas Israel, não apenas o Ocidente, mas toda a humanidade. Os redimidos são constituídos "reino e sacerdotes" — evocando Êxodo 19:6 (a vocação de Israel) e 1 Pedro 2:9 (a vocação da Igreja). O hino final enumera sete atributos que pertencem ao Cordeiro: poder, riquezas, sabedoria, força, honra, glória e louvor — a plenitude de tudo o que existe pertence a Cristo.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: O Leão que é Cordeiro</h3>
    <p>A visão do capítulo 5 — o Leão que é o Cordeiro — é a chave hermenêutica para todo o Apocalipse. Ela nos diz como Deus age na história: não pela força bruta do leão que devora, mas pelo sacrifício do cordeiro que é imolado. Esta é a lógica da Cruz — a lógica que inverte todos os valores do mundo. O mundo diz que o poder vence; Deus diz que o amor sacrificial vence. O mundo diz que a força conquista; Deus diz que a fraqueza redime. O mundo diz que os mortos perdem; Deus diz que o Cordeiro morto e ressurreto reina. Para os cristãos perseguidos de Patmos — e para os cristãos perseguidos de hoje — esta visão é a mais poderosa das esperanças: o mesmo Cordeiro que foi imolado está no centro do Trono, e nenhum poder do mundo pode mudar isso.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO: HERMENÊUTICA
# ============================================================
herm_corpo = """
<div class="sb">
  <h2>🔍 Por Que a Hermenêutica do Apocalipse é Tão Importante?</h2>
  <p>Nenhum livro da Bíblia foi mais mal interpretado do que o Apocalipse — e nenhum livro produziu mais danos quando mal interpretado. Ao longo da história, o Apocalipse foi usado para justificar guerras, perseguições, movimentos sectários e previsões apocalípticas que invariavelmente se provaram falsas. Cada geração de cristãos tendeu a ver nos símbolos do Apocalipse referências aos eventos de sua própria época — Napoleão, Hitler, Stalin, a União Soviética, o Código de Barras, o chip de identificação, a União Europeia. Todas estas identificações foram eventualmente abandonadas — mas o padrão continua.</p>
  <p>A hermenêutica — a ciência e a arte da interpretação — é especialmente crucial para o Apocalipse porque ele usa um gênero literário (a apocalíptica) que é profundamente diferente dos gêneros que estamos acostumados a ler. Quando lemos uma carta de Paulo, sabemos que devemos interpretá-la como uma carta — com suas convenções retóricas, seu contexto histórico e seu propósito pastoral. Quando lemos o Apocalipse, precisamos saber que estamos lendo apocalíptica — um gênero que usa símbolos, números e imagens de forma muito diferente da linguagem literal.</p>
</div>
<div class="sb">
  <h2>📏 Princípios para Interpretar o Apocalipse</h2>
  <div class="bloco">
    <div class="bt">1. O Gênero Determina a Interpretação</div>
    <div class="bx">O Apocalipse é simultaneamente uma carta (Ap 1:4 — "João, às sete igrejas"), uma profecia (Ap 1:3 — "as palavras desta profecia") e uma apocalipse (Ap 1:1 — "revelação"). Cada um destes gêneros tem suas próprias convenções interpretativas. Como carta, deve ser interpretado à luz de seu contexto histórico e dos destinatários originais. Como profecia, aponta para cumprimentos históricos e escatológicos. Como apocalipse, usa símbolos e imagens que não devem ser interpretados literalmente, mas que têm significados específicos enraizados no AT e na tradição judaica.</div>
  </div>
  <div class="bloco">
    <div class="bt">2. O Antigo Testamento é a Chave</div>
    <div class="bx">O Apocalipse tem 278 alusões ao AT — mais do que qualquer outro livro do NT. João nunca cita o AT diretamente (com a fórmula "está escrito"), mas o permeia de alusões e ecos. Para interpretar o Apocalipse, é preciso conhecer Daniel, Ezequiel, Isaías, Zacarias, Jeremias e os Salmos. O Dragão de Ap 12 não pode ser entendido sem o Leviatã dos Salmos e de Jó. A Besta de Ap 13 não pode ser entendida sem as bestas de Daniel 7. A Nova Jerusalém de Ap 21–22 não pode ser entendida sem Ezequiel 40–48 e Isaías 60–66.</div>
  </div>
  <div class="bloco">
    <div class="bt">3. Os Números São Simbólicos</div>
    <div class="bx">Os números do Apocalipse não são literais — são simbólicos. O 7 representa perfeição e completude. O 12 representa o povo de Deus. O 1.000 representa uma grande quantidade ou um longo período. O 144.000 (12 × 12 × 1.000) representa a plenitude do povo de Deus — não um número literal de 144.000 judeus. O 3½ (metade de 7) representa um período limitado de tribulação — "tempo, tempos e metade de um tempo" (Dn 7:25; Ap 12:14) = 42 meses = 1.260 dias. Interpretar estes números literalmente leva a conclusões absurdas e contradições internas.</div>
  </div>
  <div class="bloco">
    <div class="bt">4. A Recapitulação — Não Cronologia Linear</div>
    <div class="bx">O Apocalipse não segue uma cronologia linear — ele usa a técnica da recapitulação: as séries de 7 selos, 7 trombetas e 7 taças são visões paralelas do mesmo período histórico (a era da Igreja), não eventos sequenciais. Evidências desta recapitulação: (a) o 6º selo (Ap 6:12–17) descreve o fim do mundo — mas o livro continua por mais 16 capítulos; (b) a 7ª trombeta (Ap 11:15–19) anuncia o reino eterno de Cristo — mas o livro continua; (c) as 7 taças (Ap 16) são "as últimas pragas" — mas são seguidas por mais visões. Cada série recapitula o período da Igreja com intensidade crescente.</div>
  </div>
  <div class="bloco">
    <div class="bt">5. O Contexto Histórico é Indispensável</div>
    <div class="bx">O Apocalipse foi escrito para cristãos específicos em cidades específicas em um momento histórico específico — a perseguição de Domiciano (c. 95–96 d.C.). Qualquer interpretação que ignore este contexto histórico e trata o Apocalipse como se fosse escrito diretamente para o século XXI está cometendo um erro hermenêutico fundamental. Isto não significa que o Apocalipse não tem relevância para hoje — significa que sua relevância para hoje deve ser derivada de sua relevância para o século I, não imposta sobre ele.</div>
  </div>
  <div class="bloco">
    <div class="bt">6. O Propósito Pastoral é Central</div>
    <div class="bx">O Apocalipse foi escrito para consolar e fortalecer cristãos perseguidos — não para satisfazer a curiosidade especulativa sobre o futuro. Quando a interpretação do Apocalipse produz medo, divisão, especulação ociosa ou desengajamento do mundo, ela está servindo a um propósito oposto ao do livro. A pergunta hermenêutica fundamental não é "quando isso vai acontecer?" mas "o que este livro me diz sobre Deus, sobre Cristo, sobre a Igreja e sobre como devo viver hoje?"</div>
  </div>
</div>
<div class="sb">
  <h2>⚠️ Erros Comuns na Interpretação do Apocalipse</h2>
  <table>
    <tr><th>Erro</th><th>Exemplo</th><th>O Problema</th></tr>
    <tr><td>Literalismo excessivo</td><td>Os 144.000 são exatamente 144.000 judeus</td><td>Ignora o simbolismo numérico do Apocalipse</td></tr>
    <tr><td>Identificação com eventos contemporâneos</td><td>A Besta é [insira o vilão da sua época]</td><td>Cada geração errou nesta identificação</td></tr>
    <tr><td>Ignorar o contexto histórico</td><td>O Apocalipse fala diretamente ao século XXI</td><td>Ignora os destinatários originais do livro</td></tr>
    <tr><td>Cronologia linear</td><td>Os selos, trombetas e taças são sequenciais</td><td>Contradiz as evidências internas do livro</td></tr>
    <tr><td>Especulação sobre datas</td><td>Cristo voltará em [data específica]</td><td>Jesus disse que ninguém sabe o dia nem a hora</td></tr>
    <tr><td>Ignorar o AT</td><td>Interpretar os símbolos sem referência ao AT</td><td>O Apocalipse é incompreensível sem o AT</td></tr>
  </table>
  <div class="reflexao">
    <h3>🙏 Reflexão: A Humildade Hermenêutica</h3>
    <p>A história da interpretação do Apocalipse é uma história de humildade necessária. Cada geração que tentou identificar os símbolos do Apocalipse com eventos específicos de sua época acabou se enganando. Isto não significa que o Apocalipse é incompreensível — significa que ele é mais rico e mais profundo do que qualquer interpretação específica pode capturar. A postura hermenêutica mais sábia diante do Apocalipse é a de um estudante humilde que reconhece que o livro tem camadas de significado que transcendem qualquer época específica, que aprende com as quatro tradições interpretativas sem se prender dogmaticamente a nenhuma delas, e que mantém o foco no que o livro claramente ensina: que Deus está no controle da história, que Cristo é o Senhor soberano, que o mal será derrotado, e que a esperança final do povo de Deus é a Nova Criação. "Maranata — vem, Senhor Jesus!" (Ap 22:20).</p>
  </div>
</div>
"""

MODULOS_F1 = [
    {
        "pasta": "introducao",
        "cor": "#c084fc",
        "hero_bg": "#0d0520",
        "titulo": "Introdução ao Apocalipse",
        "subtitulo": "📜 Introdução · Gênero · Estrutura",
        "ref": "Autor · Data · Gênero Apocalíptico · 4 Escolas de Interpretação",
        "citacao": "Bem-aventurado aquele que lê, e os que ouvem as palavras desta profecia e guardam as coisas nela escritas; porque o tempo está próximo.",
        "autor_cit": "Apocalipse 1:3 — a primeira das sete bem-aventuranças do Apocalipse",
        "corpo": intro_corpo,
        "nav_prev": "/12-apocalipse/index.html",
        "nav_prev_lbl": "← Índice Bloco 12",
        "nav_next": "/12-apocalipse/joao-patmos",
        "nav_next_lbl": "João em Patmos →",
    },
    {
        "pasta": "joao-patmos",
        "cor": "#fbbf24",
        "hero_bg": "#1a1000",
        "titulo": "João em Patmos — A Visão do Filho do Homem",
        "subtitulo": "🏝️ Apocalipse 1 · Patmos · Cristo Glorificado",
        "ref": "Ap 1:1–20 · Exílio · Visão Inaugural · Sete Candeeiros",
        "citacao": "Não temas; eu sou o Primeiro e o Último, e o que vive; estive morto, mas eis que estou vivo pelos séculos dos séculos, e tenho as chaves da morte e do Hades.",
        "autor_cit": "Apocalipse 1:17–18 — Cristo ao apóstolo João em Patmos",
        "corpo": joao_corpo,
        "nav_prev": "/12-apocalipse/introducao",
        "nav_prev_lbl": "← Introdução",
        "nav_next": "/12-apocalipse/sete-igrejas",
        "nav_next_lbl": "As 7 Igrejas →",
    },
    {
        "pasta": "sete-igrejas",
        "cor": "#22d3ee",
        "hero_bg": "#001a1f",
        "titulo": "As 7 Igrejas da Ásia Menor",
        "subtitulo": "⛪ Apocalipse 2–3 · As 7 Cartas",
        "ref": "Éfeso · Esmirna · Pérgamo · Tiatira · Sardes · Filadélfia · Laodiceia",
        "citacao": "Quem tem ouvidos, ouça o que o Espírito diz às igrejas.",
        "autor_cit": "Refrão repetido nas 7 cartas — Apocalipse 2:7, 11, 17, 29; 3:6, 13, 22",
        "corpo": igrejas_corpo,
        "nav_prev": "/12-apocalipse/joao-patmos",
        "nav_prev_lbl": "← João em Patmos",
        "nav_next": "/12-apocalipse/visao-trono",
        "nav_next_lbl": "Visão do Trono →",
    },
    {
        "pasta": "visao-trono",
        "cor": "#fbbf24",
        "hero_bg": "#1a1200",
        "titulo": "A Visão do Trono e o Cordeiro",
        "subtitulo": "👑 Apocalipse 4–5 · O Trono Celestial",
        "ref": "Ap 4–5 · 24 Anciãos · 4 Seres Viventes · O Leão que é Cordeiro",
        "citacao": "Digno é o Cordeiro que foi morto de receber o poder, e riquezas, e sabedoria, e força, e honra, e glória, e louvor.",
        "autor_cit": "Apocalipse 5:12 — o hino de adoração ao Cordeiro",
        "corpo": trono_corpo,
        "nav_prev": "/12-apocalipse/sete-igrejas",
        "nav_prev_lbl": "← As 7 Igrejas",
        "nav_next": "/12-apocalipse/sete-selos",
        "nav_next_lbl": "Os 7 Selos →",
    },
    {
        "pasta": "hermeneutica",
        "cor": "#c084fc",
        "hero_bg": "#0d0520",
        "titulo": "Como Interpretar o Apocalipse",
        "subtitulo": "🔍 Hermenêutica · 4 Escolas · Princípios",
        "ref": "Preterismo · Historicismo · Futurismo · Idealismo · Erros Comuns",
        "citacao": "A revelação de Jesus Cristo, que Deus lhe deu para mostrar aos seus servos as coisas que em breve devem acontecer.",
        "autor_cit": "Apocalipse 1:1 — o propósito declarado do livro: revelar, não esconder",
        "corpo": herm_corpo,
        "nav_prev": "/12-apocalipse/nova-jerusalem",
        "nav_prev_lbl": "← Nova Jerusalém",
        "nav_next": "/12-apocalipse/index.html",
        "nav_next_lbl": "Índice Bloco 12 →",
    },
]


def main():
    for m in MODULOS_F1:
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
    print("\n🎉 Fase 1 do Bloco 12 completa!")


if __name__ == "__main__":
    main()
