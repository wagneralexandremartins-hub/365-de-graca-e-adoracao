#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera capítulos aprofundados:
1Tim (6), 2Tim (4), Tito (3), Filemom (1), Hebreus (13) = 27 capítulos
"""
import os

BASE = "/home/ubuntu/365-de-graca-e-adoracao/08-novo-testamento"

CSS = """<style>
.section-block{background:var(--panel2,#1a1a2e);border-radius:12px;padding:1.5rem;margin:1.5rem 0}
.section-block h2{color:var(--accent,#0ea5e9);margin-bottom:1rem;font-size:1.2rem}
.versiculo-bloco{border-left:3px solid var(--accent,#0ea5e9);padding:1rem 1.2rem;margin:1rem 0;background:rgba(255,255,255,0.03);border-radius:0 8px 8px 0}
.ref-v{font-size:.8rem;color:var(--accent,#0ea5e9);font-weight:700;margin-bottom:.4rem;text-transform:uppercase;letter-spacing:.05em}
.texto-v{font-style:italic;color:#e2e8f0;margin-bottom:.6rem;line-height:1.7}
.analise-v{color:#94a3b8;font-size:.92rem;line-height:1.7}
.chapter-hero{text-align:center;padding:3rem 1rem 2rem;background:linear-gradient(135deg,rgba(14,165,233,.15),rgba(99,102,241,.1))}
.chapter-number{font-size:.85rem;color:var(--accent,#0ea5e9);font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.5rem}
.chapter-subtitle{color:#94a3b8;font-style:italic;margin-top:.5rem}
.chapter-ref{color:var(--accent,#0ea5e9);font-size:.85rem}
.chapter-nav{display:flex;justify-content:space-between;padding:1.5rem;gap:1rem;flex-wrap:wrap}
.chapter-nav a{color:var(--accent,#0ea5e9);text-decoration:none;padding:.5rem 1rem;border:1px solid var(--accent,#0ea5e9);border-radius:6px}
.breadcrumb{padding:.75rem 1.5rem;font-size:.85rem;color:#64748b}
.breadcrumb a{color:var(--accent,#0ea5e9);text-decoration:none}
.wrap{max-width:860px;margin:0 auto;padding:0 1.5rem 3rem}
</style>"""

def page(livro, num, total, titulo, vk, rk, body, livro_dir, depth="../../.."):
    prev = f"capitulo-{num-1:02d}.html" if num > 1 else "../index.html"
    nxt = f"capitulo-{num+1:02d}.html" if num < total else "../index.html"
    pl = f"Anterior: {livro} {num-1}" if num > 1 else "Voltar ao Índice"
    nl = f"Próximo: {livro} {num+1}" if num < total else "Voltar ao Índice"
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{livro} {num} — {titulo} | 365 de Graça &amp; Adoração</title>
  <meta name="description" content="Estudo aprofundado de {livro} capítulo {num}: {titulo}. Análise exegética versículo por versículo.">
  <link rel="stylesheet" href="{depth}/assets/css/style.css">
  <link rel="stylesheet" href="{depth}/assets/css/bloco.css">
  {CSS}
</head>
<body class="bloco-08">
  <header class="topbar">
    <a class="brand" href="/">365 de Graça &amp; Adoração</a>
    <nav><a href="/">Início</a><a href="/08-novo-testamento/">NT</a><a href="/busca/">Buscar</a></nav>
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
    <a href="{prev}">← {pl}</a>
    <a href="../index.html">Índice de {livro}</a>
    <a href="{nxt}">{nl} →</a>
  </nav>
  <footer class="site-footer">
    <p>365 de Graça &amp; Adoração • Da Criação ao Apocalipse • © 2026</p>
  </footer>
</body>
</html>"""

def bloco(titulo, items):
    h = f'    <div class="section-block">\n      <h2>{titulo}</h2>\n'
    for ref, txt, analise in items:
        h += f'      <div class="versiculo-bloco"><div class="ref-v">{ref}</div><div class="texto-v">"{txt}"</div><div class="analise-v">{analise}</div></div>\n'
    return h + "    </div>\n"

def intro(txt):
    return f'    <div class="section-block"><p>{txt}</p></div>\n'

def salvar(livro_dir, num, html):
    path = os.path.join(BASE, livro_dir, "capitulos", f"capitulo-{num:02d}.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

# ─── 1 TIMÓTEO ─────────────────────────────────────────────────────────────────
caps_1tim = {
    1: ("Graça para o Maior dos Pecadores", "Cristo Jesus veio ao mundo para salvar os pecadores, dos quais eu sou o principal.", "1Tm 1:15",
        intro("1 Timóteo é uma das 'Epístolas Pastorais' — cartas de Paulo ao seu filho espiritual Timóteo sobre como conduzir a Igreja. O cap. 1 estabelece o propósito da lei e o Evangelho da graça.") +
        bloco("📜 O Propósito da Lei (1:8-11)", [
            ("1Tm 1:8-10", "Ora, sabemos que a lei é boa, se alguém a usa legitimamente; sabendo que a lei não é feita para o justo, mas para os transgressores e desobedientes, para os ímpios e pecadores...",
             "A lei tem um propósito legítimo: revelar o pecado e conduzir ao Evangelho. Ela não é feita para o justo (que já vive pelo Espírito), mas para os transgressores. A lista de pecados em 1:9-10 espelha os Dez Mandamentos — a lei ainda define o pecado."),
        ]) +
        bloco("💙 O Evangelho da Graça (1:12-17)", [
            ("1Tm 1:15-16", "Esta é uma palavra fiel e digna de toda a aceitação: que Cristo Jesus veio ao mundo para salvar os pecadores, dos quais eu sou o principal. Mas por isso mesmo alcancei misericórdia, para que em mim, o principal, Jesus Cristo mostrasse toda a longanimidade, para exemplo dos que hão de crer nele para a vida eterna.",
             "O 'dito fiel' (<em>pistos ho logos</em>) — fórmula litúrgica que introduz declarações doutrinais fundamentais. Paulo se chama 'o principal dos pecadores' (<em>proton</em>) — não retórica, mas convicção genuína baseada na perseguição da Igreja. Sua conversão é o exemplo máximo da longanimidade de Cristo.")
        ])),
    2: ("Oração por Todos e o Papel da Mulher", "Porque há um só Deus e um só Mediador entre Deus e os homens, Jesus Cristo homem.", "1Tm 2:5",
        intro("1 Timóteo 2 ensina sobre a oração universal e aborda questões controversas sobre o papel da mulher na adoração pública.") +
        bloco("🙏 Oração por Todos (2:1-7)", [
            ("1Tm 2:1-4", "Exorto, pois, antes de tudo, que se façam súplicas, orações, intercessões, ações de graças, por todos os homens; pelos reis e por todos os que estão em autoridade, para que vivamos uma vida tranquila e sossegada, em toda a piedade e honestidade. Porque isso é bom e aceitável diante de Deus nosso Salvador, o qual quer que todos os homens sejam salvos.",
             "A oração universal: quatro termos para oração (súplicas, orações, intercessões, ações de graças) por todos os homens, incluindo governantes. O fundamento teológico: Deus quer que todos sejam salvos (<em>pantas anthropous thelei sothenas</em>). A oração pelos governantes é ato político-espiritual — paz pública favorece a proclamação do Evangelho."),
            ("1Tm 2:5-6", "Porque há um só Deus e um só Mediador entre Deus e os homens, Jesus Cristo homem; o qual se deu a si mesmo em resgate por todos.",
             "O monoteísmo cristológico: um só Deus, um só Mediador. <em>Mesites</em> — mediador: o que está entre dois partidos para reconciliá-los. Cristo é o único mediador porque é ao mesmo tempo plenamente Deus e plenamente homem. O resgate (<em>antilytron</em>) é substitutivo — 'por todos'.")
        ])),
    3: ("Qualificações dos Líderes", "Porque, se alguém não sabe governar a sua própria casa, como cuidará da Igreja de Deus?", "1Tm 3:5",
        intro("1 Timóteo 3 lista as qualificações para bispos (presbíteros) e diáconos — o texto mais completo sobre liderança eclesiástica no NT.") +
        bloco("👑 Qualificações do Bispo (3:1-7)", [
            ("1Tm 3:1-7", "Esta é uma palavra fiel: se alguém deseja o episcopado, excelente obra deseja. É necessário, pois, que o bispo seja irrepreensível, marido de uma só mulher, sóbrio, prudente, honesto, hospitaleiro, apto para ensinar; não dado ao vinho, não espancador, mas moderado, não contencioso, não avarento; que governe bem a sua própria casa...",
             "As 15 qualificações do bispo (<em>episkopos</em>): a maioria são qualidades de caráter, não habilidades técnicas. 'Marido de uma só mulher' — debatido: proibição de poligamia, ou de segundo casamento após divórcio/viuvez? O contexto favorece fidelidade conjugal. 'Apto para ensinar' (<em>didaktikos</em>) é a única qualificação ministerial específica.")
        ]) +
        bloco("🏛️ O Mistério da Piedade (3:14-16)", [
            ("1Tm 3:16", "E, sem dúvida alguma, grande é o mistério da piedade: Deus foi manifestado em carne, justificado no Espírito, visto dos anjos, pregado entre os gentios, crido no mundo, recebido em glória.",
             "O hino cristológico de 6 linhas — provavelmente litúrgico. As seis afirmações em pares: encarnação/ressurreição, revelação angelical/proclamação humana, fé mundial/exaltação gloriosa. 'Deus foi manifestado em carne' (<em>theos ephanerothes en sarki</em>) — a encarnação como epifania divina.")
        ])),
    4: ("O Bom Ministro de Jesus Cristo", "Exercita-te na piedade; porque o exercício corporal para pouco é proveitoso, mas a piedade para tudo é proveitosa.", "1Tm 4:7-8",
        intro("1 Timóteo 4 adverte sobre apostasia nos últimos tempos e exorta Timóteo a ser um bom ministro de Cristo através do exemplo e do ensino.") +
        bloco("⚠️ Apostasia nos Últimos Tempos (4:1-5)", [
            ("1Tm 4:1-3", "Mas o Espírito expressamente diz que nos últimos tempos alguns apostatarão da fé, dando ouvidos a espíritos enganadores e a doutrinas de demônios... proibindo o casamento e ordenando que se abstenham de alimentos.",
             "A apostasia dos últimos tempos: abandono da fé, seguindo espíritos enganadores e doutrinas demoníacas. Os sinais específicos: proibição do casamento e abstinência de alimentos — ascetismo gnóstico que negava a bondade da criação material.")
        ]) +
        bloco("💪 O Bom Ministro (4:6-16)", [
            ("1Tm 4:12-13", "Ninguém te despreze pela tua mocidade; mas sê o exemplo dos fiéis, na palavra, no trato, no amor, no espírito, na fé, na pureza. Até que eu venha, aplica-te à leitura, à exortação e ao ensino.",
             "Timóteo era jovem (~30 anos) em uma cultura que valorizava a idade. Paulo o instrui a não permitir que o desprezem — não por arrogância, mas por ser exemplo em 6 áreas: palavra, trato, amor, espírito, fé, pureza. O ministério da leitura pública das Escrituras era central no culto primitivo.")
        ])),
    5: ("Cuidado com as Viúvas e os Presbíteros", "Os presbíteros que governam bem sejam tidos por dignos de duplicada honra.", "1Tm 5:17",
        intro("1 Timóteo 5 fornece instruções detalhadas sobre o cuidado com viúvas e o tratamento de presbíteros — revelando a estrutura social da Igreja primitiva.") +
        bloco("👩 As Viúvas (5:3-16)", [
            ("1Tm 5:3-5", "Honra as viúvas que são verdadeiramente viúvas. Mas, se alguma viúva tem filhos ou netos, aprendam estes primeiro a mostrar piedade para com a própria família e a recompensar os pais; porque isso é bom e aceitável diante de Deus.",
             "A Igreja primitiva tinha um 'rol de viúvas' — mulheres dedicadas ao ministério de oração e serviço. As qualificações: verdadeiramente viúva (sem família), acima de 60 anos, fiel ao marido, conhecida por boas obras. A família tem responsabilidade primária — a Igreja cuida quando a família não pode.")
        ]) +
        bloco("👑 Os Presbíteros (5:17-25)", [
            ("1Tm 5:17-19", "Os presbíteros que governam bem sejam tidos por dignos de duplicada honra, principalmente os que trabalham na palavra e no ensino. Porque diz a Escritura: Não atarás a boca ao boi que debulha; e: Digno é o obreiro do seu salário. Contra um presbítero não aceites acusação, senão sob o depoimento de duas ou três testemunhas.",
             "A 'duplicada honra' (<em>diplaes times</em>) inclui respeito e remuneração. Paulo cita Dt 25:4 e Lc 10:7 para fundamentar o sustento dos ministros. A proteção dos presbíteros contra acusações falsas é essencial — mas a disciplina pública é necessária quando comprovada a falta.")
        ])),
    6: ("Contentamento e a Boa Confissão", "Porque o amor ao dinheiro é a raiz de todos os males.", "1Tm 6:10",
        intro("1 Timóteo 6 encerra com advertências sobre o amor ao dinheiro, a exortação à piedade com contentamento, e o mandato final a Timóteo.") +
        bloco("💰 Piedade com Contentamento (6:6-19)", [
            ("1Tm 6:6-10", "Mas é grande ganho a piedade com contentamento. Porque nada trouxemos para este mundo, e manifesto é que nada podemos levar. Tendo, pois, sustento e com que nos cobrirmos, estejamos com isso contentes. Porque os que querem ser ricos caem em tentação, e em laço, e em muitas concupiscências loucas e nocivas... Porque o amor ao dinheiro é a raiz de todos os males.",
             "A equação da riqueza verdadeira: piedade + contentamento = grande ganho. O amor ao dinheiro (<em>philargyria</em>) — não o dinheiro em si, mas o amor a ele — é raiz de todos os males. A riqueza material é neutra; o amor a ela é destrutivo."),
            ("1Tm 6:17-19", "Aos ricos no século presente manda que não sejam altivos, nem ponham a sua esperança na incerteza das riquezas, mas em Deus... que sejam ricos em boas obras, prontos a distribuir, comunicativos; entesourando para si um bom fundamento para o futuro.",
             "Para os que já são ricos: não proibição, mas instrução. Quatro mandatos: não ser altivo, não confiar nas riquezas, ser rico em boas obras, ser generoso. A riqueza material pode ser convertida em riqueza eterna através da generosidade.")
        ])),
}

def gerar_1timoteo():
    for num, (titulo, vk, rk, body) in caps_1tim.items():
        html = page("1 Timóteo", num, 6, titulo, vk, rk, body, "1timoteo", "../../../..")
        salvar("1timoteo", num, html)
    print("✅ 1 Timóteo: 6 capítulos gerados")

# ─── 2 TIMÓTEO ─────────────────────────────────────────────────────────────────
caps_2tim = {
    1: ("Não te Envergonhes do Evangelho", "Porque Deus não nos deu o espírito de temor, mas de poder, de amor e de moderação.", "2Tm 1:7",
        intro("2 Timóteo é a última carta de Paulo — escrita pouco antes de sua execução (~67 d.C.). É o testamento espiritual do apóstolo, cheio de urgência e ternura.") +
        bloco("🔥 O Espírito de Poder (1:6-14)", [
            ("2Tm 1:6-8", "Por esta causa te admoesto que despertes o dom de Deus que há em ti pela imposição das minhas mãos. Porque Deus não nos deu o espírito de temor, mas de poder, de amor e de moderação. Não te envergonhes, pois, do testemunho de nosso Senhor, nem de mim, seu prisioneiro.",
             "O dom (<em>charisma</em>) de Timóteo precisa ser 'avivado' (<em>anazopyrein</em> — reavivar como brasa). O Espírito não é de temor (<em>deilia</em> — covardia) mas de poder (<em>dynamis</em>), amor (<em>agape</em>) e moderação (<em>sophronismos</em> — autodisciplina). Timóteo estava com medo — Paulo o chama à coragem."),
            ("2Tm 1:12", "Por esta causa também sofro estas coisas; mas não me envergonho, porque sei em quem tenho crido, e estou certo de que é poderoso para guardar o meu depósito até aquele dia.",
             "A confiança de Paulo na prisão: 'sei em quem tenho crido' (<em>oida ho pepisteka</em>) — não 'o que', mas 'em quem'. A fé pessoal em Cristo, não apenas em doutrinas sobre Cristo. O 'depósito' (<em>paratheke</em>) — a vida de Paulo confiada a Cristo para ser guardada até o dia do juízo.")
        ])),
    2: ("O Soldado, o Atleta e o Lavrador", "Esforça-te na graça que há em Cristo Jesus.", "2Tm 2:1",
        intro("2 Timóteo 2 usa três metáforas — soldado, atleta, lavrador — para descrever o ministério cristão, e apresenta o 'dito fiel' sobre a morte e ressurreição com Cristo.") +
        bloco("⚔️ Três Metáforas do Ministério (2:3-7)", [
            ("2Tm 2:3-6", "Sofre as aflições como bom soldado de Jesus Cristo. Nenhum soldado em serviço se envolve nos negócios da vida, para que agrade àquele que o alistou. E também, se alguém lutar como atleta, não é coroado se não lutar legitimamente. O lavrador que trabalha deve ser o primeiro a participar dos frutos.",
             "Três metáforas do ministério: (1) Soldado — foco, separação do mundo, lealdade ao comandante; (2) Atleta — disciplina, regras, recompensa; (3) Lavrador — trabalho duro, paciência, participação nos frutos. Cada metáfora ilumina um aspecto diferente do ministério fiel.")
        ]) +
        bloco("📖 A Palavra de Deus Não Está Presa (2:8-13)", [
            ("2Tm 2:9-10", "Pelo qual sofro até laços, como malfeitor; mas a palavra de Deus não está presa. Por isso tudo suporto por amor dos eleitos, para que também eles alcancem a salvação que está em Cristo Jesus com glória eterna.",
             "Paulo está acorrentado, mas a Palavra de Deus é livre. O sofrimento apostólico tem propósito: a salvação dos eleitos. O 'dito fiel' de 2:11-13 é provavelmente um hino batismal: morrer com Cristo → viver; perseverar → reinar; negar → ser negado; ser infiel → Cristo permanece fiel.")
        ])),
    3: ("Os Últimos Dias e a Escritura Inspirada", "Toda a Escritura é divinamente inspirada e proveitosa para ensinar, para repreender, para corrigir, para instruir em justiça.", "2Tm 3:16",
        intro("2 Timóteo 3 descreve a deterioração moral dos últimos dias e apresenta a Escritura como o recurso suficiente para o ministério fiel.") +
        bloco("⚠️ Os Últimos Dias (3:1-9)", [
            ("2Tm 3:1-5", "Sabe também isto: que nos últimos dias sobrevirão tempos difíceis. Porque haverá homens amantes de si mesmos, avarentos, presunçosos, soberbos, blasfemos, desobedientes aos pais, ingratos, profanos, sem afeto natural, implacáveis, caluniadores, intemperantes, cruéis, aborrecedores do bem, traidores, temerários, orgulhosos, mais amigos dos prazeres do que amigos de Deus; tendo aparência de piedade, mas negando a eficácia dela.",
             "A lista de 19 vícios dos últimos dias começa e termina com amor próprio (<em>philautoi</em>) e amor ao prazer (<em>philedoni</em>) em oposição ao amor a Deus (<em>philotheos</em>). O mais assustador: 'tendo aparência de piedade' — religiosidade sem transformação.")
        ]) +
        bloco("📖 A Escritura Inspirada (3:14-17)", [
            ("2Tm 3:16-17", "Toda a Escritura é divinamente inspirada e proveitosa para ensinar, para repreender, para corrigir, para instruir em justiça; para que o homem de Deus seja perfeito, e perfeitamente instruído para toda boa obra.",
             "<em>Theopneustos</em> — divinamente inspirada (literalmente 'soprada por Deus'): a Escritura é o sopro de Deus em forma de palavras. As quatro funções: ensinar (doutrina), repreender (erro), corrigir (conduta errada), instruir em justiça (formação positiva). O resultado: o homem de Deus 'perfeito' (<em>artios</em>) — equipado, completo.")
        ])),
    4: ("O Testamento Final de Paulo", "Combati o bom combate, acabei a carreira, guardei a fé.", "2Tm 4:7",
        intro("2 Timóteo 4 é o capítulo mais pessoal e emocionante de Paulo — seu testamento final, escrito às vésperas do martírio.") +
        bloco("📣 O Mandato Final (4:1-5)", [
            ("2Tm 4:1-2", "Conjuro-te, pois, diante de Deus e do Senhor Jesus Cristo, que há de julgar os vivos e os mortos na sua manifestação e no seu reino: Prega a palavra, insta a tempo e fora de tempo, repreende, exorta, com toda a longanimidade e doutrina.",
             "O mandato mais solene do NT: conjurado diante de Deus e de Cristo, o Juiz. 'Prega a palavra' (<em>kerygon ton logon</em>) — o imperativo central. 'A tempo e fora de tempo' (<em>eukairon akairos</em>) — conveniente ou não, oportuno ou não. A pregação fiel não espera condições favoráveis.")
        ]) +
        bloco("🏆 O Testamento de Paulo (4:6-22)", [
            ("2Tm 4:6-8", "Porque eu já estou sendo oferecido em libação, e o tempo da minha partida está próximo. Combati o bom combate, acabei a carreira, guardei a fé. Já agora a coroa da justiça me está guardada, a qual o Senhor, o justo Juiz, me dará naquele dia; e não somente a mim, mas também a todos os que amam a sua vinda.",
             "As três metáforas finais de Paulo: (1) libação (<em>spendomai</em>) — derramado como oferta; (2) combate (<em>agon</em>) — a luta foi boa; (3) corrida (<em>dromos</em>) — a carreira foi completada. A fé foi guardada. A coroa da justiça (<em>stephanos tes dikaiosyne</em>) aguarda — não apenas Paulo, mas todos os que amam a vinda de Cristo."),
            ("2Tm 4:16-17", "Na minha primeira defesa, ninguém esteve da minha parte, antes todos me desampararam; não lhes seja imputado. O Senhor, porém, esteve comigo e me fortaleceu, para que por mim fosse cumprida a pregação, e todos os gentios a ouvissem.",
             "O eco de Jesus na cruz: 'todos me desampararam' — mas o Senhor esteve comigo. Mesmo no abandono humano, a presença divina é suficiente. Paulo perdoa os que o abandonaram — 'não lhes seja imputado' — ecoando Estêvão (At 7:60) e o próprio Jesus (Lc 23:34).")
        ])),
}

def gerar_2timoteo():
    for num, (titulo, vk, rk, body) in caps_2tim.items():
        html = page("2 Timóteo", num, 4, titulo, vk, rk, body, "2timoteo", "../../../..")
        salvar("2timoteo", num, html)
    print("✅ 2 Timóteo: 4 capítulos gerados")

# ─── TITO ──────────────────────────────────────────────────────────────────────
caps_tito = {
    1: ("Qualificações dos Líderes em Creta", "Para que ponhas em boa ordem as coisas que ainda restam, e constituas presbíteros em cada cidade.", "Tt 1:5",
        intro("Tito é uma Epístola Pastoral escrita a Tito, colaborador de Paulo em Creta. O cap. 1 trata da organização eclesiástica e da refutação de falsos mestres.") +
        bloco("👑 Qualificações do Presbítero (1:5-9)", [
            ("Tt 1:5-9", "Para que ponhas em boa ordem as coisas que ainda restam, e constituas presbíteros em cada cidade, como também eu te ordenei; se alguém é irrepreensível, marido de uma só mulher, e tem filhos fiéis, que não sejam acusados de dissolução ou de desobediência.",
             "As qualificações em Tito são similares a 1Tm 3, mas com ênfase na família. 'Filhos fiéis' — o lar do líder é o laboratório de sua liderança. A qualificação central: 'retenha a fiel palavra conforme a doutrina, para que seja poderoso tanto para exortar com a sã doutrina como para convencer os que contradizem' (1:9).")
        ]) +
        bloco("⚠️ Falsos Mestres em Creta (1:10-16)", [
            ("Tt 1:12-13", "Um deles, seu próprio profeta, disse: Os cretenses são sempre mentirosos, bestas ruins, ventres preguiçosos. Este testemunho é verdadeiro. Por isso repreende-os severamente, para que sejam sãos na fé.",
             "Paulo cita o poeta cretense Epimênides (~600 a.C.) — um dos raros exemplos de Paulo usando literatura pagã. A repreensão severa (<em>apotomos</em>) é necessária para a saúde da Igreja. A sã doutrina (<em>hygiaino</em> — saudável) é o antídoto para o ensino doentio.")
        ])),
    2: ("A Graça que Ensina", "Porque a graça de Deus se manifestou salvadora a todos os homens, ensinando-nos que, renunciando à impiedade e às concupiscências mundanas, vivamos sensata, justa e piedosamente neste século.", "Tt 2:11-12",
        intro("Tito 2 apresenta instruções para diferentes grupos na Igreja e o fundamento teológico: a graça de Deus que salva e transforma.") +
        bloco("🌟 A Graça que Ensina (2:11-14)", [
            ("Tt 2:11-14", "Porque a graça de Deus se manifestou salvadora a todos os homens, ensinando-nos que, renunciando à impiedade e às concupiscências mundanas, vivamos sensata, justa e piedosamente neste século; aguardando a bem-aventurada esperança e o aparecer da glória do grande Deus e nosso Salvador Jesus Cristo; o qual se deu a si mesmo por nós, para nos remir de toda a iniquidade e purificar para si um povo seu especial, zeloso de boas obras.",
             "A graça não apenas salva — ela ensina (<em>paideuousa</em>). O currículo da graça: renunciar à impiedade, viver santamente, aguardar a vinda de Cristo. A 'bem-aventurada esperança' (<em>makarian elpida</em>) é a parusia. A declaração 'grande Deus e nosso Salvador Jesus Cristo' é uma das afirmações mais claras da divindade de Cristo no NT.")
        ])),
    3: ("Salvos pela Misericórdia de Deus", "Mas quando se manifestou a bondade de Deus nosso Salvador, e o seu amor para com os homens, ele nos salvou.", "Tt 3:4-5",
        intro("Tito 3 encerra com a teologia da regeneração e renovação pelo Espírito Santo, e exortações práticas para a vida cidadã.") +
        bloco("🕊️ Regeneração pelo Espírito (3:4-7)", [
            ("Tt 3:4-7", "Mas quando se manifestou a bondade de Deus nosso Salvador, e o seu amor para com os homens, ele nos salvou, não pelas obras de justiça que houvéssemos feito, mas segundo a sua misericórdia, pela lavagem da regeneração e da renovação do Espírito Santo; o qual derramou sobre nós ricamente por Jesus Cristo nosso Salvador; para que, sendo justificados pela sua graça, nos tornássemos herdeiros segundo a esperança da vida eterna.",
             "A trindade da salvação: Deus Pai manifestou bondade e amor; Cristo nos salvou; o Espírito renova pela regeneração. A salvação não é pelas obras de justiça (<em>ergon en dikaiosyne</em>), mas pela misericórdia divina. A 'lavagem da regeneração' (<em>loutrou palingenesias</em>) provavelmente alude ao batismo como sinal da regeneração pelo Espírito.")
        ])),
}

def gerar_tito():
    for num, (titulo, vk, rk, body) in caps_tito.items():
        html = page("Tito", num, 3, titulo, vk, rk, body, "tito", "../../../..")
        salvar("tito", num, html)
    print("✅ Tito: 3 capítulos gerados")

# ─── FILEMOM ───────────────────────────────────────────────────────────────────
caps_filemom = {
    1: ("A Intercessão por Onésimo", "Recebe-o, pois, como a mim mesmo. Se te prejudicou em alguma coisa, ou te deve alguma coisa, lança isso na minha conta.", "Fm 1:17-18",
        intro("Filemom é a carta mais pessoal de Paulo — uma intercessão pelo escravo fugitivo Onésimo. Em 25 versículos, Paulo demonstra como o Evangelho transforma as relações sociais.") +
        bloco("💙 A Intercessão de Paulo (1:8-21)", [
            ("Fm 1:10-12", "Rogo-te pelo meu filho Onésimo, que gerei nas minhas prisões; o qual noutro tempo te foi inútil, mas agora é útil tanto a ti como a mim; e to envio de volta. Tu, pois, recebe-o como as minhas próprias entranhas.",
             "O jogo de palavras: <em>Onesimos</em> significa 'útil' em grego. 'Noutro tempo inútil, agora útil' — a conversão transformou o escravo fugitivo. Paulo envia Onésimo de volta não como escravo, mas como irmão amado."),
            ("Fm 1:15-18", "Porque talvez por isso se apartou de ti por um momento, para que o recebesses para sempre; não já como escravo, mas muito mais do que escravo, como irmão amado... Recebe-o, pois, como a mim mesmo. Se te prejudicou em alguma coisa, ou te deve alguma coisa, lança isso na minha conta.",
             "A teologia da providência: 'talvez por isso' — Deus usou a fuga de Onésimo para sua conversão. A transformação social do Evangelho: de escravo a irmão amado. Paulo se oferece como fiador — 'lança na minha conta' (<em>emoi ellogas</em>) — imagem da imputação e da intercessão de Cristo.")
        ])),
}

def gerar_filemom():
    for num, (titulo, vk, rk, body) in caps_filemom.items():
        html = page("Filemom", num, 1, titulo, vk, rk, body, "filemom", "../../../..")
        salvar("filemom", num, html)
    print("✅ Filemom: 1 capítulo gerado")

# ─── HEBREUS ───────────────────────────────────────────────────────────────────
caps_hebreus = {
    1: ("O Filho Superior aos Anjos", "Tendo Deus outrora falado, muitas vezes e de muitas maneiras, aos pais pelos profetas, a nós falou-nos nestes últimos dias pelo Filho.", "Hb 1:1-2",
        intro("Hebreus é a carta mais teologicamente sofisticada do NT — uma homilia sobre a superioridade de Cristo sobre toda a revelação anterior. O cap. 1 proclama Cristo como o Filho superior aos anjos.") +
        bloco("👑 O Filho Herdeiro de Tudo (1:1-4)", [
            ("Hb 1:1-4", "Tendo Deus outrora falado, muitas vezes e de muitas maneiras, aos pais pelos profetas, a nós falou-nos nestes últimos dias pelo Filho, a quem constituiu herdeiro de todas as coisas, pelo qual também fez o universo; o qual, sendo o resplendor da sua glória e a expressa imagem da sua essência, e sustentando todas as coisas pela palavra do seu poder, havendo feito a purificação dos pecados, assentou-se à destra da Majestade nas alturas.",
             "A abertura mais literária do NT — um período de 4 versículos em grego. Cristo é apresentado com 7 atributos: (1) herdeiro de tudo; (2) criador do universo; (3) resplendor da glória (<em>apaugasma tes doxes</em>); (4) imagem da essência (<em>charakter tes hypostaseos</em>); (5) sustentador de tudo; (6) purificador dos pecados; (7) assentado à destra de Deus. A progressão é de criação a redenção a exaltação.")
        ]) +
        bloco("🌟 Superior aos Anjos (1:5-14)", [
            ("Hb 1:5-6", "Porque a qual dos anjos disse ele alguma vez: Tu és meu Filho, eu hoje te gerei? E outra vez: Eu serei para ele Pai, e ele será para mim Filho? E outra vez, quando introduz o primogênito no mundo, diz: E todos os anjos de Deus o adorem.",
             "A cadeia de 7 citações do AT prova a superioridade de Cristo sobre os anjos. Os anjos são servos (<em>leitourgika pneumata</em>); o Filho é Rei. A adoração dos anjos ao Filho (Sl 97:7) confirma sua divindade — anjos só adoram a Deus.")
        ])),
    2: ("A Salvação Tão Grande", "Como escaparemos nós, se negligenciarmos tão grande salvação?", "Hb 2:3",
        intro("Hebreus 2 apresenta o primeiro de cinco 'avisos' da carta — contra a negligência da salvação — e explica por que o Filho eterno se tornou humano.") +
        bloco("⚠️ Primeiro Aviso: Não Negligenciar (2:1-4)", [
            ("Hb 2:1-3", "Por isso importa que com mais diligência atendamos às coisas que ouvimos, para que não venhamos a perdê-las. Porque, se a palavra falada por meio de anjos foi firme, e toda transgressão e desobediência recebeu justa recompensa, como escaparemos nós, se negligenciarmos tão grande salvação?",
             "O argumento a fortiori: se a lei dada por anjos tinha consequências severas, quanto mais a salvação proclamada pelo próprio Filho. 'Negligenciar' (<em>amelesantes</em>) — não rejeição ativa, mas indiferença passiva. A maior ameaça ao cristão não é a perseguição, mas a negligência.")
        ]) +
        bloco("🙏 Por que o Filho se Tornou Homem (2:9-18)", [
            ("Hb 2:14-17", "Assim, pois, visto que os filhos participam da carne e do sangue, também ele participou das mesmas coisas, para que, pela morte, destruísse aquele que tinha o poder da morte, a saber, o diabo; e livrasse todos os que, pelo temor da morte, estavam sujeitos à escravidão durante toda a vida.",
             "A encarnação como estratégia de redenção: para destruir o diabo pelo poder da morte, o Filho precisava morrer; para morrer, precisava ser humano. A humanidade de Cristo não é acidente — é necessidade redentora. Cristo destruiu o poder da morte ao morrer e ressuscitar.")
        ])),
    3: ("Jesus Superior a Moisés", "Porque este foi julgado digno de maior glória do que Moisés, tanto quanto tem mais honra do que a casa aquele que a edificou.", "Hb 3:3",
        intro("Hebreus 3 compara Jesus a Moisés — o maior herói do judaísmo — e demonstra a superioridade de Cristo. O segundo aviso: contra a incredulidade e o endurecimento do coração.") +
        bloco("👑 Jesus Superior a Moisés (3:1-6)", [
            ("Hb 3:5-6", "E Moisés foi fiel em toda a sua casa como servo, para testemunho das coisas que haviam de ser anunciadas; mas Cristo, como Filho, sobre a sua própria casa; a qual casa somos nós, se retivermos firme até ao fim a confiança e a glória da esperança.",
             "A comparação: Moisés foi fiel como servo (<em>therapon</em>) na casa de Deus; Cristo é fiel como Filho (<em>huios</em>) sobre a casa. O servo testemunha o que virá; o Filho é o que foi prometido. A Igreja é a 'casa' de Cristo — mas apenas se perseverarmos.")
        ]) +
        bloco("⚠️ Segundo Aviso: Não Endurecer o Coração (3:7-19)", [
            ("Hb 3:12-14", "Vede, irmãos, que jamais haja em algum de vós coração mau e incrédulo, para se apartar do Deus vivo. Antes exortai-vos uns aos outros cada dia, enquanto se chama Hoje, para que nenhum de vós se endureça pelo engano do pecado.",
             "O perigo do endurecimento progressivo: o pecado engana, o coração endurece, a incredulidade cresce. O antídoto: exortação mútua diária. A comunidade cristã é o ambiente de perseverança — o individualismo espiritual é vulnerável ao endurecimento.")
        ])),
    4: ("O Descanso de Deus e o Sumo Sacerdote Compassivo", "Não temos sumo sacerdote que não possa compadecer-se das nossas fraquezas.", "Hb 4:15",
        intro("Hebreus 4 continua o aviso sobre o descanso de Deus e apresenta Cristo como o Sumo Sacerdote que nos convida a nos aproximar com confiança.") +
        bloco("🕊️ O Descanso de Deus (4:1-11)", [
            ("Hb 4:9-11", "Portanto, resta ainda um descanso para o povo de Deus. Porque aquele que entrou no seu descanso também ele descansou das suas obras, como Deus das suas. Esforcemo-nos, pois, por entrar naquele descanso.",
             "O 'descanso' (<em>sabbatismos</em>) de Deus é mais do que o Sábado ou Canaã — é a participação na vida de Deus. Os israelitas no deserto não entraram por incredulidade. O descanso ainda está disponível — 'hoje' é o dia de entrar.")
        ]) +
        bloco("⚔️ A Palavra de Deus e o Sumo Sacerdote (4:12-16)", [
            ("Hb 4:12-13", "Porque a palavra de Deus é viva e eficaz, e mais cortante do que qualquer espada de dois gumes, e penetra até ao ponto de dividir a alma e o espírito, as juntas e os tutanos, e é apta para discernir os pensamentos e intenções do coração.",
             "A Palavra de Deus como cirurgião espiritual: viva (<em>zosa</em>), eficaz (<em>energes</em>), cortante (<em>tomoteros</em>). Penetra além da superfície até o mais profundo da pessoa — discernindo pensamentos e intenções. Nada está escondido diante de Deus."),
            ("Hb 4:15-16", "Porque não temos sumo sacerdote que não possa compadecer-se das nossas fraquezas; antes, foi tentado em tudo como nós, mas sem pecado. Chegue-nos, pois, com confiança ao trono da graça, para que alcancemos misericórdia e achemos graça, a fim de sermos ajudados em tempo oportuno.",
             "A humanidade de Cristo é fundamento da nossa oração confiante. Cristo foi tentado em tudo (<em>kata panta kath homoioteta</em>) como nós — exceto o pecado. A tentação sem pecado é mais intensa, não menos — Cristo suportou a pressão total que nós aliviamos cedendo. Por isso pode compadecer-se.")
        ])),
    5: ("O Sumo Sacerdote Segundo a Ordem de Melquisedeque", "Tu és sacerdote para sempre, segundo a ordem de Melquisedeque.", "Hb 5:6",
        intro("Hebreus 5 desenvolve o sacerdócio de Cristo segundo a ordem de Melquisedeque — superior ao sacerdócio aarônico — e inclui o terceiro aviso: contra a imaturidade espiritual.") +
        bloco("👑 O Sacerdócio de Cristo (5:1-10)", [
            ("Hb 5:7-9", "O qual, nos dias da sua carne, oferecendo, com grande clamor e lágrimas, orações e súplicas àquele que o podia salvar da morte, foi ouvido por causa da sua reverência; e, ainda que era Filho, aprendeu a obediência por aquilo que padeceu; e, sendo consumado, veio a ser o autor da salvação eterna para todos os que lhe obedecem.",
             "A humanidade plena de Cristo: 'grande clamor e lágrimas' — a agonia de Getsêmani. Cristo aprendeu (<em>emathen</em>) a obediência — não que fosse desobediente, mas que a obediência foi provada e aprofundada no sofrimento. A consumação (<em>teleiotheis</em>) é a qualificação sacerdotal pela experiência do sofrimento.")
        ])),
    6: ("Avançar para a Maturidade", "Por isso, deixando os princípios elementares da doutrina de Cristo, avancemos para o que é perfeito.", "Hb 6:1",
        intro("Hebreus 6 contém o terceiro aviso — o mais severo da carta — sobre a impossibilidade de renovar ao arrependimento os que apostataram, e a âncora da esperança em Cristo.") +
        bloco("⚠️ Terceiro Aviso: A Apostasia (6:4-8)", [
            ("Hb 6:4-6", "Porque é impossível que os que foram uma vez iluminados, e provaram o dom celestial, e foram feitos participantes do Espírito Santo, e provaram a boa palavra de Deus e os poderes do século vindouro, e caíram, sejam outra vez renovados para arrependimento.",
             "O texto mais debatido de Hebreus. Os cinco privilégios dos que caem: iluminados, provaram o dom celestial, participantes do Espírito, provaram a Palavra, provaram os poderes do século vindouro. A impossibilidade de renovação: não porque Deus não perdoa, mas porque quem apostata crucifica Cristo novamente — rejeição consciente e definitiva.")
        ]) +
        bloco("⚓ A Âncora da Esperança (6:13-20)", [
            ("Hb 6:18-20", "Para que, por duas coisas imutáveis, nas quais é impossível que Deus minta, tenhamos um forte encorajamento, nós que nos refugiamos para lançar mão da esperança proposta; a qual temos como âncora da alma, segura e firme, e que penetra até ao interior do véu.",
             "Duas coisas imutáveis: a promessa e o juramento de Deus. A esperança como âncora (<em>agkyran</em>) — metáfora náutica: a âncora penetra o véu (o Santo dos Santos celestial) onde Cristo entrou como precursor. Nossa esperança está ancorada no próprio trono de Deus.")
        ])),
    7: ("Melquisedeque e o Sacerdócio Eterno", "Tu és sacerdote para sempre, segundo a ordem de Melquisedeque.", "Hb 7:17",
        intro("Hebreus 7 é o capítulo mais elaborado sobre Melquisedeque — o sacerdote-rei de Salém que prefigura o sacerdócio eterno de Cristo.") +
        bloco("👑 Melquisedeque (7:1-10)", [
            ("Hb 7:1-3", "Porque este Melquisedeque, rei de Salém, sacerdote do Deus Altíssimo, que saiu ao encontro de Abraão quando este voltava da derrota dos reis, e o abençoou; a quem também Abraão deu o dízimo de tudo; o qual é primeiramente, pela interpretação, rei de justiça, e depois também rei de Salém, que é rei de paz; sem pai, sem mãe, sem genealogia, não tendo começo de dias nem fim de vida, mas assemelhado ao Filho de Deus, permanece sacerdote para sempre.",
             "Melquisedeque (Gn 14) é apresentado como tipo de Cristo: (1) rei de justiça e paz; (2) sem genealogia registrada — tipo do eterno; (3) recebeu dízimo de Abraão — superior ao sacerdócio levítico que descende de Abraão. O argumento: se Abraão pagou dízimo a Melquisedeque, o sacerdócio de Melquisedeque é superior ao levítico.")
        ]) +
        bloco("⭐ O Sacerdócio Eterno de Cristo (7:23-28)", [
            ("Hb 7:24-25", "Mas este, porque permanece para sempre, tem um sacerdócio imutável; pelo que também pode salvar perfeitamente os que por ele se chegam a Deus, vivendo sempre para interceder por eles.",
             "A superioridade do sacerdócio de Cristo: (1) eterno — não passa para outro; (2) salva 'perfeitamente' (<em>eis to panteles</em>) — completamente, para sempre; (3) intercede continuamente. A intercessão presente de Cristo é a garantia da perseverança dos crentes.")
        ])),
    8: ("A Nova Aliança", "Eis que dias virão, diz o Senhor, em que estabelecerei nova aliança com a casa de Israel.", "Hb 8:8",
        intro("Hebreus 8 apresenta Cristo como o Sumo Sacerdote da Nova Aliança — superior à Antiga porque baseada em promessas melhores.") +
        bloco("📜 A Nova Aliança (8:6-13)", [
            ("Hb 8:10-12", "Porque esta é a aliança que farei com a casa de Israel, depois daqueles dias, diz o Senhor: Porei as minhas leis no seu entendimento, e as escreverei no seu coração; e eu serei o seu Deus, e eles serão o meu povo. E não ensinará cada um ao seu próximo, e cada um ao seu irmão, dizendo: Conhece ao Senhor; porque todos me conhecerão, desde o menor até ao maior deles.",
             "A citação de Jr 31:31-34 — a única vez que o AT usa explicitamente 'nova aliança'. As quatro características da Nova Aliança: (1) lei interiorizada — no coração, não em pedra; (2) relacionamento pessoal — 'eu serei seu Deus'; (3) conhecimento direto de Deus — sem mediação sacerdotal necessária; (4) perdão completo — 'não me lembrarei mais dos seus pecados'.")
        ])),
    9: ("O Sangue de Cristo Purifica a Consciência", "Quanto mais o sangue de Cristo... purificará as vossas consciências das obras mortas.", "Hb 9:14",
        intro("Hebreus 9 compara o tabernáculo terreno com o celestial, e o sangue de animais com o sangue de Cristo — superior porque purifica a consciência, não apenas o corpo.") +
        bloco("🩸 O Sangue de Cristo (9:11-15)", [
            ("Hb 9:11-14", "Mas Cristo, tendo aparecido como sumo sacerdote dos bens futuros, por meio do maior e mais perfeito tabernáculo, não feito por mãos, isto é, não desta criação, e não por sangue de bodes e de bezerros, mas pelo seu próprio sangue, entrou uma vez no santuário, havendo obtido eterna redenção.",
             "O contraste: tabernáculo terreno vs. celestial; sangue de animais vs. sangue de Cristo; redenção temporal vs. eterna. Cristo entrou 'uma vez' (<em>ephapax</em>) — o sacrifício definitivo, nunca a ser repetido. A redenção é eterna (<em>aionion lytrosis</em>)."),
            ("Hb 9:27-28", "E, assim como aos homens está ordenado morrerem uma vez, e depois disso o juízo, assim também Cristo, oferecendo-se uma vez para tirar os pecados de muitos, aparecerá segunda vez, sem pecado, para a salvação dos que o esperam.",
             "O paralelo morte humana / morte de Cristo: ambas acontecem uma vez. A morte de Cristo foi para tirar os pecados; a segunda vinda será para completar a salvação. A certeza do juízo (<em>krisis</em>) é o contexto da urgência do Evangelho.")
        ])),
    10: ("O Sacrifício Definitivo e a Perseverança", "Não abandoneis, pois, a vossa confiança, que tem grande galardão.", "Hb 10:35",
        intro("Hebreus 10 conclui a seção doutrinária com o sacrifício único e definitivo de Cristo, o quarto aviso (contra o abandono da fé), e o chamado à perseverança.") +
        bloco("✝️ O Sacrifício Único (10:1-18)", [
            ("Hb 10:10-14", "Na qual vontade fomos santificados pela oblação do corpo de Jesus Cristo, feita uma vez para sempre. E todo sacerdote se apresenta cada dia ministrando e oferecendo muitas vezes os mesmos sacrifícios, que nunca podem tirar os pecados. Mas este, havendo oferecido para sempre um único sacrifício pelos pecados, assentou-se à destra de Deus.",
             "O contraste definitivo: os sacerdotes ficam de pé (trabalho nunca terminado), Cristo se assentou (obra consumada). 'Uma vez para sempre' (<em>ephapax</em>) — a suficiência absoluta do sacrifício de Cristo. Ele não precisa ser repetido — nem na missa, nem em nenhum outro rito.")
        ]) +
        bloco("⚠️ Quarto Aviso: Não Abandonar (10:26-31)", [
            ("Hb 10:26-27", "Porque, se pecarmos voluntariamente depois de termos recebido o conhecimento da verdade, já não resta sacrifício pelos pecados, mas uma horrível expectação de juízo, e ardor de fogo que há de consumir os adversários.",
             "O quarto aviso: pecar 'voluntariamente' (<em>hekousios</em>) após receber o conhecimento da verdade — apostasia deliberada. Não há mais sacrifício disponível porque o único sacrifício foi rejeitado. A gravidade é proporcional ao privilégio recebido.")
        ])),
    11: ("A Galeria da Fé", "Ora, a fé é o firme fundamento das coisas que se esperam, e a prova das coisas que se não veem.", "Hb 11:1",
        intro("Hebreus 11 é o capítulo mais famoso da carta — a 'galeria da fé', uma lista de heróis do AT que viveram pela fé antes de ver o cumprimento das promessas.") +
        bloco("🌟 A Definição e os Heróis da Fé (11:1-40)", [
            ("Hb 11:1-3", "Ora, a fé é o firme fundamento das coisas que se esperam, e a prova das coisas que se não veem. Porque por ela os anciãos alcançaram bom testemunho. Pela fé entendemos que os mundos foram criados pela palavra de Deus, de modo que o visível não foi feito do que se vê.",
             "<em>Hypostasis</em> — fundamento/substância: a fé dá realidade presente ao que ainda é futuro. <em>Elenchos</em> — prova/convicção: a fé é evidência do invisível. A fé não é crença sem evidência — é confiança baseada no caráter de Deus, que dá certeza ao que ainda não é visto."),
            ("Hb 11:13-16", "Todos estes morreram na fé, sem ter recebido as promessas; mas vendo-as de longe, e crendo nelas, e as saudando, e confessando que eram estrangeiros e peregrinos sobre a terra... Mas agora desejam uma pátria melhor, isto é, a celestial.",
             "O paradoxo da fé: todos morreram sem receber as promessas. A fé não é garantia de cumprimento imediato — é visão de longo alcance. Os heróis da fé eram 'estrangeiros e peregrinos' (<em>xenoi kai parepidemos</em>) — não pertenciam ao mundo presente. Sua pátria era celestial.")
        ])),
    12: ("A Disciplina de Deus e a Cidade Celestial", "Corramos com perseverança a carreira que nos está proposta, olhando para Jesus.", "Hb 12:1-2",
        intro("Hebreus 12 usa a galeria da fé como motivação para a corrida cristã, ensina sobre a disciplina de Deus como amor paternal, e apresenta o quinto aviso: não recusar ao que fala.") +
        bloco("🏃 A Corrida da Fé (12:1-3)", [
            ("Hb 12:1-2", "Portanto, também nós, pois que estamos rodeados de tão grande nuvem de testemunhas, deixemos todo o embaraço e o pecado que nos rodeia, e corramos com perseverança a carreira que nos está proposta, olhando para Jesus, autor e consumador da fé.",
             "A metáfora do estádio: os heróis do cap. 11 são a 'nuvem de testemunhas' (<em>nephos martyron</em>) nas arquibancadas. A corrida requer: (1) largar o peso (<em>ogkon</em>); (2) largar o pecado que envolve; (3) perseverança (<em>hypomone</em>); (4) olhar para Jesus. Jesus é o <em>archegos</em> (pioneiro) e <em>teleiotes</em> (consumador) da fé.")
        ]) +
        bloco("💙 A Disciplina como Amor (12:5-11)", [
            ("Hb 12:10-11", "Porque eles nos disciplinavam por poucos dias, segundo o que lhes parecia; mas Deus nos disciplina para o nosso proveito, para que participemos da sua santidade. Ora, toda a disciplina parece no momento ser causa de tristeza, e não de alegria; mas depois produz um fruto pacífico de justiça para os que por ela foram exercitados.",
             "A disciplina divina (<em>paideia</em>) é prova de filiação, não de abandono. O pai que não disciplina não ama. O fruto da disciplina: participação na santidade de Deus, fruto pacífico de justiça. A dor presente é temporária; o fruto é eterno.")
        ])),
    13: ("Amor Fraternal e a Cidade Futura", "Jesus Cristo é o mesmo, ontem, e hoje, e eternamente.", "Hb 13:8",
        intro("Hebreus 13 encerra com exortações práticas para a vida comunitária e a declaração final da imutabilidade de Cristo.") +
        bloco("💙 Exortações Finais (13:1-17)", [
            ("Hb 13:1-3", "Persevere o amor fraternal. Não vos esqueçais da hospitalidade, porque por ela alguns, sem o saber, hospedaram anjos. Lembrai-vos dos presos, como se estivésseis presos com eles; e dos maltratados, como que estando vós mesmos no corpo.",
             "A ética de Hebreus: amor fraternal (<em>philadelphia</em>), hospitalidade (<em>philoxenia</em> — amor ao estranho), solidariedade com os presos e maltratados. A hospitalidade pode ser encontro com anjos — alusão a Abraão (Gn 18) e Ló (Gn 19)."),
            ("Hb 13:8", "Jesus Cristo é o mesmo, ontem, e hoje, e eternamente.",
             "O versículo mais memorável de Hebreus. Em contraste com os líderes que passam (13:7), Cristo é imutável. <em>Autos kai chthes kai semeron ho autos kai eis tous aionas</em>. A imutabilidade de Cristo é fundamento da fé: o que ele foi, é; o que é, será. Não há evolução, revisão ou obsolescência em Cristo.")
        ])),
}

def gerar_hebreus():
    for num, (titulo, vk, rk, body) in caps_hebreus.items():
        html = page("Hebreus", num, 13, titulo, vk, rk, body, "hebreus", "../../../..")
        salvar("hebreus", num, html)
    print("✅ Hebreus: 13 capítulos gerados")

if __name__ == "__main__":
    gerar_1timoteo()
    gerar_2timoteo()
    gerar_tito()
    gerar_filemom()
    gerar_hebreus()
    print("\n🎉 Fase 3 concluída: 1-2Tim + Tito + Filemom + Hebreus = 27 capítulos aprofundados")
