#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gerador de capítulos aprofundados de Atos — Fase 1: caps. 1–14"""
import os

OUTPUT_DIR = "/home/ubuntu/365-de-graca-e-adoracao/08-novo-testamento/atos/capitulos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def gerar_html(num, titulo, subtitulo, secoes):
    prev_link = f'capitulo-{str(num-1).zfill(2)}.html' if num > 1 else '../index.html'
    next_link = f'capitulo-{str(num+1).zfill(2)}.html' if num < 28 else '../index.html'
    secoes_html = ""
    for secao_titulo, versos in secoes:
        secoes_html += f'<div class="section-block">\n<h2>{secao_titulo}</h2>\n'
        for ref, texto, analise in versos:
            secoes_html += f'''
<div class="verse-block">
  <div class="verse-ref">{ref}</div>
  <blockquote class="verse-text">"{texto}"</blockquote>
  <div class="verse-analysis">{analise}</div>
</div>
'''
        secoes_html += '</div>\n'
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Atos {num} — {titulo} | 365 de Graça &amp; Adoração</title>
<meta name="description" content="Estudo aprofundado de Atos capítulo {num}: {subtitulo}. Análise versículo por versículo, contexto histórico e teologia do Espírito Santo.">
<meta property="og:title" content="Atos {num} — {titulo}">
<meta property="og:description" content="{subtitulo}">
<link rel="stylesheet" href="../../../assets/css/style.css">
<link rel="stylesheet" href="../../../assets/css/bloco.css">
</head>
<body class="bloco-08">
<nav class="topbar">
  <div class="topbar-inner">
    <a class="site-title" href="/">365 de Graça &amp; Adoração</a>
    <div class="nav-links">
      <a href="/">Início</a>
      <a href="/08-novo-testamento/">Novo Testamento</a>
      <a href="/busca/">Buscar</a>
    </div>
  </div>
</nav>
<main class="chapter-main">
  <nav class="breadcrumb">
    <a href="/">Início</a> ›
    <a href="/08-novo-testamento/">Novo Testamento</a> ›
    <a href="../index.html">Atos dos Apóstolos</a> ›
    <span>Capítulo {num}</span>
  </nav>
  <header class="chapter-header">
    <div class="chapter-number">Atos {num}</div>
    <h1 class="chapter-title">{titulo}</h1>
    <p class="chapter-subtitle">{subtitulo}</p>
  </header>
  <article class="chapter-content">
{secoes_html}
  </article>
  <nav class="chapter-nav">
    <a href="{prev_link}" class="nav-btn">← Anterior</a>
    <a href="../index.html" class="nav-btn center">Índice de Atos</a>
    <a href="{next_link}" class="nav-btn">Próximo →</a>
  </nav>
</main>
<footer class="site-footer">
  <p>365 de Graça &amp; Adoração • Da Criação ao Apocalipse • © 2026</p>
</footer>
</body>
</html>
'''

CAPITULOS = {
    1: ("A Ascensão e a Espera do Espírito",
        "O prólogo de Atos, a ascensão de Jesus, a promessa do Espírito e a eleição de Matias",
        [
            ("📜 O Prólogo de Atos (1:1-5)", [
                ("Atos 1:1-2", "No primeiro livro, ó Teófilo, tratei de tudo quanto Jesus começou a fazer e a ensinar, até ao dia em que foi recebido em cima, depois de ter dado mandamentos, pelo Espírito Santo, aos apóstolos que havia escolhido.",
                 "Atos é o segundo volume da obra de Lucas — o mesmo autor do Evangelho de Lucas (cf. Lc 1:1-4). A dedicatória a Teófilo confirma a continuidade. A frase 'tudo quanto Jesus começou a fazer e a ensinar' é teologicamente densa: o Evangelho de Lucas narra o que Jesus <em>começou</em> a fazer — Atos narra o que Jesus <em>continua</em> a fazer pelo Espírito Santo através da Igreja. Atos não é a história dos apóstolos — é a história do Espírito Santo agindo através dos apóstolos. O sujeito real de Atos é o Espírito Santo, mencionado mais de 50 vezes no livro. Lucas, o historiador cuidadoso, ancora a narrativa em fatos verificáveis: nomes, lugares, datas, detalhes geográficos e culturais que arqueólogos e historiadores têm confirmado repetidamente."),
                ("Atos 1:4-5", "E, estando com eles, ordenou-lhes que não se ausentassem de Jerusalém, mas que esperassem a promessa do Pai, a qual, disse ele, ouvis de mim. Porque João, na verdade, batizou com água, mas vós sereis batizados com o Espírito Santo, não muito depois destes dias.",
                 "A 'promessa do Pai' é o Espírito Santo — prometido por Jesus (Jo 14:16-17; 15:26; 16:7-15) e pelos profetas do AT (Jl 2:28-32; Ez 36:26-27; Is 44:3). O contraste entre o batismo de João (com água, preparatório) e o batismo com o Espírito Santo (definitivo, transformador) é fundamental. O batismo com o Espírito não é uma segunda experiência de graça para crentes avançados — é a marca distintiva da era messiânica, o cumprimento de toda a esperança profética. A ordem de esperar em Jerusalém é estratégica: Jerusalém é o centro do mundo judaico, o lugar do templo, o ponto de onde o Evangelho se espalhará para toda a terra (1:8)."),
            ]),
            ("🌤️ A Ascensão de Jesus (1:6-11)", [
                ("Atos 1:7-8", "E disse-lhes: Não vos pertence saber os tempos ou as épocas que o Pai estabeleceu pelo seu próprio poder; mas recebereis a virtude do Espírito Santo, que há de vir sobre vós; e ser-me-eis testemunhas, tanto em Jerusalém como em toda a Judeia e Samaria, e até aos confins da terra.",
                 "Os discípulos ainda pensavam em termos de restauração política de Israel — 'restaurarás o reino a Israel?' A resposta de Jesus redireciona: a questão não é quando, mas o que. O Espírito Santo não é dado para satisfazer curiosidade profética — é dado para missão. 'Recebereis poder' (<em>dynamis</em>) — a mesma palavra de Lucas 1:35 (o poder do Altíssimo sobre Maria) e Lucas 4:14 (Jesus cheio do poder do Espírito). O mapa missionário de Atos 1:8 é o esboço do livro inteiro: Jerusalém (caps. 1-7), Judeia e Samaria (caps. 8-12), confins da terra (caps. 13-28). A missão não é opcional — é a razão de ser da Igreja."),
                ("Atos 1:9-11", "E, havendo dito estas coisas, foi elevado às alturas, e uma nuvem o recebeu, ocultando-o aos seus olhos. E, estando eles com os olhos fitos no céu, enquanto ele subia, eis que dois homens se apresentaram junto deles em vestes brancas, e disseram: Varões galileus, por que estais olhando para o céu?",
                 "A Ascensão é um evento histórico e teológico. Historicamente, Jesus deixa de estar presente de forma física e localizada — sua presença agora é universal, pelo Espírito. Teologicamente, a Ascensão é a entronização de Jesus à direita do Pai (Sl 110:1; At 2:33-36; Hb 1:3) — ele reina como Senhor sobre toda a criação. A nuvem (<em>nephele</em>) é a nuvem da glória divina — a Shekinah (cf. Êx 40:34-38; Lc 9:34-35). Os dois anjos reorientam os discípulos: não fiquem olhando para o céu — voltem para Jerusalém e esperem o Espírito. O mesmo Jesus que subiu voltará — mas enquanto isso, há missão a cumprir."),
            ]),
            ("🗳️ A Eleição de Matias (1:12-26)", [
                ("Atos 1:14", "Todos estes perseveravam unanimemente em oração e súplica, com as mulheres, e Maria, mãe de Jesus, e com seus irmãos.",
                 "A primeira imagem da Igreja nascente é uma comunidade de oração. 'Unanimemente' (<em>homothumadon</em>) — com um só ânimo, um só coração. Este termo aparece 11 vezes em Atos — é a marca da Igreja saudável. A presença de Maria e dos irmãos de Jesus é significativa: os irmãos de Jesus, que durante o ministério eram céticos (Jo 7:5), agora são parte da comunidade. A ressurreição os convenceu. A oração não é uma atividade periférica da Igreja — é sua respiração. Antes de qualquer ação missionária, há oração. O Pentecostes nasce de uma comunidade que orou por dez dias."),
                ("Atos 1:24-26", "E, orando, disseram: Tu, Senhor, que conheces os corações de todos, mostra qual destes dois elegeste para tomar o lugar neste ministério e apostolado, de que Judas se desviou para ir ao seu próprio lugar. E lançaram sortes sobre eles, e a sorte caiu sobre Matias; e foi contado com os onze apóstolos.",
                 "A eleição de Matias por sortes pode parecer estranha, mas era um método legítimo no judaísmo para discernir a vontade de Deus (Pv 16:33; Lv 16:8). A oração que precede a sorte é fundamental — eles não estão apostando, mas consultando Deus. O critério para o apostolado é claro: testemunha ocular do ministério de Jesus desde o batismo de João até a ressurreição (1:21-22). O apostolado não é uma posição administrativa — é um testemunho baseado em experiência direta. Após o Pentecostes, o método de discernimento muda — o Espírito Santo guia diretamente (13:2; 15:28)."),
            ]),
        ]),
    2: ("O Pentecostes — O Nascimento da Igreja",
        "A descida do Espírito Santo, o discurso de Pedro, o batismo de 3.000 e a vida da Igreja primitiva",
        [
            ("🔥 A Descida do Espírito (2:1-13)", [
                ("Atos 2:1-4", "E, quando chegou o dia de Pentecostes, estavam todos reunidos no mesmo lugar. E de repente veio do céu um som, como de um vento impetuoso e veemente, e encheu toda a casa em que estavam assentados. E foram vistas por eles línguas repartidas, como que de fogo, as quais pousaram sobre cada um deles. E todos foram cheios do Espírito Santo e começaram a falar em outras línguas, conforme o Espírito Santo lhes concedia que falassem.",
                 "O Pentecostes é o nascimento da Igreja — o cumprimento da promessa do Pai (1:4) e de toda a esperança profética do AT. Os três sinais sensoriais são teologicamente carregados: (1) O <em>vento</em> (<em>pnoe</em>) — o mesmo termo de Gênesis 2:7 (o sopro de vida) e João 20:22 (Jesus sopra o Espírito sobre os discípulos). O Espírito é o sopro de Deus que dá vida nova. (2) O <em>fogo</em> — a presença de Deus no AT é frequentemente associada ao fogo: a sarça ardente (Êx 3:2), a coluna de fogo (Êx 13:21), o Sinai (Êx 19:18). O fogo purifica e ilumina. (3) As <em>línguas</em> — o milagre de falar em línguas conhecidas por estrangeiros é o reverso da Torre de Babel (Gn 11): onde Babel dividiu as línguas, o Pentecostes as une no louvor a Deus. A universalidade da missão começa aqui."),
                ("Atos 2:5-11", "E havia em Jerusalém judeus, homens religiosos, de todas as nações que estão debaixo do céu... e os ouvimos falar em nossas línguas as grandezas de Deus.",
                 "A lista de nações presentes em Jerusalém no Pentecostes é um mapa do mundo conhecido: do Oriente (Partos, Medos, Elamitas, Mesopotâmia) ao Ocidente (Roma), do Norte (Capadócia, Ponto, Ásia) ao Sul (Egito, Líbia, Cirene). Lucas está dizendo: desde o primeiro dia, o Evangelho foi para todas as nações. O milagre das línguas não é apenas um sinal espetacular — é uma declaração teológica: a mensagem de Jesus é para todos os povos, em todas as línguas. A Igreja nasce multilíngue e multicultural — não como uma seita judaica local, mas como um movimento universal."),
            ]),
            ("📢 O Discurso de Pedro (2:14-41)", [
                ("Atos 2:14-21", "Mas Pedro, pondo-se de pé com os onze, levantou a voz e disse-lhes: Varões judeus, e todos os que habitais em Jerusalém, seja-vos isto notório, e escutai as minhas palavras... Mas isto é o que foi dito pelo profeta Joel: E nos últimos dias, diz Deus, derramarei do meu Espírito sobre toda a carne.",
                 "O primeiro sermão cristão da história começa com a Escritura. Pedro não inventa uma nova religião — ele interpreta os eventos do Pentecostes à luz da profecia de Joel 2:28-32. 'Os últimos dias' (<em>eschatais hemerais</em>) — a era messiânica, o tempo entre a primeira e a segunda vinda de Cristo. Estamos nos 'últimos dias' desde o Pentecostes. 'Sobre toda a carne' — sem distinção de gênero (filhos e filhas), idade (jovens e velhos) ou status social (servos e servas). O Espírito não é privilégio de uma elite espiritual — é derramado sobre todos os que creem."),
                ("Atos 2:22-24", "Varões israelitas, ouvi estas palavras: A Jesus de Nazaré, homem aprovado por Deus entre vós com milagres, prodígios e sinais que Deus fez por ele no meio de vós, como vós mesmos sabeis; a este, que foi entregue pelo determinado conselho e presciência de Deus, vós o matastes, crucificando-o por mãos de iníquos; ao qual Deus ressuscitou, havendo desatado as dores da morte, pois não era possível que fosse retido por ela.",
                 "O núcleo do kerigma (proclamação) apostólico está aqui: (1) Jesus de Nazaré — um homem histórico, verificável; (2) aprovado por Deus — os milagres são a assinatura divina; (3) crucificado — a morte é real, não aparente; (4) pelo 'determinado conselho de Deus' — a cruz não é acidente, mas plano eterno; (5) ressuscitado — o fato central do Evangelho. 'Não era possível que fosse retido por ela' — a morte não tinha poder para reter o Autor da vida (3:15). Pedro fala para os mesmos que pediram a crucificação de Jesus — não com acusação vingativa, mas com convite ao arrependimento."),
                ("Atos 2:36-38", "Saiba, pois, com certeza toda a casa de Israel que a este Jesus, que vós crucificastes, Deus o fez Senhor e Cristo. E eles, ouvindo isto, compungiram-se no coração, e disseram a Pedro e aos outros apóstolos: Que faremos, varões irmãos? E Pedro disse-lhes: Arrependei-vos, e cada um de vós seja batizado em nome de Jesus Cristo, para remissão dos pecados; e recebereis o dom do Espírito Santo.",
                 "A conclusão do sermão é uma declaração cristológica: Jesus é 'Senhor' (<em>Kyrios</em> — o título divino do AT, YHWH) e 'Cristo' (<em>Christos</em> — o Messias ungido). A resposta do povo — 'compungiram-se no coração' (<em>katenygesan ten kardian</em> — literalmente 'foram perfurados no coração') — é a obra do Espírito Santo (Jo 16:8-11). A resposta apostólica ao arrependimento é dupla: batismo (sinal externo da nova aliança) e recebimento do Espírito Santo (realidade interna). Três mil pessoas são batizadas naquele dia — a Igreja nasce com um crescimento explosivo que só pode ser explicado pela ação sobrenatural do Espírito."),
            ]),
            ("🏘️ A Vida da Igreja Primitiva (2:42-47)", [
                ("Atos 2:42-47", "E perseveravam na doutrina dos apóstolos, e na comunhão, e no partir do pão, e nas orações... E todos os que criam estavam juntos e tinham tudo em comum... E, perseverando unânimes todos os dias no templo, e partindo o pão em casa, comiam juntos com alegria e singeleza de coração, louvando a Deus e caindo na graça de todo o povo. E o Senhor ajuntava cada dia à igreja os que haviam de ser salvos.",
                 "Este retrato da Igreja primitiva é um dos textos mais importantes do NT para a eclesiologia. Os quatro pilares da vida comunitária são: (1) <em>Doutrina dos apóstolos</em> — o ensino apostólico, que se tornará o NT. A Igreja é fundada na Palavra. (2) <em>Comunhão</em> (<em>koinonia</em>) — não apenas convívio social, mas participação mútua na vida de Deus e uns dos outros. (3) <em>Partir do pão</em> — a Ceia do Senhor, celebrada nas casas com alegria. (4) <em>Orações</em> — a vida de oração constante. A partilha de bens não é comunismo forçado — é o fruto espontâneo do amor. 'O Senhor ajuntava cada dia' — o crescimento da Igreja é obra de Deus, não de estratégia humana."),
            ]),
        ]),
    3: ("A Cura do Coxo e o Segundo Sermão de Pedro",
        "O milagre no portão Formoso, o discurso no pórtico de Salomão e o anúncio do Servo Sofredor",
        [
            ("🦿 A Cura no Portão Formoso (3:1-10)", [
                ("Atos 3:1-6", "E Pedro e João subiam juntos ao templo, à hora da oração, que era a nona. E era levado um homem, coxo desde o ventre de sua mãe, o qual puseram cada dia à porta do templo chamada Formosa, para pedir esmola aos que entravam no templo. Este, vendo Pedro e João que iam entrar no templo, pedia que lhe dessem esmola. E Pedro, com João, fixando os olhos nele, disse: Olha para nós. E ele os olhava atentamente, esperando receber alguma coisa deles. Mas Pedro disse: Não tenho prata nem ouro; mas o que tenho isso te dou: Em nome de Jesus Cristo de Nazaré, levanta-te e anda.",
                 "O milagre no portão Formoso é o primeiro sinal registrado da Igreja nascente — e é programático. O homem coxo desde o nascimento representa a condição humana: incapaz de andar, dependente de esmolas, excluído do templo (a Lei proibia coxos de entrar no templo — Lv 21:18; 2Sm 5:8). Pedro e João não têm dinheiro — mas têm algo infinitamente mais valioso: o nome de Jesus Cristo. 'Em nome de Jesus Cristo de Nazaré' — o nome (<em>onoma</em>) no mundo antigo representava a pessoa e seu poder. Curar em nome de Jesus é agir com a autoridade delegada por Jesus ressuscitado. A cura é imediata e completa — 'imediatamente se firmaram os seus pés e tornozelos' (3:7)."),
                ("Atos 3:8-10", "E, saltando, ficou em pé e andou; e entrou com eles no templo, andando, saltando e louvando a Deus. E todo o povo o viu andar e louvar a Deus. E o reconheciam como sendo aquele que se assentava a pedir esmola à porta Formosa do templo; e ficaram cheios de admiração e espanto pelo que lhe havia acontecido.",
                 "A reação do homem curado é adoração espontânea — 'andando, saltando e louvando a Deus.' Isso ecoa Isaías 35:6: 'Então o coxo saltará como um cervo.' O milagre é um sinal do Reino de Deus que irrompe na história — a restauração da criação que Jesus inaugurou. A admiração do povo cria a oportunidade para o segundo sermão de Pedro. Os milagres em Atos não são fins em si mesmos — são sinais que apontam para Jesus e abrem portas para o Evangelho."),
            ]),
            ("📢 O Segundo Sermão de Pedro (3:11-26)", [
                ("Atos 3:13-16", "O Deus de Abraão, e de Isaque, e de Jacó, o Deus de nossos pais, glorificou o seu Filho Jesus, a quem vós entregastes e negastes diante de Pilatos, quando ele havia determinado soltá-lo. Mas vós negastes o Santo e o Justo, e pedistes que vos fosse dado um homicida; e matastes o Príncipe da vida, a quem Deus ressuscitou dos mortos, do que nós somos testemunhas.",
                 "Pedro conecta o milagre ao Deus do AT — o mesmo Deus de Abraão, Isaque e Jacó. Isso é crucial: o Evangelho não é uma nova religião, mas o cumprimento da fé de Israel. A série de títulos cristológicos é impressionante: 'Filho' (<em>pais</em> — também pode ser 'Servo', ecoando o Servo Sofredor de Isaías), 'Santo e Justo' (títulos messiânicos), 'Príncipe da vida' (<em>archegos tes zoes</em> — o Iniciador/Autor da vida). A ironia é dolorosa: vocês mataram o Autor da vida — mas Deus o ressuscitou. A ressurreição é a resposta de Deus ao assassinato do Messias."),
                ("Atos 3:19-21", "Arrependei-vos, pois, e convertei-vos, para que os vossos pecados sejam apagados, e venham assim os tempos do refrigério da presença do Senhor; e ele envie a Jesus Cristo, que vos foi antes anunciado; ao qual convém que o céu receba até aos tempos da restauração de todas as coisas, de que Deus falou pela boca de todos os seus santos profetas desde o princípio do mundo.",
                 "A escatologia de Pedro é rica: (1) 'Tempos do refrigério' (<em>kairoi anapsyxeos</em>) — a era messiânica de restauração; (2) 'Restauração de todas as coisas' (<em>apokatastasis panton</em>) — a renovação cósmica prometida pelos profetas (Is 65:17-25; Ez 36:35; Rm 8:19-23). A segunda vinda de Cristo está condicionada ao arrependimento de Israel? Ou Pedro está simplesmente descrevendo a sequência dos eventos? A maioria dos intérpretes vê aqui uma descrição da esperança escatológica, não uma condição para a parusia. O ponto central é: arrependimento agora, restauração futura."),
            ]),
        ]),
    4: ("A Prisão de Pedro e João e a Oração da Igreja",
        "O primeiro confronto com o Sinédrio, a confissão corajosa de Pedro e a oração que abalou o lugar",
        [
            ("⛓️ A Prisão e o Interrogatório (4:1-22)", [
                ("Atos 4:8-12", "Então Pedro, cheio do Espírito Santo, disse-lhes: Príncipes do povo e anciãos de Israel, se somos interrogados hoje acerca do benefício feito a um homem enfermo, para saber por quem foi curado, seja notório a todos vós e a todo o povo de Israel que em nome de Jesus Cristo de Nazaré, a quem vós crucificastes e a quem Deus ressuscitou dos mortos, em nome deste está este diante de vós são. Este é a pedra que foi rejeitada por vós, os edificadores, a qual foi posta como pedra angular. E em nenhum outro há salvação; porque também debaixo do céu nenhum outro nome há, dado entre os homens, pelo qual devamos ser salvos.",
                 "Pedro, que havia negado Jesus três vezes diante de uma serva, agora confessa Jesus diante do Sinédrio — o mesmo tribunal que condenou Jesus à morte. A transformação é obra do Espírito Santo: 'cheio do Espírito Santo' (<em>plesthe pneumatos hagiou</em>). A citação do Salmo 118:22 ('a pedra rejeitada pelos edificadores') é a mesma que Jesus usou contra os líderes religiosos (Mt 21:42). A afirmação 'em nenhum outro há salvação' (<em>ouk estin en allo oudeni he soteria</em>) é a declaração mais exclusivista do NT depois de João 14:6. Não é intolerância — é a convicção de que Jesus é o único que pode fazer o que a salvação requer: morrer pelos pecados e ressuscitar para a vida eterna."),
                ("Atos 4:13", "E, vendo a ousadia de Pedro e de João, e sabendo que eram homens sem letras e indoutos, maravilhavam-se; e reconheciam que tinham estado com Jesus.",
                 "A observação do Sinédrio é uma das mais tocantes de Atos: 'reconheciam que tinham estado com Jesus.' A ousadia (<em>parresia</em>) de Pedro e João não vinha de educação formal ou habilidade retórica — vinha da presença de Jesus em suas vidas. O Espírito Santo transforma pescadores sem letras em testemunhas corajosas diante do poder. Este é o padrão de Atos: Deus usa os fracos para confundir os fortes (1Co 1:27). A marca do discipulado genuíno não é eloquência ou erudição — é a evidência de que se esteve com Jesus."),
            ]),
            ("🙏 A Oração da Igreja (4:23-31)", [
                ("Atos 4:29-31", "E agora, Senhor, olha para as suas ameaças, e concede aos teus servos que falem a tua palavra com toda a ousadia, estendendo tu a tua mão para curar; e que sinais e prodígios se façam pelo nome do teu santo Filho Jesus. E, quando acabaram de orar, o lugar em que estavam reunidos tremeu; e todos foram cheios do Espírito Santo, e falavam a palavra de Deus com ousadia.",
                 "A oração da Igreja diante da perseguição é modelar. Eles não pedem proteção ou que as ameaças cessem — pedem mais ousadia para pregar. A teologia da oração é cristocêntrica e bíblica: eles citam o Salmo 2 (4:25-26) e interpretam os eventos à luz da soberania de Deus. 'O lugar tremeu' — a resposta de Deus é imediata e física. Novamente 'cheios do Espírito Santo' — o enchimento do Espírito não é uma experiência única e definitiva, mas uma realidade que se renova na oração. A Igreja que ora com ousadia recebe ousadia para pregar."),
            ]),
        ]),
    5: ("Ananias e Safira e os Milagres dos Apóstolos",
        "O pecado da hipocrisia, o julgamento divino, os milagres de cura e a segunda prisão dos apóstolos",
        [
            ("💀 Ananias e Safira (5:1-11)", [
                ("Atos 5:1-5", "Mas um homem chamado Ananias, com Safira, sua mulher, vendeu uma propriedade, e reteve parte do preço, sabendo-o também sua mulher; e, trazendo somente uma parte, a depositou aos pés dos apóstolos. E disse Pedro: Ananias, por que encheu Satanás o teu coração para mentires ao Espírito Santo e reteres parte do preço da herdade? Não ficava ela sendo tua enquanto a conservavas? E, depois de vendida, não estava o preço em teu poder? Por que formaste no teu coração este negócio? Não mentiste aos homens, mas a Deus.",
                 "O episódio de Ananias e Safira é perturbador — e intencionalmente assim. Após o retrato idílico da Igreja em 2:42-47 e 4:32-37, Lucas registra o primeiro pecado interno da comunidade. O problema não é guardar parte do dinheiro — Pedro deixa claro que isso era permitido (5:4). O problema é a hipocrisia: fingir generosidade total enquanto retinha parte. 'Mentistes ao Espírito Santo' — Pedro identifica o Espírito Santo como uma Pessoa a quem se pode mentir, confirmando sua divindade. O julgamento imediato é chocante — mas serve como aviso: a Igreja é o templo do Espírito Santo (1Co 3:16), e a santidade de Deus não tolera hipocrisia em seu santuário. 'Grande temor' (<em>phobos megas</em>) — o resultado é reverência, não terror paralisante."),
            ]),
            ("✨ Os Milagres dos Apóstolos (5:12-16)", [
                ("Atos 5:15-16", "A ponto de levarem os enfermos para as ruas e os deitarem em camas e macas, para que, quando Pedro passasse, ao menos a sua sombra cobrisse algum deles. E também a multidão das cidades vizinhas concorria a Jerusalém, trazendo enfermos e atormentados de espíritos imundos; e todos eram curados.",
                 "A cura pela sombra de Pedro é um dos milagres mais extraordinários de Atos. Não é magia — é a manifestação do poder de Deus através de um instrumento humano totalmente consagrado. Isso ecoa a mulher que tocou a orla do manto de Jesus (Lc 8:44) e os lenços de Paulo que curavam (19:12). O poder não está na sombra ou nos lenços — está em Deus, que usa meios físicos para manifestar sua graça. A fama se espalha além de Jerusalém — o Evangelho começa a cumprir o mapa de 1:8. A cura de 'todos' (<em>hapantes</em>) é uma hipérbole retórica que expressa a abundância da graça divina."),
            ]),
        ]),
    6: ("A Eleição dos Sete Diáconos e Estêvão",
        "O conflito entre helenistas e hebreus, a instituição do diaconato e o início do ministério de Estêvão",
        [
            ("⚖️ O Conflito e a Solução (6:1-7)", [
                ("Atos 6:1-4", "E naqueles dias, crescendo o número dos discípulos, houve uma murmuração dos gregos contra os hebreus, porque as suas viúvas eram desprezadas no ministério diário. E os doze, convocando a multidão dos discípulos, disseram: Não é razoável que nós deixemos a palavra de Deus para servir às mesas. Escolhei, pois, irmãos, dentre vós sete homens de boa reputação, cheios do Espírito Santo e de sabedoria, aos quais constituamos sobre este negócio. Mas nós perseveraremos na oração e no ministério da palavra.",
                 "O primeiro conflito interno da Igreja (depois de Ananias e Safira) é um conflito cultural: helenistas (judeus da diáspora que falavam grego) versus hebreus (judeus palestinos que falavam aramaico). As viúvas helenistas estavam sendo negligenciadas na distribuição diária de alimentos. A solução apostólica é sábia e modelar: (1) reconhecem o problema sem minimizá-lo; (2) delegam a responsabilidade para pessoas qualificadas; (3) mantêm o foco em sua vocação principal (oração e Palavra). Os critérios para os sete são: 'boa reputação, cheios do Espírito Santo e de sabedoria' — não apenas competência administrativa, mas caráter espiritual. Este é o nascimento do diaconato."),
                ("Atos 6:7", "E a palavra de Deus crescia, e o número dos discípulos em Jerusalém se multiplicava muito; e uma grande multidão de sacerdotes obedecia à fé.",
                 "O versículo 7 é um dos 'sumários de progresso' de Atos (cf. 2:47; 9:31; 12:24; 16:5; 19:20; 28:30-31). Lucas registra periodicamente o crescimento da Igreja para mostrar que a missão avança apesar das perseguições e conflitos internos. 'Uma grande multidão de sacerdotes' — isso é extraordinário: os sacerdotes do templo, membros da classe que condenou Jesus, estão se convertendo. A Palavra de Deus tem poder para vencer até as resistências mais profundas."),
            ]),
            ("⭐ Estêvão — Cheio de Graça e Poder (6:8-15)", [
                ("Atos 6:8-10", "E Estêvão, cheio de fé e poder, fazia prodígios e grandes sinais entre o povo. Levantaram-se então alguns da sinagoga chamada dos libertos, e dos cireneus, e dos alexandrinos, e dos que eram da Cilícia e da Ásia, e disputavam com Estêvão. Mas não podiam resistir à sabedoria e ao Espírito com que falava.",
                 "Estêvão é o primeiro dos sete diáconos — e seu ministério transcende a administração de alimentos. Ele é descrito como 'cheio de fé e poder' (<em>pisteos kai dynameos</em>) — o mesmo vocabulário usado para os apóstolos. Os milagres e a sabedoria irresistível de Estêvão provocam a oposição da sinagoga dos libertos (ex-escravos judeus de Roma, Cirene, Alexandria, Cilícia e Ásia). A Cilícia era a região de Tarso — e é possível que o jovem Saulo (Paulo) estivesse entre os que disputavam com Estêvão (cf. 7:58). A perseguição de Estêvão será o catalisador da dispersão que levará o Evangelho para além de Jerusalém."),
            ]),
        ]),
    7: ("O Discurso e o Martírio de Estêvão",
        "A releitura de toda a história de Israel, a visão do Filho do Homem e a morte do primeiro mártir cristão",
        [
            ("📜 O Grande Discurso de Estêvão (7:1-53)", [
                ("Atos 7:2-8", "E ele disse: Varões irmãos e pais, ouvi. O Deus da glória apareceu a nosso pai Abraão, quando estava na Mesopotâmia, antes de habitar em Harã, e disse-lhe: Sai da tua terra e da tua parentela, e vem para a terra que eu te mostrar.",
                 "O discurso de Estêvão é o mais longo de Atos (52 versículos) e uma das peças mais sofisticadas de teologia bíblica do NT. Ele relê toda a história de Israel — de Abraão ao templo de Salomão — para demonstrar uma tese provocativa: Israel sempre rejeitou os mensageiros de Deus. O padrão se repete: José rejeitado pelos irmãos, Moisés rejeitado pelo povo, os profetas perseguidos — e agora Jesus, o Justo, traído e assassinado. Estêvão não está condenando Israel por ser especialmente perverso — está mostrando que a rejeição de Jesus é o clímax de um padrão histórico de resistência à graça de Deus."),
                ("Atos 7:44-50", "Nossos pais tinham no deserto o tabernáculo do testemunho... Mas Salomão lhe edificou uma casa. Todavia o Altíssimo não habita em templos feitos por mãos humanas, como diz o profeta: O céu é o meu trono, e a terra o escabelo dos meus pés. Que casa me edificareis? diz o Senhor. Ou qual é o lugar do meu repouso?",
                 "A crítica ao templo é o ponto mais explosivo do discurso — e a razão pela qual Estêvão foi acusado (6:13-14). Ele não está dizendo que o templo era errado — está dizendo que confundir o templo com a presença de Deus é idolatria. Deus não pode ser confinado em um edifício (1Rs 8:27; Is 66:1-2). O tabernáculo era melhor que o templo porque era móvel — acompanhava o povo em sua jornada. Jesus é o novo templo (Jo 2:19-21) — a presença de Deus não está mais localizada em Jerusalém, mas em Cristo e em seu corpo, a Igreja."),
            ]),
            ("✝️ O Martírio de Estêvão (7:54-60)", [
                ("Atos 7:55-60", "Mas ele, estando cheio do Espírito Santo, fixando os olhos no céu, viu a glória de Deus e Jesus em pé à direita de Deus. E disse: Eis que vejo os céus abertos e o Filho do Homem em pé à direita de Deus... E, ajoelhando-se, clamou em alta voz: Senhor, não lhes imputes este pecado. E, havendo dito isto, adormeceu.",
                 "A morte de Estêvão é modelada na morte de Jesus: ele vê os céus abertos (cf. Lc 3:21), perdoa seus algozes (cf. Lc 23:34) e entrega seu espírito a Jesus (cf. Lc 23:46). Estêvão é o primeiro mártir (<em>martys</em> — testemunha) cristão — e seu martírio inaugura a era das perseguições. 'Jesus em pé à direita de Deus' — em todos os outros textos, Jesus está 'sentado' à direita do Pai (Sl 110:1; Hb 1:3). Aqui ele está 'em pé' — como quem se levanta para receber e honrar seu servo fiel. A presença de Saulo como aprovador da execução (7:58; 8:1) é o ponto de virada: o perseguidor que se tornará o maior missionário da história."),
            ]),
        ]),
    8: ("Filipe, os Samaritanos e o Etíope",
        "A dispersão após a perseguição, o avivamento em Samaria, Simão o mágico e a conversão do etíope",
        [
            ("🌍 A Dispersão e o Avivamento em Samaria (8:1-25)", [
                ("Atos 8:1-4", "E Saulo consentia na sua morte. E naquele dia levantou-se uma grande perseguição contra a igreja em Jerusalém; e todos foram dispersos pelas terras da Judeia e de Samaria, exceto os apóstolos... E os que foram dispersos iam por toda a parte pregando a palavra.",
                 "A perseguição que parecia uma catástrofe para a Igreja torna-se o instrumento da expansão missionária. O Evangelho não pode ser contido — cada cristão disperso torna-se um missionário. 'Iam por toda a parte pregando a palavra' (<em>euangelizomenoi ton logon</em>) — não apenas os apóstolos, mas todos os crentes. A missão não é prerrogativa de uma classe clerical — é responsabilidade de toda a Igreja. Isso cumpre o mapa de 1:8: 'Judeia e Samaria.' A perseguição de Saulo, ironicamente, acelera a missão que ele tentava destruir."),
                ("Atos 8:14-17", "E os apóstolos que estavam em Jerusalém, ouvindo que a Samaria tinha recebido a palavra de Deus, enviaram-lhes Pedro e João; os quais, descendo, oraram por eles para que recebessem o Espírito Santo; porque ainda não tinha descido sobre nenhum deles, mas somente tinham sido batizados em nome do Senhor Jesus. Então lhes impuseram as mãos, e receberam o Espírito Santo.",
                 "O episódio dos samaritanos que creram mas não receberam o Espírito é um dos mais debatidos de Atos. Por que o Espírito foi retido até a chegada de Pedro e João? A explicação mais convincente é eclesiológica: Deus quis que a extensão do Evangelho aos samaritanos (inimigos históricos dos judeus) fosse confirmada pela presença apostólica, garantindo a unidade da Igreja. O Espírito não é dado automaticamente — mas sua recepção pelos samaritanos na presença de apóstolos judeus demonstra que a Igreja é uma, não dividida por fronteiras étnicas."),
            ]),
            ("🛤️ O Etíope e o Evangelho para a África (8:26-40)", [
                ("Atos 8:26-31", "E o anjo do Senhor falou a Filipe, dizendo: Levanta-te e vai para o sul, para o caminho que desce de Jerusalém a Gaza, o qual é deserto. E ele se levantou e foi. E eis que um homem etíope, eunuco, oficial de Candace, rainha dos etíopes, o qual era superintendente de todos os seus tesouros, e tinha vindo a Jerusalém para adorar, voltava, e, assentado no seu carro, lia o profeta Isaías.",
                 "A conversão do etíope é um dos momentos mais belos de Atos. Um eunuco — excluído da plena participação no culto judaico (Dt 23:1) — está lendo Isaías 53, o capítulo do Servo Sofredor. A providência divina é evidente: o Espírito guia Filipe até exatamente o ponto onde o etíope está lendo exatamente o texto que aponta para Jesus. 'Entendes o que lês?' — a Escritura precisa de interpretação. Filipe 'começando por esta Escritura, anunciou-lhe o evangelho de Jesus' (8:35). A hermenêutica cristológica do AT — toda a Escritura aponta para Jesus — é o método apostólico de pregação."),
                ("Atos 8:36-39", "E, indo eles pelo caminho, chegaram a uma água; e disse o eunuco: Eis aqui água; que impede que eu seja batizado? E Filipe disse: Se crês de todo o coração, é lícito. E, respondendo, disse: Creio que Jesus Cristo é o Filho de Deus. E mandou parar o carro; e desceram ambos à água, tanto Filipe como o eunuco, e o batizou. E, quando saíram da água, o Espírito do Senhor arrebatou a Filipe, e o eunuco não o viu mais; e seguiu o seu caminho alegre.",
                 "O batismo do etíope é imediato — a fé confessada leva ao batismo. 'Se crês de todo o coração' — a condição do batismo é a fé genuína, não um período de instrução prolongado. A confissão 'Jesus Cristo é o Filho de Deus' é o credo batismal primitivo. O etíope 'seguiu o seu caminho alegre' (<em>chairon</em>) — a alegria é o fruto do encontro com Cristo. Tradição cristã etíope afirma que este homem levou o Evangelho para a Etiópia — tornando-se o fundador de uma das mais antigas igrejas cristãs do mundo."),
            ]),
        ]),
    9: ("A Conversão de Saulo de Tarso",
        "O encontro com o Ressuscitado no caminho de Damasco, o batismo de Saulo e os primeiros anos do apóstolo",
        [
            ("⚡ O Caminho de Damasco (9:1-19)", [
                ("Atos 9:1-6", "E Saulo, respirando ainda ameaças e mortes contra os discípulos do Senhor, foi ao sumo sacerdote e pediu-lhe cartas para Damasco, para as sinagogas, a fim de que, se encontrasse alguns do Caminho, tanto homens como mulheres, os trouxesse presos a Jerusalém. E, indo no caminho, aconteceu que, ao aproximar-se de Damasco, subitamente o cercou um resplendor de luz do céu; e, caindo em terra, ouviu uma voz que lhe dizia: Saulo, Saulo, por que me persegues? E ele disse: Quem és tu, Senhor? E disse o Senhor: Eu sou Jesus, a quem tu persegues.",
                 "A conversão de Saulo é um dos eventos mais importantes da história cristã — e Lucas a narra três vezes (caps. 9, 22 e 26), sublinhando sua importância. Saulo não era um pecador comum — era um zeloso perseguidor da Igreja, convicto de estar servindo a Deus (cf. Fp 3:6; Gl 1:13-14). A revelação do Ressuscitado destrói toda a sua cosmovisão: se Jesus ressuscitou, então ele é o Messias; se ele é o Messias, então os cristãos têm razão; se os cristãos têm razão, então Saulo tem perseguido o povo de Deus. 'Por que me persegues?' — Jesus se identifica com sua Igreja: perseguir os cristãos é perseguir Cristo (cf. Mt 25:40,45). A identificação de Jesus com os marginalizados e perseguidos é total."),
                ("Atos 9:15-16", "E disse-lhe o Senhor: Vai, porque este é para mim um vaso escolhido, para levar o meu nome perante os gentios, e reis, e os filhos de Israel. Porque eu lhe mostrarei quanto lhe convém padecer pelo meu nome.",
                 "A vocação de Paulo é revelada a Ananias: 'vaso escolhido' (<em>skeuos ekloges</em>) — instrumento de eleição divina. O escopo da missão é extraordinário: gentios, reis e filhos de Israel — toda a humanidade. Mas a vocação vem com um custo: 'quanto lhe convém padecer.' O sofrimento não é um acidente na vida apostólica — é parte integrante da vocação. Paulo cumprirá essa profecia: 2 Coríntios 11:23-28 lista os sofrimentos extraordinários que ele suportou. O vaso escolhido é um vaso partido — e é exatamente por isso que a luz de Cristo brilha através dele (2Co 4:7)."),
            ]),
            ("🕊️ Ananias e o Batismo de Saulo (9:10-19)", [
                ("Atos 9:17-19", "E foi Ananias e entrou na casa, e, impondo-lhe as mãos, disse: Irmão Saulo, o Senhor Jesus, que te apareceu no caminho por onde vinhas, me enviou para que recuperes a vista e sejas cheio do Espírito Santo. E logo caíram dos seus olhos como que escamas, e recobrou a vista; e, levantando-se, foi batizado. E, tendo comido, recobrou as forças.",
                 "Ananias é um herói anônimo da história cristã. Deus pede que ele vá ao perseguidor da Igreja — e ele obedece, apesar do medo justificado. Ele chama Saulo de 'irmão' — antes mesmo do batismo, antes de qualquer prova de conversão genuína. Isso é a graça em ação: Ananias trata Saulo como irmão pela fé de que Deus está agindo nele. As 'escamas' que caem dos olhos de Saulo são um símbolo perfeito: ele estava cego antes — cego para a verdade sobre Jesus, cego para o sofrimento que causava. Agora ele vê — e o que ele vê transforma sua vida inteira."),
            ]),
        ]),
    10: ("Cornélio — O Evangelho Chega aos Gentios",
         "A visão de Pedro, a visita à casa de Cornélio e o Pentecostes dos gentios",
         [
             ("👁️ A Visão de Pedro (10:1-23)", [
                 ("Atos 10:9-16", "E no dia seguinte, indo eles pelo caminho e aproximando-se da cidade, Pedro subiu ao terraço para orar, por volta da hora sexta. E teve fome, e quis comer; mas, enquanto lhe preparavam a comida, caiu em êxtase; e viu o céu aberto e descendo um vaso, como se fosse um grande lençol, atado pelas quatro pontas e baixado à terra; no qual havia todo o gênero de quadrúpedes da terra, e répteis, e aves do céu. E veio uma voz que lhe dizia: Levanta-te, Pedro, mata e come. Mas Pedro disse: De modo nenhum, Senhor, porque nunca comi coisa alguma comum ou imunda. E a voz lhe falou segunda vez: O que Deus purificou não o chames tu comum.",
                  "A visão de Pedro é uma das mais revolucionárias do NT — e ele mesmo não a entende imediatamente. A visão repete-se três vezes (como a negação e a restauração de Pedro — o número três é significativo em sua história). A mensagem não é apenas sobre alimentos — é sobre pessoas. Pedro entenderá isso quando chegar à casa de Cornélio: 'Deus me mostrou que não devo chamar a nenhum homem comum ou imundo' (10:28). As leis alimentares do AT serviam para separar Israel das nações — agora, em Cristo, a separação foi superada. A cruz de Jesus derrubou o 'muro de separação' entre judeus e gentios (Ef 2:14)."),
             ]),
             ("🌍 O Pentecostes dos Gentios (10:34-48)", [
                 ("Atos 10:34-36", "E Pedro, abrindo a boca, disse: Reconheço por verdade que Deus não faz acepção de pessoas; mas em qualquer nação aquele que o teme e pratica a justiça lhe é aceito. A palavra que Deus enviou aos filhos de Israel, anunciando-lhes o evangelho da paz por Jesus Cristo (este é o Senhor de todos).",
                  "A declaração de Pedro — 'Deus não faz acepção de pessoas' (<em>ouk estin prosopolemptes ho theos</em>) — é uma revolução teológica. No judaísmo, a eleição de Israel era entendida como exclusiva. Pedro agora entende que a eleição de Israel era para ser canal de bênção para todas as nações (Gn 12:3) — não uma barreira. 'Este é o Senhor de todos' (<em>panton Kyrios</em>) — Jesus não é apenas o Messias de Israel, mas o Senhor de toda a humanidade."),
                 ("Atos 10:44-48", "Ainda estava Pedro falando estas palavras, quando o Espírito Santo desceu sobre todos os que ouviam a palavra. E os fiéis da circuncisão que tinham vindo com Pedro ficaram maravilhados, porque o dom do Espírito Santo foi também derramado sobre os gentios. Pois os ouviam falar em línguas e magnificar a Deus.",
                  "O 'Pentecostes dos gentios' é a confirmação divina de que o Evangelho é para todos. O Espírito Santo interrompe o sermão de Pedro — Deus não espera o fim do discurso para agir. As línguas são o sinal que os judeus presentes reconhecem: o mesmo Espírito que desceu em Jerusalém está agora sobre os gentios. Pedro tira a conclusão lógica: 'Pode alguém recusar a água do batismo a estes?' A sequência é significativa: o Espírito vem antes do batismo — mostrando que o batismo não confere o Espírito, mas o sela e confirma."),
             ]),
         ]),
    11: ("A Defesa de Pedro e a Igreja em Antioquia",
         "Pedro defende sua ação diante da Igreja em Jerusalém e o nascimento da Igreja em Antioquia",
         [
             ("🗣️ A Defesa de Pedro (11:1-18)", [
                 ("Atos 11:15-18", "E, quando comecei a falar, caiu o Espírito Santo sobre eles, como também sobre nós no princípio. E lembrei-me da palavra do Senhor, quando disse: João, na verdade, batizou com água, mas vós sereis batizados com o Espírito Santo. Pois se Deus lhes deu o mesmo dom que a nós, quando cremos no Senhor Jesus Cristo, quem era eu para poder resistir a Deus? E, ouvindo eles isto, sossegaram e glorificaram a Deus, dizendo: Então também aos gentios concedeu Deus o arrependimento para a vida.",
                  "A defesa de Pedro diante dos 'da circuncisão' em Jerusalém é um momento decisivo para a unidade da Igreja. Pedro não argumenta teologicamente — ele narra os fatos: o Espírito desceu sobre os gentios exatamente como desceu sobre nós no Pentecostes. O argumento é irrefutável: se Deus agiu, quem sou eu para resistir? A resposta da Igreja em Jerusalém é modelar: sossegaram e glorificaram a Deus. Quando a evidência da graça de Deus é clara, a resposta correta é adoração, não resistência. A conclusão teológica — também aos gentios concedeu Deus o arrependimento para a vida — é um marco na história da Igreja."),
             ]),
             ("🏙️ A Igreja em Antioquia (11:19-30)", [
                 ("Atos 11:19-21", "Ora, os que tinham sido dispersos por causa da tribulação que houve por causa de Estêvão passaram até à Fenícia, e Chipre, e Antioquia, não falando a palavra a ninguém senão somente aos judeus. Havia, porém, alguns deles, homens de Chipre e de Cirene, os quais, entrando em Antioquia, falavam também aos gregos, anunciando o evangelho do Senhor Jesus. E a mão do Senhor era com eles, e grande número de pessoas creu e se converteu ao Senhor.",
                  "Antioquia da Síria torna-se o novo centro missionário — a base de operações para as viagens de Paulo. Ela é fundada não pelos apóstolos, mas por crentes anônimos de Chipre e Cirene que tiveram a audácia de pregar aos gregos. A inovação missionária muitas vezes vem de pessoas desconhecidas, não de líderes estabelecidos. 'A mão do Senhor era com eles' — a fórmula do AT para a bênção divina (Êx 9:3; Js 4:24) agora é aplicada à missão gentílica. Antioquia será o modelo de Igreja multicultural e missionária."),
                 ("Atos 11:26", "E sucedeu que todo um ano se reuniram naquela igreja, e ensinaram muita gente; e em Antioquia foram os discípulos, pela primeira vez, chamados cristãos.",
                  "O nome 'cristãos' (<em>Christianoi</em>) é dado pelos de fora — provavelmente pelos romanos, como um apelido político (como 'herodiacos' para os seguidores de Herodes). O nome pega porque é preciso: esses discípulos são tão identificados com Cristo que seu nome define sua identidade. 'Cristão' não é um título religioso — é uma declaração de pertencimento: sou de Cristo, sigo Cristo, vivo por Cristo. Barnabé e Saulo passam um ano ensinando em Antioquia — o modelo de discipulado intensivo que formará a base para as viagens missionárias."),
             ]),
         ]),
    12: ("A Prisão de Pedro e a Morte de Herodes",
         "Herodes Agripa mata Tiago, prende Pedro, o anjo liberta Pedro e o rei blasfemo é julgado por Deus",
         [
             ("⛓️ A Prisão de Pedro (12:1-19)", [
                 ("Atos 12:5-11", "Assim Pedro era guardado na prisão; mas a igreja fazia oração a Deus por ele sem cessar... E eis que sobreveio o anjo do Senhor, e uma luz resplandeceu na cela; e, tocando Pedro no lado, o despertou, dizendo: Levanta-te depressa. E caíram-lhe as cadeias das mãos... E saindo, seguia-o, e não sabia que era verdade o que o anjo fazia, mas cuidava que via uma visão.",
                  "A libertação de Pedro é narrada com um humor sutil e delicioso: Pedro pensa que está sonhando, a serva Rode fica tão surpresa com sua voz que esquece de abrir a porta, e os crentes que oravam pela libertação de Pedro não acreditam quando ele aparece à porta. A ironia é intencional: eles oraram com fé — mas ficaram surpresos quando Deus respondeu. A oração da Igreja é poderosa mesmo quando a fé é imperfeita. O anjo guia Pedro passo a passo — 'levanta-te, veste-te, calça as sandálias, segue-me' — Deus cuida dos detalhes práticos da libertação."),
             ]),
             ("⚡ A Morte de Herodes (12:20-25)", [
                 ("Atos 12:21-23", "E num dia determinado, Herodes, vestido de traje real e assentado no tribunal, lhes fez uma alocução. E o povo gritava: Voz de Deus e não de homem! E logo o anjo do Senhor o feriu, porque não deu a glória a Deus; e, sendo comido de vermes, expirou.",
                  "O contraste é deliberado: Pedro, que recusou adoração (10:25-26), é libertado; Herodes, que aceita adoração divina, é julgado. O historiador Josefo confirma a morte de Herodes Agripa I em 44 d.C. com detalhes similares (Ant. 19.8.2). A causa da morte segundo Atos é teológica: 'porque não deu a glória a Deus.' O pecado de Herodes não é apenas vaidade — é blasfêmia: aceitar honra divina que pertence somente a Deus. O versículo seguinte é o contraste perfeito: 'E a palavra de Deus crescia e se multiplicava' (12:24). Os reis passam — a Palavra permanece."),
             ]),
         ]),
    13: ("A Primeira Viagem Missionária — Chipre e Pisídia",
         "O envio de Barnabé e Saulo pela Igreja de Antioquia, a missão em Chipre e o sermão em Antioquia da Pisídia",
         [
             ("🚀 O Envio Missionário (13:1-12)", [
                 ("Atos 13:2-4", "E, enquanto celebravam o culto do Senhor e jejuavam, disse o Espírito Santo: Separai-me a Barnabé e a Saulo para a obra a que os tenho chamado. Então, jejuando e orando, e impondo-lhes as mãos, os despediram. Eles, pois, enviados pelo Espírito Santo, desceram a Selêucia, e dali navegaram para Chipre.",
                  "O envio missionário de Barnabé e Saulo é o modelo de missão cristã: nasce da adoração e do jejum, é iniciado pelo Espírito Santo (não por decisão humana), é confirmado pela Igreja local através da imposição de mãos, e é sustentado pela oração. 'Enviados pelo Espírito Santo' (<em>ekpemphthentes hypo tou hagiou pneumatos</em>) — o Espírito é o agente principal da missão. A Igreja não envia — ela reconhece e confirma o que o Espírito já iniciou. Este é o padrão apostólico: missão como resposta à iniciativa divina, não como programa humano."),
                 ("Atos 13:9-12", "Saulo, porém, também chamado Paulo, cheio do Espírito Santo, fixando nele os olhos, disse: Ó filho do diabo, cheio de todo o engano e de toda a malícia, inimigo de toda a justiça, não cessarás de perverter os retos caminhos do Senhor? E agora eis que a mão do Senhor está sobre ti, e ficarás cego, sem ver o sol por algum tempo. E logo caiu sobre ele névoa e escuridão; e, andando em derredor, procurava quem o guiasse pela mão.",
                  "O confronto com Barjesus (Elimas) em Chipre é o primeiro conflito missionário com o poder espiritual do mal. Paulo (o nome grego de Saulo — significativamente, ele começa a ser chamado Paulo exatamente quando entra no mundo greco-romano) enfrenta o mágico com autoridade apostólica. A cegueira temporária de Elimas ecoa a cegueira temporária de Paulo em Damasco — talvez Paulo esperasse que Elimas, como ele, usasse o tempo de cegueira para reflexão e arrependimento. O procônsul Sérgio Paulo crê — a primeira conversão registrada de um funcionário romano de alto escalão."),
             ]),
             ("📢 O Sermão em Antioquia da Pisídia (13:13-52)", [
                 ("Atos 13:38-41", "Portanto, seja-vos notório, varões irmãos, que por este vos é anunciada a remissão dos pecados; e de tudo aquilo de que pela lei de Moisés não pudestes ser justificados, por este é justificado todo aquele que crê. Vede, pois, que não venha sobre vós o que está dito nos profetas: Vede, desprezadores, e maravilhai-vos e desaparecei; porque eu faço uma obra nos vossos dias, obra que de modo nenhum crereis, ainda que alguém vo-la conte.",
                  "O sermão de Paulo em Antioquia da Pisídia é o primeiro sermão paulino registrado em Atos — e é uma obra-prima de pregação cristocêntrica. Ele segue a estrutura do discurso de Pedro no Pentecostes: história de Israel → Jesus → ressurreição → chamado ao arrependimento. A novidade paulina é a afirmação explícita da justificação pela fé: 'justificado todo aquele que crê' — a linguagem que dominará suas cartas (especialmente Romanos e Gálatas). A citação de Habacuque 1:5 é um aviso solene: a graça rejeitada torna-se julgamento."),
                 ("Atos 13:46-48", "Então Paulo e Barnabé, falando ousadamente, disseram: A vós era necessário que a palavra de Deus fosse pregada primeiro; mas, visto que a rejeitais e não vos julgais dignos da vida eterna, eis que nos voltamos para os gentios. Porque assim nos mandou o Senhor: Eu te pus para ser luz dos gentios, a fim de que sejas para salvação até os confins da terra. E os gentios, ouvindo isto, alegravam-se e glorificavam a palavra do Senhor; e creram todos os que estavam ordenados para a vida eterna.",
                  "A virada para os gentios é um momento decisivo — e se repetirá em Corinto (18:6) e Roma (28:28). Paulo não abandona os judeus — ele sempre começa na sinagoga. Mas quando a mensagem é rejeitada, ele se volta para os gentios. A frase 'todos os que estavam ordenados para a vida eterna' (<em>hosoi esan tetagmenoi eis zoen aionion</em>) é um dos textos mais debatidos sobre eleição no NT. Ela afirma a soberania divina na salvação sem negar a responsabilidade humana — os gentios 'creram' (ato humano) porque estavam 'ordenados' (ato divino). A tensão entre soberania e responsabilidade é característica da teologia bíblica."),
             ]),
         ]),
    14: ("A Primeira Viagem Missionária — Icônio, Listra e Derbe",
         "Milagres e perseguições, a cura do coxo em Listra, a lapidação de Paulo e o retorno a Antioquia",
         [
             ("🏙️ Icônio e Listra (14:1-20)", [
                 ("Atos 14:8-10", "E estava assentado em Listra certo homem com os pés sem força, coxo desde o ventre de sua mãe, que nunca tinha andado. Este ouvia Paulo falar; o qual, fixando nele os olhos e vendo que tinha fé para ser curado, disse em alta voz: Levanta-te direito sobre os teus pés. E ele saltou e andou.",
                  "A cura do coxo em Listra ecoa deliberadamente a cura de Pedro no portão Formoso (cap. 3): coxo desde o nascimento, curado pela palavra apostólica, salta e anda. Lucas está mostrando que Paulo tem a mesma autoridade apostólica que Pedro. A diferença é a reação: em Jerusalém, o milagre levou à pregação; em Listra (cidade pagã sem sinagoga), a multidão conclui que os deuses desceram em forma humana — Barnabé é Zeus e Paulo é Hermes. A confusão revela a mentalidade pagã: quando algo sobrenatural acontece, os deuses devem estar envolvidos. Paulo e Barnabé rasgam as vestes em horror — o gesto judaico de protesto contra a blasfêmia."),
                 ("Atos 14:15-17", "E dizendo: Varões, por que fazeis isto? Nós também somos homens sujeitos às mesmas paixões que vós, e vos anunciamos que vos convertais destas vaidades ao Deus vivo, que fez o céu, e a terra, e o mar, e tudo o que neles há; o qual nos séculos passados deixou andar todas as nações nos seus próprios caminhos; ainda assim não se deixou a si mesmo sem testemunho, fazendo bem, dando-nos do céu chuvas e estações frutíferas, enchendo de sustento e de alegria os nossos corações.",
                  "O discurso de Paulo em Listra é o primeiro sermão para uma audiência completamente pagã — sem conhecimento do AT. A estratégia é diferente: em vez de começar com a história de Israel, Paulo começa com a teologia natural — Deus como Criador que se revela na natureza (cf. Rm 1:19-20). Isso é a 'teologia natural' ou 'revelação geral': Deus deixou testemunho de si mesmo nas chuvas, nas estações, nos alimentos. Mas a revelação natural é insuficiente para a salvação — ela aponta para Deus, mas não revela Jesus. Por isso Paulo anuncia o 'Deus vivo' — o Criador pessoal que age na história."),
                 ("Atos 14:19-20", "Sobrevieram, porém, judeus de Antioquia e de Icônio, os quais, persuadindo o povo, apedrejaram a Paulo, e o arrastaram para fora da cidade, cuidando que estava morto. Mas, rodeando-o os discípulos, levantou-se e entrou na cidade; e no dia seguinte partiu com Barnabé para Derbe.",
                  "A lapidação de Paulo em Listra é o ponto mais baixo da primeira viagem — e um cumprimento da profecia de 9:16 ('quanto lhe convém padecer'). Paulo lista esta lapidação em 2 Coríntios 11:25. O fato de que ele se levantou e entrou de volta na cidade no mesmo dia é extraordinário — alguns intérpretes veem aqui uma ressurreição ou cura milagrosa. O que é certo é que Paulo não fugiu — ele voltou para a cidade onde quase foi morto. No dia seguinte, partiu para Derbe — não para casa, mas para a próxima cidade da missão."),
             ]),
             ("🔙 O Retorno e o Relatório (14:21-28)", [
                 ("Atos 14:21-23", "E, tendo evangelizado aquela cidade e feito muitos discípulos, voltaram para Listra, e Icônio, e Antioquia, confirmando os ânimos dos discípulos, e exortando-os a que permanecessem na fé; e que por muitas tribulações nos convém entrar no reino de Deus. E, tendo-lhes constituído anciãos em cada igreja, e tendo orado com jejuns, os encomendaram ao Senhor em quem tinham crido.",
                  "O retorno de Paulo e Barnabé pelas cidades onde foram perseguidos é um ato de coragem pastoral extraordinário. Eles não apenas evangelizam — eles consolidam: 'confirmando os ânimos dos discípulos.' A mensagem de consolidação é honesta e dura: 'por muitas tribulações nos convém entrar no reino de Deus.' O discipulado não é prometido sem sofrimento — o sofrimento é o caminho, não a exceção. A constituição de 'anciãos' (<em>presbyterous</em>) em cada igreja estabelece a estrutura de liderança local — a Igreja não depende da presença contínua do missionário, mas de líderes locais formados e comissionados."),
             ]),
         ]),
}

def main():
    for num, (titulo, subtitulo, secoes) in CAPITULOS.items():
        html = gerar_html(num, titulo, subtitulo, secoes)
        filename = f"capitulo-{str(num).zfill(2)}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ Atos {str(num).zfill(2)} — {titulo[:50]}")
    print(f"\n🎉 Total gerado: {len(CAPITULOS)} capítulos de Atos (fase 1: 1-14)")

if __name__ == "__main__":
    main()
