#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera os capítulos 2-6 de Gálatas com análise versículo por versículo aprofundada.
"""

import os

COLOR = "#818cf8"
HERO_BG = "#0a0a1f"
TAG_BG = "rgba(129,140,248,0.1)"
TAG_BORDER = "rgba(129,140,248,0.25)"
TAG_HOVER = "rgba(129,140,248,0.2)"
LIVRO = "Gálatas"
LIVRO_KEY = "galatas"
TOTAL = 6

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
    .vocab-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 14px; margin-top: 16px; }}
    .vocab-card {{ background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-radius: 10px; padding: 14px 16px; }}
    .termo {{ font-size: 1.1rem; font-weight: 800; color: {COLOR}; font-family: 'Georgia', serif; }}
    .transl {{ font-size: 0.78rem; color: #64748b; font-style: italic; margin: 2px 0 6px; }}
    .def {{ font-size: 0.85rem; color: #94a3b8; line-height: 1.65; }}
    .nav-cap {{ display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.07); }}
    .nav-cap a {{ background: {TAG_BG}; border: 1px solid {TAG_BORDER}; color: {COLOR}; text-decoration: none; padding: 10px 20px; border-radius: 8px; font-size: 0.88rem; font-weight: 700; transition: all 0.2s; }}
    .nav-cap a:hover {{ background: {TAG_HOVER}; }}
"""

CAPITULOS = {
    2: {
        "titulo": "Gálatas 2 — Paulo em Jerusalém e o Incidente em Antioquia",
        "ref": "Gálatas 2:1-21 · Paulo · c. 48-55 d.C.",
        "chave": "Estou crucificado com Cristo; e vivo, não mais eu, mas Cristo vive em mim; e a vida que agora vivo na carne, vivo-a pela fé do Filho de Deus, o qual me amou e se entregou a si mesmo por mim. — Gálatas 2:20",
        "contexto": """<p>Gálatas 2 é um capítulo de autobiografia apostólica e confronto teológico. Paulo narra dois eventos cruciais: (1) sua visita a Jerusalém onde os "pilares" da Igreja — Tiago, Pedro e João — reconheceram seu apostolado e seu Evangelho (vv. 1-10); e (2) o incidente em Antioquia, onde Paulo confrontou Pedro publicamente por hipocrisia (vv. 11-21). O capítulo culmina em uma das declarações mais profundas do NT sobre a vida cristã: "Estou crucificado com Cristo; e vivo, não mais eu, mas Cristo vive em mim" (v. 20).</p>
<p>O "incidente de Antioquia" é um dos episódios mais fascinantes e perturbadores do NT: dois apóstolos — Paulo e Pedro — em conflito público sobre uma questão de comportamento que Paulo identifica como teologicamente fundamental. Pedro havia começado a comer com os gentios em Antioquia (algo que sua visão em At 10 havia libertado para fazer), mas quando chegaram "alguns da parte de Tiago" (os judaizantes de Jerusalém), Pedro se retirou e se separou dos gentios por medo dos circuncisos. Paulo viu neste comportamento não apenas hipocrisia pessoal, mas uma traição ao Evangelho da graça — e confrontou Pedro "na face" (v. 11).</p>""",
        "versiculos": [
            {
                "ref": "2:1-2 — A Segunda Visita a Jerusalém",
                "texto": "\"Depois, passados catorze anos, subi outra vez a Jerusalém com Barnabé, levando também comigo a Tito. E subi por revelação, e expus a eles o evangelho que prego entre os gentios, mas em particular aos que eram de reputação, para que não corresse ou não tivesse corrido em vão.\"",
                "analise": "Paulo descreve sua segunda visita a Jerusalém (provavelmente o Concílio de Jerusalém de At 15, ou uma visita anterior). Ele foi \"por revelação\" — não porque os apóstolos o convocaram, mas porque Deus o direcionou. A expressão \"expus a eles o evangelho\" (<em>anethemēn autois to euangelion</em>) não implica que Paulo precisava de aprovação — ele já pregava este Evangelho há 14 anos. Era uma consulta estratégica para garantir a unidade da missão, não uma submissão doutrinária. \"Para que não corresse em vão\" (<em>mē pōs eis kenon trechō</em>) — Paulo estava preocupado com a possibilidade de que a divisão entre sua missão gentílica e a missão judaica pudesse comprometer o Evangelho que pregava."
            },
            {
                "ref": "2:3-5 — Tito Não Foi Circuncidado",
                "texto": "\"Mas nem mesmo Tito, que estava comigo, sendo grego, foi obrigado a circuncidar-se; e isso por causa dos falsos irmãos introduzidos sorrateiramente, que se introduziram para espiar a nossa liberdade que temos em Cristo Jesus, para nos reduzirem à escravidão.\"",
                "analise": "O caso de Tito é o teste prático do Evangelho da graça. Tito era grego — gentio não circuncidado. Os \"falsos irmãos\" (<em>pseudadelphoi</em>) — os judaizantes — exigiam sua circuncisão como condição para ser plenamente aceito na comunidade cristã. Paulo recusou — \"nem por uma hora cedemos\" (<em>oude pros hōran eixamen tē hypotagē</em>) — porque a circuncisão de Tito teria implicado que a fé em Cristo não era suficiente para a salvação. A liberdade cristã (<em>eleutheria</em>) não é licença para o pecado (como Paulo esclarecerá em Gl 5:13), mas libertação da escravidão à Lei como sistema de justificação."
            },
            {
                "ref": "2:11-14 — O Incidente de Antioquia",
                "texto": "\"Mas, quando Pedro veio a Antioquia, resisti-lhe na face, porque era repreensível. Porque, antes de chegarem alguns da parte de Tiago, comia com os gentios; mas, depois que chegaram, retirou-se e separou-se, temendo os que eram da circuncisão.\"",
                "analise": "O confronto Paulo-Pedro em Antioquia é um dos episódios mais importantes para a compreensão da autoridade apostólica no NT. Paulo não era subordinado a Pedro — ele o confrontou publicamente quando Pedro agiu de forma contrária ao Evangelho. A hipocrisia de Pedro (<em>hypokrisis</em>) não era apenas pessoal — era teológica: ao se separar dos gentios, Pedro estava implicitamente afirmando que os gentios não eram plenamente membros do povo de Deus sem a circuncisão. \"Temendo os que eram da circuncisão\" (<em>phoboumenos tous ek peritomēs</em>) — o pecado de Pedro era o medo humano, não a convicção teológica. Até Barnabé foi arrastado pela hipocrisia (v. 13) — o que mostra o poder da pressão social mesmo sobre os mais firmes."
            },
            {
                "ref": "2:15-16 — A Tese da Justificação",
                "texto": "\"Nós, que somos judeus por natureza, e não pecadores dentre os gentios, sabendo que o homem não é justificado pelas obras da lei, mas pela fé em Jesus Cristo, também nós cremos em Jesus Cristo, para sermos justificados pela fé de Cristo, e não pelas obras da lei; pois pelas obras da lei nenhuma carne será justificada.\"",
                "analise": "Estes versículos contêm a tese central de Gálatas — e de toda a teologia paulina. A justificação (<em>dikaiōsis</em>) é o ato pelo qual Deus declara o pecador justo. Paulo afirma que esta justificação não vem \"pelas obras da Lei\" (<em>ex ergōn nomou</em>) mas \"pela fé em Jesus Cristo\" (<em>dia pisteōs Iēsou Christou</em>). A expressão grega <em>pistis Iēsou Christou</em> pode ser traduzida como \"fé em Jesus Cristo\" (genitivo objetivo — nossa fé em Cristo) ou \"fidelidade de Jesus Cristo\" (genitivo subjetivo — a fidelidade de Cristo em nossa favor). Muitos estudiosos contemporâneos preferem a segunda leitura: somos justificados pela fidelidade de Cristo — sua obediência perfeita ao Pai — recebida pela fé. A citação implícita do Sl 143:2 — \"pois pelas obras da lei nenhuma carne será justificada\" — mostra que esta não é uma inovação paulina, mas o ensino do próprio AT."
            },
            {
                "ref": "2:19-20 — Crucificado com Cristo",
                "texto": "\"Porque eu, pela lei, morri para a lei, para viver para Deus. Estou crucificado com Cristo; e vivo, não mais eu, mas Cristo vive em mim; e a vida que agora vivo na carne, vivo-a pela fé do Filho de Deus, o qual me amou e se entregou a si mesmo por mim.\"",
                "analise": "Gálatas 2:20 é um dos versículos mais profundos do NT — uma declaração de identidade cristã que vai além da justificação para a união mística com Cristo. \"Estou crucificado com Cristo\" (<em>Christō synestauōmai</em>) — o perfeito grego indica um estado presente resultante de uma ação passada: Paulo foi crucificado com Cristo (na cruz) e continua neste estado de co-crucificação. \"Não mais eu\" — o \"eu\" que vivia para si mesmo, que buscava justificação pelas obras, que perseguia a Igreja — este \"eu\" morreu. \"Cristo vive em mim\" (<em>zē en emoi Christos</em>) — não uma metáfora, mas uma realidade mística: o Cristo ressuscitado habita no crente pelo Espírito. \"O qual me amou e se entregou a si mesmo por mim\" (<em>agapēsantos me kai paradontos heauton hyper emou</em>) — Paulo personaliza o Evangelho: não apenas \"por nós\", mas \"por mim\". A morte de Cristo foi pessoal e individual — por cada pessoa específica."
            }
        ],
        "vocab": [
            {"termo": "δικαιόω", "transl": "dikaioō", "def": "Justificar, declarar justo. Termo forense: o juiz que declara o réu inocente. Em Paulo, Deus justifica o pecador — não porque o pecador seja inocente, mas porque Cristo assumiu sua culpa. A justificação é forense (declaração), não infusão de virtude."},
            {"termo": "ὑπόκρισις", "transl": "hypokrisis", "def": "Hipocrisia. Do grego para \"ator\" — alguém que usa uma máscara. A hipocrisia de Pedro em Antioquia era teologicamente perigosa: seu comportamento contradzia o Evangelho da graça que ele mesmo pregava."},
            {"termo": "ἐλευθερία", "transl": "eleutheria", "def": "Liberdade. A liberdade cristã em Gálatas é libertação da escravidão à Lei como sistema de justificação. Não é licença para o pecado (Gl 5:13), mas liberdade para servir pelo amor."},
            {"termo": "συσταυρόω", "transl": "systauroō", "def": "Ser crucificado junto com. O prefixo <em>syn</em> indica co-participação: o crente foi crucificado junto com Cristo. Esta co-crucificação é a base da nova identidade cristã — morte para o \"eu\" velho e vida em Cristo."}
        ],
        "teologia": """<p>Gálatas 2 apresenta a doutrina da justificação pela fé em sua forma mais clara e combativa. A justificação não é um processo gradual de tornar-se mais justo — é uma declaração forense de Deus que declara o pecador justo com base na obra de Cristo. Esta distinção entre justificação (declaração forense) e santificação (transformação moral) é fundamental para a teologia protestante e foi o coração da Reforma.</p>
<p>A teologia da união com Cristo em Gl 2:20 é igualmente importante. A vida cristã não é imitação de Cristo de fora — é Cristo vivendo de dentro. O crente não apenas segue os ensinamentos de Jesus como modelo moral; ele está unido a Cristo pelo Espírito, de modo que a vida de Cristo flui através dele. Esta união mística é o fundamento da ética cristã: vivemos como Cristo porque Cristo vive em nós.</p>""",
        "aplicacao": """<p>O incidente de Antioquia tem implicações permanentes para a vida da Igreja. Quando práticas eclesiásticas — mesmo as de líderes respeitados — contradizem o Evangelho da graça, elas devem ser confrontadas. A pressão social, o medo de desagradar grupos influentes, a acomodação cultural — estes são os "temores dos circuncisos" modernos que podem levar a Igreja a trair o Evangelho sem perceber.</p>
<p>A declaração de Gl 2:20 é o antídoto para o moralismo e o legalismo cristão. O cristão não vive para Deus por esforço próprio — Cristo vive nele pelo Espírito. A vida cristã não é "tente mais" mas "confie mais" — não é esforço para imitar Cristo de fora, mas rendição para que Cristo viva de dentro. Esta distinção transforma a experiência cristã de obrigação pesada para participação gozosa na vida divina.</p>"""
    },
    3: {
        "titulo": "Gálatas 3 — A Fé de Abraão e a Maldição da Lei",
        "ref": "Gálatas 3:1-29 · Paulo · c. 48-55 d.C.",
        "chave": "Não há judeu nem grego, não há servo nem livre, não há macho nem fêmea; porque todos vós sois um em Cristo Jesus. — Gálatas 3:28",
        "contexto": """<p>Gálatas 3 é o coração teológico da carta — Paulo apresenta sua argumentação bíblica mais densa contra o legalismo. Ele usa cinco argumentos distintos para provar que a justificação é pela fé, não pelas obras da Lei: (1) a experiência dos gálatas com o Espírito (vv. 1-5); (2) o exemplo de Abraão (vv. 6-9); (3) a maldição da Lei (vv. 10-14); (4) a prioridade da promessa sobre a Lei (vv. 15-18); (5) o propósito pedagógico da Lei (vv. 19-29). O capítulo culmina na declaração mais radical de igualdade do mundo antigo: "Não há judeu nem grego, não há servo nem livre, não há macho nem fêmea" (v. 28).</p>
<p>O argumento a partir de Abraão é particularmente poderoso porque os judaizantes apelavam a Abraão como fundamento da circuncisão. Paulo vira o argumento de cabeça para baixo: Abraão foi justificado pela fé (Gn 15:6) antes de ser circuncidado (Gn 17) — portanto a fé, não a circuncisão, é o princípio fundamental da relação com Deus. Os verdadeiros filhos de Abraão são os que têm a fé de Abraão, não os que têm a circuncisão de Abraão.</p>""",
        "versiculos": [
            {
                "ref": "3:1-3 — O Apelo à Experiência",
                "texto": "\"Ó gálatas insensatos! Quem vos fascinou a vós, perante cujos olhos Jesus Cristo foi evidentemente exposto como crucificado? Só isto quero saber de vós: Recebestes o Espírito pelas obras da lei, ou pela pregação da fé?\"",
                "analise": "Paulo abre com um apelo à experiência dos próprios gálatas — uma forma de argumentação retórica chamada <em>argumentum ad hominem</em> (no sentido positivo: apelo à experiência pessoal do interlocutor). \"Insensatos\" (<em>anoētoi</em>) — não estúpidos intelectualmente, mas espiritualmente cegos, sem discernimento. \"Quem vos fascinou\" (<em>tis hymas ebaskanen</em>) — o verbo <em>baskainō</em> significa literalmente \"lançar o mau-olhado\", enfeitiçar. Paulo está usando linguagem hiperbólica: os gálatas agiram como se estivessem sob um feitiço. A pergunta retórica é devastadora: eles receberam o Espírito (com todos os seus dons e transformações) pela pregação da fé — não pelas obras da Lei. Por que então tentariam completar pela Lei o que começou pelo Espírito?"
            },
            {
                "ref": "3:6-9 — O Exemplo de Abraão",
                "texto": "\"Assim como Abraão creu em Deus, e isso lhe foi imputado como justiça. Sabei, pois, que os que são da fé, esses são filhos de Abraão. E a Escritura, prevendo que Deus havia de justificar os gentios pela fé, pregou o evangelho de antemão a Abraão: Em ti serão benditas todas as nações.\"",
                "analise": "A citação de Gn 15:6 — \"Abraão creu em Deus, e isso lhe foi imputado como justiça\" — é a pedra angular do argumento paulino. A palavra \"imputado\" (<em>elogisthē</em>) é um termo contábil: algo foi creditado na conta de Abraão que não era originalmente seu. Abraão não tinha justiça própria — a justiça foi imputada a ele com base na fé. Os \"filhos de Abraão\" (<em>huioi Abraam</em>) não são definidos pela descendência biológica ou pela circuncisão, mas pela fé — o mesmo princípio pelo qual Abraão foi justificado. A citação de Gn 12:3 — \"Em ti serão benditas todas as nações\" — é interpretada por Paulo como o \"Evangelho pregado de antemão\" (<em>proeuēngelisato</em>) a Abraão: a bênção de Abraão sempre foi destinada a todas as nações, não apenas a Israel."
            },
            {
                "ref": "3:10-14 — A Maldição da Lei e a Redenção em Cristo",
                "texto": "\"Porque todos os que são das obras da lei estão debaixo da maldição; porque está escrito: Maldito todo aquele que não permanecer em todas as coisas que estão escritas no livro da lei, para fazê-las... Cristo nos resgatou da maldição da lei, sendo feito maldição por nós.\"",
                "analise": "Este é um dos argumentos mais audaciosos de Paulo. A Lei não justifica — ela amaldiçoa, porque exige obediência perfeita e ninguém a cumpre perfeitamente (citando Dt 27:26). O sistema de justificação pelas obras da Lei é, portanto, um sistema que produz maldição, não bênção. A solução de Deus é radical: Cristo \"sendo feito maldição por nós\" (<em>genomenos hyper hēmōn katara</em>) — ele assumiu a maldição que pertencia a nós. A citação de Dt 21:23 — \"Maldito todo aquele que for pendurado no madeiro\" — é aplicada à crucificação de Cristo: a cruz era, aos olhos da Lei, o sinal da maldição divina. Paulo afirma que Cristo voluntariamente se colocou sob esta maldição para nos resgatar dela. Este é o coração da teologia da substituição penal."
            },
            {
                "ref": "3:23-29 — A Lei como Pedagogo",
                "texto": "\"Mas, antes que viesse a fé, estávamos guardados debaixo da lei, encerrados para a fé que havia de ser revelada. Assim que a lei nos serviu de aio para nos conduzir a Cristo, para que pela fé fôssemos justificados.\"",
                "analise": "A metáfora do \"pedagogo\" (<em>paidagōgos</em>) é uma das mais iluminadoras de Paulo. No mundo greco-romano, o <em>paidagōgos</em> não era o professor, mas o escravo que acompanhava a criança à escola, guardava-a de perigos e a disciplinava. Era uma figura de autoridade temporária — sua função terminava quando a criança chegava à maturidade. Paulo usa esta imagem para descrever a função da Lei: ela era o pedagogo que guardava Israel até a chegada de Cristo. Com a vinda de Cristo, a era do pedagogo terminou — não porque a Lei seja má, mas porque seu propósito foi cumprido. O versículo 28 — \"Não há judeu nem grego, não há servo nem livre, não há macho nem fêmea\" — é a declaração mais radical de igualdade do mundo antigo. Em Cristo, todas as distinções que dividem a humanidade são transcendidas — não abolidas na vida social, mas irrelevantes para a salvação e para a identidade em Cristo."
            }
        ],
        "vocab": [
            {"termo": "κατάρα", "transl": "katara", "def": "Maldição. A Lei amaldiçoa quem não a cumpre perfeitamente. Cristo se tornou maldição por nós — assumindo a maldição que pertencia a nós — para nos libertar da maldição da Lei."},
            {"termo": "παιδαγωγός", "transl": "paidagōgos", "def": "Pedagogo, aio. No mundo greco-romano, o escravo que acompanhava a criança à escola. Paulo usa esta metáfora para a Lei: ela era o pedagogo temporário que guardava Israel até a chegada de Cristo."},
            {"termo": "λογίζομαι", "transl": "logizomai", "def": "Imputar, creditar, contar. Termo contábil: algo é creditado na conta de alguém. A justiça de Deus é imputada ao crente — creditada em sua conta com base na fé, não no mérito."},
            {"termo": "υἱοθεσία", "transl": "huiothesia", "def": "Adoção filial. Em Cristo, os crentes recebem o Espírito de adoção que os torna filhos de Deus — não servos, não escravos, mas filhos com todos os direitos de herdeiros."}
        ],
        "teologia": """<p>Gálatas 3 apresenta a teologia da Lei em sua relação com o Evangelho. Paulo não é antinomista — ele não rejeita a Lei como má. Mas ele é claro: a Lei nunca foi o meio de justificação. Seu propósito era diferente: revelar o pecado (Rm 3:20), guardar Israel até a chegada de Cristo, e servir como pedagogo que conduz a Cristo. Com a vinda de Cristo, a era da Lei como sistema de justificação terminou.</p>
<p>A declaração de Gl 3:28 é uma das mais revolucionárias do NT. No mundo do século I, as distinções étnicas (judeu/grego), sociais (escravo/livre) e de gênero (macho/fêmea) eram fundamentais para a identidade e o status. Paulo afirma que em Cristo todas estas distinções são transcendidas — não na vida social imediata, mas na identidade fundamental diante de Deus. Esta visão igualitária foi a semente que eventualmente transformou a cultura ocidental.</p>""",
        "aplicacao": """<p>O argumento de Paulo a partir de Abraão tem implicações permanentes para a compreensão da salvação. A fé — não a observância religiosa, não a pertença étnica, não o mérito moral — é o único canal pelo qual a justificação é recebida. Isto significa que o mais simples dos crentes e o mais erudito dos teólogos estão no mesmo nível diante de Deus: ambos justificados pela fé, não pela sabedoria ou pela virtude.</p>
<p>A visão de Gl 3:28 desafia toda forma de discriminação dentro da Igreja. Quando a comunidade cristã trata pessoas de forma diferente com base em etnia, status social ou gênero, ela contradiz o Evangelho que prega. A igualdade em Cristo não é apenas uma doutrina abstrata — é uma realidade que deve ser vivida concretamente na vida da comunidade.</p>"""
    },
    4: {
        "titulo": "Gálatas 4 — Filhos, Não Escravos",
        "ref": "Gálatas 4:1-31 · Paulo · c. 48-55 d.C.",
        "chave": "E porque sois filhos, Deus enviou aos vossos corações o Espírito de seu Filho, que clama: Aba, Pai. Assim que já não és servo, mas filho; e, se filho, também herdeiro de Deus por Cristo. — Gálatas 4:6-7",
        "contexto": """<p>Gálatas 4 aprofunda a metáfora da adoção filial introduzida no capítulo 3. Paulo usa duas imagens poderosas: (1) a do herdeiro menor que, embora dono de tudo, é tratado como escravo até atingir a maioridade (vv. 1-7); e (2) a alegoria de Agar e Sara, as duas mulheres de Abraão, que representam as duas alianças — a do Sinai (escravidão) e a de Jerusalém celestial (liberdade) (vv. 21-31). O capítulo inclui também um apelo pessoal e emocionante de Paulo aos gálatas (vv. 12-20), onde ele revela a vulnerabilidade de seu coração pastoral.</p>
<p>A expressão "Aba, Pai" (<em>Abba ho Patēr</em>) em Gl 4:6 é uma das mais íntimas do NT — <em>Abba</em> é a palavra aramaica que as crianças usavam para chamar o pai, equivalente ao nosso "papai". O fato de que o Espírito de Cristo clama esta palavra em nossos corações significa que a relação com Deus não é de servos com um senhor distante, mas de filhos com um Pai amoroso.</p>""",
        "versiculos": [
            {
                "ref": "4:1-7 — O Herdeiro Menor",
                "texto": "\"Digo, pois, que, enquanto o herdeiro é menor, em nada difere do servo, ainda que seja senhor de tudo... Assim também nós, quando éramos menores, estávamos em servidão debaixo dos rudimentos do mundo. Mas, quando veio a plenitude do tempo, Deus enviou seu Filho...\"",
                "analise": "A metáfora do herdeiro menor é juridicamente precisa: no direito romano, o filho menor (ainda sob tutores e curadores) não tinha acesso à herança, mesmo sendo seu proprietário legal. Paulo usa esta imagem para descrever a condição de Israel sob a Lei: herdeiros da promessa, mas ainda em estado de menoridade espiritual, sob a tutela da Lei. \"A plenitude do tempo\" (<em>to plērōma tou chronou</em>) — a expressão indica que a encarnação não foi um evento acidental, mas o cumprimento do tempo determinado por Deus. \"Nascido de mulher, nascido sob a lei\" (<em>genomenon ek gynaikos, genomenon hypo nomon</em>) — Cristo assumiu plenamente a condição humana (nascido de mulher) e a condição judaica (nascido sob a Lei) para resgatar os que estavam sob a Lei. O resultado é a adoção filial (<em>huiothesia</em>) — não apenas perdão, mas uma nova identidade: filhos de Deus."
            },
            {
                "ref": "4:6-7 — O Espírito de Adoção",
                "texto": "\"E porque sois filhos, Deus enviou aos vossos corações o Espírito de seu Filho, que clama: Aba, Pai. Assim que já não és servo, mas filho; e, se filho, também herdeiro de Deus por Cristo.\"",
                "analise": "\"Aba, Pai\" (<em>Abba ho Patēr</em>) é uma das expressões mais íntimas do NT. <em>Abba</em> é aramaico — a palavra que as crianças usavam para chamar o pai, com toda a intimidade e confiança que esta relação implica. O fato de que o Espírito \"clama\" (<em>krazon</em>) esta palavra em nossos corações indica que a oração cristã não é um esforço humano para alcançar Deus, mas o Espírito de Cristo orando através de nós. A sequência é trinitária: o Pai envia o Espírito do Filho para que os filhos possam clamar ao Pai. A conclusão — \"já não és servo, mas filho; e, se filho, também herdeiro\" — é a declaração de identidade mais transformadora do NT. A identidade cristã não é definida pelo desempenho moral ou pela observância religiosa, mas pela relação filial com Deus estabelecida em Cristo."
            },
            {
                "ref": "4:12-20 — O Apelo Pastoral de Paulo",
                "texto": "\"Irmãos, peço-vos que sejais como eu, porque eu também sou como vós. Nenhum agravo me fizestes... Filhinhos meus, por quem de novo sinto as dores de parto, até que Cristo seja formado em vós.\"",
                "analise": "Este é o trecho mais pessoal e emocionalmente intenso da carta. Paulo abandona temporariamente o argumento teológico para falar de coração para coração. \"Filhinhos meus\" (<em>tekna mou</em>) — a palavra grega é diminutiva e carinhosa, usada apenas aqui em todo o corpus paulino. \"As dores de parto\" (<em>ōdinō</em>) — Paulo usa a metáfora do parto para descrever sua angústia pastoral: ele sente como se estivesse dando à luz os gálatas de novo, porque eles estavam se afastando do Cristo que ele havia formado neles. \"Até que Cristo seja formado em vós\" (<em>mechris hou morphōthē Christos en hymin</em>) — o objetivo da formação espiritual não é a conformidade com regras, mas a formação de Cristo no interior do crente — uma transformação de dentro para fora."
            },
            {
                "ref": "4:21-31 — A Alegoria de Agar e Sara",
                "texto": "\"Dizei-me vós, os que quereis estar debaixo da lei: não ouvis a lei? Porque está escrito que Abraão teve dois filhos: um da escrava e outro da livre... O que é da escrava nasceu segundo a carne, mas o que é da livre nasceu pela promessa.\"",
                "analise": "A alegoria de Agar e Sara é a interpretação tipológica mais ousada de Paulo. Ele usa a narrativa histórica do Gênesis como alegoria (<em>allegoroumena</em> — Gl 4:24) para ilustrar a diferença entre as duas alianças. Agar (a escrava egípcia) representa o Monte Sinai e a aliança da Lei — que gera filhos para a escravidão. Sara (a mulher livre) representa a Jerusalém celestial e a aliança da promessa — que gera filhos para a liberdade. Ismael (filho de Agar, nascido \"segundo a carne\" — por esforço humano) representa os que buscam justificação pelas obras. Isaque (filho de Sara, nascido \"pela promessa\" — por intervenção divina) representa os que são justificados pela fé. A conclusão é direta: os cristãos são filhos de Sara, não de Agar — filhos da promessa, não da Lei."
            }
        ],
        "vocab": [
            {"termo": "Ἀββά", "transl": "Abba", "def": "Pai (aramaico). Palavra íntima que as crianças usavam para chamar o pai. O Espírito de Cristo clama esta palavra em nossos corações, revelando a intimidade da relação filial com Deus que a salvação estabelece."},
            {"termo": "υἱοθεσία", "transl": "huiothesia", "def": "Adoção filial. O ato pelo qual Deus nos torna seus filhos — não por natureza (como Cristo), mas por graça. A adoção implica todos os direitos de um filho legítimo, incluindo a herança."},
            {"termo": "μορφόω", "transl": "morphoō", "def": "Formar, moldar. Paulo usa este verbo para descrever o objetivo da formação espiritual: que Cristo seja formado no interior do crente. Não conformidade externa, mas transformação interna."},
            {"termo": "ἀλληγορέω", "transl": "allēgoreō", "def": "Alegorizar, interpretar alegoricamente. Paulo usa a narrativa histórica de Agar e Sara como alegoria das duas alianças. A interpretação alegórica não nega a historicidade, mas busca o significado espiritual mais profundo."}
        ],
        "teologia": """<p>Gálatas 4 apresenta a doutrina da adoção filial em sua forma mais rica. A salvação não é apenas perdão de pecados (justificação) ou transformação moral (santificação) — é uma mudança de status ontológico: de escravos para filhos, de estranhos para herdeiros. Esta mudança é operada pelo Espírito de Cristo que habita no crente e o capacita a clamar "Aba, Pai" com a mesma intimidade com que o próprio Jesus se relacionava com o Pai.</p>
<p>A alegoria de Agar e Sara revela o método hermenêutico de Paulo: ele lê o AT cristologicamente, buscando o significado espiritual mais profundo por trás dos eventos históricos. Isto não é uma imposição externa ao texto, mas uma leitura que o próprio Jesus autorizou: "Escrutinais as Escrituras, porque vós cuidais ter nelas a vida eterna; e são elas que testificam de mim" (Jo 5:39).</p>""",
        "aplicacao": """<p>A expressão "Aba, Pai" é um convite à oração de intimidade. Muitos cristãos oram com distância e formalidade — como servos que pedem favores a um senhor distante. Mas o Espírito de Cristo nos capacita a orar com a intimidade de filhos que confiam no amor do Pai. Esta intimidade não é irreverência — é a relação que Deus mesmo estabeleceu ao nos adotar como filhos.</p>
<p>O apelo pastoral de Paulo em Gl 4:19 — "filhinhos meus, por quem de novo sinto as dores de parto, até que Cristo seja formado em vós" — define o objetivo da formação espiritual. O ministério cristão não visa conformidade com regras ou crescimento numérico — visa a formação de Cristo no interior das pessoas. Este é o critério pelo qual todo ministério deve ser avaliado: está Cristo sendo formado nas pessoas?</p>"""
    },
    5: {
        "titulo": "Gálatas 5 — Liberdade em Cristo e os Frutos do Espírito",
        "ref": "Gálatas 5:1-26 · Paulo · c. 48-55 d.C.",
        "chave": "Mas o fruto do Espírito é: amor, gozo, paz, longanimidade, benignidade, bondade, fidelidade, mansidão, temperança. Contra estas coisas não há lei. — Gálatas 5:22-23",
        "contexto": """<p>Gálatas 5 é o capítulo da liberdade cristã — mas uma liberdade que não é licença para o pecado, e sim capacitação para o amor. Paulo começa com a declaração mais direta sobre a liberdade cristã: "Estai, pois, firmes na liberdade com que Cristo nos libertou, e não torneis a meter-vos no jugo da escravidão" (v. 1). Ele então apresenta a vida cristã como uma tensão dinâmica entre a "carne" (<em>sarx</em>) e o "Espírito" (<em>pneuma</em>) — não dualismo platônico entre corpo e alma, mas a tensão entre a velha natureza (orientada para si mesma) e a nova natureza (orientada para Deus e para o próximo).</p>
<p>O "fruto do Espírito" (vv. 22-23) é uma das listas mais conhecidas do NT. Paulo usa deliberadamente o singular "fruto" (<em>karpos</em>), não o plural "frutos" — indicando que estas qualidades são um conjunto orgânico, não virtudes isoladas que podem ser cultivadas separadamente. O fruto do Espírito é a vida de Cristo reproduzida no crente pelo Espírito Santo — não um esforço humano para ser mais amoroso ou mais paciente, mas a expressão natural de uma vida rendida ao Espírito.</p>""",
        "versiculos": [
            {
                "ref": "5:1 — A Declaração de Liberdade",
                "texto": "\"Estai, pois, firmes na liberdade com que Cristo nos libertou, e não torneis a meter-vos no jugo da escravidão.\"",
                "analise": "Este versículo é a conclusão prática de toda a argumentação teológica dos capítulos 1-4. A liberdade cristã (<em>eleutheria</em>) não é um estado passivo — ela exige uma postura ativa: \"estai firmes\" (<em>stēkete</em>). A liberdade pode ser perdida — não no sentido de perder a salvação, mas no sentido de viver como escravo quando se é livre. O \"jugo da escravidão\" (<em>zygō douleias</em>) é a metáfora da Lei como sistema de justificação. Paulo não está dizendo que a Lei é má — está dizendo que retornar à Lei como meio de justificação é retornar à escravidão, porque é tentar ganhar por esforço o que Cristo já deu de graça."
            },
            {
                "ref": "5:13-15 — Liberdade para Servir",
                "texto": "\"Porque vós, irmãos, fostes chamados à liberdade; não useis então da liberdade para dar ocasião à carne, mas servi-vos uns aos outros pelo amor. Porque toda a lei se cumpre numa só palavra, nesta: Amarás o teu próximo como a ti mesmo.\"",
                "analise": "Paulo antecipa a objeção óbvia: se somos livres da Lei, podemos pecar à vontade? Sua resposta é cristalina: a liberdade cristã não é licença para a carne (<em>aphormēn tē sarki</em>), mas capacitação para o serviço amoroso. A liberdade da Lei não leva ao antinomismo — leva ao cumprimento da Lei pelo amor. \"Servi-vos uns aos outros pelo amor\" (<em>dia tēs agapēs douleuete allēlois</em>) — a paradoxo paulino: somos livres para ser escravos uns dos outros pelo amor. Esta é a liberdade cristã em sua forma mais concreta. A citação de Lv 19:18 — \"Amarás o teu próximo como a ti mesmo\" — é o resumo de toda a Lei. Quem ama o próximo cumpre a Lei — não como meio de justificação, mas como expressão da nova vida em Cristo."
            },
            {
                "ref": "5:16-18 — Carne e Espírito",
                "texto": "\"Digo, pois: Andai em Espírito, e não cumprireis a concupiscência da carne. Porque a carne cobiça contra o Espírito, e o Espírito contra a carne; e estes opõem-se um ao outro, para que não façais o que quereis.\"",
                "analise": "A tensão entre \"carne\" (<em>sarx</em>) e \"Espírito\" (<em>pneuma</em>) em Paulo não é dualismo platônico (corpo mau vs. alma boa). A \"carne\" é a orientação do ser humano para si mesmo, independente de Deus — pode se manifestar tanto em vícios físicos quanto em orgulho espiritual. O \"Espírito\" é o Espírito Santo que habita no crente e o orienta para Deus e para o próximo. A solução para a tensão não é esforço moral, mas \"andar no Espírito\" (<em>pneumati peripateite</em>) — viver em dependência e rendição ao Espírito. Quem anda no Espírito não cumprirá a concupiscência da carne — não porque seja moralmente superior, mas porque o Espírito o orienta para o que é bom."
            },
            {
                "ref": "5:22-23 — O Fruto do Espírito",
                "texto": "\"Mas o fruto do Espírito é: amor, gozo, paz, longanimidade, benignidade, bondade, fidelidade, mansidão, temperança. Contra estas coisas não há lei.\"",
                "analise": "O \"fruto do Espírito\" (<em>ho karpos tou Pneumatos</em>) é apresentado no singular — um fruto com nove aspectos, não nove frutos separados. Esta lista é a descrição do caráter de Cristo reproduzido no crente pelo Espírito. Amor (<em>agapē</em>) é o primeiro e o fundamento de todos os outros. Gozo (<em>chara</em>) é alegria que não depende das circunstâncias. Paz (<em>eirēnē</em>) é o shalom bíblico — integridade e bem-estar em todas as dimensões. Longanimidade (<em>makrothymia</em>) é paciência com as pessoas. Benignidade (<em>chrēstotēs</em>) é gentileza ativa. Bondade (<em>agathōsynē</em>) é generosidade. Fidelidade (<em>pistis</em>) é confiabilidade. Mansidão (<em>praütēs</em>) é força sob controle. Temperança (<em>enkrateia</em>) é autodomínio. \"Contra estas coisas não há lei\" — a Lei não pode produzir estas qualidades, mas também não pode condená-las. Elas são a expressão da nova vida em Cristo que transcende a Lei."
            }
        ],
        "vocab": [
            {"termo": "ἐλευθερία", "transl": "eleutheria", "def": "Liberdade. A liberdade cristã não é ausência de restrições, mas libertação da escravidão à Lei como sistema de justificação e capacitação para o serviço amoroso. É liberdade para, não apenas liberdade de."},
            {"termo": "σάρξ", "transl": "sarx", "def": "Carne. Em Paulo, não o corpo físico, mas a orientação do ser humano para si mesmo, independente de Deus. A \"carne\" pode se manifestar em vícios físicos ou em orgulho espiritual — qualquer coisa que coloca o eu no centro."},
            {"termo": "καρπός", "transl": "karpos", "def": "Fruto. Paulo usa o singular — um fruto com múltiplos aspectos, não virtudes isoladas. O fruto do Espírito é orgânico: cresce naturalmente em quem anda no Espírito, não é produzido por esforço moral."},
            {"termo": "ἀγάπη", "transl": "agapē", "def": "Amor. O primeiro e mais fundamental fruto do Espírito. Amor que se doa sem esperar retorno, que age em favor do outro independentemente de mérito. É a essência do caráter de Deus e o resumo de toda a Lei."}
        ],
        "teologia": """<p>Gálatas 5 apresenta a ética cristã em sua forma mais distintiva. A vida moral cristã não é obediência a um código externo de regras — é a expressão natural de uma vida transformada pelo Espírito. A diferença entre o legalismo e a ética cristã é a diferença entre um escravo que obedece por medo e um filho que age por amor. O fruto do Espírito não é produzido pelo esforço humano — é o resultado orgânico de uma vida rendida ao Espírito.</p>
<p>A tensão entre carne e Espírito em Gl 5:16-18 é uma das descrições mais realistas da vida cristã no NT. Paulo não promete que a conversão elimina a tensão — ele descreve a tensão como a realidade normal da vida cristã. O crente não é nem totalmente carnal (como antes da conversão) nem totalmente espiritual (como será na glorificação) — ele vive na tensão entre os dois, caminhando no Espírito dia a dia.</p>""",
        "aplicacao": """<p>O fruto do Espírito é o critério mais confiável para avaliar a maturidade espiritual — mais confiável do que dons espirituais, experiências místicas ou conhecimento teológico. Uma pessoa pode ter dons extraordinários e conhecimento profundo e ainda assim ser imatura espiritualmente. Mas amor, paz, paciência, bondade — estas qualidades são o sinal inequívoco da obra do Espírito em uma vida.</p>
<p>A liberdade cristã de Gl 5:13 — "servi-vos uns aos outros pelo amor" — é o antídoto para o individualismo moderno. A liberdade não existe para ser consumida em benefício próprio, mas para ser investida no serviço ao próximo. O cristão mais livre é o que mais livremente serve — porque serve não por obrigação, mas por amor.</p>"""
    },
    6: {
        "titulo": "Gálatas 6 — Restauração, Perseverança e a Nova Criação",
        "ref": "Gálatas 6:1-18 · Paulo · c. 48-55 d.C.",
        "chave": "Mas longe esteja de mim gloriar-me, senão na cruz de nosso Senhor Jesus Cristo, pela qual o mundo está crucificado para mim, e eu para o mundo. Porque em Cristo Jesus nem a circuncisão nem a incircuncisão têm valor algum, mas sim uma nova criação. — Gálatas 6:14-15",
        "contexto": """<p>Gálatas 6 é a conclusão prática da carta — Paulo traduz as verdades teológicas dos capítulos anteriores em instruções concretas para a vida comunitária. O capítulo aborda três temas: (1) a restauração dos que caem (vv. 1-5); (2) a lei da semeadura e da colheita (vv. 6-10); e (3) a conclusão autógrafa de Paulo, onde ele resume toda a carta em torno do tema central: a cruz de Cristo e a nova criação (vv. 11-18).</p>
<p>A conclusão de Gálatas é uma das mais pessoais e poderosas do corpus paulino. Paulo escreve com sua própria mão (v. 11 — "com que letras grandes vos escrevi de minha própria mão") — provavelmente porque ditava normalmente suas cartas a um secretário. A conclusão resume toda a carta: os judaizantes se gloriam na circuncisão para evitar a perseguição da cruz; Paulo se gloria apenas na cruz, pela qual o mundo está crucificado para ele. A "nova criação" (<em>kainē ktisis</em>) é o horizonte escatológico de toda a teologia de Gálatas — em Cristo, não apenas o indivíduo é transformado, mas uma nova ordem da criação começa.</p>""",
        "versiculos": [
            {
                "ref": "6:1-2 — Restauração e a Lei de Cristo",
                "texto": "\"Irmãos, se algum homem for surpreendido em alguma transgressão, vós, os que sois espirituais, restaurai o tal com espírito de mansidão; olhando por ti mesmo, para que não sejas também tentado. Levai os encargos uns dos outros, e assim cumprireis a lei de Cristo.\"",
                "analise": "A instrução sobre restauração (<em>katartizete</em> — o mesmo verbo usado para consertar redes de pesca em Mt 4:21) é uma das mais práticas do NT. \"Surpreendido em alguma transgressão\" (<em>prolēmphthē en tini paraptōmati</em>) — não alguém que peca deliberadamente e sem remorso, mas alguém que foi apanhado de surpresa pelo pecado. A restauração deve ser feita pelos \"espirituais\" (<em>hoi pneumatikoi</em>) — os que andam no Espírito (Gl 5:25) — com \"espírito de mansidão\" (<em>en pneumati praütētos</em>). A mansidão é o espírito oposto ao julgamento orgulhoso: quem restaura deve lembrar que também pode cair. \"Levai os encargos uns dos outros\" (<em>allēlōn ta barē bastazete</em>) — a lei de Cristo é o amor que carrega o peso do próximo. Esta é a Lei que Paulo defende em Gálatas — não a Lei mosaica como sistema de justificação, mas a lei do amor como expressão da vida em Cristo."
            },
            {
                "ref": "6:7-10 — A Lei da Semeadura",
                "texto": "\"Não erreis: Deus não se deixa escarnecer; porque tudo o que o homem semear, isso também ceifará. Porque o que semeia na sua carne, da carne ceifará corrupção; mas o que semeia no Espírito, do Espírito ceifará vida eterna.\"",
                "analise": "A lei da semeadura e da colheita é um princípio universal que Paulo aplica à vida espiritual. \"Deus não se deixa escarnecer\" (<em>ho Theos ou myktērizetai</em>) — literalmente, \"Deus não é ridicularizado\" ou \"não se deixa enganar\". A lei da semeadura é inviolável: o que se semeia, se colhe. Semear \"na carne\" (<em>eis tēn sarka</em>) — investir na velha natureza, nas concupiscências egoístas — produz corrupção (<em>phthoran</em>). Semear \"no Espírito\" (<em>eis to Pneuma</em>) — investir na vida espiritual, nas obras do amor — produz vida eterna (<em>zōēn aiōnion</em>). A exortação de v. 9 — \"não nos cansemos de fazer o bem, porque a seu tempo ceifaremos, se não desfalecermos\" — é um dos encorajamentos mais necessários para a vida cristã: a colheita pode demorar, mas é certa."
            },
            {
                "ref": "6:14-15 — A Cruz e a Nova Criação",
                "texto": "\"Mas longe esteja de mim gloriar-me, senão na cruz de nosso Senhor Jesus Cristo, pela qual o mundo está crucificado para mim, e eu para o mundo. Porque em Cristo Jesus nem a circuncisão nem a incircuncisão têm valor algum, mas sim uma nova criação.\"",
                "analise": "A conclusão de Gálatas é uma das declarações mais sublimes de Paulo. \"Longe esteja de mim gloriar-me\" (<em>emoi de mē genoito kauchasthai</em>) — a expressão grega é a mais forte possível para uma negação: \"que jamais aconteça!\" Os judaizantes se gloriavam na circuncisão — um sinal externo de pertença ao povo de Deus. Paulo se gloria apenas na cruz — o sinal mais vergonhoso do mundo romano, transformado em símbolo de salvação. \"O mundo está crucificado para mim, e eu para o mundo\" — a cruz não é apenas o meio da salvação; é o princípio que reorganiza toda a existência. O \"mundo\" (<em>kosmos</em>) — o sistema de valores que busca glória, poder e aprovação humana — está morto para Paulo, e Paulo para ele. \"Uma nova criação\" (<em>kainē ktisis</em>) — este é o horizonte escatológico de toda a teologia de Gálatas. Em Cristo, não apenas o indivíduo é justificado — uma nova ordem da criação começa, onde as velhas distinções (circuncisão/incircuncisão, judeu/grego) são irrelevantes."
            }
        ],
        "vocab": [
            {"termo": "καταρτίζω", "transl": "katartizō", "def": "Restaurar, consertar, equipar. Usado para consertar redes de pesca (Mt 4:21) e para restaurar ossos deslocados. A restauração do que caiu deve ser feita com a mesma precisão e cuidado de um cirurgião."},
            {"termo": "καινή κτίσις", "transl": "kainē ktisis", "def": "Nova criação. O horizonte escatológico da teologia paulina: em Cristo, não apenas o indivíduo é transformado, mas uma nova ordem da criação começa. A nova criação é tanto presente (já inaugurada em Cristo) quanto futura (ainda a ser completada na parousia)."},
            {"termo": "σταυρός", "transl": "stauros", "def": "Cruz. O símbolo mais vergonhoso do mundo romano — instrumento de execução de criminosos e escravos. Paulo transforma a cruz no único motivo de glória cristã: nela, Cristo assumiu a maldição humana e inaugurou a nova criação."},
            {"termo": "σπείρω / θερίζω", "transl": "speirō / therizō", "def": "Semear / Colher. A lei da semeadura e da colheita é inviolável: o que se investe (na carne ou no Espírito) determina o que se recebe (corrupção ou vida eterna). Esta lei não é punição, mas a estrutura moral da realidade criada por Deus."}
        ],
        "teologia": """<p>Gálatas 6 apresenta a ética cristã como consequência orgânica da teologia da graça. A justificação pela fé não produz passividade moral — produz responsabilidade amorosa. Quem foi libertado da escravidão da Lei para a liberdade do Espírito usa esta liberdade para servir, restaurar, carregar encargos e semear no Espírito. A graça não elimina a responsabilidade — ela a transforma: de obrigação para amor, de medo para gratidão.</p>
<p>A "nova criação" de Gl 6:15 é o horizonte mais amplo da teologia paulina. A salvação não é apenas a salvação de almas individuais para o céu — é a inauguração de uma nova ordem da criação. Em Cristo, o novo Adão, a criação começa de novo. Esta visão cósmica da salvação é o antídoto para o individualismo espiritual que reduz o Evangelho a uma transação privada entre Deus e o indivíduo.</p>""",
        "aplicacao": """<p>A instrução sobre restauração em Gl 6:1 é um dos textos mais necessários para a Igreja contemporânea. Muitas comunidades cristãs oscilam entre dois extremos: o laxismo que não confronta o pecado e o rigorismo que condena sem restaurar. Paulo propõe um terceiro caminho: restauração com mansidão, carregando o peso do irmão que caiu, lembrando que todos somos vulneráveis à tentação.</p>
<p>A lei da semeadura de Gl 6:7-9 é um princípio de investimento espiritual. Cada decisão de semear no Espírito — cada ato de amor, cada hora de oração, cada escolha de honestidade — é um investimento com retorno garantido, mesmo que a colheita demore. "Não nos cansemos de fazer o bem, porque a seu tempo ceifaremos, se não desfalecermos" — este versículo é o antídoto para o desânimo espiritual.</p>"""
    }
}


def gerar_html(cap_num, dados):
    prev = f"/07-novo-testamento/{LIVRO_KEY}/capitulos/capitulo-{cap_num-1:02d}.html" if cap_num > 1 else f"/07-novo-testamento/{LIVRO_KEY}/index.html"
    prev_label = f"← {LIVRO} {cap_num-1}" if cap_num > 1 else f"← Índice de {LIVRO}"
    nxt = f"/07-novo-testamento/{LIVRO_KEY}/capitulos/capitulo-{cap_num+1:02d}.html" if cap_num < TOTAL else f"/07-novo-testamento/{LIVRO_KEY}/index.html"
    nxt_label = f"{LIVRO} {cap_num+1} →" if cap_num < TOTAL else f"Índice de {LIVRO} →"

    versiculos_html = ""
    for v in dados["versiculos"]:
        versiculos_html += f"""
      <div class="versiculo-bloco">
        <div class="ref-v">{v['ref']}</div>
        <div class="texto-v">{v['texto']}</div>
        <div class="analise-v">{v['analise']}</div>
      </div>"""

    vocab_html = ""
    for v in dados["vocab"]:
        vocab_html += f"""
        <div class="vocab-card">
          <div class="termo">{v['termo']}</div>
          <div class="transl">{v['transl']}</div>
          <div class="def">{v['def']}</div>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{dados['titulo']} | 365 de Graça & Adoração</title>
  <link rel="icon" href="/favicon.ico">
  <style>{CSS}</style>
</head>
<body>
  <div class="topbar"><div class="inner">
    <a href="/07-novo-testamento/{LIVRO_KEY}/index.html">← {LIVRO}</a>
    <a href="/07-novo-testamento/index.html">Novo Testamento</a>
  </div></div>
  <div class="hero">
    <span class="tag">📜 {LIVRO} {cap_num} · Epístolas Paulinas</span>
    <h1>{dados['titulo']}</h1>
    <div class="ref">{dados['ref']}</div>
    <blockquote>{dados['chave']}</blockquote>
  </div>
  <div class="wrap">
    <div class="section-block">
      <h2>📜 Contexto Histórico e Literário</h2>
      {dados['contexto']}
    </div>
    <div class="section-block">
      <h2>🔍 Análise Versículo por Versículo</h2>
      {versiculos_html}
    </div>
    <div class="section-block">
      <h2>📚 Vocabulário Grego Essencial</h2>
      <div class="vocab-grid">{vocab_html}</div>
    </div>
    <div class="section-block">
      <h2>🏛️ Teologia Sistemática</h2>
      {dados['teologia']}
    </div>
    <div class="section-block">
      <h2>✨ Aplicação Contemporânea</h2>
      {dados['aplicacao']}
    </div>
    <div class="nav-cap">
      <a href="{prev}">{prev_label}</a>
      <a href="/07-novo-testamento/{LIVRO_KEY}/index.html">📋 Índice</a>
      <a href="{nxt}">{nxt_label}</a>
    </div>
  </div>
</body>
</html>"""


def main():
    base = f"/home/ubuntu/365-de-graca-e-adoracao/07-novo-testamento/{LIVRO_KEY}/capitulos"
    os.makedirs(base, exist_ok=True)
    for cap_num, dados in CAPITULOS.items():
        path = os.path.join(base, f"capitulo-{cap_num:02d}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(gerar_html(cap_num, dados))
        print(f"✅ {LIVRO} {cap_num}: {path}")
    print(f"\n🎉 {LIVRO} completo!")


if __name__ == "__main__":
    main()
