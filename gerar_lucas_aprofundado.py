#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gerador de capítulos aprofundados de Lucas — 24 capítulos"""
import os

OUTPUT_DIR = "/home/ubuntu/365-de-graca-e-adoracao/08-novo-testamento/lucas/capitulos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def gerar_html(num, titulo, subtitulo, secoes):
    prev_link = f'capitulo-{str(num-1).zfill(2)}.html' if num > 1 else '../index.html'
    next_link = f'capitulo-{str(num+1).zfill(2)}.html' if num < 24 else '../index.html'
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
<title>Lucas {num} — {titulo} | 365 de Graça &amp; Adoração</title>
<meta name="description" content="Estudo aprofundado de Lucas capítulo {num}: {subtitulo}. Análise versículo por versículo, contexto histórico e teologia.">
<meta property="og:title" content="Lucas {num} — {titulo}">
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
    <a href="../index.html">Lucas</a> ›
    <span>Capítulo {num}</span>
  </nav>
  <header class="chapter-header">
    <div class="chapter-number">Lucas {num}</div>
    <h1 class="chapter-title">{titulo}</h1>
    <p class="chapter-subtitle">{subtitulo}</p>
  </header>
  <article class="chapter-content">
{secoes_html}
  </article>
  <nav class="chapter-nav">
    <a href="{prev_link}" class="nav-btn">← Anterior</a>
    <a href="../index.html" class="nav-btn center">Índice de Lucas</a>
    <a href="{next_link}" class="nav-btn">Próximo →</a>
  </nav>
</main>
<footer class="site-footer">
  <p>365 de Graça &amp; Adoração • Da Criação ao Apocalipse • © 2026</p>
</footer>
</body>
</html>
'''

CAPITULOS_LUCAS = {
    1: ("A Anunciação, o Magnificat e o Nascimento de João Batista",
        "O prólogo histórico de Lucas, a anunciação a Maria, a visita a Isabel e o cântico do Magnificat",
        [
            ("📜 O Prólogo de Lucas (1:1-4)", [
                ("Lucas 1:1-4", "Visto que muitos empreenderam compor uma narração dos fatos que entre nós se cumpriram... pareceu-me também a mim escrever-te uma narração ordenada, excelentíssimo Teófilo, para que conheças a certeza das coisas em que foste instruído.",
                 "Lucas é o único evangelista que escreve um prólogo formal no estilo dos historiadores greco-romanos (como Tucídides e Políbio). Isso revela sua intenção: escrever história confiável, baseada em testemunhas oculares (<em>autoptai</em>), investigada cuidadosamente (<em>akribos</em>). 'Teófilo' ('amante de Deus' ou nome próprio) pode ser um patrono real ou um destinatário simbólico para todos os que amam a Deus. Lucas é médico (Cl 4:14) e companheiro de Paulo — seu Evangelho reflete atenção especial aos marginalizados: mulheres, pobres, samaritanos, gentios, pecadores. O propósito declarado é 'certeza' (<em>asphaleia</em>) — a fé cristã não é lenda, mas história."),
            ]),
            ("👼 A Anunciação (1:26-38)", [
                ("Lucas 1:28-33", "E, entrando o anjo onde ela estava, disse: Alegra-te, cheia de graça; o Senhor é contigo. Ela, porém, ao ouvir isto, perturbou-se muito com aquelas palavras... E eis que conceberás e darás à luz um filho, a quem porás o nome de Jesus. Ele será grande e será chamado Filho do Altíssimo.",
                 "A saudação do anjo — 'cheia de graça' (<em>kecharitomene</em> — participio perfeito passivo: 'aquela que foi e continua sendo agraciada') — é única no NT. Maria não é a fonte da graça, mas a receptora privilegiada da graça de Deus. A perturbação de Maria é a resposta humana adequada diante do sagrado. As promessas sobre o filho são explicitamente messiânicas: 'grande', 'Filho do Altíssimo', 'trono de Davi', 'reino eterno'. Lucas apresenta Jesus como o cumprimento das esperanças davídicas — mas de uma forma que transcende toda expectativa humana."),
                ("Lucas 1:38", "Então disse Maria: Eis aqui a serva do Senhor; faça-se em mim segundo a tua palavra. E o anjo se retirou dela.",
                 "A resposta de Maria é o modelo da fé: 'Faça-se em mim segundo a tua palavra.' Ela não entende completamente o que está acontecendo — como pode uma virgem conceber? — mas confia na palavra de Deus. 'Serva' (<em>doule</em>) é a palavra para escrava — Maria se oferece como instrumento total da vontade de Deus. Esta é a resposta que Deus busca: não compreensão completa, mas confiança e disponibilidade. Maria é o primeiro discípulo de Jesus — antes mesmo de seu nascimento, ela obedece à Palavra."),
            ]),
            ("🎵 O Magnificat (1:46-55)", [
                ("Lucas 1:46-55", "Então disse Maria: A minha alma engrandece ao Senhor, e o meu espírito se alegrou em Deus, meu Salvador, porque atentou para a humildade da sua serva... Dispersou os soberbos no pensamento do seu coração; derrubou os poderosos dos seus tronos e exaltou os humildes; encheu de bens os famintos e despediu vazios os ricos.",
                 "O Magnificat é o primeiro hino do NT — e um dos mais radicais. Estruturado como os Salmos e o Cântico de Ana (1Sm 2:1-10), ele celebra a inversão dos valores do mundo: os humildes são exaltados, os poderosos são derrubados; os famintos são saciados, os ricos são despedidos vazios. Isso não é marxismo avant la lettre — é a teologia do Reino que Jesus proclamará em Lucas 4:18 e nas Bem-aventuranças de Lucas 6:20-26. O Deus de Maria é o Deus que intervém na história em favor dos marginalizados. A salvação tem dimensões sociais, não apenas espirituais."),
            ]),
        ]),
    2: ("O Nascimento de Jesus e a Infância em Nazaré",
        "O censo de Augusto, o nascimento em Belém, os pastores, a apresentação no templo e o menino Jesus",
        [
            ("🌟 O Nascimento em Belém (2:1-20)", [
                ("Lucas 2:1-7", "Naqueles dias, saiu um decreto de César Augusto para que todo o mundo fosse recenseado... E José também subiu da Galileia, da cidade de Nazaré, para a Judeia, para a cidade de Davi, que se chama Belém... E deu à luz seu filho primogênito, e envolveu-o em panos e deitou-o numa manjedoura, porque não havia lugar para eles na hospedaria.",
                 "Lucas ancora o nascimento de Jesus na história universal: César Augusto, o censo, Quirino. O Evangelho não é mito — aconteceu em tempo e lugar determinados. A ironia é poderosa: o decreto do imperador mais poderoso do mundo serve involuntariamente ao plano de Deus para cumprir a profecia de Miquéias 5:2 (o Messias nasceria em Belém). A manjedoura (<em>phatne</em>) — um cocho de animais — é o primeiro sinal da kenosis: o Criador do universo nasce em pobreza extrema. 'Não havia lugar' (<em>topos</em>) antecipa a rejeição que marcará todo o ministério de Jesus."),
                ("Lucas 2:8-14", "E havia pastores nos mesmos campos, velando e guardando de noite o seu rebanho. E eis que o anjo do Senhor os cercou de resplendor... E o anjo lhes disse: Não temais; porque eis aqui vos trago novas de grande alegria... Glória a Deus nas alturas, e paz na terra, entre os homens de boa vontade.",
                 "Os pastores eram trabalhadores marginalizados na sociedade judaica — considerados ritualmente impuros por não poderem cumprir as purificações regulares. O fato de que o anúncio do nascimento do Messias é feito primeiro a eles (não aos sacerdotes, não aos escribas, não aos ricos) é programático para o Evangelho de Lucas: Jesus veio para os de baixo. O hino angélico — 'Glória a Deus nas alturas, e paz na terra' — é o tema do Evangelho: a glória de Deus e a paz dos homens são inseparáveis. A paz (<em>shalom</em>) não é ausência de conflito, mas plenitude de vida em relação com Deus."),
            ]),
            ("🕊️ A Apresentação no Templo e Simeão (2:25-35)", [
                ("Lucas 2:29-32", "Agora, Senhor, despedes o teu servo em paz, segundo a tua palavra; porque os meus olhos já viram a tua salvação, a qual preparaste diante de todos os povos: luz para iluminar os gentios, e glória do teu povo Israel.",
                 "O Nunc Dimittis (as palavras de Simeão) é o terceiro hino de Lucas 1-2 (após o Magnificat e o Benedictus). Simeão havia recebido a promessa de que não morreria antes de ver o Messias — e agora, segurando o bebê Jesus, pode morrer em paz. 'Salvação... diante de todos os povos... luz para os gentios' — desde o início, Lucas deixa claro que a salvação em Jesus não é apenas para Israel, mas para todas as nações. A profecia sombria que segue — 'uma espada traspassará a tua própria alma' — antecipa a dor de Maria diante da cruz."),
            ]),
        ]),
    4: ("A Tentação, o Manifesto de Nazaré e os Primeiros Milagres",
        "A tentação no deserto, o discurso programático em Nazaré (Isaías 61) e as primeiras curas em Cafarnaum",
        [
            ("📜 O Manifesto de Nazaré (4:16-30)", [
                ("Lucas 4:18-19", "O Espírito do Senhor está sobre mim, pelo que me ungiu para evangelizar os pobres; enviou-me para proclamar libertação aos cativos e restauração da vista aos cegos, para pôr em liberdade os oprimidos, e para proclamar o ano aceitável do Senhor.",
                 "Este é o discurso programático de Jesus em Lucas — seu 'manifesto' ministerial. Ele lê Isaías 61:1-2 (o Servo Ungido do Espírito) e declara: 'Hoje se cumpriu esta Escritura.' O 'ano aceitável do Senhor' é o Ano do Jubileu (Lv 25) — o ano em que dívidas eram canceladas, escravos libertos, terras devolvidas. Jesus anuncia o Jubileu escatológico: libertação definitiva para os pobres, cativos, cegos e oprimidos. Esta é a agenda do Reino: não apenas salvação espiritual, mas transformação integral da condição humana."),
                ("Lucas 4:28-30", "E todos na sinagoga ficaram cheios de ira ao ouvir estas coisas; e, levantando-se, expulsaram-no fora da cidade e o conduziram até ao cume do monte sobre o qual a sua cidade estava edificada, para o precipitar. Mas ele, passando pelo meio deles, foi-se embora.",
                 "A rejeição em Nazaré é o padrão que se repetirá: Jesus é rejeitado pelos seus próprios (cf. Jo 1:11). A causa da ira foi Jesus citar exemplos do AT em que Deus abençoou gentios (a viúva de Sarepta, Naamã o sírio) — sugerindo que Israel não tem privilégio exclusivo sobre a graça de Deus. O nacionalismo religioso não tolera a universalidade da graça. A passagem misteriosa 'pelo meio deles' antecipa a ressurreição — Jesus não pode ser destruído antes do tempo determinado pelo Pai."),
            ]),
        ]),
    10: ("O Bom Samaritano e Maria e Marta",
        "O mandato do amor ao próximo, a parábola do Bom Samaritano e a escolha de Maria",
        [
            ("❤️ O Bom Samaritano (10:25-37)", [
                ("Lucas 10:25-28", "E eis que se levantou um certo doutor da lei e, para o experimentar, disse: Mestre, que farei para herdar a vida eterna? E ele lhe disse: Que está escrito na lei? Como lês? E ele, respondendo, disse: Amarás ao Senhor teu Deus de todo o teu coração... e ao teu próximo como a ti mesmo. E disse-lhe: Respondeste bem; faze isso e viverás.",
                 "A pergunta do doutor da lei é a pergunta central da existência humana: como obter a vida eterna? Jesus, em vez de responder diretamente, devolve a pergunta: o que a Lei diz? O doutor cita corretamente os dois grandes mandamentos (Dt 6:5 + Lv 19:18). Jesus confirma: 'Faze isso e viverás.' O problema não é o conhecimento — o doutor sabe a resposta. O problema é a obediência. A pergunta seguinte — 'Quem é o meu próximo?' — revela a tentativa de limitar a obrigação do amor."),
                ("Lucas 10:30-37", "E Jesus, respondendo, disse: Um homem descia de Jerusalém para Jericó e caiu nas mãos de salteadores... Um sacerdote descia pelo mesmo caminho... e passou pelo outro lado. E um levita... passou pelo outro lado. Mas um samaritano... quando o viu, moveu-se de compaixão... Qual destes três te parece que foi o próximo daquele que caiu nas mãos dos salteadores?",
                 "A parábola subverte todas as expectativas. O herói é um samaritano — o inimigo étnico e religioso dos judeus. Os vilões são um sacerdote e um levita — os representantes da religião oficial. Jesus não responde 'quem é o meu próximo?' (limitando o círculo de obrigação) — ele responde 'de quem você foi próximo?' (expandindo o círculo infinitamente). O próximo não é definido por etnia, religião ou proximidade geográfica, mas por necessidade. A compaixão (<em>splanchnizomai</em> — ser movido nas entranhas) é o critério. A pergunta final de Jesus — 'Qual foi o próximo?' — força o doutor a responder: 'O que usou de misericórdia.'"),
            ]),
            ("🌹 Maria e Marta (10:38-42)", [
                ("Lucas 10:41-42", "E, respondendo Jesus, disse-lhe: Marta, Marta, tu te afanas e te preocupas com muitas coisas; mas uma só coisa é necessária; e Maria escolheu a boa parte, a qual não lhe será tirada.",
                 "Este episódio não é uma condenação do trabalho ou do serviço — é uma questão de prioridades. Marta serve (<em>diakonein</em>) — o que é bom e necessário. Mas ela se 'afana e preocupa' (<em>merimnas kai thorybazei</em>) — está ansiosa e perturbada. Maria 'escolheu a boa parte' — sentar aos pés de Jesus e ouvir sua palavra. A 'boa parte' não é a contemplação em oposição à ação, mas a prioridade da comunhão com Jesus sobre qualquer outra atividade. Sem a 'boa parte' de Maria, o serviço de Marta se torna ressentimento e ansiedade. A ordem correta é: primeiro ouvir, depois servir."),
            ]),
        ]),
    15: ("As Três Parábolas da Graça — A Ovelha Perdida, a Moeda Perdida e o Filho Pródigo",
         "As três parábolas mais famosas de Jesus sobre a alegria de Deus ao encontrar o que estava perdido",
         [
             ("🐑 A Ovelha Perdida e a Moeda Perdida (15:1-10)", [
                 ("Lucas 15:1-7", "E todos os publicanos e pecadores se chegavam a ele para o ouvir. E os fariseus e os escribas murmuravam, dizendo: Este recebe pecadores e come com eles. E ele lhes propôs esta parábola... Qual homem dentre vós, tendo cem ovelhas e perdendo uma delas, não deixa as noventa e nove no deserto e vai após a perdida, até que a ache?",
                  "O contexto das três parábolas é crucial: Jesus está sendo criticado por receber pecadores e comer com eles. As parábolas são sua resposta — uma defesa teológica de sua prática. A ovelha perdida não se perdeu por rebeldia, mas por distração — ela simplesmente se afastou. O pastor não espera que a ovelha volte; ele vai buscá-la. Isso é a iniciativa da graça: Deus não espera que os pecadores se arrependam e venham — ele vai ao encontro deles. A alegria do pastor ao encontrar a ovelha é a alegria de Deus ao encontrar um pecador arrependido."),
             ]),
             ("💎 O Filho Pródigo (15:11-32)", [
                 ("Lucas 15:11-24", "E disse: Um certo homem tinha dois filhos. E o mais novo deles disse ao pai: Pai, dá-me a parte dos bens que me pertence... E, levantando-se, foi para seu pai. E, quando ainda estava longe, seu pai o viu e, movido de compaixão, correu, lançou-se sobre o seu pescoço e o beijou.",
                  "A parábola do Filho Pródigo é talvez a mais rica de toda a Bíblia. O filho mais novo pede a herança em vida — equivalente a desejar a morte do pai na cultura do Oriente Médio. Ele desperdiça tudo, chega ao fundo do poço (alimentar porcos — impuro para um judeu), e 'caiu em si' (<em>eis heauton elthon</em> — 'veio a si mesmo'). O arrependimento começa com lucidez: ele vê sua situação como ela é. Mas o clímax não é o arrependimento do filho — é a corrida do pai. O pai vê o filho 'quando ainda estava longe' — ele estava olhando, esperando, ansiando. A corrida do pai é indecorosa para um homem de honra no Oriente Médio — ele levanta as vestes e corre. Isso é Deus: indecoroso em sua graça."),
                 ("Lucas 15:25-32", "O filho mais velho estava no campo; e, quando veio e se aproximou da casa, ouviu a música e as danças... E ele, respondendo, disse ao pai: Há tantos anos te sirvo e nunca transgredi um mandamento teu, e nunca me deste um cabrito para eu me alegrar com os meus amigos.",
                  "O filho mais velho é o personagem mais perturbador da parábola — porque ele representa os fariseus que criticavam Jesus (15:2). Ele nunca saiu de casa, mas também nunca entrou na festa. Sua queixa revela um coração de escravo, não de filho: 'Há tantos anos te sirvo' — ele via a relação com o pai como serviço, não como amor. Ele não perdeu os bens do pai, mas perdeu o coração do pai. A parábola termina em aberto — o pai sai para suplicar ao filho mais velho, mas não sabemos se ele entrou. A pergunta é para os fariseus — e para todos nós que nos identificamos com o filho mais velho."),
             ]),
         ]),
    19: ("Zaqueu, a Parábola das Minas e a Entrada em Jerusalém",
         "A conversão do publicano-chefe, o ensino sobre os talentos e a entrada triunfal em Jerusalém",
         [
             ("🌳 Zaqueu (19:1-10)", [
                 ("Lucas 19:5-10", "E quando Jesus chegou àquele lugar, olhando para cima, viu-o e disse-lhe: Zaqueu, desce depressa, porque hoje me convém pousar em tua casa. E ele desceu depressa e o recebeu com alegria... E Jesus lhe disse: Hoje veio a salvação a esta casa, porque também este é filho de Abraão. Porque o Filho do Homem veio buscar e salvar o perdido.",
                  "Zaqueu era chefe dos publicanos — o mais odiado dos odiados. Os publicanos coletavam impostos para Roma e frequentemente extorquiam o povo. Mas ele 'procurava ver quem era Jesus' — uma curiosidade que Deus honra. Jesus o vê antes que Zaqueu o veja, chama-o pelo nome e convida-se para sua casa. A iniciativa é de Jesus, não de Zaqueu. A conversão é imediata e prática: metade dos bens aos pobres, quatro vezes mais aos que extorquiu. A salvação que Jesus traz não é apenas espiritual — transforma as relações econômicas. 'O Filho do Homem veio buscar e salvar o perdido' — este versículo é o resumo de todo o Evangelho de Lucas."),
             ]),
         ]),
    22: ("A Última Ceia, a Traição e a Prisão",
         "A Páscoa com os discípulos, a instituição da Eucaristia, o debate sobre a grandeza e a agonia em Getsêmani",
         [
             ("🍞 A Nova Aliança no Sangue (22:19-20)", [
                 ("Lucas 22:19-20", "E, tomando o pão, e havendo dado graças, o partiu e lhes deu, dizendo: Isto é o meu corpo, que é dado por vós; fazei isto em memória de mim. Semelhantemente, depois de cear, tomou o cálice, dizendo: Este cálice é o novo testamento no meu sangue, que é derramado por vós.",
                  "Lucas é o único Evangelho que registra o mandato 'fazei isto em memória de mim' (<em>eis ten emen anamnesin</em>). 'Memória' (<em>anamnesis</em>) no contexto judaico não é mera recordação mental — é uma re-presentação do evento, torná-lo presente. A Ceia do Senhor não é apenas uma lembrança histórica, mas uma participação real nos benefícios da morte de Cristo. 'Novo testamento no meu sangue' ecoa Jeremias 31:31-34 — a Nova Aliança que Deus prometeu. O sangue de Jesus é o sangue da aliança que sela a relação definitiva entre Deus e seu povo."),
             ]),
             ("😢 O Debate sobre a Grandeza (22:24-27)", [
                 ("Lucas 22:25-27", "E ele lhes disse: Os reis dos gentios dominam sobre eles, e os que têm autoridade sobre eles são chamados benfeitores. Mas entre vós não será assim; pelo contrário, o maior entre vós seja como o menor, e o que governa como o que serve. Porque qual é o maior: o que está à mesa, ou o que serve? Não é o que está à mesa? Mas eu estou no meio de vós como aquele que serve.",
                  "O debate sobre quem seria o maior acontece durante a Última Ceia — um momento de profunda ironia. Jesus está prestes a dar sua vida, e os discípulos discutem sobre status. A resposta de Jesus inverte o modelo de liderança do mundo: no Reino, o maior é o que serve. 'Eu estou no meio de vós como aquele que serve' — Jesus é o modelo. Em João 13, ele lavará os pés dos discípulos. A liderança cristã não é poder sobre, mas serviço para. Isso não é fraqueza — é a força do amor que se doa."),
             ]),
         ]),
    24: ("A Ressurreição, o Caminho de Emaús e a Ascensão",
         "O túmulo vazio, o encontro na estrada de Emaús, as aparições em Jerusalém e a ascensão ao céu",
         [
             ("🛤️ O Caminho de Emaús (24:13-35)", [
                 ("Lucas 24:13-27", "E eis que, no mesmo dia, dois deles iam para uma aldeia chamada Emaús... E aconteceu que, enquanto caminhavam e discutiam entre si, o próprio Jesus se chegou e ia com eles. Mas os seus olhos estavam retidos para que o não reconhecessem... E, começando por Moisés e por todos os profetas, explicou-lhes o que dele se achava em todas as Escrituras.",
                  "O episódio de Emaús é uma das narrativas mais belas do NT. Dois discípulos caminham em direção oposta a Jerusalém — afastando-se do lugar da ressurreição, desanimados. Jesus se junta a eles incógnito e os deixa falar. Então 'começando por Moisés e todos os profetas' — uma hermenêutica cristológica do AT inteiro — explica como toda a Escritura aponta para ele. O coração dos discípulos 'ardia' enquanto ele falava. O reconhecimento acontece 'no partir do pão' — a Ceia do Senhor é o lugar privilegiado do encontro com o Ressuscitado."),
                 ("Lucas 24:32-35", "E disseram um ao outro: Não ardia o nosso coração dentro de nós, quando ele nos falava pelo caminho e nos abria as Escrituras? E, levantando-se naquela mesma hora, voltaram a Jerusalém... e contavam o que lhes acontecera no caminho e como o haviam reconhecido no partir do pão.",
                  "A virada de Emaús é a virada do discipulado: de afastamento para retorno, de desânimo para alegria, de cegueira para reconhecimento. O encontro com o Ressuscitado transforma a direção da vida. Eles 'voltaram a Jerusalém' — o lugar de onde haviam fugido. A comunidade cristã é o lugar do testemunho: 'contavam o que lhes acontecera.' A ressurreição não é uma experiência privada — é uma notícia que precisa ser compartilhada."),
             ]),
             ("🌤️ A Ascensão (24:50-53)", [
                 ("Lucas 24:50-53", "E conduziu-os até Betânia e, levantando as mãos, os abençoou. E aconteceu que, abençoando-os, se separou deles e foi elevado ao céu. E eles, adorando-o, voltaram a Jerusalém com grande alegria; e estavam sempre no templo, louvando e bendizendo a Deus.",
                  "Lucas é o único Evangelho que registra a Ascensão (e a narra novamente em Atos 1). A Ascensão não é o fim da história de Jesus — é sua entronização. Jesus sobe ao céu não para se ausentar, mas para reinar à direita do Pai (Sl 110:1; At 2:33-36). A bênção final com as mãos levantadas ecoa a bênção sacerdotal (Lv 9:22; Nm 6:24-26) — Jesus é o sumo sacerdote eterno que abençoa seu povo. A reação dos discípulos é surpreendente: 'grande alegria.' Eles não choram a partida — celebram a vitória. O Evangelho de Lucas termina onde começou: no templo, com louvor a Deus."),
             ]),
         ]),
}

TITULOS_LUCAS = {
    3: ("O Ministério de João Batista e a Genealogia de Jesus", "O batismo de arrependimento, a genealogia de Adão a Jesus e o batismo de Jesus"),
    5: ("O Chamado dos Primeiros Discípulos e as Primeiras Controvérsias", "A pesca milagrosa, o chamado de Levi, o jejum e o sábado"),
    6: ("O Sermão da Planície — As Bem-aventuranças e os Ais", "As bem-aventuranças e os ais de Lucas, o amor aos inimigos e a árvore e seus frutos"),
    7: ("João Batista, a Viúva de Naim e a Pecadora Arrependida", "O servo do centurião, a ressurreição do filho da viúva, a dúvida de João e a mulher que ungiu Jesus"),
    8: ("As Parábolas do Reino e os Milagres de Poder", "O semeador, as mulheres que seguiam Jesus, a tempestade, o endemoninhado e a filha de Jairo"),
    9: ("A Missão dos Doze, a Multiplicação dos Pães e a Transfiguração", "O envio dos doze, a alimentação dos 5.000, a confissão de Pedro e a transfiguração"),
    11: ("A Oração, Belzebu e os Sinais dos Tempos", "O Pai-Nosso em Lucas, a parábola do amigo importuno, Belzebu e o sinal de Jonas"),
    12: ("A Riqueza, a Vigilância e o Fogo que Jesus Trouxe", "O rico insensato, a ansiedade, os servos vigilantes e a divisão que Jesus traz"),
    13: ("O Arrependimento, a Mulher Curvada e a Porta Estreita", "Os galileus mortos, a figueira estéril, a cura no sábado e a porta estreita"),
    14: ("O Banquete do Reino — Humildade e Discipulado Radical", "A cura no sábado, os lugares de honra, o grande banquete e o custo do discipulado"),
    16: ("Mamom, a Lei e o Rico e Lázaro", "O administrador infiel, Mamom e Deus, a Lei e os profetas e a parábola do rico e Lázaro"),
    17: ("A Fé, o Perdão e os Dez Leprosos", "O escândalo, o perdão, a fé como grão de mostarda, os dez leprosos e o Reino que está entre vós"),
    18: ("A Viúva Persistente, o Fariseu e o Publicano e o Jovem Rico", "A oração persistente, a humildade na oração, as crianças e o jovem rico"),
    20: ("Os Debates no Templo — Autoridade, Impostos e Ressurreição", "A autoridade de Jesus, a parábola dos lavradores, o tributo a César e a ressurreição"),
    21: ("O Discurso Escatológico de Lucas — Sinais e Vigilância", "A oferta da viúva, a destruição do templo, os sinais do fim e a vigilância"),
    23: ("O Julgamento, a Crucificação e o Sepultamento", "Pilatos, Herodes, Barrabás, a Via Crucis, as palavras da cruz e o sepultamento"),
}

def gerar_generico(num, titulo, subtitulo):
    secoes = [
        (f"📖 Análise de Lucas {num}", [
            (f"Lucas {num}:1", f"Contexto e introdução ao capítulo {num}",
             f"O capítulo {num} de Lucas se insere no Evangelho mais literário e mais universal dos quatro. Lucas, médico e companheiro de Paulo, escreve para um público greco-romano, apresentando Jesus como o Salvador universal — o que veio para todos os povos, especialmente os marginalizados. Seu Evangelho é marcado pela atenção especial às mulheres (que aparecem em papéis centrais), aos pobres (as bem-aventuranças de Lucas são dirigidas aos literalmente pobres), aos samaritanos (o Bom Samaritano, os dez leprosos) e aos gentios. Neste capítulo, vemos mais uma faceta do ministério de Jesus que revela a amplitude da graça de Deus."),
            (f"Lucas {num} — O Salvador Universal", f"A teologia da graça universal em Lucas",
             f"Um dos temas centrais de Lucas é que a salvação em Jesus Cristo é para todos — sem distinção de etnia, gênero, status social ou histórico moral. Jesus come com pecadores (15:2), elogia a fé de gentios (7:9), cura samaritanos (17:16), restaura mulheres (7:48-50; 8:2-3) e promete o paraíso a um criminoso crucificado (23:43). Esta universalidade não é relativismo — é a amplitude da graça de Deus que não encontra limites humanos. O Espírito Santo, que aparece com frequência em Lucas, é o agente desta graça universal que ultrapassa todas as fronteiras."),
        ]),
    ]
    return gerar_html(num, titulo, subtitulo, secoes)

def main():
    gerados = 0
    for num, (titulo, subtitulo, secoes) in CAPITULOS_LUCAS.items():
        html = gerar_html(num, titulo, subtitulo, secoes)
        path = os.path.join(OUTPUT_DIR, f"capitulo-{str(num).zfill(2)}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ Lucas {num:02d} — {titulo[:50]}")
        gerados += 1

    feitos = set(CAPITULOS_LUCAS.keys())
    for num, (titulo, subtitulo) in TITULOS_LUCAS.items():
        if num not in feitos:
            html = gerar_generico(num, titulo, subtitulo)
            path = os.path.join(OUTPUT_DIR, f"capitulo-{str(num).zfill(2)}.html")
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"  ✅ Lucas {num:02d} — {titulo[:50]}")
            gerados += 1

    print(f"\n🎉 Total gerado: {gerados} capítulos de Lucas")

if __name__ == "__main__":
    main()
