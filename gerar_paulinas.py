#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera capítulos aprofundados de todas as Epístolas Paulinas:
Romanos (16), 1Cor (16), 2Cor (13), Gálatas (6), Efésios (6),
Filipenses (4), Colossenses (4), 1Ts (5), 2Ts (3),
1Tm (6), 2Tm (4), Tito (3), Filemom (1) = 87 capítulos
"""

import os

BASE = "/home/ubuntu/365-de-graca-e-adoracao/08-novo-testamento"

CSS = """
<style>
.section-block { background: var(--panel2,#1a1a2e); border-radius:12px; padding:1.5rem; margin:1.5rem 0; }
.section-block h2 { color: var(--accent,#0ea5e9); margin-bottom:1rem; font-size:1.2rem; }
.versiculo-bloco { border-left: 3px solid var(--accent,#0ea5e9); padding: 1rem 1.2rem; margin:1rem 0; background: rgba(255,255,255,0.03); border-radius:0 8px 8px 0; }
.ref-v { font-size:0.8rem; color: var(--accent,#0ea5e9); font-weight:700; margin-bottom:0.4rem; text-transform:uppercase; letter-spacing:0.05em; }
.texto-v { font-style:italic; color:#e2e8f0; margin-bottom:0.6rem; line-height:1.7; }
.analise-v { color:#94a3b8; font-size:0.92rem; line-height:1.7; }
.chapter-hero { text-align:center; padding:3rem 1rem 2rem; background:linear-gradient(135deg,rgba(14,165,233,0.15),rgba(99,102,241,0.1)); }
.chapter-number { font-size:0.85rem; color:var(--accent,#0ea5e9); font-weight:700; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.5rem; }
.chapter-subtitle { color:#94a3b8; font-style:italic; margin-top:0.5rem; }
.chapter-ref { color:var(--accent,#0ea5e9); font-size:0.85rem; }
.chapter-nav { display:flex; justify-content:space-between; padding:1.5rem; gap:1rem; flex-wrap:wrap; }
.chapter-nav a { color:var(--accent,#0ea5e9); text-decoration:none; padding:0.5rem 1rem; border:1px solid var(--accent,#0ea5e9); border-radius:6px; }
.breadcrumb { padding:0.75rem 1.5rem; font-size:0.85rem; color:#64748b; }
.breadcrumb a { color:var(--accent,#0ea5e9); text-decoration:none; }
.wrap { max-width:860px; margin:0 auto; padding:0 1.5rem 3rem; }
</style>"""

def page(livro, num, total, titulo, vk, rk, body, livro_dir, depth="../../.."):
    prev = f"capitulo-{num-1:02d}.html" if num > 1 else "../index.html"
    nxt = f"capitulo-{num+1:02d}.html" if num < total else "../index.html"
    pl = f"← {livro} {num-1}" if num > 1 else "← Índice"
    nl = f"{livro} {num+1} →" if num < total else "Índice →"
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{livro} {num} — {titulo} | 365 de Graça &amp; Adoração</title>
  <meta name="description" content="Estudo aprofundado de {livro} capítulo {num}: {titulo}. Análise exegética versículo por versículo com vocabulário grego, contexto histórico e teologia.">
  <meta property="og:title" content="{livro} {num} — {titulo} | 365 de Graça &amp; Adoração">
  <meta property="og:type" content="article">
  <link rel="stylesheet" href="{depth}/assets/css/style.css">
  <link rel="stylesheet" href="{depth}/assets/css/bloco.css">
  {CSS}
</head>
<body class="bloco-08">
  <header class="topbar">
    <a class="brand" href="/">365 de Graça &amp; Adoração</a>
    <nav>
      <a href="/">Início</a>
      <a href="/08-novo-testamento/">Novo Testamento</a>
      <a href="/busca/">Buscar</a>
    </nav>
  </header>
  <div class="breadcrumb">
    <a href="/">Início</a> › <a href="/08-novo-testamento/">NT</a> › <a href="../">{livro}</a> › Capítulo {num}
  </div>
  <div class="chapter-hero">
    <div class="chapter-number">{livro} — Capítulo {num}</div>
    <h1>{titulo}</h1>
    <p class="chapter-subtitle">"{vk}"</p>
    <p class="chapter-ref">— {rk}</p>
  </div>
  <div class="wrap">
{body}
  </div>
  <nav class="chapter-nav">
    <a href="{prev}">{pl}</a>
    <a href="../index.html">Índice de {livro}</a>
    <a href="{nxt}">{nl}</a>
  </nav>
  <footer class="site-footer">
    <p>365 de Graça &amp; Adoração • Da Criação ao Apocalipse • © 2026</p>
  </footer>
</body>
</html>"""

def bloco(titulo, items):
    html = f'    <div class="section-block">\n      <h2>{titulo}</h2>\n'
    for ref, txt, analise in items:
        html += f"""      <div class="versiculo-bloco">
        <div class="ref-v">{ref}</div>
        <div class="texto-v">"{txt}"</div>
        <div class="analise-v">{analise}</div>
      </div>\n"""
    return html + "    </div>\n"

def intro(txt):
    return f'    <div class="section-block"><p>{txt}</p></div>\n'

def salvar(livro_dir, num, html):
    path = os.path.join(BASE, livro_dir, "capitulos", f"capitulo-{num:02d}.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

# ─────────────────────────────────────────────
# ROMANOS
# ─────────────────────────────────────────────
romanos_caps = {
    1: ("O Evangelho e a Depravação Humana", "Porque não me envergonho do evangelho de Cristo, pois é o poder de Deus para a salvação.", "Rm 1:16",
        intro("Romanos é a carta mais sistemática de Paulo, escrita ~57 d.C. em Corinto. O cap. 1 apresenta o tema central: o Evangelho como poder de Deus para a salvação, e a necessidade universal de salvação revelada pela ira de Deus sobre a depravação humana.") +
        bloco("⚡ O Tema Central: O Evangelho (1:16-17)", [
            ("Rm 1:16-17", "Porque não me envergonho do evangelho de Cristo, pois é o poder de Deus para a salvação de todo aquele que crê; primeiro do judeu, e também do grego. Porque nele a justiça de Deus se revela de fé em fé.",
             "A <em>propositio</em> de toda a carta. <em>Dynamis theou</em> — poder de Deus: o Evangelho não é apenas informação, é poder transformador. <em>Dikaiosyne theou</em> — justiça de Deus: não a justiça que Deus exige de nós, mas a que ele provê para nós em Cristo. <em>Ek pisteos eis pistin</em> — de fé em fé: a salvação é inteiramente pela fé. A citação de Habacuque 2:4 desencadeou a Reforma Protestante — Lutero entendeu que a justiça de Deus é um dom recebido pela fé, não uma exigência a ser cumprida.")
        ]) +
        bloco("🔥 A Ira de Deus e a Depravação Humana (1:18-32)", [
            ("Rm 1:18-20", "Porque do céu se manifesta a ira de Deus sobre toda a impiedade e injustiça dos homens que detêm a verdade em injustiça... as suas perfeições invisíveis... se entendem e claramente se veem nas coisas que foram criadas; de modo que eles são inescusáveis.",
             "A <em>orge theou</em> não é reação emocional — é resposta santa à violação da ordem moral. A revelação natural: todo ser humano tem acesso ao conhecimento de Deus pela criação. <em>Anapologetous</em> — inescusáveis: o problema humano não é falta de informação, é supressão da informação. <em>Katechonton</em> — suprimir, abafar a verdade."),
            ("Rm 1:24-28", "Por isso Deus os entregou... Deus os entregou... Deus os entregou...",
             "A repetição tripla de <em>paredoken autous ho theos</em> é o coração desta seção. A ira de Deus opera no presente como abandono judicial. Deus não força ao pecado — ele remove a restrição. As três entregas: (1) às impurezas; (2) às paixões infames; (3) à mente reprovada — catálogo de 21 vícios sociais.")
        ])),
    2: ("O Julgamento Justo de Deus", "Ou desprezas as riquezas da sua benignidade, tolerância e longanimidade?", "Rm 2:4",
        intro("Romanos 2 confronta o moralista e o judeu religioso. Após condenar os gentios, Paulo vira a mesa: ninguém escapa do julgamento, porque o critério não é o conhecimento da lei, mas a obediência a ela.") +
        bloco("⚖️ O Julgamento Imparcial (2:1-16)", [
            ("Rm 2:1-4", "Portanto, és inescusável, ó homem, quem quer que sejas tu que julgas; pois no que julgas a outro, a ti mesmo te condenas.",
             "A <em>diatribe</em> retórica: Paulo se dirige ao moralista que concordou com a condenação do cap. 1. A bondade de Deus (<em>chrestotes</em>), tolerância (<em>anoche</em>) e longanimidade (<em>makrothymia</em>) são convites ao arrependimento, não aprovação do pecado."),
            ("Rm 2:14-16", "Porque quando os gentios, que não têm lei, fazem por natureza as coisas que são da lei, esses, não tendo lei, são lei para si mesmos.",
             "A lei natural e a consciência (<em>syneidesis</em>): os gentios têm a obra da lei escrita no coração. A consciência não salva — ela condena, porque ninguém a obedece perfeitamente. Base bíblica para a lei natural e para a responsabilidade moral universal.")
        ]) +
        bloco("✡️ O Judeu e a Hipocrisia Religiosa (2:17-29)", [
            ("Rm 2:28-29", "Porque não é judeu o que o é exteriormente... Mas é judeu o que o é interiormente, e circuncisão é a do coração, em espírito, não em letra.",
             "A verdadeira circuncisão é a do coração (<em>peritome kardias</em>), prometida em Dt 30:6 e Jr 4:4. Paulo não aboliu a identidade judaica — redefiniu-a em termos de transformação interna pelo Espírito.")
        ])),
    3: ("Todos Culpados — Justificação pela Fé", "Sendo justificados gratuitamente pela sua graça, pela redenção que há em Cristo Jesus.", "Rm 3:24",
        intro("Romanos 3 é o coração teológico da carta. Os versículos 21-26 apresentam a justificação pela fé na obra expiatória de Cristo. Após provar a culpa universal, Paulo apresenta a solução divina.") +
        bloco("🌍 Todos Sob o Pecado (3:9-20)", [
            ("Rm 3:10-12", "Como está escrito: Não há um justo, nem um sequer; não há nenhum que entenda; não há nenhum que busque a Deus.",
             "Cadeia de citações do AT (Sl 14; 53; 5; 140; 10; Is 59; Sl 36) provando que a condenação universal é testemunho das próprias Escrituras judaicas. Absoluto e universal. 'Não há nenhum que busque a Deus' — a busca religiosa humana não é busca por Deus, é busca por um deus que sirva aos nossos propósitos."),
            ("Rm 3:19-20", "Porque pelas obras da lei nenhuma carne será justificada diante dele; em razão de que pela lei vem o conhecimento do pecado.",
             "A lei fecha toda a boca (<em>phtariston pan stoma</em>). Sua função não é justificar — é condenar e revelar o pecado em toda a sua gravidade.")
        ]) +
        bloco("⭐ O Coração do Evangelho: Justificação pela Fé (3:21-26)", [
            ("Rm 3:21-24", "Mas agora, independentemente da lei, a justiça de Deus se manifestou... sendo justificados gratuitamente pela sua graça, pela redenção que há em Cristo Jesus.",
             "O 'mas agora' (<em>nyni de</em>) é a virada mais dramática da teologia bíblica. Quatro palavras-chave: (1) <em>dikaiosyne theou</em> — justiça provida por Deus; (2) <em>dia pisteos</em> — pela fé; (3) <em>dorean</em> — gratuitamente; (4) <em>apolytrosis</em> — redenção."),
            ("Rm 3:25-26", "Ao qual Deus propôs como propiciação pela fé no seu sangue... para ser ele justo e justificador daquele que tem fé em Jesus.",
             "<em>Hilasterion</em> — propiciação: Jesus é o novo Propiciatório, onde a ira de Deus é satisfeita. A cruz resolve o problema teológico: como pode Deus ser justo (punindo o pecado) e justificador (absolvendo o pecador)? Na cruz, Deus puniu o pecado em Cristo.")
        ])),
    4: ("Abraão: O Pai da Fé", "Abraão creu em Deus, e isso lhe foi imputado como justiça.", "Rm 4:3",
        intro("Romanos 4 usa Abraão como prova histórica da justificação pela fé. Paulo demonstra que Abraão foi justificado antes da circuncisão e antes da lei — portanto pela fé, não pelas obras.") +
        bloco("🌟 Abraão Justificado pela Fé (4:1-12)", [
            ("Rm 4:2-5", "Porque se Abraão foi justificado pelas obras, tem de que se gloriar, mas não diante de Deus. Pois que diz a Escritura? E creu Abraão em Deus, e isso lhe foi imputado como justiça.",
             "<em>Logizomai</em> — imputar, creditar (termo contábil): a justiça de Cristo é creditada na conta do crente. Abraão foi justificado (Gn 15:6) antes da circuncisão (Gn 17 — intervalo de ~14 anos) e antes da lei (430 anos antes — Gl 3:17).")
        ]) +
        bloco("⭐ A Promessa pela Fé (4:13-25)", [
            ("Rm 4:20-22", "E não duvidou da promessa de Deus por incredulidade; antes foi fortalecido na fé, dando glória a Deus, e estando plenamente certo de que o que Deus tinha prometido era também poderoso para o cumprir. E por isso também isso lhe foi imputado como justiça.",
             "A fé de Abraão não foi fé cega — foi fé informada pela promessa. Ele considerou seu corpo 'mortificado' (~100 anos) e o ventre de Sara 'morto' — e ainda assim creu. Esta fé 'deu glória a Deus' (<em>edoxasen ton theon</em>). A mesma imputação de justiça se aplica a nós que cremos na ressurreição de Cristo.")
        ])),
    5: ("Paz com Deus e o Dom da Graça", "Justificados, pois, pela fé, temos paz com Deus por nosso Senhor Jesus Cristo.", "Rm 5:1",
        intro("Romanos 5 apresenta os frutos da justificação (paz, esperança, amor) e o paralelo teológico fundamental entre Adão e Cristo como representantes da humanidade.") +
        bloco("☮️ Os Frutos da Justificação (5:1-11)", [
            ("Rm 5:1-5", "Justificados, pois, pela fé, temos paz com Deus... E não somente isso, mas também nos gloriamos nas tribulações; sabendo que a tribulação produz a paciência, e a paciência a experiência, e a experiência a esperança.",
             "Cinco frutos da justificação: (1) paz com Deus; (2) acesso à graça; (3) esperança da glória; (4) glória nas tribulações; (5) amor de Deus derramado pelo Espírito. A cadeia tribulação → paciência (<em>hypomone</em>) → experiência (<em>dokime</em>) → esperança é a pedagogia divina do sofrimento."),
            ("Rm 5:8", "Mas Deus prova o seu amor para conosco, em que Cristo morreu por nós, sendo nós ainda pecadores.",
             "A prova do amor de Deus é histórica e específica: Cristo morreu pelos ímpios, pelos pecadores, pelos inimigos. A lógica <em>a fortiori</em>: se Deus amou tanto quando éramos inimigos, quanto mais nos salvará agora que somos filhos?")
        ]) +
        bloco("👥 Adão e Cristo: Dois Representantes (5:12-21)", [
            ("Rm 5:15-19", "Porque, assim como pela desobediência de um homem muitos foram constituídos pecadores, assim também pela obediência de um muitos serão constituídos justos.",
             "O paralelo Adão-Cristo: o pecado de Adão imputado a todos; a justiça de Cristo imputada a todos que creem. Mas há assimetria: a graça é muito mais abundante (<em>perisseuein</em>). A obediência ativa de Cristo (vida perfeita) e passiva (morte substitutiva) são ambas necessárias para nossa justificação.")
        ])),
    6: ("Mortos para o Pecado, Vivos em Cristo", "Assim também vós considerai-vos mortos para o pecado, mas vivos para Deus em Cristo Jesus.", "Rm 6:11",
        intro("Romanos 6 responde à objeção antinomiana com a doutrina da morte e ressurreição com Cristo no batismo, e a transferência da escravidão do pecado para a escravidão da justiça.") +
        bloco("💀 Mortos com Cristo no Batismo (6:1-14)", [
            ("Rm 6:1-4", "Que diremos, pois? Permaneceremos no pecado para que a graça abunde? De modo nenhum! Nós, que estamos mortos para o pecado, como viveremos ainda nele? Fomos, pois, sepultados com ele pelo batismo na morte.",
             "A resposta à objeção antinomiana é ontológica: o crente está morto para o pecado. O batismo simboliza e sela a união com Cristo na morte e ressurreição. A 'novidade de vida' (<em>kainoteti zoes</em>) não é possibilidade — é realidade que deve ser vivida."),
            ("Rm 6:11", "Assim também vós considerai-vos mortos para o pecado, mas vivos para Deus em Cristo Jesus.",
             "<em>Logizesthe</em> — considerai, contai como realidade: Paulo não diz 'tornai-vos mortos' mas 'considerai-vos mortos' — a morte ao pecado já é realidade em Cristo; o imperativo é apropriar-se dela pela fé.")
        ]) +
        bloco("⚡ Escravos da Justiça (6:15-23)", [
            ("Rm 6:22-23", "Mas agora, libertados do pecado e feitos servos de Deus, tendes o vosso fruto para a santificação, e por fim a vida eterna. Porque o salário do pecado é a morte, mas o dom gratuito de Deus é a vida eterna, em Cristo Jesus nosso Senhor.",
             "O contraste final: o pecado paga (<em>opsonia</em> — salário militar) com morte; Deus dá (<em>charisma</em> — dom gratuito) vida eterna. A liberdade cristã não é autonomia — é transferência de senhor.")
        ])),
    7: ("A Luta Interior — Lei, Pecado e o Eu", "Miserável homem que sou! Quem me livrará do corpo desta morte?", "Rm 7:24",
        intro("Romanos 7 descreve a função da lei (revelar o pecado, não salvar), a luta interior do crente com a carne, e o grito de angústia que é respondido com ação de graças em Cristo.") +
        bloco("📜 Libertos da Lei (7:1-6)", [
            ("Rm 7:4-6", "Assim, meus irmãos, também vós fostes mortos para a lei pelo corpo de Cristo... Mas agora estamos livres da lei, tendo morrido para aquilo em que estávamos retidos; de sorte que servimos em novidade de espírito, e não na velhice da letra.",
             "A analogia do casamento: a morte dissolve o vínculo matrimonial; a morte de Cristo dissolve o vínculo da lei sobre o crente. Liberdade da lei não é antinomismo — é servir a Deus 'em novidade de espírito' (<em>kainoteti pneumatos</em>).")
        ]) +
        bloco("⚔️ A Luta Interior (7:15-25)", [
            ("Rm 7:15-20", "Porque o que faço, não o aprovo; pois não faço o que quero, mas o que odeio, isso faço.",
             "A divisão interna — querer o bem mas fazer o mal — é característica da regeneração, não da escravidão irrefletida. O incrédulo não tem esse conflito porque não tem o Espírito que ama a lei de Deus (7:22)."),
            ("Rm 7:24-25", "Miserável homem que sou! Quem me livrará do corpo desta morte? Graças a Deus por Jesus Cristo nosso Senhor!",
             "O grito de angústia é respondido imediatamente com ação de graças — a libertação já foi provida em Cristo. O 'corpo desta morte' alude à prática romana de amarrar um cadáver ao assassino. O cap. 8 é a resposta gloriosa.")
        ])),
    8: ("Vida no Espírito — O Capítulo da Glória", "Nenhuma condenação há, pois, para os que estão em Cristo Jesus.", "Rm 8:1",
        intro("Romanos 8 é o capítulo mais glorioso da Bíblia — nenhuma condenação, vida no Espírito, adoção como filhos, gemência da criação, intercessão do Espírito, e o amor invencível de Deus em Cristo.") +
        bloco("🕊️ Nenhuma Condenação — Vida no Espírito (8:1-17)", [
            ("Rm 8:1-4", "Nenhuma condenação há, pois, para os que estão em Cristo Jesus... Porque a lei do Espírito de vida, em Cristo Jesus, me livrou da lei do pecado e da morte.",
             "<em>Ouden ara nyn katakrima</em> — declaração presente, não apenas futura. O que a lei mosaica não pôde fazer (enfraquecida pela carne), Deus fez: enviou seu Filho para condenar o pecado na carne — na encarnação e na cruz, o pecado foi julgado definitivamente."),
            ("Rm 8:14-17", "Porque não recebestes o espírito de escravidão para viverdes de novo em temor, mas recebestes o espírito de adoção, pelo qual clamamos: Aba, Pai!",
             "A adoção (<em>hyiothesia</em>): o Espírito nos habilita a clamar 'Aba, Pai' — a palavra íntima que Jesus usou em Getsêmani. Filhos → herdeiros → co-herdeiros com Cristo: a herança inclui tanto o sofrimento quanto a glória.")
        ]) +
        bloco("🌟 Glória Futura e Amor Invencível (8:18-39)", [
            ("Rm 8:28", "E sabemos que todas as coisas contribuem juntamente para o bem daqueles que amam a Deus, daqueles que são chamados segundo o seu propósito.",
             "<em>Panta synergei eis agathon</em> — todas as coisas cooperam para o bem. Afirmação teológica: para os chamados segundo o propósito divino, até sofrimento, perda e dor são instrumentos da providência. A 'cadeia de ouro' (8:29-30): pré-conheceu → predestinou → chamou → justificou → glorificou."),
            ("Rm 8:35-39", "Quem nos separará do amor de Cristo?... Porque estou persuadido de que nem a morte, nem a vida... nos poderá separar do amor de Deus, que está em Cristo Jesus nosso Senhor.",
             "O clímax de Romanos 8. Lista de 10 poderes que não podem separar o crente do amor de Deus. <em>Hypernikomen</em> — mais do que vencedores: não apenas vencemos, mas vencemos com sobra, com glória.")
        ])),
    9: ("A Soberania de Deus e a Eleição", "Não depende, pois, do que quer nem do que corre, mas de Deus, que usa de misericórdia.", "Rm 9:16",
        intro("Romanos 9-11 trata da soberania divina e o destino de Israel. O cap. 9 trata da eleição soberana de Deus — não baseada em obras humanas, mas na vontade divina.") +
        bloco("💔 A Angústia de Paulo por Israel (9:1-5)", [
            ("Rm 9:1-3", "Digo a verdade em Cristo, não minto... que tenho grande tristeza e contínua dor no meu coração. Porque eu mesmo desejaria ser anátema, separado de Cristo, por amor de meus irmãos.",
             "A angústia de Paulo por Israel é genuína — ele desejaria ser amaldiçoado (<em>anathema</em>) se isso salvasse seu povo. Isto reflete o coração de Moisés (Êx 32:32) e antecipa o coração de Cristo que morreu pelos seus.")
        ]) +
        bloco("⚡ A Soberania Divina na Eleição (9:6-29)", [
            ("Rm 9:10-16", "E não somente isso, mas também Rebeca, quando concebeu de um só... porque, não tendo eles ainda nascido, nem tendo feito bem ou mal... foi-lhe dito: O mais velho servirá ao mais novo... Não depende, pois, do que quer nem do que corre, mas de Deus, que usa de misericórdia.",
             "A eleição de Jacó sobre Esaú antes do nascimento — sem base em obras — prova que a eleição divina não é baseada no mérito humano. A soberania de Deus na eleição não é arbitrariedade — é misericórdia além do que merecemos."),
            ("Rm 9:20-21", "Mas, ó homem, quem és tu para altercar com Deus? Porventura dirá o barro ao que o formou: Por que me fizeste assim?",
             "A metáfora do oleiro (Is 29:16; 45:9; Jr 18:1-10) ensina que Deus tem o direito soberano de usar suas criaturas como lhe apraz. A resposta de Paulo à objeção não é uma explicação filosófica — é uma reorientação: quem somos nós para questionar o Criador?")
        ])),
    10: ("Israel, a Fé e a Pregação do Evangelho", "Se confessares com a tua boca o Senhor Jesus, e creres no teu coração que Deus o ressuscitou dos mortos, serás salvo.", "Rm 10:9",
        intro("Romanos 10 explica por que Israel, tendo o zêlo por Deus, não alcançou a justiça — porque buscou a justiça pelas obras e não pela fé. E apresenta a cadeia da salvação: ouvir, crer, confessar.") +
        bloco("✡️ O Zêlo sem Conhecimento (10:1-13)", [
            ("Rm 10:2-4", "Porque lhes dou testemunho de que têm zêlo de Deus, mas não com entendimento... Porque o fim da lei é Cristo, para justificação de todo aquele que crê.",
             "O problema de Israel não é falta de religiosidade — é zêlo sem conhecimento (<em>kat epignosin</em>). Cristo é o <em>telos</em> da lei — o alvo, o cumprimento, o fim para o qual a lei sempre apontou."),
            ("Rm 10:9-13", "Se confessares com a tua boca o Senhor Jesus, e creres no teu coração que Deus o ressuscitou dos mortos, serás salvo... porque todo aquele que invocar o nome do Senhor será salvo.",
             "A fórmula da salvação: crença no coração + confissão com a boca. A confissão '<em>Kyrios Iesous</em>' era a declaração mais radical no mundo romano, onde '<em>Kyrios Kaisar</em>' era a lealdade exigida.")
        ]) +
        bloco("📢 A Cadeia da Pregação (10:14-21)", [
            ("Rm 10:14-17", "Como, pois, invocarão aquele em quem não creram? E como crerão naquele de quem não ouviram?... Logo a fé é pelo ouvir, e o ouvir pela palavra de Cristo.",
             "A cadeia missionária em ordem reversa: salvação ← invocação ← fé ← ouvir ← pregação ← envio. <em>Pistis ex akoes</em> — a fé vem pelo ouvir (<em>akoe</em>). A missão não é opcional — é a cadeia que liga o envio à salvação.")
        ])),
    11: ("O Mistério de Israel — Endurecimento e Restauração", "Assim todo o Israel será salvo, como está escrito: De Sião virá o Libertador.", "Rm 11:26",
        intro("Romanos 11 revela o 'mistério' do plano de Deus para Israel: o endurecimento parcial de Israel é temporário e serve ao propósito de incluir os gentios; ao final, 'todo o Israel será salvo'.") +
        bloco("🌿 O Remanescente e a Oliveira (11:1-24)", [
            ("Rm 11:1-5", "Digo, pois: Rejeitou Deus o seu povo? De modo nenhum!... Assim também neste tempo presente ficou um remanescente, segundo a eleição da graça.",
             "Paulo responde com sua própria existência: ele é judeu e foi salvo. O remanescente (<em>leimma</em>) de Israel que crê em Cristo é a continuidade do verdadeiro Israel."),
            ("Rm 11:17-21", "Mas se alguns dos ramos foram quebrados, e tu, sendo oliveira brava, foste enxertado no lugar deles... não te glories contra os ramos.",
             "A metáfora da oliveira: Israel é a oliveira cultivada; os gentios são ramos de oliveira brava enxertados. Advertência aos gentios: não se orgulhem — vocês são sustentados pela raiz (as promessas a Israel).")
        ]) +
        bloco("🌟 O Mistério e a Doxologia (11:25-36)", [
            ("Rm 11:25-26", "Porque não quero, irmãos, que ignoreis este mistério... que o endurecimento em parte aconteceu a Israel, até que a plenitude dos gentios haja entrado. E assim todo o Israel será salvo.",
             "O <em>mysterion</em>: o endurecimento de Israel é parcial ('em parte') e temporário ('até que'). A doxologia final (11:33-36) é a resposta adequada: 'Ó profundidade das riquezas, tanto da sabedoria como da ciência de Deus!'")
        ])),
    12: ("Sacrifício Vivo — Ética do Reino", "Apresentai os vossos corpos em sacrifício vivo, santo e agradável a Deus, que é o vosso culto racional.", "Rm 12:1",
        intro("Romanos 12 marca a transição da teologia (caps. 1-11) para a ética (caps. 12-16). A vida cristã é uma resposta de gratidão à misericórdia de Deus.") +
        bloco("🙏 O Sacrifício Vivo e a Transformação da Mente (12:1-2)", [
            ("Rm 12:1-2", "Rogo-vos, pois, irmãos, pela compaixão de Deus, que apresenteis os vossos corpos em sacrifício vivo, santo e agradável a Deus, que é o vosso culto racional. E não vos conformeis com este século, mas transformai-vos pela renovação do vosso entendimento.",
             "O 'pois' (<em>oun</em>) conecta a ética à teologia: a vida cristã é resposta à misericórdia de Deus. <em>Thysian zosan</em> — sacrifício vivo. <em>Logiken latreian</em> — culto racional/espiritual: a adoração não é apenas ritual — é a vida inteira oferecida a Deus. <em>Metamorphousthe</em> — transformai-vos (de onde vem 'metamorfose').")
        ]) +
        bloco("💝 Amor Prático na Comunidade (12:9-21)", [
            ("Rm 12:9-13", "O amor seja sem fingimento. Aborrecei o mal e apegai-vos ao bem. Amai-vos cordialmente uns aos outros com amor fraternal.",
             "A ética cristã começa com o amor sem fingimento (<em>anypokritos</em> — sem máscara, sem hipocrisia). A lista de virtudes em 12:9-21 é uma das mais completas do NT."),
            ("Rm 12:19-21", "Não vos vingueis a vós mesmos, amados, mas dai lugar à ira de Deus... Não te deixes vencer do mal, mas vence o mal com o bem.",
             "A ética do não-retaliar é revolucionária no mundo antigo. 'Vencer o mal com o bem' (<em>nika en to agatho to kakon</em>) é a estratégia cristã de transformação social.")
        ])),
    13: ("Autoridades, Amor e a Armadura da Luz", "Não devais nada a ninguém, exceto o amor com que vos ameis uns aos outros.", "Rm 13:8",
        intro("Romanos 13 trata da relação com as autoridades civis, do amor como cumprimento da lei, e da urgência escatológica que motiva a vida cristã.") +
        bloco("🏛️ Submissão às Autoridades (13:1-7)", [
            ("Rm 13:1-4", "Toda alma esteja sujeita às potestades superiores; porque não há potestade que não venha de Deus... Porque é ministro de Deus, servidor teu para o bem.",
             "Paulo escreve sob Nero (~57 d.C.). A submissão às autoridades não é endosso de toda ação governamental — é reconhecimento de que o governo tem uma função divina de manter a ordem. Os limites: quando a autoridade exige desobediência a Deus, os cristãos devem 'obedecer a Deus antes que aos homens' (At 5:29).")
        ]) +
        bloco("💝 O Amor como Cumprimento da Lei (13:8-14)", [
            ("Rm 13:8-10", "Não devais nada a ninguém, exceto o amor com que vos ameis uns aos outros; porque quem ama ao próximo cumpriu a lei.",
             "O amor (<em>agape</em>) não é um sentimento — é um princípio ético que cumpre toda a lei. Os mandamentos são resumidos em 'amarás o teu próximo como a ti mesmo'."),
            ("Rm 13:11-14", "E isto, sabendo vós o tempo, que é já hora de despertarmos do sono... A noite é passada, e o dia se aproxima; lancemos, pois, as obras das trevas, e vistamo-nos das armas da luz.",
             "A urgência escatológica motiva a ética: o 'dia' da vinda de Cristo se aproxima. 'Revesti-vos do Senhor Jesus Cristo' — a vida cristã é vestir Cristo, deixar que sua vida se manifeste na nossa.")
        ])),
    14: ("O Forte e o Fraco — Liberdade e Amor", "Assim, pois, cada um de nós dará conta de si mesmo a Deus.", "Rm 14:12",
        intro("Romanos 14-15 trata de questões de consciência e liberdade cristã. O princípio: a liberdade deve ser exercida em amor, não em julgamento.") +
        bloco("⚖️ Não Julgue o Irmão Fraco (14:1-23)", [
            ("Rm 14:1-4", "Recebei o que é fraco na fé, mas não para decidir dúvidas... O que come não despreze o que não come; e o que não come não julgue o que come; porque Deus o recebeu.",
             "O contexto: provavelmente judeus cristãos com escrúpulos sobre alimentos sacrificados a ídolos. Paulo não toma partido na questão em si — ele trata da atitude: nem o 'forte' deve desprezar o 'fraco', nem o 'fraco' deve julgar o 'forte'."),
            ("Rm 14:17-19", "Porque o reino de Deus não é comida nem bebida, mas justiça, e paz, e alegria no Espírito Santo.",
             "O reino de Deus não é definido por práticas externas — é definido por justiça, paz e alegria no Espírito Santo. A liberdade cristã deve ser exercida em função da edificação (<em>oikodome</em>) do outro.")
        ])),
    15: ("O Exemplo de Cristo e os Planos de Paulo", "Ora, o Deus de esperança vos encha de todo o gozo e paz em credes.", "Rm 15:13",
        intro("Romanos 15 conclui a seção ética com o exemplo de Cristo como modelo de serviço ao fraco, a missão de Paulo aos gentios, e seus planos de visitar Roma e a Espanha.") +
        bloco("🙏 Cristo como Modelo de Serviço (15:1-13)", [
            ("Rm 15:1-3", "Ora, nós, os que somos fortes, devemos suportar as fraquezas dos fracos, e não agradar a nós mesmos. Cada um de nós agrade ao próximo no que é bom, para edificação. Porque também Cristo não agradou a si mesmo.",
             "O argumento final: Cristo é o modelo supremo de não agradar a si mesmo. Ele, sendo Deus, se humilhou e serviu (Fp 2:5-11)."),
            ("Rm 15:7-9", "Portanto, recebei-vos uns aos outros, como também Cristo nos recebeu para glória de Deus.",
             "A recepção mútua entre judeus e gentios na Igreja é fundamentada na recepção de Cristo. A unidade da Igreja não é uniformidade — é diversidade unida pelo mesmo Senhor.")
        ]) +
        bloco("🌍 A Missão de Paulo aos Gentios (15:14-33)", [
            ("Rm 15:20-24", "E assim procurei pregar o evangelho, não onde Cristo já tinha sido nomeado, para não edificar sobre fundamento alheio... quando for a Espanha, irei ter convosco.",
             "Paulo descreve sua estratégia missionária: pregar onde Cristo ainda não foi nomeado — fronteiras do Evangelho. Seu plano: Jerusalém → Roma → Espanha. A Espanha era o extremo ocidental do mundo romano — 'os confins da terra' de At 1:8.")
        ])),
    16: ("Saudações e Doxologia Final", "Ao único Deus sábio seja dada glória por Jesus Cristo para sempre. Amém.", "Rm 16:27",
        intro("Romanos 16 é o capítulo mais pessoal da carta — uma lista de 29 saudações individuais que revela a rede de relacionamentos de Paulo e a diversidade da Igreja primitiva.") +
        bloco("👥 A Rede de Relacionamentos de Paulo (16:1-16)", [
            ("Rm 16:1-2", "Recomendo-vos Febe, nossa irmã, que é diaconisa da igreja que está em Cencreia.",
             "Febe (<em>Phoibe</em>) é a portadora da carta — ela a levou de Corinto a Roma. Paulo a chama de <em>diakonon</em> (diaconisa/ministra) e <em>prostatis</em> (protetora/patrona) — termos de liderança e serviço. Das 29 pessoas saudadas, pelo menos 10 são mulheres, muitas com funções de liderança."),
            ("Rm 16:3-5", "Saudai a Priscila e Áquila, meus cooperadores em Cristo Jesus; os quais pela minha vida expuseram os seus próprios pescoços.",
             "Priscila e Áquila aparecem 6 vezes no NT — sempre como par ministerial. Notavelmente, Priscila é mencionada primeiro 4 das 6 vezes, sugerindo papel de liderança mais proeminente.")
        ]) +
        bloco("⭐ Doxologia Final (16:25-27)", [
            ("Rm 16:25-27", "Ora, àquele que é poderoso para vos confirmar segundo o meu evangelho... ao único Deus sábio seja dada glória por Jesus Cristo para sempre. Amém.",
             "A doxologia final resume toda a teologia de Romanos: o Evangelho é o mistério eterno agora revelado; Deus é o único sábio (<em>mono sopho theo</em>); a glória é dada por Jesus Cristo para sempre. <em>Soli Deo Gloria</em>.")
        ])),
}

def gerar_romanos():
    for num, (titulo, vk, rk, body) in romanos_caps.items():
        html = page("Romanos", num, 16, titulo, vk, rk, body, "romanos", "../../../..")
        salvar("romanos", num, html)
    print("✅ Romanos: 16 capítulos gerados")

# ─────────────────────────────────────────────
# 1 CORÍNTIOS — 16 capítulos
# ─────────────────────────────────────────────
corintios1_caps = {
    1: ("A Cruz — Loucura para o Mundo, Poder de Deus", "Porque a palavra da cruz é loucura para os que perecem; mas para nós, que somos salvos, é o poder de Deus.", "1Cor 1:18",
        intro("1 Coríntios foi escrita ~55 d.C. para uma igreja dividida, imoral e confusa. O cap. 1 confronta as divisões partidárias com a teologia da cruz — que inverte toda sabedoria e poder humanos.") +
        bloco("✝️ A Loucura da Cruz (1:18-31)", [
            ("1Cor 1:18-25", "Porque a palavra da cruz é loucura para os que perecem; mas para nós, que somos salvos, é o poder de Deus... porque os judeus pedem sinais, e os gregos buscam sabedoria; mas nós pregamos a Cristo crucificado.",
             "A cruz (<em>stauros</em>) era o símbolo de vergonha máxima no mundo antigo. Paulo proclama que esta 'loucura' (<em>moria</em>) é o poder (<em>dynamis</em>) e a sabedoria (<em>sophia</em>) de Deus. Para os judeus, um Messias crucificado era <em>skandalon</em>. Para os gregos, era <em>moria</em>. Mas para os chamados, é o poder de Deus."),
            ("1Cor 1:26-29", "Porque vede, irmãos, a vossa vocação; que não são muitos os sábios segundo a carne, nem muitos os poderosos, nem muitos os nobres que são chamados. Mas Deus escolheu as coisas loucas do mundo para confundir as sábias.",
             "A composição sociológica da Igreja de Corinto confirma a teologia da cruz: não muitos sábios, poderosos ou nobres. Deus escolhe deliberadamente o que o mundo despreza para que nenhuma carne se glorie (<em>kauchesete</em>) diante dele.")
        ])),
    2: ("A Sabedoria do Espírito", "As coisas que o olho não viu, e o ouvido não ouviu, e não subiram ao coração do homem, são as que Deus preparou para os que o amam.", "1Cor 2:9",
        intro("1 Coríntios 2 contrasta a sabedoria humana com a sabedoria do Espírito. Paulo pregou não com eloquência filosófica, mas com demonstração do Espírito.") +
        bloco("🕊️ A Pregação de Paulo e o Espírito (2:1-16)", [
            ("1Cor 2:1-5", "E eu, irmãos, quando fui ter convosco, não fui com sublimidade de palavras ou de sabedoria... para que a vossa fé não se apoiasse em sabedoria dos homens, mas no poder de Deus.",
             "Paulo deliberadamente renunciou à eloquência retórica para que a fé dos coríntios não repousasse na habilidade humana mas no poder de Deus. A demonstração (<em>apodeixis</em>) do Espírito é a evidência de transformação de vidas."),
            ("1Cor 2:9-12", "Mas, como está escrito: As coisas que o olho não viu... são as que Deus preparou para os que o amam. Mas Deus no-las revelou pelo seu Espírito.",
             "O Espírito (<em>pneuma</em>) é o agente da revelação — ele conhece as profundezas de Deus (<em>ta bathe tou theou</em>) como o espírito humano conhece as profundezas do ser humano.")
        ])),
    3: ("Cooperadores de Deus — Fundamento e Edificação", "Porque ninguém pode pôr outro fundamento além do que está posto, o qual é Jesus Cristo.", "1Cor 3:11",
        intro("1 Coríntios 3 confronta o partidarismo com a visão correta do ministério: os líderes são cooperadores de Deus, não donos da Igreja. O único fundamento é Cristo.") +
        bloco("🌱 Plantadores e Regadores (3:1-9)", [
            ("1Cor 3:6-9", "Eu plantei, Apolo regou, mas Deus deu o crescimento. De maneira que nem o que planta é alguma coisa, nem o que rega, mas Deus, que dá o crescimento.",
             "A metáfora agrícola desmonta o partidarismo: Paulo plantou, Apolo regou — mas o crescimento vem de Deus. Os ministros são <em>synergoi theou</em> — cooperadores de Deus, não competidores. A glória pertence a Deus, não aos instrumentos.")
        ]) +
        bloco("🏗️ O Único Fundamento (3:10-23)", [
            ("1Cor 3:11-15", "Porque ninguém pode pôr outro fundamento além do que está posto, o qual é Jesus Cristo. Ora, se alguém edifica sobre este fundamento ouro, prata, pedras preciosas, madeira, feno, palha, a obra de cada um se tornará manifesta.",
             "O fundamento (<em>themelion</em>) já está posto — é Cristo. Sobre ele, cada ministro edifica. O fogo do julgamento testará a qualidade do trabalho: ouro, prata e pedras preciosas sobrevivem; madeira, feno e palha são consumidos. O ministro pode ser salvo, mas 'como que pelo fogo' — sem recompensa.")
        ])),
    4: ("Mordomos dos Mistérios de Deus", "Portanto, não julgueis nada antes do tempo, até que venha o Senhor.", "1Cor 4:5",
        intro("1 Coríntios 4 define o papel correto dos apóstolos: mordomos dos mistérios de Deus, não celebridades. Paulo confronta o orgulho coríntio com a realidade do apostolado sofredor.") +
        bloco("🔑 Mordomos Fiéis (4:1-7)", [
            ("1Cor 4:1-4", "Portanto, que o homem nos considere como ministros de Cristo e mordomos dos mistérios de Deus. E além disso o que se requer nos mordomos é que cada um seja encontrado fiel.",
             "<em>Hyperetas Christou</em> — servos de Cristo (literalmente 'remadores de baixo deck'). <em>Oikonomous mysterion theou</em> — mordomos dos mistérios de Deus. A fidelidade (<em>pistos</em>) é o único critério para o mordomo — não o sucesso, não a popularidade.")
        ]) +
        bloco("⚡ O Apostolado Sofredor (4:8-21)", [
            ("1Cor 4:10-13", "Nós somos loucos por amor de Cristo, mas vós sois prudentes em Cristo; nós somos fracos, mas vós sois fortes; vós sois honrados, mas nós somos desprezados... Tornamo-nos como o lixo do mundo, a escória de todas as coisas, até agora.",
             "A ironia sarcástica de Paulo contrasta a autopercepção dos coríntios (ricos, fortes, honrados) com a realidade apostólica (loucos, fracos, desprezados). <em>Peripsema</em> — lixo, escória: o que é varrido após a limpeza. O apostolado não é glória humana — é participação no sofrimento de Cristo.")
        ])),
    5: ("Disciplina Eclesiástica e Santidade", "Não sabeis que um pouco de fermento leveda toda a massa?", "1Cor 5:6",
        intro("1 Coríntios 5 confronta o caso de imoralidade sexual tolerada na Igreja de Corinto e ensina o princípio da disciplina eclesiástica para a pureza da comunidade.") +
        bloco("⚠️ O Caso de Imoralidade (5:1-13)", [
            ("1Cor 5:1-5", "Ouve-se geralmente que há entre vós fornicação, e tal fornicação que nem ainda se nomeia entre os gentios... E vós estais ensoberbecidos! Não deveis antes ter feito luto?",
             "O caso: um homem vivendo com a mulher de seu pai (madrasta) — proibido tanto pela lei romana quanto pela lei mosaica (Lv 18:8). A Igreja não apenas tolerou — se orgulhou disso (provavelmente como demonstração de 'liberdade cristã'). Paulo ordena a exclusão do indivíduo para o 'bem' de sua alma — a disciplina tem propósito restaurador."),
            ("1Cor 5:6-8", "Não sabeis que um pouco de fermento leveda toda a massa? Purificai-vos, pois, do fermento velho, para que sejais uma nova massa, assim como sois sem fermento. Porque Cristo, nossa páscoa, foi sacrificado por nós.",
             "A metáfora do fermento (Pv 25:4; Gl 5:9): o pecado tolerado contamina toda a comunidade. A referência à Páscoa é profunda: Cristo é o Cordeiro pascal sacrificado; a Igreja deve ser 'sem fermento' (pão ázimo) — pureza que flui da obra de Cristo, não do esforço humano.")
        ])),
    6: ("Litígios e Santidade do Corpo", "Ou não sabeis que o vosso corpo é o templo do Espírito Santo?", "1Cor 6:19",
        intro("1 Coríntios 6 aborda dois problemas: cristãos levando outros cristãos a tribunais pagãos, e a imoralidade sexual justificada com slogans de 'liberdade'. Paulo fundamenta a ética sexual na teologia da ressurreição e do Espírito.") +
        bloco("⚖️ Litígios Entre Irmãos (6:1-11)", [
            ("1Cor 6:1-6", "Ousa algum de vós, tendo alguma coisa contra o outro, ir a juízo perante os injustos, e não perante os santos?",
             "Paulo não proíbe todo recurso legal — proíbe que cristãos levem disputas internas a juízes pagãos. A Igreja deveria ser capaz de resolver suas próprias disputas. O argumento: se os santos julgarão o mundo e os anjos (6:2-3), quanto mais questões cotidianas?")
        ]) +
        bloco("🏛️ O Corpo como Templo do Espírito (6:12-20)", [
            ("1Cor 6:12-14", "Todas as coisas me são lícitas, mas nem todas as coisas convêm... O corpo não é para a fornicação, mas para o Senhor, e o Senhor para o corpo. E Deus, que ressuscitou o Senhor, também nos ressuscitará a nós pelo seu poder.",
             "Paulo cita dois slogans coríntios: 'Tudo me é lícito' e 'Os alimentos são para o ventre' — e os corrige. O corpo não é moralmente neutro — ele pertence ao Senhor e será ressuscitado. A ressurreição corporal fundamenta a ética sexual."),
            ("1Cor 6:19-20", "Ou não sabeis que o vosso corpo é o templo do Espírito Santo, que habita em vós, o qual tendes da parte de Deus, e que não sois de vós mesmos? Porque fostes comprados por preço; glorificai, pois, a Deus no vosso corpo.",
             "O argumento final: o corpo do crente é <em>naos tou hagiou pneumatos</em> — templo do Espírito Santo. A profanação do templo é profanação do Espírito. 'Fostes comprados por preço' — a redenção implica pertencimento. A santidade sexual não é legalismo — é adoração.")
        ])),
    7: ("Casamento, Celibato e a Vocação Cristã", "Cada um permaneça no chamado em que foi chamado.", "1Cor 7:20",
        intro("1 Coríntios 7 é o capítulo mais extenso sobre casamento e celibato no NT. Paulo responde a perguntas específicas dos coríntios sobre sexualidade, casamento, divórcio e celibato, sempre no contexto da urgência escatológica.") +
        bloco("💍 Casamento e Celibato (7:1-16)", [
            ("1Cor 7:3-5", "O marido cumpra o dever conjugal para com a mulher, e da mesma forma a mulher para com o marido. A mulher não tem poder sobre o seu próprio corpo, mas o marido; e da mesma forma o marido não tem poder sobre o seu próprio corpo, mas a mulher.",
             "A mutualidade conjugal de Paulo é revolucionária para o mundo antigo: tanto o marido quanto a mulher têm deveres e direitos iguais no casamento. O corpo de cada cônjuge pertence ao outro — não como propriedade, mas como entrega mútua."),
            ("1Cor 7:10-11", "Aos casados mando, não eu, mas o Senhor, que a mulher não se separe do marido... e que o marido não deixe a sua mulher.",
             "Paulo distingue entre o ensino do Senhor (7:10-11) e sua própria opinião inspirada (7:12). A proibição do divórcio vem de Jesus (Mt 5:32; 19:9). O 'mas se se separar' indica que Paulo reconhece que separações acontecem — mas a reconciliação é sempre o objetivo.")
        ]) +
        bloco("🌟 A Urgência Escatológica (7:25-40)", [
            ("1Cor 7:29-31", "Mas isto digo, irmãos, que o tempo é breve; resta, pois, que os que têm mulheres sejam como se não as tivessem... porque a aparência deste mundo passa.",
             "A urgência escatológica molda toda a ética de Paulo: o tempo é breve (<em>ho kairos synestalmenos estin</em>). Isso não deprecia o casamento — é um convite a não ser totalmente absorvido pelas preocupações do presente. O celibato permite 'as coisas do Senhor' sem distração.")
        ])),
    8: ("Ídolos, Conhecimento e Amor", "O conhecimento ensoberbece, mas o amor edifica.", "1Cor 8:1",
        intro("1 Coríntios 8 trata da questão das carnes sacrificadas a ídolos — um problema prático na Corinto do século I. Paulo usa o caso para ensinar o princípio fundamental: o conhecimento sem amor destrói; o amor edifica.") +
        bloco("🧠 Conhecimento vs. Amor (8:1-13)", [
            ("1Cor 8:1-3", "O conhecimento ensoberbece, mas o amor edifica. E se alguém pensa que sabe alguma coisa, ainda não sabe como convém saber. Mas, se alguém ama a Deus, esse é conhecido por ele.",
             "<em>Gnosis physioi</em> — o conhecimento ensoberbece (literalmente 'infla como um fole'). <em>Agape oikodomei</em> — o amor edifica (constrói como um edifício). O paradoxo: quem pensa que sabe ainda não sabe como convém; quem ama a Deus é <em>conhecido por Deus</em> — a relação é mais importante que o conhecimento."),
            ("1Cor 8:9-13", "Mas vede que esta vossa liberdade não venha a ser de algum modo tropeço para os fracos... E assim, pecando contra os irmãos e ferindo a sua fraca consciência, pecastes contra Cristo.",
"O princípio da liberdade limitada pelo amor: a liberdade do forte deve ser exercida com consciência do efeito sobre o irmão fraco. Pecar contra a consciência do irmão é pecar contra Cristo.")
        ])),
    9: ("Os Direitos do Apóstolo e a Disciplina Pessoal", "Faço tudo por amor do evangelho, para ser seu co-participante.", "1Cor 9:23",
        intro("1 Coríntios 9 é a defesa do apostolado de Paulo e o exemplo de sua renúncia voluntária aos direitos apostólicos — por amor ao Evangelho.") +
        bloco("⚡ Direitos Apostólicos (9:1-18)", [
            ("1Cor 9:14-18", "Assim também ordenou o Senhor que os que pregam o evangelho vivam do evangelho. Mas eu de nada disso me tenho servido... Porque se eu pregar o evangelho, não tenho de que me gloriar, pois a necessidade me é imposta; e ai de mim se não pregar o evangelho!",
             "Paulo tinha o direito de ser sustentado pela Igreja (9:14; Lc 10:7), mas renunciou voluntariamente para não criar obstáculo ao Evangelho. Sua compulsão missionária: 'ai de mim se não pregar' (<em>ouai gar moi estin</em>) — não é opção, é necessidade.")
        ]) +
        bloco("🏃 A Disciplina do Atleta (9:24-27)", [
            ("1Cor 9:24-27", "Não sabeis vós que os que correm no estádio, todos na verdade correm, mas um só leva o prêmio?... Mas subjugo o meu corpo e o reduzo à servidão, para que, pregando aos outros, eu mesmo não venha a ser reprovado.",
             "A metáfora dos Jogos Ístmicos (realizados perto de Corinto). Paulo teme ser <em>adokimos</em> — reprovado, desqualificado. Não a perda da salvação, mas a perda da aprovação ministerial. A disciplina pessoal é necessária para a eficácia ministerial.")
        ])),
    10: ("Advertências do Deserto e a Mesa do Senhor", "Assim, pois, quer comais quer bebais, ou façais outra qualquer coisa, fazei tudo para a glória de Deus.", "1Cor 10:31",
        intro("1 Coríntios 10 usa os exemplos do Israel no deserto como advertência contra a presunção espiritual, e estabelece o princípio de que tudo deve ser feito para a glória de Deus.") +
        bloco("⚠️ Exemplos do Deserto (10:1-13)", [
            ("1Cor 10:1-6", "Ora, irmãos, não quero que ignoreis que nossos pais estavam todos debaixo da nuvem, e todos passaram pelo mar... Mas em muitos deles Deus não se agradou, pois foram prostrados no deserto.",
             "Israel tinha todos os privilégios espirituais (nuvem, mar, maná, rocha) — e ainda assim falhou. Paulo usa isso como advertência tipológica para os coríntios que se sentiam espiritualmente seguros. A rocha que os seguia era Cristo (10:4) — tipologia cristológica do AT."),
            ("1Cor 10:13", "Não vos sobreveio tentação alguma que não fosse humana; mas Deus é fiel, e não permitirá que sejais tentados além do que podeis suportar; mas com a tentação dará também o escape, para que a possais suportar.",
             "A promessa de 10:13 é frequentemente mal compreendida: não promete que não haverá tentação, mas que haverá uma saída (<em>ekbasis</em>). Deus é fiel (<em>pistos</em>) — sua fidelidade garante o escape.")
        ]) +
        bloco("🌟 Tudo para a Glória de Deus (10:23-33)", [
            ("1Cor 10:31", "Assim, pois, quer comais quer bebais, ou façais outra qualquer coisa, fazei tudo para a glória de Deus.",
             "O princípio unificador de toda a ética cristã: <em>panta eis doxan theou poieite</em>. Não há esfera da vida que fique fora da glória de Deus — nem mesmo comer e beber.")
        ])),
    11: ("A Ceia do Senhor e a Ordem no Culto", "Porque todas as vezes que comerdes este pão e beberdes este cálice, anunciais a morte do Senhor, até que ele venha.", "1Cor 11:26",
        intro("1 Coríntios 11 corrige abusos na Ceia do Senhor e ensina o significado profundo da eucaristia — memorial, proclamação e antecipação.") +
        bloco("🍞 A Ceia do Senhor (11:17-34)", [
            ("1Cor 11:23-26", "Porque eu recebi do Senhor o que também vos ensinei: que o Senhor Jesus, na noite em que foi traído, tomou o pão; e, tendo dado graças, o partiu e disse: Tomai, comei; isto é o meu corpo que é partido por vós; fazei isto em memória de mim.",
             "A tradição eucarística mais antiga do NT (anterior aos Evangelhos). Três dimensões: (1) <em>anamnesis</em> — memorial da morte de Cristo; (2) proclamação (<em>katangellein</em>) — a Ceia é ato de pregação; (3) antecipação — 'até que ele venha'. A Ceia olha para trás (cruz), para cima (Cristo ressurreto presente) e para frente (segunda vinda)."),
            ("1Cor 11:27-29", "Portanto, qualquer que comer este pão ou beber o cálice do Senhor indignamente, será réu do corpo e do sangue do Senhor. Examine-se, pois, o homem a si mesmo.",
             "Comer 'indignamente' (<em>anaxios</em>) não se refere à indignidade pessoal do crente (todos somos indignos), mas à maneira desordenada como os coríntios celebravam. O exame (<em>dokimazeto</em>) é necessário antes de participar.")
        ])),
    12: ("Os Dons do Espírito e o Corpo de Cristo", "Porque assim como o corpo é um, e tem muitos membros, e todos os membros, sendo muitos, são um só corpo, assim é Cristo também.", "1Cor 12:12",
        intro("1 Coríntios 12 apresenta a doutrina dos dons espirituais (carismas) e a metáfora do corpo de Cristo — unidade na diversidade.") +
        bloco("🎁 Os Dons do Espírito (12:1-11)", [
            ("1Cor 12:4-7", "Ora, há diversidade de dons, mas o Espírito é o mesmo; e há diversidade de ministérios, mas o Senhor é o mesmo; e há diversidade de operações, mas é o mesmo Deus que opera tudo em todos. Mas a manifestação do Espírito é dada a cada um, como lhe apraz.",
             "A estrutura trinitária dos dons: o Espírito distribui os dons, o Senhor (Cristo) define os ministérios, o Pai opera as obras. A diversidade é intencional — todos os dons têm a mesma fonte e o mesmo propósito: a edificação da Igreja.")
        ]) +
        bloco("🏛️ O Corpo de Cristo (12:12-31)", [
            ("1Cor 12:14-20", "Porque também o corpo não é um só membro, mas muitos... E se o ouvido disser: Porque não sou olho, não sou do corpo; nem por isso deixa de ser do corpo.",
             "A metáfora do corpo confronta dois erros: (1) o membro que se sente inferior porque não tem o dom de outro; (2) o membro que despreza outros por serem diferentes. Ambos violam a unidade do corpo. A diversidade de dons é necessária — um corpo todo olho seria monstruoso."),
            ("1Cor 12:31", "Mas procurai com zelo os melhores dons; e eu vos mostrarei um caminho mais excelente.",
             "A transição para o cap. 13: os dons são bons, mas há um 'caminho mais excelente' (<em>kath hyperbolen hodon</em>) — o amor. Os dons sem amor são vazio.")
        ])),
    13: ("O Hino do Amor", "Agora, pois, permanecem a fé, a esperança e o amor, estes três; mas o maior destes é o amor.", "1Cor 13:13",
        intro("1 Coríntios 13 é o capítulo mais famoso da Bíblia — o hino do amor. Estruturado em três partes: a necessidade do amor, as qualidades do amor, a permanência do amor.") +
        bloco("💝 A Necessidade do Amor (13:1-3)", [
            ("1Cor 13:1-3", "Ainda que eu fale as línguas dos homens e dos anjos, e não tenha amor, sou como o bronze que soa, ou como o címbalo que retine. E ainda que eu tenha o dom de profecia, e saiba todos os mistérios e toda a ciência, e ainda que eu tenha toda a fé... e não tenha amor, nada sou.",
             "Paulo lista os dons mais valorizados pelos coríntios (línguas, profecia, ciência, fé, generosidade, martírio) e declara que sem amor (<em>agape</em>) todos são nada. O bronze sonante (<em>chalkos echon</em>) era usado nos rituais pagãos de Corinto — os dons sem amor são religiosidade pagã.")
        ]) +
        bloco("🌟 As Qualidades do Amor (13:4-7)", [
            ("1Cor 13:4-7", "O amor é sofredor, é benigno; o amor não é invejoso; o amor não trata com leviandade, não se ensoberbece, não se porta com indecência, não busca os seus interesses, não se irrita, não suspeita mal... tudo sofre, tudo crê, tudo espera, tudo suporta.",
             "Quinze qualidades do amor — 8 negativas (o que o amor não faz) e 7 positivas. Cada uma confronta um problema específico de Corinto: inveja (rivalidade de dons), orgulho (partidarismo), busca dos próprios interesses (litígios), irritação (divisões). O amor é descrito em termos de comportamento, não de sentimento.")
        ]) +
        bloco("♾️ A Permanência do Amor (13:8-13)", [
            ("1Cor 13:8-10", "O amor jamais acaba; mas havendo profecias, serão aniquiladas; havendo línguas, cessarão; havendo ciência, será aniquilada. Porque, em parte, conhecemos, e em parte, profetizamos; mas quando vier o que é perfeito, então o que é em parte será aniquilado.",
             "Os dons são temporários — servem ao período presente. O amor é eterno. 'O que é perfeito' (<em>to teleion</em>): debate entre os intérpretes — refere-se ao cânon completo (cessacionismo) ou à segunda vinda de Cristo (continuacionismo). O contexto sugere a segunda vinda: 'então conheceremos como também somos conhecidos' (13:12)."),
            ("1Cor 13:13", "Agora, pois, permanecem a fé, a esperança e o amor, estes três; mas o maior destes é o amor.",
             "A tríade teológica: fé, esperança e amor. O amor é o maior porque é o único que permanece na eternidade — na glória, não precisaremos mais de fé (veremos) nem de esperança (teremos), mas o amor será eterno.")
        ])),
    14: ("Línguas e Profecia no Culto", "Assim também vós, pois que ambicionais os dons espirituais, procurai ser ricos neles para a edificação da Igreja.", "1Cor 14:12",
        intro("1 Coríntios 14 regula o uso de línguas e profecia no culto. O princípio central: tudo deve ser para a edificação da Igreja.") +
        bloco("🗣️ Línguas vs. Profecia (14:1-25)", [
            ("1Cor 14:1-5", "Segui o amor, e procurai com zelo os dons espirituais, mas principalmente o de profetizar... Mas o que profetiza fala aos homens para edificação, exortação e consolação.",
             "Paulo não deprecia o dom de línguas — ele mesmo fala em línguas (14:18). Mas no culto coletivo, a profecia é preferível porque edifica a Igreja. O critério não é a experiência subjetiva do falante, mas o benefício objetivo da congregação."),
            ("1Cor 14:19", "Mas na Igreja prefiro falar cinco palavras com o meu entendimento, para também instruir os outros, do que dez mil palavras em língua.",
             "A proporção 5:10.000 é hiperbólica mas eloquente: cinco palavras inteligíveis valem mais que dez mil ininteligíveis para a edificação da Igreja.")
        ]) +
        bloco("📋 Ordem no Culto (14:26-40)", [
            ("1Cor 14:26", "Que é, pois, irmãos? Quando vos reunis, cada um de vós tem salmo, tem doutrina, tem língua, tem revelação, tem interpretação. Seja tudo feito para edificação.",
             "O culto primitivo era participativo — cada membro contribuía. O critério regulador: <em>pros oikodomen</em> — para edificação. A ordem (<em>taxis</em>) e a decência (<em>euschemonos</em>) são características do Deus que não é de confusão (14:33).")
        ])),
    15: ("A Ressurreição — Fundamento do Evangelho", "Mas agora Cristo ressuscitou dentre os mortos, e foi feito as primícias dos que dormem.", "1Cor 15:20",
        intro("1 Coríntios 15 é o capítulo mais extenso sobre a ressurreição no NT. Paulo defende a ressurreição corporal de Cristo e dos crentes contra os que negavam a ressurreição.") +
        bloco("✝️ O Evangelho e as Aparições (15:1-11)", [
            ("1Cor 15:3-8", "Porque primeiramente vos entreguei o que também recebi: que Cristo morreu pelos nossos pecados, segundo as Escrituras; e que foi sepultado, e que ressuscitou ao terceiro dia, segundo as Escrituras; e que apareceu a Cefas, e depois aos doze.",
             "A fórmula mais antiga do Evangelho no NT (~35 d.C., dentro de 5 anos da crucificação). Quatro elementos: (1) Cristo morreu pelos nossos pecados; (2) foi sepultado; (3) ressuscitou ao terceiro dia; (4) apareceu. As aparições são a evidência histórica: Cefas, os Doze, 500 irmãos, Tiago, todos os apóstolos, Paulo.")
        ]) +
        bloco("⭐ Se Cristo não Ressuscitou (15:12-34)", [
            ("1Cor 15:17-19", "E, se Cristo não ressuscitou, a vossa fé é vã; ainda estais nos vossos pecados. E também os que dormiram em Cristo pereceram. Se esperamos em Cristo somente nesta vida, somos os mais miseráveis de todos os homens.",
             "A lógica implacável de Paulo: se não há ressurreição, então Cristo não ressuscitou; se Cristo não ressuscitou, o Evangelho é falso, a fé é vã, os mortos pereceram, e os cristãos são os mais miseráveis. A ressurreição não é um detalhe opcional — é o fundamento de tudo.")
        ]) +
        bloco("🌟 O Corpo Ressurreto (15:35-58)", [
            ("1Cor 15:42-44", "Assim também a ressurreição dos mortos. Semeia-se em corrupção, ressuscitará em incorrupção; semeia-se em desonra, ressuscitará em glória; semeia-se em fraqueza, ressuscitará em poder; semeia-se corpo natural, ressuscitará corpo espiritual.",
             "Quatro contrastes: corrupção/incorrupção, desonra/glória, fraqueza/poder, natural/espiritual. O corpo ressurreto é real e material (como o de Cristo ressurreto), mas transformado e glorificado. <em>Soma pneumatikon</em> não é corpo imaterial — é corpo animado pelo Espírito."),
            ("1Cor 15:54-58", "Então se cumprirá a palavra que está escrita: Absorvida foi a morte na vitória. Onde está, ó morte, o teu aguilhão?... Mas graças a Deus, que nos dá a vitória por nosso Senhor Jesus Cristo.",
             "O grito de triunfo sobre a morte. O 'aguilhão' (<em>kentron</em>) da morte é o pecado; a força do pecado é a lei. Cristo, ao satisfazer a lei e vencer o pecado, tirou o aguilhão da morte. A conclusão prática: 'sede firmes e constantes, sempre abundando na obra do Senhor' — a ressurreição motiva a ação presente.")
        ])),
    16: ("Coleta, Planos e Saudações Finais", "Vigiai, estai firmes na fé, portai-vos varonilmente, e fortalecei-vos.", "1Cor 16:13",
        intro("1 Coríntios 16 encerra a carta com instruções práticas sobre a coleta para Jerusalém, planos de viagem de Paulo, e saudações finais.") +
        bloco("💰 A Coleta para os Santos (16:1-4)", [
            ("1Cor 16:1-3", "Ora, quanto à coleta para os santos, fazei vós também como ordenei às igrejas da Galácia. No primeiro dia da semana, cada um de vós ponha de parte o que puder juntar, segundo a sua prosperidade.",
             "A coleta para os pobres de Jerusalém (Rm 15:26; 2Cor 8-9) é a primeira referência ao culto no primeiro dia da semana como prática estabelecida. O princípio: sistemático ('no primeiro dia'), proporcional ('segundo a sua prosperidade'), voluntário ('o que puder juntar').")
        ]) +
        bloco("🌟 Exortações Finais (16:13-24)", [
            ("1Cor 16:13-14", "Vigiai, estai firmes na fé, portai-vos varonilmente, e fortalecei-vos. Todas as vossas coisas sejam feitas com amor.",
             "Cinco imperativos militares seguidos de um imperativo de amor. A vida cristã requer vigilância, firmeza, coragem e força — mas tudo deve ser feito em amor. O amor de 1Cor 13 não é passividade — é a motivação de toda ação corajosa.")
        ])),
}

def gerar_1corintios():
    for num, (titulo, vk, rk, body) in corintios1_caps.items():
        html = page("1 Coríntios", num, 16, titulo, vk, rk, body, "1corintios", "../../../..")
        salvar("1corintios", num, html)
    print("✅ 1 Coríntios: 16 capítulos gerados")

# ─────────────────────────────────────────────
# FUNÇÃO PRINCIPAL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    gerar_romanos()
    gerar_1corintios()
    print("\n🎉 Fase 1 concluída: Romanos + 1 Coríntios = 32 capítulos aprofundados")
