#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os módulos da fase 3 do Bloco 12 — Babilônia, Milênio e Nova Jerusalém."""

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
    th { padding: 10px 14px; text-align: left; font-weight: 700; }
    td { padding: 10px 14px; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; }
    tr:hover td { background: rgba(255,255,255,0.02); }
    .nav-mod { display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.07); flex-wrap: wrap; gap: 10px; }
    .nav-mod a { padding: 10px 20px; border-radius: 8px; font-size: 0.88rem; font-weight: 700; transition: all 0.2s; }
    .reflexao { border-radius: 12px; padding: 22px 26px; margin-top: 32px; background: rgba(34,197,94,0.05); border: 1px solid rgba(34,197,94,0.15); }
    .reflexao h3 { color: #22c55e; font-size: 0.95rem; font-weight: 800; margin-bottom: 10px; }
    .reflexao p { color: #94a3b8; font-size: 0.9rem; line-height: 1.82; margin-bottom: 10px; }
    .reflexao p:last-child { margin-bottom: 0; }
    .escola-card { border-radius: 12px; padding: 20px 22px; margin-bottom: 16px; border: 1px solid rgba(255,255,255,0.07); background: rgba(255,255,255,0.02); }
    .ec-titulo { font-size: 1rem; font-weight: 800; margin-bottom: 6px; }
    .ec-desc { font-size: 0.9rem; color: #94a3b8; line-height: 1.8; }
    .destaque { border-radius: 14px; padding: 24px 28px; margin-bottom: 24px; }
    .destaque h3 { font-size: 1.05rem; font-weight: 800; margin-bottom: 12px; }
    .destaque p { font-size: 0.92rem; line-height: 1.85; margin-bottom: 10px; }
    .destaque p:last-child { margin-bottom: 0; }
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
    .ec-titulo {{ color: {cor}; }}
    .destaque {{ background: {cor}08; border: 1px solid {cor}20; }}
    .destaque h3 {{ color: {cor}; }}
    .destaque p {{ color: #94a3b8; }}
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
# MÓDULO: BABILÔNIA (Caps. 17–18)
# ============================================================
babilonia_corpo = """
<div class="sb">
  <h2>🏛️ Babilônia — O Símbolo do Poder Mundano</h2>
  <p>Os capítulos 17–18 do Apocalipse são dedicados à queda de "Babilônia, a Grande" — um dos símbolos mais poderosos e complexos de todo o livro. Babilônia não é apenas a cidade histórica no rio Eufrates — ela é um símbolo teológico de qualquer sistema político, econômico e cultural que se opõe a Deus, que seduz as nações com suas riquezas e prazeres, e que persegue os fiéis. No contexto do século I, Babilônia era claramente Roma — a cidade sobre sete montes (Ap 17:9), a grande potência imperial que governava o mundo mediterrâneo e perseguia os cristãos. Mas Babilônia transcende Roma: ela é qualquer "Roma" de qualquer época — qualquer poder que exige lealdade absoluta e persegue aqueles que recusam.</p>
  <p>A imagem de Babilônia como "Grande Prostituta" (Ap 17:1) é chocante — mas tem raízes profundas nos profetas do AT. Isaías, Jeremias, Ezequiel e Naum usam a metáfora da prostituição para descrever cidades e nações que seduzem outras nações com suas riquezas e poder, corrompendo-as e afastando-as de Deus (Is 23:17; Na 3:4). A prostituição de Babilônia não é sexual — é espiritual e política: ela seduz os reis da terra com suas riquezas e os mercadores com seus lucros, corrompendo-os e fazendo-os participar de sua idolatria e injustiça.</p>
</div>
<div class="sb">
  <h2>📖 Apocalipse 17 — A Grande Prostituta</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 17:1–6</div>
    <div class="v-texto">"Vem, mostrar-te-ei o julgamento da grande prostituta que está sentada sobre muitas águas, com a qual os reis da terra se prostituíram, e os habitantes da terra se embriagaram com o vinho de sua prostituição... E vi a mulher embriagada com o sangue dos santos e com o sangue das testemunhas de Jesus."</div>
    <div class="v-analise">A Prostituta está "sentada sobre muitas águas" — Ap 17:15 explica que as águas são "povos, multidões, nações e línguas" — o poder global de Babilônia. Ela está "embriagada com o sangue dos santos" — a perseguição dos cristãos é parte integrante do sistema de Babilônia. A taça de ouro "cheia de abominações" (Ap 17:4) é a antítese das taças de ouro do templo — Babilônia perverte e falsifica a adoração verdadeira. O contraste com a Mulher do capítulo 12 é deliberado: a Mulher vestida de sol representa o povo de Deus; a Prostituta representa o sistema do mundo. Cada ser humano está, em algum sentido, escolhendo entre estas duas mulheres.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 17:7–18</div>
    <div class="v-texto">"E o anjo me disse: Por que te admiraste? Eu te direi o mistério da mulher e da besta que a carrega, que tem as sete cabeças e os dez chifres... As sete cabeças são sete montes sobre os quais a mulher está sentada. São também sete reis: cinco já caíram, um existe, o outro ainda não veio."</div>
    <div class="v-analise">As "sete cabeças" têm duplo significado: sete montes (Roma era famosa como "a cidade sobre sete montes") e sete reis (sete impérios ou imperadores). A identificação dos sete reis é debatida: podem ser sete imperadores romanos (Augusto, Tibério, Calígula, Cláudio, Nero, Vespasiano, Domiciano), ou podem ser sete impérios históricos (Egito, Assíria, Babilônia, Pérsia, Grécia, Roma, e um futuro). Os "dez chifres" são dez reis que ainda não receberam reino — poderes que se aliarão à Besta no fim. A aliança final entre a Besta e os reis da terra contra o Cordeiro (Ap 17:14) é o Armagedom — e o resultado é certo: "o Cordeiro os vencerá, porque é Senhor dos senhores e Rei dos reis."</div>
  </div>
</div>
<div class="sb">
  <h2>📖 Apocalipse 18 — A Queda de Babilônia</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 18:1–8</div>
    <div class="v-texto">"Depois disto, vi outro anjo descer do céu, com grande autoridade; e a terra foi iluminada com a sua glória. E clamou em grande voz, dizendo: Caiu, caiu a grande Babilônia, e se tornou habitação de demônios... Saí dela, povo meu, para que não sejais participantes dos seus pecados e para que não recebais as suas pragas."</div>
    <div class="v-analise">"Caiu, caiu a grande Babilônia" — o anúncio profético usa o passado (o "passado profético" hebraico) para descrever um evento futuro como se já tivesse acontecido — tão certo é o julgamento de Deus. O chamado "Saí dela, povo meu" evoca Isaías 48:20 e Jeremias 51:45 — o chamado ao exílio babilônico para sair antes do julgamento. Para os cristãos do século I, este era um chamado a não se comprometer com o sistema romano — a não participar de sua idolatria, sua injustiça e sua violência. Para os cristãos de hoje, é um chamado ao discernimento: quais aspectos da cultura contemporânea são "Babilônia" — sistemas que nos seduzem e nos corrompem — e dos quais precisamos "sair"?</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 18:9–19 — O Lamento dos Reis e Mercadores</div>
    <div class="v-texto">"E os reis da terra, que se prostituíram e viveram na devassidão com ela, chorarão e se lamentarão sobre ela, quando virem a fumaça do seu incêndio, parados à distância por causa do medo do seu tormento, dizendo: Ai, ai, a grande cidade, Babilônia, a cidade forte! Pois em uma hora chegou o teu julgamento."</div>
    <div class="v-analise">O lamento dos reis, mercadores e marinheiros (Ap 18:9–19) é uma das seções mais literariamente elaboradas do Apocalipse — uma elegia fúnebre que evoca os lamentos de Ezequiel sobre Tiro (Ez 27). A lista de mercadorias de Babilônia (Ap 18:12–13) é um catálogo do luxo do Império Romano — ouro, prata, pedras preciosas, linho, madeira, marfim, especiarias, vinho, azeite, trigo, animais, cavalos, carruagens, e — no final, chocantemente — "corpos e almas de homens" (escravos). O sistema econômico de Babilônia é construído sobre a escravidão e a exploração. O lamento dos mercadores não é arrependimento — é luto pela perda de seus lucros. Eles choram não por Babilônia, mas por seus negócios.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 18:20–24 — O Regozijo do Céu</div>
    <div class="v-texto">"Alegra-te sobre ela, ó céu, e vós, santos, apóstolos e profetas; porque Deus julgou o vosso julgamento sobre ela... E em ti foi achado o sangue de profetas e de santos e de todos os que foram mortos sobre a terra."</div>
    <div class="v-analise">O contraste entre o lamento da terra e o regozijo do céu é deliberado: o que a terra chora (a perda de seus lucros), o céu celebra (a justiça de Deus). O gesto do anjo que lança uma pedra como uma grande mó no mar (Ap 18:21) evoca a profecia de Jeremias sobre a queda de Babilônia (Jr 51:63–64). "Em ti foi achado o sangue de profetas e de santos" — a acusação final contra Babilônia é a perseguição dos fiéis. O sistema que parecia invencível — o maior império da história — é julgado por Deus e cai em "uma hora." Nenhum poder humano é eterno; apenas o reino de Deus dura para sempre.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: Onde Está Babilônia Hoje?</h3>
    <p>A queda de Babilônia no Apocalipse não é apenas uma profecia sobre Roma — é um padrão que se repete na história. Cada grande potência que construiu seu poder sobre a exploração, a idolatria e a perseguição dos fiéis eventualmente caiu: Roma, o Império Mongol, o Colonialismo europeu, os regimes totalitários do século XX. O chamado "Saí dela, povo meu" não é um chamado ao isolamento do mundo — é um chamado ao discernimento e à não-conformidade. Os cristãos vivem no mundo, mas não são do mundo (Jo 17:16). Eles participam da vida econômica, cultural e política de sua época — mas recusam-se a dar a César o que pertence a Deus. A questão não é "onde está Babilônia?" mas "onde estou eu em relação a ela?"</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO: MILÊNIO E JULGAMENTO FINAL (Caps. 19–20)
# ============================================================
milenio_corpo = """
<div class="sb">
  <h2>⚔️ A Vitória de Cristo e o Milênio</h2>
  <p>Os capítulos 19–20 do Apocalipse descrevem a vitória final de Cristo e o julgamento definitivo — o clímax do conflito que o livro inteiro tem preparado. Eles começam com o hino de "Aleluia" do céu (Ap 19:1–8) — a primeira e única vez que esta palavra hebraica aparece no NT — e culminam com o Grande Trono Branco do Juízo Final (Ap 20:11–15). Entre estes dois pontos, encontramos a batalha final (Ap 19:11–21), o Milênio (Ap 20:1–6), a soltura e derrota final de Satanás (Ap 20:7–10) e o Juízo Final (Ap 20:11–15).</p>
  <p>O Milênio (Ap 20:1–6) — o reinado de 1.000 anos — é um dos temas mais debatidos de toda a escatologia cristã. As quatro posições principais (Pré-Milenarismo, Pós-Milenarismo, Amilenarismo e Pré-Tribulacionismo) representam interpretações radicalmente diferentes do mesmo texto. Este debate não é apenas acadêmico — ele afeta profundamente a forma como os cristãos entendem a história, a missão da Igreja e a esperança cristã. Uma compreensão cuidadosa das quatro posições é essencial para uma escatologia madura e equilibrada.</p>
</div>
<div class="sb">
  <h2>📖 Apocalipse 19 — O Cavaleiro Branco e a Ceia das Núpcias</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 19:1–8 — O Aleluia do Céu</div>
    <div class="v-texto">"Depois disto, ouvi como que uma grande voz de numerosa multidão no céu, dizendo: Aleluia! A salvação, a glória e o poder pertencem ao nosso Deus... E ouvi como que a voz de numerosa multidão e como que o ruído de muitas águas e como que o ruído de fortes trovões, dizendo: Aleluia! Porque o Senhor nosso Deus, o Todo-Poderoso, reina. Alegremo-nos e regozijemo-nos e demos-lhe a glória, porque chegou o casamento do Cordeiro, e a sua esposa se preparou."</div>
    <div class="v-analise">"Aleluia" (hebraico: <em>Hallelu-Yah</em> — "Louvai a YHWH") aparece quatro vezes neste capítulo (vv. 1, 3, 4, 6) — a única ocorrência no NT. O quádruplo "Aleluia" é a resposta do céu à queda de Babilônia (cap. 18) — a justiça de Deus é motivo de adoração. "O casamento do Cordeiro" é a metáfora final da relação entre Cristo e a Igreja — a consumação da aliança que começou no AT (Israel como esposa de Deus) e foi renovada no NT (a Igreja como noiva de Cristo). A "esposa se preparou" — a Igreja não é passiva na preparação para o casamento; ela se prepara através da fidelidade e das "obras justas dos santos" (Ap 19:8).</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 19:11–16 — O Cavaleiro Branco</div>
    <div class="v-texto">"E vi o céu aberto, e eis um cavalo branco, e o que estava montado nele se chamava Fiel e Verdadeiro, e com justiça julga e peleja. Seus olhos eram como chama de fogo, e sobre a sua cabeça havia muitas coroas; e tinha um nome escrito que ninguém conhecia, senão ele mesmo... E o seu nome é chamado: A Palavra de Deus... E tem na sua veste e na sua coxa um nome escrito: Rei dos reis e Senhor dos senhores."</div>
    <div class="v-analise">O Cavaleiro Branco de Apocalipse 19 é claramente Cristo — em contraste com o cavaleiro branco ambíguo do 1º selo (Ap 6:2). Os títulos são inequívocos: "Fiel e Verdadeiro" (Ap 3:14), "A Palavra de Deus" (Jo 1:1), "Rei dos reis e Senhor dos senhores" (Ap 17:14). A "espada afiada" que sai de sua boca (Ap 19:15) é a palavra de Deus que julga — não uma espada literal. A batalha final não é uma batalha militar convencional — é o julgamento de Cristo sobre os poderes do mal através de sua palavra soberana. O "lagar do vinho do furor da ira de Deus" evoca Isaías 63:1–6 — o Messias que pisa o lagar do julgamento.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 Apocalipse 20:1–6 — O Milênio</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 20:1–6</div>
    <div class="v-texto">"E vi um anjo descer do céu, tendo a chave do abismo e uma grande corrente na mão. E prendeu o dragão, a antiga serpente, que é o Diabo e Satanás, e o amarrou por mil anos... E vi tronos, e os que estavam assentados neles receberam autoridade para julgar; e vi as almas dos que foram decapitados por causa do testemunho de Jesus e por causa da palavra de Deus... E reinaram com Cristo durante mil anos."</div>
    <div class="v-analise">O "mil anos" (<em>chilia etē</em>) é o período do Milênio — e sua interpretação divide os cristãos em quatro campos principais. A amarração de Satanás (Ap 20:2–3) é descrita como impedindo-o de "enganar as nações" — o que o Amilenarismo interpreta como a limitação do poder de Satanás durante a era da Igreja (cf. Mt 12:29; Lc 10:18; Jo 12:31). Os "tronos" e o "reinado com Cristo" podem se referir ao reinado presente dos mártires com Cristo no céu (a "primeira ressurreição" como ressurreição espiritual) ou a um reinado futuro literal na terra. A "primeira ressurreição" (Ap 20:5–6) é interpretada como ressurreição espiritual (regeneração — Jo 5:25; Ef 2:6) pelos Amilenaristas, ou como ressurreição física dos santos antes do Milênio pelos Pré-Milenaristas.</div>
  </div>
  <h2>📊 As Quatro Posições sobre o Milênio</h2>
  <div class="escola-card">
    <div class="ec-titulo">1. Amilenarismo — "O Milênio é Simbólico"</div>
    <div class="ec-desc">O Amilenarismo (defendido por Agostinho, Calvino, Berkhof, Hoekema) interpreta o "mil anos" como um número simbólico representando o período entre a primeira e a segunda vinda de Cristo — a era da Igreja. O reinado de Cristo é presente e espiritual (os cristãos já reinam com Cristo — Ef 2:6; Cl 3:1). A amarração de Satanás é a limitação de seu poder realizada pela Cruz (Jo 12:31; Cl 2:15). A "primeira ressurreição" é a regeneração ou a ressurreição dos mártires que já estão com Cristo. Esta é a posição dominante na tradição reformada e em grande parte da tradição católica e ortodoxa.</div>
  </div>
  <div class="escola-card">
    <div class="ec-titulo">2. Pós-Milenarismo — "Cristo Volta Depois do Milênio"</div>
    <div class="ec-desc">O Pós-Milenarismo (defendido por Jonathan Edwards, Charles Hodge, B.B. Warfield) interpreta o Milênio como um período futuro de grande prosperidade e expansão do Evangelho — quando a maior parte da humanidade será convertida e o mundo será transformado pelo Evangelho — antes do retorno de Cristo. O Milênio não é necessariamente literal de 1.000 anos — é um longo período de triunfo do Evangelho. Cristo volta depois (pós) deste período de prosperidade. Esta posição foi muito influente no protestantismo do século XIX, mas perdeu força após as guerras mundiais do século XX.</div>
  </div>
  <div class="escola-card">
    <div class="ec-titulo">3. Pré-Milenarismo Histórico — "Cristo Volta Antes do Milênio"</div>
    <div class="ec-desc">O Pré-Milenarismo Histórico (defendido por Justino Mártir, Ireneu, Papias, e modernamente por George Ladd, Wayne Grudem) interpreta o Milênio como um período futuro literal de 1.000 anos em que Cristo reinará na terra após seu retorno. A "primeira ressurreição" é a ressurreição física dos santos antes do Milênio. A Igreja passa pela Grande Tribulação antes do retorno de Cristo. Esta posição tem raízes na tradição patrística mais antiga e é defendida por muitos estudiosos evangélicos conservadores.</div>
  </div>
  <div class="escola-card">
    <div class="ec-titulo">4. Dispensacionalismo Pré-Tribulacional — "O Arrebatamento Secreto"</div>
    <div class="ec-desc">O Dispensacionalismo (sistematizado por John Nelson Darby no século XIX, popularizado pelo Scofield Reference Bible e pela série Left Behind) acrescenta ao Pré-Milenarismo a doutrina do "Arrebatamento secreto" — a remoção da Igreja da terra antes da Grande Tribulação. Esta posição distingue radicalmente entre Israel e a Igreja, e interpreta grande parte do Apocalipse como se referindo exclusivamente a Israel durante a Tribulação. Embora seja a posição mais popular no evangelicalismo americano, ela é relativamente recente (século XIX) e não tem precedente na tradição cristã anterior a Darby.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 Apocalipse 20:7–15 — O Julgamento Final</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 20:7–10 — Satanás Solto e Derrotado</div>
    <div class="v-texto">"E quando os mil anos se completarem, Satanás será solto da sua prisão, e sairá para enganar as nações que estão nos quatro cantos da terra, Gogue e Magogue, para reuni-las para a batalha... E o diabo, que as enganava, foi lançado no lago de fogo e enxofre, onde estão a besta e o falso profeta; e serão atormentados dia e noite pelos séculos dos séculos."</div>
    <div class="v-analise">A soltura final de Satanás e sua derrota definitiva revelam que mesmo após o Milênio — seja ele simbólico ou literal — haverá uma última rebelião. "Gogue e Magogue" evoca Ezequiel 38–39 — os inimigos escatológicos de Israel — mas no Apocalipse eles representam todas as nações que se opõem a Deus no fim. A derrota de Satanás é total e definitiva: ele é "lançado no lago de fogo e enxofre" — o mesmo destino da Besta e do Falso Profeta (Ap 19:20). O "lago de fogo" é o símbolo do julgamento eterno — a separação definitiva de Deus.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 20:11–15 — O Grande Trono Branco</div>
    <div class="v-texto">"E vi um grande trono branco e aquele que estava assentado nele, de cuja face fugiram a terra e o céu, e não se achou lugar para eles. E vi os mortos, os grandes e os pequenos, em pé diante do trono, e os livros foram abertos; e outro livro foi aberto, que é o livro da vida; e os mortos foram julgados pelas coisas que estavam escritas nos livros, segundo as suas obras."</div>
    <div class="v-analise">O Grande Trono Branco é a cena do Juízo Final — o julgamento de todos os mortos, "grandes e pequenos." A universalidade do julgamento é enfatizada: ninguém escapa — nem os poderosos nem os humildes. Os "livros" representam o registro das obras humanas — o princípio da responsabilidade moral. O "livro da vida" é o registro dos que pertencem a Deus — a base da salvação não é as obras, mas a graça de Deus que escreve os nomes no livro da vida (cf. Fp 4:3; Ap 3:5; 13:8; 17:8). "A morte e o Hades foram lançados no lago de fogo" — a morte, o último inimigo (1 Co 15:26), é finalmente destruída. "Esta é a segunda morte, o lago de fogo" — a separação eterna de Deus.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: O Julgamento e a Graça</h3>
    <p>O Juízo Final do Apocalipse é uma das doutrinas mais desconfortáveis da fé cristã — e uma das mais necessárias. Sem julgamento, não há justiça; sem justiça, não há esperança para as vítimas da história. O Juízo Final é a garantia de que o sofrimento dos mártires, a injustiça dos opressores e o mal que parece triunfar na história não terão a última palavra. Deus terá a última palavra — e ela será justa. Mas o Juízo Final também é uma chamada à humildade: "os mortos foram julgados pelas coisas que estavam escritas nos livros, segundo as suas obras." Nossas obras importam — não como base da salvação, mas como evidência de quem somos. A graça que salva também transforma — e a transformação se manifesta em obras. A esperança do cristão diante do Juízo Final não é a confiança em suas próprias obras, mas a confiança no Cordeiro cujo nome está escrito no livro da vida.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO: NOVA JERUSALÉM (Caps. 21–22)
# ============================================================
nova_jerusalem_corpo = """
<div class="sb">
  <h2>🌟 A Nova Criação — O Clímax da Bíblia</h2>
  <p>Os capítulos 21–22 do Apocalipse são o clímax não apenas do Apocalipse, mas de toda a Bíblia. Eles descrevem a consumação de tudo o que Deus prometeu desde Gênesis 1 — a restauração da criação, a eliminação do pecado e da morte, e a comunhão perfeita e eterna entre Deus e seu povo. A Nova Jerusalém não é apenas o fim da história — é o começo de uma nova história, uma história sem fim, em que a humanidade redimida vive em comunhão plena com o Criador no novo céu e na nova terra.</p>
  <p>A visão da Nova Jerusalém é construída sobre centenas de alusões ao AT — especialmente Ezequiel 40–48 (a visão do templo restaurado), Isaías 60–66 (a glória futura de Sião) e Gênesis 1–3 (o Éden original). A Nova Jerusalém não é apenas um retorno ao Éden — é muito mais do que o Éden. O Éden era um jardim; a Nova Jerusalém é uma cidade-jardim. O Éden tinha a possibilidade do pecado; a Nova Jerusalém não tem mais pecado. O Éden tinha a árvore da vida; a Nova Jerusalém tem a árvore da vida no meio de uma cidade inteira. A nova criação é a velha criação transfigurada e glorificada — não destruída, mas renovada.</p>
</div>
<div class="sb">
  <h2>📖 Apocalipse 21:1–8 — O Novo Céu e a Nova Terra</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 21:1–4</div>
    <div class="v-texto">"E vi um novo céu e uma nova terra; pois o primeiro céu e a primeira terra passaram, e o mar não existe mais. E vi a santa cidade, a nova Jerusalém, descendo do céu de Deus, preparada como uma noiva adornada para o seu marido. E ouvi uma grande voz do trono, dizendo: Eis o tabernáculo de Deus com os homens; ele habitará com eles, e eles serão o seu povo, e o próprio Deus estará com eles. E limpará dos seus olhos toda lágrima, e a morte não existirá mais; não haverá mais luto, nem choro, nem dor, pois as primeiras coisas passaram."</div>
    <div class="v-analise">"Novo céu e nova terra" — a palavra grega <em>kainos</em> ("novo") significa "novo em qualidade" — não <em>neos</em> ("novo em tempo"). A nova criação não é uma criação ex nihilo que substitui a atual — é a criação atual transfigurada e renovada (cf. Rm 8:21; 2 Pe 3:13). "O mar não existe mais" — no AT, o mar simbolizava o caos, o mal e a separação (cf. Is 57:20; Dn 7:2–3). A ausência do mar na nova criação significa a eliminação do caos e da ameaça. "O tabernáculo de Deus com os homens" — a promessa central de toda a Bíblia: "Eu serei o vosso Deus e vós sereis o meu povo" (Lv 26:12; Jr 31:33; Ez 37:27) finalmente cumprida em sua plenitude. "Limpará dos seus olhos toda lágrima" — a promessa de Isaías 25:8, citada aqui: o Deus que viu cada lágrima de seu povo (Sl 56:8) as limpa todas com sua própria mão.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 21:5–8</div>
    <div class="v-texto">"E o que estava assentado no trono disse: Eis que faço novas todas as coisas... Está feito. Eu sou o Alfa e o Ômega, o Princípio e o Fim. Ao sedento darei de graça da fonte da água da vida. O vencedor herdará estas coisas, e eu serei o seu Deus e ele será meu filho."</div>
    <div class="v-analise">"Eis que faço novas todas as coisas" — não "eis que faço todas as coisas novas" (destruindo o antigo e criando do nada), mas "eis que faço novas todas as coisas" (renovando e transfigurando o que existe). Esta distinção é crucial para a teologia da criação: Deus não abandona sua criação — ele a redime. "Está feito" (<em>Gegonen</em>) — o mesmo verbo do 7º taça (Ap 16:17) — a nova criação é a consumação do julgamento e da redenção. "Ao sedento darei de graça da fonte da água da vida" — a salvação é gratuita, não merecida. "O vencedor herdará estas coisas" — a herança da nova criação pertence aos que perseveraram na fé.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 Apocalipse 21:9–27 — A Nova Jerusalém</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 21:9–14 — A Cidade que Desce do Céu</div>
    <div class="v-texto">"E veio um dos sete anjos que tinham as sete taças cheias das sete últimas pragas, e falou comigo, dizendo: Vem, mostrar-te-ei a noiva, a esposa do Cordeiro. E me transportou em espírito a um monte grande e alto, e me mostrou a santa cidade, Jerusalém, descendo do céu de Deus, tendo a glória de Deus. O seu brilho era semelhante ao de uma pedra preciosíssima, como pedra de jaspe, cristalina."</div>
    <div class="v-analise">A Nova Jerusalém é apresentada como "a noiva, a esposa do Cordeiro" — a cidade e o povo são inseparáveis. A cidade não é apenas um lugar geográfico — ela é a comunidade dos redimidos em sua forma glorificada. "Descendo do céu de Deus" — a Nova Jerusalém não é construída pelos humanos, mas dada por Deus — a salvação é sempre iniciativa divina. "Tendo a glória de Deus" — a Shekinah, a presença gloriosa de Deus que habitou no tabernáculo (Ex 40:34–35) e no templo (1 Rs 8:10–11), agora permeia toda a cidade. As 12 portas com os nomes das 12 tribos e os 12 fundamentos com os nomes dos 12 apóstolos revelam que a Nova Jerusalém é o cumprimento tanto do AT quanto do NT — o povo de Deus em sua totalidade.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 21:15–21 — As Dimensões da Cidade</div>
    <div class="v-texto">"E aquele que falava comigo tinha uma cana de medir de ouro para medir a cidade, as suas portas e a sua muralha. E a cidade está disposta em quadrado, e o seu comprimento é igual à sua largura; e mediu a cidade com a cana: doze mil estádios; o seu comprimento, largura e altura são iguais."</div>
    <div class="v-analise">A Nova Jerusalém é um cubo perfeito de 12.000 estádios (aproximadamente 2.200 km) em cada dimensão — uma dimensão obviamente simbólica, não literal. O cubo perfeito evoca o Santo dos Santos do templo de Salomão (1 Rs 6:20) — a Nova Jerusalém inteira é o Santo dos Santos, o lugar da presença de Deus. O número 12.000 (12 × 1.000) é a plenitude do povo de Deus multiplicada pela plenitude. As fundações são decoradas com 12 pedras preciosas que evocam as 12 pedras do peitoral do sumo sacerdote (Ex 28:17–20) — toda a cidade é sacerdotal. As portas de pérola e as ruas de ouro transparente são imagens da glória incomparável da nova criação — não descrições literais de materiais de construção.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 21:22–27 — Sem Templo, Sem Sol</div>
    <div class="v-texto">"E não vi nenhum templo nela, porque o Senhor Deus, o Todo-Poderoso, é o seu templo, assim como o Cordeiro. E a cidade não tem necessidade do sol nem da lua para lhe darem luz, porque a glória de Deus a iluminou, e o seu candeeiro é o Cordeiro. E as nações andarão na sua luz, e os reis da terra trarão a sua glória para ela."</div>
    <div class="v-analise">"Não vi nenhum templo nela" — esta é uma das afirmações mais surpreendentes do Apocalipse. O templo era o centro da vida religiosa de Israel — o lugar onde Deus habitava e onde os humanos se aproximavam dele. Na Nova Jerusalém, não há templo porque toda a cidade é o templo — Deus habita em toda parte, e os redimidos têm acesso direto e ininterrupto à sua presença. "As nações andarão na sua luz" — a Nova Jerusalém não é exclusivamente para Israel ou para a Igreja — ela é o destino de todas as nações (cf. Is 60:3). "Os reis da terra trarão a sua glória" — as realizações humanas — arte, cultura, ciência, música — não são destruídas na nova criação, mas purificadas e oferecidas a Deus.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 Apocalipse 22:1–5 — O Rio e a Árvore da Vida</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 22:1–5</div>
    <div class="v-texto">"E mostrou-me um rio de água da vida, brilhante como cristal, que saía do trono de Deus e do Cordeiro. No meio da praça da cidade e de ambos os lados do rio havia a árvore da vida, que produz doze frutos, dando o seu fruto cada mês; e as folhas da árvore são para a cura das nações. E não haverá mais nenhuma maldição. E o trono de Deus e do Cordeiro estará nela, e os seus servos o servirão. E verão a sua face, e o seu nome estará nas suas testas. E não haverá mais noite, e não terão necessidade de luz de candeeiro nem de luz do sol, porque o Senhor Deus os iluminará; e reinarão pelos séculos dos séculos."</div>
    <div class="v-analise">O "rio de água da vida" evoca Gênesis 2:10 (o rio do Éden), Ezequiel 47:1–12 (o rio do templo) e João 7:38 ("rios de água viva"). A "árvore da vida" evoca Gênesis 2:9 e 3:22–24 — a árvore que Adão e Eva foram impedidos de comer após a Queda. Na Nova Jerusalém, o acesso à árvore da vida é restaurado — a maldição do Éden é revertida. "As folhas da árvore são para a cura das nações" — a nova criação não é apenas para os indivíduos, mas para as nações — a dimensão coletiva da redenção. "Verão a sua face" — a <em>visio Dei</em>, a visão de Deus face a face, é a esperança suprema da espiritualidade cristã (Mt 5:8; 1 Co 13:12; 1 Jo 3:2). No Éden, Adão e Eva caminhavam com Deus; na Nova Jerusalém, os redimidos verão sua face. "Reinarão pelos séculos dos séculos" — o destino humano não é a passividade contemplativa, mas o reinado ativo — a participação na governança da nova criação com Cristo.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 Apocalipse 22:6–21 — O Epílogo</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 22:12–21</div>
    <div class="v-texto">"Eis que venho em breve, e o meu galardão está comigo, para retribuir a cada um segundo as suas obras. Eu sou o Alfa e o Ômega, o Primeiro e o Último, o Princípio e o Fim... E o Espírito e a noiva dizem: Vem! E aquele que ouve, diga: Vem! E aquele que tem sede, venha; aquele que quiser, tome de graça a água da vida... Aquele que dá testemunho destas coisas diz: Certamente venho em breve. Amém! Vem, Senhor Jesus!"</div>
    <div class="v-analise">O epílogo do Apocalipse — e da Bíblia inteira — é uma troca de vozes entre Cristo e a Igreja. Cristo promete: "Venho em breve." A Igreja responde: "Vem, Senhor Jesus!" (<em>Maranata</em> — a oração mais antiga da Igreja, 1 Co 16:22). O convite final é universal: "aquele que tem sede, venha; aquele que quiser, tome de graça a água da vida" — a salvação é gratuita e aberta a todos. A última palavra da Bíblia não é um julgamento — é uma bênção: "A graça do Senhor Jesus seja com todos" (Ap 22:21). A Bíblia começa com "No princípio, Deus criou" (Gn 1:1) e termina com "A graça do Senhor Jesus seja com todos" — da criação à graça, da origem ao destino, de Gênesis ao Apocalipse, a história de Deus com a humanidade é uma história de amor redentor.</div>
  </div>
  <div class="destaque">
    <h3>🌟 A Nova Criação e a Esperança Cristã</h3>
    <p>A visão da Nova Jerusalém no Apocalipse é a resposta definitiva a todas as perguntas sobre o destino humano e o propósito da história. Ela nos diz que a criação não será destruída, mas renovada; que a história não é um ciclo sem sentido, mas uma narrativa com destino; que o sofrimento dos fiéis não é em vão, mas será vindicado; que a morte não é a última palavra, mas a penúltima; que a última palavra pertence a Deus — e ela é graça.</p>
    <p>A esperança da Nova Jerusalém não é uma fuga do mundo — é a motivação para o engajamento com o mundo. Porque sabemos que Deus fará novas todas as coisas, trabalhamos para a renovação do mundo agora. Porque sabemos que a injustiça será julgada, lutamos pela justiça agora. Porque sabemos que as lágrimas serão limpas, choramos com os que choram agora. Porque sabemos que as nações trarão sua glória para a Nova Jerusalém, valorizamos a diversidade cultural agora. A escatologia cristã não paralisa — ela liberta e motiva.</p>
    <p>"Maranata — vem, Senhor Jesus!" (Ap 22:20). Esta é a oração que encerra a Bíblia — e é a oração que deve caracterizar a vida da Igreja em toda época: a expectativa ansiosa e esperançosa do retorno de Cristo, que fará novas todas as coisas.</p>
  </div>
</div>
"""

MODULOS_F3 = [
    {
        "pasta": "babilonia",
        "cor": "#94a3b8",
        "hero_bg": "#0a0a0a",
        "titulo": "Babilônia — A Grande Prostituta",
        "subtitulo": "🏛️ Apocalipse 17–18 · Babilônia",
        "ref": "Grande Prostituta · Roma · Queda de Babilônia · Saí dela, povo meu",
        "citacao": "Saí dela, povo meu, para que não sejais participantes dos seus pecados e para que não recebais as suas pragas.",
        "autor_cit": "Apocalipse 18:4 — o chamado divino à separação do sistema mundano",
        "corpo": babilonia_corpo,
        "nav_prev": "/12-apocalipse/sete-tacas",
        "nav_prev_lbl": "← As 7 Taças",
        "nav_next": "/12-apocalipse/milenio",
        "nav_next_lbl": "O Milênio →",
    },
    {
        "pasta": "milenio",
        "cor": "#22c55e",
        "hero_bg": "#001a08",
        "titulo": "O Milênio e o Julgamento Final",
        "subtitulo": "⚔️ Apocalipse 19–20 · Milênio · Juízo",
        "ref": "Cavaleiro Branco · Ceia das Núpcias · Milênio · 4 Posições · Grande Trono Branco",
        "citacao": "E vi um grande trono branco e aquele que estava assentado nele, de cuja face fugiram a terra e o céu, e não se achou lugar para eles.",
        "autor_cit": "Apocalipse 20:11 — a cena do Juízo Final",
        "corpo": milenio_corpo,
        "nav_prev": "/12-apocalipse/babilonia",
        "nav_prev_lbl": "← Babilônia",
        "nav_next": "/12-apocalipse/nova-jerusalem",
        "nav_next_lbl": "Nova Jerusalém →",
    },
    {
        "pasta": "nova-jerusalem",
        "cor": "#fbbf24",
        "hero_bg": "#1a1200",
        "titulo": "A Nova Jerusalém — A Nova Criação",
        "subtitulo": "🌟 Apocalipse 21–22 · Nova Criação",
        "ref": "Novo Céu · Nova Terra · Tabernáculo de Deus · Rio da Vida · Árvore da Vida · Maranata",
        "citacao": "E limpará dos seus olhos toda lágrima, e a morte não existirá mais; não haverá mais luto, nem choro, nem dor, pois as primeiras coisas passaram.",
        "autor_cit": "Apocalipse 21:4 — a promessa final de Deus ao seu povo",
        "corpo": nova_jerusalem_corpo,
        "nav_prev": "/12-apocalipse/milenio",
        "nav_prev_lbl": "← O Milênio",
        "nav_next": "/12-apocalipse/hermeneutica",
        "nav_next_lbl": "Hermenêutica →",
    },
]


def main():
    for m in MODULOS_F3:
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
    print("\n🎉 Fase 3 do Bloco 12 completa!")


if __name__ == "__main__":
    main()
