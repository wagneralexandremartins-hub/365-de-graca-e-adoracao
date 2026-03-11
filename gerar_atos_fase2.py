#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gerador de capítulos aprofundados de Atos — Fase 2: caps. 15–28"""
import os

OUTPUT_DIR = "/home/ubuntu/365-de-graca-e-adoracao/08-novo-testamento/atos/capitulos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def gerar_html(num, titulo, subtitulo, secoes):
    prev_link = f'capitulo-{str(num-1).zfill(2)}.html'
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
<meta name="description" content="Estudo aprofundado de Atos capítulo {num}: {subtitulo}. Análise versículo por versículo, contexto histórico e teologia missionária.">
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
    15: ("O Concílio de Jerusalém — A Grande Decisão",
         "O debate sobre a circuncisão, os discursos de Pedro e Tiago, e a carta apostólica aos gentios",
         [
             ("⚖️ O Conflito Teológico (15:1-5)", [
                 ("Atos 15:1-2", "E alguns que tinham descido da Judeia ensinavam os irmãos: Se não vos circuncidardes segundo o costume de Moisés, não podeis ser salvos. Tendo, pois, Paulo e Barnabé não pequena contenda e discussão com eles, determinaram que Paulo e Barnabé, e alguns outros deles, subissem a Jerusalém, aos apóstolos e presbíteros, acerca desta questão.",
                  "O Concílio de Jerusalém (c. 49 d.C.) é o primeiro concílio da Igreja cristã — e o modelo para todos os que se seguiram. A questão em debate é a mais fundamental possível: o que é necessário para a salvação? Os judaizantes (cristãos judeus de Jerusalém) insistiam que a circuncisão era necessária para a salvação — a fé em Jesus não era suficiente. Paulo e Barnabé resistem vigorosamente: isso seria um 'evangelho diferente' (Gl 1:6-9), uma negação da suficiência da graça. A solução é conciliar: levar a questão à liderança apostólica em Jerusalém. Este é o modelo de resolução de conflitos doutrinários: diálogo, consulta às lideranças, decisão coletiva."),
             ]),
             ("🗣️ Os Discursos e a Decisão (15:6-29)", [
                 ("Atos 15:7-11", "E, havendo muito debate, levantou-se Pedro e disse-lhes: Varões irmãos, vós sabeis que já há muito tempo Deus me escolheu entre nós, para que os gentios ouvissem pela minha boca a palavra do evangelho e cressem. E Deus, que conhece os corações, lhes deu testemunho, dando-lhes o Espírito Santo, como também a nós; e não fez diferença alguma entre nós e eles, purificando os seus corações pela fé. Agora, pois, por que tentais a Deus, pondo sobre a cerviz dos discípulos um jugo que nem nossos pais nem nós pudemos suportar? Mas cremos que seremos salvos pela graça do Senhor Jesus Cristo, como eles também.",
                  "O discurso de Pedro é decisivo: ele apela à sua própria experiência com Cornélio (caps. 10-11) como evidência de que Deus não faz distinção entre judeus e gentios. O argumento é irônico e poderoso: se a Lei não conseguiu salvar os próprios judeus ('nem nossos pais nem nós pudemos suportar'), por que impô-la aos gentios? A frase final é a essência do Evangelho: 'seremos salvos pela graça do Senhor Jesus Cristo' — não pela Lei, não pela circuncisão, não pelas obras. Esta é a tese central de Romanos e Gálatas em uma frase."),
                 ("Atos 15:13-21", "E, depois que eles calaram, respondeu Tiago, dizendo: Varões irmãos, ouvi-me. Simão relatou como Deus primeiro visitou os gentios para tomar deles um povo para o seu nome. E com isto concordam as palavras dos profetas, como está escrito: Depois disto voltarei, e reedificarei o tabernáculo de Davi, que está caído...",
                  "Tiago, irmão de Jesus e líder da Igreja de Jerusalém, dá a palavra final. Ele confirma o testemunho de Pedro com a Escritura — Amós 9:11-12 — mostrando que a inclusão dos gentios estava prevista nos profetas. A decisão de Tiago é sábia e pastoral: não impor a circuncisão aos gentios, mas pedir que evitem quatro coisas que ofenderiam os judeus: ídolos, imoralidade sexual, carne estrangulada e sangue. Isso não é salvação por obras — é consideração pastoral para a convivência entre judeus e gentios na mesma comunidade. O Concílio de Jerusalém é um triunfo da graça e da unidade eclesial."),
                 ("Atos 15:28-29", "Porque pareceu bem ao Espírito Santo e a nós não vos impor mais encargo algum além destas coisas necessárias: que vos abstenhais das coisas sacrificadas aos ídolos, e do sangue, e do sufocado, e da fornicação; das quais coisas se vos guardardes, bem fareis. Passai bem.",
                  "A fórmula 'pareceu bem ao Espírito Santo e a nós' (<em>edoxen gar to pneumati to hagio kai hemin</em>) é única no NT — e profundamente significativa. A decisão conciliar não é apenas humana (consenso dos líderes) nem apenas divina (revelação direta) — é a confluência de ambas. O Espírito Santo guia a Igreja através do processo de deliberação humana: oração, debate, Escritura, testemunho de experiência, consenso. Este é o modelo de discernimento eclesiástico que a Igreja tem seguido por dois milênios."),
             ]),
         ]),
    16: ("A Segunda Viagem — Filipos e a Prisão de Meia-Noite",
         "A visão do macedônio, Lídia em Filipos, a escrava com espírito de adivinhação e o terremoto libertador",
         [
             ("🌙 A Visão do Macedônio (16:6-10)", [
                 ("Atos 16:6-10", "E, atravessando a Frígia e a região da Galácia, foram impedidos pelo Espírito Santo de pregar a palavra na Ásia; e, chegando à Mísia, tentavam ir para a Bitínia, mas o Espírito de Jesus não lho permitiu... E Paulo teve de noite uma visão: um homem macedônio estava em pé, rogando-lhe e dizendo: Passa à Macedônia e ajuda-nos. E logo depois da visão procuramos partir para a Macedônia, concluindo que o Senhor nos chamara para lhes anunciar o evangelho.",
                  "A visão do macedônio é um dos momentos mais decisivos da história missionária — e da história ocidental. Se Paulo tivesse ido para o Leste (Ásia, Bitínia), o Evangelho teria penetrado mais profundamente na Ásia. Mas o Espírito Santo o redireciona para o Oeste — para a Europa. A missão europeia de Paulo é o fundamento histórico do Cristianismo ocidental. O método de discernimento é notável: o Espírito 'impediu' (provavelmente por circunstâncias ou profecias), 'não permitiu' (idem), e então 'chamou' por uma visão. Deus guia por múltiplos meios — fechando portas e abrindo janelas."),
             ]),
             ("💜 Lídia e o Batismo em Filipos (16:11-15)", [
                 ("Atos 16:13-15", "E no dia de sábado saímos fora da cidade, junto de um rio, onde costumava fazer-se a oração; e, assentando-nos, falávamos às mulheres que se tinham reunido. E uma mulher chamada Lídia, vendedora de púrpura, da cidade de Tiatira, e que temia a Deus, nos ouvia; e o Senhor lhe abriu o coração para que atendesse ao que Paulo dizia. E, quando foi batizada, ela e a sua casa, nos rogou, dizendo: Se julgastes que eu sou fiel ao Senhor, entrai em minha casa e ficai. E nos constrangeu.",
                  "A primeira convertida europeia é uma mulher de negócios — Lídia, vendedora de púrpura (um produto de luxo, indicando prosperidade). A frase 'o Senhor lhe abriu o coração' (<em>dienoixen ten kardian</em>) é a descrição mais precisa da conversão no NT: a iniciativa é divina (Deus abre o coração), mas a resposta é humana (ela atende ao que Paulo dizia). A conversão não é apenas intelectual — é doméstica: 'ela e a sua casa.' A hospitalidade de Lídia — 'nos constrangeu' — é o modelo de generosidade cristã. Sua casa torna-se a primeira Igreja europeia."),
             ]),
             ("⛓️ A Prisão e o Terremoto (16:16-40)", [
                 ("Atos 16:25-31", "E, pela meia-noite, Paulo e Silas oravam e cantavam hinos a Deus, e os outros presos os ouviam. E de repente houve um grande terremoto, de modo que os alicerces da prisão foram abalados; e logo todas as portas se abriram, e as algemas de todos se soltaram. E o carcereiro, acordando e vendo as portas da prisão abertas, tirou a espada e ia matar-se, julgando que os presos tinham fugido. Paulo, porém, clamou em alta voz, dizendo: Não te faças nenhum mal, que todos aqui estamos. E ele, pedindo luz, entrou precipitadamente, e, tremendo, se prostrou aos pés de Paulo e de Silas; e, tirando-os para fora, disse: Senhores, que é necessário que eu faça para me salvar? E eles disseram: Crê no Senhor Jesus Cristo e serás salvo, tu e a tua casa.",
                  "A cena da prisão de Filipos é um dos momentos mais dramáticos e teologicamente ricos de Atos. Paulo e Silas, injustamente presos e açoitados, oram e cantam hinos à meia-noite — não como performance espiritual, mas como expressão genuína de fé que transcende as circunstâncias. O terremoto é a resposta de Deus — mas o milagre maior não é a abertura das portas: é que Paulo e Silas não fogem. Eles ficam — e por isso o carcereiro é salvo. A pergunta do carcereiro — 'que é necessário que eu faça para me salvar?' — é a pergunta mais importante que um ser humano pode fazer. A resposta apostólica é simples e completa: 'Crê no Senhor Jesus Cristo.'"),
             ]),
         ]),
    17: ("Atenas — O Discurso no Areópago",
         "Tessalônica, Bereia e o encontro de Paulo com a filosofia grega no coração de Atenas",
         [
             ("🏛️ O Areópago de Atenas (17:16-34)", [
                 ("Atos 17:16-18", "Enquanto Paulo os esperava em Atenas, o seu espírito se exasperava dentro dele, vendo a cidade entregue à idolatria. Disputava, pois, na sinagoga com os judeus e com os prosélitos, e diariamente na praça com os que ali se encontravam. E alguns filósofos epicureus e estóicos contendiam com ele; e uns diziam: Que quer dizer este palavreiro? E outros: Parece que é pregador de novos deuses; porque lhes pregava a Jesus e a ressurreição.",
                  "Atenas era o centro intelectual do mundo greco-romano — o lar de Sócrates, Platão e Aristóteles. Paulo não é intimidado pela grandeza cultural da cidade — mas é 'exasperado' (<em>paroxyneto</em> — literalmente 'provocado até a indignação') pela idolatria. Sua estratégia é dupla: sinagoga (para judeus) e ágora (para todos). Os filósofos epicureus (que buscavam a felicidade na ausência de dor, negavam a providência divina e a vida após a morte) e estóicos (que criam em uma razão divina impessoal que governa o universo) representam as duas grandes escolas filosóficas helenísticas. Paulo vai ao Areópago — o tribunal filosófico-religioso de Atenas — para apresentar o Evangelho no mais alto fórum intelectual do mundo."),
                 ("Atos 17:22-28", "E Paulo, estando em pé no meio do Areópago, disse: Atenienses, em tudo vos vejo como que muito religiosos. Porque, passando e observando os objetos do vosso culto, achei também um altar em que estava escrito: AO DEUS DESCONHECIDO. Esse, pois, que vós honrais sem o conhecer, é o que eu vos anuncio. O Deus que fez o mundo e tudo o que nele há, sendo Senhor do céu e da terra, não habita em templos feitos por mãos humanas... Porque nele vivemos, e nos movemos, e existimos; como também alguns dos vossos poetas disseram: Pois somos também sua geração.",
                  "O discurso do Areópago é a obra-prima da apologética cristã — e o modelo de contextualização missionária. Paulo não começa com a Bíblia (que os atenienses não conhecem) — começa com o que eles já sabem: o altar ao 'Deus Desconhecido' e as citações dos poetas gregos (Arato e Cleanto). Ele usa a cultura local como ponto de contato para anunciar o Deus bíblico. Mas a contextualização tem limites: Paulo não adapta o Evangelho à filosofia grega — ele usa a filosofia como ponte para anunciar a ressurreição, que é o escândalo inaceitável para os gregos (17:32). A contextualização serve ao Evangelho — não o substitui."),
                 ("Atos 17:30-34", "Deus, tendo passado por alto os tempos da ignorância, anuncia agora a todos os homens, em todo o lugar, que se arrependam; porque estabeleceu um dia em que há de julgar o mundo com justiça, por meio do varão que destinou; e disso deu certeza a todos, ressuscitando-o dos mortos. E, ouvindo a ressurreição dos mortos, uns escarneciam, e outros diziam: Acerca disto te ouviremos outra vez. Assim Paulo saiu do meio deles.",
                  "A reação ao discurso do Areópago é mista: escárnio (pela ressurreição), interesse (ouviremos outra vez) e fé (Dionísio, Dâmaris e outros). A ressurreição é o ponto de ruptura — para os gregos, o corpo era uma prisão da alma; a ideia de ressurreição corporal era absurda ou indesejável. Paulo não suaviza a mensagem para evitar o escárnio — ele prega a ressurreição mesmo sabendo que será ridicularizado. O Evangelho tem um núcleo irredutível que não pode ser adaptado sem ser destruído. O 'fracasso' em Atenas (poucos convertidos) não é um fracasso missionário — é a resposta esperada quando o Evangelho encontra a sabedoria humana (1Co 1:18-25)."),
             ]),
         ]),
    18: ("Corinto — A Segunda Viagem Termina",
         "Aquila e Priscila, o ministério de 18 meses em Corinto, a visão de encorajamento e o retorno a Antioquia",
         [
             ("🏙️ Corinto — A Cidade dos Contrastes (18:1-17)", [
                 ("Atos 18:1-4", "E depois destas coisas, saindo Paulo de Atenas, foi a Corinto; e, achando um judeu chamado Áquila, natural do Ponto, que havia pouco viera da Itália com Priscila, sua mulher (porque Cláudio havia ordenado que todos os judeus saíssem de Roma), foi ter com eles; e, como era do mesmo ofício, ficou com eles e trabalhavam, pois eram fabricantes de tendas de ofício. E disputava na sinagoga todos os sábados, e persuadia judeus e gregos.",
                  "Corinto era a cidade mais cosmopolita do mundo romano — porto comercial, centro de jogos (Jogos Ístmicos), famosa pela imoralidade (o verbo grego 'corintianizar' significava prostituir-se). Paulo chega sozinho, sem recursos, após o relativo 'fracasso' em Atenas. Ele encontra Áquila e Priscila — expulsos de Roma pelo édito de Cláudio (c. 49 d.C., confirmado pelo historiador Suetônio). O trabalho manual de Paulo (fabricante de tendas) não é uma concessão à necessidade — é uma escolha teológica: ele não quer ser um fardo para a Igreja (1Co 9:15-18; 2Co 11:7-9). Áquila e Priscila tornam-se os colaboradores mais importantes de Paulo — mencionados seis vezes no NT."),
                 ("Atos 18:9-11", "E disse o Senhor a Paulo em visão de noite: Não temas, mas fala, e não te cales; porque eu sou contigo, e ninguém lançará mão de ti para te fazer mal; porque tenho muito povo nesta cidade. E ficou ali um ano e seis meses, ensinando entre eles a palavra de Deus.",
                  "A visão de encorajamento em Corinto revela a humanidade de Paulo: ele estava com medo. A cidade era hostil, a oposição judaica era intensa, e Paulo estava sozinho. A resposta de Deus é pessoal e específica: 'Não temas... eu sou contigo... tenho muito povo nesta cidade.' Deus não promete ausência de sofrimento — promete presença divina no sofrimento. 'Tenho muito povo nesta cidade' (<em>laos polys estin moi en te polei taute</em>) — a eleição divina precede a evangelização: Deus já sabe quem vai crer. Isso não elimina a responsabilidade missionária — a motiva. Paulo fica 18 meses — o ministério mais longo registrado em Atos."),
             ]),
         ]),
    19: ("Éfeso — O Centro da Terceira Viagem",
         "O batismo dos discípulos de João, os milagres extraordinários, a revolta dos ourives e o poder do Evangelho",
         [
             ("🕊️ Os Discípulos de João em Éfeso (19:1-7)", [
                 ("Atos 19:1-6", "E aconteceu que, estando Apolo em Corinto, Paulo, percorrendo as regiões superiores, chegou a Éfeso, e achou alguns discípulos. E disse-lhes: Recebestes o Espírito Santo quando crestes? E eles disseram-lhe: Nem ainda ouvimos que haja Espírito Santo. E ele disse-lhes: Em que fostes, pois, batizados? E eles disseram: No batismo de João. Então Paulo disse: João, na verdade, batizou com o batismo de arrependimento, dizendo ao povo que cresse naquele que havia de vir depois dele, isto é, em Jesus Cristo. E, ouvindo isto, foram batizados em nome do Senhor Jesus. E, impondo-lhes Paulo as mãos, veio sobre eles o Espírito Santo, e falavam em línguas e profetizavam.",
                  "Os 'discípulos' de Éfeso são um caso único em Atos: eles creram em Jesus (são chamados 'discípulos'), mas só conheciam o batismo de João e não sabiam do Espírito Santo. Isso sugere que eram convertidos incompletos — talvez discípulos de Apolo antes de sua instrução por Priscila e Áquila (18:26). A sequência — fé em Jesus, batismo em nome de Jesus, imposição de mãos, recebimento do Espírito — não é um modelo normativo para todos os cristãos. É uma situação especial de completar uma conversão incompleta. O ponto teológico é claro: o batismo cristão e o Espírito Santo estão intrinsecamente ligados à fé em Jesus."),
             ]),
             ("✨ Os Milagres Extraordinários e a Revolta (19:11-41)", [
                 ("Atos 19:11-12", "E Deus fazia milagres não vulgares pelas mãos de Paulo; de modo que até os lenços e aventais que tinham tocado o seu corpo eram levados aos enfermos, e as doenças os deixavam, e os espíritos malignos saíam.",
                  "Os milagres em Éfeso são descritos como 'não vulgares' (<em>ou tas tychousas</em> — literalmente 'não os comuns') — uma litotes que enfatiza o extraordinário. Os lenços e aventais de Paulo que curavam os doentes ecoam a sombra de Pedro (5:15) e a orla do manto de Jesus (Lc 8:44). Éfeso era o centro do ocultismo no mundo antigo — o lar do templo de Ártemis, um dos Sete Maravilhas do Mundo, e um centro de magia (os 'Efésios' eram famosos papiros mágicos). Deus demonstra seu poder no coração do território inimigo — os milagres são sinais do Reino que derrota os poderes das trevas."),
                 ("Atos 19:23-27", "E naquele tempo houve não pequena perturbação acerca do Caminho. Porque um ourives chamado Demétrio, que fazia de prata templos de Ártemis, dava não pouco lucro aos artistas; o qual, reunindo-os, e também os outros que trabalhavam em coisas semelhantes, disse: Varões, sabeis que desta indústria nos vem a nossa riqueza; e vedes e ouvis que não somente em Éfeso, mas em quase toda a Ásia, este Paulo persuadiu e apartou grande multidão, dizendo que não são deuses os que se fazem com as mãos.",
                  "A revolta de Demétrio é a mais honesta avaliação do impacto do Evangelho em Atos: o Evangelho é tão eficaz que está destruindo o negócio dos ourives que fabricam ídolos. A motivação de Demétrio é econômica, mas ele a veste em linguagem religiosa — 'o templo da grande deusa Ártemis será desprezado.' Quando o Evangelho é genuinamente pregado, ele tem consequências econômicas e sociais: destrói indústrias baseadas na idolatria, liberta escravos do vício, transforma comunidades. A oposição ao Evangelho frequentemente tem motivação econômica disfarçada de religiosa."),
             ]),
         ]),
    20: ("O Discurso de Mileto — O Testamento de Paulo",
         "A ressurreição de Êutico, o discurso de despedida aos anciãos de Éfeso e a profecia do sofrimento em Jerusalém",
         [
             ("🌙 A Ressurreição de Êutico (20:7-12)", [
                 ("Atos 20:7-12", "E no primeiro dia da semana, estando nós reunidos para partir o pão, Paulo, que havia de partir no dia seguinte, discursava com eles, e prolongou o discurso até à meia-noite... E um jovem chamado Êutico, que estava assentado na janela, foi tomado de um sono profundo; e, dormindo Paulo por muito tempo, caiu do terceiro andar abaixo, e foi levantado morto. Paulo, porém, descendo, se deitou sobre ele, e o abraçou, e disse: Não vos perturbeis, porque a sua alma está nele. E, subindo, e partindo o pão, e comendo, e tendo falado largamente até à alvorada, assim partiu. E trouxeram o jovem vivo, e ficaram não pouco consolados.",
                  "O episódio de Êutico é narrado com humor sutil: Paulo prega tão longamente que um jovem adormece e cai da janela. O milagre que se segue ecoa Elias (1Rs 17:21) e Eliseu (2Rs 4:34) — Paulo se deita sobre o jovem morto e ele revive. Mas o detalhe mais significativo é o que acontece depois: Paulo sobe, parte o pão, come, e continua pregando até o amanhecer. A ressurreição de Êutico não interrompe o culto — é integrada a ele. A Ceia do Senhor ('partir o pão') é celebrada no 'primeiro dia da semana' — o domingo, o dia da ressurreição — estabelecendo o padrão do culto cristão dominical."),
             ]),
             ("💔 O Discurso de Mileto (20:17-38)", [
                 ("Atos 20:24-28", "Mas de nada disto faço caso, nem a minha vida me é preciosa, contanto que acabe a minha carreira com gozo, e o ministério que recebi do Senhor Jesus, para dar testemunho do evangelho da graça de Deus. E agora eis que eu sei que não vereis mais o meu rosto, vós todos por quem passei pregando o reino de Deus... Olhai, pois, por vós, e por todo o rebanho sobre que o Espírito Santo vos constituiu bispos, para apascentardes a Igreja de Deus, que ele resgatou com seu próprio sangue.",
                  "O discurso de Mileto é o único sermão de Paulo para uma audiência cristã registrado em Atos — e é um dos textos mais emocionantes do NT. Paulo se despede dos anciãos de Éfeso sabendo que não os verá mais. O discurso é um testamento pastoral: ele relembra seu ministério (20:18-21), anuncia seu destino (20:22-24), alerta sobre os perigos futuros (20:29-31) e os encomienda a Deus (20:32). A frase 'a Igreja de Deus, que ele resgatou com seu próprio sangue' é uma das declarações mais explícitas da divindade de Cristo no NT — o sangue derramado na cruz é o sangue de Deus encarnado."),
                 ("Atos 20:35-38", "Em tudo vos mostrei que, trabalhando assim, é necessário auxiliar os enfermos, e recordar as palavras do Senhor Jesus, que disse: Mais bem-aventurado é dar do que receber. E, havendo dito isto, ajoelhou-se e orou com todos eles. E houve grande choro de todos; e, lançando-se sobre o pescoço de Paulo, o beijavam, entristecidos principalmente pela palavra que disse, que não veriam mais o seu rosto. E o acompanharam até ao navio.",
                  "A cena final do discurso de Mileto é de uma ternura extraordinária: Paulo ajoelha-se e ora com os anciãos, eles choram, abraçam-no e o acompanham até o navio. A citação de Jesus — 'Mais bem-aventurado é dar do que receber' — não está registrada em nenhum dos quatro Evangelhos. É um 'agraphon' (dito não escrito de Jesus) preservado pela tradição oral e citado por Paulo. Isso nos lembra que os Evangelhos não registraram tudo o que Jesus disse (Jo 21:25). A despedida de Mileto é o modelo de relação pastoral: amor profundo, transparência, fidelidade ao Evangelho e confiança na graça de Deus."),
             ]),
         ]),
    21: ("A Viagem a Jerusalém e a Prisão de Paulo",
         "As profecias sobre a prisão, a chegada a Jerusalém, o tumulto no templo e a intervenção romana",
         [
             ("⚠️ As Profecias do Sofrimento (21:1-16)", [
                 ("Atos 21:10-14", "E, demorando-nos ali muitos dias, desceu da Judeia um profeta chamado Ágabo; e, vindo ter conosco, tomou o cinto de Paulo, e, ligando os seus próprios pés e mãos, disse: Assim diz o Espírito Santo: Assim ligarão os judeus em Jerusalém o homem de quem é este cinto, e o entregarão nas mãos dos gentios. E, ouvindo nós isto, rogávamos, tanto nós como os daquela cidade, que não subisse a Jerusalém. Então Paulo respondeu: Que fazeis, chorando e oprimindo-me o coração? Porque eu estou pronto, não somente a ser ligado, mas também a morrer em Jerusalém pelo nome do Senhor Jesus.",
                  "A profecia de Ágabo sobre a prisão de Paulo é a terceira advertência profética que Paulo recebe (cf. 20:23; 21:4). A resposta de Paulo é modelar: ele não ignora as profecias, mas também não as interpreta como proibições divinas. A vontade de Deus não é sempre o caminho mais fácil — às vezes é o caminho do sofrimento. 'Estou pronto, não somente a ser ligado, mas também a morrer em Jerusalém' — Paulo segue o modelo de Jesus, que 'pôs o rosto para ir a Jerusalém' (Lc 9:51) sabendo o que o esperava. O discipulado é participação no sofrimento de Cristo (Fp 3:10; Cl 1:24)."),
             ]),
             ("⛓️ O Tumulto no Templo (21:27-40)", [
                 ("Atos 21:27-30", "E, quando os sete dias estavam quase no fim, os judeus da Ásia, vendo-o no templo, alvoroçaram todo o povo, e lançaram as mãos sobre ele, gritando: Varões israelitas, acudi! Este é o homem que por toda a parte ensina todos contra o povo, e contra a lei, e contra este lugar; e ainda mais introduziu gregos no templo, e profanou este santo lugar.",
                  "A prisão de Paulo em Jerusalém é o cumprimento de todas as profecias. A acusação é falsa (Paulo não introduziu Trófimo, um gentio, no templo — 21:29), mas o tumulto é real. A ironia é dolorosa: Paulo veio a Jerusalém para trazer uma oferta de amor das igrejas gentílicas (Rm 15:25-27) — e é quase morto pelos judeus que ele amava profundamente (Rm 9:1-3). A intervenção do tribuno romano Lísias salva a vida de Paulo — mais uma vez, o poder romano serve involuntariamente aos propósitos de Deus. Paulo pedirá para falar ao povo — e o que se segue é um dos discursos mais pessoais de Atos (cap. 22)."),
             ]),
         ]),
    22: ("O Discurso de Paulo ao Povo de Jerusalém",
         "Paulo narra sua conversão em aramaico, a reação furiosa da multidão e a cidadania romana como escudo",
         [
             ("📢 A Defesa Pessoal de Paulo (22:1-21)", [
                 ("Atos 22:3-8", "Sou judeu, nascido em Tarso da Cilícia, mas criado nesta cidade, instruído aos pés de Gamaliel, na exatidão da lei dos pais, sendo zeloso de Deus, como vós todos o sois hoje. E persegui este Caminho até à morte, prendendo e entregando às prisões homens e mulheres... E, indo eu no caminho, e aproximando-me de Damasco, ao meio-dia, de repente me cercou uma grande luz do céu. E caí em terra, e ouvi uma voz que me dizia: Saulo, Saulo, por que me persegues? E eu respondi: Quem és tu, Senhor? E ele me disse: Eu sou Jesus de Nazaré, a quem tu persegues.",
                  "Paulo fala em aramaico — a língua do povo — e isso silencia a multidão. Ele se apresenta como um deles: judeu, nascido em Tarso, criado em Jerusalém, discípulo de Gamaliel (o maior rabino da geração). Ele não é um traidor de Israel — é um judeu que encontrou o Messias de Israel. A narrativa da conversão é pessoal e poderosa: Paulo não argumenta — ele testemunha. O testemunho pessoal tem um poder que a argumentação não tem: é difícil refutar a experiência de alguém. A multidão ouve em silêncio até Paulo mencionar os gentios (22:21) — então explode em fúria. O problema não é Jesus — é a inclusão dos gentios em igualdade com Israel."),
             ]),
         ]),
    23: ("Paulo Diante do Sinédrio e a Conspiração",
         "O conflito entre fariseus e saduceus, a visão noturna do Senhor e a conspiração para matar Paulo",
         [
             ("⚡ A Divisão do Sinédrio (23:1-11)", [
                 ("Atos 23:6-11", "E Paulo, sabendo que uma parte era de saduceus e a outra de fariseus, clamou no Sinédrio: Varões irmãos, eu sou fariseu, filho de fariseu; sou julgado por causa da esperança e da ressurreição dos mortos. E, dizendo ele isto, houve contenda entre os fariseus e os saduceus, e a multidão dividiu-se... E na noite seguinte, aparecendo-lhe o Senhor, disse: Tem bom ânimo, Paulo; porque, assim como testificaste as coisas a meu respeito em Jerusalém, assim também importa que testifiques em Roma.",
                  "A estratégia de Paulo de invocar a ressurreição para dividir o Sinédrio é brilhante — ou, como alguns críticos dizem, manipuladora. Mas Paulo não está sendo desonesto: ele genuinamente é fariseu e genuinamente crê na ressurreição — a ressurreição de Jesus. Ao invocar esse ponto de concordância com os fariseus, ele expõe a divisão teológica do Sinédrio e escapa de uma condenação unânime. A visão noturna do Senhor é o ponto central do capítulo: 'Tem bom ânimo... importa que testifiques em Roma.' O sofrimento de Paulo não é acidente — é o caminho para Roma, o centro do mundo. O Evangelho chegará ao coração do Império."),
             ]),
         ]),
    24: ("Paulo Diante de Félix — A Defesa em Cesareia",
         "A acusação de Tértulo, a defesa de Paulo, as conversas com Félix e a detenção por dois anos",
         [
             ("⚖️ A Defesa Diante de Félix (24:10-21)", [
                 ("Atos 24:14-16", "Mas isto te confesso, que segundo o Caminho, a que chamam seita, assim sirvo ao Deus de meus pais, crendo em tudo o que está escrito na lei e nos profetas; tendo em Deus a esperança, que eles mesmos também esperam, de que há de haver ressurreição, tanto dos justos como dos injustos. E por isso mesmo me esforço por ter sempre uma consciência sem ofensa, tanto para com Deus como para com os homens.",
                  "A defesa de Paulo diante de Félix é um modelo de apologética cristã. Ele não nega ser do 'Caminho' (<em>hodos</em> — o nome primitivo do Cristianismo, baseado em Jo 14:6) — mas redefine o que isso significa: não é uma seita separatista, mas o cumprimento do judaísmo. 'Sirvo ao Deus de meus pais, crendo em tudo o que está escrito na lei e nos profetas' — o Evangelho não contradiz o AT, ele o cumpre. A menção da 'ressurreição dos justos e injustos' (cf. Dn 12:2; Jo 5:28-29) é a afirmação do julgamento final — um elemento que Paulo usa consistentemente em sua apologética."),
                 ("Atos 24:24-26", "E, passados alguns dias, veio Félix com Drusila, sua mulher, que era judia, e mandou chamar a Paulo, e ouviu-o acerca da fé em Cristo Jesus. E, discorrendo ele acerca da justiça, e da temperança, e do juízo vindouro, Félix, ficando atemorizado, respondeu: Por agora vai-te; quando tiver ocasião conveniente, chamar-te-ei. E ao mesmo tempo esperava que Paulo lhe desse dinheiro; pelo que muitas vezes o mandava chamar e conversava com ele.",
                  "As conversas de Paulo com Félix são fascinantes. Félix — um ex-escravo que se tornou governador, casado com Drusila (filha de Herodes Agripa I, que havia matado Tiago e preso Pedro) — ouve Paulo sobre 'justiça, temperança e juízo vindouro.' A reação de Félix — 'ficou atemorizado' (<em>emphobos genomenos</em>) — mostra que o Evangelho tocou sua consciência. Mas ele adia a decisão: 'quando tiver ocasião conveniente.' Esta é a tragédia do adiamento: a 'ocasião conveniente' nunca chega. Félix mantém Paulo preso por dois anos — esperando suborno e querendo agradar aos judeus (24:27)."),
             ]),
         ]),
    25: ("Paulo Diante de Festo e Agripa",
         "O apelo a César, o encontro com Herodes Agripa II e a declaração de inocência de Paulo",
         [
             ("👑 O Apelo a César (25:1-12)", [
                 ("Atos 25:10-12", "E Paulo disse: Estou diante do tribunal de César, onde devo ser julgado; não fiz nenhum agravo aos judeus, como tu muito bem sabes. Porque se sou culpado e fiz alguma coisa digna de morte, não recuso morrer; mas se não há nada naquilo de que estes me acusam, ninguém me pode entregar a eles. Apelo a César. Então Festo, havendo conferenciado com o conselho, respondeu: Apelaste a César; a César irás.",
                  "O apelo de Paulo a César é o momento decisivo que determinará o destino do Evangelho em Roma. Paulo usa seu direito de cidadão romano — um direito que ele havia guardado em reserva para este momento crucial. O apelo a César (<em>Kaisara epikaloumai</em>) era irrevogável: uma vez feito, o caso tinha que ser levado a Roma. Paulo não apela por medo — ele apela porque sabe que é o caminho para Roma, o destino que o Senhor lhe revelou (23:11). A providência divina usa o sistema legal romano para cumprir o propósito missionário de Deus."),
             ]),
             ("🎭 O Discurso Diante de Agripa (26:1-32)", [
                 ("Atos 26:27-29", "Crês, ó rei Agripa, nos profetas? Eu sei que crês. E Agripa disse a Paulo: Por pouco me persuades a fazer-me cristão. E Paulo disse: Prouvera a Deus que, não somente por pouco, mas também por muito, não somente tu, mas também todos os que hoje me ouvem se tornassem tais qual eu sou, exceto estas cadeias.",
                 "O discurso de Paulo diante de Herodes Agripa II é o mais pessoal e evangelístico de todos. Paulo não está apenas se defendendo — está pregando o Evangelho ao rei. A pergunta 'Crês nos profetas?' coloca Agripa em uma posição impossível: se diz que sim, tem que aceitar que Jesus é o Messias; se diz que não, perde credibilidade diante do povo judeu. A resposta de Agripa — 'por pouco me persuades a fazer-me cristão' — é ambígua: pode ser sarcástica ou genuinamente tocada. A resposta de Paulo é extraordinária: ele deseja que todos sejam como ele — 'exceto estas cadeias.' Paulo, acorrentado, é mais livre do que seus juízes."),
             ]),
         ]),
    27: ("O Naufrágio — A Providência no Mar",
         "A viagem para Roma, a tempestade, o anjo de Deus, o naufrágio em Malta e a salvação de todos a bordo",
         [
             ("⛵ A Tempestade e o Anjo (27:13-44)", [
                 ("Atos 27:21-26", "E, havendo passado muito tempo sem comer, Paulo, pondo-se em pé no meio deles, disse: Certamente, ó varões, convinha ouvir-me a mim, e não partir de Creta, para evitar este dano e perda. Mas agora vos admoesto que tenhais bom ânimo; porque nenhuma vida se perderá entre vós, mas somente o navio. Porque esta noite um anjo do Deus de quem sou e a quem sirvo me apareceu, dizendo: Paulo, não temas; importa que compareças diante de César; e eis que Deus te deu todos os que navegam contigo. Portanto, ó varões, tende bom ânimo; porque confio em Deus que assim será como me foi dito.",
                  "O naufrágio em Atos 27 é narrado com detalhes náuticos tão precisos que estudiosos modernos o usam como documento histórico sobre navegação antiga. Lucas estava a bordo ('nós' — 27:1) e registrou tudo com a acuidade de um observador treinado. O papel de Paulo durante a crise é notável: ele passa de prisioneiro a líder de facto do navio. Sua autoridade não vem de título ou posição — vem da presença de Deus e da confiança que isso gera. O anjo garante a salvação de todos os 276 a bordo — não por mérito deles, mas 'por causa de Paulo' (27:24). A presença de um servo de Deus pode ser bênção para todos ao redor."),
                 ("Atos 27:33-36", "E, esperando que amanhecesse, Paulo exortava a todos que comessem, dizendo: Hoje faz catorze dias que esperais e continuais em jejum, sem comer nada. Portanto, rogo-vos que comais, pois isso é para a vossa saúde; porque nem um cabelo da cabeça de nenhum de vós perecerá. E, havendo dito isto, tomou o pão, e deu graças a Deus diante de todos, e, partindo-o, começou a comer. E todos, ficando animados, também comeram.",
                  "A cena de Paulo partindo o pão no meio da tempestade tem ecos eucarísticos deliberados: ele 'tomou o pão, deu graças a Deus diante de todos, e partindo-o, começou a comer' — a mesma sequência da Última Ceia (Lc 22:19) e de Emaús (Lc 24:30). Em meio ao caos e ao perigo, Paulo celebra a graça de Deus. A fé não é negação da realidade — é confiança em Deus dentro da realidade. Paulo não nega a tempestade — ele come em meio a ela, confiando na promessa divina."),
             ]),
         ]),
    28: ("Roma — O Evangelho Chega ao Centro do Mundo",
         "Malta, a serpente, a chegada a Roma, o discurso final aos judeus e o Evangelho pregado livremente",
         [
             ("🐍 Malta — A Serpente e os Milagres (28:1-10)", [
                 ("Atos 28:3-6", "E Paulo, ajuntando uma porção de gravetos, e pondo-os no fogo, saiu-lhe uma víbora por causa do calor, e se lhe prendeu na mão. E, quando os bárbaros viram o réptil pendurado na sua mão, diziam uns aos outros: Certamente este homem é homicida, pois, escapando do mar, a justiça não o deixa viver. Ele, porém, sacudindo o réptil no fogo, não sofreu nenhum mal. E eles esperavam que ele havia de inchar, ou cair morto de repente; mas, depois de esperar muito, e vendo que nenhum mal lhe acontecia, mudando de opinião, diziam que era um deus.",
                  "O episódio da serpente em Malta é narrado com humor: os habitantes da ilha passam de 'este homem é um assassino' para 'este homem é um deus' — tudo em questão de minutos. A resposta de Paulo — sacudir a serpente no fogo sem sofrer mal — cumpre a promessa de Jesus em Lucas 10:19 ('pisar sobre serpentes e escorpiões'). Paulo não faz nenhum discurso sobre o milagre — ele simplesmente continua sua missão. Os milagres em Malta (a serpente, a cura do pai de Públio, a cura de outros doentes) abrem o coração dos habitantes para o Evangelho — mesmo que Lucas não registre explicitamente conversões."),
             ]),
             ("🏛️ Roma — O Fim e o Começo (28:11-31)", [
                 ("Atos 28:23-28", "E, tendo-lhe marcado um dia, muitos vieram ter com ele à estalagem; aos quais ele expunha, testificando o reino de Deus, e persuadindo-os acerca de Jesus, tanto pela lei de Moisés como pelos profetas, desde a manhã até à tarde... E alguns criam nas coisas que eram ditas, e outros não criam... Portanto, seja-vos notório que esta salvação de Deus foi enviada aos gentios, e eles a ouvirão.",
                  "A chegada de Paulo a Roma é o cumprimento do mapa missionário de 1:8 — 'até aos confins da terra.' Roma era o centro do mundo conhecido — o lugar de onde os caminhos se irradiavam para toda a terra. Paulo chega como prisioneiro — mas prega livremente. A última cena de Atos é deliberadamente aberta: Paulo está em Roma, pregando 'sem impedimento' (<em>akolutos</em> — a última palavra do livro em grego). Lucas não narra o julgamento de Paulo, sua libertação ou sua morte. Por quê? Porque Atos não é a história de Paulo — é a história do Evangelho. E o Evangelho não pode ser aprisionado."),
                 ("Atos 28:30-31", "E Paulo ficou dois anos inteiros em sua própria casa alugada, e recebia todos os que a ele vinham, pregando o reino de Deus e ensinando as coisas concernentes ao Senhor Jesus Cristo, com toda a ousadia, sem impedimento.",
                  "O final de Atos é um final aberto — e isso é intencional. Lucas termina com Paulo pregando em Roma 'com toda a ousadia, sem impedimento' (<em>meta pases parresias akolutos</em>). A <em>parresia</em> (ousadia, franqueza) é a marca do ministério apostólico desde o Pentecostes (4:13,29,31). O <em>akolutos</em> (sem impedimento) é a última palavra do livro — uma declaração de triunfo: o Evangelho não pode ser detido por prisões, naufráfios, serpentes ou imperadores. Atos continua sendo escrito — na história da Igreja, em cada geração que prega o Evangelho com ousadia. Somos o capítulo 29 de Atos."),
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
        print(f"  ✅ Atos {str(num).zfill(2)} — {titulo[:55]}")
    print(f"\n🎉 Total gerado: {len(CAPITULOS)} capítulos de Atos (fase 2: 15-28)")

if __name__ == "__main__":
    main()
