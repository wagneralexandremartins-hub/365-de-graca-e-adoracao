#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os 8 módulos aprofundados do Bloco 10 — Cruzadas e Guerras Religiosas."""

import os

BASE = "/home/ubuntu/365-de-graca-e-adoracao/10-cruzadas"

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
    .aviso { border-radius: 12px; padding: 20px 24px; margin: 20px 0 28px; background: rgba(239,68,68,0.05); border: 1px solid rgba(239,68,68,0.15); }
    .aviso h4 { color: #ef4444; font-size: 0.9rem; font-weight: 800; margin-bottom: 8px; }
    .aviso p { color: #94a3b8; font-size: 0.88rem; line-height: 1.75; margin-bottom: 0; }
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
    """
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titulo} | Bloco 10 — 365 de Graça & Adoração</title>
  <link rel="icon" href="/favicon.ico">
  <style>{CSS_COMUM}{css_extra}</style>
</head>
<body>
  <div class="topbar"><div class="inner">
    <a href="/10-cruzadas/index.html">← Bloco 10</a>
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
      <a href="/10-cruzadas/index.html">📋 Índice</a>
      <a href="{nav_next}">{nav_next_lbl}</a>
    </div>
  </div>
</body>
</html>"""


# ============================================================
# MÓDULO 1: CONTEXTO HISTÓRICO
# ============================================================
contexto_corpo = """
<div class="sb">
  <h2>🗺️ O Mundo em 1095</h2>
  <p>Para compreender as Cruzadas, é preciso compreender o mundo em que elas nasceram — um mundo profundamente diferente do nosso. Em 1095, a Europa Ocidental era uma sociedade feudal, guerreira e profundamente religiosa. A violência era endêmica: os cavaleiros — a classe guerreira — passavam a vida em guerras privadas, pilhagens e duelos. A Igreja havia tentado limitar esta violência com a "Paz de Deus" e a "Trégua de Deus" — proibindo ataques a civis e combates em dias santos. As Cruzadas foram, em parte, uma tentativa de canalizar esta violência para um objetivo "sagrado."</p>
  <p>O Papado, sob a liderança de reformadores como Gregório VII (1073–1085), havia acabado de passar por uma revolução institucional. A Reforma Gregoriana havia afirmado a independência da Igreja em relação ao poder secular, a autoridade suprema do Papa sobre todos os reis e bispos, e a necessidade de uma Igreja moralmente renovada. O Papa Urbano II (1088–1099), que convocou a Primeira Cruzada, era um produto desta reforma — um papa confiante em sua autoridade e disposto a usá-la de forma audaciosa.</p>
</div>
<div class="sb">
  <h2>☪️ A Expansão Islâmica e a Ameaça aos Cristãos</h2>
  <div class="bloco">
    <div class="bt">A Conquista Islâmica do Mundo Cristão</div>
    <div class="bx">Em menos de um século após a morte de Maomé (632 d.C.), o Islã havia conquistado dois terços do mundo cristão: a Síria, a Palestina, o Egito, o Norte da África, a Espanha e a Pérsia. Estas regiões — berço do Cristianismo e sede das mais antigas igrejas — foram incorporadas ao Califado. Os cristãos que permaneceram nestas regiões (os "dhimmis") viviam como cidadãos de segunda classe, sujeitos a impostos especiais e restrições religiosas. Esta situação variava muito conforme o governante: alguns califas eram tolerantes; outros, perseguidores.</div>
  </div>
  <div class="bloco">
    <div class="bt">Os Turcos Seljúcidas e a Nova Ameaça</div>
    <div class="bx">A situação se agravou com a chegada dos Turcos Seljúcidas — um povo guerreiro da Ásia Central que havia se convertido ao Islã sunita. Em 1071, os Seljúcidas derrotaram o exército bizantino na Batalha de Manzikerte e conquistaram a maior parte da Anatólia (atual Turquia) — o coração do Império Bizantino. Em 1076, conquistaram Jerusalém dos Fatímidas egípcios. Os Seljúcidas eram menos tolerantes com os peregrinos cristãos que os Fatímidas: relatos de perseguições e dificuldades para os peregrinos chegaram ao Ocidente e contribuíram para o clima que tornou possível as Cruzadas.</div>
  </div>
  <div class="bloco">
    <div class="bt">O Apelo de Aleixo I Comneno</div>
    <div class="bx">Em 1095, o Imperador Bizantino Aleixo I Comneno enviou embaixadores ao Papa Urbano II pedindo auxílio militar contra os Turcos Seljúcidas. Aleixo queria mercenários ocidentais para ajudar a reconquistar a Anatólia — não uma Cruzada para libertar Jerusalém. Urbano II, porém, transformou o pedido de Aleixo em algo muito maior: uma guerra santa para libertar os Lugares Santos e ajudar os cristãos do Oriente. O que Aleixo pediu e o que Urbano convocou eram coisas muito diferentes — e esta diferença de objetivos seria uma fonte constante de conflito durante as Cruzadas.</div>
  </div>
</div>
<div class="sb">
  <h2>🎤 O Discurso de Clermont (1095)</h2>
  <p>O discurso do Papa Urbano II no Concílio de Clermont (novembro de 1095) foi um dos mais consequentes da história. Não temos o texto exato — temos cinco versões diferentes, escritas por cronistas que o ouviram ou o reconstruíram. Mas todas concordam nos pontos essenciais: Urbano descreveu as atrocidades cometidas pelos turcos contra os cristãos do Oriente (algumas exageradas ou inventadas), convocou os cavaleiros ocidentais a partir em auxílio dos irmãos orientais, prometeu indulgência plenária (remissão de todas as penas dos pecados) a quem participasse da expedição, e apresentou a libertação de Jerusalém como o objetivo supremo.</p>
  <p>A resposta da multidão foi imediata e avassaladora: "Deus lo vult!" ("Deus quer!") — o grito que se tornaria o slogan das Cruzadas. Milhares de cavaleiros e peregrinos costuraram cruzes em suas vestes e prometeram partir para a Terra Santa. O que Urbano havia desencadeado era algo que nem ele mesmo poderia controlar completamente — um movimento de massas que misturava devoção religiosa genuína, aventura, ganância e violência.</p>
  <div class="reflexao">
    <h3>🙏 Reflexão: Fé e Violência</h3>
    <p>O discurso de Clermont levanta uma questão teológica fundamental: pode a violência ser sagrada? Pode Deus querer que seus seguidores matem em seu nome? A tradição cristã sempre teve dificuldade com esta questão. Agostinho desenvolveu a doutrina da "guerra justa" — a violência pode ser justificada quando usada para defender os inocentes, restaurar a paz e punir o mal. Mas a guerra justa tem condições estritas: deve ser declarada por autoridade legítima, ter causa justa, ser conduzida com intenção reta e usar meios proporcionais. As Cruzadas satisfizeram algumas destas condições — mas violaram outras de forma flagrante. Os massacres de judeus no Reno, o saque de Constantinopla e o massacre de Jerusalém em 1099 não podem ser justificados por nenhuma doutrina de guerra justa. Eles são o que são: crimes cometidos em nome de Deus.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 2: PRIMEIRA CRUZADA
# ============================================================
primeira_corpo = """
<div class="sb">
  <h2>⚔️ A Cruzada Popular — O Povo de Pedro, o Eremita</h2>
  <p>Antes mesmo que os cavaleiros organizados partissem, uma multidão de camponeses, clérigos e cavaleiros menores — liderada pelo pregador carismático Pedro, o Eremita — partiu em direção ao Oriente em abril de 1096. Esta "Cruzada Popular" (também chamada de "Cruzada dos Pobres") era uma massa desorganizada de talvez 40.000 pessoas, sem provisões adequadas, sem liderança militar competente e sem estratégia. Eles marcharam pelo Reno, pela Hungria e pelos Bálcãs, saqueando as populações locais para sobreviver.</p>
  <p>No caminho, as hordas da Cruzada Popular cometeram um dos primeiros grandes crimes das Cruzadas: os massacres de comunidades judaicas nas cidades do Reno — Worms, Maguncia, Colônia e outras. Milhares de judeus foram mortos ou forçados ao batismo. Os perpetradores usaram a lógica perversa de que era contraditório ir lutar contra os "inimigos de Cristo" na Terra Santa enquanto os "inimigos de Cristo" viviam entre eles na Europa. Bispos e autoridades locais tentaram proteger os judeus — com sucesso limitado. Estes massacres inauguraram uma tradição de violência antissemita que marcaria as Cruzadas e a história europeia medieval.</p>
</div>
<div class="sb">
  <h2>🏰 A Cruzada dos Príncipes</h2>
  <div class="bloco">
    <div class="bt">Os Líderes</div>
    <div class="bx">A Cruzada dos Príncipes — a expedição militar organizada que partiu em agosto de 1096 — foi liderada por quatro grandes contingentes: Godofredo de Bulhão (Lorena), com seu irmão Balduíno; Raimundo IV de Toulouse (Provença); Boemundo de Taranto (sul da Itália normanda), com seu sobrinho Tancredo; e Hugo de Vermandois, irmão do rei da França. Não havia um comando unificado — os príncipes eram rivais entre si tanto quanto aliados. Esta falta de unidade seria uma fonte constante de problemas.</div>
  </div>
  <div class="bloco">
    <div class="bt">O Cerco de Niceia (1097)</div>
    <div class="bx">O primeiro grande objetivo dos cruzados foi Niceia — a capital seljúcida na Anatólia, a poucos quilômetros de Constantinopla. Após um cerco de seis semanas, Niceia se rendeu — mas ao Imperador Bizantino Aleixo I, não aos cruzados. Aleixo havia negociado secretamente com os defensores para evitar o saque da cidade. Os cruzados ficaram furiosos — eles esperavam saquear Niceia. Esta traição percebida aprofundou a desconfiança entre os cruzados e os bizantinos que os acompanhava desde o início.</div>
  </div>
  <div class="bloco">
    <div class="bt">O Cerco de Antioquia (1097–1098)</div>
    <div class="bx">O cerco de Antioquia foi o episódio mais dramático da Primeira Cruzada. A cidade era uma das maiores e mais bem defendidas do Oriente — suas muralhas tinham 400 torres. Os cruzados a sitiaram por sete meses, sofrendo fome, doenças e ataques de exércitos de socorro muçulmanos. Em junho de 1098, um traidor dentro da cidade abriu uma porta para Boemundo, que conquistou Antioquia. Mas no dia seguinte, um enorme exército muçulmano de Mossul chegou e sitiou os sitiantes. Os cruzados, enfraquecidos e desesperados, foram salvos — segundo eles — pela descoberta da "Sagrada Lança" (a lança que teria perfurado Cristo) e por uma visão de São Jorge e outros santos guerreiros. Eles saíram em batalha e derrotaram o exército muçulmano em uma vitória que pareceu milagrosa.</div>
  </div>
</div>
<div class="sb">
  <h2>🏙️ A Conquista de Jerusalém (1099)</h2>
  <p>Os cruzados chegaram às portas de Jerusalém em junho de 1099 — três anos após partirem da Europa. A cidade era defendida pelos Fatímidas egípcios, que haviam reconquistado Jerusalém dos Seljúcidas apenas um ano antes. Após um cerco de cinco semanas, os cruzados escalaram as muralhas em 15 de julho de 1099 e tomaram a cidade. O que se seguiu foi um dos episódios mais sangrentos das Cruzadas.</p>
  <p>O cronista Raimundo de Aguilers descreveu a cena: "Havia no Templo e no Pórtico de Salomão cavaleiros andando no sangue dos sarracenos até os joelhos e as rédeas dos cavalos." Muçulmanos e judeus foram massacrados indiscriminadamente. A comunidade judaica de Jerusalém, que havia se refugiado na sinagoga, foi queimada viva. Estima-se que entre 10.000 e 70.000 pessoas foram mortas — os números variam enormemente conforme as fontes. Após o massacre, os cruzados foram ao Santo Sepulcro e oraram, chorando de alegria, com as mãos ainda manchadas de sangue.</p>
  <div class="aviso">
    <h4>⚠️ Uma Nota Histórica Importante</h4>
    <p>O massacre de Jerusalém em 1099 é frequentemente comparado com a reconquista de Saladino em 1187, quando o sultão permitiu que os cristãos saíssem em paz. Este contraste é real e significativo. Mas é importante evitar a idealização de Saladino: ele também cometeu massacres em outras ocasiões (como a execução dos prisioneiros de Hattin). A violência não era monopólio de nenhum lado neste conflito.</p>
  </div>
</div>
<div class="sb">
  <h2>🏛️ Os Estados Cruzados</h2>
  <p>Após a conquista de Jerusalém, os cruzados estabeleceram quatro estados no Levante: o Condado de Edessa (o primeiro a ser fundado e o primeiro a cair, em 1144), o Principado de Antioquia, o Condado de Trípoli e o Reino de Jerusalém. Estes estados eram ilhas cristãs em um mar muçulmano — dependentes de reforços constantes da Europa e vulneráveis a qualquer poder muçulmano unificado. Godofredo de Bulhão foi eleito governante de Jerusalém, mas recusou o título de "Rei" — preferindo o de "Advogado do Santo Sepulcro." Seu irmão Balduíno I (1100–1118) foi o primeiro a usar o título de Rei de Jerusalém.</p>
  <div class="reflexao">
    <h3>🙏 Reflexão: A Conquista e o Evangelho</h3>
    <p>A conquista de Jerusalém em 1099 levanta uma questão que os cruzados não se fizeram — mas que nós devemos nos fazer: o que Jesus pensaria deste massacre em seu nome? O mesmo Jesus que disse "Bem-aventurados os pacificadores" (Mt 5:9), que ordenou a Pedro "Guarda a tua espada" (Jo 18:11), que curou a orelha do servo do sumo sacerdote que Pedro havia cortado (Lc 22:51). O mesmo Jesus que morreu sem resistência, pedindo perdão para seus algozes. A conquista de Jerusalém em 1099 não foi um triunfo do Evangelho — foi uma traição do Evangelho, cometida em nome do Evangelho. Esta distinção é crucial para qualquer avaliação cristã das Cruzadas.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 3: CRUZADAS SEGUINTES
# ============================================================
seguintes_corpo = """
<div class="sb">
  <h2>🏰 A Segunda Cruzada (1147–1149) — O Fracasso em Damasco</h2>
  <p>A Segunda Cruzada foi convocada pelo Papa Eugênio III após a queda do Condado de Edessa para o atabegue Zengi de Mossul (1144). Foi pregada com eloquência incomparável por Bernardo de Claraval — o monge mais influente da Europa, fundador da Ordem Cisterciense e conselheiro de papas e reis. Bernardo recrutou os dois maiores reis da Europa: Luís VII da França e Conrado III da Alemanha. A expectativa era enorme — e o fracasso foi correspondentemente humilhante.</p>
  <p>Os exércitos alemão e francês sofreram pesadas perdas na Anatólia antes mesmo de chegar à Terra Santa. Quando finalmente chegaram, os líderes cruzados tomaram a decisão incompreensível de atacar Damasco — a cidade muçulmana que era aliada dos francos estabelecidos na Terra Santa contra Zengi. O cerco de Damasco (1148) durou apenas quatro dias antes de ser abandonado em circunstâncias humilhantes. A Segunda Cruzada terminou sem nenhuma conquista e com a reputação das Cruzadas seriamente abalada.</p>
</div>
<div class="sb">
  <h2>⚔️ Saladino e a Queda de Jerusalém (1187)</h2>
  <div class="bloco">
    <div class="bt">Saladino — O Grande Adversário</div>
    <div class="bx">Saladino (Salah ad-Din Yusuf ibn Ayyub, 1137–1193) foi o maior líder muçulmano das Cruzadas e um dos estadistas mais notáveis da Idade Média. Curdo de origem, ele unificou o Egito e a Síria sob seu comando e transformou a jihad contra os cruzados em uma causa pan-islâmica. Era conhecido por sua generosidade, sua palavra honrada e seu tratamento relativamente humano dos prisioneiros — qualidades que o tornaram admirado mesmo por seus inimigos cristãos. O cronista cruzado Guilherme de Tiro o descreveu como "um homem de grande generosidade e clemência."</div>
  </div>
  <div class="bloco">
    <div class="bt">A Batalha de Hattin (1187)</div>
    <div class="bx">A Batalha de Hattin (4 de julho de 1187) foi a maior derrota da história dos estados cruzados. O Rei Guido de Lusignan, provocado pelo fanático Reinaldo de Chatillon, levou o exército cruzado para o deserto em pleno verão para socorrer o Castelo de Tiberíades. Saladino cortou o acesso à água e cercou o exército exausto e desidratado nos "Chifres de Hattin" — duas colinas vulcânicas. O exército cruzado foi aniquilado. O Rei Guido foi capturado. Reinaldo de Chatillon foi executado pessoalmente por Saladino — que havia jurado matá-lo por ter atacado uma caravana de peregrinos muçulmanos. A Verdadeira Cruz (a relíquia mais sagrada dos cruzados) foi capturada e nunca mais foi vista.</div>
  </div>
  <div class="bloco">
    <div class="bt">A Reconquista de Jerusalém</div>
    <div class="bx">Após Hattin, Saladino conquistou sistematicamente os castelos e cidades cruzados. Jerusalém se rendeu em outubro de 1187. Ao contrário dos cruzados em 1099, Saladino não massacrou a população: ele permitiu que os cristãos saíssem mediante resgate. Aqueles que não podiam pagar o resgate foram escravizados — mas Saladino libertou muitos deles por generosidade pessoal. Este contraste entre o comportamento de Saladino em 1187 e o dos cruzados em 1099 tornou-se um símbolo poderoso na memória islâmica das Cruzadas.</div>
  </div>
</div>
<div class="sb">
  <h2>⚔️ A Terceira Cruzada (1189–1192) — Ricardo vs. Saladino</h2>
  <p>A notícia da queda de Jerusalém chocou a Europa. O Papa Gregório VIII morreu de desgosto (segundo a tradição). O Papa Clemente III convocou a Terceira Cruzada, que reuniu os três maiores reis da Europa: Frederico I Barbarossa da Alemanha (que morreu afogado num rio na Anatólia antes de chegar à Terra Santa), Filipe II Augusto da França e Ricardo I "Coração de Leão" da Inglaterra. A rivalidade entre Ricardo e Filipe — aliados e inimigos ao mesmo tempo — marcou toda a Cruzada.</p>
  <p>Ricardo I foi o maior guerreiro das Cruzadas — um rei-cavaleiro de coragem extraordinária e talento militar excepcional. Ele reconquistou Acre após um longo cerco (1191), derrotou Saladino na Batalha de Arsuf e avançou até a vista de Jerusalém — mas nunca a atacou. Duas vezes ele chegou perto o suficiente para ver a cidade; duas vezes recuou, reconhecendo que não tinha forças suficientes para tomá-la e mantê-la. O Tratado de Jaffa (setembro de 1192) encerrou a Terceira Cruzada: Saladino manteve Jerusalém, mas garantiu aos cristãos o livre acesso aos Lugares Santos. Ricardo partiu sem ter reconquistado Jerusalém — mas com a reputação de ser o maior guerreiro da cristandade.</p>
  <div class="reflexao">
    <h3>🙏 Reflexão: A Admiração Mútua de Ricardo e Saladino</h3>
    <p>Um dos aspectos mais fascinantes da Terceira Cruzada é a admiração mútua entre Ricardo e Saladino — dois homens que nunca se encontraram pessoalmente, mas que trocaram mensageiros, presentes e gestos de cavalheirismo ao longo de toda a campanha. Quando Ricardo adoeceu, Saladino lhe enviou frutas e neve das montanhas para refrescá-lo. Quando o cavalo de Ricardo foi morto em batalha, Saladino lhe enviou dois cavalos de reposição. Esta admiração mútua não impediu que eles se combatessem com toda a ferocidade — mas ela revela que mesmo no contexto da guerra religiosa, a humanidade comum pode criar pontes inesperadas. É uma lição que permanece relevante hoje.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 4: SAQUE DE CONSTANTINOPLA
# ============================================================
saque_corpo = """
<div class="sb">
  <h2>🔥 A Quarta Cruzada — O Desvio Fatal</h2>
  <p>A Quarta Cruzada (1202–1204) é o episódio mais vergonhoso das Cruzadas — e um dos mais reveladores sobre a natureza real do movimento cruzadístico. Convocada pelo Papa Inocêncio III com o objetivo de conquistar o Egito (a base do poder muçulmano no Oriente Médio) e de lá libertar Jerusalém, ela terminou com o saque da maior cidade cristã do mundo — Constantinopla, capital do Império Bizantino — por cruzados ocidentais.</p>
  <p>O desvio começou com problemas financeiros: os cruzados não tinham dinheiro suficiente para pagar os venezianos pelo transporte marítimo. Veneza, liderada pelo ancião e cego Doge Enrico Dandolo (que tinha 90 anos e ainda assim liderou pessoalmente o ataque a Constantinopla), propôs um acordo: em vez de dinheiro, os cruzados ajudariam Veneza a reconquistar a cidade de Zara (atual Zadar, na Croácia) — uma cidade cristã que havia se rebelado contra Veneza. O Papa Inocêncio III proibiu o ataque a Zara — mas os cruzados o fizeram assim mesmo. Inocêncio os excomungou — e depois levantou a excomunhão para não perder o controle da Cruzada.</p>
</div>
<div class="sb">
  <h2>🏛️ O Saque de Constantinopla (1204)</h2>
  <div class="bloco">
    <div class="bt">As Circunstâncias do Saque</div>
    <div class="bx">Após Zara, os cruzados foram desviados para Constantinopla por um pretendente ao trono bizantino — Aleixo Ângelo — que prometeu recompensas generosas se o ajudassem a recuperar o trono de seu pai. Os cruzados instalaram Aleixo IV no trono (1203) — mas ele não conseguiu cumprir suas promessas. Uma revolta popular derrubou Aleixo IV e instalou um novo imperador hostil aos ocidentais. Os cruzados, sem dinheiro e sem alternativa, decidiram tomar a cidade pela força.</div>
  </div>
  <div class="bloco">
    <div class="bt">O Saque</div>
    <div class="bx">O saque de Constantinopla (abril de 1204) durou três dias. Os cruzados roubaram tudo o que podiam carregar — ouro, prata, relíquias, obras de arte, manuscritos. Igrejas foram profanadas. Freiras foram estupradas. A Hagia Sofia — a maior catedral do mundo cristão — foi saqueada e uma prostituta foi colocada no trono do Patriarca. O cronista Nicetas Choniates, que sobreviveu ao saque, escreveu: "Os sarracenos são mais misericordiosos e humanos do que estes homens que carregam a Cruz de Cristo no ombro." A Quarta Cruzada não chegou à Terra Santa — ela destruiu o maior baluarte cristão do Oriente.</div>
  </div>
  <div class="bloco">
    <div class="bt">O Império Latino de Constantinopla</div>
    <div class="bx">Após o saque, os cruzados dividiram o Império Bizantino entre si e estabeleceram o "Império Latino de Constantinopla" (1204–1261). Balduíno de Flandres foi coroado Imperador. Veneza ficou com os portos e ilhas estratégicas. O Patriarca latino substituiu o Patriarca ortodoxo. Este "Império Latino" foi uma criação artificial e frágil — nunca controlou mais do que uma fração do território bizantino e foi constantemente ameaçado pelos estados gregos que sobreviveram ao saque. Em 1261, o Imperador Miguel VIII Paleólogo reconquistou Constantinopla e restaurou o Império Bizantino.</div>
  </div>
</div>
<div class="sb">
  <h2>💔 A Ferida que Nunca Cicatrizou</h2>
  <p>O saque de Constantinopla em 1204 é considerado pela Igreja Ortodoxa como o evento mais traumático de sua história — mais do que a conquista turca de 1453. Ele aprofundou o Cisma de 1054 de forma irreparável: antes de 1204, havia esperança de reconciliação entre Roma e Constantinopla; depois de 1204, esta esperança foi destruída por gerações. O Papa João Paulo II pediu perdão pelo saque em 2001, durante uma visita à Grécia — um gesto significativo, mas que não apagou séculos de memória dolorosa.</p>
  <p>O saque de Constantinopla também teve consequências geopolíticas devastadoras: ele enfraqueceu o Império Bizantino de forma irreversível. Quando os Turcos Otomanos ameaçaram Constantinopla no século XIV e XV, o Império estava tão enfraquecido pelo saque de 1204 e suas consequências que não conseguiu resistir. A queda de Constantinopla para os otomanos em 1453 foi, em parte, uma consequência tardia da Quarta Cruzada.</p>
  <div class="reflexao">
    <h3>🙏 Reflexão: Quando a Fé se Torna Pretexto</h3>
    <p>A Quarta Cruzada é o exemplo mais claro de como a fé pode ser instrumentalizada para fins que nada têm a ver com ela. Os cruzados usaram a linguagem da guerra santa para justificar o que era, na realidade, uma operação de saque e conquista movida por interesses políticos e econômicos venezianos. O Papa Inocêncio III, que havia convocado a Cruzada com as melhores intenções, viu-a escapar completamente de seu controle e ser usada para destruir o que pretendia defender. Esta lição é permanentemente relevante: quando a fé é instrumentalizada pelo poder, ela não apenas falha em seus objetivos religiosos — ela se torna uma ferramenta de destruição. "Nem todo aquele que me diz: Senhor, Senhor, entrará no reino dos céus" (Mt 7:21).</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 5: CRUZADAS DO NORTE E INTERIOR
# ============================================================
nordeste_corpo = """
<div class="sb">
  <h2>🌲 As Cruzadas do Norte — Contra os Pagãos do Báltico</h2>
  <p>As Cruzadas não foram apenas para a Terra Santa. A partir do século XII, o conceito de Cruzada foi expandido para incluir guerras contra pagãos e hereges na Europa. As Cruzadas do Norte (ou Cruzadas Bálticas) foram campanhas militares contra os povos eslavos e bálticos pagãos do norte da Europa — Prussianos, Lituanos, Letões, Estonios e outros. Estas campanhas foram lideradas principalmente pela Ordem Teutônica — uma ordem militar fundada durante as Cruzadas na Terra Santa que foi transferida para o Báltico em 1226.</p>
  <p>As Cruzadas Bálticas duraram mais de dois séculos (1193–1410) e resultaram na cristianização forçada de grande parte do norte da Europa. A Ordem Teutônica estabeleceu um estado monástico-militar na Prússia e na Livônia que durou até o século XVI. A violência destas campanhas foi brutal: populações inteiras foram massacradas, escravizadas ou forçadas ao batismo. A Lituânia foi o último estado pagão da Europa a se converter ao Cristianismo — em 1387, quando o Grão-Duque Jogaila se batizou para se casar com a rainha da Polônia.</p>
</div>
<div class="sb">
  <h2>🔥 A Cruzada Albigense (1209–1229) — Contra os Cátaros</h2>
  <div class="bloco">
    <div class="bt">Quem Eram os Cátaros?</div>
    <div class="bx">Os Cátaros (do grego <em>katharos</em> — "puro") eram um movimento religioso dualista que floresceu no sul da França (Languedoc) e no norte da Itália nos séculos XII e XIII. Eles acreditavam que o mundo material era obra de um deus maligno e que o espírito humano estava aprisionado na matéria. A salvação consistia em libertar o espírito da matéria através de uma vida ascética rigorosa. Os Cátaros rejeitavam a Igreja Católica, os sacramentos, o casamento e a reprodução (que perpetuava o aprisionamento das almas na matéria). Sua elite espiritual — os "Perfeitos" — vivia em pobreza extrema e celibato. O povo comum — os "Crentes" — podia viver normalmente, recebendo o sacramento cátaro (<em>consolamentum</em>) apenas no leito de morte.</div>
  </div>
  <div class="bloco">
    <div class="bt">O Massacre de Béziers (1209)</div>
    <div class="bx">O Papa Inocêncio III convocou a Cruzada Albigense em 1208, após o assassinato de seu legado papal no Languedoc (atribuído ao Conde Raimundo VI de Toulouse). O exército cruzado, liderado pelo Abade Arnaldo Amaury e pelo cavaleiro Simão de Montfort, chegou à cidade de Béziers em julho de 1209. A cidade tinha uma população mista de católicos e cátaros. Os cruzados perguntaram ao legado papal como distinguir os hereges dos católicos. A resposta atribuída a Arnaldo Amaury tornou-se infame: "Matai todos — Deus reconhecerá os seus." A cidade foi massacrada: estima-se que entre 7.000 e 20.000 pessoas foram mortas, incluindo os católicos que haviam se refugiado na catedral.</div>
  </div>
  <div class="bloco">
    <div class="bt">A Inquisição Medieval</div>
    <div class="bx">A Cruzada Albigense foi acompanhada pela criação da Inquisição Medieval — um tribunal eclesiástico especializado na investigação e punição da heresia. A Inquisição foi estabelecida pelo Papa Gregório IX em 1231 e confiada principalmente aos Dominicanos. Ela usava métodos que hoje consideramos bárbaros — incluindo a tortura (autorizada pelo Papa Inocêncio IV em 1252) e a pena de morte por fogueira (executada pelo poder civil). A Inquisição Medieval foi mais moderada do que sua reputação popular sugere — ela condenou à morte uma proporção menor de acusados do que os tribunais civis da época — mas ela representa uma das páginas mais sombrias da história da Igreja: a perseguição sistemática de pessoas por suas crenças.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: A Coerção na Fé</h3>
    <p>A Cruzada Albigense e a Inquisição Medieval levantam uma questão fundamental: pode a fé ser imposta pela força? A resposta cristã deve ser um não inequívoco. Jesus nunca coagiu ninguém a segui-lo — ele convidou, chamou, desafiou. Quando os discípulos perguntaram se deveriam "mandar fogo descer do céu" sobre uma aldeia samaritana que os havia rejeitado, Jesus os repreendeu (Lc 9:54-55). A liberdade religiosa não é apenas um direito humano moderno — é uma exigência do Evangelho. A fé que precisa de espada para se manter não é fé — é medo. E o Deus que precisa de inquisidores para ser adorado não é o Deus de Jesus Cristo.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 6: ORDENS MILITARES
# ============================================================
ordens_corpo = """
<div class="sb">
  <h2>🛡️ O Paradoxo do Monge-Guerreiro</h2>
  <p>As Ordens Militares foram uma das criações mais originais — e mais paradoxais — das Cruzadas. Elas combinavam dois ideais que pareciam incompatíveis: o monge, que renunciava ao mundo e à violência, e o guerreiro, cuja profissão era a violência. Bernardo de Claraval, o grande teólogo das Cruzadas, defendeu este paradoxo em seu tratado <em>De laude novae militiae</em> ("Em louvor da nova cavalaria"): o monge-guerreiro não mata por ódio ou ganância, mas por obediência e amor à Igreja. Ele não é um homicida (<em>homicida</em>) mas um "malicida" (<em>malicida</em>) — um matador do mal. Esta distinção teológica era sofisticada — mas não convenceu a todos, e a história das Ordens Militares mostrou que a linha entre "malicida" e homicida era frequentemente cruzada.</p>
</div>
<div class="sb">
  <h2>⚔️ As Três Grandes Ordens Militares</h2>
  <div class="pers-grid">
    <div class="pers-card">
      <div class="pers-nome">Ordem dos Templários</div>
      <div class="pers-datas">Fund. 1119 · Dissolvida 1312</div>
      <div class="pers-desc">Fundada por Hugo de Payns para proteger os peregrinos na Terra Santa. Nome oficial: "Pobres Cavaleiros de Cristo e do Templo de Salomão." Tornaram-se a ordem mais rica e poderosa da Europa medieval, com castelos, bancos e propriedades em toda a cristandade. Dissolvida pelo Papa Clemente V sob pressão do Rei Filipe IV da França.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Ordem dos Hospitalários</div>
      <div class="pers-datas">Fund. c. 1099 · Ativa até hoje</div>
      <div class="pers-desc">Fundada para cuidar dos peregrinos doentes em Jerusalém. Tornou-se também uma ordem militar. Após a queda da Terra Santa, transferiu-se para Rodes (1310) e depois para Malta (1530) — daí "Cavaleiros de Malta." Ainda existe como organização humanitária: a Ordem de Malta.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Ordem Teutônica</div>
      <div class="pers-datas">Fund. 1190 · Ativa até hoje</div>
      <div class="pers-desc">Fundada durante o cerco de Acre para cuidar dos cruzados alemães doentes. Tornou-se uma ordem militar e foi transferida para o Báltico em 1226, onde conduziu as Cruzadas contra os pagãos prussianos e lituanos. Estabeleceu um estado monástico-militar na Prússia que durou até 1525. Ainda existe como ordem religiosa na Áustria.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Ordem de Santiago</div>
      <div class="pers-datas">Fund. 1170 · Ativa até hoje</div>
      <div class="pers-desc">Fundada na Espanha para a Reconquista — a guerra cristã contra os mouros na Península Ibérica. Uma das várias ordens militares ibéricas (junto com Calatrava, Alcântara e Avis). Protegia os peregrinos no Caminho de Santiago de Compostela. Ainda existe como ordem honorífica espanhola.</div>
    </div>
  </div>
</div>
<div class="sb">
  <h2>⚖️ O Julgamento dos Templários (1307–1312)</h2>
  <p>A dissolução da Ordem dos Templários é um dos episódios mais dramáticos da história medieval. Em outubro de 1307, o Rei Filipe IV da França ("o Belo") ordenou a prisão simultânea de todos os Templários na França — cerca de 2.000 homens. Eles foram acusados de heresia, apostasia, sodomia, adoração de um ídolo chamado "Baphomet" e de cuspir na Cruz durante os rituais de iniciação. Sob tortura, muitos Templários confessaram estas acusações — e depois as retrataram.</p>
  <p>O processo foi claramente motivado por razões políticas e financeiras: Filipe IV estava profundamente endividado com os Templários e queria se apropriar de seus bens. O Papa Clemente V — um francês que residia em Avignon sob a influência do rei francês — cedeu às pressões de Filipe e dissolveu a Ordem no Concílio de Viena (1312). O último Grão-Mestre dos Templários, Jacques de Molay, foi queimado na fogueira em Paris em 1314. Segundo a tradição, antes de morrer, ele amaldiçoou o Papa e o Rei — ambos morreram no mesmo ano.</p>
  <div class="reflexao">
    <h3>🙏 Reflexão: Poder, Riqueza e Corrupção</h3>
    <p>A história das Ordens Militares é uma parábola sobre o que acontece quando instituições religiosas acumulam poder e riqueza excessivos. Os Templários começaram como "pobres cavaleiros de Cristo" — e terminaram como a maior potência financeira da Europa medieval. Esta trajetória — da pobreza evangélica ao poder institucional — é uma tentação recorrente na história da Igreja. Jesus disse: "Não podeis servir a Deus e a Mamom" (Mt 6:24). As Ordens Militares tentaram servir a ambos — e a tensão entre estes dois senhores eventualmente as destruiu. A lição não é que a Igreja não deve ter recursos — mas que os recursos devem servir à missão, não a missão servir aos recursos.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 7: FRANCISCO E O SULTÃO
# ============================================================
francisco_corpo = """
<div class="sb">
  <h2>🕊️ O Encontro Mais Surpreendente das Cruzadas</h2>
  <p>Em setembro de 1219, durante a Quinta Cruzada, um frade italiano de meia-idade atravessou as linhas inimigas no Egito e pediu para ser levado ao Sultão Al-Kamil — o sobrinho de Saladino e governante do Egito. O frade se chamava Francisco de Assis. Ele não tinha armas, não tinha escolta, não tinha credenciais diplomáticas. Ele tinha apenas sua fé e seu desejo de pregar o Evangelho ao sultão — ou, se necessário, de morrer como mártir. O que aconteceu a seguir foi um dos encontros mais surpreendentes e mais significativos da história das Cruzadas.</p>
  <p>Francisco e seus companheiros foram capturados pelos soldados muçulmanos e levados ao sultão. Al-Kamil, em vez de executá-los (como era o destino habitual dos espiões e intrusos), os recebeu com cortesia. Ele ouviu Francisco pregar o Evangelho por vários dias. Segundo as fontes franciscanas, Francisco propôs uma prova de fé: ele e os imãs muçulmanos entrariam juntos numa fogueira, e a verdade da religião seria determinada por quem sobrevivesse. Al-Kamil recusou educadamente — mas ficou impressionado com a coragem e a sinceridade de Francisco. Após vários dias de conversas, Al-Kamil enviou Francisco de volta ao campo cruzado, com salvo-conduto e presentes.</p>
</div>
<div class="sb">
  <h2>👤 Francisco de Assis — O Homem e a Missão</h2>
  <div class="bloco">
    <div class="bt">Quem Era Francisco de Assis?</div>
    <div class="bx">Francisco de Assis (1181/82–1226) foi o filho de um rico comerciante de tecidos de Assis, na Úmbria italiana. Após uma experiência de conversão (c. 1205), ele abraçou a pobreza radical, cuidou de leprosos e começou a pregar. Sua Ordem dos Frades Menores (Franciscanos) foi aprovada pelo Papa Inocêncio III em 1209 e cresceu rapidamente para milhares de membros. Francisco era um homem de oração profunda, alegria contagiante e amor radical pela criação — seu "Cântico das Criaturas" é um dos mais belos poemas da literatura italiana. Ele recebeu os estigmas — as chagas de Cristo — em 1224, dois anos antes de morrer.</div>
  </div>
  <div class="bloco">
    <div class="bt">Por Que Francisco Foi ao Sultão?</div>
    <div class="bx">Francisco foi ao Sultão por razões que eram ao mesmo tempo simples e profundas. Simples: ele queria pregar o Evangelho a todos os povos, incluindo os muçulmanos. Profundas: ele acreditava que o testemunho desarmado — a presença pacífica, a palavra gentil, o amor concreto — era o único método de missão compatível com o Evangelho de Jesus. Ele havia escrito em sua Regra que os frades que iam "entre os sarracenos e outros infiéis" não deveriam "fazer disputas ou contendas, mas serem sujeitos a toda criatura humana por amor de Deus." Esta abordagem era radicalmente diferente do modelo cruzadístico — e radicalmente mais fiel ao Evangelho.</div>
  </div>
</div>
<div class="sb">
  <h2>🌍 Al-Kamil — O Sultão que Ouviu</h2>
  <p>Al-Kamil (1177–1238) foi um dos governantes mais inteligentes e cultivados de seu tempo. Ele era conhecido por seu interesse intelectual, sua tolerância religiosa e sua disposição para o diálogo. Ele havia tentado negociar uma paz com os cruzados antes da chegada de Francisco — oferecendo a devolução de Jerusalém em troca de uma retirada cruzada do Egito. Os cruzados recusaram, instigados pelo legado papal Pelágio, que esperava uma vitória total. Esta recusa foi um erro estratégico que custou caro aos cruzados.</p>
  <p>O encontro de Al-Kamil com Francisco foi genuinamente impressionante para o sultão. As fontes islâmicas são mais esparsas do que as cristãs sobre este episódio — mas há evidências de que Al-Kamil ficou profundamente tocado pela personalidade de Francisco. Ele enviou Francisco de volta com presentes e um salvo-conduto que permitia aos Franciscanos visitar os Lugares Santos — um privilégio que a Ordem mantém até hoje: os Franciscanos são os guardiões oficiais dos Lugares Santos em Jerusalém.</p>
  <div class="reflexao">
    <h3>🙏 Reflexão: A Missão Desarmada</h3>
    <p>O encontro de Francisco com Al-Kamil é uma das histórias mais inspiradoras da história cristã — e uma das mais relevantes para o nosso tempo. Num contexto de guerra religiosa brutal, Francisco escolheu o caminho do diálogo desarmado. Ele não foi ao sultão para convertê-lo pela força ou pela ameaça — foi para testemunhar o Evangelho com sua vida. O resultado não foi uma conversão espetacular — mas foi algo talvez mais valioso: um encontro humano genuíno, marcado pelo respeito mútuo e pela abertura ao outro. Esta é a missão cristã em sua forma mais pura: não a conquista, mas o testemunho; não a coerção, mas o amor. "Ide por todo o mundo e pregai o Evangelho a toda criatura" (Mc 16:15) — mas pregai como Francisco pregou: com as mãos vazias e o coração cheio.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO 8: CONSEQUÊNCIAS
# ============================================================
consequencias_corpo = """
<div class="sb">
  <h2>🌍 O Fracasso Militar das Cruzadas</h2>
  <p>Do ponto de vista de seu objetivo declarado — a conquista permanente da Terra Santa — as Cruzadas foram um fracasso. A Primeira Cruzada conquistou Jerusalém em 1099; a cidade foi perdida para Saladino em 1187 e nunca mais foi recuperada pelos cruzados. A Sexta Cruzada (1228–1229) recuperou Jerusalém diplomaticamente — mas a perdeu novamente em 1244. A Sétima e a Oitava Cruzadas (lideradas por São Luís IX da França) fracassaram miseravelmente no Egito e na Tunísia. A queda de Acre em 1291 encerrou a presença cruzada na Terra Santa após dois séculos de esforço e imenso custo humano.</p>
  <p>Por que as Cruzadas fracassaram militarmente? Várias razões: a distância e a dificuldade de manter linhas de abastecimento; a falta de unidade de comando entre os príncipes cruzados; a superioridade numérica e logística dos estados muçulmanos; a incapacidade de colonizar permanentemente uma região tão distante da Europa; e, fundamentalmente, a impossibilidade de manter indefinidamente a mobilização religiosa que havia tornado possível a Primeira Cruzada. Após o fracasso da Segunda Cruzada, o entusiasmo popular pelas Cruzadas nunca se recuperou completamente.</p>
</div>
<div class="sb">
  <h2>📚 O Legado Cultural das Cruzadas</h2>
  <div class="bloco">
    <div class="bt">Intercâmbio Intelectual</div>
    <div class="bx">As Cruzadas foram um dos canais pelos quais o conhecimento islâmico chegou à Europa medieval. Matemática, astronomia, medicina, filosofia — muito do que a Europa aprendeu de Aristóteles chegou através de traduções árabes. Os cruzados trouxeram de volta especiarias, tecidos, técnicas arquitetônicas e ideias que enriqueceram a cultura europeia. O contato com o Islã — mesmo no contexto da guerra — estimulou a curiosidade intelectual europeia e contribuiu para o Renascimento do século XII.</div>
  </div>
  <div class="bloco">
    <div class="bt">Comércio e Economia</div>
    <div class="bx">As Cruzadas estimularam o comércio entre a Europa e o Oriente. As cidades italianas — Veneza, Gênova, Pisa — enriqueceram enormemente como fornecedoras de transporte e abastecimento para as Cruzadas e como intermediárias no comércio com o Levante. As rotas comerciais estabelecidas durante as Cruzadas prepararam o terreno para a expansão comercial europeia dos séculos seguintes. O capitalismo comercial europeu tem raízes parciais nas Cruzadas.</div>
  </div>
  <div class="bloco">
    <div class="bt">Arquitetura</div>
    <div class="bx">Os castelos cruzados — como o Krak des Chevaliers na Síria — são algumas das estruturas militares mais impressionantes da Idade Média. Os cruzados trouxeram de volta técnicas arquitetônicas islâmicas que influenciaram a arquitetura europeia. O estilo gótico — com seus arcos apontados, suas abóbadas nervuradas e suas rosáceas — tem influências parciais da arquitetura islâmica que os cruzados conheceram no Oriente.</div>
  </div>
</div>
<div class="sb">
  <h2>🕊️ O Legado Espiritual</h2>
  <div class="bloco">
    <div class="bt">A Peregrinação</div>
    <div class="bx">As Cruzadas intensificaram a tradição cristã da peregrinação — a viagem física a lugares sagrados como ato de devoção. A peregrinação a Jerusalém tornou-se o ideal supremo da piedade medieval. Mesmo após o fracasso das Cruzadas, a peregrinação à Terra Santa continuou — e continua até hoje. Os Franciscanos, guardiões dos Lugares Santos desde o século XIII, facilitam esta peregrinação para milhões de cristãos anualmente.</div>
  </div>
  <div class="bloco">
    <div class="bt">As Ordens Religiosas</div>
    <div class="bx">As Cruzadas estimularam o florescimento das ordens religiosas medievais. Os Franciscanos e os Dominicanos — as duas grandes ordens mendicantes do século XIII — nasceram em parte como resposta às Cruzadas: os Franciscanos com o modelo de Francisco no Egito (missão pacífica), os Dominicanos com o modelo de Domingos na Cruzada Albigense (pregação contra a heresia). Estas ordens transformaram a Igreja medieval e continuam ativas até hoje.</div>
  </div>
</div>
<div class="sb">
  <h2>🌐 As Cruzadas na Memória Contemporânea</h2>
  <p>As Cruzadas têm uma presença surpreendentemente viva na política contemporânea. No mundo islâmico, as Cruzadas são frequentemente invocadas como símbolo da agressão ocidental contra o Islã — uma narrativa que ignora os séculos de conquista islâmica que precederam as Cruzadas, mas que tem um poder emocional real. Osama Bin Laden chamava os americanos de "cruzados" — usando as Cruzadas como enquadramento para o conflito contemporâneo entre o Ocidente e o mundo islâmico.</p>
  <p>No Ocidente, as Cruzadas são frequentemente invocadas em dois sentidos opostos: pelos críticos da religião como exemplo do perigo da fé militante, e pelos defensores da "civilização ocidental" como exemplo de uma resistência legítima à expansão islâmica. Ambas as narrativas são simplificações que ignoram a complexidade histórica. As Cruzadas foram ao mesmo tempo uma expressão de fé genuína e uma manifestação de violência injustificável — e qualquer avaliação honesta deve reconhecer ambas as dimensões.</p>
  <div class="reflexao">
    <h3>🙏 Reflexão Final: O Que Aprender das Cruzadas?</h3>
    <p>As Cruzadas nos ensinam várias lições dolorosas mas necessárias. Primeira: a fé pode ser corrompida pelo poder e pela violência — e quando isso acontece, ela se torna uma força de destruição, não de salvação. Segunda: o fim não justifica os meios — mesmo objetivos legítimos (proteger peregrinos, defender comunidades cristãs) não justificam massacres de civis, saque de cidades aliadas ou coerção religiosa. Terceira: o diálogo é sempre preferível à guerra — o encontro de Francisco com Al-Kamil é um modelo mais fiel ao Evangelho do que qualquer batalha cruzada. Quarta: a humildade histórica é necessária — a Igreja deve reconhecer os crimes cometidos em seu nome, não para se destruir, mas para se purificar. "Se confessarmos os nossos pecados, ele é fiel e justo para nos perdoar os pecados e nos purificar de toda injustiça" (1 Jo 1:9).</p>
  </div>
</div>
"""

MODULOS_10 = [
    {
        "pasta": "contexto-historico",
        "cor": "#dc2626",
        "hero_bg": "#1a0000",
        "titulo": "Contexto Histórico das Cruzadas",
        "subtitulo": "🗺️ Contexto · Séc. XI",
        "ref": "O Mundo em 1095 · Expansão Islâmica · Reforma Gregoriana · Clermont",
        "citacao": "Deus lo vult! — Deus quer!",
        "autor_cit": "Grito da multidão no Concílio de Clermont, ao ouvir o discurso do Papa Urbano II (1095)",
        "corpo": contexto_corpo,
        "nav_prev": "/10-cruzadas/index.html",
        "nav_prev_lbl": "← Índice Bloco 10",
        "nav_next": "/10-cruzadas/primeira-cruzada",
        "nav_next_lbl": "Primeira Cruzada →",
    },
    {
        "pasta": "primeira-cruzada",
        "cor": "#f59e0b",
        "hero_bg": "#1a0e00",
        "titulo": "A Primeira Cruzada (1096–1099)",
        "subtitulo": "⚔️ Primeira Cruzada · 1096–1099",
        "ref": "Pedro o Eremita · Godofredo de Bulhão · Antioquia · Conquista de Jerusalém",
        "citacao": "No Templo e no Pórtico de Salomão, cavaleiros andavam no sangue dos sarracenos até os joelhos e as rédeas dos cavalos.",
        "autor_cit": "Raimundo de Aguilers, cronista da Primeira Cruzada, descrevendo a conquista de Jerusalém (1099)",
        "corpo": primeira_corpo,
        "nav_prev": "/10-cruzadas/contexto-historico",
        "nav_prev_lbl": "← Contexto Histórico",
        "nav_next": "/10-cruzadas/cruzadas-seguintes",
        "nav_next_lbl": "Cruzadas Seguintes →",
    },
    {
        "pasta": "cruzadas-seguintes",
        "cor": "#ef4444",
        "hero_bg": "#1a0000",
        "titulo": "As Cruzadas Seguintes (2ª a 3ª)",
        "subtitulo": "🏰 2ª e 3ª Cruzadas · 1147–1192",
        "ref": "Bernardo de Claraval · Saladino · Hattin · Ricardo Coração de Leão",
        "citacao": "Vim ver um homem honrado e encontrei mais do que isso.",
        "autor_cit": "Saladino, sobre Ricardo Coração de Leão, segundo os cronistas medievais",
        "corpo": seguintes_corpo,
        "nav_prev": "/10-cruzadas/primeira-cruzada",
        "nav_prev_lbl": "← Primeira Cruzada",
        "nav_next": "/10-cruzadas/saque-constantinopla",
        "nav_next_lbl": "Saque de Constantinopla →",
    },
    {
        "pasta": "saque-constantinopla",
        "cor": "#a855f7",
        "hero_bg": "#0d001a",
        "titulo": "O Saque de Constantinopla (1204)",
        "subtitulo": "🔥 Quarta Cruzada · 1204",
        "ref": "Desvio Veneziano · Enrico Dandolo · Império Latino · Ferida Ecumênica",
        "citacao": "Os sarracenos são mais misericordiosos e humanos do que estes homens que carregam a Cruz de Cristo no ombro.",
        "autor_cit": "Nicetas Choniates, cronista bizantino, sobre o saque de Constantinopla pelos cruzados (1204)",
        "corpo": saque_corpo,
        "nav_prev": "/10-cruzadas/cruzadas-seguintes",
        "nav_prev_lbl": "← Cruzadas Seguintes",
        "nav_next": "/10-cruzadas/cruzadas-nordeste",
        "nav_next_lbl": "Cruzadas do Norte →",
    },
    {
        "pasta": "cruzadas-nordeste",
        "cor": "#22d3ee",
        "hero_bg": "#001a1f",
        "titulo": "Cruzadas do Norte e do Interior",
        "subtitulo": "🌲 Báltico · Albigense · Séc. XII–XIII",
        "ref": "Ordem Teutônica · Cátaros · Béziers · Inquisição Medieval",
        "citacao": "Matai todos — Deus reconhecerá os seus.",
        "autor_cit": "Frase atribuída ao legado papal Arnaldo Amaury no massacre de Béziers (1209) — símbolo da Cruzada Albigense",
        "corpo": nordeste_corpo,
        "nav_prev": "/10-cruzadas/saque-constantinopla",
        "nav_prev_lbl": "← Saque de Constantinopla",
        "nav_next": "/10-cruzadas/ordens-militares",
        "nav_next_lbl": "Ordens Militares →",
    },
    {
        "pasta": "ordens-militares",
        "cor": "#818cf8",
        "hero_bg": "#0a0a1f",
        "titulo": "As Ordens Militares",
        "subtitulo": "🛡️ Templários · Hospitalários · Teutônicos",
        "ref": "Monges-Guerreiros · Bernardo de Claraval · Jacques de Molay · Cavaleiros de Malta",
        "citacao": "O cavaleiro de Cristo mata com segurança e morre com mais segurança ainda. Ele serve a Cristo quando mata, e serve a si mesmo quando é morto.",
        "autor_cit": "Bernardo de Claraval, De laude novae militiae — defesa teológica das Ordens Militares",
        "corpo": ordens_corpo,
        "nav_prev": "/10-cruzadas/cruzadas-nordeste",
        "nav_prev_lbl": "← Cruzadas do Norte",
        "nav_next": "/10-cruzadas/francisco-sultan",
        "nav_next_lbl": "Francisco e o Sultão →",
    },
    {
        "pasta": "francisco-sultan",
        "cor": "#22c55e",
        "hero_bg": "#001a08",
        "titulo": "Francisco de Assis e o Sultão Al-Kamil",
        "subtitulo": "🕊️ Damieta · 1219",
        "ref": "Quinta Cruzada · Missão Desarmada · Diálogo Inter-Religioso · Guardiões dos Lugares Santos",
        "citacao": "Os frades que vão entre os sarracenos não façam disputas nem contendas, mas sejam sujeitos a toda criatura humana por amor de Deus.",
        "autor_cit": "Francisco de Assis, Regra dos Frades Menores — o modelo de missão que ele levou ao Sultão",
        "corpo": francisco_corpo,
        "nav_prev": "/10-cruzadas/ordens-militares",
        "nav_prev_lbl": "← Ordens Militares",
        "nav_next": "/10-cruzadas/consequencias",
        "nav_next_lbl": "Consequências →",
    },
    {
        "pasta": "consequencias",
        "cor": "#10b981",
        "hero_bg": "#001a0e",
        "titulo": "Consequências e Legado das Cruzadas",
        "subtitulo": "🌍 Legado · Séc. XIII–XXI",
        "ref": "Fracasso Militar · Intercâmbio Cultural · Memória Islâmica · Avaliação Cristã",
        "citacao": "As Cruzadas foram uma das maiores tragédias da história cristã — e um dos maiores estímulos ao intercâmbio cultural entre o Oriente e o Ocidente.",
        "autor_cit": "Síntese historiográfica contemporânea sobre o legado das Cruzadas",
        "corpo": consequencias_corpo,
        "nav_prev": "/10-cruzadas/francisco-sultan",
        "nav_prev_lbl": "← Francisco e o Sultão",
        "nav_next": "/10-cruzadas/index.html",
        "nav_next_lbl": "Índice Bloco 10 →",
    },
]


def main():
    for m in MODULOS_10:
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
    print("\n🎉 Bloco 10 completo!")


if __name__ == "__main__":
    main()
