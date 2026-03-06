#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera os capítulos 2-6 de Efésios com análise versículo por versículo aprofundada.
"""

import os

COLOR = "#22d3ee"
HERO_BG = "#001a1f"
TAG_BG = "rgba(34,211,238,0.1)"
TAG_BORDER = "rgba(34,211,238,0.25)"
TAG_HOVER = "rgba(34,211,238,0.2)"
LIVRO = "Efésios"
LIVRO_KEY = "efesios"
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
        "titulo": "Efésios 2 — Mortos e Vivificados em Cristo",
        "ref": "Efésios 2:1-22 · Paulo · c. 60-62 d.C. · Roma",
        "chave": "Porque pela graça sois salvos, por meio da fé; e isso não vem de vós; é dom de Deus. Não vem das obras, para que ninguém se glorie. — Efésios 2:8-9",
        "contexto": """<p>Efésios 2 é um dos capítulos mais importantes do NT para a compreensão da salvação. Ele tem duas partes distintas mas complementares: (1) a salvação individual — de mortos em delitos e pecados para vivificados em Cristo (vv. 1-10); e (2) a reconciliação comunitária — judeus e gentios unidos em um só corpo em Cristo (vv. 11-22). A primeira parte culmina nos versículos 8-9, a declaração mais clara do NT sobre a graça: "Porque pela graça sois salvos, por meio da fé; e isso não vem de vós; é dom de Deus." A segunda parte culmina na visão da Igreja como "templo santo no Senhor" e "habitação de Deus no Espírito" (vv. 21-22).</p>
<p>O contraste entre o "antes" e o "agora" estrutura todo o capítulo. "Antes" (vv. 1-3, 11-12): mortos em pecados, filhos da desobediência, filhos da ira, sem Cristo, sem esperança, sem Deus. "Agora" (vv. 4-10, 13-22): vivificados, ressuscitados, assentados nos lugares celestiais, criados para boas obras, aproximados pelo sangue de Cristo, concidadãos dos santos, habitação de Deus. Este contraste radical é o Evangelho em sua forma mais concreta.</p>""",
        "versiculos": [
            {
                "ref": "2:1-3 — Mortos em Delitos e Pecados",
                "texto": "\"E vos vivificou, estando vós mortos nos vossos delitos e pecados, nos quais andastes outrora segundo o curso deste século, segundo o príncipe da potestade do ar, do espírito que agora opera nos filhos da desobediência.\"",
                "analise": "A descrição da condição humana antes da salvação é devastadora em sua precisão. \"Mortos\" (<em>nekrous</em>) — não doentes, não fracos, não confusos, mas mortos. A morte espiritual é a incapacidade total de responder a Deus por iniciativa própria. \"Delitos\" (<em>paraptōmasin</em>) — quedas, desvios do caminho certo. \"Pecados\" (<em>hamartiais</em>) — erros, falhas em atingir o alvo. O ser humano morto em pecados opera em três esferas de influência: (1) \"o curso deste século\" (<em>aiōna tou kosmou toutou</em>) — a cultura e os valores do mundo presente; (2) \"o príncipe da potestade do ar\" (<em>archonta tēs exousias tou aeros</em>) — Satanás, que exerce influência sobre o mundo presente; (3) \"os desejos da nossa carne\" (<em>thelēmata tēs sarkos</em>) — a orientação interna para o egoísmo. A condição humana sem Cristo é de escravidão tripla: ao mundo, ao diabo e à carne."
            },
            {
                "ref": "2:4-7 — Mas Deus...",
                "texto": "\"Mas Deus, que é rico em misericórdia, pelo seu muito amor com que nos amou, e estando nós mortos em delitos, nos vivificou juntamente com Cristo; pela graça sois salvos. E nos ressuscitou juntamente, e nos fez assentar nos lugares celestiais em Cristo Jesus.\"",
                "analise": "\"Mas Deus\" (<em>ho de Theos</em>) — estas duas palavras são as mais importantes do capítulo. Elas marcam a virada radical: a condição humana era desesperadora, mas Deus interveio. A motivação da salvação é dupla: \"rico em misericórdia\" (<em>plousios ōn en eleei</em>) e \"pelo seu muito amor\" (<em>dia tēn pollēn agapēn autou</em>). A salvação não foi motivada por nada em nós — foi motivada pela natureza de Deus. \"Nos vivificou juntamente com Cristo\" (<em>synezōopoiēsen tō Christō</em>) — o prefixo <em>syn</em> (\"junto com\") aparece três vezes nesta seção: vivificados com Cristo (v. 5), ressuscitados com Cristo (v. 6), assentados com Cristo (v. 6). A salvação é participação na experiência de Cristo — sua morte, ressurreição e exaltação tornam-se nossa morte, ressurreição e exaltação. \"Nos fez assentar nos lugares celestiais\" — os crentes já estão posicionados nos lugares celestiais em Cristo, mesmo vivendo na terra. Esta é a realidade presente da salvação, não apenas uma esperança futura."
            },
            {
                "ref": "2:8-10 — Graça, Fé e Boas Obras",
                "texto": "\"Porque pela graça sois salvos, por meio da fé; e isso não vem de vós; é dom de Deus. Não vem das obras, para que ninguém se glorie. Porque somos feitura sua, criados em Cristo Jesus para as boas obras, as quais Deus preparou para que andássemos nelas.\"",
                "analise": "Efésios 2:8-9 é a declaração mais clara do NT sobre a graça. Cada elemento é preciso: \"pela graça\" (<em>tē chariti</em>) — o meio da salvação é a graça, não o mérito. \"Por meio da fé\" (<em>dia pisteōs</em>) — o canal pelo qual a graça é recebida é a fé. \"Não vem de vós\" (<em>ouk ex hymōn</em>) — nem a graça nem a fé são de origem humana. \"É dom de Deus\" (<em>Theou to dōron</em>) — a salvação em sua totalidade é dom divino. \"Não vem das obras\" (<em>ouk ex ergōn</em>) — as obras não são o meio da salvação. \"Para que ninguém se glorie\" (<em>hina mē tis kauchēsētai</em>) — o propósito da graça é eliminar o orgulho humano. Mas o versículo 10 é igualmente importante: \"somos feitura sua\" (<em>poiēma</em> — obra de arte, poema) \"criados para as boas obras\". A graça não elimina as obras — ela as fundamenta corretamente. As obras não são o meio da salvação, mas o propósito da salvação."
            },
            {
                "ref": "2:11-16 — A Reconciliação de Judeus e Gentios",
                "texto": "\"Porque ele é a nossa paz, que de ambos fez um, e derrubou a parede de separação que estava no meio, tendo abolido na sua carne a inimizade... para criar em si mesmo, dos dois, um novo homem, fazendo a paz.\"",
                "analise": "A segunda parte de Efésios 2 aplica a salvação à dimensão comunitária. O \"muro de separação\" (<em>to mesotoichon tou phragmou</em>) é provavelmente uma referência ao muro no Templo de Jerusalém que separava o pátio dos gentios do pátio de Israel — ultrapassar este muro era punível com a morte. Paulo afirma que Cristo derrubou este muro pela cruz. \"Um novo homem\" (<em>hena kainon anthrōpon</em>) — Cristo não fez dos gentios judeus, nem dos judeus gentios; ele criou uma terceira entidade — o \"novo homem\" que é a Igreja. Esta é uma das declarações mais revolucionárias do NT: a Igreja não é uma seita judaica nem uma religião gentílica — é uma nova humanidade em Cristo. \"Ele é a nossa paz\" (<em>autos gar estin hē eirēnē hēmōn</em>) — Cristo não apenas traz a paz; ele é a paz. A reconciliação entre judeus e gentios é inseparável da reconciliação com Deus."
            },
            {
                "ref": "2:19-22 — O Templo do Espírito",
                "texto": "\"Assim, pois, já não sois estrangeiros e forasteiros, mas concidadãos dos santos e da família de Deus, edificados sobre o fundamento dos apóstolos e dos profetas, sendo o principal fundamento o próprio Jesus Cristo, no qual todo o edifício, bem ajustado, cresce para ser um templo santo no Senhor.\"",
                "analise": "A metáfora do templo é a conclusão da seção sobre a reconciliação. Paulo usa três metáforas para descrever a Igreja: (1) cidade — \"concidadãos dos santos\" (<em>sympolitai tōn hagiōn</em>); (2) família — \"da família de Deus\" (<em>oikeioi tou Theou</em>); (3) templo — \"templo santo no Senhor\" (<em>naon hagion en Kyriō</em>). A metáfora do templo é particularmente poderosa no contexto de Efésios: Éfeso tinha o templo de Ártemis, uma das sete maravilhas do mundo. Paulo afirma que a Igreja — uma comunidade de judeus e gentios reconciliados em Cristo — é o verdadeiro templo de Deus, a habitação do Espírito Santo. O fundamento é duplo: \"apóstolos e profetas\" (a revelação apostólica e profética) com Cristo como \"pedra angular\" (<em>akrogōniaios</em>) — a pedra que determina o alinhamento de todo o edifício."
            }
        ],
        "vocab": [
            {"termo": "νεκρός", "transl": "nekros", "def": "Morto. A condição humana sem Cristo é morte espiritual — não fraqueza ou doença, mas morte. O morto não pode se curar a si mesmo; precisa de vivificação divina."},
            {"termo": "χάρις", "transl": "charis", "def": "Graça. O meio da salvação — o favor imerecido de Deus. Em Ef 2:8-9, Paulo afirma que a salvação é inteiramente dom de Deus, não mérito humano."},
            {"termo": "ποίημα", "transl": "poiēma", "def": "Obra de arte, poema, criação. Os crentes são a 'obra de arte' de Deus — criados em Cristo Jesus para as boas obras. A palavra sugere que cada crente é uma criação única e intencional de Deus."},
            {"termo": "εἰρήνη", "transl": "eirēnē", "def": "Paz. Do hebraico shalom — integridade, bem-estar, harmonia em todas as dimensões. Cristo é a nossa paz — ele não apenas traz a paz, mas é a paz. A reconciliação com Deus e com o próximo são inseparáveis."}
        ],
        "teologia": """<p>Efésios 2 apresenta a salvação em suas duas dimensões inseparáveis: vertical (reconciliação com Deus) e horizontal (reconciliação entre os seres humanos). A teologia da graça de Ef 2:8-9 é o fundamento; a eclesiologia de Ef 2:11-22 é a consequência. Quem é salvo pela graça é incorporado em uma comunidade onde as divisões humanas são transcendidas.</p>
<p>A doutrina da "morte espiritual" em Ef 2:1-3 é fundamental para a compreensão da graça. Se o ser humano está morto em pecados, ele não pode contribuir para sua própria salvação — nem mesmo a fé é uma contribuição humana, mas um dom de Deus (Ef 2:8). Esta é a base do que os teólogos chamam de "graça irresistível" ou "graça eficaz": Deus não apenas oferece a salvação, mas a realiza naqueles que ele escolheu.</p>""",
        "aplicacao": """<p>A declaração "mas Deus" de Ef 2:4 é o ponto de virada mais importante de qualquer vida. Quando a situação parece sem esperança — mortos em pecados, escravos do mundo e da carne — "mas Deus" intervém. Esta é a estrutura do Evangelho: diagnóstico honesto da condição humana, seguido pela intervenção soberana e misericordiosa de Deus.</p>
<p>A visão da Igreja como "novo homem" em Ef 2:15 desafia toda forma de segregação eclesiástica. Quando igrejas são homogêneas — apenas de uma etnia, classe social ou cultura — elas contradizem a visão de Paulo. A Igreja que reflete o "novo homem" de Efésios 2 é aquela onde as divisões humanas são visíveis mas transcendidas pela unidade em Cristo.</p>"""
    },
    3: {
        "titulo": "Efésios 3 — O Mistério de Cristo e a Oração pela Plenitude",
        "ref": "Efésios 3:1-21 · Paulo · c. 60-62 d.C. · Roma",
        "chave": "Para que Cristo habite pela fé nos vossos corações; a fim de que, arraigados e fundados em amor, possais compreender com todos os santos qual seja a largura, e o comprimento, e a altura, e a profundidade. — Efésios 3:17-18",
        "contexto": """<p>Efésios 3 tem duas partes: (1) a revelação do "mistério de Cristo" — o plano eterno de Deus de incluir os gentios como co-herdeiros com Israel (vv. 1-13); e (2) a segunda grande oração de Paulo pela Igreja (vv. 14-21), que culmina na doxologia mais sublime do corpus paulino (vv. 20-21). O capítulo é uma janela para o coração de Paulo como apóstolo dos gentios — ele vê sua missão não como carreira, mas como participação no mistério eterno de Deus.</p>
<p>O "mistério" (<em>mystērion</em>) de Cristo que Paulo descreve não é algo obscuro ou esotérico — é o plano eterno de Deus, antes oculto, agora revelado: que os gentios são "co-herdeiros, co-membros do corpo e co-participantes da promessa em Cristo Jesus" (v. 6). Este plano não é uma improvisação divina — estava "escondido desde os séculos em Deus" (v. 9) e agora é revelado através da Igreja, para que "os principados e potestades nos lugares celestiais" conheçam "a multiforme sabedoria de Deus" (v. 10).</p>""",
        "versiculos": [
            {
                "ref": "3:1-7 — O Mistério Revelado",
                "texto": "\"Por esta causa eu, Paulo, prisioneiro de Cristo Jesus por vós, os gentios... como por revelação me foi dado a conhecer o mistério... que os gentios são co-herdeiros, e co-membros do mesmo corpo, e co-participantes da promessa em Cristo Jesus pelo evangelho.\"",
                "analise": "Paulo se descreve como \"prisioneiro de Cristo Jesus\" (<em>desmios Christou Iēsou</em>) — não prisioneiro de Roma, mas de Cristo. Sua prisão não é acidente histórico, mas parte do plano de Deus. O \"mistério\" (<em>mystērion</em>) que Paulo recebeu por revelação é descrito com três compostos com o prefixo <em>syn</em> (\"co-\"): co-herdeiros (<em>synklēronoma</em>), co-membros do mesmo corpo (<em>syssōma</em>), co-participantes da promessa (<em>symmetocha</em>). Estes três termos descrevem a plena igualdade dos gentios com Israel na herança da salvação — não como cidadãos de segunda classe, mas como iguais em tudo. Este era o mistério que estava \"escondido nos séculos\" (v. 9) — não que os gentios seriam abençoados através de Israel (isso o AT já prometia), mas que seriam incorporados em igualdade plena no mesmo corpo."
            },
            {
                "ref": "3:10-12 — A Igreja e os Poderes Celestiais",
                "texto": "\"Para que agora, pela Igreja, a multiforme sabedoria de Deus seja conhecida dos principados e potestades nos lugares celestiais, segundo o eterno propósito que fez em Cristo Jesus nosso Senhor.\"",
                "analise": "Este versículo contém uma das afirmações mais ousadas sobre a Igreja em todo o NT. A Igreja não existe apenas para si mesma — ela é o instrumento pelo qual Deus revela sua sabedoria aos poderes celestiais. \"A multiforme sabedoria de Deus\" (<em>hē polypoikilos sophia tou Theou</em>) — o adjetivo <em>polypoikilos</em> é hapax legomenon (aparece apenas aqui no NT) e significa \"multifacetada\", \"de muitas cores\", \"variada\". A sabedoria de Deus revelada na Igreja é tão rica e variada que nem os anjos a compreendem completamente — eles aprendem observando a Igreja. \"O eterno propósito\" (<em>prothesis tōn aiōnōn</em>) — a Igreja não é um plano B de Deus após a rejeição de Israel; é o cumprimento do propósito eterno que Deus tinha antes da criação."
            },
            {
                "ref": "3:14-19 — A Segunda Oração de Paulo",
                "texto": "\"Por esta causa me ponho de joelhos perante o Pai de nosso Senhor Jesus Cristo... para que vos dê, segundo as riquezas da sua glória, o ser corroborados com poder pelo seu Espírito no homem interior; para que Cristo habite pela fé nos vossos corações.\"",
                "analise": "A segunda oração de Paulo em Efésios (a primeira está em 1:15-23) é uma das mais belas do NT. \"Me ponho de joelhos\" (<em>kamptō ta gonata mou</em>) — a postura de oração judaica normal era em pé; ajoelhar-se indicava urgência e intensidade especial. Paulo ora por quatro coisas progressivas: (1) ser corroborado com poder no homem interior pelo Espírito; (2) que Cristo habite pela fé nos corações; (3) que sejam arraigados e fundados em amor; (4) que compreendam as dimensões do amor de Cristo. A metáfora das dimensões — \"largura, comprimento, altura e profundidade\" — é espacial: o amor de Cristo é tão vasto que não pode ser contido em nenhuma dimensão. A conclusão — \"ser cheios de toda a plenitude de Deus\" (<em>plērōthēte eis pan to plērōma tou Theou</em>) — é a mais ousada petição de oração do NT: ser preenchido com a própria plenitude divina."
            },
            {
                "ref": "3:20-21 — A Doxologia",
                "texto": "\"Ora, àquele que é poderoso para fazer tudo muito mais abundantemente além do que pedimos ou pensamos, segundo o poder que em nós opera, a ele seja glória na Igreja e em Cristo Jesus, por todas as gerações, para todo o sempre. Amém.\"",
                "analise": "A doxologia de Ef 3:20-21 é a mais sublime do corpus paulino. Ela tem três camadas de superação: (1) \"tudo\" — Deus pode fazer tudo; (2) \"muito mais abundantemente\" (<em>hyperekperissou</em> — um superlativo superlativo: \"imensamente mais do que\"); (3) \"além do que pedimos ou pensamos\" — os limites da oração e da imaginação humana são transcendidos. O fundamento desta capacidade divina não é abstrato — é \"o poder que em nós opera\" (<em>tēn dynamin tēn energoumenēn en hēmin</em>): o mesmo poder que ressuscitou Cristo (Ef 1:19-20) opera dentro dos crentes. A glória é dada \"na Igreja e em Cristo Jesus\" — a Igreja é o palco onde a glória de Deus é manifestada no mundo."
            }
        ],
        "vocab": [
            {"termo": "μυστήριον", "transl": "mystērion", "def": "Mistério. Em Paulo, não algo obscuro, mas algo antes oculto e agora revelado: a inclusão dos gentios como co-herdeiros com Israel na salvação. Este mistério estava escondido em Deus desde os séculos."},
            {"termo": "πολυποίκιλος", "transl": "polypoikilos", "def": "Multifacetada, de muitas cores, variada. Hapax legomenon (aparece apenas em Ef 3:10 no NT). Descreve a sabedoria de Deus revelada na Igreja — tão rica e variada que nem os anjos a compreendem completamente."},
            {"termo": "πλήρωμα", "transl": "plērōma", "def": "Plenitude, completude. Paulo ora para que os efésios sejam 'cheios de toda a plenitude de Deus' — a mais ousada petição de oração do NT. A plenitude de Deus habitando nos crentes é o objetivo final da salvação."},
            {"termo": "ὑπερεκπερισσοῦ", "transl": "hyperekperissou", "def": "Imensamente mais do que, superabundantemente. Um superlativo superlativo — Paulo empilha prefixos intensificadores para descrever a capacidade de Deus de superar qualquer pedido ou imaginação humana."}
        ],
        "teologia": """<p>Efésios 3 apresenta a eclesiologia em sua dimensão mais cósmica. A Igreja não é apenas uma organização humana ou uma comunidade de crentes — é o instrumento pelo qual Deus revela sua sabedoria multifacetada aos poderes celestiais. Esta visão da Igreja como agente cósmico da revelação divina é uma das contribuições mais únicas de Efésios ao NT.</p>
<p>A oração de Paulo em Ef 3:14-21 revela a hierarquia de valores do apóstolo. Ele não ora por libertação da prisão, por saúde, por sucesso missionário — ora pela plenitude espiritual da Igreja. O objetivo supremo da vida cristã não é conforto ou prosperidade, mas ser "cheio de toda a plenitude de Deus" — a habitação do próprio Deus no interior do crente.</p>""",
        "aplicacao": """<p>A visão da Igreja como revelação da sabedoria de Deus aos poderes celestiais (Ef 3:10) é um antídoto para o pessimismo eclesiástico. Quando a Igreja parece fraca, dividida e irrelevante, é fácil desanimar. Mas Paulo afirma que a Igreja — com todas as suas imperfeições — é o instrumento escolhido por Deus para revelar sua sabedoria ao cosmos. Isto não é motivo de orgulho, mas de responsabilidade e humildade.</p>
<p>A doxologia de Ef 3:20-21 é o fundamento da oração audaciosa. "Aquele que é poderoso para fazer tudo muito mais abundantemente além do que pedimos ou pensamos" — esta é a base para pedir grandes coisas a Deus. A limitação não está na capacidade de Deus, mas na estreiteza de nossa imaginação e fé. Paulo nos convida a ampliar nossa visão do que Deus pode fazer.</p>"""
    },
    4: {
        "titulo": "Efésios 4 — A Unidade do Corpo e a Maturidade em Cristo",
        "ref": "Efésios 4:1-32 · Paulo · c. 60-62 d.C. · Roma",
        "chave": "Antes, seguindo a verdade em amor, cresçamos em tudo naquele que é a cabeça, Cristo, de quem todo o corpo, bem ajustado e ligado pelo auxílio de todas as juntas, segundo a justa atividade de cada parte, faz o aumento do corpo para sua edificação em amor. — Efésios 4:15-16",
        "contexto": """<p>Efésios 4 marca a virada da carta: dos capítulos 1-3 (teologia) para os capítulos 4-6 (ética). A transição é marcada pelo "portanto" (<em>oun</em>) do versículo 1 — a ética cristã é sempre consequência da teologia, não condição para ela. O capítulo 4 tem três seções: (1) o apelo à unidade (vv. 1-6); (2) a diversidade dos dons para a edificação do corpo (vv. 7-16); e (3) o contraste entre a velha vida e a nova vida em Cristo (vv. 17-32).</p>
<p>O apelo à unidade em Ef 4:1-6 é fundamentado em sete "uns": um corpo, um Espírito, uma esperança, um Senhor, uma fé, um batismo, um Deus e Pai. Esta lista é o "credo da unidade" de Paulo — a unidade da Igreja não é uma conquista humana, mas um dado teológico que deve ser preservado e manifestado. A diversidade dos dons (vv. 7-16) não contradiz a unidade — ela a enriquece: é a diversidade dos membros que permite ao corpo funcionar como um todo.</p>""",
        "versiculos": [
            {
                "ref": "4:1-3 — O Apelo à Unidade",
                "texto": "\"Rogo-vos, pois, eu, o prisioneiro do Senhor, que andeis de modo digno da vocação com que fostes chamados, com toda a humildade e mansidão, com longanimidade, suportando-vos uns aos outros em amor, procurando guardar a unidade do Espírito pelo vínculo da paz.\"",
                "analise": "\"Andar de modo digno\" (<em>axiōs peripatēsai</em>) — a palavra \"digno\" (<em>axios</em>) significa \"do mesmo peso\", \"equivalente\". A vida cristã deve ter o mesmo peso que a vocação cristã — a conduta deve corresponder à identidade. As quatro virtudes listadas — humildade (<em>tapeinophrosynē</em>), mansidão (<em>praütēs</em>), longanimidade (<em>makrothymia</em>), suportando-se em amor (<em>anechomenoi en agapē</em>) — são as virtudes relacionais que tornam a unidade possível. A humildade era desprezada no mundo greco-romano (era a virtude dos escravos); Paulo a coloca no topo da lista. \"Guardar a unidade do Espírito\" (<em>tērein tēn henotēta tou Pneumatos</em>) — a unidade já existe (é obra do Espírito); o dever dos crentes é preservá-la, não criá-la."
            },
            {
                "ref": "4:4-6 — Os Sete Uns",
                "texto": "\"Um só corpo e um só Espírito, como também fostes chamados em uma só esperança da vossa vocação; um só Senhor, uma só fé, um só batismo; um só Deus e Pai de todos, o qual é sobre todos, e por todos, e em todos.\"",
                "analise": "Os \"sete uns\" de Ef 4:4-6 são o fundamento teológico da unidade da Igreja. Eles têm uma estrutura trinitária: o Espírito (v. 4), o Senhor/Cristo (v. 5), o Pai (v. 6). A unidade da Igreja é fundamentada na unidade da Trindade. \"Um só corpo\" — a Igreja é um único organismo, não uma federação de comunidades independentes. \"Uma só fé\" — não uniformidade de opiniões em todas as questões, mas a fé apostólica comum transmitida nas Escrituras. \"Um só batismo\" — o batismo é o rito de iniciação que incorpora o crente no único corpo de Cristo. \"Um só Deus e Pai de todos\" — a paternidade universal de Deus é o fundamento último da fraternidade humana."
            },
            {
                "ref": "4:11-16 — Os Dons para a Edificação do Corpo",
                "texto": "\"E ele mesmo deu uns para apóstolos, e outros para profetas, e outros para evangelistas, e outros para pastores e doutores, para o aperfeiçoamento dos santos, para a obra do ministério, para a edificação do corpo de Cristo.\"",
                "analise": "A lista de dons em Ef 4:11 é a mais ministerial do NT — Paulo lista funções de liderança, não dons carismáticos como em 1 Co 12. Os cinco dons (ou quatro, se \"pastores e doutores\" forem um único dom) têm um propósito preciso: \"o aperfeiçoamento dos santos\" (<em>pros ton katartismon tōn hagiōn</em>). O modelo de ministério aqui é equipe, não hierarquia: os líderes existem para equipar os santos para o ministério, não para fazer o ministério em lugar dos santos. O objetivo final é \"a edificação do corpo de Cristo\" (<em>eis oikodomēn tou sōmatos tou Christou</em>) — a maturidade coletiva da Igreja, não apenas o crescimento numérico. \"Até que todos cheguemos à unidade da fé\" (v. 13) — o critério de maturidade é a medida de Cristo, não a comparação com outros crentes."
            },
            {
                "ref": "4:22-24 — O Velho e o Novo Homem",
                "texto": "\"Que, quanto ao trato passado, vos despojeis do velho homem, que se corrompe pelas concupiscências do engano; e vos renoveis no espírito da vossa mente; e vos revistais do novo homem, que segundo Deus é criado em verdadeira justiça e santidade.\"",
                "analise": "A metáfora do \"velho homem\" (<em>palaion anthrōpon</em>) e do \"novo homem\" (<em>kainon anthrōpon</em>) é uma das mais importantes da ética paulina. O \"velho homem\" é a velha identidade — a pessoa que éramos antes da conversão, orientada para o egoísmo e a corrupção. O \"novo homem\" é a nova identidade em Cristo — criado segundo a imagem de Deus em \"verdadeira justiça e santidade\" (<em>en dikaiosynē kai hosiotēti tēs alētheias</em>). Os três verbos — \"despojeis\" (<em>apothesthai</em>), \"renoveis\" (<em>ananeousthai</em>), \"revistais\" (<em>endysasthai</em>) — descrevem o processo de transformação moral como uma mudança de roupa: tirar a velha, renovar a mente, vestir a nova. A renovação da mente (<em>ananeousthai tō pneumati tou noos</em>) é o ponto central: a transformação começa na mente, não no comportamento."
            }
        ],
        "vocab": [
            {"termo": "ἑνότης", "transl": "henotēs", "def": "Unidade. Em Ef 4:3, Paulo exorta a 'guardar a unidade do Espírito'. A unidade já existe — é obra do Espírito; o dever dos crentes é preservá-la através das virtudes relacionais."},
            {"termo": "κατάρτισμος", "transl": "katartismos", "def": "Aperfeiçoamento, equipamento. O propósito dos dons ministeriais é equipar os santos para o ministério. Os líderes não fazem o ministério em lugar dos santos — eles os equipam para fazê-lo."},
            {"termo": "παλαιὸς ἄνθρωπος", "transl": "palaios anthrōpos", "def": "Velho homem. A velha identidade — a pessoa que éramos antes da conversão, orientada para o egoísmo e a corrupção. Deve ser 'despojada' como uma roupa velha."},
            {"termo": "ἀλήθεια", "transl": "alētheia", "def": "Verdade. Em Ef 4:15, Paulo exorta a 'seguir a verdade em amor' — o equilíbrio entre a integridade doutrinária e o amor relacional. A verdade sem amor é arrogância; o amor sem verdade é sentimentalismo."}
        ],
        "teologia": """<p>Efésios 4 apresenta a eclesiologia em sua dimensão prática. A Igreja é um corpo orgânico — não uma organização burocrática — onde cada membro tem uma função e onde a diversidade dos dons serve à unidade do todo. O modelo de ministério de Ef 4:11-16 é radicalmente diferente do clericalismo que dominou grande parte da história da Igreja: os líderes existem para equipar os membros, não para substituí-los.</p>
<p>A renovação da mente em Ef 4:23 é o coração da transformação cristã. A ética cristã não começa com a mudança de comportamento, mas com a renovação da mente — a transformação da forma como vemos a realidade, a Deus, a nós mesmos e ao próximo. Quando a mente é renovada, o comportamento segue naturalmente.</p>""",
        "aplicacao": """<p>Os "sete uns" de Ef 4:4-6 são o critério para avaliar a unidade ecumênica. A unidade cristã não exige uniformidade em todas as questões — mas exige acordo nos fundamentos: um corpo, um Espírito, uma esperança, um Senhor, uma fé, um batismo, um Deus e Pai. Divisões sobre questões secundárias são lamentáveis; divisões sobre estes fundamentos são impossíveis sem abandonar o Evangelho.</p>
<p>O modelo de ministério de Ef 4:11-12 desafia a passividade dos leigos e o clericalismo dos líderes. Os líderes que fazem tudo enquanto os membros assistem não estão seguindo o modelo de Paulo — estão privando os membros de sua vocação ministerial e a Igreja de sua plena capacidade. O ministério eficaz é aquele que multiplica ministros, não que os substitui.</p>"""
    },
    5: {
        "titulo": "Efésios 5 — Imitadores de Deus e o Mistério do Casamento",
        "ref": "Efésios 5:1-33 · Paulo · c. 60-62 d.C. · Roma",
        "chave": "Maridos, amai vossas mulheres, como também Cristo amou a Igreja e a si mesmo se entregou por ela. — Efésios 5:25",
        "contexto": """<p>Efésios 5 é um dos capítulos mais ricos e mais debatidos do NT. Ele tem três seções: (1) o apelo a imitar Deus no amor (vv. 1-7); (2) a vida como filhos da luz (vv. 8-21); e (3) a instrução sobre o casamento como reflexo da relação de Cristo com a Igreja (vv. 22-33). A seção sobre o casamento é uma das mais profundas e mais mal compreendidas do NT — ela não é primariamente um manual de relações conjugais, mas uma meditação teológica sobre o mistério da união de Cristo com a Igreja.</p>
<p>O versículo 18 — "não vos embriagueis com vinho, em que há devassidão; mas enchei-vos do Espírito" — é o pivô do capítulo. O contraste entre embriaguez e plenitude do Espírito não é apenas moral, mas litúrgico: Paulo está descrevendo o culto cristão como alternativa ao culto dionisíaco de Éfeso, onde a embriaguez era usada como meio de êxtase religioso. A plenitude do Espírito, ao contrário, produz louvor, gratidão e submissão mútua.</p>""",
        "versiculos": [
            {
                "ref": "5:1-2 — Imitadores de Deus",
                "texto": "\"Sede, pois, imitadores de Deus, como filhos amados; e andai em amor, como também Cristo nos amou, e se entregou a si mesmo por nós, em oferta e sacrifício a Deus, em cheiro suave.\"",
                "analise": "\"Imitadores de Deus\" (<em>mimetai tou Theou</em>) — a exortação mais ousada do NT. No mundo greco-romano, a imitação dos deuses era impossível — os deuses eram caprichosos, invejosos e imorais. Paulo afirma que os cristãos devem imitar Deus — porque são seus \"filhos amados\" (<em>tekna agapēta</em>) e porque Deus se tornou imitável em Cristo. O modelo de imitação é o amor de Cristo — \"se entregou a si mesmo por nós\" (<em>paredōken heauton hyper hēmōn</em>). A linguagem sacrificial — \"oferta e sacrifício a Deus, em cheiro suave\" — ecoa a linguagem do AT sobre os sacrifícios do templo (Lv 1:9,13,17). A morte de Cristo é o sacrifício definitivo que cumpre e transcende todos os sacrifícios do AT."
            },
            {
                "ref": "5:15-21 — Filhos da Luz e Plenitude do Espírito",
                "texto": "\"Olhai, pois, com diligência como andais, não como néscios, mas como sábios; remindo o tempo, porque os dias são maus... E não vos embriagueis com vinho, em que há devassidão; mas enchei-vos do Espírito, falando entre vós com salmos, e hinos, e cânticos espirituais.\"",
                "analise": "\"Remindo o tempo\" (<em>exagorazomenoi ton kairon</em>) — o verbo <em>exagorazō</em> é o mesmo usado para a redenção de escravos: \"comprar de volta\" o tempo que foi desperdiçado. O <em>kairos</em> (tempo qualitativo, oportuno) deve ser aproveitado porque \"os dias são maus\" (<em>hai hēmerai ponērai eisin</em>) — o mundo presente é hostil ao Evangelho. O contraste entre embriaguez e plenitude do Espírito é deliberado: ambas produzem estados alterados de consciência, mas de naturezas opostas. A embriaguez produz devassidão (<em>asōtia</em>); a plenitude do Espírito produz louvor, gratidão e submissão mútua. A lista de expressões do Espírito — \"salmos, hinos e cânticos espirituais\" — é a base bíblica para a diversidade de estilos de adoração na Igreja."
            },
            {
                "ref": "5:22-25 — O Mistério do Casamento",
                "texto": "\"As mulheres sejam submissas a seus próprios maridos, como ao Senhor... Maridos, amai vossas mulheres, como também Cristo amou a Igreja e a si mesmo se entregou por ela.\"",
                "analise": "A instrução sobre o casamento em Ef 5:22-33 deve ser lida no contexto do versículo 21 — \"sujeitando-vos uns aos outros no temor de Deus\" — que é a instrução geral da qual as instruções específicas (esposas, maridos, filhos, pais, escravos, senhores) são aplicações. A submissão da esposa (v. 22) é uma aplicação específica da submissão mútua geral (v. 21), não uma regra universal de hierarquia. A instrução ao marido (v. 25) é muito mais exigente: amar a esposa \"como Cristo amou a Igreja e a si mesmo se entregou por ela\" — o amor sacrificial de Cristo é o modelo, não o domínio patriarcal. O \"mistério\" (<em>mystērion</em>) de v. 32 — \"este mistério é grande; digo-o, porém, com respeito a Cristo e à Igreja\" — revela que Paulo está usando o casamento como ícone da relação de Cristo com a Igreja, não apenas como instituição social."
            }
        ],
        "vocab": [
            {"termo": "μιμητής", "transl": "mimētēs", "def": "Imitador. Os cristãos são chamados a imitar Deus — possível porque Deus se tornou imitável em Cristo. O modelo de imitação é o amor sacrificial de Cristo."},
            {"termo": "πληρόω", "transl": "plēroō", "def": "Encher, completar. 'Enchei-vos do Espírito' — a plenitude do Espírito é o estado normal da vida cristã, não uma experiência excepcional. É o oposto da embriaguez: em vez de ser controlado pelo vinho, ser controlado pelo Espírito."},
            {"termo": "ὑποτάσσω", "transl": "hypotassō", "def": "Submeter, sujeitar. Em Ef 5:21, a submissão mútua é a instrução geral; em 5:22, a submissão da esposa é uma aplicação específica. A submissão cristã é voluntária, não coercitiva."},
            {"termo": "μυστήριον", "transl": "mystērion", "def": "Mistério. O casamento é um 'mistério' — um ícone da relação de Cristo com a Igreja. Paulo usa o casamento como janela para compreender a relação de Cristo com seu povo."}
        ],
        "teologia": """<p>Efésios 5 apresenta a ética cristã como imitação de Deus — possível porque Deus se tornou imitável em Cristo. A vida moral cristã não é obediência a um código externo, mas participação na vida de Deus revelada em Cristo. O amor sacrificial de Cristo é o modelo e o poder da vida cristã.</p>
<p>A teologia do casamento em Ef 5:22-33 é uma das contribuições mais únicas de Paulo. O casamento não é apenas uma instituição social ou um contrato legal — é um sacramento, um sinal visível de uma realidade invisível: a relação de amor entre Cristo e a Igreja. Esta visão sacramental do casamento eleva a dignidade da instituição e define o padrão pelo qual deve ser vivida.</p>""",
        "aplicacao": """<p>A exortação "sede imitadores de Deus" (Ef 5:1) é o fundamento de toda a ética cristã. Não "siga as regras" ou "evite o pecado", mas "imite Deus" — seja como Deus é, ame como Deus ama. Esta é uma ética de caráter, não de conformidade; de identidade, não de performance.</p>
<p>A instrução sobre o casamento em Ef 5:25 — "maridos, amai vossas mulheres, como também Cristo amou a Igreja e a si mesmo se entregou por ela" — é o padrão mais alto possível para o amor conjugal. Cristo não apenas sentiu afeto pela Igreja — ele se entregou por ela. O amor conjugal cristão não é sentimento, mas entrega — o marido que ama como Cristo ama está disposto a morrer pelo bem da esposa.</p>"""
    },
    6: {
        "titulo": "Efésios 6 — A Armadura de Deus e a Guerra Espiritual",
        "ref": "Efésios 6:1-24 · Paulo · c. 60-62 d.C. · Roma",
        "chave": "Finalmente, irmãos, fortalecei-vos no Senhor e na força do seu poder. Revesti-vos de toda a armadura de Deus, para que possais ficar firmes contra as astutas ciladas do diabo. — Efésios 6:10-11",
        "contexto": """<p>Efésios 6 é o clímax da carta — a aplicação prática de toda a teologia dos capítulos anteriores à realidade da guerra espiritual. O capítulo tem três seções: (1) instruções às crianças, pais, escravos e senhores (vv. 1-9) — a continuação do "código doméstico" iniciado em 5:22; (2) a armadura de Deus (vv. 10-20) — a preparação para a guerra espiritual; e (3) a conclusão pessoal (vv. 21-24).</p>
<p>A metáfora da armadura de Deus é uma das mais conhecidas do NT. Paulo, escrevendo de Roma onde estava preso e provavelmente acorrentado a um soldado romano, usa o equipamento do soldado romano como metáfora para os recursos espirituais do crente. Mas há uma diferença crucial: as peças da armadura são identificadas com realidades teológicas — verdade, justiça, paz, fé, salvação, Palavra de Deus, oração — não com virtudes morais que o crente deve desenvolver. A armadura é de Deus, não do crente.</p>""",
        "versiculos": [
            {
                "ref": "6:10-12 — A Realidade da Guerra Espiritual",
                "texto": "\"Finalmente, irmãos, fortalecei-vos no Senhor e na força do seu poder. Revesti-vos de toda a armadura de Deus, para que possais ficar firmes contra as astutas ciladas do diabo. Porque não temos que lutar contra a carne e o sangue, mas contra os principados, contra as potestades, contra os príncipes das trevas desta era, contra as hostes espirituais da maldade nos lugares celestiais.\"",
                "analise": "\"Fortalecei-vos no Senhor\" (<em>endynamousthe en Kyriō</em>) — o verbo é passivo: não \"fortifique-se\" por esforço próprio, mas \"seja fortalecido\" pelo Senhor. A força para a guerra espiritual não é gerada pelo crente, mas recebida do Senhor. \"Toda a armadura de Deus\" (<em>tēn panoplian tou Theou</em>) — a <em>panoplia</em> era o equipamento completo do soldado de infantaria pesada. A ênfase em \"toda\" é importante: não partes da armadura, mas a armadura completa. \"Não temos que lutar contra a carne e o sangue\" — a guerra espiritual não é contra pessoas (inimigos humanos), mas contra poderes espirituais. \"Principados, potestades, príncipes das trevas, hostes espirituais da maldade\" — Paulo usa quatro termos para descrever a hierarquia dos poderes espirituais malignos. Esta não é mitologia — é a descrição da realidade espiritual que Paulo afirma existir por trás dos eventos históricos e das estruturas sociais."
            },
            {
                "ref": "6:13-17 — As Peças da Armadura",
                "texto": "\"Portanto, tomai toda a armadura de Deus, para que possais resistir no dia mau, e, havendo feito tudo, ficar firmes. Ficai, pois, firmes, tendo cingidos os vossos lombos com a verdade, e vestida a couraça da justiça, e calçados os pés com a preparação do evangelho da paz; tomando sobretudo o escudo da fé... o capacete da salvação e a espada do Espírito, que é a palavra de Deus.\"",
                "analise": "Cada peça da armadura corresponde a uma realidade teológica: (1) \"cinto da verdade\" (<em>alētheia</em>) — a verdade do Evangelho que sustenta tudo; (2) \"couraça da justiça\" (<em>dikaiosynē</em>) — a justiça imputada de Cristo que protege o coração; (3) \"calçados com o evangelho da paz\" (<em>euangelion tēs eirēnēs</em>) — a prontidão para proclamar o Evangelho; (4) \"escudo da fé\" (<em>pistis</em>) — a fé que apaga os \"dardos inflamados do maligno\"; (5) \"capacete da salvação\" (<em>sōtēria</em>) — a certeza da salvação que protege a mente; (6) \"espada do Espírito\" (<em>rhēma tou Theou</em>) — a Palavra de Deus como única arma ofensiva. A maioria das peças é defensiva — a guerra espiritual é primariamente resistência, não ataque. A única arma ofensiva é a Palavra de Deus — o Evangelho proclamado."
            },
            {
                "ref": "6:18-20 — A Oração como Arma",
                "texto": "\"Orando em todo o tempo com toda a oração e súplica no Espírito, e vigiando nisto com toda a perseverança e súplica por todos os santos; e por mim, para que me seja dada palavra ao abrir a minha boca, para fazer conhecido com ousadia o mistério do evangelho.\"",
                "analise": "A oração não é listada como uma peça da armadura — ela é a atmosfera em que toda a guerra espiritual é travada. \"Em todo o tempo\" (<em>en panti kairō</em>), \"com toda a oração\" (<em>dia pasēs proseuchēs</em>), \"com toda a perseverança\" (<em>en pasē proskarterēsei</em>) — a tripla ênfase em \"todo\" indica que a oração não é uma atividade entre outras, mas o modo de vida do guerreiro espiritual. O pedido de Paulo por si mesmo é revelador: ele não pede libertação da prisão, mas \"palavra ao abrir a minha boca\" — a capacidade de proclamar o Evangelho com ousadia (<em>parrēsia</em>). Para Paulo, a prisão não é o problema — o silêncio seria o problema."
            }
        ],
        "vocab": [
            {"termo": "πανοπλία", "transl": "panoplia", "def": "Armadura completa. O equipamento completo do soldado de infantaria pesada. Paulo usa esta metáfora para os recursos espirituais do crente — não virtudes a serem desenvolvidas, mas dons de Deus a serem recebidos."},
            {"termo": "ἀρχή / ἐξουσία", "transl": "archē / exousia", "def": "Principados / Potestades. Termos para poderes espirituais na hierarquia angélica e demoníaca. Em Paulo, estes poderes existem, são reais, mas foram derrotados por Cristo (Cl 2:15) e serão completamente subjugados na consumação."},
            {"termo": "παρρησία", "transl": "parrēsia", "def": "Ousadia, franqueza, liberdade de expressão. Paulo pede para proclamar o Evangelho com parrēsia — a ousadia que vem do Espírito, não da personalidade ou da circunstância. É a característica da pregação apostólica em Atos."},
            {"termo": "ῥῆμα", "transl": "rhēma", "def": "Palavra (falada, específica). A 'espada do Espírito' é o rhēma de Deus — a Palavra de Deus específica e aplicada, não apenas o texto geral das Escrituras. É a Palavra viva e ativa que o Espírito usa como arma."}
        ],
        "teologia": """<p>Efésios 6 apresenta a escatologia em sua dimensão prática: vivemos no "dia mau" (v. 13) — o período entre a primeira e a segunda vinda de Cristo, quando os poderes do mal ainda exercem influência, embora já derrotados pela cruz. A guerra espiritual não é uma batalha pelo resultado — Cristo já venceu (Cl 2:15). É uma batalha pelo território — a aplicação da vitória de Cristo à realidade presente.</p>
<p>A armadura de Deus revela que a guerra espiritual é fundamentalmente uma batalha pela mente e pelo coração. As peças da armadura — verdade, justiça, paz, fé, salvação, Palavra de Deus — são todas realidades cognitivas e espirituais. O inimigo ataca através de mentiras, acusações, dúvidas e distorções da realidade. A defesa é a verdade do Evangelho aplicada pela fé.</p>""",
        "aplicacao": """<p>A descrição da guerra espiritual em Ef 6:12 é um antídoto para dois erros opostos: o ceticismo que nega a existência de poderes espirituais, e o sensacionalismo que vê demônios em tudo. Paulo afirma que há poderes espirituais reais que se opõem ao Evangelho — mas que eles já foram derrotados por Cristo e que o crente tem toda a armadura necessária para resistir a eles.</p>
<p>O pedido de Paulo por "ousadia" (Ef 6:19-20) é um modelo de oração missionária. Em vez de pedir por circunstâncias favoráveis, Paulo pede pelo caráter necessário para proclamar o Evangelho em qualquer circunstância. A ousadia apostólica não depende de liberdade ou segurança — Paulo a pede de dentro de uma prisão romana.</p>"""
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
