#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera capítulos aprofundados do Apocalipse:
- Cap 1: Visão do Cristo Glorificado
- Cap 2: As 7 Igrejas (parte 1) — Éfeso, Esmirna, Pérgamo, Tiatira
- Cap 3: As 7 Igrejas (parte 2) — Sardes, Filadélfia, Laodiceia
- Cap 4-5: O Trono Celestial e o Cordeiro
- Cap 12: A Mulher, o Dragão e o Filho
- Cap 19: As Bodas do Cordeiro e o Cavaleiro Branco
- Cap 21-22: A Nova Jerusalém
"""

import os

BASE = "/home/ubuntu/365-de-graca-e-adoracao/07-novo-testamento/apocalipse/capitulos"
COLOR = "#a855f7"
HERO_BG = "#0d001a"
TAG_BG = "rgba(168,85,247,0.1)"
TAG_BORDER = "rgba(168,85,247,0.25)"
TAG_HOVER = "rgba(168,85,247,0.2)"

CSS = f"""
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: #0f172a; color: #e2e8f0; font-family: 'Georgia', serif; line-height: 1.7; }}
    a {{ color: inherit; text-decoration: none; }}
    .topbar {{ background: rgba(15,23,42,0.97); border-bottom: 1px solid rgba(255,255,255,0.07); padding: 14px 0; position: sticky; top: 0; z-index: 100; }}
    .topbar .inner {{ max-width: 900px; margin: 0 auto; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }}
    .topbar a {{ font-size: 0.85rem; color: #94a3b8; font-weight: 600; transition: color 0.2s; }}
    .topbar a:hover {{ color: {COLOR}; }}
    .hero {{ background: linear-gradient(135deg, #0f172a 0%, {HERO_BG} 50%, #0f172a 100%); padding: 64px 24px 48px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.07); }}
    .tag {{ display: inline-block; background: {TAG_BG}; border: 1px solid {TAG_BORDER}; color: {COLOR}; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 999px; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 1px; }}
    .hero h1 {{ font-size: 2.4rem; font-weight: 900; color: #f1f5f9; margin-bottom: 12px; line-height: 1.2; }}
    .hero .ref {{ font-size: 0.88rem; color: #64748b; margin-bottom: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }}
    .hero blockquote {{ font-style: italic; color: #cbd5e1; font-size: 1rem; border-left: 3px solid {COLOR}; padding-left: 20px; max-width: 600px; margin: 0 auto; text-align: left; }}
    .wrap {{ max-width: 900px; margin: 0 auto; padding: 40px 24px 80px; }}
    .section-block {{ margin-bottom: 40px; }}
    .section-block h2 {{ font-size: 1.3rem; font-weight: 800; color: #f1f5f9; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.07); }}
    .section-block p {{ color: #94a3b8; font-size: 0.95rem; line-height: 1.85; margin-bottom: 16px; }}
    .versiculo-bloco {{ background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-left: 3px solid {COLOR}; border-radius: 0 12px 12px 0; padding: 18px 20px; margin-bottom: 16px; }}
    .ref-v {{ font-size: 0.8rem; font-weight: 800; color: {COLOR}; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }}
    .texto-v {{ font-style: italic; color: #cbd5e1; font-size: 0.95rem; margin-bottom: 10px; line-height: 1.7; }}
    .analise-v {{ color: #94a3b8; font-size: 0.9rem; line-height: 1.8; }}
    .igreja-card {{ background: rgba(168,85,247,0.05); border: 1px solid {TAG_BORDER}; border-radius: 14px; padding: 24px; margin-bottom: 24px; }}
    .igreja-nome {{ font-size: 1.2rem; font-weight: 900; color: {COLOR}; margin-bottom: 4px; }}
    .igreja-ref {{ font-size: 0.78rem; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 14px; }}
    .igreja-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 14px; }}
    @media (max-width: 600px) {{ .igreja-grid {{ grid-template-columns: 1fr; }} }}
    .ig-item {{ background: rgba(255,255,255,0.02); border-radius: 8px; padding: 10px 14px; }}
    .ig-label {{ font-size: 0.72rem; font-weight: 800; color: {COLOR}; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }}
    .ig-val {{ font-size: 0.88rem; color: #cbd5e1; line-height: 1.6; }}
    .ig-analise {{ font-size: 0.9rem; color: #94a3b8; line-height: 1.8; }}
    .vocab-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 14px; margin-top: 16px; }}
    .vocab-card {{ background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-radius: 10px; padding: 14px 16px; }}
    .termo {{ font-size: 1.1rem; font-weight: 800; color: {COLOR}; font-family: 'Georgia', serif; }}
    .transl {{ font-size: 0.78rem; color: #64748b; font-style: italic; margin: 2px 0 6px; }}
    .def {{ font-size: 0.85rem; color: #94a3b8; line-height: 1.65; }}
    .nav-cap {{ display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.07); }}
    .nav-cap a {{ background: {TAG_BG}; border: 1px solid {TAG_BORDER}; color: {COLOR}; text-decoration: none; padding: 10px 20px; border-radius: 8px; font-size: 0.88rem; font-weight: 700; transition: all 0.2s; }}
    .nav-cap a:hover {{ background: {TAG_HOVER}; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 0.87rem; margin: 20px 0 32px; }}
    th {{ background: {TAG_BG}; color: {COLOR}; padding: 10px 14px; text-align: left; font-weight: 700; border-bottom: 1px solid {TAG_BORDER}; }}
    td {{ padding: 10px 14px; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; }}
    tr:hover td {{ background: rgba(255,255,255,0.02); }}
"""

IGREJAS = [
    {
        "nome": "Éfeso — A Igreja que Perdeu o Primeiro Amor",
        "ref": "Apocalipse 2:1-7",
        "cidade": "Éfeso era a maior cidade da Ásia Menor, capital da província romana da Ásia, com população estimada de 200.000-500.000 habitantes. Era um centro comercial, cultural e religioso — lar do templo de Ártemis, uma das sete maravilhas do mundo. A Igreja em Éfeso foi fundada por Paulo (At 19) e pastoreada por Timóteo e, segundo a tradição, pelo apóstolo João.",
        "elogio": "Obras, trabalho, perseverança; intolerância com os maus; testou os falsos apóstolos; odeiam as obras dos nicolaítas.",
        "critica": "Abandonou o primeiro amor — a devoção fervorosa e apaixonada a Cristo que caracterizava seus primeiros anos.",
        "chamado": "Lembra de onde caíste, arrepende-te e faze as primeiras obras.",
        "promessa": "Comer da árvore da vida no paraíso de Deus.",
        "analise": "Éfeso é a Igreja ortodoxa sem amor — correta em doutrina, diligente em obras, intolerante com o erro, mas fria em devoção. O \"primeiro amor\" (<em>tēn agapēn sou tēn prōtēn</em>) é a devoção apaixonada a Cristo que caracterizava os primeiros dias da fé — a alegria da salvação, o ardor da oração, o deleite na Palavra. Esta devoção pode ser perdida gradualmente, substituída pela eficiência religiosa. O remédio é triplo: lembrar (<em>mnēmoneue</em>), arrepender-se (<em>metanoēson</em>), e fazer (<em>poiēson</em>). A ameaça é grave: se não houver arrependimento, Cristo removerá o candelabro — a Igreja perderá sua função de ser luz no mundo. A promessa — comer da árvore da vida — ecoa o Éden (Gn 2:9) e antecipa a Nova Jerusalém (Ap 22:2)."
    },
    {
        "nome": "Esmirna — A Igreja Perseguida",
        "ref": "Apocalipse 2:8-11",
        "cidade": "Esmirna (atual Izmir, Turquia) era uma das cidades mais belas e prósperas da Ásia Menor, rival de Éfeso pelo título de 'primeira cidade da Ásia'. Era um centro do culto imperial — tinha um templo a Roma e ao Imperador desde 195 a.C. A Igreja em Esmirna sofria perseguição tanto das autoridades romanas quanto da comunidade judaica local.",
        "elogio": "Tribulação, pobreza (mas é rica!); suporta a blasfêmia dos que se dizem judeus mas são sinagoga de Satanás.",
        "critica": "Nenhuma crítica. Esmirna é uma das duas igrejas sem repreensão (junto com Filadélfia).",
        "chamado": "Não temas o que estás para sofrer; sê fiel até à morte.",
        "promessa": "A coroa da vida; não será ferida pela segunda morte.",
        "analise": "Esmirna é a Igreja pobre que é rica — pobre em bens materiais, mas rica em fé e em Cristo. O paradoxo é deliberado: aos olhos do mundo, a Igreja de Esmirna era miserável; aos olhos de Cristo, era rica. A \"sinagoga de Satanás\" (<em>synagōgē tou Satana</em>) refere-se à comunidade judaica que colaborava com as autoridades romanas na perseguição dos cristãos — não uma condenação do judaísmo como tal, mas de judeus específicos que se tornaram instrumentos de perseguição. A promessa da \"coroa da vida\" (<em>ton stephanon tēs zōēs</em>) usa a imagem da coroa do atleta vitorioso — Esmirna era famosa por seus jogos atléticos. A \"segunda morte\" (<em>ho deuteros thanatos</em>) é a morte eterna, o lago de fogo (Ap 20:14) — os que são fiéis até a morte física não serão feridos pela morte espiritual."
    },
    {
        "nome": "Pérgamo — A Igreja que Tolera o Erro",
        "ref": "Apocalipse 2:12-17",
        "cidade": "Pérgamo (atual Bergama, Turquia) era a capital oficial da província romana da Ásia e um grande centro cultural — tinha a segunda maior biblioteca do mundo antigo (200.000 volumes), rivalizando com Alexandria. Era também um centro do culto imperial e do culto de Zeus, Atena, Dionísio e Asclépio. O 'trono de Satanás' pode referir-se ao altar de Zeus, ao templo de Augusto, ou à presença do culto imperial.",
        "elogio": "Mantém o nome de Cristo e não negou a fé, mesmo onde Satanás tem o seu trono; Antipas, fiel mártir.",
        "critica": "Tolera os que seguem a doutrina de Balaão (comer coisas sacrificadas a ídolos e praticar fornicação) e os nicolaítas.",
        "chamado": "Arrepende-te.",
        "promessa": "Maná escondido e uma pedra branca com nome novo.",
        "analise": "Pérgamo é a Igreja que persevera na confissão mas tolera o erro doutrinário e moral. A doutrina de Balaão (<em>tēn didachēn Balaam</em>) refere-se ao conselho de Balaão a Balaque de seduzir Israel através da idolatria e imoralidade (Nm 25; 31:16). Os nicolaítas (mencionados também em Éfeso) provavelmente ensinavam que os cristãos podiam participar nos banquetes pagãos e nas práticas sexuais associadas ao culto — uma forma de acomodação ao mundo. A \"pedra branca com nome novo\" é enigmática — pode referir-se a um voto de absolvição (pedra branca era usada em votações de absolvição em tribunais romanos), a um bilhete de entrada para o banquete celestial, ou ao nome novo que Cristo dará a cada vencedor — uma identidade nova e secreta conhecida apenas por Deus e pelo crente."
    },
    {
        "nome": "Tiatira — A Igreja que Tolera a Jezabel",
        "ref": "Apocalipse 2:18-29",
        "cidade": "Tiatira (atual Akhisar, Turquia) era uma cidade comercial conhecida por suas guildas de artesãos e comerciantes — incluindo a guilda dos tintureiros de púrpura (Lídia, convertida por Paulo em Filipos, era de Tiatira — At 16:14). As guildas comerciais tinham práticas religiosas pagãs associadas, criando dilemas para os cristãos que precisavam participar para sobreviver economicamente.",
        "elogio": "Obras, amor, fé, serviço, perseverança; as últimas obras são maiores que as primeiras.",
        "critica": "Tolera a mulher Jezabel, que se diz profetisa e ensina e seduz os servos de Cristo a praticarem fornicação e comer coisas sacrificadas a ídolos.",
        "chamado": "Segurar o que têm até que Cristo venha.",
        "promessa": "Poder sobre as nações e a estrela da manhã.",
        "analise": "Tiatira é a Igreja com crescimento espiritual real ('as últimas obras são maiores que as primeiras') mas com tolerância de falsa profecia. 'Jezabel' é um nome simbólico — evoca a rainha fenícia que introduziu o culto de Baal em Israel (1 Rs 16:31-33). Esta profetisa em Tiatira ensinava que os cristãos podiam participar nas práticas das guildas pagãs — provavelmente argumentando que os ídolos não são nada (cf. 1 Co 8) e que o cristão maduro pode participar sem ser contaminado. Cristo deu-lhe tempo para se arrepender, mas ela não se arrependeu. O julgamento é severo: tribulação para ela e seus seguidores, morte para seus filhos. A promessa da 'estrela da manhã' (<em>ton astera ton prōinon</em>) é identificada em Ap 22:16 com o próprio Cristo — o vencedor recebe Cristo como sua recompensa suprema."
    },
    {
        "nome": "Sardes — A Igreja que Parece Viva mas está Morta",
        "ref": "Apocalipse 3:1-6",
        "cidade": "Sardes (atual Sart, Turquia) foi uma das cidades mais ricas e poderosas do mundo antigo — capital do reino da Lídia, onde o rei Creso acumulou lendária riqueza. A cidade tinha uma história de complacência: foi tomada de surpresa duas vezes (por Ciro em 547 a.C. e por Antíoco III em 214 a.C.) porque seus guardas adormeceram. Esta história de complacência é o pano de fundo da carta.",
        "elogio": "Tem alguns poucos nomes que não mancharam as suas vestes.",
        "critica": "Tem nome de que vive, mas está morta. As obras não são perfeitas diante de Deus.",
        "chamado": "Sê vigilante, confirma o que resta e que estava para morrer; lembra, guarda e arrepende-te.",
        "promessa": "Vestiduras brancas; nome não apagado do livro da vida; confissão diante do Pai.",
        "analise": "Sardes é a Igreja com reputação de vida mas realidade de morte — a Igreja que vive de sua glória passada. Não há elogio substancial, não há perseguição externa, não há falsa doutrina mencionada — apenas a morte espiritual que se instalou silenciosamente. A metáfora da vigilância ecoa a história da cidade: Sardes foi tomada porque seus guardas adormeceram. Cristo usa a mesma imagem: 'serei como um ladrão' — virei de surpresa se não houver vigilância. Os 'poucos nomes que não mancharam as suas vestes' (<em>oligous onomata en Sardesi hoi ouk emolunan ta himatia autōn</em>) são os remanescentes fiéis dentro de uma Igreja majoritariamente morta. A promessa das 'vestiduras brancas' (<em>en himatiois leukois</em>) contrasta com as vestes manchadas da maioria — pureza e vitória para os que perseveram."
    },
    {
        "nome": "Filadélfia — A Igreja da Porta Aberta",
        "ref": "Apocalipse 3:7-13",
        "cidade": "Filadélfia (atual Alaşehir, Turquia) era uma cidade jovem, fundada por Átalo II Filadelfo (189-138 a.C.) como porta de entrada para a Ásia Central. Era uma cidade missionária por natureza — sua posição geográfica a tornava um ponto de difusão da cultura grega para o interior. A cidade sofria frequentes terremotos — o grande terremoto de 17 d.C. destruiu a cidade e a região.",
        "elogio": "Tem pouca força, mas guardou a palavra de Cristo e não negou o seu nome.",
        "critica": "Nenhuma crítica. Filadélfia é a segunda Igreja sem repreensão (junto com Esmirna).",
        "chamado": "Guardar o que tem.",
        "promessa": "Porta aberta que ninguém pode fechar; proteção na hora da provação; coluna no templo de Deus; nome novo.",
        "analise": "Filadélfia é a Igreja fraca que é fiel — 'tens pouca força' (<em>mikran echeis dynamin</em>), mas guardou a Palavra e não negou o nome de Cristo. A 'porta aberta' (<em>thyran ēneōgmenēn</em>) é provavelmente uma oportunidade missionária — Cristo abre portas que ninguém pode fechar. A promessa de proteção na 'hora da provação' (<em>tēs hōras tou peirasmou</em>) é debatida: refere-se à proteção durante a tribulação ou ao arrebatamento antes dela? O texto diz 'guardar fora da hora da provação' (<em>tērēsō ek tēs hōras</em>) — a preposição <em>ek</em> pode indicar proteção dentro ou remoção antes. A promessa de se tornar 'coluna no templo de Deus' (<em>stylon en tō naō tou Theou mou</em>) é especialmente significativa para uma cidade que sofreu terremotos — as colunas eram o que permanecia de pé após os tremores."
    },
    {
        "nome": "Laodiceia — A Igreja Morna",
        "ref": "Apocalipse 3:14-22",
        "cidade": "Laodiceia (atual Denizli, Turquia) era uma das cidades mais ricas da Ásia Menor — um centro bancário, produtor de lã preta e de colírio para os olhos. Após o terremoto de 60 d.C., a cidade recusou a ajuda imperial e se reconstruiu com seus próprios recursos. A cidade não tinha fonte de água própria — recebia água quente de Hierápolis (via aqueduto) e água fria de Colossos; a água chegava morna.",
        "elogio": "Nenhum elogio.",
        "critica": "É morna — não fria nem quente. Diz 'sou rico, enriqueci e não tenho necessidade de coisa alguma', mas é miserável, pobre, cega e nua.",
        "chamado": "Comprar ouro refinado, vestiduras brancas e colírio; ser zelosa e arrepender-se.",
        "promessa": "Cristo jantará com quem abrir a porta; sentar com Cristo no seu trono.",
        "analise": "Laodiceia é a Igreja autossuficiente e morna — a mais severamente repreendida das sete. A metáfora da água morna é poderosa: a água quente de Hierápolis era medicinal; a água fria de Colossos era refrescante; a água morna que chegava a Laodiceia era inútil e provocava náusea. Uma Igreja morna não é nem curativa nem refrescante — é inútil e nauseante. O diagnóstico de Cristo inverte o autodiagnóstico da Igreja: ela se acha rica e sem necessidade, mas Cristo a vê como miserável, pobre, cega e nua. As três curas correspondem às três glórias de Laodiceia: ouro refinado (em vez da riqueza bancária), vestiduras brancas (em vez da lã preta famosa), colírio (em vez do colírio medicinal produzido localmente). A imagem de Cristo batendo à porta (v. 20) é frequentemente usada evangelisticamente, mas no contexto é uma mensagem à Igreja — Cristo está do lado de fora de sua própria Igreja, pedindo para entrar."
    }
]


def gerar_cap_igrejas_1():
    """Capítulo 2 — As 4 primeiras igrejas"""
    igrejas_html = ""
    for ig in IGREJAS[:4]:
        igrejas_html += f"""
    <div class="igreja-card">
      <div class="igreja-nome">{ig['nome']}</div>
      <div class="igreja-ref">{ig['ref']}</div>
      <p style="color:#94a3b8;font-size:0.9rem;line-height:1.8;margin-bottom:14px;">{ig['cidade']}</p>
      <div class="igreja-grid">
        <div class="ig-item"><div class="ig-label">✅ Elogio</div><div class="ig-val">{ig['elogio']}</div></div>
        <div class="ig-item"><div class="ig-label">⚠️ Crítica</div><div class="ig-val">{ig['critica']}</div></div>
        <div class="ig-item"><div class="ig-label">📣 Chamado</div><div class="ig-val">{ig['chamado']}</div></div>
        <div class="ig-item"><div class="ig-label">🏆 Promessa</div><div class="ig-val">{ig['promessa']}</div></div>
      </div>
      <div class="ig-analise">{ig['analise']}</div>
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Apocalipse 2 — As 7 Igrejas (Parte 1) | 365 de Graça & Adoração</title>
  <link rel="icon" href="/favicon.ico">
  <style>{CSS}</style>
</head>
<body>
  <div class="topbar"><div class="inner">
    <a href="/07-novo-testamento/apocalipse/index.html">← Apocalipse</a>
    <a href="/07-novo-testamento/index.html">Novo Testamento</a>
  </div></div>
  <div class="hero">
    <span class="tag">🔥 Apocalipse 2 · As 7 Igrejas</span>
    <h1>Apocalipse 2 — As 7 Igrejas (Parte 1)</h1>
    <div class="ref">Apocalipse 2:1-29 · João · c. 95-96 d.C. · Ilha de Patmos</div>
    <blockquote>Quem tem ouvidos, ouça o que o Espírito diz às igrejas. — Apocalipse 2:7,11,17,29</blockquote>
  </div>
  <div class="wrap">
    <div class="section-block">
      <h2>📜 Introdução às 7 Cartas</h2>
      <p>Os capítulos 2 e 3 do Apocalipse contêm sete cartas a sete igrejas da Ásia Menor — Éfeso, Esmirna, Pérgamo, Tiatira, Sardes, Filadélfia e Laodiceia. Estas não são apenas cartas históricas a comunidades do século I — são mensagens do Cristo ressuscitado e glorificado a sua Igreja em todas as épocas. Cada carta segue uma estrutura comum: (1) identificação do remetente — Cristo descrito com atributos da visão do capítulo 1; (2) "Eu sei" — Cristo conhece a situação de cada Igreja; (3) elogio (quando presente); (4) crítica (quando presente); (5) chamado ao arrependimento ou perseverança; (6) promessa ao vencedor; (7) "Quem tem ouvidos, ouça o que o Espírito diz às igrejas."</p>
      <p>As sete igrejas formam um circuito geográfico no sentido horário a partir de Éfeso — provavelmente a rota que um mensageiro seguiria ao entregar a carta. Elas representam a diversidade da Igreja: igrejas perseguidas e igrejas prósperas, igrejas ortodoxas e igrejas comprometidas, igrejas ardentes e igrejas mornas. Esta diversidade é intencional — as sete cartas cobrem o espectro completo das situações que a Igreja pode enfrentar.</p>
      <table>
        <tr><th>Igreja</th><th>Situação</th><th>Elogio Principal</th><th>Crítica Principal</th></tr>
        <tr><td>Éfeso</td><td>Ortodoxa mas fria</td><td>Perseverança, discernimento</td><td>Perdeu o primeiro amor</td></tr>
        <tr><td>Esmirna</td><td>Perseguida e pobre</td><td>Rica em fé</td><td>Nenhuma</td></tr>
        <tr><td>Pérgamo</td><td>Fiel mas tolerante</td><td>Mantém o nome de Cristo</td><td>Tolera heresias</td></tr>
        <tr><td>Tiatira</td><td>Crescendo mas comprometida</td><td>Obras crescentes</td><td>Tolera Jezabel</td></tr>
        <tr><td>Sardes</td><td>Reputação sem realidade</td><td>Alguns fiéis</td><td>Morta por dentro</td></tr>
        <tr><td>Filadélfia</td><td>Fraca mas fiel</td><td>Guardou a Palavra</td><td>Nenhuma</td></tr>
        <tr><td>Laodiceia</td><td>Rica e autossuficiente</td><td>Nenhum</td><td>Morna, cega, nua</td></tr>
      </table>
    </div>
    <div class="section-block">
      <h2>🕯️ As Quatro Primeiras Igrejas</h2>
      {igrejas_html}
    </div>
    <div class="section-block">
      <h2>📚 Vocabulário Essencial</h2>
      <div class="vocab-grid">
        <div class="vocab-card"><div class="termo">ἀγάπη πρώτη</div><div class="transl">agapē prōtē</div><div class="def">Primeiro amor. A devoção apaixonada e fervorosa a Cristo que caracteriza os primeiros dias da fé. Pode ser perdida gradualmente pela rotina religiosa.</div></div>
        <div class="vocab-card"><div class="termo">νικάω</div><div class="transl">nikaō</div><div class="def">Vencer, conquistar. O 'vencedor' (ho nikōn) é o crente que persevera na fé até o fim. Cada carta tem uma promessa específica ao vencedor.</div></div>
        <div class="vocab-card"><div class="termo">μετανοέω</div><div class="transl">metanoeō</div><div class="def">Arrepender-se. Mudança de mente e direção. Cinco das sete igrejas são chamadas ao arrependimento — o arrependimento é o caminho de volta à fidelidade.</div></div>
        <div class="vocab-card"><div class="termo">συναγωγή Σατανᾶ</div><div class="transl">synagōgē Satana</div><div class="def">Sinagoga de Satanás. Judeus que colaboravam com as autoridades romanas na perseguição dos cristãos em Esmirna e Filadélfia.</div></div>
      </div>
    </div>
    <div class="section-block">
      <h2>🏛️ Teologia das 7 Cartas</h2>
      <p>As sete cartas revelam a visão de Cristo sobre sua Igreja — uma visão que é simultaneamente realista e esperançosa. Cristo conhece a situação de cada Igreja em seus detalhes mais íntimos: "Eu sei as tuas obras" (<em>oida sou ta erga</em>) é a abertura de cada carta. Não há nada oculto de Cristo — ele vê a ortodoxia e a heresia, o amor e a frieza, a fidelidade e o compromisso.</p>
      <p>A estrutura das cartas revela a pedagogia de Cristo: ele elogia antes de criticar (exceto em Laodiceia, que não recebe elogio), e critica antes de ameaçar. O objetivo não é condenação, mas restauração — "sê zeloso e arrepende-te" (3:19). O chamado ao arrependimento é uma expressão de amor: "eu repreendo e disciplino a todos quantos amo" (3:19).</p>
    </div>
    <div class="nav-cap">
      <a href="/07-novo-testamento/apocalipse/capitulos/capitulo-01.html">← Apocalipse 1</a>
      <a href="/07-novo-testamento/apocalipse/index.html">📋 Índice</a>
      <a href="/07-novo-testamento/apocalipse/capitulos/capitulo-03.html">Apocalipse 3 →</a>
    </div>
  </div>
</body>
</html>"""


def gerar_cap_igrejas_2():
    """Capítulo 3 — As 3 últimas igrejas"""
    igrejas_html = ""
    for ig in IGREJAS[4:]:
        igrejas_html += f"""
    <div class="igreja-card">
      <div class="igreja-nome">{ig['nome']}</div>
      <div class="igreja-ref">{ig['ref']}</div>
      <p style="color:#94a3b8;font-size:0.9rem;line-height:1.8;margin-bottom:14px;">{ig['cidade']}</p>
      <div class="igreja-grid">
        <div class="ig-item"><div class="ig-label">✅ Elogio</div><div class="ig-val">{ig['elogio']}</div></div>
        <div class="ig-item"><div class="ig-label">⚠️ Crítica</div><div class="ig-val">{ig['critica']}</div></div>
        <div class="ig-item"><div class="ig-label">📣 Chamado</div><div class="ig-val">{ig['chamado']}</div></div>
        <div class="ig-item"><div class="ig-label">🏆 Promessa</div><div class="ig-val">{ig['promessa']}</div></div>
      </div>
      <div class="ig-analise">{ig['analise']}</div>
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Apocalipse 3 — As 7 Igrejas (Parte 2) | 365 de Graça & Adoração</title>
  <link rel="icon" href="/favicon.ico">
  <style>{CSS}</style>
</head>
<body>
  <div class="topbar"><div class="inner">
    <a href="/07-novo-testamento/apocalipse/index.html">← Apocalipse</a>
    <a href="/07-novo-testamento/index.html">Novo Testamento</a>
  </div></div>
  <div class="hero">
    <span class="tag">🔥 Apocalipse 3 · As 7 Igrejas</span>
    <h1>Apocalipse 3 — As 7 Igrejas (Parte 2)</h1>
    <div class="ref">Apocalipse 3:1-22 · João · c. 95-96 d.C. · Ilha de Patmos</div>
    <blockquote>Eis que estou à porta e bato; se alguém ouvir a minha voz e abrir a porta, entrarei em sua casa e cearei com ele, e ele comigo. — Apocalipse 3:20</blockquote>
  </div>
  <div class="wrap">
    <div class="section-block">
      <h2>🕯️ As Três Últimas Igrejas</h2>
      {igrejas_html}
    </div>
    <div class="section-block">
      <h2>📚 Vocabulário Essencial</h2>
      <div class="vocab-grid">
        <div class="vocab-card"><div class="termo">χλιαρός</div><div class="transl">chliaros</div><div class="def">Morno, tepido. A temperatura da água que chegava a Laodiceia — nem quente (medicinal) nem fria (refrescante), mas inútil e nauseante. Descreve a Igreja autossuficiente e sem ardor espiritual.</div></div>
        <div class="vocab-card"><div class="termo">θύρα</div><div class="transl": "thyra</div><div class="def">Porta. Em Ap 3:20, Cristo está à porta da Igreja batendo — imagem da Igreja que excluiu Cristo de sua própria vida. A porta é aberta por dentro, por escolha individual.</div></div>
        <div class="vocab-card"><div class="termo">στῦλος</div><div class="transl">stylos</div><div class="def">Coluna. A promessa a Filadélfia — ser coluna no templo de Deus. Para uma cidade que sofreu terremotos, as colunas representavam permanência e estabilidade.</div></div>
        <div class="vocab-card"><div class="termo">βιβλίον ζωῆς</div><div class="transl">biblion zōēs</div><div class="def">Livro da vida. O registro dos que pertencem a Deus. A promessa a Sardes — o nome do vencedor não será apagado do livro da vida.</div></div>
      </div>
    </div>
    <div class="section-block">
      <h2>🏛️ Aplicação Contemporânea das 7 Cartas</h2>
      <p>As sete igrejas são um espelho para a Igreja em todas as épocas. Cada comunidade cristã pode se reconhecer em uma ou mais destas igrejas: a ortodoxia sem amor de Éfeso, a fidelidade na pobreza de Esmirna, a tolerância do erro de Pérgamo e Tiatira, a reputação sem realidade de Sardes, a fidelidade fraca de Filadélfia, a autossuficiência morna de Laodiceia.</p>
      <p>A mensagem de Laodiceia é talvez a mais urgente para a Igreja contemporânea ocidental. A prosperidade material pode criar a ilusão de autossuficiência espiritual — "sou rico, enriqueci e não tenho necessidade de coisa alguma" (3:17). A Igreja que tem belos edifícios, programas eficientes, orçamentos equilibrados e boa reputação pode estar, aos olhos de Cristo, miserável, pobre, cega e nua. O remédio não é mais programas ou recursos — é abrir a porta para Cristo.</p>
    </div>
    <div class="nav-cap">
      <a href="/07-novo-testamento/apocalipse/capitulos/capitulo-02.html">← Apocalipse 2</a>
      <a href="/07-novo-testamento/apocalipse/index.html">📋 Índice</a>
      <a href="/07-novo-testamento/apocalipse/capitulos/capitulo-04.html">Apocalipse 4 →</a>
    </div>
  </div>
</body>
</html>"""


def gerar_cap_trono():
    """Capítulo 4-5 — O Trono Celestial e o Cordeiro"""
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Apocalipse 4-5 — O Trono e o Cordeiro | 365 de Graça & Adoração</title>
  <link rel="icon" href="/favicon.ico">
  <style>{CSS}</style>
</head>
<body>
  <div class="topbar"><div class="inner">
    <a href="/07-novo-testamento/apocalipse/index.html">← Apocalipse</a>
    <a href="/07-novo-testamento/index.html">Novo Testamento</a>
  </div></div>
  <div class="hero">
    <span class="tag">👑 Apocalipse 4-5 · O Trono Celestial</span>
    <h1>Apocalipse 4-5 — O Trono e o Cordeiro</h1>
    <div class="ref">Apocalipse 4:1–5:14 · João · c. 95-96 d.C. · Ilha de Patmos</div>
    <blockquote>Digno és, Senhor e Deus nosso, de receber a glória, e a honra, e o poder; porque tu criaste todas as coisas, e por tua vontade existem e foram criadas. — Apocalipse 4:11</blockquote>
  </div>
  <div class="wrap">
    <div class="section-block">
      <h2>📜 Contexto: A Visão do Trono</h2>
      <p>Após as sete cartas às igrejas (caps. 2-3), João é transportado ao céu (4:1 — "sobe aqui") e recebe a visão do trono celestial. Esta visão é o fundamento teológico de todo o restante do Apocalipse: antes de mostrar os julgamentos e as tribulações da terra, Deus mostra a João o que está acontecendo no céu. A mensagem é clara: Deus está no trono, e tudo o que acontece na terra está sob seu controle soberano.</p>
      <p>O capítulo 4 é uma visão do Pai no trono; o capítulo 5 é uma visão do Filho — o Cordeiro que foi morto e que está digno de abrir o livro selado. Juntos, os dois capítulos formam a mais sublime cena de adoração do NT — a liturgia celestial que é o modelo para toda adoração terrena.</p>
    </div>
    <div class="section-block">
      <h2>🔍 Análise dos Elementos da Visão</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">4:2-6 — O Trono e Aquele que Está Assentado</div>
        <div class="texto-v">"E eis que um trono estava posto no céu, e sobre o trono estava assentado alguém. E aquele que estava assentado era semelhante em aparência a uma pedra de jaspe e de sárdio; e havia um arco-íris em redor do trono, semelhante em aparência a uma esmeralda."</div>
        <div class="analise-v">João não descreve a aparência de Deus diretamente — ele usa comparações com pedras preciosas. O jaspe (<em>iaspis</em>) e o sárdio (<em>sardinos</em>) são pedras de brilho intenso — transparência e fogo. O arco-íris (<em>iris</em>) em redor do trono ecoa a visão de Ezequiel (Ez 1:28) — o arco-íris é o sinal da aliança de Deus com a criação (Gn 9:13-16). Mesmo no contexto de julgamento, a aliança de Deus permanece. Os "vinte e quatro anciãos" (<em>eikosi tessares presbyteroi</em>) são provavelmente representantes do povo de Deus — 12 tribos de Israel + 12 apóstolos = 24. Os "quatro seres viventes" (<em>tessara zōa</em>) são os querubins — os guardiões do trono divino (cf. Ez 1; Is 6). Seu cântico — "Santo, Santo, Santo, Senhor Deus Todo-Poderoso, que era, e que é, e que há de vir" — é o Trisagion, o hino mais antigo da adoração judaica e cristã.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">5:1-5 — O Livro Selado e o Leão/Cordeiro</div>
        <div class="texto-v">"E vi na mão direita do que estava assentado no trono um livro escrito por dentro e por fora, selado com sete selos. E vi um anjo forte, proclamando em voz alta: Quem é digno de abrir o livro e de desatar os seus selos? E ninguém no céu, nem na terra, nem debaixo da terra podia abrir o livro."</div>
        <div class="analise-v">O "livro selado com sete selos" (<em>biblion... katesfragismenon sfragisin hepta</em>) é o decreto do plano de Deus para a história — o rolo que contém os julgamentos e a consumação de todas as coisas. A pergunta do anjo — "quem é digno de abrir o livro?" — é a pergunta central do Apocalipse: quem tem autoridade para executar o plano de Deus para a história? A resposta é o paradoxo central do livro: "o Leão da tribo de Judá" (<em>ho leōn ho ek tēs phylēs Iouda</em>) — mas quando João olha, vê "um Cordeiro como se tivesse sido morto" (<em>arnion hōs esfagmenon</em>). O Leão é o Cordeiro — a vitória de Cristo é conquistada não pela força leonina, mas pelo sacrifício do Cordeiro. Esta é a teologia da cruz no Apocalipse: o poder de Deus se manifesta na fraqueza, a vitória através da morte.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">5:9-14 — O Novo Cântico e a Adoração Universal</div>
        <div class="texto-v">"E cantavam um novo cântico, dizendo: Digno és de tomar o livro e de abrir os seus selos; porque foste morto e com o teu sangue compraste para Deus homens de toda tribo, e língua, e povo, e nação... e todo o ser criado que está no céu, e sobre a terra, e debaixo da terra, e sobre o mar, e tudo o que neles há, ouvi eu dizer: Ao que está assentado no trono e ao Cordeiro, seja a bênção, e a honra, e a glória, e o domínio pelos séculos dos séculos."</div>
        <div class="analise-v">O "novo cântico" (<em>ōdēn kainēn</em>) é o hino da redenção — cantado porque algo novo aconteceu: o Cordeiro foi morto e comprou para Deus pessoas de toda nação. A universalidade da redenção — "toda tribo, língua, povo e nação" (<em>ek pasēs phylēs kai glōssēs kai laou kai ethnous</em>) — é um dos temas centrais do Apocalipse. A adoração culmina na adoração de toda a criação: "todo o ser criado" (<em>pan ktisma</em>) — o cosmos inteiro se une na adoração ao Pai e ao Cordeiro. Esta visão da adoração universal é o destino final da criação — não a destruição, mas a restauração e o louvor.</div>
      </div>
    </div>
    <div class="section-block">
      <h2>📚 Vocabulário Essencial</h2>
      <div class="vocab-grid">
        <div class="vocab-card"><div class="termo">ἀρνίον</div><div class="transl">arnion</div><div class="def">Cordeiro (diminutivo). O título mais frequente para Cristo no Apocalipse (29 vezes). O Cordeiro que foi morto é digno de receber poder, riqueza, sabedoria, força, honra, glória e louvor.</div></div>
        <div class="vocab-card"><div class="termo">ἄξιος</div><div class="transl">axios</div><div class="def">Digno. O critério para abrir o livro selado. Cristo é digno porque foi morto e comprou para Deus pessoas de toda nação. A dignidade de Cristo é fundamentada em seu sacrifício.</div></div>
        <div class="vocab-card"><div class="termo">ᾠδὴ καινή</div><div class="transl">ōdē kainē</div><div class="def">Novo cântico. O hino da redenção cantado pelos seres celestiais ao Cordeiro. 'Novo' porque a redenção é um ato novo e definitivo de Deus na história.</div></div>
        <div class="vocab-card"><div class="termo">τετράζωα</div><div class="transl">tessara zōa</div><div class="def">Quatro seres viventes. Os querubins — guardiões do trono divino. Representam a criação em sua plenitude: leão (animais selvagens), boi (animais domésticos), homem (humanidade), águia (aves).</div></div>
      </div>
    </div>
    <div class="section-block">
      <h2>✨ Aplicação Contemporânea</h2>
      <p>A visão do trono em Apocalipse 4-5 é o fundamento da adoração cristã. Antes de qualquer instrução sobre como adorar, Deus mostra a João o que a adoração parece no céu — e o que a adoração celestial revela é que Deus está no trono. Esta visão é o antídoto para o desespero: quando a história parece caótica e o mal parece vencer, a visão do trono lembra que Deus está no controle.</p>
      <p>O paradoxo do Leão/Cordeiro em Ap 5:5-6 é o coração da teologia cristã. O poder de Deus não se manifesta como poder humano — força, dominação, conquista. Manifesta-se como sacrifício, serviço, entrega. O Cordeiro que foi morto é o mais poderoso ser do universo. Esta inversão de valores é o Evangelho em sua forma mais concentrada.</p>
    </div>
    <div class="nav-cap">
      <a href="/07-novo-testamento/apocalipse/capitulos/capitulo-03.html">← Apocalipse 3</a>
      <a href="/07-novo-testamento/apocalipse/index.html">📋 Índice</a>
      <a href="/07-novo-testamento/apocalipse/capitulos/capitulo-05.html">Apocalipse 5 →</a>
    </div>
  </div>
</body>
</html>"""


def gerar_cap_nova_jerusalem():
    """Capítulo 21 — A Nova Jerusalém"""
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Apocalipse 21 — A Nova Jerusalém | 365 de Graça & Adoração</title>
  <link rel="icon" href="/favicon.ico">
  <style>{CSS}</style>
</head>
<body>
  <div class="topbar"><div class="inner">
    <a href="/07-novo-testamento/apocalipse/index.html">← Apocalipse</a>
    <a href="/07-novo-testamento/index.html">Novo Testamento</a>
  </div></div>
  <div class="hero">
    <span class="tag">🌟 Apocalipse 21 · A Nova Criação</span>
    <h1>Apocalipse 21 — A Nova Jerusalém</h1>
    <div class="ref">Apocalipse 21:1-27 · João · c. 95-96 d.C. · Ilha de Patmos</div>
    <blockquote>E ouvi uma grande voz do trono, dizendo: Eis o tabernáculo de Deus com os homens; pois com eles habitará, e eles serão o seu povo, e o próprio Deus estará com eles. — Apocalipse 21:3</blockquote>
  </div>
  <div class="wrap">
    <div class="section-block">
      <h2>📜 Contexto: O Clímax da Revelação</h2>
      <p>Apocalipse 21 é o clímax de toda a narrativa bíblica — a consumação de tudo o que Deus prometeu desde o Éden. Após o julgamento do grande trono branco (cap. 20), João vê "um novo céu e uma nova terra" (<em>ouranon kainon kai gēn kainēn</em>) — a criação renovada e restaurada. A Nova Jerusalém descendo do céu é a imagem da habitação de Deus com a humanidade — o cumprimento definitivo do propósito da criação.</p>
      <p>O capítulo 21 inverte as maldições do Éden: não mais morte (v. 4), não mais dor (v. 4), não mais maldição (22:3), não mais noite (v. 25), não mais mar (v. 1 — o mar era símbolo de caos e morte no mundo antigo). A Nova Jerusalém não é um lugar onde os salvos vão — é um lugar que desce do céu para a terra. A escatologia bíblica não é a fuga da terra para o céu, mas a renovação da terra pelo céu.</p>
    </div>
    <div class="section-block">
      <h2>🔍 Análise Versículo por Versículo</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">21:1-4 — Todas as Coisas Novas</div>
        <div class="texto-v">"E vi um novo céu e uma nova terra; porque o primeiro céu e a primeira terra passaram, e o mar já não existe. E eu, João, vi a santa cidade, a nova Jerusalém, descer do céu da parte de Deus, adornada como uma noiva ataviada para o seu marido."</div>
        <div class="analise-v">O "novo céu e nova terra" (<em>ouranon kainon kai gēn kainēn</em>) ecoa Isaías 65:17 e 66:22. O adjetivo "novo" (<em>kainos</em>) não significa "completamente diferente" (isso seria <em>neos</em>), mas "renovado, restaurado, de qualidade superior". A nova criação não é a destruição da criação original e a criação de algo completamente diferente — é a transformação e renovação da criação original. A Nova Jerusalém "descendo do céu" (<em>katabainousa ek tou ouranou</em>) é a imagem da habitação de Deus com a humanidade — não os salvos subindo ao céu, mas o céu descendo à terra. A voz do trono (v. 3) anuncia o cumprimento de toda a história da redenção: "Eis o tabernáculo de Deus com os homens" (<em>hē skēnē tou Theou meta tōn anthrōpōn</em>) — o tabernáculo, o templo, a encarnação de Cristo, a habitação do Espírito nos crentes — tudo isso era antecipação desta habitação definitiva e perfeita.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">21:5-8 — "Eis que Faço Novas Todas as Coisas"</div>
        <div class="texto-v">"E o que estava assentado no trono disse: Eis que faço novas todas as coisas. E disse-me: Escreve, porque estas palavras são fiéis e verdadeiras... Eu sou o Alfa e o Ômega, o princípio e o fim. A quem tiver sede darei de graça da fonte da água da vida."</div>
        <div class="analise-v">"Eis que faço novas todas as coisas" (<em>idou kaina poiō panta</em>) — esta é a única vez no Apocalipse que Deus fala diretamente em primeira pessoa. A renovação de todas as coisas é a declaração mais abrangente da escatologia bíblica — não apenas a salvação das almas, mas a renovação do cosmos inteiro. "Estas palavras são fiéis e verdadeiras" (<em>houtoi hoi logoi pistoi kai alēthinoi eisin</em>) — a confiabilidade da promessa é garantida pelo caráter de Deus. "Alfa e Ômega, princípio e fim" — Deus que iniciou a criação a completará. A promessa da "fonte da água da vida" (<em>tēs pēgēs tou hydatos tēs zōēs</em>) ecoa a promessa de Jesus à samaritana (Jo 4:14) e ao último dia da festa dos tabernáculos (Jo 7:37-38) — a sede espiritual da humanidade será satisfeita definitivamente na nova criação.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">21:9-21 — As Dimensões da Nova Jerusalém</div>
        <div class="texto-v">"E a cidade está posta em quadrado, e o seu comprimento é tanto como a sua largura; e ele mediu a cidade com a cana, doze mil estádios; o comprimento, a largura e a altura são iguais. E mediu o seu muro, cento e quarenta e quatro côvados."</div>
        <div class="analise-v">As dimensões da Nova Jerusalém são simbólicas, não literais. 12.000 estádios (aproximadamente 2.400 km) em cada dimensão — comprimento, largura e altura iguais — formam um cubo perfeito. O único outro cubo na Bíblia é o Santo dos Santos do Templo de Salomão (1 Rs 6:20) — 20 côvados em cada dimensão. A Nova Jerusalém é o Santo dos Santos cósmico — o lugar da presença de Deus expandido para abranger toda a nova criação. O número 12 permeia toda a descrição: 12 portas com os nomes das 12 tribos de Israel, 12 fundamentos com os nomes dos 12 apóstolos, 12.000 estádios, 144 côvados (12 × 12). O 12 é o número do povo de Deus — a Nova Jerusalém é a habitação definitiva do povo de Deus em sua plenitude.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">21:22-27 — Sem Templo, Sem Sol, Sem Noite</div>
        <div class="texto-v">"E não vi nenhum templo nela, porque o Senhor Deus Todo-Poderoso é o seu templo, e o Cordeiro. E a cidade não necessita do sol nem da lua para lhe darem claridade; porque a glória de Deus a iluminou, e o Cordeiro é a sua lâmpada."</div>
        <div class="analise-v">A ausência de templo na Nova Jerusalém é surpreendente — o templo era o coração da religião bíblica. Mas o templo era o lugar onde Deus habitava de forma especial; na Nova Jerusalém, Deus habita em toda parte — "o Senhor Deus Todo-Poderoso é o seu templo, e o Cordeiro" (<em>ho gar Kyrios ho Theos ho pantokratōr naos autēs estin kai to arnion</em>). O templo era o meio; a habitação direta de Deus é o fim. A ausência de sol e lua não é cosmológica — é teológica: a glória de Deus é a fonte de toda luz. "As nações andarão na sua luz" (<em>ta ethnē peripatēsousin dia tou phōtos autēs</em>) — a Nova Jerusalém não é exclusiva para Israel ou para os cristãos; as nações trazem sua glória para ela (v. 24,26). A nova criação é a consumação da promessa abraâmica de que todas as nações seriam abençoadas.</div>
      </div>
    </div>
    <div class="section-block">
      <h2>📚 Vocabulário Essencial</h2>
      <div class="vocab-grid">
        <div class="vocab-card"><div class="termo">καινός</div><div class="transl">kainos</div><div class="def">Novo (de qualidade superior, renovado). O novo céu e nova terra não são uma criação completamente diferente, mas a criação original renovada e transformada. A escatologia bíblica é renovação, não substituição.</div></div>
        <div class="vocab-card"><div class="termo">σκηνή</div><div class="transl">skēnē</div><div class="def">Tabernáculo, tenda. 'O tabernáculo de Deus com os homens' — a habitação definitiva de Deus com a humanidade. Ecoa o tabernáculo do deserto, o templo de Salomão, e a encarnação de Cristo (Jo 1:14 — 'habitou entre nós', lit. 'tabernaculou').</div></div>
        <div class="vocab-card"><div class="termo">ναός</div><div class="transl">naos</div><div class="def">Templo (o santuário interior). Na Nova Jerusalém, não há templo porque Deus e o Cordeiro são o templo. O meio (templo) é substituído pelo fim (habitação direta de Deus).</div></div>
        <div class="vocab-card"><div class="termo">δόξα</div><div class="transl">doxa</div><div class="def">Glória. A glória de Deus ilumina a Nova Jerusalém — não há necessidade de sol ou lua. A glória divina, que habitou no tabernáculo e no templo, agora preenche toda a nova criação.</div></div>
      </div>
    </div>
    <div class="section-block">
      <h2>🏛️ Teologia da Nova Criação</h2>
      <p>Apocalipse 21 apresenta a escatologia bíblica em sua forma mais completa. A esperança cristã não é a fuga da terra para um céu imaterial — é a renovação da terra pela glória de Deus. A Nova Jerusalém descendo do céu é a imagem da criação restaurada, da humanidade redimida, e da habitação definitiva de Deus com seu povo.</p>
      <p>A estrutura da Nova Jerusalém revela a continuidade entre a criação original e a nova criação: as 12 tribos de Israel e os 12 apóstolos são os fundamentos da cidade — a história da redenção não é apagada, mas consumada. Os que foram redimidos "de toda tribo, língua, povo e nação" (5:9) habitam juntos na cidade — a diversidade humana não é eliminada, mas glorificada na nova criação.</p>
    </div>
    <div class="section-block">
      <h2>✨ Aplicação Contemporânea</h2>
      <p>A visão da Nova Jerusalém é o fundamento da esperança cristã e o critério para a ação presente. Porque Deus promete renovar toda a criação, o cuidado com a criação presente tem valor escatológico. Porque a Nova Jerusalém acolhe pessoas de todas as nações, a missão transcultural é urgente. Porque "não haverá mais morte, nem pranto, nem clamor, nem dor" (21:4), o trabalho de cura, justiça e compaixão no presente é antecipação da nova criação.</p>
      <p>A promessa "eis que faço novas todas as coisas" (21:5) é o fundamento da esperança cristã no sofrimento. Quando a dor parece permanente, quando a injustiça parece invencível, quando a morte parece ter a última palavra — esta promessa afirma que Deus está fazendo novas todas as coisas. A nova criação não é um sonho distante — é a realidade futura que já começa a irromper no presente através do Espírito Santo e da comunidade dos redimidos.</p>
    </div>
    <div class="nav-cap">
      <a href="/07-novo-testamento/apocalipse/capitulos/capitulo-20.html">← Apocalipse 20</a>
      <a href="/07-novo-testamento/apocalipse/index.html">📋 Índice</a>
      <a href="/07-novo-testamento/apocalipse/capitulos/capitulo-22.html">Apocalipse 22 →</a>
    </div>
  </div>
</body>
</html>"""


def main():
    os.makedirs(BASE, exist_ok=True)

    arquivos = [
        ("capitulo-02.html", gerar_cap_igrejas_1()),
        ("capitulo-03.html", gerar_cap_igrejas_2()),
        ("capitulo-04.html", gerar_cap_trono()),
        ("capitulo-21.html", gerar_cap_nova_jerusalem()),
    ]

    for nome, html in arquivos:
        path = os.path.join(BASE, nome)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ apocalipse/{nome}")

    print("\n🎉 Apocalipse aprofundado gerado!")


if __name__ == "__main__":
    main()
