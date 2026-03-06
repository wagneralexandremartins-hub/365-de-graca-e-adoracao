#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar capítulos aprofundados das Epístolas Paulinas
com análise versículo por versículo, contexto histórico e vocabulário grego.
"""

import os

CSS_TEMPLATE = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: #0f172a; color: #e2e8f0; font-family: 'Georgia', serif; line-height: 1.7; }
    a { color: inherit; text-decoration: none; }
    .topbar { background: rgba(15,23,42,0.97); border-bottom: 1px solid rgba(255,255,255,0.07); padding: 14px 0; position: sticky; top: 0; z-index: 100; }
    .topbar .inner { max-width: 900px; margin: 0 auto; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
    .topbar a { font-size: 0.85rem; color: #94a3b8; font-weight: 600; transition: color 0.2s; }
    .topbar a:hover { color: {COLOR}; }
    .hero { background: linear-gradient(135deg, #0f172a 0%, {HERO_BG} 50%, #0f172a 100%); padding: 64px 24px 48px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.07); }
    .tag { display: inline-block; background: {TAG_BG}; border: 1px solid {TAG_BORDER}; color: {COLOR}; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 999px; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 1px; }
    .hero h1 { font-size: 2.4rem; font-weight: 900; color: #f1f5f9; margin-bottom: 12px; line-height: 1.2; }
    .hero .ref { font-size: 0.88rem; color: #64748b; margin-bottom: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .hero blockquote { font-style: italic; color: #cbd5e1; font-size: 1rem; border-left: 3px solid {COLOR}; padding-left: 20px; max-width: 600px; margin: 0 auto; text-align: left; }
    .wrap { max-width: 900px; margin: 0 auto; padding: 40px 24px 80px; }
    .section-block { margin-bottom: 40px; }
    .section-block h2 { font-size: 1.3rem; font-weight: 800; color: #f1f5f9; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.07); }
    .section-block p { color: #94a3b8; font-size: 0.95rem; line-height: 1.85; margin-bottom: 16px; }
    .mapa-box { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 24px 28px; margin: 22px 0; }
    .mapa-box h3 { color: {COLOR}; font-size: 1rem; margin: 0 0 12px; }
    .mapa-visual { background: linear-gradient(135deg,rgba(15,23,42,0.9) 0%,rgba(30,41,59,0.9) 100%); border: 1px solid {TAG_BORDER}; border-radius: 12px; padding: 28px; margin: 12px 0; position: relative; overflow: hidden; min-height: 180px; display: flex; align-items: center; justify-content: center; }
    .mapa-visual::before { content: '🗺️'; position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); font-size: 5rem; opacity: 0.08; }
    .mapa-desc { color: #94a3b8; font-size: 0.91rem; line-height: 1.75; margin-top: 12px; }
    .mapa-pontos { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }
    .mapa-ponto { background: {TAG_BG}; border: 1px solid {TAG_BORDER}; color: {COLOR}; font-size: 0.78rem; font-weight: 700; padding: 4px 12px; border-radius: 999px; }
    .versiculo-bloco { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-left: 3px solid {COLOR}; border-radius: 0 12px 12px 0; padding: 18px 20px; margin-bottom: 16px; }
    .ref-v { font-size: 0.8rem; font-weight: 800; color: {COLOR}; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
    .texto-v { font-style: italic; color: #cbd5e1; font-size: 0.95rem; margin-bottom: 10px; line-height: 1.7; }
    .analise-v { color: #94a3b8; font-size: 0.9rem; line-height: 1.8; }
    .vocab-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 14px; margin-top: 16px; }
    .vocab-card { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-radius: 10px; padding: 14px 16px; }
    .termo { font-size: 1.1rem; font-weight: 800; color: {COLOR}; font-family: 'Georgia', serif; }
    .transl { font-size: 0.78rem; color: #64748b; font-style: italic; margin: 2px 0 6px; }
    .def { font-size: 0.85rem; color: #94a3b8; line-height: 1.65; }
    .nav-cap { display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.07); }
    .nav-cap a { background: {TAG_BG}; border: 1px solid {TAG_BORDER}; color: {COLOR}; text-decoration: none; padding: 10px 20px; border-radius: 8px; font-size: 0.88rem; font-weight: 700; transition: all 0.2s; }
    .nav-cap a:hover { background: {TAG_HOVER}; }
"""

# Dados dos capítulos aprofundados
CAPITULOS = {
    "galatas": {
        "color": "#818cf8",
        "hero_bg": "#0a0a1f",
        "tag_bg": "rgba(129,140,248,0.1)",
        "tag_border": "rgba(129,140,248,0.25)",
        "tag_hover": "rgba(129,140,248,0.2)",
        "livro": "Gálatas",
        "total": 6,
        "capitulos": {
            1: {
                "titulo": "Gálatas 1 — Outro Evangelho Não Há",
                "ref": "Gálatas 1:1-24 · Paulo · c. 48-55 d.C.",
                "versículo_chave": "Mas, ainda que nós ou um anjo do céu vos pregue algum evangelho além do que já vos pregamos, seja anátema. — Gálatas 1:8",
                "contexto": """<p>Gálatas é provavelmente a carta mais apaixonada e urgente de Paulo — ele não abre com ação de graças (como em todas as outras cartas), mas vai diretamente ao problema: as igrejas da Galácia estão sendo seduzidas por "outro evangelho" que exige a circuncisão e a observância da Lei mosaica como condição para a salvação. Os "judaizantes" — cristãos judeus que insistiam que os gentios deveriam se tornar judeus para ser plenamente salvos — haviam chegado às igrejas que Paulo fundou e estavam desfazendo seu trabalho.</p>
<p>A questão em Gálatas não é periférica — é central: o que é o Evangelho? É graça mais obras? É fé mais circuncisão? Paulo responde com uma clareza que não deixa espaço para ambiguidade: qualquer adição ao Evangelho da graça é uma perversão do Evangelho. Esta carta é o "manifesto da liberdade cristã" — e foi o texto que desencadeou a Reforma Protestante quando Lutero a leu em 1515.</p>
<p>A data e os destinatários de Gálatas são debatidos. A teoria da "Galácia do Sul" (que Paulo escreveu para as igrejas de Antioquia da Pisídia, Icônio, Listra e Derbe, fundadas na primeira viagem missionária) sugere uma data de c. 48-49 d.C. — tornando Gálatas possivelmente a mais antiga carta de Paulo. A teoria da "Galácia do Norte" sugere uma data posterior (c. 53-55 d.C.).</p>""",
                "versiculos": [
                    {
                        "ref": "1:1",
                        "texto": "\"Paulo, apóstolo — não da parte de homens, nem por meio de homem algum, mas por Jesus Cristo e por Deus Pai, que o ressuscitou dentre os mortos.\"",
                        "analise": "A abertura de Gálatas é defensiva e combativa — Paulo está respondendo a ataques à sua autoridade apostólica. Os judaizantes argumentavam que Paulo era um apóstolo de segunda categoria, derivando sua autoridade dos apóstolos de Jerusalém (Pedro, Tiago, João) e portanto subordinado a eles. Paulo refuta esta acusação desde a primeira palavra: seu apostolado não vem de homens (<em>ouk ap' anthrōpōn</em>) nem por meio de homem (<em>oude di' anthrōpou</em>), mas diretamente de Jesus Cristo e de Deus Pai. A ressurreição é mencionada imediatamente — é o fundamento do apostolado de Paulo: ele encontrou o Cristo ressuscitado no caminho de Damasco (At 9; Gl 1:15-16)."
                    },
                    {
                        "ref": "1:6-7",
                        "texto": "\"Maravilho-me de que tão depressa vos afasteis daquele que vos chamou pela graça de Cristo, para seguirdes um evangelho diferente; o qual não é outro, senão que há alguns que vos perturbam e querem perverter o evangelho de Cristo.\"",
                        "analise": "A palavra \"maravilho-me\" (<em>thaumazō</em>) é surpreendente — Paulo normalmente abre com ação de graças. Aqui, em vez de gratidão, há espanto e consternação. \"Tão depressa\" (<em>houtōs tacheōs</em>) indica a rapidez com que os gálatas estavam se desviando — Paulo acabara de fundar essas igrejas. \"Afasteis\" (<em>metatithesthe</em>) é um verbo usado para deserção militar — uma traição. O \"outro evangelho\" (<em>heteron euangelion</em>) não é simplesmente uma variante do mesmo Evangelho — é uma perversão (<em>metastrepsai</em>) do Evangelho de Cristo. A adição de qualquer condição humana (circuncisão, obras da Lei) ao Evangelho da graça não o enriquece — o destrói."
                    },
                    {
                        "ref": "1:8-9 — O Anátema Duplo",
                        "texto": "\"Mas, ainda que nós ou um anjo do céu vos pregue algum evangelho além do que já vos pregamos, seja anátema. Assim como já dissemos, também agora de novo digo: se alguém vos pregar algum evangelho além do que já recebestes, seja anátema.\"",
                        "analise": "O anátema duplo é um dos textos mais fortes do NT. <em>Anathema</em> é a palavra grega para o hebraico <em>cherem</em> — algo entregue à destruição divina, separado de Deus. Paulo está dizendo: quem prega um evangelho diferente está sob a maldição de Deus. A hipérbole é deliberada: \"ainda que nós\" (os apóstolos!) ou \"um anjo do céu\" — nem a autoridade apostólica nem a autoridade angélica pode alterar o Evangelho. O critério de autenticidade do Evangelho não é a autoridade do pregador, mas a conformidade com o Evangelho já revelado. A repetição do anátema no versículo 9 é intencional — Paulo quer que não haja dúvida sobre a seriedade da questão."
                    },
                    {
                        "ref": "1:11-12",
                        "texto": "\"Mas faço-vos saber, irmãos, que o evangelho que foi por mim pregado não é segundo o homem; pois não o recebi de homem algum, nem me foi ensinado, mas recebi-o por revelação de Jesus Cristo.\"",
                        "analise": "Paulo afirma a origem divina do seu Evangelho de forma inequívoca. \"Não é segundo o homem\" (<em>ouk estin kata anthrōpon</em>) — não é de origem humana, não segue lógica humana, não pode ser alterado por autoridade humana. \"Não o recebi de homem algum\" (<em>oute gar egō para anthrōpou parelabon</em>) — Paulo não aprendeu o Evangelho dos apóstolos de Jerusalém, como os judaizantes insinuavam. Ele o recebeu \"por revelação de Jesus Cristo\" (<em>di' apokalypseos Iēsou Christou</em>) — no encontro no caminho de Damasco. Esta afirmação não contradiz o que Paulo diz em 1 Co 15:3 (\"recebi o que também vos transmiti\") — ele recebeu a tradição apostólica, mas sua compreensão do Evangelho da graça veio por revelação direta."
                    },
                    {
                        "ref": "1:13-17 — A Autobiografia de Paulo",
                        "texto": "\"Porque já ouvistes qual foi o meu procedimento outrora no judaísmo, como sobremaneira perseguia a Igreja de Deus e a destruía... Mas, quando aprouve a Deus, que me separou desde o ventre de minha mãe e me chamou pela sua graça, revelar seu Filho em mim...\"",
                        "analise": "Paulo oferece sua autobiografia como prova da origem divina do seu Evangelho. Antes da conversão, ele era o perseguidor mais zeloso da Igreja — o último a inventar um Evangelho favorável aos cristãos. Sua conversão foi um ato soberano de Deus, não uma decisão humana. A linguagem de \"separado desde o ventre de minha mãe\" (<em>aphorisas me ek koilias mētros mou</em>) ecoa deliberadamente Jeremias (Jr 1:5) e o Servo do Senhor (Is 49:1) — Paulo se vê como profeta apostólico com uma missão análoga à dos profetas do AT. \"Revelar seu Filho em mim\" (<em>apokalypsai ton Huion autou en emoi</em>) — a revelação não foi apenas para Paulo, mas <em>em</em> Paulo: uma transformação interior, não apenas uma visão externa."
                    }
                ],
                "vocab": [
                    {"termo": "εὐαγγέλιον", "transl": "euangelion", "def": "Evangelho, boa notícia. Em Gálatas, Paulo defende a pureza do Evangelho da graça contra qualquer adição de obras ou condições humanas. O Evangelho é exclusivamente a boa notícia da justificação pela fé em Cristo."},
                    {"termo": "ἀνάθεμα", "transl": "anathema", "def": "Maldição, separação de Deus. Do hebraico <em>cherem</em> — algo entregue à destruição divina. Paulo usa este termo para quem prega um evangelho diferente do Evangelho da graça."},
                    {"termo": "ἀποκάλυψις", "transl": "apokalypsis", "def": "Revelação, desvelamento. Paulo recebeu o Evangelho por revelação direta de Jesus Cristo, não por transmissão humana. Esta é a base da autoridade independente do seu apostolado."},
                    {"termo": "χάρις", "transl": "charis", "def": "Graça. O conceito central de Gálatas: a salvação é inteiramente dom gratuito de Deus, não mérito humano. Qualquer adição de obras à graça destrói a graça (Rm 11:6)."}
                ],
                "teologia": """<p>Gálatas 1 estabelece dois pilares teológicos fundamentais. Primeiro, a autoridade do Evangelho: o Evangelho não é propriedade de nenhum apóstolo, bispo ou concílio — ele tem autoridade divina que transcende qualquer autoridade humana. Mesmo Paulo, o apóstolo que o recebeu por revelação, não pode alterá-lo. O critério de autenticidade não é a autoridade do pregador, mas a conformidade com o Evangelho já revelado nas Escrituras.</p>
<p>Segundo, a exclusividade da graça: a adição de qualquer condição humana ao Evangelho — circuncisão, obras da Lei, mérito moral — não enriquece o Evangelho, mas o destrói. A graça é graça precisamente porque é incondicional: Deus justifica o ímpio (Rm 4:5), não o merecedor. Esta é a verdade que Paulo defende com tal intensidade em Gálatas — e que a Reforma Protestante redescobriu no século XVI.</p>""",
                "aplicacao": """<p>O anátema duplo de Gálatas 1:8-9 é um texto perturbador para uma cultura que valoriza a tolerância acima de tudo. Mas Paulo não está sendo intolerante — está sendo preciso. Há uma diferença entre questões periféricas onde há espaço para diversidade (como práticas litúrgicas, formas de governo eclesiástico, interpretações proféticas) e questões centrais onde a essência do Evangelho está em jogo. A justificação pela fé, não pelas obras, é uma questão central — não periférica.</p>
<p>A autobiografia de Paulo em Gálatas 1:13-17 é um testemunho poderoso da graça soberana de Deus. O maior perseguidor da Igreja tornou-se seu maior apóstolo — não por mérito, mas por graça. Esta inversão radical é o Evangelho em ação: Deus não escolhe os dignos, mas torna dignos os escolhidos.</p>"""
            }
        }
    },
    "efesios": {
        "color": "#22d3ee",
        "hero_bg": "#001a1f",
        "tag_bg": "rgba(34,211,238,0.1)",
        "tag_border": "rgba(34,211,238,0.25)",
        "tag_hover": "rgba(34,211,238,0.2)",
        "livro": "Efésios",
        "total": 6,
        "capitulos": {
            1: {
                "titulo": "Efésios 1 — Bênçãos Espirituais em Cristo",
                "ref": "Efésios 1:1-23 · Paulo · c. 60-62 d.C. · Roma (prisão)",
                "versículo_chave": "Bendito seja o Deus e Pai de nosso Senhor Jesus Cristo, que nos abençoou com todas as bênçãos espirituais nos lugares celestiais em Cristo. — Efésios 1:3",
                "contexto": """<p>Efésios é uma das "Epístolas da Prisão" — escrita por Paulo durante seu primeiro encarceramento em Roma (c. 60-62 d.C.), junto com Filipenses, Colossenses e Filemon. É uma das cartas mais elevadas teologicamente do NT — mais um tratado teológico do que uma resposta a problemas específicos. Seu tema central é a Igreja como corpo de Cristo e habitação do Espírito, e o plano eterno de Deus de reunir todas as coisas em Cristo.</p>
<p>Éfeso era a capital da província romana da Ásia — uma das maiores cidades do Império, com uma população estimada em 200.000-500.000 habitantes. Era lar do templo de Ártemis (uma das sete maravilhas do mundo antigo), um centro de magia e ocultismo, e uma cidade de intensa atividade comercial e cultural. Paulo passou três anos em Éfeso durante sua terceira viagem missionária (At 20:31) — o período mais longo que passou em qualquer cidade.</p>
<p>O capítulo 1 de Efésios contém uma das mais longas e densas sentenças do NT grego — os versículos 3-14 formam uma única sentença de 202 palavras no original grego, um hino de louvor à Trindade pelo plano eterno de salvação. É um texto que exige leitura lenta e meditativa.</p>""",
                "versiculos": [
                    {
                        "ref": "1:3 — O Hino de Louvor",
                        "texto": "\"Bendito seja o Deus e Pai de nosso Senhor Jesus Cristo, que nos abençoou com todas as bênçãos espirituais nos lugares celestiais em Cristo.\"",
                        "analise": "O hino de Ef 1:3-14 é uma das peças mais sublimes da teologia paulina. A abertura — <em>Eulogētos ho Theos</em> (\"Bendito seja Deus\") — ecoa a forma das bênçãos judaicas (<em>berakot</em>), que começam com \"Bendito seja o Senhor\". Paulo está adaptando a liturgia judaica para a adoração cristã. \"Todas as bênçãos espirituais\" (<em>pasē eulogia pneumatikē</em>) — não algumas, não a maioria, mas todas. A salvação em Cristo é completa e suficiente — nada falta. \"Nos lugares celestiais\" (<em>en tois epouraniois</em>) — esta expressão única de Efésios (aparece 5 vezes: 1:3,20; 2:6; 3:10; 6:12) indica a esfera espiritual onde Cristo reina e onde os crentes já estão posicionados em Cristo, mesmo vivendo na terra."
                    },
                    {
                        "ref": "1:4-6 — Eleição e Predestinação",
                        "texto": "\"Como também nos elegeu nele antes da fundação do mundo, para que fôssemos santos e irrepreensíveis diante dele em amor; e nos predestinou para sermos adotados filhos seus por Jesus Cristo, segundo o beneplácito de sua vontade, para louvor da glória da sua graça.\"",
                        "analise": "A eleição (<em>exelexato hēmas en autō</em>) é \"em Cristo\" — não uma eleição abstrata de indivíduos, mas uma eleição em Cristo, o Eleito por excelência. Quem está em Cristo está entre os eleitos. \"Antes da fundação do mundo\" (<em>pro katabolēs kosmou</em>) — a eleição não é uma resposta de Deus à fé humana prevista; é um ato soberano anterior à criação. O propósito da eleição é moral: \"para que fôssemos santos e irrepreensíveis\" — a eleição não é para privilégio, mas para santidade. A predestinação (<em>proorisas</em>) é para a adoção filial — o destino dos eleitos é ser filhos de Deus, não servos ou escravos. O critério final é teocêntrico: \"para louvor da glória da sua graça\" — a salvação existe para a glória de Deus, não para a satisfação humana."
                    },
                    {
                        "ref": "1:7-10 — Redenção e o Mistério da Vontade de Deus",
                        "texto": "\"Em quem temos a redenção pelo seu sangue, a remissão das ofensas, segundo as riquezas da sua graça... tendo-nos dado a conhecer o mistério da sua vontade, segundo o seu beneplácito, que propusera em si mesmo, de reunir em Cristo todas as coisas.\"",
                        "analise": "\"Redenção\" (<em>apolytrōsis</em>) é um termo do mercado de escravos — o pagamento do resgate para libertar um escravo. A redenção cristã é \"pelo seu sangue\" (<em>dia tou haimatos autou</em>) — não por dinheiro, não por mérito humano, mas pelo sacrifício de Cristo. O \"mistério\" (<em>mystērion</em>) em Paulo não é algo obscuro e incompreensível, mas algo que estava oculto e agora foi revelado: o plano eterno de Deus de \"reunir em Cristo todas as coisas\" (<em>anakephalaiōsasthai ta panta en tō Christō</em>). O verbo <em>anakephalaiōō</em> significa literalmente \"recapitular\" — colocar tudo sob uma única cabeça. Cristo é o ponto de convergência de toda a criação, o princípio unificador do cosmos."
                    },
                    {
                        "ref": "1:13-14 — O Selo do Espírito",
                        "texto": "\"Em quem também vós, depois de terdes ouvido a palavra da verdade, o evangelho da vossa salvação, e tendo crido nele, fostes selados com o Espírito Santo da promessa, que é o penhor da nossa herança.\"",
                        "analise": "O Espírito Santo é descrito com duas metáforas complementares: \"selo\" (<em>sphragizō</em>) e \"penhor\" (<em>arrabōn</em>). O selo era a marca de propriedade e autenticidade — o Espírito marca os crentes como propriedade de Deus. O <em>arrabōn</em> era um termo comercial grego para o depósito inicial que garantia o pagamento futuro — o Espírito é o \"adiantamento\" da herança celestial, a garantia de que o que Deus prometeu será cumprido. A sequência soteriológica nestes versículos é precisa: ouvir o Evangelho → crer → ser selado com o Espírito. A fé precede o selo do Espírito — o Espírito é dado a quem crê, não para produzir a fé."
                    },
                    {
                        "ref": "1:15-23 — A Oração de Paulo pela Igreja",
                        "texto": "\"Por isso também eu, tendo ouvido a fé que tendes no Senhor Jesus e o amor para com todos os santos, não cesso de dar graças por vós, fazendo menção de vós nas minhas orações; para que o Deus de nosso Senhor Jesus Cristo, o Pai da glória, vos dê espírito de sabedoria e de revelação no conhecimento dele.\"",
                        "analise": "A oração de Paulo em Ef 1:15-23 é um modelo de intercessão cristã. Paulo não ora por prosperidade material ou saúde física — ora por três coisas espirituais: (1) \"espírito de sabedoria e de revelação no conhecimento dele\" — conhecimento de Deus, não apenas conhecimento sobre Deus; (2) \"os olhos do vosso entendimento iluminados\" para conhecer a esperança do chamado, as riquezas da herança e a grandeza do poder de Deus; (3) o conhecimento deste poder — o mesmo poder que ressuscitou Cristo e o entronizou acima de todo principado, potestade, poder e domínio. A cristologia dos vv. 20-23 é das mais altas do NT: Cristo ressuscitado está sentado à direita de Deus, acima de toda autoridade cósmica, e é dado como cabeça sobre todas as coisas à Igreja, que é seu corpo."
                    }
                ],
                "vocab": [
                    {"termo": "ἐκλογή", "transl": "eklogē", "def": "Eleição, escolha. Em Efésios, a eleição é \"em Cristo\" — não uma escolha abstrata de indivíduos, mas a inclusão em Cristo, o Eleito. O propósito da eleição é a santidade e a adoção filial."},
                    {"termo": "μυστήριον", "transl": "mystērion", "def": "Mistério. Em Paulo, não algo obscuro, mas algo antes oculto e agora revelado: o plano eterno de Deus de reunir todas as coisas em Cristo. Aparece 6 vezes em Efésios."},
                    {"termo": "ἀρραβών", "transl": "arrabōn", "def": "Penhor, depósito, garantia. Termo comercial grego para o adiantamento que garante o pagamento futuro. O Espírito Santo é o penhor da herança celestial — a garantia de que a salvação será completada."},
                    {"termo": "πλήρωμα", "transl": "plērōma", "def": "Plenitude, completude. A Igreja é a \"plenitude\" de Cristo (Ef 1:23) — não porque Cristo esteja incompleto sem a Igreja, mas porque a Igreja é o espaço onde Cristo se manifesta e atua no mundo."}
                ],
                "teologia": """<p>Efésios 1 é um dos textos mais ricos para a teologia da salvação. O hino de Ef 1:3-14 apresenta a salvação como obra da Trindade: o Pai elege (vv. 4-6), o Filho redime (vv. 7-12), o Espírito sela (vv. 13-14). Cada pessoa da Trindade tem um papel distinto, mas o objetivo é único: "para louvor da glória de Deus" (vv. 6, 12, 14 — a frase aparece três vezes, uma para cada pessoa da Trindade).</p>
<p>A doutrina da eleição em Efésios 1 é apresentada não como um problema filosófico a ser resolvido, mas como motivo de louvor e adoração. Paulo não debate a compatibilidade entre eleição e livre-arbítrio — ele adora. A eleição é "em Cristo" — não um decreto arbitrário sobre indivíduos, mas a inclusão no Eleito por excelência. Quem está em Cristo está entre os eleitos; quem está fora de Cristo está fora da eleição.</p>""",
                "aplicacao": """<p>A oração de Paulo em Ef 1:15-23 desafia o padrão de oração da maioria dos cristãos contemporâneos. Quantas vezes oramos pedindo prosperidade, saúde, sucesso — e quantas vezes oramos pedindo "espírito de sabedoria e de revelação no conhecimento de Deus"? Paulo ora pelo que é mais importante: o conhecimento de Deus, a esperança do chamado, a compreensão do poder divino. Estas são as riquezas que nenhuma perseguição pode roubar e nenhuma crise pode destruir.</p>
<p>A visão cósmica de Efésios 1 — Cristo como cabeça de todas as coisas, a Igreja como seu corpo, o plano eterno de reunir tudo em Cristo — é o antídoto para o provincianismo espiritual. O cristão que vive apenas para sua própria salvação, sua própria família, sua própria comunidade, perdeu de vista a grandeza do plano de Deus. A Igreja existe não apenas para si mesma, mas como instrumento do plano cósmico de Deus de reconciliar todas as coisas em Cristo.</p>"""
            }
        }
    }
}


def gerar_capitulo(livro_key, cap_num, dados_livro, dados_cap):
    """Gera o HTML de um capítulo aprofundado."""
    color = dados_livro["color"]
    hero_bg = dados_livro["hero_bg"]
    tag_bg = dados_livro["tag_bg"]
    tag_border = dados_livro["tag_border"]
    tag_hover = dados_livro["tag_hover"]
    livro = dados_livro["livro"]
    total = dados_livro["total"]

    css = CSS_TEMPLATE.replace("{COLOR}", color).replace("{HERO_BG}", hero_bg) \
        .replace("{TAG_BG}", tag_bg).replace("{TAG_BORDER}", tag_border) \
        .replace("{TAG_HOVER}", tag_hover)

    # Navegação
    prev_cap = f"/07-novo-testamento/{livro_key}/capitulos/capitulo-{cap_num-1:02d}.html" if cap_num > 1 else f"/07-novo-testamento/{livro_key}/index.html"
    prev_label = f"← {livro} {cap_num-1}" if cap_num > 1 else f"← Índice de {livro}"
    next_cap = f"/07-novo-testamento/{livro_key}/capitulos/capitulo-{cap_num+1:02d}.html" if cap_num < total else f"/07-novo-testamento/{livro_key}/index.html"
    next_label = f"{livro} {cap_num+1} →" if cap_num < total else f"Índice de {livro} →"

    # Versículos
    versiculos_html = ""
    for v in dados_cap["versiculos"]:
        versiculos_html += f"""
      <div class="versiculo-bloco">
        <div class="ref-v">{v['ref']}</div>
        <div class="texto-v">{v['texto']}</div>
        <div class="analise-v">{v['analise']}</div>
      </div>"""

    # Vocabulário
    vocab_html = ""
    for v in dados_cap["vocab"]:
        vocab_html += f"""
        <div class="vocab-card">
          <div class="termo">{v['termo']}</div>
          <div class="transl">{v['transl']}</div>
          <div class="def">{v['def']}</div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{dados_cap['titulo']} | 365 de Graça & Adoração</title>
  <link rel="icon" href="/favicon.ico">
  <style>{css}</style>
</head>
<body>
  <div class="topbar"><div class="inner">
    <a href="/07-novo-testamento/{livro_key}/index.html">← {livro}</a>
    <a href="/07-novo-testamento/index.html">Novo Testamento</a>
  </div></div>
  <div class="hero">
    <span class="tag">📜 {livro} {cap_num} · Epístolas Paulinas</span>
    <h1>{dados_cap['titulo']}</h1>
    <div class="ref">{dados_cap['ref']}</div>
    <blockquote>{dados_cap['versículo_chave']}</blockquote>
  </div>
  <div class="wrap">

    <div class="section-block">
      <h2>📜 Contexto Histórico e Literário</h2>
      {dados_cap['contexto']}
    </div>

    <div class="section-block">
      <h2>🔍 Análise Versículo por Versículo</h2>
      {versiculos_html}
    </div>

    <div class="section-block">
      <h2>📚 Vocabulário Grego Essencial</h2>
      <div class="vocab-grid">
        {vocab_html}
      </div>
    </div>

    <div class="section-block">
      <h2>🏛️ Teologia Sistemática</h2>
      {dados_cap['teologia']}
    </div>

    <div class="section-block">
      <h2>✨ Aplicação Contemporânea</h2>
      {dados_cap['aplicacao']}
    </div>

    <div class="nav-cap">
      <a href="{prev_cap}">{prev_label}</a>
      <a href="/07-novo-testamento/{livro_key}/index.html">📋 Índice</a>
      <a href="{next_cap}">{next_label}</a>
    </div>
  </div>
</body>
</html>"""
    return html


def main():
    base_dir = "/home/ubuntu/365-de-graca-e-adoracao/07-novo-testamento"
    
    for livro_key, dados_livro in CAPITULOS.items():
        cap_dir = os.path.join(base_dir, livro_key, "capitulos")
        os.makedirs(cap_dir, exist_ok=True)
        
        for cap_num, dados_cap in dados_livro["capitulos"].items():
            filename = f"capitulo-{cap_num:02d}.html"
            filepath = os.path.join(cap_dir, filename)
            
            html = gerar_capitulo(livro_key, cap_num, dados_livro, dados_cap)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            
            print(f"✅ Criado: {livro_key}/capitulos/{filename}")
    
    print("\n🎉 Capítulos aprofundados gerados com sucesso!")


if __name__ == "__main__":
    main()
