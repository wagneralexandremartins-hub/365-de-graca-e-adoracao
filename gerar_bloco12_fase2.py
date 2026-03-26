#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os módulos da fase 2 do Bloco 12 — 7 Selos, 7 Trombetas, Mulher/Dragão, 7 Taças."""

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
    .cavaleiro { border-radius: 14px; padding: 20px 22px; margin-bottom: 18px; border: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.02); }
    .cav-header { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
    .cav-num { font-size: 1.6rem; }
    .cav-nome { font-size: 1rem; font-weight: 800; color: #f1f5f9; }
    .cav-ref { font-size: 0.78rem; color: #64748b; font-weight: 600; }
    .cav-desc { font-size: 0.9rem; color: #94a3b8; line-height: 1.82; }
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
    .cav-nome {{ color: {cor}; }}
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
# MÓDULO: OS 7 SELOS (Caps. 6–8)
# ============================================================
selos_corpo = """
<div class="sb">
  <h2>🔓 Os 7 Selos — Contexto e Significado</h2>
  <p>Com a abertura dos sete selos pelo Cordeiro (Ap 6–8), o Apocalipse entra em sua primeira série de julgamentos. Os selos representam o desdobramento do plano de Deus para a história — o "livro selado" que o Cordeiro é digno de abrir (Ap 5). Cada selo revela um aspecto da condição humana e do julgamento divino durante o período entre a primeira e a segunda vinda de Cristo. Eles não são eventos futuros específicos — são realidades que caracterizam toda a era da Igreja: guerra, fome, morte, perseguição, julgamento cósmico.</p>
  <p>Os primeiros quatro selos introduzem os famosos "Quatro Cavaleiros do Apocalipse" — uma imagem que se tornou parte do imaginário cultural universal. Eles têm raízes em Zacarias 1:8–17 e 6:1–8, onde cavaleiros de diferentes cores patrulham a terra. No Apocalipse, eles representam as forças que Deus permite que operem na história como instrumentos de julgamento e advertência — não como agentes do caos, mas como servos do Senhor soberano da história.</p>
</div>
<div class="sb">
  <h2>🐴 Os Quatro Cavaleiros (Ap 6:1–8)</h2>
  <div class="cavaleiro">
    <div class="cav-header"><div class="cav-num">🤍</div><div><div class="cav-nome">1º Selo — O Cavaleiro Branco</div><div class="cav-ref">Ap 6:1–2 · Arco · Coroa · Conquista</div></div></div>
    <div class="cav-desc">O cavaleiro branco com arco e coroa "saiu conquistando e para conquistar." Há debate sobre sua identidade: alguns o identificam com Cristo (como em Ap 19:11), mas a maioria dos comentaristas o identifica com o Anticristo ou com o espírito de conquista e imperialismo que caracteriza a história humana. O arco sem flechas pode sugerir conquista por meios políticos ou diplomáticos, não apenas militares. O branco pode ser uma imitação enganosa da pureza — o Anticristo sempre se apresenta como alternativa ao Cristo verdadeiro. Esta interpretação é consistente com o padrão do Apocalipse de apresentar falsificações satânicas das realidades divinas.</div>
  </div>
  <div class="cavaleiro">
    <div class="cav-header"><div class="cav-num">❤️</div><div><div class="cav-nome">2º Selo — O Cavaleiro Vermelho</div><div class="cav-ref">Ap 6:3–4 · Grande Espada · Guerra · Derramamento de Sangue</div></div></div>
    <div class="cav-desc">O cavaleiro vermelho "recebeu poder para tirar a paz da terra, para que os homens se matassem uns aos outros; e foi-lhe dada uma grande espada." O vermelho é a cor do sangue e da guerra. A "grande espada" (<em>machaira megale</em>) é a espada do combate — não a espada da justiça. Este cavaleiro representa a guerra em todas as suas formas: guerras entre nações, guerras civis, conflitos tribais e étnicos. A guerra é uma constante da história humana — e o Apocalipse a reconhece como parte da realidade do mundo caído, permitida por Deus como julgamento e advertência.</div>
  </div>
  <div class="cavaleiro">
    <div class="cav-header"><div class="cav-num">🖤</div><div><div class="cav-nome">3º Selo — O Cavaleiro Negro</div><div class="cav-ref">Ap 6:5–6 · Balança · Fome · Escassez</div></div></div>
    <div class="cav-desc">O cavaleiro negro carrega uma balança — instrumento de medição e racionamento. Uma voz anuncia: "Uma medida de trigo por um denário, e três medidas de cevada por um denário; mas não danifiques o azeite e o vinho." Um denário era o salário diário de um trabalhador — o preço anunciado significa que um dia inteiro de trabalho compraria apenas o suficiente para alimentar uma pessoa. O azeite e o vinho — artigos de luxo — permanecem acessíveis, revelando a injustiça social que acompanha a escassez: os ricos continuam a prosperar enquanto os pobres passam fome. A fome é frequentemente consequência da guerra — os cavaleiros não são independentes, mas se seguem e se alimentam mutuamente.</div>
  </div>
  <div class="cavaleiro">
    <div class="cav-header"><div class="cav-num">💚</div><div><div class="cav-nome">4º Selo — O Cavaleiro Amarelo-Esverdeado (Morte)</div><div class="cav-ref">Ap 6:7–8 · Morte · Hades · Espada · Fome · Pestilência · Feras</div></div></div>
    <div class="cav-desc">O quarto cavaleiro é o único com nome: "Morte" (<em>Thanatos</em>). O Hades o segue — a morte e o reino dos mortos andam juntos. Ele tem poder sobre um quarto da terra, para matar "com espada, com fome, com pestilência e com as feras da terra" — os quatro julgamentos de Ezequiel 14:21. A cor "amarelo-esverdeada" (<em>chloros</em>) é a cor da palidez cadavérica — a cor da morte. Este cavaleiro é a síntese dos três anteriores: conquista, guerra e fome culminam na morte em massa. A limitação a "um quarto da terra" é importante: os julgamentos dos selos são parciais — advertências, não o julgamento final.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 Os Selos 5, 6 e 7</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 6:9–11 — 5º Selo: Os Mártires sob o Altar</div>
    <div class="v-texto">"Quando abriu o quinto selo, vi debaixo do altar as almas dos que tinham sido mortos por causa da palavra de Deus e por causa do testemunho que tinham dado. E clamavam em grande voz, dizendo: Até quando, ó Soberano Senhor, santo e verdadeiro, não julgas e não vingas o nosso sangue dos que habitam na terra? E foi dada a cada um deles uma veste branca; e foi-lhes dito que descansassem ainda um pouco de tempo."</div>
    <div class="v-analise">O 5º selo é radicalmente diferente dos quatro primeiros — não é um cavaleiro, mas uma visão do altar celestial. "Debaixo do altar" evoca o ritual do AT em que o sangue dos animais sacrificados era derramado na base do altar (Lv 4:7) — os mártires são apresentados como sacrifícios oferecidos a Deus. O clamor "Até quando?" é o clamor dos Salmos de lamento (Sl 6:3; 13:1–2; 79:5) — a oração mais honesta e corajosa da Bíblia. A resposta divina não é uma explicação teológica — é uma veste branca (símbolo de vitória e pureza) e um chamado à paciência. O sofrimento dos mártires não é esquecido por Deus — ele está sendo contado e será vindicado.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 6:12–17 — 6º Selo: Os Sinais Cósmicos</div>
    <div class="v-texto">"Vi quando abriu o sexto selo, e houve um grande terremoto; e o sol tornou-se negro como saco de crina, e a lua inteira tornou-se como sangue; e as estrelas do céu caíram sobre a terra... E os reis da terra, os grandes, os comandantes, os ricos, os poderosos e todo escravo e todo livre esconderam-se nas cavernas e nas rochas das montanhas; e diziam às montanhas e às rochas: Caí sobre nós e escondei-nos da face do que está assentado no trono e da ira do Cordeiro."</div>
    <div class="v-analise">O 6º selo usa a linguagem da "desolação cósmica" — um recurso literário comum nos profetas do AT para descrever grandes julgamentos históricos (Is 13:10 sobre Babilônia; Ez 32:7–8 sobre o Egito; Jl 2:10 sobre o Dia do Senhor). Esta linguagem não deve ser interpretada literalmente — ela descreve a magnitude do julgamento divino em termos que evocam o fim do mundo, mesmo quando se refere a eventos históricos. A cena dos poderosos da terra se escondendo "da ira do Cordeiro" é profundamente irônica: o Cordeiro — símbolo de fraqueza e sacrifício — é o objeto de terror dos mais poderosos do mundo. Nenhum poder humano pode escapar do julgamento de Deus.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 7:1–17 — O Interlúdio: Os 144.000 e a Multidão Incontável</div>
    <div class="v-texto">"Depois disto, vi uma grande multidão que ninguém podia contar, de todas as nações, tribos, povos e línguas, que estava em pé diante do trono e diante do Cordeiro, vestida de vestes brancas e com palmas nas mãos; e clamavam em grande voz, dizendo: A salvação pertence ao nosso Deus, que está assentado no trono, e ao Cordeiro."</div>
    <div class="v-analise">O capítulo 7 é um interlúdio entre o 6º e o 7º selos — uma pausa para responder à pergunta do 6º selo: "Quem poderá subsistir?" (Ap 6:17). A resposta é dupla: os 144.000 selados (representando o povo de Deus protegido durante a tribulação) e a multidão incontável (representando o povo de Deus glorificado após a tribulação). Os 144.000 (12 tribos × 12.000 cada) é um número simbólico representando a plenitude do povo de Deus — não 144.000 judeus literais. A multidão incontável "de todas as nações, tribos, povos e línguas" é a resposta à promessa de Abraão (Gn 12:3) e ao mandato missionário de Jesus (Mt 28:19): a salvação alcança toda a humanidade.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 8:1 — 7º Selo: Silêncio no Céu</div>
    <div class="v-texto">"Quando abriu o sétimo selo, houve silêncio no céu por quase meia hora."</div>
    <div class="v-analise">O 7º selo é o mais surpreendente de todos — não um julgamento dramático, mas silêncio. Após a adoração incessante dos capítulos 4–7, o silêncio é ensurdecedor. Este silêncio pode representar: (1) o silêncio antes da tempestade — a pausa antes dos julgamentos mais severos das trombetas; (2) o silêncio da reverência diante da majestade de Deus; (3) o silêncio das orações dos santos sendo apresentadas a Deus (Ap 8:3–4). O 7º selo não é um julgamento em si — ele abre para a série das 7 trombetas, revelando que os selos e as trombetas estão conectados em uma progressão de intensidade crescente.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: Os Cavaleiros e a Esperança</h3>
    <p>Os Quatro Cavaleiros do Apocalipse são uma das imagens mais poderosas da Escritura — e uma das mais mal compreendidas. Eles não são agentes do caos que escaparam do controle de Deus — eles são libertados pelo Cordeiro, que abre cada selo. Isto significa que mesmo as piores calamidades da história — guerra, fome, pestilência, morte — estão sob a soberania de Deus. Ele não as causa, mas as permite e as limita. Para os cristãos perseguidos de Patmos — e para os cristãos que sofrem hoje — esta é uma afirmação de imenso conforto: o sofrimento não é evidência de que Deus perdeu o controle. É evidência de que vivemos em um mundo caído que está sendo redimido pelo Cordeiro que foi imolado e que voltará para fazer novas todas as coisas.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO: AS 7 TROMBETAS (Caps. 8–11)
# ============================================================
trombetas_corpo = """
<div class="sb">
  <h2>🎺 As 7 Trombetas — Advertências Progressivas</h2>
  <p>As sete trombetas (Ap 8:2–11:19) são a segunda série de julgamentos do Apocalipse. Elas seguem um padrão estrutural semelhante aos selos, mas com intensidade crescente: enquanto os selos afetam "um quarto" da terra, as trombetas afetam "um terço." Esta progressão sugere que as trombetas são advertências mais severas — chamados ao arrependimento antes do julgamento final das sete taças. As trombetas têm raízes profundas nas pragas do Êxodo (Ex 7–12) — assim como Deus julgou o Egito para libertar seu povo, ele julga o mundo para libertar sua Igreja.</p>
  <p>As trombetas são precedidas por uma cena de intercessão: os anjos apresentam as orações dos santos diante do altar celestial, e o incenso das orações sobe diante de Deus (Ap 8:3–5). Isto é teologicamente fundamental: os julgamentos das trombetas são, em parte, a resposta de Deus às orações de seu povo — especialmente ao clamor dos mártires do 5º selo: "Até quando?" Os julgamentos não são caprichosos — eles são a resposta de Deus à injustiça e à perseguição.</p>
</div>
<div class="sb">
  <h2>📖 As Primeiras Quatro Trombetas (Ap 8:6–12)</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 8:7 — 1ª Trombeta: Granizo, Fogo e Sangue</div>
    <div class="v-texto">"O primeiro tocou a trombeta, e houve granizo e fogo misturados com sangue, e foram lançados sobre a terra; e a terça parte da terra foi queimada, e a terça parte das árvores foi queimada, e toda a erva verde foi queimada."</div>
    <div class="v-analise">A 1ª trombeta evoca a 7ª praga do Egito (granizo — Ex 9:23–24) e o fogo de Ezequiel 38:22. A destruição de "um terço" da terra e das árvores é parcial — uma advertência, não o julgamento final. As árvores no AT frequentemente simbolizam nações e reinos (Dn 4:10–12; Ez 31). A destruição da "erva verde" afeta a base da cadeia alimentar — um julgamento econômico e ecológico.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 8:8–9 — 2ª Trombeta: A Grande Montanha em Chamas</div>
    <div class="v-texto">"O segundo anjo tocou a trombeta, e algo como uma grande montanha ardendo em fogo foi lançado no mar; e a terça parte do mar tornou-se sangue, e morreu a terça parte das criaturas que viviam no mar, e a terça parte dos navios foi destruída."</div>
    <div class="v-analise">A "grande montanha ardendo em fogo" evoca Jeremias 51:25, onde Babilônia é chamada de "montanha destruidora." No AT, "montanha" frequentemente simboliza um reino ou poder político. O mar se tornando sangue evoca a 1ª praga do Egito (Ex 7:20–21). A destruição de "um terço dos navios" afeta o comércio marítimo — o sustento econômico do Império Romano, que dependia do Mediterrâneo para seu comércio.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 8:10–11 — 3ª Trombeta: A Estrela Absinto</div>
    <div class="v-texto">"O terceiro anjo tocou a trombeta, e caiu do céu uma grande estrela, ardendo como uma tocha, e caiu sobre a terça parte dos rios e sobre as fontes das águas. O nome da estrela é Absinto; e a terça parte das águas tornou-se absinto, e muitos homens morreram por causa das águas, porque se tornaram amargas."</div>
    <div class="v-analise">"Absinto" (<em>Apsinthos</em>) é uma planta amarga e venenosa. A contaminação das águas evoca a 1ª praga do Egito e Jeremias 9:15 ("darei a este povo água de absinto para beber"). Uma estrela caindo do céu frequentemente simboliza um anjo ou um governante caído (Is 14:12; Lc 10:18). A amargura das águas pode simbolizar a corrupção da verdade e do ensinamento — "fontes" frequentemente simbolizam ensinamento no AT (Pv 5:15–16; Is 12:3).</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 8:12 — 4ª Trombeta: Trevas Parciais</div>
    <div class="v-texto">"O quarto anjo tocou a trombeta, e foi atingida a terça parte do sol, a terça parte da lua e a terça parte das estrelas, de modo que a terça parte deles se escureceu, e o dia perdeu a terça parte do seu brilho, e a noite da mesma forma."</div>
    <div class="v-analise">A 4ª trombeta evoca a 9ª praga do Egito (trevas — Ex 10:21–23) e a linguagem profética de julgamento (Is 13:10; Jl 2:10). O escurecimento parcial dos luminares celestiais representa a perturbação da ordem cósmica — o mundo criado sendo desestabilizado pelo pecado e pelo julgamento. No AT, o sol, a lua e as estrelas frequentemente simbolizam governantes e poderes (Gn 37:9; Is 24:23). A perturbação dos "luminares" pode simbolizar a queda de poderes políticos e religiosos.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 As Três "Ais" — As Trombetas 5, 6 e 7</h2>
  <p>Após as quatro primeiras trombetas, uma águia voa pelo céu proclamando: "Ai, ai, ai dos que habitam na terra, por causa das demais vozes de trombeta dos três anjos que ainda hão de tocar" (Ap 8:13). As três últimas trombetas são chamadas de "ais" (<em>ouai</em>) — um termo de lamento profético que indica julgamentos de intensidade ainda maior.</p>
  <div class="versiculo">
    <div class="v-ref">Ap 9:1–12 — 5ª Trombeta (1º Ai): Os Gafanhotos do Abismo</div>
    <div class="v-texto">"O quinto anjo tocou a trombeta, e vi uma estrela que havia caído do céu à terra; e foi-lhe dada a chave do poço do abismo. E abriu o poço do abismo, e subiu fumaça do poço, como a fumaça de uma grande fornalha... E da fumaça saíram gafanhotos para a terra, e foi-lhes dado poder como o poder que têm os escorpiões da terra."</div>
    <div class="v-analise">A "estrela que havia caído do céu" é provavelmente Satanás ou um anjo caído (cf. Is 14:12; Lc 10:18). O "poço do abismo" (<em>phrear tēs abyssou</em>) é a prisão dos demônios (Lc 8:31; 2 Pe 2:4). Os gafanhotos evocam a 8ª praga do Egito (Ex 10:12–15) e Joel 1–2, mas são radicalmente diferentes dos gafanhotos naturais: eles não atacam a vegetação, mas os seres humanos que não têm o selo de Deus. Seu rei é "Abadão" (hebraico) / "Apolião" (grego) — "o Destruidor." O período de seu tormento é "cinco meses" — o período de vida dos gafanhotos naturais, sugerindo um período limitado e controlado.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 9:13–21 — 6ª Trombeta (2º Ai): O Exército do Eufrates</div>
    <div class="v-texto">"O sexto anjo tocou a trombeta, e ouvi uma voz dos quatro chifres do altar de ouro que está diante de Deus, dizendo ao sexto anjo que tinha a trombeta: Solta os quatro anjos que estão presos junto ao grande rio Eufrates. E foram soltos os quatro anjos que estavam preparados para a hora, o dia, o mês e o ano, para matar a terça parte dos homens."</div>
    <div class="v-analise">O Eufrates era a fronteira oriental do Império Romano — de lá vinham os temidos Partos, os únicos inimigos que Roma nunca conseguiu derrotar completamente. O "exército de duzentos milhões" (Ap 9:16) é claramente simbólico — um número impossível de soldados literais. Os cavalos com cabeças de leão e caudas de serpente são imagens de destruição sobrenatural. O propósito deste julgamento é o arrependimento — mas o versículo 20–21 registra a resposta trágica: "os demais homens, que não foram mortos por estas pragas, não se arrependeram." O julgamento sem arrependimento é a tragédia central do Apocalipse.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 10–11 — O Interlúdio: O Livrinho e os Dois Testemunhos</div>
    <div class="v-texto">"E vi outro anjo poderoso descendo do céu... tendo na mão um livrinho aberto... E a voz que ouvi do céu falou comigo outra vez, dizendo: Vai, toma o livrinho aberto na mão do anjo... Tomei o livrinho da mão do anjo e o comi; e era doce como mel na minha boca, mas depois que o comi, o meu estômago ficou amargo."</div>
    <div class="v-analise">O interlúdio entre a 6ª e a 7ª trombeta (caps. 10–11) apresenta dois elementos cruciais. O "livrinho" que João come evoca Ezequiel 3:1–3 — o profeta que come o rolo da palavra de Deus. A palavra de Deus é doce (a promessa da salvação) mas amarga (o peso do julgamento que ela anuncia). Os "Dois Testemunhos" (Ap 11:3–13) são figuras proféticas que testemunham durante "1.260 dias" (3½ anos) — o período simbólico da tribulação. Eles têm poderes que evocam Moisés (transformar água em sangue) e Elias (fechar o céu). Eles são mortos, ressuscitam e ascendem ao céu — um padrão que evoca a morte e ressurreição de Cristo e antecipa a ressurreição dos fiéis.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 11:15–19 — 7ª Trombeta (3º Ai): O Reino de Deus</div>
    <div class="v-texto">"O sétimo anjo tocou a trombeta, e houve grandes vozes no céu, dizendo: O reino do mundo se tornou o reino do nosso Senhor e do seu Cristo, e ele reinará pelos séculos dos séculos."</div>
    <div class="v-analise">A 7ª trombeta não é um julgamento — é uma proclamação de vitória. "O reino do mundo se tornou o reino do nosso Senhor e do seu Cristo" — esta é a afirmação central do Apocalipse: a história não está fora do controle de Deus, mas está sendo conduzida em direção ao seu reino eterno. Os 24 anciãos prostram-se em adoração, e o templo celestial se abre, revelando a arca da aliança — o símbolo da presença e da fidelidade de Deus ao seu povo. Esta visão de vitória é o clímax teológico da primeira metade do Apocalipse — e ela precede as visões mais sombrias dos capítulos 12–16, lembrando ao leitor que o resultado final já está determinado.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: Julgamento e Misericórdia</h3>
    <p>As sete trombetas revelam uma tensão fundamental na natureza de Deus: ele é simultaneamente justo (ele julga o pecado) e misericordioso (ele chama ao arrependimento antes do julgamento final). A tragédia registrada em Apocalipse 9:20–21 — "não se arrependeram" — é o coração partido de Deus diante da recusa humana de responder à sua graça. Os julgamentos do Apocalipse não são expressões de sadismo divino — são expressões do amor de Deus que usa todos os meios disponíveis para chamar a humanidade ao arrependimento antes que seja tarde demais. A pergunta que as trombetas nos fazem é: "Estamos respondendo aos julgamentos de Deus com arrependimento e fé, ou com endurecimento e recusa?"</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO: MULHER, DRAGÃO E AS BESTAS (Caps. 12–14)
# ============================================================
dragao_corpo = """
<div class="sb">
  <h2>🐉 O Coração do Conflito Cósmico</h2>
  <p>Os capítulos 12–14 são o centro literário e teológico do Apocalipse — a seção que revela as forças espirituais por trás dos julgamentos e perseguições descritos nos capítulos anteriores. Aqui o véu é levantado e o conflito cósmico é revelado em toda a sua magnitude: de um lado, a Mulher (o povo de Deus), o Cordeiro e os 144.000; do outro, o Dragão (Satanás), a Besta do mar (o Anticristo) e a Besta da terra (o Falso Profeta). Esta é a "Santíssima Trindade Satânica" — uma falsificação diabólica da Trindade divina.</p>
  <p>A linguagem destes capítulos é deliberadamente mítica e cósmica — ela opera em um nível que transcende qualquer identificação histórica específica. A Mulher não é apenas Israel ou apenas a Igreja — ela é o povo de Deus em toda a sua extensão histórica. O Dragão não é apenas Satanás em um momento específico — ele é o adversário eterno de Deus e de seu povo. A Besta não é apenas Nero ou Domiciano — ela é qualquer poder político que exige adoração absoluta e persegue os fiéis. Esta dimensão mítica e atemporal é o que torna estes capítulos tão poderosos e tão relevantes para cada geração.</p>
</div>
<div class="sb">
  <h2>📖 A Mulher Vestida de Sol (Ap 12:1–6)</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 12:1–6</div>
    <div class="v-texto">"E um grande sinal apareceu no céu: uma mulher vestida do sol, com a lua debaixo dos seus pés, e uma coroa de doze estrelas sobre a sua cabeça. Ela estava grávida e clamava com as dores do parto, angustiada para dar à luz... E apareceu outro sinal no céu: eis um grande dragão vermelho, com sete cabeças e dez chifres, e sobre as suas cabeças sete diademas."</div>
    <div class="v-analise">A Mulher vestida de sol evoca o sonho de José em Gênesis 37:9 (sol, lua e estrelas = a família de Israel) e a imagem de Israel como esposa de Deus nos profetas (Is 54:5–6; Jr 3:20; Os 2:16). Ela representa o povo de Deus — Israel no AT que deu à luz o Messias, e a Igreja no NT que continua a missão messiânica. As "dores do parto" evocam Isaías 26:17 e Miquéias 4:10 — o sofrimento do povo de Deus antes da redenção. O Dragão vermelho com sete cabeças e dez chifres é identificado em Ap 12:9 como "a antiga serpente, chamada Diabo e Satanás." As sete cabeças e dez chifres evocam as bestas de Daniel 7 — Satanás opera através dos impérios mundiais.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 A Guerra no Céu (Ap 12:7–17)</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 12:7–12</div>
    <div class="v-texto">"E houve batalha no céu: Miguel e os seus anjos batalharam contra o dragão; e o dragão e os seus anjos batalharam, mas não prevaleceram, e já não se achou lugar para eles no céu. E foi expulso o grande dragão, a antiga serpente, chamado Diabo e Satanás, o sedutor de todo o mundo; foi atirado para a terra, e os seus anjos foram atirados com ele... Ai da terra e do mar! Porque o diabo desceu a vós, cheio de grande furor, sabendo que tem pouco tempo."</div>
    <div class="v-analise">A guerra no céu e a expulsão de Satanás é um evento que o Apocalipse conecta à morte e ressurreição de Cristo: "Agora veio a salvação, e o poder, e o reino do nosso Deus, e a autoridade do seu Cristo; porque foi expulso o acusador de nossos irmãos" (Ap 12:10). A Cruz foi a derrota decisiva de Satanás (Jo 12:31; Cl 2:15). A expulsão de Satanás do céu não é um evento futuro — é a realidade presente que a Cruz estabeleceu. A "grande furor" de Satanás é a furor do derrotado — ele sabe que "tem pouco tempo." A perseguição da Igreja não é evidência do poder de Satanás — é evidência de seu desespero.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 A Besta do Mar — O Anticristo (Ap 13:1–10)</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 13:1–4</div>
    <div class="v-texto">"E vi uma besta subindo do mar, com dez chifres e sete cabeças, e sobre os seus chifres dez diademas, e sobre as suas cabeças nomes de blasfêmia. A besta que vi era semelhante a um leopardo, e os seus pés como os de urso, e a sua boca como a boca de leão; e o dragão lhe deu o seu poder, o seu trono e grande autoridade."</div>
    <div class="v-analise">A Besta do mar é uma combinação das quatro bestas de Daniel 7 (leão = Babilônia, urso = Medo-Pérsia, leopardo = Grécia, besta terrível = Roma) — ela representa a síntese de todos os impérios opressores da história. O "mar" no AT frequentemente simboliza o caos e as nações pagãs (Is 57:20; Dn 7:2–3). A Besta recebe seu poder do Dragão — ela é o instrumento político de Satanás. A ferida mortal curada (Ap 13:3) pode aludir ao mito de Nero redivivus (a crença de que Nero havia ressuscitado) ou pode simbolizar a aparente invencibilidade dos poderes opressores. A adoração da Besta — "Quem é semelhante à besta? Quem pode batalhar contra ela?" — é a adoração do poder bruto.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 13:5–10</div>
    <div class="v-texto">"E foi-lhe dada uma boca que proferiu palavras arrogantes e blasfêmias; e foi-lhe dado poder para agir durante quarenta e dois meses... E foi-lhe dado poder para fazer guerra contra os santos e para vencê-los; e foi-lhe dado poder sobre toda tribo, povo, língua e nação."</div>
    <div class="v-analise">"Quarenta e dois meses" = 3½ anos = 1.260 dias = "tempo, tempos e metade de um tempo" (Dn 7:25; 12:7) — o período simbólico da tribulação, derivado da profecia de Daniel. Este período é deliberadamente metade de 7 — o número da perfeição — indicando que a tribulação é limitada e controlada por Deus. A Besta "faz guerra contra os santos e os vence" — uma afirmação chocante que o Apocalipse não suaviza. Os santos são vencidos externamente (martírio) mas vencem internamente (fidelidade). "Aqui está a perseverança e a fé dos santos" (Ap 13:10) — a resposta à perseguição não é resistência armada, mas perseverança fiel.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 A Besta da Terra e o Número 666 (Ap 13:11–18)</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 13:11–18</div>
    <div class="v-texto">"E vi outra besta subindo da terra; ela tinha dois chifres semelhantes aos de um cordeiro, mas falava como dragão... Aqui está a sabedoria. Aquele que tem entendimento calcule o número da besta, pois é número de homem. O seu número é seiscentos e sessenta e seis."</div>
    <div class="v-analise">A Besta da terra (identificada em Ap 16:13 como o "falso profeta") é o braço religioso e propagandístico da Besta do mar. Ela "tem dois chifres semelhantes aos de um cordeiro" — uma imitação de Cristo — "mas fala como dragão." Ela realiza sinais e maravilhas para enganar (evocando os falsos profetas de Dt 13:1–3 e Mt 24:24). O número 666 é um exemplo de <em>gematria</em> — a prática de atribuir valores numéricos a letras. Em grego e hebraico, cada letra tem um valor numérico, e o nome de uma pessoa pode ser calculado somando os valores de suas letras. A identificação mais provável no contexto do século I é Nero César (em hebraico: נרון קסר = 50+200+6+50+100+60+200 = 666). Mas o número também funciona simbolicamente: 7 é o número da perfeição; 6 é o número da imperfeição humana; 666 é a imperfeição triplicada — o homem que tenta ser Deus mas sempre fica aquém.</div>
  </div>
</div>
<div class="sb">
  <h2>📖 O Cordeiro no Monte Sião (Ap 14:1–5)</h2>
  <div class="versiculo">
    <div class="v-ref">Ap 14:1–5</div>
    <div class="v-texto">"E olhei, e eis o Cordeiro em pé sobre o monte Sião, e com ele cento e quarenta e quatro mil que tinham o nome dele e o nome de seu Pai escrito nas suas testas... E cantavam um novo cântico diante do trono... Estes são os que seguem o Cordeiro por onde quer que ele vá. Estes foram comprados dentre os homens como primícias para Deus e para o Cordeiro."</div>
    <div class="v-analise">Após a visão sombria das Bestas (cap. 13), o capítulo 14 começa com uma visão de esperança: o Cordeiro no Monte Sião com os 144.000. Esta é a resposta divina às Bestas — enquanto a Besta marca seus seguidores com seu número (Ap 13:16–17), o Cordeiro tem seus seguidores marcados com o nome de Deus. O Monte Sião é o monte da presença de Deus — o lugar da adoração e da proteção divina. Os 144.000 "seguem o Cordeiro por onde quer que ele vá" — um chamado ao discipulado radical, mesmo até o martírio. Eles são "primícias" — os primeiros de uma colheita maior (a multidão incontável de Ap 7:9).</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: A Besta Ainda Existe</h3>
    <p>A Besta do Apocalipse não é apenas uma figura histórica do passado (Nero, Domiciano) ou uma figura escatológica do futuro. Ela é uma realidade presente em cada geração: qualquer poder político, econômico ou cultural que exige lealdade absoluta, que persegue os fiéis por se recusarem a dobrar o joelho, que usa a propaganda e os "sinais e maravilhas" da mídia e da tecnologia para manipular e controlar — esse poder está manifestando o espírito da Besta. A pergunta que o Apocalipse nos faz não é "quem é a Besta?" mas "estamos seguindo o Cordeiro ou a Besta?" A marca da Besta (Ap 13:16–17) e o selo de Deus (Ap 7:3; 14:1) são marcas de lealdade — e cada geração de cristãos é chamada a escolher de qual lado está.</p>
  </div>
</div>
"""

# ============================================================
# MÓDULO: AS 7 TAÇAS (Caps. 15–16)
# ============================================================
tacas_corpo = """
<div class="sb">
  <h2>🏺 As 7 Taças — O Julgamento Final</h2>
  <p>As sete taças (Ap 15–16) são a terceira e última série de julgamentos do Apocalipse — e a mais severa. Enquanto os selos afetavam "um quarto" e as trombetas afetavam "um terço", as taças são completas e totais. Elas são chamadas de "as últimas pragas, pois com elas se consumou a ira de Deus" (Ap 15:1). As taças têm paralelos ainda mais estreitos com as pragas do Êxodo do que as trombetas — elas são o Êxodo final, a libertação definitiva do povo de Deus do poder do "Egito" espiritual (Babilônia/Roma/o mundo).</p>
  <p>Os capítulos 15–16 são precedidos por uma cena de adoração: os vencedores cantam o "Cântico de Moisés e do Cordeiro" (Ap 15:3–4) — o mesmo cântico que Israel cantou após a travessia do Mar Vermelho (Ex 15). Esta justaposição é deliberada: assim como o Êxodo foi precedido pelas pragas do Egito e seguido pelo cântico de vitória, o julgamento final (as taças) é precedido pelo cântico de vitória dos redimidos. A adoração precede e sustenta o julgamento — os fiéis não são espectadores passivos, mas participantes ativos da vitória de Deus.</p>
</div>
<div class="sb">
  <h2>📖 As Sete Taças (Ap 16)</h2>
  <table>
    <tr><th>Taça</th><th>Julgamento</th><th>Paralelo no Êxodo</th><th>Alvo</th></tr>
    <tr><td>1ª</td><td>Úlceras malignas sobre os que têm a marca da Besta</td><td>6ª praga (Ex 9:8–12)</td><td>Os seguidores da Besta</td></tr>
    <tr><td>2ª</td><td>O mar se torna sangue; toda criatura marinha morre</td><td>1ª praga (Ex 7:17–21)</td><td>O sistema econômico mundial</td></tr>
    <tr><td>3ª</td><td>Rios e fontes se tornam sangue</td><td>1ª praga (Ex 7:17–21)</td><td>Os que derramaram sangue dos santos</td></tr>
    <tr><td>4ª</td><td>O sol queima os homens com fogo</td><td>—</td><td>Os que adoraram a Besta</td></tr>
    <tr><td>5ª</td><td>Trevas sobre o trono da Besta</td><td>9ª praga (Ex 10:21–23)</td><td>O reino da Besta</td></tr>
    <tr><td>6ª</td><td>Eufrates seco; espíritos de rãs; Armagedom</td><td>—</td><td>Os reis do Oriente; batalha final</td></tr>
    <tr><td>7ª</td><td>Terremoto, granizo; "Está feito!"</td><td>7ª praga (Ex 9:22–26)</td><td>Babilônia e o mundo</td></tr>
  </table>
  <div class="versiculo">
    <div class="v-ref">Ap 16:5–7 — O Anjo das Águas Justifica o Julgamento</div>
    <div class="v-texto">"E ouvi o anjo das águas dizer: Justo és tu, que és e que eras, o Santo, porque julgaste assim; pois derramaram sangue de santos e de profetas, e tu lhes deste sangue para beber; são dignos disso. E ouvi o altar dizer: Sim, Senhor Deus, o Todo-Poderoso, verdadeiros e justos são os teus juízos."</div>
    <div class="v-analise">A justificação do julgamento divino é um tema central do Apocalipse — Deus não é um tirano caprichoso, mas um juiz justo. O princípio de talião ("derramaram sangue... tu lhes deste sangue para beber") é a lei da retribuição justa — o julgamento corresponde ao crime. O "altar" que fala é o altar sob o qual os mártires clamavam (Ap 6:9–10) — suas orações foram respondidas. O julgamento divino é a vindicação dos mártires e a resposta ao clamor "Até quando?"</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 16:12–16 — A 6ª Taça e Armagedom</div>
    <div class="v-texto">"O sexto anjo derramou a sua taça sobre o grande rio Eufrates; e as suas águas secaram, para que fosse preparado o caminho dos reis do Oriente... E os reuniu no lugar que em hebraico se chama Armagedom."</div>
    <div class="v-analise">"Armagedom" (hebraico: <em>Har Megiddo</em> — "Monte de Megido") é o vale de Jezreel, no norte de Israel — o local de batalhas decisivas na história de Israel (Juízes 5:19; 2 Rs 23:29). No Apocalipse, ele se torna o símbolo da batalha final entre Deus e as forças do mal — não necessariamente uma batalha geográfica literal, mas o conflito escatológico definitivo. Os "espíritos de rãs" que saem da boca do Dragão, da Besta e do Falso Profeta são espíritos demoníacos que enganam os reis da terra para reuní-los para esta batalha — a propaganda satânica que mobiliza o mundo contra Deus.</div>
  </div>
  <div class="versiculo">
    <div class="v-ref">Ap 16:17–21 — A 7ª Taça: "Está Feito!"</div>
    <div class="v-texto">"O sétimo anjo derramou a sua taça no ar, e saiu do templo uma grande voz, do trono, dizendo: Está feito! E houve relâmpagos, vozes e trovões; e houve um grande terremoto, qual nunca houve desde que há homens sobre a terra, tão grande terremoto e tão grande. E a grande cidade foi dividida em três partes, e as cidades das nações caíram; e a grande Babilônia foi lembrada diante de Deus, para lhe dar o cálice do vinho do furor da sua ira."</div>
    <div class="v-analise">"Está feito!" (<em>Gegonen</em> — "Aconteceu!") ecoa o "Está consumado!" de João 19:30 — a morte de Cristo que consumou a redenção. O julgamento final é a consumação do que a Cruz iniciou. O "maior terremoto da história" é linguagem apocalíptica para o colapso total da ordem mundial que se opõe a Deus. "A grande Babilônia foi lembrada diante de Deus" — Deus não esquece a injustiça, por mais que ela pareça triunfar. O julgamento de Babilônia é o tema dos capítulos 17–18.</div>
  </div>
  <div class="reflexao">
    <h3>🙏 Reflexão: A Ira do Cordeiro</h3>
    <p>As sete taças revelam um aspecto de Deus que a teologia contemporânea frequentemente evita: a ira divina. Mas a ira de Deus no Apocalipse não é a ira caprichosa de um tirano — é a ira justa do Deus que ama seus filhos e não pode tolerar que os opressores continuem impunes. A ira de Deus é o verso da moeda do amor de Deus: porque ele ama os mártires e os oprimidos, ele julga os opressores. Uma teologia que nega a ira de Deus acaba por negar também sua justiça — e uma teologia sem justiça não tem nada a dizer aos que sofrem injustamente. O Apocalipse insiste: Deus é justo, e sua justiça será feita. "Verdadeiros e justos são os teus juízos" (Ap 16:7).</p>
  </div>
</div>
"""

MODULOS_F2 = [
    {
        "pasta": "sete-selos",
        "cor": "#ef4444",
        "hero_bg": "#1a0000",
        "titulo": "Os 7 Selos — Os Quatro Cavaleiros e os Mártires",
        "subtitulo": "🔓 Apocalipse 6–8 · Os 7 Selos",
        "ref": "4 Cavaleiros · Mártires · Sinais Cósmicos · 144.000 · Silêncio no Céu",
        "citacao": "Até quando, ó Soberano Senhor, santo e verdadeiro, não julgas e não vingas o nosso sangue dos que habitam na terra?",
        "autor_cit": "Apocalipse 6:10 — o clamor dos mártires sob o altar celestial",
        "corpo": selos_corpo,
        "nav_prev": "/12-apocalipse/visao-trono",
        "nav_prev_lbl": "← Visão do Trono",
        "nav_next": "/12-apocalipse/sete-trombetas",
        "nav_next_lbl": "As 7 Trombetas →",
    },
    {
        "pasta": "sete-trombetas",
        "cor": "#f97316",
        "hero_bg": "#1a0800",
        "titulo": "As 7 Trombetas — Advertências e os Dois Testemunhos",
        "subtitulo": "🎺 Apocalipse 8–11 · As 7 Trombetas",
        "ref": "Pragas · Gafanhotos do Abismo · Eufrates · Dois Testemunhos · 7ª Trombeta",
        "citacao": "O reino do mundo se tornou o reino do nosso Senhor e do seu Cristo, e ele reinará pelos séculos dos séculos.",
        "autor_cit": "Apocalipse 11:15 — a proclamação da 7ª trombeta",
        "corpo": trombetas_corpo,
        "nav_prev": "/12-apocalipse/sete-selos",
        "nav_prev_lbl": "← Os 7 Selos",
        "nav_next": "/12-apocalipse/mulher-dragao",
        "nav_next_lbl": "Mulher e Dragão →",
    },
    {
        "pasta": "mulher-dragao",
        "cor": "#a855f7",
        "hero_bg": "#0d0020",
        "titulo": "A Mulher, o Dragão e as Bestas",
        "subtitulo": "🐉 Apocalipse 12–14 · O Conflito Cósmico",
        "ref": "Mulher Vestida de Sol · Dragão · Besta do Mar · 666 · Falso Profeta · Cordeiro no Sião",
        "citacao": "E eles o venceram por causa do sangue do Cordeiro e por causa da palavra do seu testemunho; e não amaram as suas vidas até à morte.",
        "autor_cit": "Apocalipse 12:11 — a fórmula da vitória dos mártires",
        "corpo": dragao_corpo,
        "nav_prev": "/12-apocalipse/sete-trombetas",
        "nav_prev_lbl": "← As 7 Trombetas",
        "nav_next": "/12-apocalipse/sete-tacas",
        "nav_next_lbl": "As 7 Taças →",
    },
    {
        "pasta": "sete-tacas",
        "cor": "#dc2626",
        "hero_bg": "#1a0000",
        "titulo": "As 7 Taças da Ira de Deus",
        "subtitulo": "🏺 Apocalipse 15–16 · As Pragas Finais",
        "ref": "Cântico de Moisés · 7 Pragas Finais · Armagedom · Está Feito!",
        "citacao": "Verdadeiros e justos são os teus juízos, ó Senhor Deus, o Todo-Poderoso.",
        "autor_cit": "Apocalipse 16:7 — o altar celestial justifica os julgamentos de Deus",
        "corpo": tacas_corpo,
        "nav_prev": "/12-apocalipse/mulher-dragao",
        "nav_prev_lbl": "← Mulher e Dragão",
        "nav_next": "/12-apocalipse/babilonia",
        "nav_next_lbl": "Babilônia →",
    },
]


def main():
    for m in MODULOS_F2:
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
    print("\n🎉 Fase 2 do Bloco 12 completa!")


if __name__ == "__main__":
    main()
