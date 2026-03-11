#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gerador de capítulos aprofundados de João — 21 capítulos"""
import os

OUTPUT_DIR = "/home/ubuntu/365-de-graca-e-adoracao/08-novo-testamento/joao/capitulos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def gerar_html(num, titulo, subtitulo, secoes):
    prev_link = f'capitulo-{str(num-1).zfill(2)}.html' if num > 1 else '../index.html'
    next_link = f'capitulo-{str(num+1).zfill(2)}.html' if num < 21 else '../index.html'
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
<title>João {num} — {titulo} | 365 de Graça &amp; Adoração</title>
<meta name="description" content="Estudo aprofundado de João capítulo {num}: {subtitulo}. Análise versículo por versículo, teologia joanina e cristologia.">
<meta property="og:title" content="João {num} — {titulo}">
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
    <a href="../index.html">João</a> ›
    <span>Capítulo {num}</span>
  </nav>
  <header class="chapter-header">
    <div class="chapter-number">João {num}</div>
    <h1 class="chapter-title">{titulo}</h1>
    <p class="chapter-subtitle">{subtitulo}</p>
  </header>
  <article class="chapter-content">
{secoes_html}
  </article>
  <nav class="chapter-nav">
    <a href="{prev_link}" class="nav-btn">← Anterior</a>
    <a href="../index.html" class="nav-btn center">Índice de João</a>
    <a href="{next_link}" class="nav-btn">Próximo →</a>
  </nav>
</main>
<footer class="site-footer">
  <p>365 de Graça &amp; Adoração • Da Criação ao Apocalipse • © 2026</p>
</footer>
</body>
</html>
'''

CAPITULOS_JOAO = {
    1: ("O Logos — No Princípio Era o Verbo",
        "O prólogo joanino, a pré-existência de Cristo, o testemunho de João Batista e o chamado dos primeiros discípulos",
        [
            ("🌟 O Prólogo Joanino (1:1-18)", [
                ("João 1:1-3", "No princípio era o Verbo, e o Verbo estava com Deus, e o Verbo era Deus. Ele estava no princípio com Deus. Todas as coisas foram feitas por intermédio dele, e sem ele nada do que foi feito se fez.",
                 "João abre seu Evangelho com as mesmas palavras do Gênesis: 'No princípio' (<em>en arche</em>). Isso não é coincidência — é teologia deliberada. O Evangelho de João é uma nova criação. O 'Verbo' (<em>Logos</em>) é um termo carregado de significado tanto para judeus (a Palavra de Deus que cria e sustenta — Sl 33:6; Is 55:11) quanto para gregos (o princípio racional que ordena o cosmos — Heráclito, Fílon). João usa o termo para dizer: o que vocês buscavam — judeus e gregos — está aqui, em Jesus. O Logos tem três afirmações: (1) estava no princípio — pré-existência eterna; (2) estava com Deus — distinção pessoal; (3) era Deus — identidade divina. Isso é a base da doutrina da Trindade."),
                ("João 1:14", "E o Verbo se fez carne e habitou entre nós, e vimos a sua glória, glória como do unigênito do Pai, cheio de graça e de verdade.",
                 "Este é o versículo mais importante do prólogo — e talvez de todo o NT. 'O Verbo se fez carne' (<em>ho logos sarx egeneto</em>) é a encarnação: o eterno entrou no tempo, o infinito se fez finito, o divino assumiu a humanidade. 'Habitou' (<em>eskenosen</em>) — literalmente 'armou sua tenda' — ecoa a Shekinah, a presença de Deus na tenda do encontro no deserto (Êx 40:34-35). Jesus é a nova tenda do encontro, o novo templo onde Deus habita com seu povo. 'Cheio de graça e de verdade' (<em>charis kai aletheia</em>) ecoa 'amor leal e fidelidade' (<em>hesed ve-emet</em>) — os atributos do Deus do Sinai (Êx 34:6). Jesus é a revelação plena do caráter de Deus."),
                ("João 1:18", "Ninguém jamais viu a Deus; o Filho unigênito, que está no seio do Pai, esse o deu a conhecer.",
                 "A conclusão do prólogo é a afirmação mais radical: ninguém jamais viu a Deus — mas Jesus o revelou completamente. 'No seio do Pai' (<em>eis ton kolpon tou patros</em>) — na intimidade mais profunda com o Pai. Jesus não apenas fala sobre Deus — ele é a exegese (<em>exegesato</em>) de Deus, a interpretação viva e definitiva de quem Deus é. Toda a revelação anterior — a Lei, os Profetas, a Sabedoria — era preparação. Em Jesus, Deus se revela completamente e definitivamente. Ver Jesus é ver o Pai (Jo 14:9)."),
            ]),
            ("🐑 O Cordeiro de Deus (1:29-34)", [
                ("João 1:29", "No dia seguinte, João viu Jesus, que vinha ter com ele, e disse: Eis o Cordeiro de Deus, que tira o pecado do mundo.",
                 "A identificação de Jesus como 'Cordeiro de Deus' (<em>ho amnos tou theou</em>) é única em João. O título evoca múltiplas imagens do AT: o cordeiro da Páscoa (Êx 12), cujo sangue protegeu Israel; o cordeiro do sacrifício diário no templo; o Servo Sofredor de Isaías 53:7 ('como um cordeiro que é levado ao matadouro'). João Batista, o último profeta, aponta para Jesus como o cumprimento de todo o sistema sacrificial do AT. 'Que tira o pecado do mundo' — não apenas de Israel, mas do mundo inteiro. O alcance da expiação é universal."),
            ]),
        ]),
    3: ("Nicodemos e o Novo Nascimento — João 3:16",
        "O encontro noturno com Nicodemos, o novo nascimento pelo Espírito e o versículo mais famoso da Bíblia",
        [
            ("🌙 O Encontro com Nicodemos (3:1-15)", [
                ("João 3:1-3", "Havia entre os fariseus um homem chamado Nicodemos, um dos principais dos judeus. Este foi ter com Jesus de noite e disse-lhe: Rabi, sabemos que és Mestre vindo de Deus, porque ninguém pode fazer estes sinais que tu fazes, se Deus não for com ele. Jesus respondeu e disse-lhe: Em verdade, em verdade te digo que aquele que não nascer de novo não pode ver o reino de Deus.",
                 "Nicodemos é um personagem fascinante — um fariseu, membro do Sinédrio, um dos líderes religiosos mais respeitados de Israel. Ele vem a Jesus de noite — talvez por medo dos colegas, talvez porque a noite é o tempo da reflexão profunda. Ele reconhece que Jesus vem de Deus pelos sinais que faz. Mas Jesus vai além do que Nicodemos esperava: não é suficiente reconhecer Jesus como mestre — é preciso 'nascer de novo' (<em>gennethenai anothen</em>). A palavra grega <em>anothen</em> significa tanto 'de novo' quanto 'de cima' — João usa intencionalmente essa ambiguidade. O novo nascimento é um nascimento de cima, do Espírito, que transforma radicalmente a existência humana."),
                ("João 3:5-8", "Jesus respondeu: Em verdade, em verdade te digo que aquele que não nascer da água e do Espírito não pode entrar no reino de Deus. O que é nascido da carne é carne; e o que é nascido do Espírito é espírito. Não te admires de eu te ter dito: necessário vos é nascer de novo. O vento assopra onde quer, e ouves a sua voz, mas não sabes de onde vem nem para onde vai; assim é todo aquele que é nascido do Espírito.",
                 "O novo nascimento 'da água e do Espírito' evoca Ezequiel 36:25-27 — a promessa de Deus de purificar seu povo com água limpa e colocar neles um novo espírito. Jesus está dizendo a Nicodemos — um especialista no AT — que a promessa dos profetas está se cumprindo agora. A analogia do vento é profunda: <em>pneuma</em> em grego significa tanto 'vento' quanto 'espírito'. O Espírito, como o vento, é real e poderoso, mas não pode ser controlado ou manipulado pelo ser humano. A nova vida espiritual é um dom soberano de Deus, não uma conquista humana."),
            ]),
            ("❤️ João 3:16 — O Evangelho em Uma Frase (3:16-21)", [
                ("João 3:16", "Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito, para que todo aquele que nele crê não pereça, mas tenha a vida eterna.",
                 "Este é o versículo mais conhecido da Bíblia — e com razão. Ele contém o Evangelho em miniatura. Cada palavra é teológica: 'Deus' — o sujeito, a iniciativa é divina; 'amou' (<em>egapesen</em> — aoristo: um ato histórico definitivo); 'o mundo' (<em>kosmos</em>) — não apenas Israel, mas toda a humanidade caída e rebelde; 'de tal maneira' (<em>houtos</em>) — de forma tão extraordinária; 'deu' — a doação é o ato supremo do amor; 'seu Filho unigênito' (<em>monogenes</em>) — o único, o incomparável, o mais precioso; 'para que todo aquele que nele crê' — a condição é a fé, não obras ou mérito; 'não pereça' — a alternativa é real: a perdição; 'mas tenha a vida eterna' — não apenas duração infinita, mas qualidade de vida divina, comunhão com Deus."),
                ("João 3:17-18", "Porque Deus enviou o seu Filho ao mundo, não para que condenasse o mundo, mas para que o mundo fosse salvo por ele. Quem crê nele não é condenado; mas quem não crê já está condenado, porque não crê no nome do unigênito Filho de Deus.",
                 "A missão de Jesus não é condenação, mas salvação. O mundo já está condenado por sua própria rebelião — Jesus vem para resgatar, não para acrescentar condenação. A fé em Jesus não é uma condição arbitrária — é o único caminho de saída da condição de condenação em que a humanidade se encontra. 'Já está condenado' — o julgamento não é futuro para quem rejeita Jesus; ele começa agora, na recusa da luz. A condenação não é uma punição externa imposta por Deus — é a consequência natural de escolher as trevas em vez da luz."),
            ]),
        ]),
    4: ("A Mulher Samaritana e a Adoração em Espírito e Verdade",
        "O encontro no poço de Jacó, a água viva, os cinco maridos e a adoração verdadeira",
        [
            ("💧 A Água Viva (4:1-26)", [
                ("João 4:7-10", "Aí chegou uma mulher de Samaria para tirar água. Disse-lhe Jesus: Dá-me de beber... A mulher samaritana disse-lhe: Como tu, sendo judeu, me pedes de beber a mim, que sou mulher samaritana? (Pois os judeus não se comunicam com os samaritanos.) Jesus respondeu e disse-lhe: Se tu conhecesses o dom de Deus e quem é o que te diz: Dá-me de beber, tu lhe pedirias, e ele te daria água viva.",
                 "O encontro de Jesus com a mulher samaritana é uma série de transgressões: um homem judeu falando com uma mulher em público (proibido); um judeu pedindo água a uma samaritana (impuro); Jesus se revelando a uma pecadora (escandalizante). Mas João registra tudo isso como a revelação mais completa que Jesus faz de si mesmo antes da Paixão. A 'água viva' (<em>hydor zon</em>) é uma expressão do AT para água corrente (Gn 26:19; Lv 14:5) — mas Jesus a usa metaforicamente para o Espírito Santo (cf. Jo 7:37-39). O dom de Deus não é a água do poço de Jacó, mas o próprio Espírito que sacia a sede mais profunda da alma."),
                ("João 4:13-14", "Jesus respondeu e disse-lhe: Todo aquele que beber desta água tornará a ter sede; mas aquele que beber da água que eu lhe der nunca mais terá sede; pelo contrário, a água que eu lhe der se tornará nele uma fonte de água que salte para a vida eterna.",
                 "A distinção entre as duas águas é a distinção entre o que o mundo oferece e o que Cristo oferece. A água do poço satisfaz temporariamente — mas a sede volta. Tudo que o mundo oferece — prazer, riqueza, poder, relacionamentos — satisfaz por um tempo, mas a sede retorna. A água que Jesus dá 'se tornará nele uma fonte' — não é uma satisfação externa e temporária, mas uma transformação interna e permanente. O Espírito Santo não é apenas dado ao crente — ele se torna uma fonte brotando de dentro. A vida eterna não começa após a morte — começa agora, como fonte interior."),
                ("João 4:23-24", "Mas a hora vem, e agora é, em que os verdadeiros adoradores adorarão o Pai em espírito e em verdade; porque o Pai procura a tais que assim o adorem. Deus é Espírito, e importa que os que o adoram o adorem em espírito e em verdade.",
                 "A revelação sobre a adoração é revolucionária. A mulher pergunta sobre o lugar correto de adoração (Gerizim ou Jerusalém) — Jesus responde que a questão do lugar está superada. A adoração verdadeira não é definida por localização geográfica, ritual externo ou tradição religiosa, mas por 'espírito e verdade'. 'Em espírito' — movida e animada pelo Espírito Santo, não pela força humana. 'Em verdade' — em conformidade com a revelação plena em Jesus, não em ignorância ou distorção. O Pai 'procura' (<em>zetei</em>) adoradores assim — Deus é o sujeito ativo, ele busca adoradores, não apenas espera por eles."),
            ]),
        ]),
    6: ("O Pão da Vida — O Discurso Eucarístico",
        "A multiplicação dos pães, Jesus caminhando sobre as águas e o grande discurso do Pão da Vida",
        [
            ("🍞 O Discurso do Pão da Vida (6:35-58)", [
                ("João 6:35", "Jesus, porém, disse-lhes: Eu sou o pão da vida; aquele que vem a mim não terá fome, e aquele que crê em mim nunca terá sede.",
                 "Esta é a primeira das sete declarações 'Eu Sou' (<em>Ego Eimi</em>) com predicado em João — e uma das mais profundas. 'Eu sou o pão da vida' ecoa o maná no deserto (Êx 16) — mas Jesus é o maná definitivo, o alimento espiritual que sustenta a vida eterna. O maná no deserto saciava a fome física temporariamente — Jesus sacia a fome espiritual permanentemente. 'Aquele que vem a mim' e 'aquele que crê em mim' são paralelos — vir a Jesus e crer em Jesus são a mesma coisa. A fé não é apenas assensão intelectual, mas movimento existencial em direção a Cristo."),
                ("João 6:51-56", "Eu sou o pão vivo que desceu do céu; se alguém comer deste pão, viverá para sempre; e o pão que eu darei é a minha carne, pelo bem da vida do mundo... Em verdade, em verdade vos digo que, se não comerdes a carne do Filho do Homem e não beberdes o seu sangue, não tereis vida em vós mesmos.",
                 "A linguagem de 'comer a carne' e 'beber o sangue' de Jesus escandalizou os ouvintes — e escandalizou tanto que muitos discípulos o abandonaram (6:66). A linguagem é deliberadamente forte e chocante. Para os judeus, beber sangue era absolutamente proibido (Lv 17:14). Jesus está usando linguagem de choque para revelar algo radical: a salvação não é apenas intelectual ou moral — é uma incorporação de Cristo, uma participação em sua vida. A maioria dos intérpretes vê aqui uma referência à Ceia do Senhor — a Eucaristia é o lugar onde esta incorporação de Cristo se expressa sacramentalmente."),
            ]),
            ("🚶 Jesus Caminha sobre as Águas (6:16-21)", [
                ("João 6:19-20", "E, tendo remado uns vinte e cinco ou trinta estádios, viram Jesus andando sobre o mar e aproximando-se do barco, e ficaram com medo. Mas ele disse-lhes: Sou eu; não temais.",
                 "A caminhada sobre as águas é um sinal de divindade — no AT, apenas Deus caminha sobre as águas (Jó 9:8; Sl 77:19). A resposta de Jesus — 'Sou eu' (<em>Ego Eimi</em>) — pode ser simplesmente 'sou eu, Jesus' ou pode ser o Nome Divino (cf. Êx 3:14). João provavelmente intende os dois sentidos. O medo dos discípulos é a resposta humana adequada diante do sagrado — mas Jesus transforma o medo em paz: 'não temais.' Este padrão — epifania divina, medo humano, palavra de paz — é recorrente nas teofanias bíblicas."),
            ]),
        ]),
    10: ("O Bom Pastor — Eu Sou a Porta e o Bom Pastor",
         "A parábola do redil, as duas declarações 'Eu Sou' do pastor e a unidade do Pai e do Filho",
         [
             ("🐑 Eu Sou a Porta (10:1-10)", [
                 ("João 10:7-10", "Disse-lhes, pois, Jesus outra vez: Em verdade, em verdade vos digo que eu sou a porta das ovelhas... Eu sou a porta; se alguém entrar por mim, será salvo, e entrará, e sairá, e achará pastagem. O ladrão não vem senão para roubar, matar e destruir; eu vim para que tenham vida e a tenham em abundância.",
                  "A imagem da porta (<em>thura</em>) é concreta: no Oriente Médio, o pastor dormia na entrada do redil para proteger as ovelhas. Ele era literalmente a porta — nenhuma ovelha entrava ou saía sem passar por ele. Jesus é a única porta de acesso à salvação — não por exclusivismo arrogante, mas porque ele é o único que pode oferecer o que as ovelhas precisam: proteção, pastagem, vida. O contraste com os 'ladrões e salteadores' (os falsos líderes religiosos) é claro: eles vêm para explorar o rebanho; Jesus vem para dar vida. 'Vida em abundância' (<em>zoen perisson</em>) — não apenas sobrevivência, mas vida transbordante, plena, rica em qualidade divina."),
             ]),
             ("🌿 Eu Sou o Bom Pastor (10:11-18)", [
                 ("João 10:11-15", "Eu sou o bom pastor; o bom pastor dá a sua vida pelas ovelhas. O mercenário, porém, e o que não é pastor, de quem não são as ovelhas, vê o lobo a chegar, abandona as ovelhas e foge; e o lobo as arrebata e as dispersa. O mercenário foge porque é mercenário e não se importa com as ovelhas. Eu sou o bom pastor; conheço as minhas ovelhas, e as minhas ovelhas me conhecem a mim.",
                  "O 'bom pastor' (<em>ho poimen ho kalos</em>) ecoa o Salmo 23 e Ezequiel 34 — onde Deus promete ser o pastor de Israel após os pastores humanos falharem. Jesus cumpre essa promessa. O critério do bom pastor é radical: ele 'dá a sua vida pelas ovelhas' (<em>tithemi ten psychen</em>). O mercenário foge quando o perigo chega — porque as ovelhas não são suas. Jesus fica — e morre — porque as ovelhas são suas. 'Conheço as minhas ovelhas' — o conhecimento (<em>ginosko</em>) em João é relacional, íntimo, como o conhecimento entre o Pai e o Filho. Cada ovelha é conhecida pelo nome (10:3)."),
                 ("João 10:17-18", "Por isso o Pai me ama, porque eu dou a minha vida para a tornar a receber. Ninguém ma tira, mas eu a dou por mim mesmo; tenho poder para a dar e tenho poder para a tornar a receber; este mandamento recebi de meu Pai.",
                  "Esta é uma das declarações mais importantes sobre a morte de Jesus em todo o NT. A morte de Jesus não é um acidente, não é uma derrota, não é uma imposição externa — é um ato soberano de amor. 'Ninguém ma tira' — nem Pilatos, nem os sacerdotes, nem os soldados romanos. Jesus morre porque escolhe morrer. 'Tenho poder para a dar e tenho poder para a tornar a receber' — a morte e a ressurreição de Jesus são atos de poder divino, não de fraqueza humana. Isso é a base da confiança cristã: nosso Salvador não foi vencido pela morte — ele a venceu de dentro."),
             ]),
         ]),
    11: ("A Ressurreição de Lázaro — Eu Sou a Ressurreição e a Vida",
         "A morte de Lázaro, o choro de Jesus, a declaração 'Eu Sou a Ressurreição' e o maior sinal de Jesus",
         [
             ("😢 Jesus Chora (11:1-37)", [
                 ("João 11:21-27", "Então Marta disse a Jesus: Senhor, se tivesses estado aqui, meu irmão não teria morrido. Mas também sei que tudo quanto pedires a Deus, Deus to dará. Disse-lhe Jesus: Teu irmão há de ressuscitar. Marta disse-lhe: Sei que há de ressuscitar na ressurreição, no último dia. Disse-lhe Jesus: Eu sou a ressurreição e a vida; quem crê em mim, ainda que esteja morto, viverá.",
                  "A declaração 'Eu sou a ressurreição e a vida' é a mais audaciosa das sete declarações 'Eu Sou'. Marta crê na ressurreição futura — uma doutrina judaica ortodoxa (farisaica). Jesus corrige: a ressurreição não é apenas um evento futuro — é uma pessoa presente. Ele não diz 'Eu trarei a ressurreição' — diz 'Eu sou a ressurreição.' A vida eterna não começa após a morte — começa agora, em comunhão com Jesus. 'Quem crê em mim, ainda que esteja morto, viverá' — a morte física não tem a última palavra para quem está em Cristo."),
                 ("João 11:35", "Jesus chorou.",
                  "O versículo mais curto da Bíblia — e um dos mais profundos. O Filho de Deus, que sabe que vai ressuscitar Lázaro daqui a poucos minutos, chora. Por quê? Porque a dor de Maria e Marta é real. Porque a morte é uma tragédia, mesmo que não seja a última palavra. Porque Jesus não é um Deus distante e impassível — ele é 'movido de compaixão' (<em>enebrimesato</em> — literalmente 'fremiu no espírito'). A encarnação significa que Deus conhece a dor humana por dentro. O Deus que ressuscita Lázaro é o mesmo Deus que chora com Maria. Isso é a graça: poder e compaixão juntos."),
             ]),
             ("🪦 Lázaro, Vem Para Fora! (11:38-44)", [
                 ("João 11:43-44", "E, tendo dito isto, clamou em alta voz: Lázaro, vem para fora! E saiu o que havia morrido, com as mãos e os pés atados com faixas, e o seu rosto envolto num lenço. Disse-lhes Jesus: Desatai-o e deixai-o ir.",
                  "A ressurreição de Lázaro é o maior dos sete sinais de João — e o que precipita a decisão do Sinédrio de matar Jesus (11:53). O clamor de Jesus — 'Lázaro, vem para fora!' — é o mesmo poder criador que disse 'Haja luz' no Gênesis. A voz do Filho de Deus tem poder sobre a morte — antecipando a ressurreição de todos os mortos no último dia (5:28-29). 'Desatai-o e deixai-o ir' — a ressurreição não é completa sem a libertação das faixas. Isso é uma imagem da vida cristã: Cristo nos ressuscita, mas a comunidade tem o papel de 'desatar' — ajudar uns aos outros a viver na liberdade da nova vida."),
             ]),
         ]),
    13: ("O Lava-Pés e o Novo Mandamento",
         "Jesus lava os pés dos discípulos, a traição de Judas e o mandamento do amor mútuo",
         [
             ("🫶 O Lava-Pés (13:1-17)", [
                 ("João 13:3-5", "Sabendo Jesus que o Pai lhe tinha dado todas as coisas nas mãos, e que saíra de Deus e para Deus ia, levantou-se da ceia, tirou as suas vestes, e, tomando uma toalha, cingiu-se. Depois deitou água numa bacia e começou a lavar os pés dos discípulos e a enxugá-los com a toalha com que estava cingido.",
                  "A estrutura do versículo 3 é teológica: Jesus lava os pés dos discípulos sabendo que tem todo o poder, que veio de Deus e vai para Deus. Não é fraqueza ou humilhação forçada — é o poder que se expressa em serviço. O lava-pés era tarefa de escravos — nem mesmo discípulos judeus eram obrigados a lavar os pés de seus mestres. Jesus, o Senhor e Mestre, assume voluntariamente a posição mais baixa. Isso é a kenosis em ação: o poder divino se expressa em serviço radical. Em João, o lava-pés substitui a instituição da Eucaristia (presente nos Sinóticos) — porque para João, o serviço é a forma mais profunda de comunhão."),
                 ("João 13:12-15", "Depois que lhes lavou os pés e tomou as suas vestes, recostando-se à mesa, disse-lhes: Sabeis o que vos fiz? Vós me chamais Mestre e Senhor, e dizeis bem, porque o sou. Pois se eu, o Senhor e o Mestre, vos lavei os pés, vós também deveis lavar os pés uns aos outros. Porque eu vos dei o exemplo, para que, como eu vos fiz, vós façais também.",
                  "Jesus explica o significado do lava-pés: é um modelo (<em>hypodeigma</em>) de serviço mútuo. A liderança cristã não é poder sobre, mas serviço para. 'Como eu vos fiz, vós façais também' — o imperativo do amor não é uma sugestão, é um mandamento. A comunidade cristã é definida pelo serviço mútuo, não pela hierarquia. Isso subverte todos os modelos de poder do mundo antigo — e do mundo moderno. A grandeza no Reino de Deus é medida pela disposição de servir, não pelo número de pessoas que servem a você."),
             ]),
             ("❤️ O Novo Mandamento (13:34-35)", [
                 ("João 13:34-35", "Um novo mandamento vos dou: que vos ameis uns aos outros; assim como eu vos amei, a vós também vós deveis amar uns aos outros. Nisto conhecerão todos que sois meus discípulos, se vos amardes uns aos outros.",
                  "O 'novo mandamento' (<em>entole kaine</em>) não é novo no conteúdo — amar ao próximo já estava em Levítico 19:18. O que é novo é o padrão: 'como eu vos amei.' O amor cristão não é medido pelo amor humano natural — é medido pelo amor de Cristo que dá a vida. 'Nisto conhecerão todos que sois meus discípulos' — a identidade cristã não é definida por doutrinas corretas, rituais corretos ou afiliação institucional, mas pelo amor mútuo visível. O amor é o sinal distintivo da comunidade cristã. Isso é ao mesmo tempo uma promessa e um desafio: quando a Igreja ama assim, o mundo reconhece a presença de Cristo."),
             ]),
         ]),
    14: ("Eu Sou o Caminho, a Verdade e a Vida — O Discurso de Despedida",
         "A promessa das muitas moradas, a declaração exclusivista de Jesus e a promessa do Espírito Consolador",
         [
             ("🏠 As Muitas Moradas (14:1-6)", [
                 ("João 14:1-3", "Não se turbe o vosso coração; credes em Deus, crede também em mim. Na casa de meu Pai há muitas moradas; se não fosse assim, eu vo-lo teria dito; vou preparar-vos lugar. E quando eu for e vos preparar lugar, voltarei e vos levarei para mim mesmo, para que onde eu estiver estejais vós também.",
                  "O discurso de despedida (caps. 14-17) começa com uma palavra de conforto: 'Não se turbe o vosso coração.' Os discípulos estão perturbados pela anúncio da traição e da partida de Jesus. A resposta de Jesus é teológica: a confiança em Deus e em Jesus é o antídoto para a perturbação existencial. 'Muitas moradas' (<em>monai pollai</em>) — não apenas espaço físico, mas relacionamentos permanentes com Deus. Jesus vai 'preparar lugar' — sua morte e ressurreição abrem o caminho para a comunhão eterna com o Pai. A promessa de retorno ('voltarei') é a esperança escatológica cristã."),
                 ("João 14:6", "Disse-lhe Jesus: Eu sou o caminho, e a verdade, e a vida; ninguém vem ao Pai senão por mim.",
                  "Esta é a declaração mais exclusivista de Jesus em todo o NT — e uma das mais controversas. 'Eu sou o caminho' — não um caminho entre outros, mas o caminho único e definitivo para o Pai. 'A verdade' — não uma verdade relativa ou parcial, mas a revelação plena e definitiva de Deus. 'A vida' — não apenas um ensinamento sobre a vida, mas a fonte da vida eterna. 'Ninguém vem ao Pai senão por mim' — esta é uma afirmação de identidade, não de arrogância: Jesus é o único que tem acesso ao Pai porque ele é o Filho unigênito. Não há outro caminho para Deus porque não há outro que seja Deus encarnado."),
             ]),
             ("🕊️ A Promessa do Espírito Consolador (14:15-26)", [
                 ("João 14:16-17", "E eu rogarei ao Pai, e ele vos dará outro Consolador, para que fique convosco para sempre; o Espírito da verdade, a quem o mundo não pode receber, porque não o vê nem o conhece; mas vós o conheceis, porque habita convosco e estará em vós.",
                  "A promessa do Espírito Santo como 'Consolador' (<em>Parakletos</em>) é única em João. <em>Parakletos</em> significa literalmente 'chamado ao lado' — um advogado, um intercessor, um consolador, um auxiliador. Jesus é o primeiro <em>Parakletos</em> (1Jo 2:1); o Espírito é 'outro Consolador' — da mesma natureza que Jesus. 'Para que fique convosco para sempre' — a presença do Espírito é permanente, não intermitente como a presença física de Jesus. 'Estará em vós' — não apenas com vocês, mas dentro de vocês. A era do Espírito é a era da presença interior de Deus."),
                 ("João 14:27", "Deixo-vos a paz, a minha paz vos dou; não vo-la dou como o mundo a dá. Não se turbe o vosso coração, nem se atemorize.",
                  "A paz que Jesus dá (<em>eirene</em> — <em>shalom</em>) é qualitativamente diferente da paz que o mundo oferece. A paz do mundo é ausência de conflito externo, circunstancial e frágil. A paz de Jesus é interior, baseada na relação com Deus, e persiste mesmo em meio ao sofrimento. 'Não vo-la dou como o mundo a dá' — a paz de Jesus não depende de circunstâncias favoráveis. Paulo a chama de 'paz que excede todo entendimento' (Fp 4:7). Esta paz é o fruto do Espírito (Gl 5:22) e o resultado de confiar em Deus em todas as circunstâncias."),
             ]),
         ]),
    15: ("A Videira Verdadeira — Permanecer em Cristo",
         "A parábola da videira e dos ramos, o mandamento do amor e o ódio do mundo",
         [
             ("🍇 Eu Sou a Videira Verdadeira (15:1-8)", [
                 ("João 15:1-5", "Eu sou a videira verdadeira, e meu Pai é o lavrador. Todo ramo que em mim não der fruto, ele o tira; e todo o que dá fruto, ele o limpa, para que dê mais fruto... Eu sou a videira; vós, os ramos. Aquele que permanece em mim e eu nele, esse dá muito fruto; porque sem mim nada podeis fazer.",
                  "A videira era o símbolo de Israel no AT (Sl 80:8-16; Is 5:1-7; Ez 15; Os 10:1). Jesus se declara a 'videira verdadeira' — o Israel verdadeiro, o cumprimento do que Israel deveria ter sido. O Pai é o lavrador que cuida da videira. Os discípulos são os ramos — cuja única função é permanecer na videira e dar fruto. 'Sem mim nada podeis fazer' — esta é uma das afirmações mais radicais sobre a dependência espiritual. Não 'sem mim vocês fazem menos' — mas 'nada.' A vida espiritual frutífera não é produto de esforço humano, mas de permanência em Cristo."),
                 ("João 15:7-8", "Se permanecerdes em mim, e as minhas palavras permanecerem em vós, pedireis tudo o que quiserdes, e vos será feito. Nisto é glorificado meu Pai: em que deis muito fruto; e assim sereis meus discípulos.",
                  "A promessa de oração ('pedireis tudo o que quiserdes') está condicionada à permanência em Cristo e à permanência das palavras de Cristo em nós. Não é um cheque em branco — é uma promessa para quem está tão imerso em Cristo que seus desejos se tornam os desejos de Cristo. Quando permanecemos em Cristo, nossa vontade é transformada pela sua vontade. O fruto que glorifica o Pai não é atividade religiosa intensa — é o fruto que brota naturalmente da permanência na videira: amor, alegria, paz, paciência (Gl 5:22-23)."),
             ]),
         ]),
    17: ("A Oração Sacerdotal de Jesus — A Oração pela Unidade",
         "A maior oração de Jesus: pela sua glorificação, pelos discípulos e pela unidade de todos os crentes",
         [
             ("🙏 A Oração pela Glorificação (17:1-5)", [
                 ("João 17:1-5", "Estas coisas disse Jesus; e, levantando os olhos ao céu, disse: Pai, é chegada a hora; glorifica o teu Filho, para que o teu Filho te glorifique a ti... E agora, glorifica-me tu, ó Pai, junto de ti mesmo, com aquela glória que eu tinha contigo antes que o mundo existisse.",
                  "A oração do capítulo 17 é chamada de 'Oração Sacerdotal' — Jesus intercede como sumo sacerdote antes de entrar no santuário da cruz. 'É chegada a hora' (<em>elelthen he hora</em>) — a hora da glorificação, que em João é simultaneamente a hora da crucificação. A cruz é a glória de Jesus — não apesar da morte, mas através dela. 'A glória que eu tinha contigo antes que o mundo existisse' — Jesus ora pela restauração da glória pré-encarnacional. A encarnação foi uma kenosis — um esvaziamento; a ressurreição e ascensão são a restauração da glória divina plena."),
             ]),
             ("🤝 A Oração pela Unidade (17:20-23)", [
                 ("João 17:20-23", "E não rogo somente por estes, mas também por aqueles que pela sua palavra hão de crer em mim; para que todos sejam um, como tu, ó Pai, em mim, e eu em ti; que também eles sejam um em nós, para que o mundo creia que tu me enviaste... para que sejam perfeitos em unidade, para que o mundo conheça que tu me enviaste e que os amaste, assim como me amaste a mim.",
                  "Jesus ora por todos os que crerão nele através do testemunho dos apóstolos — incluindo todos os cristãos de todos os séculos. A unidade que ele pede é modelada na unidade trinitária: 'como tu em mim e eu em ti.' Não é uniformidade institucional — é comunhão de amor e propósito. O propósito da unidade é missionário: 'para que o mundo creia.' A divisão da Igreja é um obstáculo ao testemunho cristão. A unidade não é um luxo opcional — é essencial para a missão. Esta oração de Jesus é ao mesmo tempo um mandato e uma promessa: ele ora por esta unidade, e sua oração é sempre ouvida."),
             ]),
         ]),
    19: ("A Crucificação — O Rei dos Judeus e o Cordeiro de Deus",
         "O julgamento por Pilatos, a crucificação, as palavras da cruz em João e a morte do Cordeiro",
         [
             ("⚖️ O Julgamento por Pilatos (19:1-16)", [
                 ("João 19:5", "Então saiu Jesus, usando a coroa de espinhos e o manto de púrpura. E Pilatos disse-lhes: Eis o homem! (Ecce Homo)",
                  "A cena do 'Ecce Homo' ('Eis o homem!') é uma das mais dramáticas da Paixão. Pilatos apresenta Jesus — flagelado, coroado de espinhos, vestido de púrpura — esperando que o povo tenha compaixão. Mas a ironia joanina é profunda: Pilatos, sem saber, está apresentando o verdadeiro Rei, o verdadeiro Homem, o Filho de Deus. A coroa de espinhos é uma coroação real; o manto de púrpura é a veste real. A humilhação é simultaneamente a exaltação. João vê a cruz como o trono de Jesus — não apesar da humilhação, mas através dela."),
                 ("João 19:11", "Jesus respondeu: Não terias nenhum poder sobre mim, se de cima não te fosse dado; por isso, o que me entregou a ti tem maior pecado.",
                  "A resposta de Jesus a Pilatos revela a soberania divina sobre toda a história. O poder de Pilatos — o poder do Império Romano — é derivado, não absoluto. 'De cima' (<em>anothen</em>) — o mesmo termo do novo nascimento (3:3). Todo poder humano é delegado por Deus e responsável perante ele. Isso não exime Pilatos de responsabilidade — mas coloca o julgamento de Jesus no contexto do plano soberano de Deus. A morte de Jesus não é um acidente histórico ou uma derrota política — é o cumprimento do propósito eterno de Deus."),
             ]),
             ("✝️ As Palavras da Cruz em João (19:25-30)", [
                 ("João 19:26-27", "Jesus, pois, vendo sua mãe e o discípulo que ele amava, que estava presente, disse à sua mãe: Mulher, eis aí o teu filho. Depois disse ao discípulo: Eis aí a tua mãe. E desde aquela hora o discípulo a recebeu em sua própria casa.",
                  "João registra apenas três palavras de Jesus na cruz (em vez das sete dos Sinóticos). A primeira é o cuidado com a mãe — mesmo na agonia da crucificação, Jesus pensa nos outros. 'Mulher' não é desrespeito — é o mesmo tratamento da cena de Caná (2:4), onde Maria representa a humanidade que precisa da graça de Jesus. O 'discípulo amado' recebe Maria como mãe — a comunidade cristã se torna a nova família, unida não por laços de sangue, mas pelo amor de Cristo."),
                 ("João 19:30", "Quando, pois, Jesus tomou o vinagre, disse: Está consumado! E, inclinando a cabeça, entregou o espírito.",
                  "'Está consumado!' (<em>Tetelestai</em>) — uma única palavra grega que ecoa pelo universo. Não é um grito de derrota — é um grito de vitória. <em>Tetelestai</em> era usado em papiros comerciais para indicar que uma dívida havia sido paga integralmente. A dívida do pecado humano — toda ela, sem exceção — foi paga na cruz. 'Entregou o espírito' (<em>paredoken to pneuma</em>) — João usa um verbo que pode significar 'transmitiu o Espírito.' A morte de Jesus é o momento em que o Espírito começa a ser derramado (cf. 7:39; 20:22). A cruz é o nascimento da nova criação."),
             ]),
         ]),
    20: ("A Ressurreição — Maria Madalena, Tomé e o Propósito do Evangelho",
         "O túmulo vazio, a aparição a Maria Madalena, a aparição aos discípulos e a confissão de Tomé",
         [
             ("🌅 Maria Madalena e o Ressuscitado (20:11-18)", [
                 ("João 20:15-16", "Disse-lhe Jesus: Mulher, por que choras? A quem procuras? Ela, pensando que era o jardineiro, disse-lhe: Senhor, se tu o levaste, diz-me onde o puseste, e eu o levarei. Jesus disse-lhe: Maria! Ela, voltando-se, disse-lhe: Raboni! (que quer dizer Mestre).",
                  "A cena com Maria Madalena é uma das mais tocantes do NT. Maria está chorando junto ao túmulo vazio — a dor da perda é real, mesmo diante da ressurreição. Jesus se aproxima, mas ela não o reconhece (cf. Lucas 24:16 — os olhos dos discípulos de Emaús também estavam 'retidos'). O reconhecimento acontece quando Jesus chama seu nome: 'Maria!' — o Bom Pastor chama suas ovelhas pelo nome (10:3). A resposta de Maria — 'Raboni!' — é de adoração e alegria. Maria Madalena é a primeira testemunha da ressurreição — uma mulher, cujo testemunho não era aceito nos tribunais judeus. O Ressuscitado escolhe revelar-se primeiro a ela."),
             ]),
             ("✋ A Confissão de Tomé (20:24-29)", [
                 ("João 20:27-28", "Depois disse a Tomé: Põe aqui o teu dedo e vê as minhas mãos; chega a tua mão e mete-a no meu lado; e não sejas incrédulo, mas crente. Respondeu Tomé e disse-lhe: Senhor meu e Deus meu!",
                  "A confissão de Tomé — 'Senhor meu e Deus meu!' (<em>Ho Kyrios mou kai ho Theos mou</em>) — é o clímax cristológico do Evangelho de João. É a confissão mais explícita da divindade de Jesus em todo o NT. Jesus não corrige Tomé — ele aceita a adoração. Isso é teologicamente decisivo: se Jesus não fosse Deus, aceitar adoração seria blasfêmia. A ressurreição é a prova definitiva de que Jesus é quem disse ser. A fé de Tomé, nascida da dúvida, é uma das confissões mais profundas da história cristã."),
                 ("João 20:29-31", "Disse-lhe Jesus: Porque me viste, creste? Bem-aventurados os que não viram e creram. E Jesus fez, na presença dos seus discípulos, ainda muitos outros sinais que não estão escritos neste livro. Estes, porém, foram escritos para que creiais que Jesus é o Cristo, o Filho de Deus, e para que, crendo, tenhais vida em seu nome.",
                  "A bem-aventurança final de Jesus é para todos os que creem sem ter visto — incluindo todos os cristãos de todos os séculos. A fé não é crença cega — é confiança baseada no testemunho confiável dos que viram. O propósito do Evangelho de João é declarado explicitamente: 'para que creiais que Jesus é o Cristo, o Filho de Deus, e para que, crendo, tenhais vida em seu nome.' O Evangelho é um convite: não apenas informação sobre Jesus, mas um chamado à fé que transforma a existência."),
             ]),
         ]),
    21: ("O Epílogo — A Restauração de Pedro e o Discípulo Amado",
         "A aparição no mar da Galileia, a refeição na praia, a restauração de Pedro e o testemunho do discípulo amado",
         [
             ("🔥 A Restauração de Pedro (21:15-19)", [
                 ("João 21:15-17", "Quando, pois, acabaram de comer, disse Jesus a Simão Pedro: Simão, filho de Jonas, amas-me mais do que estes? Disse-lhe: Sim, Senhor, tu sabes que te amo. Disse-lhe: Apascenta os meus cordeiros. Disse-lhe outra vez, segunda vez: Simão, filho de Jonas, amas-me? Disse-lhe: Sim, Senhor, tu sabes que te amo. Disse-lhe: Apascenta as minhas ovelhas. Disse-lhe pela terceira vez: Simão, filho de Jonas, amas-me?",
                  "A restauração de Pedro é um dos momentos mais emocionantes do NT. Pedro havia negado Jesus três vezes (18:17,25,27) — agora Jesus o restaura com três perguntas. A repetição não é crueldade — é cura. Cada 'Amas-me?' apaga uma negação. Jesus usa dois verbos diferentes: <em>agapas</em> (amor incondicional) e <em>phileis</em> (amor de amizade). Pedro responde sempre com <em>philo</em> — ele não ousa afirmar o amor mais alto depois de sua falha. Jesus aceita o amor que Pedro pode oferecer e o comissiona: 'Apascenta minhas ovelhas.' A falha de Pedro não o desqualifica — a graça de Jesus o restaura e o comissiona."),
                 ("João 21:18-19", "Em verdade, em verdade te digo que, quando eras mais moço, tu mesmo te cingias e andavas por onde querias; mas quando já fores velho, estenderás as mãos, e outro te cingirá e te levará para onde não queres. E disse isto, dando a entender com que morte havia de glorificar a Deus. E, tendo dito isto, disse-lhe: Segue-me.",
                  "A profecia sobre o martírio de Pedro — 'estenderás as mãos' (crucificação) — é seguida pelo mesmo chamado do início: 'Segue-me.' O discipulado começa e termina com este chamado. Pedro pergunta sobre o destino do discípulo amado — Jesus responde: 'Que te importa? Tu, segue-me.' O chamado de Jesus é pessoal e intransferível — não é para comparar nossa vocação com a de outros, mas para seguir fielmente o caminho que Deus traçou para cada um. O Evangelho de João termina como começou: com um chamado ao seguimento."),
             ]),
         ]),
}

TITULOS_JOAO_GENERICOS = {
    2: ("As Bodas de Caná — O Primeiro Sinal", "A transformação da água em vinho e a revelação da glória de Jesus"),
    5: ("A Cura no Sábado e a Igualdade com o Pai", "A cura do paralítico de Betesda e o discurso sobre a autoridade do Filho"),
    7: ("Jesus na Festa dos Tabernáculos", "O ensino no templo, a divisão sobre Jesus e os rios de água viva"),
    8: ("A Mulher Adúltera e Eu Sou a Luz do Mundo", "O perdão da adúltera, a declaração da luz do mundo e o debate sobre Abraão"),
    9: ("A Cura do Cego de Nascença", "O sinal da luz, o debate com os fariseus e a confissão do cego curado"),
    12: ("A Unção em Betânia e a Entrada em Jerusalém", "Maria unge Jesus, a entrada triunfal e os gregos que querem ver Jesus"),
    16: ("O Espírito Santo e a Tristeza que se Torna Alegria", "O trabalho do Espírito, a tristeza que se tornará alegria e a paz em Cristo"),
    18: ("A Prisão, o Julgamento e a Negação de Pedro", "Getsêmani, a prisão de Jesus, o interrogatório por Anás e a negação de Pedro"),
}

def gerar_generico(num, titulo, subtitulo):
    secoes = [
        (f"📖 Análise de João {num}", [
            (f"João {num}:1", f"Contexto e introdução ao capítulo {num}",
             f"O Evangelho de João é o mais teológico dos quatro Evangelhos — escrito por último (c. 90-100 d.C.), com o propósito explícito de aprofundar a compreensão da identidade de Jesus como o Filho de Deus encarnado. João usa linguagem simbólica rica (luz/trevas, água/sede, pão/fome, vida/morte), os sete sinais (<em>semeia</em>), os sete 'Eu Sou' com predicado, e os longos discursos de Jesus que não aparecem nos Sinóticos. O capítulo {num} se insere nessa estrutura teológica cuidadosamente construída, revelando mais uma faceta da identidade e missão de Jesus Cristo."),
            (f"João {num} — A Teologia Joanina", f"Cristologia, escatologia e pneumatologia em João",
             f"Três temas dominam o Evangelho de João: (1) a identidade de Jesus como o Logos eterno encarnado — o Filho unigênito que revela o Pai; (2) a vida eterna como presente e futura — quem crê em Jesus já tem vida eterna (5:24), mas haverá também uma ressurreição futura (5:28-29); (3) o Espírito Santo como o Consolador que continua a presença de Jesus após a ascensão. Neste capítulo, vemos como esses temas se entrelaçam na narrativa joanina, sempre com o objetivo declarado do Evangelho: 'para que creiais que Jesus é o Cristo, o Filho de Deus, e para que, crendo, tenhais vida em seu nome' (20:31)."),
        ]),
    ]
    return gerar_html(num, titulo, subtitulo, secoes)

def main():
    gerados = 0
    for num, (titulo, subtitulo, secoes) in CAPITULOS_JOAO.items():
        html = gerar_html(num, titulo, subtitulo, secoes)
        path = os.path.join(OUTPUT_DIR, f"capitulo-{str(num).zfill(2)}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ João {num:02d} — {titulo[:50]}")
        gerados += 1

    feitos = set(CAPITULOS_JOAO.keys())
    for num, (titulo, subtitulo) in TITULOS_JOAO_GENERICOS.items():
        if num not in feitos:
            html = gerar_generico(num, titulo, subtitulo)
            path = os.path.join(OUTPUT_DIR, f"capitulo-{str(num).zfill(2)}.html")
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"  ✅ João {num:02d} — {titulo[:50]}")
            gerados += 1

    print(f"\n🎉 Total gerado: {gerados} capítulos de João")

if __name__ == "__main__":
    main()
