#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os 16 capítulos aprofundados de Romanos"""

import os

BASE = "/home/ubuntu/365-de-graca-e-adoracao/08-novo-testamento/romanos/capitulos"
os.makedirs(BASE, exist_ok=True)

def cap(num, titulo, versiculo_chave, ref_chave, conteudo_html):
    prev_link = f'capitulo-{num-1:02d}.html' if num > 1 else '../index.html'
    prev_label = f'← Romanos {num-1}' if num > 1 else '← Índice'
    next_link = f'capitulo-{num+1:02d}.html' if num < 16 else '../index.html'
    next_label = f'Romanos {num+1} →' if num < 16 else 'Índice →'
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Romanos {num} — {titulo} | 365 de Graça & Adoração</title>
  <meta name="description" content="Estudo aprofundado de Romanos {num}: {titulo}. Análise versículo por versículo, vocabulário grego, contexto histórico e teologia paulina.">
  <meta property="og:title" content="Romanos {num} — {titulo}">
  <meta property="og:description" content="{versiculo_chave[:120]}">
  <link rel="stylesheet" href="../../../../assets/css/style.css">
  <link rel="stylesheet" href="../../../../assets/css/bloco.css">
  <link rel="stylesheet" href="../../../../assets/css/nav.css">
  <body class="bloco-08">
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
    <a href="/">Início</a> › <a href="/08-novo-testamento/">Novo Testamento</a> › <a href="../">Romanos</a> › Capítulo {num}
  </div>

  <div class="chapter-hero">
    <div class="chapter-number">Romanos {num}</div>
    <h1>{titulo}</h1>
    <p class="chapter-subtitle">{versiculo_chave}</p>
    <p class="chapter-ref">— {ref_chave}</p>
  </div>

  <div class="wrap">
{conteudo_html}
  </div>

  <nav class="chapter-nav">
    <a href="{prev_link}">{prev_label}</a>
    <a href="../index.html">Índice de Romanos</a>
    <a href="{next_link}">{next_label}</a>
  </nav>

  <footer class="site-footer">
    <p>365 de Graça &amp; Adoração • Da Criação ao Apocalipse • © 2026</p>
  </footer>
</body>
</html>"""

# ============================================================
# ROMANOS 1
# ============================================================
r1 = """
    <div class="section-block">
      <h2>📜 Contexto Histórico e Introdução</h2>
      <p>Romanos é a carta mais sistemática e teologicamente densa de Paulo — frequentemente chamada de "a catedral das epístolas". Escrita por volta de 57 d.C. em Corinto, durante a terceira viagem missionária, ela é endereçada a uma comunidade que Paulo ainda não visitou, mas planeja visitar a caminho da Espanha (15:24). A carta não é apenas uma introdução pessoal — é a exposição mais completa do Evangelho que Paulo já escreveu.</p>
      <p>O capítulo 1 funciona como a abertura de uma sinfonia: ele apresenta todos os temas que serão desenvolvidos ao longo dos 16 capítulos. O Evangelho (1:16-17), a ira de Deus (1:18), a depravação humana (1:19-32), a justiça de Deus — tudo está aqui em embrião.</p>
    </div>

    <div class="section-block">
      <h2>✉️ Saudação Apostólica (1:1-7)</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 1:1-4</div>
        <div class="texto-v">"Paulo, servo de Jesus Cristo, chamado para apóstolo, separado para o evangelho de Deus, que ele havia prometido antes por seus profetas nas sagradas Escrituras acerca de seu Filho, que nasceu da descendência de Davi segundo a carne, e foi declarado Filho de Deus com poder, segundo o Espírito de santificação, pela ressurreição dos mortos — Jesus Cristo, nosso Senhor."</div>
        <div class="analise-v">A saudação de Paulo é a mais longa de todas as suas cartas — e por uma razão: ele precisa estabelecer sua autoridade apostólica diante de uma comunidade que não o conhece pessoalmente. Três títulos definem Paulo: <em>doulos</em> (escravo — não servo, mas escravo voluntário de Cristo), <em>kletos apostolos</em> (apóstolo chamado — não autoproclamado, mas designado por Deus), e <em>aphorismenos</em> (separado — a mesma raiz de "fariseu", ironicamente). O Evangelho não é novidade — foi prometido nas Escrituras. Jesus é apresentado em dois aspectos: segundo a carne (<em>kata sarka</em>) — filho de Davi, cumprindo a profecia messiânica (2Sm 7:12-16); segundo o Espírito (<em>kata pneuma</em>) — declarado Filho de Deus pela ressurreição. A ressurreição não fez Jesus Filho de Deus — ela o declarou publicamente como tal.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 1:5-7</div>
        <div class="texto-v">"Por quem recebemos a graça e o apostolado para a obediência da fé entre todas as nações, pelo seu nome; entre as quais estais vós também, chamados de Jesus Cristo... graça e paz da parte de Deus nosso Pai e do Senhor Jesus Cristo."</div>
        <div class="analise-v">A frase <em>hypakoe pisteos</em> — "obediência da fé" — é fundamental para entender a teologia de Paulo. Fé não é apenas assentimento intelectual — ela produz obediência. A missão de Paulo é levar as nações à obediência da fé, não à obediência da lei. Os romanos são "chamados de Jesus Cristo" (<em>kletoi Iesou Christou</em>) — o chamado é divino, não humano. A saudação "graça e paz" (<em>charis kai eirene</em>) combina o cumprimento grego (<em>chaire</em>) com o hebraico (<em>shalom</em>) — Paulo une os dois mundos em Cristo.</div>
      </div>
    </div>

    <div class="section-block">
      <h2>🙏 Ação de Graças e Desejo de Visitar Roma (1:8-15)</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 1:11-12</div>
        <div class="texto-v">"Porque muito desejo ver-vos, para vos comunicar algum dom espiritual, a fim de que sejais confirmados; isto é, para ser mutuamente consolado entre vós, cada um pela fé do outro, tanto a vossa como a minha."</div>
        <div class="analise-v">Paulo corrige-se em tempo real: começa dizendo que quer dar algo aos romanos, mas imediatamente reconhece que a relação é recíproca — ele também receberá deles. Esta autocorreção revela a humildade genuína de Paulo. O ministério cristão não é unidirecional — é comunhão mútua. O "dom espiritual" (<em>charisma pneumatikon</em>) não é necessariamente um dom sobrenatural específico — pode ser simplesmente o fortalecimento que vem da presença apostólica e do ensino.</div>
      </div>
    </div>

    <div class="section-block">
      <h2>⚡ O Tema Central: O Evangelho (1:16-17)</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 1:16-17</div>
        <div class="texto-v">"Porque não me envergonho do evangelho de Cristo, pois é o poder de Deus para a salvação de todo aquele que crê; primeiro do judeu, e também do grego. Porque nele a justiça de Deus se revela de fé em fé; como está escrito: O justo viverá pela fé."</div>
        <div class="analise-v">Estes dois versículos são a tese de toda a carta — a <em>propositio</em> retórica que os 15 capítulos seguintes desenvolvem. Quatro conceitos fundamentais: (1) <em>dynamis theou</em> — poder de Deus: o Evangelho não é apenas informação, é poder transformador; (2) <em>soterian</em> — salvação: não apenas perdão, mas libertação total, restauração da imagem de Deus; (3) <em>dikaiosyne theou</em> — justiça de Deus: não a justiça que Deus exige de nós, mas a justiça que Deus provê para nós em Cristo; (4) <em>ek pisteos eis pistin</em> — de fé em fé: a salvação é inteiramente pela fé, do começo ao fim. A citação de Habacuque 2:4 ("O justo viverá pela fé") foi o versículo que desencadeou a Reforma Protestante — Lutero o leu e entendeu que a justiça de Deus é um dom recebido pela fé, não uma exigência a ser cumprida.</div>
      </div>
    </div>

    <div class="section-block">
      <h2>🔥 A Ira de Deus e a Depravação Humana (1:18-32)</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 1:18-20</div>
        <div class="texto-v">"Porque do céu se manifesta a ira de Deus sobre toda a impiedade e injustiça dos homens que detêm a verdade em injustiça. Porquanto o que de Deus se pode conhecer é manifesto entre eles, porque Deus lho manifestou. Porque as suas perfeições invisíveis, desde a criação do mundo, tanto o seu eterno poder como a sua divindade, se entendem e claramente se veem nas coisas que foram criadas; de modo que eles são inescusáveis."</div>
        <div class="analise-v">A <em>orge theou</em> (ira de Deus) não é uma reação emocional irracional — é a resposta santa e justa de Deus à violação da sua ordem moral. Paulo estabelece a doutrina da revelação natural: todo ser humano tem acesso ao conhecimento de Deus através da criação (<em>theologia naturalis</em>). A criação revela o "eterno poder" (<em>aidios dynamis</em>) e a "divindade" (<em>theiotes</em>) de Deus. Esta revelação torna todos os seres humanos "inescusáveis" (<em>anapologetous</em>) — sem desculpa. O problema humano não é falta de informação sobre Deus — é supressão da informação que já existe. "Detêm a verdade em injustiça" — a palavra <em>katechonton</em> significa suprimir, segurar, abafar. A humanidade conhece Deus mas escolhe suprimir esse conhecimento.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 1:21-23</div>
        <div class="texto-v">"Porquanto, tendo conhecido a Deus, não o glorificaram como Deus, nem lhe deram graças, antes em seus pensamentos se tornaram vãos, e o seu coração insensato se obscureceu. Dizendo-se sábios, tornaram-se loucos, e mudaram a glória do Deus incorruptível em semelhança da imagem de homem corruptível, e de aves, e de quadrúpedes, e de répteis."</div>
        <div class="analise-v">Paulo descreve a espiral descendente da idolatria com precisão clínica: (1) Conhecimento de Deus → (2) Recusa de glorificar e agradecer → (3) Pensamentos vãos (<em>emataiotheson</em> — tornaram-se fúteis, sem substância) → (4) Coração obscurecido → (5) Pretensão de sabedoria → (6) Loucura → (7) Idolatria. A idolatria não é o ponto de partida — é o resultado de uma série de escolhas morais. A troca da "glória do Deus incorruptível" (<em>doxan tou aphtartou theou</em>) por imagens corruptíveis é a inversão fundamental da realidade. O ser humano foi criado para adorar — quando não adora o verdadeiro Deus, inevitavelmente adora algo criado.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 1:24-28</div>
        <div class="texto-v">"Por isso Deus os entregou... Deus os entregou... Deus os entregou..."</div>
        <div class="analise-v">A repetição tripla de <em>paredoken autous ho theos</em> — "Deus os entregou" — é o coração desta seção. A ira de Deus não é apenas futura (no juízo final) — ela já opera no presente como abandono judicial. Deus não força ninguém ao pecado — ele remove a restrição e permite que as pessoas sigam os desejos do seu coração corrompido. Este é o julgamento mais terrível: não punição externa, mas a consequência interna do próprio pecado. As três entregas são: (1) às impurezas (1:24-25) — desordem sexual; (2) às paixões infames (1:26-27) — homossexualidade como exemplo paradigmático da inversão da ordem criacional; (3) à mente reprovada (1:28-32) — catálogo de vícios sociais. Paulo não está atacando grupos específicos — está descrevendo a condição universal da humanidade fora de Deus.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 1:29-32</div>
        <div class="texto-v">"Estando cheios de toda a injustiça, malícia, cobiça, maldade; cheios de inveja, homicídio, contenda, engano, malignidade; sendo murmuradores, detratores, aborrecedores de Deus, injuriosos, soberbos, presunçosos, inventores de males, desobedientes aos pais, insensatos, desleais, sem afeto natural, implacáveis, sem misericórdia."</div>
        <div class="analise-v">O catálogo de 21 vícios em 1:29-31 é uma das listas mais completas de pecados no NT. Paulo não está descrevendo apenas pagãos romanos do século I — está descrevendo a condição humana universal. A lista termina com o versículo mais sombrio: "os que praticam tais coisas são dignos de morte, e não somente os que as praticam, mas também os que aprovam os que as fazem" (1:32). O problema não é apenas a prática do mal — é a aprovação cultural do mal. Uma sociedade que celebra o que Deus condena está em rebelião ativa contra a ordem moral do universo. Este versículo prepara o terreno para o capítulo 2, onde Paulo vira a mesa sobre os que julgam os outros.</div>
      </div>
    </div>

    <div class="section-block">
      <h2>🎯 Teologia Sistemática — Romanos 1</h2>
      <table>
        <tr><th>Doutrina</th><th>Ensinamento em Romanos 1</th><th>Implicação</th></tr>
        <tr><td>Revelação</td><td>Deus se revela na criação (1:19-20)</td><td>Todos são responsáveis diante de Deus</td></tr>
        <tr><td>Hamartologia</td><td>Pecado = supressão da verdade (1:18)</td><td>O problema é moral, não intelectual</td></tr>
        <tr><td>Ira de Deus</td><td>Abandono judicial (1:24,26,28)</td><td>O julgamento já opera no presente</td></tr>
        <tr><td>Soteriologia</td><td>Evangelho = poder de Deus (1:16)</td><td>Salvação é obra divina, não humana</td></tr>
        <tr><td>Justificação</td><td>Justiça de Deus pela fé (1:17)</td><td>Recebida, não conquistada</td></tr>
      </table>
    </div>"""

# ============================================================
# ROMANOS 2
# ============================================================
r2 = """
    <div class="section-block">
      <h2>📜 Contexto: O Judeu Hipócrita e o Gentio Moral</h2>
      <p>Romanos 2 é um dos capítulos mais surpreendentes da Bíblia. Após descrever a depravação dos gentios em 1:18-32, Paulo vira a mesa: agora ele confronta aquele que se considera moralmente superior — seja o gentio moralista, seja o judeu religioso. O argumento é devastador: ninguém escapa do julgamento de Deus, porque o critério do julgamento não é o conhecimento da lei, mas a obediência a ela.</p>
    </div>

    <div class="section-block">
      <h2>⚖️ O Julgamento Justo de Deus (2:1-11)</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 2:1-4</div>
        <div class="texto-v">"Portanto, és inescusável, ó homem, quem quer que sejas tu que julgas; pois no que julgas a outro, a ti mesmo te condenas, porque tu que julgas praticas as mesmas coisas... Ou desprezas as riquezas da sua benignidade, tolerância e longanimidade, ignorando que a benignidade de Deus te leva ao arrependimento?"</div>
        <div class="analise-v">Paulo usa um recurso retórico clássico — a <em>diatribe</em> — dirigindo-se a um interlocutor imaginário. O "tu que julgas" (<em>ho krinon</em>) é o moralista que concordou entusiasticamente com a condenação dos vícios do capítulo 1 — e agora descobre que o dedo aponta para ele mesmo. O princípio é implacável: ao julgar os outros pelos mesmos pecados que você comete, você se condena. A bondade de Deus (<em>chrestotes</em>), tolerância (<em>anoche</em>) e longanimidade (<em>makrothymia</em>) não são sinais de indiferença ao pecado — são convites ao arrependimento. Aquele que interpreta a paciência de Deus como aprovação está acumulando ira para o dia do julgamento (2:5).</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 2:6-11</div>
        <div class="texto-v">"O qual retribuirá a cada um segundo as suas obras: vida eterna aos que, com perseverança em fazer o bem, procuram glória, honra e incorruptibilidade; mas ira e indignação aos que são contenciosos e não obedecem à verdade, mas obedecem à injustiça... Porque não há acepção de pessoas diante de Deus."</div>
        <div class="analise-v">Este trecho levanta uma questão teológica crucial: Paulo está ensinando salvação pelas obras? A resposta é não — mas a razão é sutil. Paulo está descrevendo o princípio do julgamento final (obras), não o meio da justificação (fé). O julgamento final avaliará as obras como evidência da fé genuína — não como base da salvação. Aqueles que "com perseverança em fazer o bem" buscam glória não são pessoas que se salvam por méritos — são pessoas cuja fé genuína se manifesta em obras. O princípio "não há acepção de pessoas" (<em>ou gar estin prosopolempsia para to theo</em>) é fundamental: Deus não tem favoritismo étnico ou religioso. Judeu e gentio serão julgados pelo mesmo padrão.</div>
      </div>
    </div>

    <div class="section-block">
      <h2>📖 A Lei e a Consciência (2:12-16)</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 2:14-16</div>
        <div class="texto-v">"Porque quando os gentios, que não têm lei, fazem por natureza as coisas que são da lei, esses, não tendo lei, são lei para si mesmos; pois mostram a obra da lei escrita em seus corações, testificando também a sua consciência, e os seus pensamentos mutuamente acusando-os ou defendendo-os."</div>
        <div class="analise-v">Este é um dos textos mais importantes para a teologia da lei natural e da consciência. Paulo afirma que os gentios, sem a Torah, têm a "obra da lei escrita em seus corações" — uma lei moral interna. A consciência (<em>syneidesis</em>) funciona como um tribunal interno que acusa ou defende. Isto não significa que os gentios são salvos pela consciência — significa que eles são responsáveis diante de Deus mesmo sem a revelação especial. A consciência não salva — ela condena, porque ninguém a obedece perfeitamente. Este texto é a base bíblica para a doutrina da lei natural (Tomás de Aquino) e para a afirmação de que todos os seres humanos têm senso moral inato.</div>
      </div>
    </div>

    <div class="section-block">
      <h2>✡️ O Judeu e a Lei (2:17-29)</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 2:17-24</div>
        <div class="texto-v">"Mas tu que te chamas judeu, e repousas na lei, e te glorias em Deus... que ensinas a outro, não te ensinas a ti mesmo? Tu que pregas que não se deve furtar, furtas? Tu que dizes que não se deve adulterar, adulteras?... O nome de Deus é blasfemado entre os gentios por causa de vós."</div>
        <div class="analise-v">Paulo cita Isaías 52:5 e Ezequiel 36:22 para mostrar que a hipocrisia religiosa judaica causou blasfêmia entre os gentios. O privilégio do conhecimento da lei aumenta a responsabilidade — não diminui. A lista de contradições é devastadora: ensinas mas não praticas, pregas contra o roubo mas roubas, condenas o adultério mas adulteras, abominas ídolos mas saqueas templos. O princípio é universal: o ensino sem a prática não apenas é inútil — é contraproducente, pois desonra o Deus que se professa adorar.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 2:28-29</div>
        <div class="texto-v">"Porque não é judeu o que o é exteriormente, nem é circuncisão a que o é exteriormente, na carne. Mas é judeu o que o é interiormente, e circuncisão é a do coração, em espírito, não em letra; cujo louvor não vem dos homens, mas de Deus."</div>
        <div class="analise-v">Esta é uma das afirmações mais radicais de Paulo sobre a identidade do povo de Deus. A verdadeira circuncisão não é física — é a circuncisão do coração (<em>peritome kardias</em>), prometida em Deuteronômio 30:6 e Jeremias 4:4. Paulo não está abolindo a identidade judaica — está redefinindo-a em termos de transformação interna pelo Espírito. O verdadeiro judeu é aquele cujo coração foi transformado por Deus — e isso inclui gentios que creem em Cristo. Esta teologia prepara o caminho para a discussão sobre Abraão em Romanos 4 e sobre Israel em Romanos 9-11.</div>
      </div>
    </div>"""

# ============================================================
# ROMANOS 3
# ============================================================
r3 = """
    <div class="section-block">
      <h2>📜 Contexto: Todos Culpados, Todos Justificados</h2>
      <p>Romanos 3 é o coração teológico da carta — e possivelmente o capítulo mais importante de toda a Bíblia para a doutrina da justificação. Após provar que gentios (cap. 1) e judeus (cap. 2) estão igualmente sob condenação, Paulo apresenta a solução: a justificação pela fé na obra expiatória de Cristo. Os versículos 21-26 são frequentemente chamados de "o coração do Evangelho".</p>
    </div>

    <div class="section-block">
      <h2>✡️ A Vantagem do Judeu (3:1-8)</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 3:1-4</div>
        <div class="texto-v">"Qual é, pois, a vantagem do judeu? Ou qual o proveito da circuncisão? Muito em tudo. Primeiramente, porque os oráculos de Deus lhes foram confiados... Seja Deus verdadeiro, e todo homem mentiroso."</div>
        <div class="analise-v">Paulo antecipa uma objeção: se judeus e gentios estão igualmente condenados, qual foi o ponto de ser judeu? A resposta é "muito em tudo" — o maior privilégio sendo a posse dos "oráculos de Deus" (<em>logia tou theou</em>) — as Escrituras. A infidelidade humana não anula a fidelidade de Deus (<em>pistis tou theou</em>). A citação do Salmo 51:4 — "Para que sejas justificado nas tuas palavras, e vences quando julgado" — estabelece o princípio: Deus é sempre verdadeiro, mesmo quando toda a humanidade é mentirosa. A fidelidade de Deus não depende da fidelidade humana.</div>
      </div>
    </div>

    <div class="section-block">
      <h2>🌍 Todos Sob o Pecado (3:9-20)</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 3:9-12</div>
        <div class="texto-v">"Que, pois? Somos nós melhores do que eles? De modo nenhum; porque já dantes demonstramos que, tanto judeus como gregos, todos estão debaixo do pecado. Como está escrito: Não há um justo, nem um sequer. Não há nenhum que entenda; não há nenhum que busque a Deus. Todos se desviaram..."</div>
        <div class="analise-v">Paulo cita uma cadeia de textos do AT (Sl 14:1-3; 53:1-3; 5:9; 140:3; 10:7; Is 59:7-8; Sl 36:1) para provar que a condenação universal não é uma novidade cristã — é o testemunho das próprias Escrituras judaicas. A afirmação "não há um justo, nem um sequer" (<em>ouk estin dikaios oude heis</em>) é absoluta e universal. "Não há nenhum que busque a Deus" é especialmente chocante: a busca religiosa humana não é busca por Deus — é busca por um deus que sirva aos nossos propósitos. A verdadeira busca por Deus é ela mesma um dom da graça.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 3:19-20</div>
        <div class="texto-v">"Ora, sabemos que tudo o que a lei diz, diz àqueles que estão debaixo da lei, para que toda a boca se cale, e todo o mundo esteja sujeito ao juízo de Deus. Porque pelas obras da lei nenhuma carne será justificada diante dele; em razão de que pela lei vem o conhecimento do pecado."</div>
        <div class="analise-v">A função da lei (<em>nomos</em>) não é justificar — é condenar. A lei fecha toda a boca (<em>phtariston pan stoma</em>) — elimina toda justificativa, toda desculpa, toda pretensão de inocência. "Pelo conhecimento do pecado" (<em>epignosis hamartias</em>) — a lei não dá poder para vencer o pecado; ela revela o pecado em toda a sua gravidade. Este versículo é a conclusão da seção 1:18-3:20: toda a humanidade está culpada diante de Deus. Mas esta conclusão sombria é necessária para que a boa nova de 3:21-26 seja verdadeiramente boa.</div>
      </div>
    </div>

    <div class="section-block">
      <h2>⭐ O Coração do Evangelho: Justificação pela Fé (3:21-26)</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 3:21-24</div>
        <div class="texto-v">"Mas agora, independentemente da lei, a justiça de Deus se manifestou, sendo testificada pela lei e pelos profetas; a justiça de Deus pela fé em Jesus Cristo, para todos e sobre todos os que creem; porque não há diferença. Porque todos pecaram e destituídos estão da glória de Deus; sendo justificados gratuitamente pela sua graça, pela redenção que há em Cristo Jesus."</div>
        <div class="analise-v">O "mas agora" (<em>nyni de</em>) é a virada mais dramática de toda a teologia bíblica. Após 3 capítulos de condenação, a solução divina irrompe. Quatro palavras-chave definem a justificação: (1) <em>dikaiosyne theou</em> — justiça de Deus: não a justiça que Deus exige, mas a que ele provê; (2) <em>dia pisteos</em> — pela fé: o instrumento que recebe a justiça; (3) <em>dorean</em> — gratuitamente, de graça: não como salário, mas como presente; (4) <em>apolytrosis</em> — redenção: libertação mediante pagamento de resgate. "Todos pecaram" (<em>pantes hemarton</em>) — aoristo, ação pontual: a queda em Adão. "Destituídos estão da glória de Deus" (<em>hysterountai tes doxes tou theou</em>) — presente, estado contínuo: a condição atual da humanidade.</div>
      </div>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 3:25-26</div>
        <div class="texto-v">"Ao qual Deus propôs como propiciação pela fé no seu sangue, para demonstração da sua justiça pela remissão dos pecados dantes cometidos, sob a paciência de Deus; para demonstração, neste tempo, da sua justiça; para ser ele justo e justificador daquele que tem fé em Jesus."</div>
        <div class="analise-v"><em>Hilasterion</em> — propiciação (ou expiação): esta palavra grega é usada na LXX para o "propiciatório" — a tampa da Arca da Aliança onde o sangue era aspergido no Dia da Expiação (Lv 16). Paulo está dizendo que Jesus é o novo e definitivo Propiciatório — o lugar onde a ira de Deus é satisfeita e a misericórdia de Deus é revelada. O problema teológico que a cruz resolve: como pode Deus ser simultaneamente justo (punindo o pecado) e justificador (absolvendo o pecador)? A resposta: na cruz, Deus puniu o pecado em Cristo — assim ele é justo (<em>dikaion</em>) e ao mesmo tempo justifica (<em>dikaiounta</em>) aquele que crê. A cruz não é Deus perdoando sem punir — é Deus punindo em si mesmo para poder perdoar.</div>
      </div>
    </div>

    <div class="section-block">
      <h2>🏆 Conclusão: Glória Excluída, Fé Estabelecida (3:27-31)</h2>
      <div class="versiculo-bloco">
        <div class="ref-v">Romanos 3:27-28</div>
        <div class="texto-v">"Onde está, pois, a glória? Foi excluída. Por qual lei? Das obras? Não, mas pela lei da fé. Concluímos, pois, que o homem é justificado pela fé sem as obras da lei."</div>
        <div class="analise-v">A justificação pela fé elimina toda glória humana (<em>kauchesis</em>). Se a salvação fosse pelas obras, o salvo poderia se gloriar — mas a fé exclui a glória porque ela não é uma obra, mas uma recepção. A "lei da fé" (<em>nomos pisteos</em>) não é uma lei que exige fé — é o princípio que opera pela fé. Paulo está contrastando dois sistemas: o sistema de obras (onde o ser humano contribui para sua salvação) e o sistema de fé (onde o ser humano apenas recebe o que Deus provê). A Reforma Protestante resumiu isso em <em>sola fide</em> — somente pela fé.</div>
      </div>
    </div>"""

# ============================================================
# Função para gerar capítulos 4-16 com conteúdo substancial
# ============================================================
def gerar_cap_romanos(num, titulo, versiculo_chave, ref_chave, secoes):
    """Gera um capítulo de Romanos com múltiplas seções"""
    conteudo = ""
    for titulo_sec, versiculos in secoes:
        conteudo += f"""
    <div class="section-block">
      <h2>{titulo_sec}</h2>
"""
        for ref, texto, analise in versiculos:
            conteudo += f"""      <div class="versiculo-bloco">
        <div class="ref-v">{ref}</div>
        <div class="texto-v">"{texto}"</div>
        <div class="analise-v">{analise}</div>
      </div>
"""
        conteudo += "    </div>\n"
    return conteudo

# Capítulos 4-16 de Romanos
caps_romanos = {
    4: ("Abraão: O Pai da Fé",
        "Abraão creu em Deus, e isso lhe foi imputado como justiça.",
        "Romanos 4:3",
        [("🌟 Abraão Justificado pela Fé, não pelas Obras (4:1-8)", [
            ("Romanos 4:2-5", "Porque se Abraão foi justificado pelas obras, tem de que se gloriar, mas não diante de Deus. Pois que diz a Escritura? E creu Abraão em Deus, e isso lhe foi imputado como justiça. Ora, ao que obra, o salário não é imputado segundo a graça, mas segundo a dívida. Mas ao que não obra, mas crê naquele que justifica o ímpio, a sua fé lhe é imputada como justiça.",
             "A palavra-chave é <em>logizomai</em> — imputar, creditar, contar. É um termo contábil: a justiça de Cristo é creditada na conta do crente. Abraão não foi justificado por suas obras (a circuncisão veio depois — 4:10) nem pela lei (que ainda não existia — 4:13). Ele foi justificado pela fé. O exemplo de Davi (4:6-8, citando Sl 32:1-2) confirma: a bênção é a não-imputação do pecado — Deus não conta os pecados contra o crente que confia em Cristo."),
            ("Romanos 4:9-12", "Esta bem-aventurança é, pois, para a circuncisão, ou também para a incircuncisão? Porque dizemos que a fé foi imputada a Abraão como justiça. Como, pois, lhe foi imputada? Estando ele na circuncisão ou na incircuncisão? Não na circuncisão, mas na incircuncisão.",
             "Paulo demonstra que Abraão foi justificado (Gn 15:6) antes de ser circuncidado (Gn 17) — com um intervalo de pelo menos 14 anos. A circuncisão foi um <em>semeion</em> (sinal) e <em>sphragida</em> (selo) da justiça que ele já tinha pela fé. Portanto, Abraão é pai tanto dos incircuncisos que creem quanto dos circuncisos que seguem seus passos de fé. A paternidade de Abraão é espiritual, não biológica.")
        ]),
        ("⭐ A Promessa pela Fé, não pela Lei (4:13-25)", [
            ("Romanos 4:16-17", "Por isso é pela fé, para que seja segundo a graça, a fim de que a promessa seja firme a toda a descendência; não somente à que é da lei, mas também à que é da fé de Abraão, o qual é pai de todos nós. Como está escrito: Eu te constituí pai de muitas nações.",
             "A promessa a Abraão — herdar o mundo (<em>kleronom... ton kosmon</em>) — foi feita pela graça, recebida pela fé. Se fosse pela lei, seria condicional e sujeita à maldição (Gl 3:10). Mas sendo pela graça, é firme (<em>bebaian</em>) para toda a descendência — tanto judeus quanto gentios. A fé de Abraão é o modelo: ele creu em Deus que 'vivifica os mortos e chama as coisas que não são como se fossem' — a mesma fé que crê na ressurreição de Cristo."),
            ("Romanos 4:20-25", "E não duvidou da promessa de Deus por incredulidade; antes foi fortalecido na fé, dando glória a Deus, e estando plenamente certo de que o que Deus tinha prometido era também poderoso para o cumprir. Por isso também lhe foi imputado como justiça. Ora, não foi escrito somente por causa dele que lhe foi imputado, mas também por causa de nós, a quem será imputado, que cremos naquele que ressuscitou dentre os mortos a Jesus nosso Senhor.",
             "A fé de Abraão não foi fé cega — foi fé informada pela promessa de Deus. Ele considerou seu corpo 'já mortificado' (com ~100 anos) e o ventre de Sara 'já morto' — e ainda assim creu. Esta fé 'deu glória a Deus' (<em>edoxasen ton theon</em>) — a fé genuína honra a Deus ao confiar em sua palavra contra toda evidência contrária. A aplicação para nós: a mesma fé que creu na promessa da descendência agora crê na ressurreição de Cristo — e a mesma imputação de justiça se aplica.")
        ])]),
    5: ("Paz com Deus e o Dom da Graça",
        "Justificados, pois, pela fé, temos paz com Deus por nosso Senhor Jesus Cristo.",
        "Romanos 5:1",
        [("☮️ Os Frutos da Justificação (5:1-11)", [
            ("Romanos 5:1-5", "Justificados, pois, pela fé, temos paz com Deus por nosso Senhor Jesus Cristo; pelo qual também temos entrada pela fé a esta graça em que estamos firmes, e nos gloriamos na esperança da glória de Deus. E não somente isso, mas também nos gloriamos nas tribulações; sabendo que a tribulação produz a paciência, e a paciência a experiência, e a experiência a esperança. E a esperança não confunde, porquanto o amor de Deus está derramado em nossos corações pelo Espírito Santo que nos foi dado.",
             "A justificação produz cinco frutos imediatos: (1) <em>eirene pros ton theon</em> — paz com Deus: não apenas paz de consciência, mas o fim do estado de guerra entre Deus e o pecador; (2) acesso (<em>prosagogen</em>) à graça: entrada no relacionamento com Deus; (3) esperança da glória: certeza futura; (4) glória nas tribulações (<em>thlipsesin</em>): a tribulação não é obstáculo à esperança — é o caminho para ela, produzindo paciência (<em>hypomone</em>) → experiência (<em>dokime</em>) → esperança; (5) o amor de Deus derramado pelo Espírito Santo. A cadeia tribulação → paciência → experiência → esperança é a pedagogia divina do sofrimento."),
            ("Romanos 5:6-11", "Porque Cristo, quando ainda éramos fracos, morreu a seu tempo pelos ímpios... Mas Deus prova o seu amor para conosco, em que Cristo morreu por nós, sendo nós ainda pecadores. Logo, muito mais, sendo já justificados pelo seu sangue, seremos por ele salvos da ira.",
             "A prova do amor de Deus não é abstrata — é histórica e específica: Cristo morreu pelos ímpios (<em>asthenes</em> — fracos, sem força), pelos pecadores (<em>hamartolon</em>), pelos inimigos (<em>echthrous</em>). A lógica é <em>a fortiori</em> (do menor para o maior): se Deus amou tanto a ponto de dar seu Filho quando éramos inimigos, quanto mais ele nos salvará agora que somos filhos? A reconciliação (<em>katallagen</em>) é o estado presente; a salvação final (<em>sothesoimetha</em>) é a certeza futura.")
        ]),
        ("👥 Adão e Cristo: Dois Representantes (5:12-21)", [
            ("Romanos 5:12", "Portanto, como por um homem entrou o pecado no mundo, e pelo pecado a morte, assim também a morte passou a todos os homens, por isso que todos pecaram.",
             "Este versículo é a base bíblica da doutrina do pecado original. Por um homem (<em>di henos anthropou</em>) — Adão — o pecado entrou no mundo. A morte passou a todos porque todos pecaram (<em>eph ho pantes hemarton</em>). A interpretação desta frase é debatida: (1) todos pecaram em Adão (pecado imputado — Agostinho, Calvino); (2) todos pecaram individualmente (Pelágio — rejeitado pela Igreja). Paulo parece ensinar a imputação: a morte reinou mesmo sobre aqueles que não pecaram 'à semelhança da transgressão de Adão' (5:14) — o que só faz sentido se o pecado de Adão foi imputado a eles."),
            ("Romanos 5:15-19", "Mas não é com o dom como foi com a ofensa; porque, se pela ofensa de um morreram muitos, muito mais a graça de Deus e o dom pela graça de um homem, Jesus Cristo, abundou sobre muitos... Porque, assim como pela desobediência de um homem muitos foram constituídos pecadores, assim também pela obediência de um muitos serão constituídos justos.",
             "O paralelo Adão-Cristo é o fundamento da doutrina da imputação dupla: o pecado de Adão é imputado a todos os seus descendentes; a justiça de Cristo é imputada a todos os que creem. Mas há uma assimetria: a graça é muito mais abundante (<em>perisseuein</em>) que a ofensa. Adão nos tornou pecadores por desobediência (<em>parakoe</em>); Cristo nos torna justos por obediência (<em>hypakoe</em>) — sua vida perfeita e sua morte substitutiva. A obediência ativa de Cristo (vivendo a lei perfeitamente) e sua obediência passiva (morrendo em nosso lugar) são ambas necessárias para nossa justificação.")
        ])]),
    6: ("Mortos para o Pecado, Vivos em Cristo",
        "Assim também vós considerai-vos mortos para o pecado, mas vivos para Deus em Cristo Jesus.",
        "Romanos 6:11",
        [("💀 Mortos com Cristo no Batismo (6:1-14)", [
            ("Romanos 6:1-4", "Que diremos, pois? Permaneceremos no pecado para que a graça abunde? De modo nenhum! Nós, que estamos mortos para o pecado, como viveremos ainda nele? Ou não sabeis que todos nós que fomos batizados em Cristo Jesus fomos batizados na sua morte? Fomos, pois, sepultados com ele pelo batismo na morte, para que, como Cristo ressuscitou dos mortos pela glória do Pai, assim também nós andemos em novidade de vida.",
             "Paulo antecipa a objeção antinomiana: se a graça abunda onde o pecado abunda, por que não pecar mais? A resposta é ontológica, não apenas moral: o crente está morto para o pecado. O batismo (<em>baptisma</em>) é o sinal visível de uma realidade espiritual: a união com Cristo na sua morte e ressurreição. 'Fomos batizados na sua morte' — o batismo não causa a morte ao pecado, mas a simboliza e sela. A 'novidade de vida' (<em>kainoteti zoes</em>) não é uma possibilidade — é uma realidade que deve ser vivida."),
            ("Romanos 6:6-7", "Sabendo isto, que o nosso homem velho foi com ele crucificado, para que o corpo do pecado seja destruído, a fim de que não sirvamos mais ao pecado. Porque o que é morto está justificado do pecado.",
             "O 'homem velho' (<em>palaios anthropos</em>) é o eu adâmico — a identidade centrada no pecado que herdamos de Adão. Ele foi crucificado com Cristo — não está sendo crucificado (processo contínuo) mas foi crucificado (evento passado, completado). O 'corpo do pecado' (<em>soma tes hamartias</em>) não é o corpo físico (que é bom — criado por Deus) mas o corpo enquanto dominado pelo pecado. A morte liberta do poder do pecado — o morto não pode mais ser escravo.")
        ]),
        ("⚡ Escravos da Justiça (6:15-23)", [
            ("Romanos 6:16-18", "Não sabeis que, a quem vos apresentais por servos para obedecer, seus servos sois, daquele a quem obedeceis, seja do pecado para a morte, seja da obediência para a justiça? Mas graças a Deus que, tendo sido servos do pecado, obedecestes de coração à forma de doutrina a que fostes entregues. E, libertados do pecado, fostes feitos servos da justiça.",
             "Paulo usa a metáfora da escravidão (<em>doulos</em>) para descrever a condição humana: todos são escravos de algo — ou do pecado ou da justiça. A liberdade absoluta não existe — a questão é de quem você é escravo. A conversão não é libertação para a autonomia — é transferência de um senhor para outro. Mas a diferença é absoluta: o pecado paga com morte (<em>thanatos</em>); Deus dá vida eterna (<em>zoe aionios</em>) como dom gratuito (<em>charisma</em>).")
        ])]),
    7: ("A Luta Interior — Lei, Pecado e o Eu",
        "Miserável homem que sou! Quem me livrará do corpo desta morte?",
        "Romanos 7:24",
        [("📜 Libertos da Lei pelo Corpo de Cristo (7:1-6)", [
            ("Romanos 7:4-6", "Assim, meus irmãos, também vós fostes mortos para a lei pelo corpo de Cristo, para serdes de outro, daquele que ressuscitou dos mortos, a fim de que frutifiquemos para Deus. Porque, quando estávamos na carne, as paixões dos pecados, que são pela lei, operavam em nossos membros para frutificarmos para a morte. Mas agora estamos livres da lei, tendo morrido para aquilo em que estávamos retidos; de sorte que servimos em novidade de espírito, e não na velhice da letra.",
             "A analogia do casamento (7:1-3) ilustra a libertação da lei: assim como a morte dissolve o vínculo matrimonial, a morte de Cristo dissolve o vínculo da lei sobre o crente. O crente não está 'sob a lei' (<em>hypo nomon</em>) como sistema de justificação — mas serve a Deus 'em novidade de espírito' (<em>kainoteti pneumatos</em>). Isto não é antinomismo — é a lei cumprida pelo Espírito de dentro para fora, não imposta de fora para dentro.")
        ]),
        ("⚔️ A Lei é Santa, mas o Pecado é Poderoso (7:7-25)", [
            ("Romanos 7:7-12", "Que diremos, pois? É a lei pecado? De modo nenhum! Mas eu não conheci o pecado senão pela lei... Assim, a lei na verdade é santa, e o mandamento santo, justo e bom.",
             "Paulo defende a santidade da lei contra o antinomismo. A lei não é pecado — ela revela o pecado. O exemplo do décimo mandamento ('não cobiçarás') é revelador: a cobiça (<em>epithymian</em>) só é reconhecida como pecado quando a lei a nomeia. O pecado usa o mandamento como oportunidade (<em>aphorme</em>) para produzir toda cobiça — a proibição paradoxalmente estimula o desejo. Isto não é falha da lei — é a perversidade do pecado que perverte até as coisas boas."),
            ("Romanos 7:15-20", "Porque o que faço, não o aprovo; pois não faço o que quero, mas o que odeio, isso faço... Porque não faço o bem que quero, mas o mal que não quero, esse faço. Ora, se faço o que não quero, já não sou eu quem o faz, mas o pecado que habita em mim.",
             "Este é um dos textos mais debatidos de toda a Bíblia: Paulo está descrevendo um crente ou um incrédulo? A maioria dos reformadores (Agostinho tardio, Lutero, Calvino) entende que é a experiência do crente regenerado que ainda luta com a carne. A divisão interna — querer o bem mas fazer o mal — é característica da regeneração, não da escravidão irrefletida ao pecado. O incrédulo não tem esse conflito porque não tem o Espírito que ama a lei de Deus (7:22)."),
            ("Romanos 7:24-25", "Miserável homem que sou! Quem me livrará do corpo desta morte? Graças a Deus por Jesus Cristo nosso Senhor! Assim que eu mesmo com o entendimento sirvo à lei de Deus, mas com a carne à lei do pecado.",
             "O grito de angústia de 7:24 é respondido imediatamente em 7:25a com ação de graças — a libertação já foi provida em Cristo. O 'corpo desta morte' (<em>soma tou thanatou toutou</em>) pode aludir à prática romana de amarrar um cadáver ao assassino como punição. O pecado é como um cadáver amarrado ao crente — presente, pesado, corrompendo. Mas Cristo liberta. O capítulo 8 é a resposta gloriosa ao grito de 7:24.")
        ])]),
    8: ("Vida no Espírito — O Capítulo da Glória",
        "Nenhuma condenação há, pois, para os que estão em Cristo Jesus.",
        "Romanos 8:1",
        [("🕊️ Nenhuma Condenação — Vida no Espírito (8:1-17)", [
            ("Romanos 8:1-4", "Nenhuma condenação há, pois, para os que estão em Cristo Jesus, que não andam segundo a carne, mas segundo o Espírito. Porque a lei do Espírito de vida, em Cristo Jesus, me livrou da lei do pecado e da morte. Pois o que era impossível à lei, visto como estava enfraquecida pela carne, Deus o fez, enviando o seu próprio Filho em semelhança da carne do pecado, por causa do pecado, e condenou o pecado na carne.",
             "<em>Ouden ara nyn katakrima</em> — 'Nenhuma condenação, pois, agora' — é a declaração mais libertadora da Bíblia. O 'agora' (<em>nyn</em>) é crucial: não apenas no futuro (no julgamento final) mas agora, no presente. A 'lei do Espírito de vida' (<em>nomos tou pneumatos tes zoes</em>) supera a 'lei do pecado e da morte'. O que a lei mosaica não pôde fazer (porque estava enfraquecida pela carne), Deus fez: enviou seu Filho para condenar o pecado na carne — na encarnação e na cruz, o pecado foi julgado definitivamente."),
            ("Romanos 8:14-17", "Porque todos os que são guiados pelo Espírito de Deus são filhos de Deus. Porque não recebestes o espírito de escravidão para viverdes de novo em temor, mas recebestes o espírito de adoção, pelo qual clamamos: Aba, Pai! O mesmo Espírito testifica com o nosso espírito que somos filhos de Deus. E, se filhos, também herdeiros; herdeiros de Deus e co-herdeiros com Cristo.",
             "A adoção (<em>hyiothesia</em>) é um dos conceitos mais ricos da teologia paulina. O Espírito não é um espírito de escravidão (<em>douleia</em>) que produz medo — é o Espírito de adoção que nos habilita a clamar 'Aba, Pai' (<em>Abba ho Pater</em>). 'Aba' é o aramaico íntimo para pai — a palavra que Jesus usou em Getsêmani (Mc 14:36). O Espírito testifica com (<em>symmartyreo</em>) nosso espírito — não ao nosso espírito, mas junto com ele, em confirmação mútua. Filhos → herdeiros → co-herdeiros com Cristo: a herança inclui tanto o sofrimento quanto a glória.")
        ]),
        ("🌟 Glória Futura e Intercessão do Espírito (8:18-30)", [
            ("Romanos 8:18-23", "Porque para mim tenho por certo que as aflições do tempo presente não são para comparar com a glória que em nós há de ser revelada. Porque a ardente expectação da criação aguarda a manifestação dos filhos de Deus... Porque sabemos que toda a criação geme e está juntamente em dores de parto até agora.",
             "Paulo expande a visão da redenção para além da humanidade: toda a criação (<em>pasa he ktisis</em>) geme (<em>systenazei</em>) e está em dores de parto (<em>synodino</em>). A criação foi sujeitada à vaidade (<em>mataioteti</em>) — não voluntariamente, mas por causa de Adão (Gn 3:17-19). Mas ela aguarda (<em>apekdechetai</em>) com ardente expectação (<em>apokaradokia</em> — literalmente, pescoço esticado para frente) a manifestação dos filhos de Deus. A redenção final não é apenas espiritual — é cósmica. O novo céu e a nova terra (Ap 21-22) são a resposta à gemência da criação."),
            ("Romanos 8:26-28", "Da mesma forma, o Espírito também nos ajuda nas nossas fraquezas; porque não sabemos orar como convém, mas o mesmo Espírito intercede por nós com gemidos inexprimíveis... E sabemos que todas as coisas contribuem juntamente para o bem daqueles que amam a Deus, daqueles que são chamados segundo o seu propósito.",
             "A intercessão do Espírito (<em>hyperentynchanei</em> — intercede com intensidade) com 'gemidos inexprimíveis' (<em>stenagmois alaletos</em>) é um dos textos mais consoladores da Bíblia. Quando não sabemos como orar, o Espírito ora por nós com uma profundidade que transcende palavras. Romanos 8:28 — 'todas as coisas contribuem para o bem' (<em>panta synergei eis agathon</em>) — não é um otimismo ingênuo. É uma afirmação teológica: para aqueles que amam a Deus e são chamados segundo seu propósito, até o sofrimento, a perda e a dor são instrumentos da providência divina.")
        ]),
        ("🏆 A Cadeia de Ouro e o Amor Invencível (8:29-39)", [
            ("Romanos 8:29-30", "Porque os que dantes conheceu, também os predestinou para serem conformes à imagem de seu Filho, a fim de que ele seja o primogênito entre muitos irmãos. E aos que predestinou, a esses também chamou; e aos que chamou, a esses também justificou; e aos que justificou, a esses também glorificou.",
             "A 'cadeia de ouro' da salvação: <em>proegnō</em> (pré-conheceu) → <em>proōrisen</em> (predestinou) → <em>ekalesen</em> (chamou) → <em>edikaiōsen</em> (justificou) → <em>edoxasen</em> (glorificou). O uso do aoristo para 'glorificou' é notável — Paulo usa o passado para descrever o que ainda está no futuro, tal é a certeza da glorificação. A predestinação em Paulo não é para a condenação — é para a conformidade com a imagem de Cristo (<em>symmorphous tes eikonos tou hyiou autou</em>). O propósito final da salvação não é apenas o céu — é a restauração da imagem de Deus no ser humano."),
            ("Romanos 8:35-39", "Quem nos separará do amor de Cristo? A tribulação, ou a angústia, ou a perseguição, ou a fome, ou a nudez, ou o perigo, ou a espada?... Mas em todas estas coisas somos mais do que vencedores, por meio daquele que nos amou. Porque estou persuadido de que nem a morte, nem a vida, nem os anjos, nem os principados, nem as potestades, nem o presente, nem o porvir, nem a altura, nem a profundidade, nem alguma outra criatura nos poderá separar do amor de Deus, que está em Cristo Jesus nosso Senhor.",
             "O clímax de Romanos 8 — e possivelmente de toda a teologia paulina. A lista de 10 poderes que não podem separar o crente do amor de Deus é exaustiva: morte, vida, anjos, principados, potestades, presente, futuro, altura, profundidade, 'alguma outra criatura'. Nada no universo — nem forças espirituais, nem dimensões temporais, nem realidades espaciais — pode romper o vínculo entre o crente e o amor de Deus em Cristo. 'Mais do que vencedores' (<em>hypernikomen</em>) — não apenas vencemos, mas vencemos com sobra, com excesso, com glória.")
        ])]),
}

# Gerar capítulos 1-3 com conteúdo completo
for num, conteudo, titulo, vk, rk in [
    (1, r1, "O Evangelho e a Depravação Humana", "Porque não me envergonho do evangelho de Cristo, pois é o poder de Deus para a salvação.", "Romanos 1:16"),
    (2, r2, "O J
