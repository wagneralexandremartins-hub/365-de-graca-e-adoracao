#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera todos os capítulos aprofundados das Epístolas Paulinas e Gerais
Romanos, 1-2 Coríntios, Gálatas, Efésios, Filipenses, Colossenses,
1-2 Tessalonicenses, 1-2 Timóteo, Tito, Filemon, Hebreus,
Tiago, 1-2 Pedro, 1-2-3 João, Judas
"""

import os

BASE_NT = "/home/ubuntu/365-de-graca-e-adoracao/08-novo-testamento"

def html_cap(livro, num, total, titulo, vk, rk, conteudo, path_prefix="../../.."):
    prev_link = f"capitulo-{num-1:02d}.html" if num > 1 else "../index.html"
    prev_label = f"← {livro} {num-1}" if num > 1 else "← Índice"
    next_link = f"capitulo-{num+1:02d}.html" if num < total else "../index.html"
    next_label = f"{livro} {num+1} →" if num < total else "Índice →"
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{livro} {num} — {titulo} | 365 de Graça & Adoração</title>
  <meta name="description" content="Estudo aprofundado de {livro} {num}: {titulo}. Análise versículo por versículo, vocabulário grego, contexto histórico e teologia.">
  <meta property="og:title" content="{livro} {num} — {titulo}">
  <meta property="og:description" content="{vk[:120]}">
  <link rel="stylesheet" href="{path_prefix}/assets/css/style.css">
  <link rel="stylesheet" href="{path_prefix}/assets/css/bloco.css">
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
    <a href="/">Início</a> › <a href="/08-novo-testamento/">NT</a> › <a href="../">{ livro}</a> › Cap. {num}
  </div>
  <div class="chapter-hero">
    <div class="chapter-number">{livro} {num}</div>
    <h1>{titulo}</h1>
    <p class="chapter-subtitle">{vk}</p>
    <p class="chapter-ref">— {rk}</p>
  </div>
  <div class="wrap">
{conteudo}
  </div>
  <nav class="chapter-nav">
    <a href="{prev_link}">{prev_label}</a>
    <a href="../index.html">Índice de {livro}</a>
    <a href="{next_link}">{next_label}</a>
  </nav>
  <footer class="site-footer">
    <p>365 de Graça &amp; Adoração • Da Criação ao Apocalipse • © 2026</p>
  </footer>
</body>
</html>"""

def sec(titulo, versiculos):
    """Gera uma seção com versículos"""
    html = f'    <div class="section-block">\n      <h2>{titulo}</h2>\n'
    for ref, texto, analise in versiculos:
        html += f"""      <div class="versiculo-bloco">
        <div class="ref-v">{ref}</div>
        <div class="texto-v">"{texto}"</div>
        <div class="analise-v">{analise}</div>
      </div>
"""
    html += "    </div>\n"
    return html

def intro(texto):
    return f'    <div class="section-block">\n      <p>{texto}</p>\n    </div>\n'

def salvar(livro_dir, num, html):
    path = os.path.join(BASE_NT, livro_dir, "capitulos", f"capitulo-{num:02d}.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

# ==============================================================
# ROMANOS — 16 capítulos
# ==============================================================
def gerar_romanos():
    caps = [
        (1, "O Evangelho e a Depravação Humana",
         "Porque não me envergonho do evangelho de Cristo, pois é o poder de Deus para a salvação.",
         "Romanos 1:16",
         intro("Romanos é a carta mais sistemática de Paulo, escrita ~57 d.C. em Corinto. O cap. 1 apresenta o tema central: o Evangelho como poder de Deus para a salvação, e a necessidade universal de salvação revelada pela ira de Deus sobre a depravação humana.") +
         sec("⚡ O Tema Central: O Evangelho (1:16-17)", [
             ("Romanos 1:16-17", "Porque não me envergonho do evangelho de Cristo, pois é o poder de Deus para a salvação de todo aquele que crê; primeiro do judeu, e também do grego. Porque nele a justiça de Deus se revela de fé em fé; como está escrito: O justo viverá pela fé.",
              "A <em>propositio</em> de toda a carta. <em>Dynamis theou</em> — poder de Deus: o Evangelho não é apenas informação, é poder transformador. <em>Dikaiosyne theou</em> — justiça de Deus: não a justiça que Deus exige de nós, mas a que ele provê para nós em Cristo. <em>Ek pisteos eis pistin</em> — de fé em fé: a salvação é inteiramente pela fé. A citação de Habacuque 2:4 desencadeou a Reforma Protestante — Lutero entendeu que a justiça de Deus é um dom recebido pela fé, não uma exigência a ser cumprida.")
         ]) +
         sec("🔥 A Ira de Deus e a Depravação Humana (1:18-32)", [
             ("Romanos 1:18-20", "Porque do céu se manifesta a ira de Deus sobre toda a impiedade e injustiça dos homens que detêm a verdade em injustiça. Porquanto o que de Deus se pode conhecer é manifesto entre eles, porque Deus lho manifestou. Porque as suas perfeições invisíveis, desde a criação do mundo, tanto o seu eterno poder como a sua divindade, se entendem e claramente se veem nas coisas que foram criadas; de modo que eles são inescusáveis.",
              "A <em>orge theou</em> não é reação emocional — é resposta santa à violação da ordem moral. A revelação natural: todo ser humano tem acesso ao conhecimento de Deus pela criação. <em>Anapologetous</em> — inescusáveis: o problema humano não é falta de informação, é supressão da informação. <em>Katechonton</em> — suprimir, abafar a verdade."),
             ("Romanos 1:24-28", "Por isso Deus os entregou... Deus os entregou... Deus os entregou...",
              "A repetição tripla de <em>paredoken autous ho theos</em> é o coração desta seção. A ira de Deus opera no presente como abandono judicial. Deus não força ao pecado — ele remove a restrição. As três entregas: (1) às impurezas — desordem sexual; (2) às paixões infames — inversão da ordem criacional; (3) à mente reprovada — catálogo de 21 vícios sociais.")
         ])),
        (2, "O Julgamento Justo de Deus",
         "Ou desprezas as riquezas da sua benignidade, tolerância e longanimidade, ignorando que a benignidade de Deus te leva ao arrependimento?",
         "Romanos 2:4",
         intro("Romanos 2 confronta o moralista e o judeu religioso. Após condenar os gentios, Paulo vira a mesa: ninguém escapa do julgamento, porque o critério não é o conhecimento da lei, mas a obediência a ela.") +
         sec("⚖️ O Julgamento Imparcial de Deus (2:1-16)", [
             ("Romanos 2:1-4", "Portanto, és inescusável, ó homem, quem quer que sejas tu que julgas; pois no que julgas a outro, a ti mesmo te condenas, porque tu que julgas praticas as mesmas coisas.",
              "A <em>diatribe</em> retórica: Paulo se dirige ao moralista que concordou com a condenação do cap. 1. A bondade de Deus (<em>chrestotes</em>), tolerância (<em>anoche</em>) e longanimidade (<em>makrothymia</em>) são convites ao arrependimento, não aprovação do pecado."),
             ("Romanos 2:14-16", "Porque quando os gentios, que não têm lei, fazem por natureza as coisas que são da lei, esses, não tendo lei, são lei para si mesmos; pois mostram a obra da lei escrita em seus corações, testificando também a sua consciência.",
              "A lei natural e a consciência (<em>syneidesis</em>): os gentios têm a obra da lei escrita no coração. A consciência não salva — ela condena, porque ninguém a obedece perfeitamente. Base bíblica para a lei natural (Tomás de Aquino) e para a responsabilidade moral universal.")
         ]) +
         sec("✡️ O Judeu e a Hipocrisia Religiosa (2:17-29)", [
             ("Romanos 2:28-29", "Porque não é judeu o que o é exteriormente, nem é circuncisão a que o é exteriormente, na carne. Mas é judeu o que o é interiormente, e circuncisão é a do coração, em espírito, não em letra.",
              "A verdadeira circuncisão é a do coração (<em>peritome kardias</em>), prometida em Dt 30:6 e Jr 4:4. Paulo não aboliu a identidade judaica — redefiniu-a em termos de transformação interna pelo Espírito. Prepara o caminho para Romanos 4 (Abraão) e 9-11 (Israel).")
         ])),
        (3, "Todos Culpados — A Justificação pela Fé",
         "Sendo justificados gratuitamente pela sua graça, pela redenção que há em Cristo Jesus.",
         "Romanos 3:24",
         intro("Romanos 3 é o coração teológico da carta. Os versículos 21-26 — 'o coração do Evangelho' — apresentam a justificação pela fé na obra expiatória de Cristo. Após provar a culpa universal, Paulo apresenta a solução divina.") +
         sec("🌍 Todos Sob o Pecado (3:9-20)", [
             ("Romanos 3:9-12", "Que, pois? Somos nós melhores do que eles? De modo nenhum; porque já dantes demonstramos que, tanto judeus como gregos, todos estão debaixo do pecado. Como está escrito: Não há um justo, nem um sequer.",
              "Cadeia de citações do AT (Sl 14; 53; 5; 140; 10; Is 59; Sl 36) provando que a condenação universal é testemunho das próprias Escrituras judaicas. <em>Ouk estin dikaios oude heis</em> — absoluto e universal. 'Não há nenhum que busque a Deus' — a busca religiosa humana não é busca por Deus, é busca por um deus que sirva aos nossos propósitos."),
             ("Romanos 3:19-20", "Porque pelas obras da lei nenhuma carne será justificada diante dele; em razão de que pela lei vem o conhecimento do pecado.",
              "A lei fecha toda a boca (<em>phtariston pan stoma</em>). Sua função não é justificar — é condenar e revelar o pecado em toda a sua gravidade. Esta conclusão sombria é necessária para que a boa nova de 3:21-26 seja verdadeiramente boa.")
         ]) +
         sec("⭐ O Coração do Evangelho: Justificação pela Fé (3:21-26)", [
             ("Romanos 3:21-24", "Mas agora, independentemente da lei, a justiça de Deus se manifestou... sendo justificados gratuitamente pela sua graça, pela redenção que há em Cristo Jesus.",
              "O 'mas agora' (<em>nyni de</em>) é a virada mais dramática da teologia bíblica. Quatro palavras-chave: (1) <em>dikaiosyne theou</em> — justiça provida por Deus; (2) <em>dia pisteos</em> — pela fé; (3) <em>dorean</em> — gratuitamente; (4) <em>apolytrosis</em> — redenção, libertação mediante resgate."),
             ("Romanos 3:25-26", "Ao qual Deus propôs como propiciação pela fé no seu sangue... para ser ele justo e justificador daquele que tem fé em Jesus.",
              "<em>Hilasterion</em> — propiciação: Jesus é o novo Propiciatório, o lugar onde a ira de Deus é satisfeita. A cruz resolve o problema teológico: como pode Deus ser justo (punindo o pecado) e justificador (absolvendo o pecador)? Na cruz, Deus puniu o pecado em Cristo — assim é <em>dikaion</em> (justo) e <em>dikaiounta</em> (justificador) simultaneamente.")
         ])),
        (4, "Abraão: O Pai da Fé",
         "Abraão creu em Deus, e isso lhe foi imputado como justiça.",
         "Romanos 4:3",
         intro("Romanos 4 usa Abraão como prova histórica da justificação pela fé. Paulo demonstra que Abraão foi justificado antes da circuncisão e antes da lei — portanto pela fé, não pelas obras.") +
         sec("🌟 Abraão Justificado pela Fé (4:1-12)", [
             ("Romanos 4:2-5", "Porque se Abraão foi justificado pelas obras, tem de que se gloriar, mas não diante de Deus. Pois que diz a Escritura? E creu Abraão em Deus, e isso lhe foi imputado como justiça.",
              "<em>Logizomai</em> — imputar, creditar (termo contábil): a justiça de Cristo é creditada na conta do crente. Abraão foi justificado (Gn 15:6) antes da circuncisão (Gn 17 — intervalo de ~14 anos) e antes da lei (430 anos antes — Gl 3:17). Portanto, é pai tanto dos incircuncisos que creem quanto dos circuncisos que seguem seus passos de fé."),
         ]) +
         sec("⭐ A Promessa pela Fé (4:13-25)", [
             ("Romanos 4:20-25", "E não duvidou da promessa de Deus por incredulidade; antes foi fortalecido na fé, dando glória a Deus, e estando plenamente certo de que o que Deus tinha prometido era também poderoso para o cumprir.",
              "A fé de Abraão não foi fé cega — foi fé informada pela promessa. Ele considerou seu corpo 'mortificado' (~100 anos) e o ventre de Sara 'morto' — e ainda assim creu. Esta fé 'deu glória a Deus' (<em>edoxasen ton theon</em>). A aplicação: a mesma fé que creu na promessa da descendência agora crê na ressurreição de Cristo — e a mesma imputação de justiça se aplica.")
         ])),
        (5, "Paz com Deus e o Dom da Graça",
         "Justificados, pois, pela fé, temos paz com Deus por nosso Senhor Jesus Cristo.",
         "Romanos 5:1",
         intro("Romanos 5 apresenta os frutos da justificação (paz, esperança, amor — 5:1-11) e o paralelo teológico fundamental entre Adão e Cristo como representantes da humanidade (5:12-21).") +
         sec("☮️ Os Frutos da Justificação (5:1-11)", [
             ("Romanos 5:1-5", "Justificados, pois, pela fé, temos paz com Deus... E não somente isso, mas também nos gloriamos nas tribulações; sabendo que a tribulação produz a paciência, e a paciência a experiência, e a experiência a esperança.",
              "Cinco frutos da justificação: (1) <em>eirene pros ton theon</em> — paz com Deus (fim do estado de guerra); (2) acesso à graça; (3) esperança da glória; (4) glória nas tribulações; (5) amor de Deus derramado pelo Espírito. A cadeia tribulação → paciência (<em>hypomone</em>) → experiência (<em>dokime</em>) → esperança é a pedagogia divina do sofrimento."),
             ("Romanos 5:8", "Mas Deus prova o seu amor para conosco, em que Cristo morreu por nós, sendo nós ainda pecadores.",
              "A prova do amor de Deus é histórica e específica: Cristo morreu pelos ímpios, pelos pecadores, pelos inimigos. A lógica <em>a fortiori</em>: se Deus amou tanto quando éramos inimigos, quanto mais nos salvará agora que somos filhos?")
         ]) +
         sec("👥 Adão e Cristo: Dois Representantes (5:12-21)", [
             ("Romanos 5:12", "Portanto, como por um homem entrou o pecado no mundo, e pelo pecado a morte, assim também a morte passou a todos os homens, por isso que todos pecaram.",
              "Base bíblica do pecado original. <em>Eph ho pantes hemarton</em> — 'por isso que todos pecaram': todos pecaram em Adão (pecado imputado). A morte reinou mesmo sobre os que não pecaram 'à semelhança da transgressão de Adão' — o que só faz sentido se o pecado de Adão foi imputado a eles."),
             ("Romanos 5:15-19", "Porque, assim como pela desobediência de um homem muitos foram constituídos pecadores, assim também pela obediência de um muitos serão constituídos justos.",
              "O paralelo Adão-Cristo: o pecado de Adão imputado a todos; a justiça de Cristo imputada a todos que creem. Mas há assimetria: a graça é muito mais abundante (<em>perisseuein</em>). A obediência ativa de Cristo (vida perfeita) e passiva (morte substitutiva) são ambas necessárias para nossa justificação.")
         ])),
        (6, "Mortos para o Pecado, Vivos em Cristo",
         "Assim também vós considerai-vos mortos para o pecado, mas vivos para Deus em Cristo Jesus.",
         "Romanos 6:11",
         intro("Romanos 6 responde à objeção antinomiana ('devemos pecar para que a graça abunde?') com a doutrina da morte e ressurreição com Cristo no batismo, e a transferência da escravidão do pecado para a escravidão da justiça.") +
         sec("💀 Mortos com Cristo no Batismo (6:1-14)", [
             ("Romanos 6:1-4", "Que diremos, pois? Permaneceremos no pecado para que a graça abunde? De modo nenhum! Nós, que estamos mortos para o pecado, como viveremos ainda nele? Fomos, pois, sepultados com ele pelo batismo na morte.",
              "A resposta à objeção antinomiana é ontológica: o crente está morto para o pecado. O batismo simboliza e sela a união com Cristo na morte e ressurreição. A 'novidade de vida' (<em>kainoteti zoes</em>) não é possibilidade — é realidade que deve ser vivida."),
             ("Romanos 6:11", "Assim também vós considerai-vos mortos para o pecado, mas vivos para Deus em Cristo Jesus.",
              "<em>Logizesthe</em> — considerai, contai como realidade: Paulo não diz 'tornai-vos mortos' mas 'considerai-vos mortos' — a morte ao pecado já é realidade em Cristo; o imperativo é apropriar-se dela pela fé. Santificação é viver a realidade da nossa posição em Cristo.")
         ]) +
         sec("⚡ Escravos da Justiça (6:15-23)", [
             ("Romanos 6:22-23", "Mas agora, libertados do pecado e feitos servos de Deus, tendes o vosso fruto para a santificação, e por fim a vida eterna. Porque o salário do pecado é a morte, mas o dom gratuito de Deus é a vida eterna, em Cristo Jesus nosso Senhor.",
              "O contraste final: o pecado paga (<em>opsonia</em> — salário militar) com morte; Deus dá (<em>charisma</em> — dom gratuito) vida eterna. A liberdade cristã não é autonomia — é transferência de senhor. Mas a diferença é absoluta: um senhor mata, o outro dá vida.")
         ])),
        (7, "A Luta Interior — Lei, Pecado e o Eu",
         "Miserável homem que sou! Quem me livrará do corpo desta morte?",
         "Romanos 7:24",
         intro("Romanos 7 é um dos capítulos mais debatidos da Bíblia. Paulo descreve a função da lei (revelar o pecado, não salvar), a luta interior do crente com a carne, e o grito de angústia que é respondido com ação de graças em Cristo.") +
         sec("📜 Libertos da Lei (7:1-6)", [
             ("Romanos 7:4-6", "Assim, meus irmãos, também vós fostes mortos para a lei pelo corpo de Cristo... Mas agora estamos livres da lei, tendo morrido para aquilo em que estávamos retidos; de sorte que servimos em novidade de espírito, e não na velhice da letra.",
              "A analogia do casamento: a morte dissolve o vínculo matrimonial; a morte de Cristo dissolve o vínculo da lei sobre o crente. Liberdade da lei não é antinomismo — é servir a Deus 'em novidade de espírito' (<em>kainoteti pneumatos</em>), a lei cumprida pelo Espírito de dentro para fora.")
         ]) +
         sec("⚔️ A Luta Interior (7:15-25)", [
             ("Romanos 7:15-20", "Porque o que faço, não o aprovo; pois não faço o que quero, mas o que odeio, isso faço... Porque não faço o bem que quero, mas o mal que não quero, esse faço.",
              "A divisão interna — querer o bem mas fazer o mal — é característica da regeneração, não da escravidão irrefletida. O incrédulo não tem esse conflito porque não tem o Espírito que ama a lei de Deus (7:22). Este é o crente regenerado que ainda luta com a carne."),
             ("Romanos 7:24-25", "Miserável homem que sou! Quem me livrará do corpo desta morte? Graças a Deus por Jesus Cristo nosso Senhor!",
              "O grito de angústia é respondido imediatamente com ação de graças — a libertação já foi provida em Cristo. O 'corpo desta morte' (<em>soma tou thanatou toutou</em>) alude à prática romana de amarrar um cadáver ao assassino. O pecado é como um cadáver amarrado — presente, pesado, corrompendo. Mas Cristo liberta. O cap. 8 é a resposta gloriosa.")
         ])),
        (8, "Vida no Espírito — O Capítulo da Glória",
         "Nenhuma condenação há, pois, para os que estão em Cristo Jesus.",
         "Romanos 8:1",
         intro("Romanos 8 é o capítulo mais glorioso da Bíblia — a resposta ao grito de 7:24. Nenhuma condenação, vida no Espírito, adoção como filhos, gemência da criação, intercessão do Espírito, e o amor invencível de Deus em Cristo.") +
         sec("🕊️ Nenhuma Condenação — Vida no Espírito (8:1-17)", [
             ("Romanos 8:1-4", "Nenhuma condenação há, pois, para os que estão em Cristo Jesus... Porque a lei do Espírito de vida, em Cristo Jesus, me livrou da lei do pecado e da morte.",
              "<em>Ouden ara nyn katakrima</em> — 'Nenhuma condenação, pois, agora': declaração presente, não apenas futura. O que a lei mosaica não pôde fazer (enfraquecida pela carne), Deus fez: enviou seu Filho para condenar o pecado na carne — na encarnação e na cruz, o pecado foi julgado definitivamente."),
             ("Romanos 8:14-17", "Porque não recebestes o espírito de escravidão para viverdes de novo em temor, mas recebestes o espírito de adoção, pelo qual clamamos: Aba, Pai!",
              "A adoção (<em>hyiothesia</em>): o Espírito nos habilita a clamar 'Aba, Pai' — a palavra íntima que Jesus usou em Getsêmani. O Espírito testifica <em>com</em> (<em>symmartyreo</em>) nosso espírito. Filhos → herdeiros → co-herdeiros com Cristo: a herança inclui tanto o sofrimento quanto a glória.")
         ]) +
         sec("🌟 Glória Futura e Amor Invencível (8:18-39)", [
             ("Romanos 8:18", "Porque para mim tenho por certo que as aflições do tempo presente não são para comparar com a glória que em nós há de ser revelada.",
              "A esperança cristã é proporcional: as aflições presentes são reais, mas incomparáveis com a glória futura. Toda a criação geme (<em>systenazei</em>) aguardando a manifestação dos filhos de Deus. A redenção final é cósmica — novo céu e nova terra (Ap 21-22) respondem à gemência da criação."),
             ("Romanos 8:28", "E sabemos que todas as coisas contribuem juntamente para o bem daqueles que amam a Deus, daqueles que são chamados segundo o seu propósito.",
              "<em>Panta synergei eis agathon</em> — todas as coisas cooperam para o bem. Não otimismo ingênuo — afirmação teológica: para os chamados segundo o propósito divino, até sofrimento, perda e dor são instrumentos da providência. A 'cadeia de ouro' (8:29-30): pré-conheceu → predestinou → chamou → justificou → glorificou."),
             ("Romanos 8:35-39", "Quem nos separará do amor de Cristo?... Porque estou persuadido de que nem a morte, nem a vida, nem os anjos, nem os principados... nos poderá separar do amor de Deus, que está em Cristo Jesus nosso Senhor.",
              "O clímax de Romanos 8. Lista de 10 poderes que não podem separar o crente do amor de Deus: morte, vida, anjos, principados, potestades, presente, futuro, altura, profundidade, 'alguma outra criatura'. <em>Hypernikomen</em> — mais do que vencedores: não apenas vencemos, mas vencemos com sobra, com glória.")
         ])),
        (9, "A Soberania de Deus e a Eleição de Israel",
         "Não depende, pois, do que quer nem do que corre, mas de Deus, que usa de misericórdia.",
         "Romanos 9:16",
         intro("Romanos 9-11 é a seção mais profunda sobre a soberania divina e o destino de Israel. O cap. 9 trata da eleição soberana de Deus — não baseada em obras humanas, mas na vontade divina.") +
         sec("💔 A Angústia de Paulo por Israel (9:1-5)", [
             ("Romanos 9:1-5", "Digo a verdade em Cristo, não minto, dando-me testemunho a minha consciência no Espírito Santo, que tenho grande tristeza e contínua dor no meu coração. Porque eu mesmo desejaria ser anátema, separado de Cristo, por amor de meus irmãos, meus parentes segundo a carne.",
              "A angústia de Paulo por Israel é genuína e profunda — ele desejaria ser amaldiçoado (<em>anathema</em>) se isso salvasse seu povo. Isto reflete o coração de Moisés (Êx 32:32) e antecipa o coração de Cristo que morreu pelos seus. Os privilégios de Israel listados (9:4-5) são extraordinários: adoção, glória, alianças, lei, culto, promessas, patriarcas, e de quem é Cristo segundo a carne.")
         ]) +
         sec("⚡ A Soberania Divina na Eleição (9:6-29)", [
             ("Romanos 9:10-16", "E não somente isso, mas também Rebeca, quando concebeu de um só, de Isaque, nosso pai; porque, não tendo eles ainda nascido, nem tendo feito bem ou mal... foi-lhe dito: O mais velho servirá ao mais novo... Não depende, pois, do que quer nem do que corre, mas de Deus, que usa de misericórdia.",
              "A eleição de Jacó sobre Esaú antes do nascimento — sem base em obras — prova que a eleição divina não é baseada no mérito humano. <em>Ou tou thelontos oude tou trechontos alla tou eleountos theou</em> — não do que quer nem do que corre, mas de Deus que usa de misericórdia. A soberania de Deus na eleição não é arbitrariedade — é misericórdia além do que merecemos."),
             ("Romanos 9:20-21", "Mas, ó homem, quem és tu para altercar com Deus? Porventura dirá o barro ao que o formou: Por que me fizeste assim? Ou não tem o oleiro poder sobre o barro, para do mesmo barro fazer um vaso para honra e outro para desonra?",
              "A metáfora do oleiro (Is 29:16; 45:9; Jr 18:1-10) não ensina que Deus cria pessoas para a condenação — ensina que Deus tem o direito soberano de usar suas criaturas como lhe apraz. A resposta de Paulo à objeção não é uma explicação filosófica — é uma reorientação: quem somos nós para questionar o Criador?")
         ])),
        (10, "Israel, a Fé e a Pregação do Evangelho",
         "Se confessares com a tua boca o Senhor Jesus, e creres no teu coração que Deus o ressuscitou dos mortos, serás salvo.",
         "Romanos 10:9",
         intro("Romanos 10 explica por que Israel, tendo o zêlo por Deus, não alcançou a justiça — porque buscou a justiça pelas obras e não pela fé. E apresenta a cadeia da salvação: ouvir, crer, confessar.") +
         sec("✡️ O Zêlo sem Conhecimento (10:1-13)", [
             ("Romanos 10:2-4", "Porque lhes dou testemunho de que têm zêlo de Deus, mas não com entendimento. Porque, ignorando a justiça de Deus e procurando estabelecer a sua própria justiça, não se sujeitaram à justiça de Deus. Porque o fim da lei é Cristo, para justificação de todo aquele que crê.",
              "O problema de Israel não é falta de religiosidade — é zêlo sem conhecimento (<em>kat epignosin</em>). Eles procuram estabelecer sua própria justiça (<em>idian dikaiosynen</em>) em vez de se sujeitar à justiça de Deus. Cristo é o <em>telos</em> da lei — o alvo, o cumprimento, o fim para o qual a lei sempre apontou."),
             ("Romanos 10:9-13", "Se confessares com a tua boca o Senhor Jesus, e creres no teu coração que Deus o ressuscitou dos mortos, serás salvo. Porque com o coração se crê para a justiça, e com a boca se faz confissão para a salvação... Porque todo aquele que invocar o nome do Senhor será salvo.",
              "A fórmula da salvação: crença no coração (<em>kardia</em>) + confissão com a boca (<em>stoma</em>). A confissão '<em>Kyrios Iesous</em>' — 'Jesus é Senhor' — era a declaração mais radical no mundo romano, onde '<em>Kyrios Kaisar</em>' era a lealdade exigida. Invocar o nome do Senhor (citação de Jl 2:32) é agora invocar Jesus — Paulo aplica um texto sobre YHWH a Jesus.")
         ]) +
         sec("📢 A Cadeia da Pregação (10:14-21)", [
             ("Romanos 10:14-17", "Como, pois, invocarão aquele em quem não creram? E como crerão naquele de quem não ouviram? E como ouvirão, se não há quem pregue? E como pregarão, se não forem enviados?... Logo a fé é pelo ouvir, e o ouvir pela palavra de Cristo.",
              "A cadeia missionária em ordem reversa: salvação ← invocação ← fé ← ouvir ← pregação ← envio. <em>Pistis ex akoes</em> — a fé vem pelo ouvir (<em>akoe</em>). A missão não é opcional — é a cadeia que liga o envio à salvação. Sem pregação, sem fé; sem fé, sem salvação.")
         ])),
        (11, "O Mistério de Israel — Endurecimento e Restauração",
         "Assim todo o Israel será salvo, como está escrito: De Sião virá o Libertador.",
         "Romanos 11:26",
         intro("Romanos 11 revela o 'mistério' (<em>mysterion</em>) do plano de Deus para Israel: o endurecimento parcial de Israel é temporário e serve ao propósito de incluir os gentios; ao final, 'todo o Israel será salvo'.") +
         sec("🌿 O Remanescente e o Endurecimento (11:1-10)", [
             ("Romanos 11:1-5", "Digo, pois: Rejeitou Deus o seu povo? De modo nenhum! Porque também eu sou israelita, da descendência de Abraão, da tribo de Benjamim... Assim também neste tempo presente ficou um remanescente, segundo a eleição da graça.",
              "Paulo responde com sua própria existência: ele é judeu e foi salvo. O remanescente (<em>leimma</em>) de Israel que crê em Cristo é a continuidade do verdadeiro Israel. A eleição da graça (<em>kat eklogon charitos</em>) exclui as obras — se fosse pelas obras, não seria graça.")
         ]) +
         sec("🌳 A Oliveira — Gentios Enxertados (11:11-24)", [
             ("Romanos 11:17-21", "Mas se alguns dos ramos foram quebrados, e tu, sendo oliveira brava, foste enxertado no lugar deles, e te fizeste participante da raiz e da seiva da oliveira, não te glories contra os ramos. E se te gloriares, sabe que não és tu que sustentas a raiz, mas a raiz a ti.",
              "A metáfora da oliveira: Israel é a oliveira cultivada; os gentios são ramos de oliveira brava enxertados. Os ramos naturais (judeus incrédulos) foram quebrados por incredulidade; os ramos selvagens (gentios) foram enxertados por fé. Advertência aos gentios: não se orgulhem — vocês são sustentados pela raiz (as promessas a Israel), não o contrário.")
         ]) +
         sec("🌟 O Mistério e a Doxologia (11:25-36)", [
             ("Romanos 11:25-26", "Porque não quero, irmãos, que ignoreis este mistério, para que não sejais presumidos em vós mesmos: que o endurecimento em parte aconteceu a Israel, até que a plenitude dos gentios haja entrado. E assim todo o Israel será salvo.",
              "O <em>mysterion</em> (segredo revelado): o endurecimento de Israel é parcial ('em parte') e temporário ('até que'). A 'plenitude dos gentios' (<em>pleroma ton ethnon</em>) é o número completo dos gentios eleitos. 'Todo o Israel será salvo' — interpretado como: (1) a nação Israel como um todo no final dos tempos; (2) o Israel espiritual (todos os eleitos). A doxologia final (11:33-36) é a resposta adequada à profundidade do plano de Deus: 'Ó profundidade das riquezas, tanto da sabedoria como da ciência de Deus!'")
         ])),
        (12, "Sacrifício Vivo — Ética do Reino",
         "Apresentai os vossos corpos em sacrifício vivo, santo e agradável a Deus, que é o vosso culto racional.",
         "Romanos 12:1",
         intro("Romanos 12 marca a transição da teologia (caps. 1-11) para a ética (caps. 12-16). A vida cristã é uma resposta de gratidão à misericórdia de Deus — um sacrifício vivo que transforma a mente e se manifesta em amor prático.") +
         sec("🙏 O Sacrifício Vivo e a Transformação da Mente (12:1-2)", [
             ("Romanos 12:1-2", "Rogo-vos, pois, irmãos, pela compaixão de Deus, que apresenteis os vossos corpos em sacrifício vivo, santo e agradável a Deus, que é o vosso culto racional. E não vos conformeis com este século, mas transformai-vos pela renovação do vosso entendimento.",
              "O 'pois' (<em>oun</em>) conecta a ética à teologia: a vida cristã é resposta à misericórdia de Deus (caps. 1-11). <em>Thysian zosan</em> — sacrifício vivo: ao contrário do sacrifício animal que morria, o cristão vive para Deus. <em>Logiken latreian</em> — culto racional/espiritual: a adoração não é apenas ritual — é a vida inteira oferecida a Deus. <em>Metamorphousthe</em> — transformai-vos (de onde vem 'metamorfose'): a renovação da mente (<em>anakainosis tou noos</em>) é o processo contínuo de santificação.")
         ]) +
         sec("💝 Amor Prático na Comunidade (12:3-21)", [
             ("Romanos 12:9-13", "O amor seja sem fingimento. Aborrecei o mal e apegai-vos ao bem. Amai-vos cordialmente uns aos outros com amor fraternal... No amor fraternal, amai-vos uns aos outros; na honra, preferindo-vos uns aos outros.",
              "A ética cristã começa com o amor sem fingimento (<em>anypokritos</em> — sem máscara, sem hipocrisia). A lista de virtudes em 12:9-21 é uma das mais completas do NT: amor fraternal, honra mútua, fervor no espírito, alegria na esperança, paciência na tribulação, perseverança na oração, hospitalidade, bênção aos perseguidores, empatia, humildade."),
             ("Romanos 12:19-21", "Não vos vingueis a vós mesmos, amados, mas dai lugar à ira de Deus; porque está escrito: A mim pertence a vingança; eu recompensarei, diz o Senhor. Portanto, se o teu inimigo tiver fome, dá-lhe de comer; se tiver sede, dá-lhe de beber... Não te deixes vencer do mal, mas vence o mal com o bem.",
              "A ética do não-retaliar é revolucionária no mundo antigo. A citação de Dt 32:35 e Pv 25:21-22 fundamenta a não-vingança: a vingança pertence a Deus — ao deixar para Deus, o cristão não está sendo passivo, mas confiando na justiça divina. 'Vencer o mal com o bem' (<em>nika en to agatho to kakon</em>) é a estratégia cristã de transformação social.")
         ])),
        (13, "Autoridades, Amor e a Armadura da Luz",
         "Não devais nada a ninguém, exceto o amor com que vos ameis uns aos outros.",
         "Romanos 13:8",
         intro("Romanos 13 trata da relação com as autoridades civis, do amor como cumprimento da lei, e da urgência escatológica que motiva a vida cristã.") +
         sec("🏛️ Submissão às Autoridades (13:1-7)", [
             ("Romanos 13:1-4", "Toda alma esteja sujeita às potestades superiores; porque não há potestade que não venha de Deus; e as potestades que há foram ordenadas por Deus. Por isso quem resiste à potestade resiste à ordenação de Deus... Porque é ministro de Deus, servidor teu para o bem.",
              "Paulo escreve sob Nero (~57 d.C.) — o mesmo imperador que mais tarde perseguiria os cristãos. A submissão às autoridades não é endosso de toda ação governamental — é reconhecimento de que o governo tem uma função divina de manter a ordem. Os limites: quando a autoridade exige desobediência a Deus, os cristãos devem 'obedecer a Deus antes que aos homens' (At 5:29). A submissão é a norma; a resistência é a exceção justificada pela fidelidade a Deus.")
         ]) +
         sec("💝 O Amor como Cumprimento da Lei (13:8-14)", [
             ("Romanos 13:8-10", "Não devais nada a ninguém, exceto o amor com que vos ameis uns aos outros; porque quem ama ao próximo cumpriu a lei... O amor não faz mal ao próximo; de sorte que o cumprimento da lei é o amor.",
              "O amor (<em>agape</em>) não é um sentimento — é um princípio ético que cumpre toda a lei. Os mandamentos (não adulterar, não matar, não furtar, não cobiçar) são resumidos em 'amarás o teu próximo como a ti mesmo'. O amor não substitui a lei — ele a cumpre, porque quem genuinamente ama não fará o que a lei proíbe."),
             ("Romanos 13:11-14", "E isto, sabendo vós o tempo, que é já hora de despertarmos do sono; porque a nossa salvação está agora mais perto de nós do que quando cremos. A noite é passada, e o dia se aproxima; lancemos, pois, as obras das trevas, e vistamo-nos das armas da luz.",
              "A urgência escatológica motiva a ética: o 'dia' (<em>hemera</em>) da vinda de Cristo se aproxima. A armadura da luz (<em>hopla tou photos</em>) contrasta com as obras das trevas. 'Revesti-vos do Senhor Jesus Cristo' — a vida cristã é vestir Cristo, deixar que sua vida se manifeste na nossa.")
         ])),
        (14, "O Forte e o Fraco — Liberdade e Amor",
         "Assim, pois, cada um de nós dará conta de si mesmo a Deus.",
         "Romanos 14:12",
         intro("Romanos 14-15 trata de questões de consciência e liberdade cristã — especialmente a relação entre o 'forte' (que tem liberdade de consciência) e o 'fraco' (que tem escrúpulos). O princípio: a liberdade deve ser exercida em amor, não em julgamento.") +
         sec("⚖️ Não Julgue o Irmão Fraco (14:1-12)", [
             ("Romanos 14:1-4", "Recebei o que é fraco na fé, mas não para decidir dúvidas. Porque um crê que pode comer de tudo, mas o que é fraco come legumes. O que come não despreze o que não come; e o que não come não julgue o que come; porque Deus o recebeu.",
              "O contexto: provavelmente judeus cristãos com escrúpulos sobre alimentos sacrificados a ídolos ou leis dietéticas judaicas. Paulo não toma partido na questão em si — ele trata da atitude: nem o 'forte' deve desprezar o 'fraco', nem o 'fraco' deve julgar o 'forte'. O critério não é a prática — é a recepção por Deus.")
         ]) +
         sec("🙏 Viver para o Senhor (14:13-23)", [
             ("Romanos 14:17-19", "Porque o reino de Deus não é comida nem bebida, mas justiça, e paz, e alegria no Espírito Santo. Porque quem nisto serve a Cristo agradável é a Deus e aprovado dos homens. Sigamos, pois, as coisas que servem para a paz e para a edificação de uns para com os outros.",
              "O reino de Deus não é definido por práticas externas — é definido por justiça, paz e alegria no Espírito Santo. A liberdade cristã deve ser exercida em função da edificação (<em>oikodome</em>) do outro, não da satisfação própria. O princípio: 'tudo o que não é de fé é pecado' — agir contra a consciência, mesmo que a prática seja objetivamente lícita, é pecado para aquele que age.")
         ])),
        (15, "O Exemplo de Cristo e os Planos de Paulo",
         "Ora, o Deus de esperança vos encha de todo o gozo e paz em credes, para que abundeis em esperança pela virtude do Espírito Santo.",
         "Romanos 15:13",
         intro("Romanos 15 conclui a seção ética com o exemplo de Cristo como modelo de serviço ao fraco, a missão de Paulo aos gentios, e seus planos de visitar Roma e a Espanha.") +
         sec("🙏 Cristo como Modelo de Serviço (15:1-13)", [
             ("Romanos 15:1-3", "Ora, nós, os que somos fortes, devemos suportar as fraquezas dos fracos, e não agradar a nós mesmos. Cada um de nós agrade ao próximo no que é bom, para edificação. Porque também Cristo não agradou a si mesmo.",
              "O argumento final: Cristo é o modelo supremo de não agradar a si mesmo. Ele, sendo Deus, se humilhou e serviu (Fp 2:5-11). O forte que usa sua liberdade em detrimento do fraco está agindo de forma contrária ao exemplo de Cristo."),
             ("Romanos 15:7-9", "Portanto, recebei-vos uns aos outros, como também Cristo nos recebeu para glória de Deus. Digo, pois, que Jesus Cristo foi ministro da circuncisão pela verdade de Deus, para confirmar as promessas feitas aos pais; e para que os gentios glorifiquem a Deus pela sua misericórdia.",
              "A recepção mútua entre judeus e gentios na Igreja é fundamentada na recepção de Cristo. Jesus ministrou aos judeus para confirmar as promessas; os gentios glorificam a Deus pela misericórdia. A unidade da Igreja não é uniformidade — é diversidade unida pelo mesmo Senhor.")
         ]) +
         sec("🌍 A Missão de Paulo aos Gentios (15:14-33)", [
             ("Romanos 15:20-24", "E assim procurei pregar o evangelho, não onde Cristo já tinha sido nomeado, para não edificar sobre fundamento alheio... Mas agora, não tendo já lugar nestas regiões, e tendo há muitos anos grande desejo de ir ter convosco, quando for a Espanha, irei ter convosco.",
              "Paulo descreve sua estratégia missionária: pregar onde Cristo ainda não foi nomeado — fronteiras do Evangelho. Ele não constrói sobre fundamento alheio (<em>ep allotrion themelion</em>). Seu plano: Jerusalém (levar a oferta) → Roma (visita de passagem) → Espanha (nova fronteira missionária). A Espanha era o extremo ocidental do mundo romano — 'os confins da terra' de At 1:8.")
         ])),
        (16, "Saudações e Doxologia Final",
         "Ao único Deus sábio seja dada glória por Jesus Cristo para sempre. Amém.",
         "Romanos 16:27",
         intro("Romanos 16 é o capítulo mais pessoal da carta — uma lista de 29 saudações individuais que revela a rede de relacionamentos de Paulo e a diversidade da Igreja primitiva. Termina com uma doxologia que resume toda a teologia da carta.") +
         sec("👥 A Rede de Relacionamentos de Paulo (16:1-16)", [
             ("Romanos 16:1-2", "Recomendo-vos Febe, nossa irmã, que é diaconisa da igreja que está em Cencreia; para que a recebais no Senhor, como convém aos santos, e a assistais em qualquer coisa de que ela precisar de vós; porque ela tem sido protetora de muitos, e também de mim mesmo.",
              "Febe (<em>Phoibe</em>) é a portadora da carta — ela a levou de Corinto a Roma. Paulo a chama de <em>diakonon</em> (diaconisa/ministra) e <em>prostatis</em> (protetora/patrona) — termos de liderança e serviço. Das 29 pessoas saudadas, pelo menos 10 são mulheres, muitas com funções de liderança. A Igreja primitiva era muito mais igualitária do que frequentemente imaginado."),
             ("Romanos 16:3-5", "Saudai a Priscila e Áquila, meus cooperadores em Cristo Jesus; os quais pela minha vida expuseram os seus próprios pescoços, aos quais não somente eu dou graças, mas também todas as igrejas dos gentios. Saudai também a igreja que está em sua casa.",
              "Priscila e Áquila aparecem 6 vezes no NT — sempre como par ministerial. Notavelmente, Priscila é mencionada primeiro 4 das 6 vezes, sugerindo que ela tinha papel de liderança mais proeminente. Eles arriscaram a vida por Paulo (provavelmente em Éfeso — At 19) e hospedavam uma igreja em sua casa.")
         ]) +
         sec("⚠️ Advertência Final e Doxologia (16:17-27)", [
             ("Romanos 16:17-18", "Rogo-vos, irmãos, que noteis os que causam divisões e escândalos contra a doutrina que aprendestes; e desviai-vos deles. Porque os tais não servem ao nosso Senhor Jesus Cristo, mas ao seu ventre; e com suaves palavras e lisonjas enganam os corações dos simples.",
              "A advertência final: cuidado com os que causam divisões (<em>dichostasias</em>) e escândalos (<em>skandala</em>) contra a doutrina recebida. O critério de identificação: eles servem ao 'ventre' (<em>koilia</em>) — seus próprios interesses — e usam linguagem suave para enganar. A unidade da Igreja é protegida pela fidelidade à doutrina apostólica."),
             ("Romanos 16:25-27", "Ora, àquele que é poderoso para vos confirmar segundo o meu evangelho e a pregação de Jesus Cristo, segundo a revelação do mistério que desde os tempos eternos esteve oculto, mas que agora foi manifestado... ao único Deus sábio seja dada glória por Jesus Cristo para sempre. Amém.",
              "A doxologia final resume toda a teologia de Romanos: o Evangelho é o mistério eterno agora revelado; Deus é o único sábio (<em>mono sopho theo</em>); a glória é dada por Jesus Cristo para sempre. A carta que começou com o Evangelho como 'poder de Deus para a salvação' termina com toda a glória voltando para Deus. <em>Soli Deo Gloria</em>.")
         ])),
    ]

    for num, titulo, vk, rk, conteudo in caps:
        html = html_cap("Romanos", num, 16, titulo, vk, rk, conteudo, "../../../..")
        salvar("romanos", num, html)
    print(f"✅ Romanos: 16 capítulos gerados")

# ==============================================================
# 1 CORÍNTIOS — 16 capítulos
# ==============================================================
def gerar_1corintios():
    caps = [
        (1, "A Cruz — Loucura para o Mundo, Poder de Deus",
         "Porque a palavra da cruz é loucura para os que perecem; mas para nós, que somos salvos, é o poder de Deus.",
         "1 Coríntios 1:18",
         intro("1 Coríntios foi escrita ~55 d.C. para uma igreja dividida, imoral e confusa. O cap. 1 confronta as divisões partidárias com a teologia da cruz — que inverte toda sabedoria e poder humanos.") +
         sec("✝️ A Loucura da Cruz (1:18-31)", [
             ("1 Coríntios 1:18-25", "Porque a palavra da cruz é loucura para os que perecem; mas para nós, que somos salvos, é o poder de Deus... Porque os judeus pedem sinais, e os gregos buscam sabedoria; mas nós pregamos a Cristo crucificado, que é escândalo para os judeus, e loucura para os gregos.",
              "A cruz (<em>stauros</em>) era o símbolo de vergonha máxima no mundo antigo — morte de escravos e criminosos. Paulo proclama que esta 'loucura' (<em>moria</em>) é o poder (<em>dynamis</em>) e a sabedoria (<em>sophia</em>) de Deus. Para os judeus, um Messias crucificado era <em>skandalon</em> (tropeço — Dt 21:23: 'maldito todo aquele que é pendurado no madeiro'). Para os gregos, era <em>moria</em> (loucura — um deus que morre é contradição em termos). Mas para os chamados, é o poder de Deus."),
             ("1 Coríntios 1:26-29", "Porque vede, irmãos, a vossa vocação; que não são muitos os sábios segundo a carne, nem muitos os poderosos, nem muitos os nobres que são chamados. Mas Deus escolheu as coisas loucas do mundo para confundir as sábias; e Deus escolheu as coisas fracas do mundo para confundir as fortes.",
              "A composição sociológica da Igreja de Corinto confirma a teologia da cruz: não muitos sábios, poderosos ou nobres. Deus escolhe deliberadamente o que o mundo despreza para que nenhuma carne se glorie (<em>kauchesete</em>) diante dele. A eleição divina inverte a hierarquia humana — não porque Deus prefira a ignorância, mas porque a graça não pode ser misturada com o mérito.")
         ])),
        (2, "A Sabedoria do Espírito",
         "Mas, como está escrito: As coisas que o olho não viu, e o ouvido não ouviu, e não subiram ao coração do homem, são as que Deus preparou para os que o amam.",
         "1 Coríntios 2:9",
         intro("1 Coríntios 2 contrasta a sabedoria humana com a sabedoria do Espírito. Paulo pregou não com eloquência filosófica, mas com demonstração do Espírito — e o Espírito revela o que a mente humana não pode alcançar.") +
         sec("🕊️ A Pregação de Paulo e o Espírito (2:1-16)", [
             ("1 Coríntios 2:1-5", "E eu, irmãos, quando fui ter convosco, não fui com sublimidade de palavras ou de sabedoria, anunciar-vos o testemunho de Deus. Porque nada me propus saber entre vós, senão a Jesus Cristo, e este crucificado... para que a vossa fé não se apoiasse em sabedoria dos homens, mas no poder de Deus.",
              "Paulo deliberadamente renunciou à eloquência retórica (<em>hyperoche logou e sophias</em>) para que a fé dos coríntios não repousasse na habilidade humana mas no poder de Deus. Esta não é anti-intelectualismo — é a recusa de usar a sabedoria humana como substituto do poder do Espírito. A demonstração (<em>apodeixis</em>) do Espírito é a evidência de transformação de vidas."),
             ("1 Coríntios 2:9-12", "Mas, como está escrito: As coisas que o olho não viu, e o ouvido não ouviu, e não subiram ao coração do homem, são as que Deus preparou para os que o amam. Mas Deus no-las revelou pelo seu Espírito; porque o Espírito penetra todas as coisas, até as profundezas de Deus.",
              "A citação de Isaías 64:4 é aplicada à revelação do Evangelho. O Espírito (<em>pneuma</em>) é o agente da revelação — ele conhece as profundezas de Deus (<em>ta bathe tou theou</em>) como o espírito humano conhece as profundezas do ser humano. O crente recebeu 'o Espírito que é de Deus' — portanto pode conhecer o que Deus preparou, não por especulação filosófica, mas por revelação.")
         ])),
        (3, "Cooperadores de Deus — Fundamento e Edificação",
         "Porque n
