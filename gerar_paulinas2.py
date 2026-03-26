#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera capítulos aprofundados:
2Cor (13), Gálatas (6), Efésios (6), Filipenses (4),
Colossenses (4), 1Ts (5), 2Ts (3) = 41 capítulos
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
    pl = f"← {livro} {num-1}" if num > 1 else "← Índice"
    nl = f"{livro} {num+1} →" if num < total else "Índice →"
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
    <a href="{prev}">{pl}</a>
    <a href="../index.html">Índice de {livro}</a>
    <a href="{nxt}">{nl}</a>
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

# ─── 2 CORÍNTIOS ───────────────────────────────────────────────────────────────
caps_2cor = {
    1: ("Consolação no Sofrimento", "Bendito seja o Deus e Pai de nosso Senhor Jesus Cristo, o Pai das misericórdias e o Deus de toda a consolação.", "2Cor 1:3",
        intro("2 Coríntios é a carta mais pessoal e autobiográfica de Paulo. Escrita ~56 d.C. após uma crise dolorosa com a Igreja. O cap. 1 apresenta a teologia do sofrimento e da consolação.") +
        bloco("💙 O Deus de Toda Consolação (1:3-11)", [
            ("2Cor 1:3-5", "Bendito seja o Deus e Pai de nosso Senhor Jesus Cristo, o Pai das misericórdias e o Deus de toda a consolação, que nos consola em toda a nossa tribulação, para que também possamos consolar os que estiverem em alguma tribulação.",
             "A teologia da consolação: Deus é <em>ho theos pases parakleseos</em> — o Deus de toda consolação. A consolação recebida no sofrimento é passada adiante. O sofrimento de Paulo não é desperdício — é escola de consolação para o ministério."),
            ("2Cor 1:8-10", "Porque não queremos que ignoreis, irmãos, a tribulação que nos sobreveio na Ásia; pois fomos sobremaneira oprimidos... de modo que duvidávamos até da nossa vida. Mas tínhamos em nós mesmos a sentença de morte, para que não confiássemos em nós mesmos, mas em Deus que ressuscita os mortos.",
             "Paulo descreve uma crise de vida ou morte na Ásia (provavelmente Éfeso). O propósito divino: aprender a não confiar em si mesmo, mas em Deus que ressuscita os mortos. O sofrimento extremo é escola de fé radical.")
        ])),
    2: ("O Aroma de Cristo", "Mas graças a Deus, que sempre nos faz triunfar em Cristo, e que por nós manifesta em todo lugar o aroma do seu conhecimento.", "2Cor 2:14",
        intro("2 Coríntios 2 trata da reconciliação com o membro disciplinado (1Cor 5) e apresenta a metáfora do triunfo romano e do aroma de Cristo.") +
        bloco("🌸 O Aroma de Cristo (2:14-17)", [
            ("2Cor 2:14-16", "Mas graças a Deus, que sempre nos faz triunfar em Cristo, e que por nós manifesta em todo lugar o aroma do seu conhecimento. Porque para Deus somos o bom aroma de Cristo, tanto nos que se salvam como nos que se perdem.",
             "A metáfora do triunfo romano (<em>thriambeuo</em>): o general vitorioso desfilava com prisioneiros e incenso. Para uns, o aroma era de vida; para os prisioneiros, de morte. O Evangelho tem o mesmo efeito duplo: para os que creem, aroma de vida; para os que rejeitam, aroma de morte.")
        ])),
    3: ("Ministros da Nova Aliança", "Mas o Senhor é o Espírito; e onde está o Espírito do Senhor, aí há liberdade.", "2Cor 3:17",
        intro("2 Coríntios 3 contrasta os ministérios da Antiga e Nova Aliança — letras de pedra vs. letras do Espírito, glória que passa vs. glória que permanece.") +
        bloco("📜 Antiga vs. Nova Aliança (3:6-18)", [
            ("2Cor 3:6-8", "O qual nos habilitou para sermos ministros de uma nova aliança, não da letra, mas do espírito; porque a letra mata, mas o espírito vivifica.",
             "A antítese letra/espírito não é AT/NT em geral — é lei como exigência externa vs. Espírito como transformação interna. A lei mata porque revela o pecado sem prover poder para obedecer; o Espírito vivifica porque transforma de dentro."),
            ("2Cor 3:17-18", "Mas o Senhor é o Espírito; e onde está o Espírito do Senhor, aí há liberdade. E todos nós, com o rosto descoberto, contemplando como por espelho a glória do Senhor, somos transformados de glória em glória na mesma imagem.",
             "A transformação progressiva: <em>metamorphoumetha apo doxes eis doxan</em> — de glória em glória. O agente é o Espírito. A contemplação de Cristo transforma — a santificação é essencialmente contemplativa.")
        ])),
    4: ("Tesouros em Vasos de Barro", "Trazemos, porém, este tesouro em vasos de barro, para que a excelência do poder seja de Deus, e não de nós.", "2Cor 4:7",
        intro("2 Coríntios 4 é uma das passagens mais profundas sobre o ministério cristão — o tesouro do Evangelho em vasos de barro, e a teologia da fraqueza como veículo do poder divino.") +
        bloco("🏺 Vasos de Barro (4:7-18)", [
            ("2Cor 4:7-10", "Trazemos, porém, este tesouro em vasos de barro, para que a excelência do poder seja de Deus, e não de nós. Em tudo somos atribulados, mas não angustiados; perplexos, mas não desesperados; perseguidos, mas não desamparados; abatidos, mas não destruídos.",
             "O contraste tesouro/vaso de barro é deliberado: Deus coloca o Evangelho em instrumentos frágeis para que ninguém atribua o poder ao instrumento. Os quatro pares de paradoxos descrevem a vida apostólica: pressão sem esmagamento, perplexidade sem desespero, perseguição sem abandono, abatimento sem destruição."),
            ("2Cor 4:16-18", "Por isso não desfalecemos; mas, ainda que o nosso homem exterior se corrompa, o interior, contudo, se renova de dia em dia. Porque a nossa leve e momentânea tribulação produz para nós um peso eterno de glória acima de toda medida.",
             "A perspectiva eterna transforma o sofrimento presente: as tribulações são 'leves' (<em>elaphron</em>) e 'momentâneas' (<em>parautika</em>) comparadas ao 'peso eterno de glória' (<em>baros aionion doxes</em>). A fé olha para o invisível eterno, não para o visível temporário.")
        ])),
    5: ("A Nova Criação e o Ministério da Reconciliação", "Assim que, se alguém está em Cristo, nova criatura é; as coisas velhas já passaram; eis que tudo se fez novo.", "2Cor 5:17",
        intro("2 Coríntios 5 apresenta a esperança da ressurreição, a motivação do amor de Cristo, a nova criação em Cristo, e o ministério da reconciliação como embaixada divina.") +
        bloco("🌟 Nova Criação em Cristo (5:14-21)", [
            ("2Cor 5:17", "Assim que, se alguém está em Cristo, nova criatura é; as coisas velhas já passaram; eis que tudo se fez novo.",
             "<em>Kaine ktisis</em> — nova criação: não apenas reforma do antigo, mas criação nova. O crente em Cristo participa da nova criação inaugurada pela ressurreição de Cristo. As 'coisas velhas' (<em>ta archaia</em>) — o status antigo de inimigo de Deus, a vida sob o pecado — passaram."),
            ("2Cor 5:18-21", "E tudo isso provém de Deus, que nos reconciliou consigo mesmo por Jesus Cristo, e nos deu o ministério da reconciliação... Como se Deus rogasse por nosso intermédio, nós vos rogamos da parte de Cristo: Reconciliai-vos com Deus.",
             "O ministério da reconciliação (<em>diakonia tes katallages</em>): Deus iniciou a reconciliação em Cristo; nós somos embaixadores (<em>presbytereuo</em>) que comunicam a oferta. O versículo 21 é o coração da expiação substitutiva: 'Aquele que não conheceu pecado, o fez pecado por nós, para que nele nos tornássemos justiça de Deus.'")
        ])),
    6: ("O Ministério Aprovado no Sofrimento", "Eis agora o tempo aceitável; eis agora o dia da salvação.", "2Cor 6:2",
        intro("2 Coríntios 6 descreve o ministério apostólico como aprovado no sofrimento, e chama os coríntios à separação do mundo.") +
        bloco("⚡ O Ministério no Sofrimento (6:3-10)", [
            ("2Cor 6:4-10", "Antes, em tudo nos recomendamos como ministros de Deus: em muita paciência, em aflições, em necessidades, em angústias... como tristes, mas sempre alegres; como pobres, mas enriquecendo a muitos; como nada tendo, e possuindo tudo.",
             "A lista de 27 paradoxos do ministério apostólico. Os últimos quatro são os mais profundos: triste/alegre, pobre/enriquecendo, nada tendo/possuindo tudo. O ministério cristão é definido por paradoxos que só fazem sentido à luz da ressurreição.")
        ])),
    7: ("A Tristeza Segundo Deus", "Porque a tristeza segundo Deus produz arrependimento para a salvação, de que ninguém se arrepende.", "2Cor 7:10",
        intro("2 Coríntios 7 relata o alívio de Paulo ao receber boas notícias de Corinto por Tito, e ensina a distinção crucial entre tristeza segundo Deus e tristeza do mundo.") +
        bloco("💙 Tristeza Segundo Deus vs. Tristeza do Mundo (7:8-13)", [
            ("2Cor 7:10-11", "Porque a tristeza segundo Deus produz arrependimento para a salvação, de que ninguém se arrepende; mas a tristeza do mundo produz morte. Porque eis que isto mesmo, o serdes contristados segundo Deus, quanto cuidado não produziu em vós!",
             "A distinção fundamental: a tristeza segundo Deus (<em>kata theon lype</em>) leva ao arrependimento (<em>metanoia</em>) e à salvação; a tristeza do mundo (<em>tou kosmou lype</em>) leva à morte. A tristeza segundo Deus é produtiva — produz cuidado, defesa, indignação, temor, saudade, zelo, punição.")
        ])),
    8: ("A Graça da Generosidade", "Porque conheceis a graça de nosso Senhor Jesus Cristo, que, sendo rico, se fez pobre por amor de vós.", "2Cor 8:9",
        intro("2 Coríntios 8-9 é o ensino mais extenso do NT sobre generosidade cristã. O cap. 8 usa o exemplo das igrejas da Macedônia e de Cristo como motivação para a oferta.") +
        bloco("💰 A Generosidade Macedônia e o Exemplo de Cristo (8:1-15)", [
            ("2Cor 8:1-5", "Também vos fazemos saber, irmãos, a graça de Deus que foi dada às igrejas da Macedônia; como em muita prova de tribulação, a abundância do seu gozo e a sua profunda pobreza abundaram em riquezas da sua generosidade.",
             "As igrejas macedônias (Filipos, Tessalônica, Bereia) deram generosamente apesar da pobreza extrema. O paradoxo: pobreza profunda + alegria abundante = generosidade rica. A generosidade não é função da riqueza — é função da graça."),
            ("2Cor 8:9", "Porque conheceis a graça de nosso Senhor Jesus Cristo, que, sendo rico, se fez pobre por amor de vós, para que pela sua pobreza vós fosseis enriquecidos.",
             "O fundamento teológico da generosidade: a encarnação de Cristo. Ele era rico (<em>plousios</em>) — possuía toda a glória divina — e se fez pobre (<em>ptochos</em>) — assumiu a condição humana e a morte. Nossa generosidade é resposta à generosidade de Cristo.")
        ])),
    9: ("Deus Ama o Doador Alegre", "Deus ama ao que dá com alegria.", "2Cor 9:7",
        intro("2 Coríntios 9 continua o ensino sobre a oferta com os princípios da semeadura e da colheita, e a promessa de que Deus provê para os generosos.") +
        bloco("🌱 Semeadura e Colheita (9:6-15)", [
            ("2Cor 9:6-8", "Mas isto digo: o que semeia pouco, pouco também ceifará; e o que semeia em abundância, em abundância também ceifará. Cada um contribua segundo propôs no seu coração, não com tristeza ou por necessidade; porque Deus ama ao que dá com alegria.",
             "O princípio da semeadura: a generosidade é investimento, não perda. 'Deus ama ao que dá com alegria' (<em>hilaron doten agapa ho theos</em>) — <em>hilaron</em> é a raiz de 'hilário'. A oferta forçada ou ressentida não agrada a Deus."),
            ("2Cor 9:10-11", "E o que dá semente ao semeador, e pão para comer, também multiplicará a vossa semeadura, e aumentará os frutos da vossa justiça; para que em tudo sejais enriquecidos para toda a generosidade.",
             "Deus provê para os generosos não para que acumulem, mas para que sejam mais generosos. O enriquecimento divino tem propósito: <em>eis pasan haploteta</em> — para toda generosidade.")
        ])),
    10: ("A Autoridade Apostólica", "Porque as armas da nossa milícia não são carnais, mas sim poderosas em Deus para destruição de fortalezas.", "2Cor 10:4",
        intro("2 Coríntios 10-13 é a 'carta das lágrimas' — Paulo defende seu apostolado contra os 'super-apóstolos'. O cap. 10 apresenta a natureza espiritual da guerra apostólica.") +
        bloco("⚔️ Armas Espirituais (10:3-6)", [
            ("2Cor 10:3-5", "Porque, ainda que andemos na carne, não militamos segundo a carne. Porque as armas da nossa milícia não são carnais, mas sim poderosas em Deus para destruição de fortalezas; destruindo os argumentos e toda a altivez que se levanta contra o conhecimento de Deus.",
             "A guerra espiritual não é contra pessoas — é contra 'fortalezas' (<em>ochyromata</em>), 'argumentos' (<em>logismous</em>) e 'altivez' (<em>hypsoma</em>). As fortalezas são sistemas de pensamento que se opõem ao conhecimento de Deus. As armas espirituais (oração, Palavra, proclamação) derrubam o que as armas carnais não podem tocar.")
        ])),
    11: ("O Apóstolo e os Falsos Apóstolos", "Porque esses são falsos apóstolos, obreiros fraudulentos, que se transfiguram em apóstolos de Cristo.", "2Cor 11:13",
        intro("2 Coríntios 11 é a 'loucura' de Paulo — ele se compara aos falsos apóstolos, mas sua 'glória' é o sofrimento pelo Evangelho.") +
        bloco("😤 A Loucura de Paulo (11:16-33)", [
            ("2Cor 11:23-27", "São ministros de Cristo? (falo como louco) Eu ainda mais: em trabalhos muito mais; em açoites sem número; em prisões muito mais; em perigos de morte muitas vezes. Cinco vezes recebi dos judeus quarenta açoites menos um.",
             "A lista de sofrimentos de Paulo é o currículo apostólico mais impressionante do NT: 5 vezes 39 açoites, 3 vezes varas, 1 vez apedrejado, 3 naufrágios, 1 noite e dia no mar, perigos de rios, de ladrões, de compatriotas, de gentios, na cidade, no deserto, no mar, entre falsos irmãos. Este é o 'sucesso' apostólico segundo Deus.")
        ])),
    12: ("O Espinho na Carne e a Graça Suficiente", "A minha graça te basta, porque o meu poder se aperfeiçoa na fraqueza.", "2Cor 12:9",
        intro("2 Coríntios 12 relata a visão do terceiro céu e o espinho na carne — a fraqueza que se torna veículo do poder de Deus.") +
        bloco("🌟 O Terceiro Céu e o Espinho (12:1-10)", [
            ("2Cor 12:2-4", "Conheço um homem em Cristo que, há catorze anos... foi arrebatado até ao terceiro céu. E sei que tal homem... foi arrebatado ao paraíso, e ouviu palavras inefáveis, que ao homem não é lícito falar.",
             "Paulo fala de si mesmo na terceira pessoa. O 'terceiro céu' / 'paraíso' é a presença imediata de Deus. A experiência é inefável — não pode ser comunicada. Paulo não usa isso para se promover — usa para justificar o espinho que veio depois."),
            ("2Cor 12:7-10", "E, para que eu não me exaltasse pela excelência das revelações, foi-me dado um espinho na carne, um mensageiro de Satanás para me esbofetear... E disse-me: A minha graça te basta, porque o meu poder se aperfeiçoa na fraqueza.",
             "O espinho (<em>skolops te sarki</em>) — identidade debatida (doença ocular, epilepsia, oposição humana). O que importa: foi dado para prevenir o orgulho, é instrumento de Satanás mas sob controle de Deus, e Deus respondeu não removendo mas provendo graça suficiente. <em>Arkei soi he charis mou</em> — a graça é suficiente.")
        ])),
    13: ("Exame Final e Bênção Apostólica", "A graça do Senhor Jesus Cristo, e o amor de Deus, e a comunhão do Espírito Santo seja com todos vós.", "2Cor 13:14",
        intro("2 Coríntios 13 encerra com um chamado ao autoexame, uma advertência final e a bênção trinitária mais completa do NT.") +
        bloco("🔍 Exame e Bênção Final (13:5-14)", [
            ("2Cor 13:5", "Examinai-vos a vós mesmos, se estais na fé; provai-vos a vós mesmos. Ou não reconheceis que Jesus Cristo está em vós? a menos que sejais reprovados.",
             "<em>Heautous peirazete</em> — examinai-vos: o autoexame é responsabilidade do crente. O critério: Cristo está em mim? A presença de Cristo é a evidência da fé genuína."),
            ("2Cor 13:14", "A graça do Senhor Jesus Cristo, e o amor de Deus, e a comunhão do Espírito Santo seja com todos vós. Amém.",
             "A bênção apostólica trinitária mais completa do NT. Cada pessoa da Trindade com seu atributo distintivo: Cristo — graça (<em>charis</em>); Pai — amor (<em>agape</em>); Espírito — comunhão (<em>koinonia</em>). Usada até hoje como bênção final no culto cristão.")
        ])),
}

def gerar_2corintios():
    for num, (titulo, vk, rk, body) in caps_2cor.items():
        html = page("2 Coríntios", num, 13, titulo, vk, rk, body, "2corintios", "../../../..")
        salvar("2corintios", num, html)
    print("✅ 2 Coríntios: 13 capítulos gerados")

# ─── GÁLATAS ───────────────────────────────────────────────────────────────────
caps_galatas = {
    1: ("Outro Evangelho Não Há", "Mas, ainda que nós ou um anjo do céu vos anuncie outro evangelho além do que já vos anunciamos, seja anátema.", "Gl 1:8",
        intro("Gálatas é a Magna Carta da liberdade cristã. Escrita ~48-49 d.C. (a mais antiga carta de Paulo), é a defesa mais apaixonada do Evangelho da graça contra o legalismo judaizante.") +
        bloco("🔥 A Defesa do Evangelho (1:6-10)", [
            ("Gl 1:6-9", "Maravilho-me de que tão depressa vos tenhais desviado daquele que vos chamou pela graça de Cristo, para outro evangelho... Mas, ainda que nós ou um anjo do céu vos anuncie outro evangelho além do que já vos anunciamos, seja anátema.",
             "A abertura mais abrupta de todas as cartas de Paulo — sem ação de graças. A urgência é extrema: os gálatas estão abandonando o Evangelho. O duplo <em>anathema</em> (maldição) sobre qualquer um que pregue outro evangelho — incluindo Paulo mesmo ou um anjo — demonstra que o Evangelho não é negociável.")
        ]) +
        bloco("📖 O Evangelho Recebido por Revelação (1:11-24)", [
            ("Gl 1:11-12", "Mas faço-vos saber, irmãos, que o evangelho por mim anunciado não é segundo o homem; porque não o recebi nem aprendi de homem algum, mas pela revelação de Jesus Cristo.",
             "Paulo defende a origem divina de seu Evangelho — não recebido de outros apóstolos, mas por revelação direta de Cristo. Sua conversão e chamado independentes confirmam a autoridade apostólica.")
        ])),
    2: ("A Verdade do Evangelho em Antioquia", "Fui crucificado com Cristo; e vivo, não mais eu, mas Cristo vive em mim.", "Gl 2:20",
        intro("Gálatas 2 relata o confronto de Paulo com Pedro em Antioquia — o episódio mais dramático de conflito apostólico no NT — e apresenta a justificação pela fé em sua forma mais concisa.") +
        bloco("⚔️ Paulo Confronta Pedro (2:11-14)", [
            ("Gl 2:11-14", "Quando, porém, Cefas veio a Antioquia, resisti-lhe na face, porque era repreensível... Mas, quando vi que não andavam com retidão, conforme a verdade do evangelho, disse a Cefas na presença de todos...",
             "O confronto de Paulo com Pedro é o episódio mais dramático de conflito apostólico no NT. Pedro, por medo dos judaizantes, se separava dos gentios — negando na prática o que confessava na teologia. A hipocrisia de Pedro era teologicamente fatal: implicava que os gentios precisavam da lei para ser aceitos.")
        ]) +
        bloco("⭐ Justificação pela Fé (2:15-21)", [
            ("Gl 2:16", "Sabendo, todavia, que o homem não é justificado pelas obras da lei, mas pela fé em Jesus Cristo, nós também cremos em Cristo Jesus, para sermos justificados pela fé de Cristo e não pelas obras da lei; pois pelas obras da lei nenhuma carne será justificada.",
             "A tese central de Gálatas: justificação pela fé em Cristo, não pelas obras da lei. Repetida três vezes em um versículo para ênfase. <em>Erga nomou</em> — obras da lei: não apenas obras meritórias, mas toda a prática da lei mosaica como sistema de acesso a Deus."),
            ("Gl 2:20", "Fui crucificado com Cristo; e vivo, não mais eu, mas Cristo vive em mim; e a vida que agora vivo na carne, vivo-a na fé do Filho de Deus, o qual me amou e se entregou a si mesmo por mim.",
             "O versículo mais autobiográfico de Paulo. A vida cristã é definida por: (1) co-crucificação com Cristo — morte do eu autônomo; (2) Cristo vivendo em mim — a vida é dele; (3) fé no Filho de Deus; (4) amor pessoal — 'que me amou e se entregou por mim'.")
        ])),
    3: ("A Fé de Abraão e a Maldição da Lei", "Cristo nos resgatou da maldição da lei, fazendo-se maldição por nós.", "Gl 3:13",
        intro("Gálatas 3 é o capítulo mais teológico da carta — Paulo demonstra pela Escritura que a justificação sempre foi pela fé (Abraão), que a lei não anula a promessa, e que Cristo nos redimiu da maldição da lei.") +
        bloco("🌟 Abraão e a Promessa (3:6-18)", [
            ("Gl 3:6-9", "Assim como Abraão creu em Deus, e isso lhe foi imputado como justiça. Sabei, pois, que os que são da fé, esses são filhos de Abraão.",
             "Paulo usa Abraão como prova histórica: a justificação pela fé não é novidade cristã — é o princípio eterno de Deus. Os filhos de Abraão são definidos pela fé, não pela descendência biológica ou pela circuncisão."),
            ("Gl 3:13-14", "Cristo nos resgatou da maldição da lei, fazendo-se maldição por nós; porque está escrito: Maldito todo aquele que for pendurado em madeira; para que a bênção de Abraão chegasse aos gentios em Cristo Jesus.",
             "A expiação substitutiva em sua forma mais direta: Cristo se tornou maldição (<em>katara</em>) para nos resgatar da maldição. A citação de Dt 21:23 (maldito quem for pendurado em madeira) aplicada à crucificação. O propósito: a bênção de Abraão (justificação pela fé) chegasse aos gentios.")
        ]) +
        bloco("📜 A Função da Lei (3:19-29)", [
            ("Gl 3:24-26", "De maneira que a lei nos serviu de aio para nos conduzir a Cristo, a fim de que pela fé fôssemos justificados. Mas, depois que veio a fé, já não estamos debaixo do aio. Porque todos vós sois filhos de Deus pela fé em Cristo Jesus.",
             "<em>Paidagogos</em> — aio (pedagogo): o escravo que acompanhava a criança à escola, não o professor. A lei era temporária, preparatória, condutora a Cristo. Com a vinda de Cristo e da fé, o papel do aio terminou.")
        ])),
    4: ("Filhos, Não Escravos", "Assim, já não és mais escravo, mas filho; e, se filho, também herdeiro de Deus por Cristo.", "Gl 4:7",
        intro("Gálatas 4 aprofunda a metáfora da adoção — de escravos a filhos — e usa a alegoria de Agar e Sara para ilustrar a diferença entre as duas alianças.") +
        bloco("👑 Adoção como Filhos (4:1-7)", [
            ("Gl 4:4-7", "Mas, quando veio a plenitude do tempo, Deus enviou seu Filho, nascido de mulher, nascido sob a lei, para remir os que estavam sob a lei, a fim de recebermos a adoção de filhos. E, porque sois filhos, Deus enviou ao nosso coração o Espírito de seu Filho, que clama: Aba, Pai!",
             "A 'plenitude do tempo' (<em>pleroma tou chronou</em>): o momento histórico preparado por Deus — Pax Romana, língua grega comum, estradas romanas, dispersão judaica. A adoção (<em>hyiothesia</em>) é o resultado da redenção. O Espírito que clama 'Aba, Pai' é a evidência da adoção.")
        ]) +
        bloco("📖 Alegoria de Agar e Sara (4:21-31)", [
            ("Gl 4:22-26", "Porque está escrito que Abraão teve dois filhos: um da escrava e outro da livre. Mas o da escrava nasceu segundo a carne, e o da livre por promessa. O que é alegoria; porque estas mulheres são dois testamentos.",
             "A alegoria: Agar = Monte Sinai = Jerusalém terrena = escravidão da lei; Sara = Jerusalém celestial = liberdade da graça. Isaque nasceu por promessa sobrenatural; os crentes nascem do Espírito. A conclusão: 'Estai, pois, firmes na liberdade com que Cristo nos libertou' (5:1).")
        ])),
    5: ("Liberdade em Cristo e o Fruto do Espírito", "Mas o fruto do Espírito é: amor, alegria, paz, longanimidade, benignidade, bondade, fidelidade, mansidão, temperança.", "Gl 5:22-23",
        intro("Gálatas 5 é o capítulo da liberdade cristã — não liberdade para pecar, mas liberdade para amar. O Espírito produz fruto que a lei nunca pôde produzir.") +
        bloco("🕊️ Liberdade para Amar (5:1-15)", [
            ("Gl 5:1", "Estai, pois, firmes na liberdade com que Cristo nos libertou, e não torneis a sujeitar-vos ao jugo da escravidão.",
             "O imperativo central de Gálatas: permanecer na liberdade que Cristo conquistou. A liberdade cristã não é ausência de compromisso — é libertação do sistema de ganhar aceitação por obras. O 'jugo da escravidão' é a lei como meio de justificação."),
            ("Gl 5:13-14", "Porque vós, irmãos, fostes chamados à liberdade; não useis, porém, a liberdade como ocasião para a carne, mas servi-vos uns aos outros pelo amor. Porque toda a lei se cumpre numa só palavra, nesta: Amarás o teu próximo como a ti mesmo.",
             "A liberdade cristã não é licença — é serviço pelo amor. O paradoxo: somos livres para servir. Toda a lei é cumprida no amor ao próximo — não pela obediência externa à lei, mas pela transformação interna pelo Espírito.")
        ]) +
        bloco("🌸 O Fruto do Espírito (5:16-26)", [
            ("Gl 5:22-23", "Mas o fruto do Espírito é: amor, alegria, paz, longanimidade, benignidade, bondade, fidelidade, mansidão, temperança; contra estas coisas não há lei.",
             "Note: <em>karpos</em> (fruto) é singular — não são 9 frutos separados, mas um fruto com 9 facetas. O fruto é produzido pelo Espírito, não fabricado pelo esforço humano. 'Contra estas coisas não há lei' — o Espírito produz o que a lei exigia mas não podia produzir.")
        ])),
    6: ("Carregar os Fardos e a Nova Criação", "Longe de mim gloriar-me, senão na cruz de nosso Senhor Jesus Cristo.", "Gl 6:14",
        intro("Gálatas 6 conclui com princípios práticos de vida comunitária e a declaração final: o único fundamento de glória é a cruz de Cristo.") +
        bloco("🤝 Carregar os Fardos (6:1-10)", [
            ("Gl 6:1-2", "Irmãos, se algum homem for surpreendido em alguma transgressão, vós, os que sois espirituais, restaurai o tal com espírito de mansidão; olhando por ti mesmo, para que não sejas também tentado. Levai os fardos uns dos outros, e assim cumprireis a lei de Cristo.",
             "A restauração (<em>katartizete</em> — recolocar no lugar, como um osso deslocado) deve ser feita com mansidão e consciência da própria vulnerabilidade. 'A lei de Cristo' é o amor — carregar os fardos uns dos outros é o cumprimento prático do amor."),
            ("Gl 6:7-9", "Não vos enganeis; Deus não se deixa escarnecer; porque tudo o que o homem semear, isso também ceifará... E não nos cansemos de fazer o bem, porque a seu tempo ceifaremos, se não desfalecermos.",
             "O princípio da semeadura e colheita aplicado à vida moral. Semear para a carne produz corrupção; semear para o Espírito produz vida eterna. A exortação à perseverança: 'não nos cansemos' — o cansaço é real, mas a colheita é certa.")
        ]) +
        bloco("✝️ A Cruz como Único Fundamento (6:14-18)", [
            ("Gl 6:14-15", "Longe de mim gloriar-me, senão na cruz de nosso Senhor Jesus Cristo, pela qual o mundo está crucificado para mim, e eu para o mundo. Porque em Cristo Jesus nem a circuncisão nem a incircuncisão têm valor algum, mas sim a nova criação.",
             "A conclusão de toda a carta: a cruz é o único fundamento de glória. Não a circuncisão, não as obras da lei, não o sucesso ministerial. A cruz crucificou o mundo para Paulo e Paulo para o mundo — separação radical de todo sistema de valores mundano. A nova criação (<em>kaine ktisis</em>) é o que importa.")
        ])),
}

def gerar_galatas():
    for num, (titulo, vk, rk, body) in caps_galatas.items():
        html = page("Gálatas", num, 6, titulo, vk, rk, body, "galatas", "../../../..")
        salvar("galatas", num, html)
    print("✅ Gálatas: 6 capítulos gerados")

# ─── EFÉSIOS ───────────────────────────────────────────────────────────────────
caps_efesios = {
    1: ("Bênçãos Espirituais em Cristo", "Bendito seja o Deus e Pai de nosso Senhor Jesus Cristo, que nos abençoou com todas as bênçãos espirituais nos lugares celestiais em Cristo.", "Ef 1:3",
        intro("Efésios é a carta mais elevada de Paulo — a mais rica em teologia da graça, da Igreja e da vida cristã. O cap. 1 é uma doxologia de 12 versículos listando as bênçãos da eleição, redenção e selamento.") +
        bloco("⭐ As Bênçãos da Eleição (1:3-14)", [
            ("Ef 1:3-6", "Bendito seja o Deus e Pai de nosso Senhor Jesus Cristo, que nos abençoou com todas as bênçãos espirituais nos lugares celestiais em Cristo; como também nos elegeu nele antes da fundação do mundo, para sermos santos e irrepreensíveis diante dele em amor.",
             "A 'eulogia' de 1:3-14 é uma única frase em grego — a mais longa do NT. Três estrofes trinitárias: o Pai elege (1:3-6), o Filho redime (1:7-12), o Espírito sela (1:13-14). A eleição (<em>exelexato</em>) é 'antes da fundação do mundo' (<em>pro kataboles kosmou</em>) — não baseada em méritos previstos."),
            ("Ef 1:13-14", "Em quem também vós estais, depois que ouvistes a palavra da verdade, o evangelho da vossa salvação; e, tendo nele também crido, fostes selados com o Espírito Santo da promessa, o qual é o penhor da nossa herança.",
             "O Espírito Santo como <em>arrhabon</em> — penhor, arras, sinal de garantia. O Espírito é o pagamento inicial que garante a herança completa. A sequência: ouvir → crer → ser selado com o Espírito.")
        ]) +
        bloco("🙏 A Oração pela Sabedoria (1:15-23)", [
            ("Ef 1:17-19", "Para que o Deus de nosso Senhor Jesus Cristo, o Pai da glória, vos dê espírito de sabedoria e de revelação no pleno conhecimento dele... e qual a suprema grandeza do seu poder para com nós, os que cremos.",
             "A primeira oração de Paulo em Efésios: três pedidos — (1) espírito de sabedoria e revelação; (2) olhos do coração iluminados para conhecer a esperança do chamado; (3) conhecer a suprema grandeza do poder de Deus. O poder é o mesmo que ressuscitou Cristo e o colocou acima de todo principado.")
        ])),
    2: ("Mortos e Vivificados — Graça pela Fé", "Porque pela graça sois salvos, por meio da fé; e isso não vem de vós; é dom de Deus.", "Ef 2:8",
        intro("Efésios 2 é o capítulo da graça — a descrição mais completa do estado humano sem Cristo e da salvação como obra exclusiva de Deus.") +
        bloco("💀 Mortos em Delitos e Pecados (2:1-3)", [
            ("Ef 2:1-3", "E vos vivificou, estando vós mortos nos vossos delitos e pecados, nos quais andastes outrora, segundo o curso deste século, segundo o príncipe das potestades do ar... entre os quais também todos nós andamos outrora nas concupiscências da nossa carne.",
             "O estado humano sem Cristo: (1) mortos (<em>nekrous</em>) — incapacidade espiritual total; (2) seguindo o curso do século (<em>aion</em>); (3) sob o príncipe do ar (Satanás); (4) filhos da ira por natureza. A morte espiritual não é doença — é morte.")
        ]) +
        bloco("⭐ Graça pela Fé (2:4-10)", [
            ("Ef 2:4-6", "Mas Deus, que é rico em misericórdia, pelo seu muito amor com que nos amou, e estando nós mortos em nossos delitos, nos vivificou juntamente com Cristo (pela graça sois salvos), e nos ressuscitou juntamente com ele, e nos fez assentar nos lugares celestiais em Cristo Jesus.",
             "O 'mas Deus' (<em>ho de theos</em>) é a virada mais dramática da teologia bíblica. Três ações divinas: vivificou, ressuscitou, fez assentar — todas no passado (aoristo), todas 'juntamente com Cristo' (<em>syn</em>-). A posição do crente é 'nos lugares celestiais' — presente, não apenas futura."),
            ("Ef 2:8-10", "Porque pela graça sois salvos, por meio da fé; e isso não vem de vós; é dom de Deus. Não vem das obras, para que ninguém se glorie. Porque somos feitura sua, criados em Cristo Jesus para as boas obras.",
             "O versículo mais claro sobre a graça no NT. A salvação é: (1) pela graça (<em>chariti</em>); (2) por meio da fé (<em>dia pisteos</em>); (3) dom de Deus (<em>theou to doron</em>); (4) não de obras. Mas o v. 10 completa: somos criados para boas obras — a graça não elimina as obras, elimina as obras como meio de salvação.")
        ]) +
        bloco("🏛️ Judeus e Gentios Reconciliados (2:11-22)", [
            ("Ef 2:14-16", "Porque ele é a nossa paz, o qual de ambos fez um, e derrubou a parede de separação que estava no meio, abolindo em sua carne a inimizade... para criar em si mesmo, dos dois, um novo homem, fazendo a paz.",
             "O 'muro de separação' (<em>to mesotoichon tou phragmou</em>) pode aludir ao muro do Templo que separava o átrio dos gentios do átrio de Israel. Cristo derrubou toda barreira étnica, social e religiosa. A Igreja é o 'novo homem' (<em>kainon anthropon</em>) — nova humanidade em Cristo.")
        ])),
    3: ("O Mistério de Cristo e a Oração pela Plenitude", "Para que habiteis pela fé no coração de Cristo; para que, arraigados e fundados em amor...", "Ef 3:17",
        intro("Efésios 3 revela o 'mistério' de Cristo — a inclusão dos gentios como co-herdeiros — e contém a segunda grande oração de Paulo: pela plenitude de Deus.") +
        bloco("🔮 O Mistério Revelado (3:1-13)", [
            ("Ef 3:4-6", "Pelo que, lendo isto, podeis perceber o meu entendimento no mistério de Cristo; o qual noutras gerações não foi dado a conhecer aos filhos dos homens, como agora foi revelado pelo Espírito aos seus santos apóstolos e profetas; a saber, que os gentios são co-herdeiros, e membros do mesmo corpo, e co-participantes da promessa em Cristo Jesus pelo evangelho.",
             "O <em>mysterion</em> de Cristo: não que os gentios seriam salvos (isso o AT já anunciava), mas que seriam <em>co-herdeiros, co-membros, co-participantes</em> — iguais aos judeus em Cristo. Esta igualdade radical era o escândalo do Evangelho para os judeus do século I.")
        ]) +
        bloco("🙏 A Oração pela Plenitude (3:14-21)", [
            ("Ef 3:17-19", "Para que habiteis pela fé no coração de Cristo; para que, arraigados e fundados em amor, possais compreender com todos os santos qual seja a largura, e o comprimento, e a altura, e a profundidade, e conhecer o amor de Cristo, que excede todo o entendimento, para que sejais cheios de toda a plenitude de Deus.",
             "A oração mais abrangente do NT. Paulo pede: (1) fortalecimento interior pelo Espírito; (2) habitação de Cristo no coração; (3) compreensão das dimensões do amor de Cristo; (4) ser cheios de toda a plenitude de Deus (<em>pleroma tou theou</em>). A doxologia final (3:20-21) é o pico da carta: 'Àquele que é poderoso para fazer tudo muito mais abundantemente.'")
        ])),
    4: ("A Unidade do Corpo e o Crescimento em Cristo", "Antes, seguindo a verdade em amor, cresçamos em tudo naquele que é a cabeça, Cristo.", "Ef 4:15",
        intro("Efésios 4 marca a transição da teologia (caps. 1-3) para a ética (caps. 4-6). A vida cristã é andar digno do chamado — em unidade, crescimento e renovação.") +
        bloco("🕊️ A Unidade do Espírito (4:1-16)", [
            ("Ef 4:4-6", "Há um só corpo e um só Espírito, como também fostes chamados em uma só esperança da vossa vocação; um só Senhor, uma só fé, um só batismo; um só Deus e Pai de todos, o qual é sobre todos, e por todos, e em todos.",
             "O credo da unidade cristã: 7 'uns' — corpo, Espírito, esperança, Senhor, fé, batismo, Deus. A unidade não é uniformidade — é diversidade de dons (4:11-12) servindo ao mesmo corpo. Os dons ministeriais (apóstolos, profetas, evangelistas, pastores-mestres) são para equipar os santos para o ministério."),
            ("Ef 4:15-16", "Antes, seguindo a verdade em amor, cresçamos em tudo naquele que é a cabeça, Cristo; do qual todo o corpo, bem ajustado e unido pelo auxílio de todas as juntas, segundo a justa atividade de cada parte, faz o aumento do corpo para a sua edificação em amor.",
             "O crescimento da Igreja é orgânico: cada membro contribui (<em>kata meran energeian</em>) para o crescimento do corpo. A cabeça é Cristo — o crescimento é em direção a ele.")
        ]) +
        bloco("🔄 Renovação da Mente (4:17-32)", [
            ("Ef 4:22-24", "Que, quanto ao trato passado, vos despojeis do velho homem, que se corrompe pelas concupiscências do engano; e vos renoveis no espírito da vossa mente; e vos revistais do novo homem, que segundo Deus é criado em verdadeira justiça e santidade.",
             "O processo da santificação: despir (<em>apothesthai</em>), renovar (<em>ananeousthai</em>), vestir (<em>endysasthai</em>). O 'velho homem' é o eu adâmico; o 'novo homem' é o eu em Cristo. A renovação da mente é o mecanismo da transformação.")
        ])),
    5: ("Filhos da Luz e a Armadura de Deus", "E não vos embriagueis com vinho, em que há contenda, mas enchei-vos do Espírito.", "Ef 5:18",
        intro("Efésios 5 chama os crentes a andar como filhos da luz, e apresenta o modelo do casamento cristão fundamentado no relacionamento de Cristo com a Igreja.") +
        bloco("☀️ Filhos da Luz (5:1-20)", [
            ("Ef 5:8-10", "Porque noutro tempo éreis trevas, mas agora sois luz no Senhor; andai como filhos da luz; (porque o fruto do Espírito está em toda a bondade, e justiça, e verdade;) aprovando o que é agradável ao Senhor.",
             "A transformação ontológica: de trevas (<em>skotos</em>) a luz (<em>phos</em>) — não apenas comportamento, mas natureza. 'Filhos da luz' (<em>tekna photos</em>) é identidade, não apenas instrução."),
            ("Ef 5:18-20", "E não vos embriagueis com vinho, em que há contenda, mas enchei-vos do Espírito; falando entre vós em salmos, e hinos, e cânticos espirituais; cantando e salmodiando ao Senhor no vosso coração.",
             "O contraste embriaguez/plenitude do Espírito: ambos alteram o estado de consciência, mas em direções opostas. A plenitude do Espírito se manifesta em adoração comunitária (salmos, hinos, cânticos), gratidão e submissão mútua.")
        ]) +
        bloco("💍 Casamento e Cristo-Igreja (5:22-33)", [
            ("Ef 5:25-27", "Maridos, amai vossas mulheres, como também Cristo amou a Igreja, e a si mesmo se entregou por ela; para a santificar, purificando-a com a lavagem da água, pela palavra; para a apresentar a si mesmo Igreja gloriosa, sem mácula, nem ruga, nem coisa semelhante, mas santa e irrepreensível.",
             "O modelo do casamento cristão é o amor de Cristo pela Igreja — sacrificial, santificador, comprometido com a glória da esposa. O marido é chamado a um amor que se doa até a morte, não a um domínio que subjuga.")
        ])),
    6: ("A Armadura de Deus", "Revesti-vos de toda a armadura de Deus, para que possais estar firmes contra as astutas ciladas do diabo.", "Ef 6:11",
        intro("Efésios 6 encerra com a metáfora da armadura de Deus — o equipamento espiritual para a guerra contra os principados e potestades.") +
        bloco("⚔️ A Armadura Completa de Deus (6:10-20)", [
            ("Ef 6:10-12", "Quanto ao mais, irmãos meus, fortalecei-vos no Senhor e na força do seu poder. Revesti-vos de toda a armadura de Deus, para que possais estar firmes contra as astutas ciladas do diabo. Porque não temos que lutar contra a carne e o sangue, mas contra os principados, contra as potestades, contra os príncipes das trevas desta era, contra as hostes espirituais da maldade nos lugares celestiais.",
             "A guerra espiritual é real mas invisível. Os inimigos não são pessoas (<em>sarx kai haima</em>), mas poderes espirituais: principados (<em>archas</em>), potestades (<em>exousias</em>), príncipes das trevas (<em>kosmokratoras</em>), hostes espirituais (<em>pneumatika tes ponerias</em>). A armadura é necessária porque o inimigo é real e poderoso."),
            ("Ef 6:14-17", "Estai, pois, firmes, tendo cingidos os vossos lombos com a verdade, e vestida a couraça da justiça, e calçados os pés com a preparação do evangelho da paz; tomando sobretudo o escudo da fé... e o capacete da salvação, e a espada do Espírito, que é a palavra de Deus.",
             "As 6 peças da armadura: (1) cinto da verdade — integridade; (2) couraça da justiça — a justiça de Cristo; (3) calçado do Evangelho — prontidão para proclamar; (4) escudo da fé — apagar os dardos inflamados; (5) capacete da salvação — proteção da mente; (6) espada do Espírito — a Palavra de Deus, única arma ofensiva.")
        ]) +
        bloco("🙏 A Oração como Arma (6:18-20)", [
            ("Ef 6:18-19", "Orando em todo o tempo com toda a oração e súplica no Espírito, e vigiando nisto com toda a perseverança e súplica por todos os santos; e por mim, para que me seja dada a palavra ao abrir a minha boca com confiança, para fazer conhecer o mistério do evangelho.",
             "A oração não é a sétima peça da armadura — é a atmosfera em que toda a guerra é travada. 'Em todo o tempo, com toda a oração, no Espírito, com toda a perseverança.' Paulo pede oração não pela sua libertação da prisão, mas pela ousadia para proclamar o Evangelho.")
        ])),
}

def gerar_efesios():
    for num, (titulo, vk, rk, body) in caps_efesios.items():
        html = page("Efésios", num, 6, titulo, vk, rk, body, "efesios", "../../../..")
        salvar("efesios", num, html)
    print("✅ Efésios: 6 capítulos gerados")

# ─── FILIPENSES ────────────────────────────────────────────────────────────────
caps_filipenses = {
    1: ("Alegria na Prisão", "Para mim o viver é Cristo, e o morrer é ganho.", "Fp 1:21",
        intro("Filipenses é a carta da alegria — escrita da prisão, a palavra 'alegria' aparece 16 vezes. O cap. 1 apresenta a alegria no sofrimento e o dilema de Paulo: viver ou morrer.") +
        bloco("😊 Alegria na Prisão (1:12-26)", [
            ("Fp 1:12-14", "Ora, quero que saibais, irmãos, que as coisas que me têm acontecido têm redundado antes para o progresso do evangelho; de modo que os meus laços em Cristo se tornaram manifestos em todo o pretório e em todos os outros lugares.",
             "O paradoxo da prisão: o que parecia obstáculo tornou-se oportunidade. A guarda pretoriana (soldados de elite) ouviu o Evangelho. A prisão de Paulo encorajou outros a pregar com mais ousadia. Deus usa as circunstâncias adversas para avançar o Evangelho."),
            ("Fp 1:21-23", "Para mim o viver é Cristo, e o morrer é ganho. Mas se o viver na carne me der fruto no trabalho, então não sei o que hei de preferir. Porque de ambas as partes me vejo constrangido: tenho desejo de partir e estar com Cristo, porque isto é muito melhor.",
             "O dilema de Paulo: viver = Cristo (não apenas para Cristo, mas Cristo mesmo é o conteúdo da vida); morrer = ganho (estar com Cristo). A morte não é perda — é ganho. Esta é a base da paz cristã diante da morte.")
        ])),
    2: ("A Mente de Cristo — Hino da Kenosis", "Haja em vós o mesmo sentimento que houve em Cristo Jesus.", "Fp 2:5",
        intro("Filipenses 2 contém o hino cristológico mais elevado do NT — a kenosis de Cristo. É ao mesmo tempo teologia profunda e modelo prático de humildade.") +
        bloco("👑 O Hino da Kenosis (2:5-11)", [
            ("Fp 2:5-8", "Haja em vós o mesmo sentimento que houve em Cristo Jesus, o qual, sendo em forma de Deus, não teve por usurpação ser igual a Deus, mas esvaziou-se a si mesmo, tomando a forma de servo, fazendo-se semelhante aos homens.",
             "<em>Morphe theou</em> — forma de Deus: a natureza divina essencial. <em>Ekenosen</em> — esvaziou-se: a kenosis (do grego <em>kenos</em>, vazio). Cristo não se esvaziou da divindade, mas dos privilégios e prerrogativas divinas. O movimento é descendente: Deus → servo → morte → morte de cruz."),
            ("Fp 2:9-11", "Por isso Deus o exaltou soberanamente, e lhe deu um nome que é sobre todo o nome; para que ao nome de Jesus se dobre todo joelho... e toda língua confesse que Jesus Cristo é o Senhor.",
             "A exaltação como resposta à humilhação. O nome acima de todo nome é <em>Kyrios</em> (Senhor) — o título divino do AT (YHWH). A confissão universal 'Jesus Cristo é o Senhor' é o credo mais antigo da Igreja. A humilhação voluntária de Cristo é o modelo para a humildade cristã.")
        ])),
    3: ("Contar como Perda por Cristo", "Mas o que para mim era ganho, isso considerei perda por amor de Cristo.", "Fp 3:7",
        intro("Filipenses 3 é a autobiografia espiritual de Paulo — a renúncia de todos os privilégios religiosos por amor ao conhecimento de Cristo.") +
        bloco("📊 O Balanço de Paulo (3:4-14)", [
            ("Fp 3:4-8", "Ainda que eu também tenho de que confiar na carne. Se alguém pensa que pode confiar na carne, eu ainda mais: circuncidado ao oitavo dia, da linhagem de Israel, da tribo de Benjamim, hebreu de hebreus... Mas o que para mim era ganho, isso considerei perda por amor de Cristo.",
             "Paulo lista 7 credenciais judaicas — o currículo religioso mais impecável possível. Então os conta como 'perda' (<em>zemia</em>) e 'lixo' (<em>skybala</em> — palavra forte, quase vulgar). O conhecimento de Cristo supera qualquer realização religiosa humana."),
            ("Fp 3:10-12", "Para conhecê-lo, e ao poder da sua ressurreição, e à comunicação das suas aflições, sendo conformado com ele na sua morte; para ver se de alguma forma posso chegar à ressurreição dentre os mortos.",
             "O objetivo de Paulo: conhecer Cristo (<em>gnonai auton</em>). Não apenas saber sobre Cristo, mas conhecimento relacional. O poder da ressurreição e a participação nos sofrimentos são inseparáveis — a vida cristã é paschal: morte e ressurreição.")
        ])),
    4: ("A Paz que Excede Todo Entendimento", "Posso tudo em Cristo que me fortalece.", "Fp 4:13",
        intro("Filipenses 4 é o capítulo da paz e do contentamento — os dois presentes mais preciosos da vida cristã segundo Paulo.") +
        bloco("🕊️ A Paz de Deus (4:4-9)", [
            ("Fp 4:4-7", "Alegrai-vos sempre no Senhor; outra vez digo: alegrai-vos. A vossa moderação seja conhecida de todos os homens. O Senhor está próximo. Não estejais ansiosos de coisa alguma; antes as vossas petições sejam em tudo conhecidas diante de Deus pela oração e súplica, com ação de graças. E a paz de Deus, que excede todo o entendimento, guardará os vossos corações e os vossos pensamentos em Cristo Jesus.",
             "O antídoto para a ansiedade: oração com ação de graças. O resultado: a paz de Deus (<em>eirene tou theou</em>) que excede todo entendimento (<em>hyperechousa panta noun</em>). A paz não é ausência de problemas — é a guarda divina do coração no meio dos problemas."),
            ("Fp 4:11-13", "Não que o diga por causa da necessidade, pois aprendi a estar contente em qualquer estado em que me encontre. Sei estar abatido, e sei também ter abundância; em toda a maneira, e em todas as coisas estou instruído, tanto a ter fartura, como a ter fome, tanto a ter abundância, como a padecer necessidade. Posso tudo em Cristo que me fortalece.",
             "O contentamento (<em>autarkeia</em>) é aprendido, não inato. Paulo 'aprendeu' (<em>emathon</em>) — escola de sofrimento. 'Posso tudo em Cristo' não é promessa de sucesso material — é declaração de suficiência espiritual em qualquer circunstância.")
        ])),
}

def gerar_filipenses():
    for num, (titulo, vk, rk, body) in caps_filipenses.items():
        html = page("Filipenses", num, 4, titulo, vk, rk, body, "filipenses", "../../../..")
        salvar("filipenses", num, html)
    print("✅ Filipenses: 4 capítulos gerados")

# ─── COLOSSENSES ───────────────────────────────────────────────────────────────
caps_colossenses = {
    1: ("A Supremacia de Cristo", "Porque nele foram criadas todas as coisas... tudo foi criado por ele e para ele.", "Cl 1:16",
        intro("Colossenses é a carta da supremacia de Cristo — escrita para combater uma heresia sincretista que diminuía Cristo. O hino cristológico de 1:15-20 é o mais elevado do NT.") +
        bloco("👑 O Hino da Supremacia (1:15-20)", [
            ("Cl 1:15-17", "O qual é a imagem do Deus invisível, o primogênito de toda a criação; porque nele foram criadas todas as coisas que há nos céus e na terra, visíveis e invisíveis... tudo foi criado por ele e para ele. E ele é antes de todas as coisas, e todas as coisas subsistem por ele.",
             "<em>Eikon tou theou</em> — imagem de Deus: não cópia, mas representação perfeita. <em>Prototokos pases ktiseos</em> — primogênito de toda a criação: não o primeiro criado, mas o soberano sobre toda a criação (cf. Sl 89:27 onde 'primogênito' = soberano). Cristo é a causa (<em>di autou</em>), o sustentador (<em>en auto synesteken</em>) e o alvo (<em>eis auton</em>) de toda a criação."),
            ("Cl 1:18-20", "E ele é a cabeça do corpo, da Igreja; é o princípio e o primogênito dentre os mortos, para que em tudo tenha a preeminência. Porque foi do agrado do Pai que nele habitasse toda a plenitude; e que, havendo feito a paz pelo sangue da sua cruz, por meio dele reconciliasse consigo mesmo todas as coisas.",
             "Cristo é cabeça da Igreja e primogênito dos mortos — a ressurreição como nova criação. A <em>pleroma</em> (plenitude) habita em Cristo — contra os gnósticos que dividiam o divino em emanações. A paz foi feita 'pelo sangue da sua cruz' — a reconciliação é cósmica.")
        ])),
    2: ("A Plenitude em Cristo contra o Legalismo", "Porque nele habita corporalmente toda a plenitude da divindade.", "Cl 2:9",
        intro("Colossenses 2 é a refutação direta da heresia colossense — uma mistura de filosofia grega, legalismo judaico e misticismo. Cristo é a resposta a tudo.") +
        bloco("⚠️ Contra a Filosofia Vã (2:8-23)", [
            ("Cl 2:8-10", "Vede que ninguém vos faça presa sua por meio de filosofias e vãs sutilezas, segundo a tradição dos homens, segundo os rudimentos do mundo, e não segundo Cristo. Porque nele habita corporalmente toda a plenitude da divindade; e estais nele completos.",
             "A heresia colossense: filosofia (<em>philosophia</em>) + tradição humana + rudimentos do mundo (<em>stoicheia tou kosmou</em>). A resposta: em Cristo habita <em>corporalmente</em> (<em>somatikos</em>) toda a plenitude da divindade. Os crentes estão 'completos' (<em>pepleromenoi</em>) em Cristo — nada precisa ser adicionado."),
            ("Cl 2:14-15", "Cancelando a cédula que havia contra nós nas suas ordenanças, que nos era contrária, e a tirou do meio, cravando-a na cruz; e, despojando os principados e potestades, os expôs publicamente, triunfando sobre eles em si mesmo.",
             "A cruz como vitória cósmica: (1) cancelou o 'documento de dívida' (<em>cheirographon</em>) da lei; (2) despojou os principados e potestades; (3) os expôs publicamente como derrotados. A crucificação, que parecia derrota, foi o maior triunfo da história.")
        ])),
    3: ("A Vida Escondida com Cristo", "Portanto, se fostes ressuscitados com Cristo, buscai as coisas que são lá de cima.", "Cl 3:1",
        intro("Colossenses 3 apresenta a ética da ressurreição — a vida nova em Cristo expressa em relações transformadas: família, trabalho, comunidade.") +
        bloco("☀️ Buscar as Coisas de Cima (3:1-17)", [
            ("Cl 3:1-4", "Portanto, se fostes ressuscitados com Cristo, buscai as coisas que são lá de cima, onde Cristo está assentado à destra de Deus. Pensai nas coisas que são lá de cima, não nas que são cá da terra. Porque morrestes, e a vossa vida está escondida com Cristo em Deus.",
             "A ética colossense é baseada na ontologia: você foi ressuscitado com Cristo, portanto busque as coisas de cima. A vida cristã é 'escondida com Cristo em Deus' — a identidade real do crente não é visível ao mundo, mas será revelada na parusia."),
            ("Cl 3:11", "Onde não há grego nem judeu, circuncisão nem incircuncisão, bárbaro, cita, escravo, livre; mas Cristo é tudo em todos.",
             "A nova humanidade em Cristo transcende todas as divisões étnicas, religiosas, culturais e sociais. 'Cristo é tudo em todos' (<em>ta panta kai en pasin Christos</em>) — a identidade cristã supera todas as outras identidades.")
        ])),
    4: ("Oração, Sabedoria e Saudações Finais", "Andai em sabedoria para com os que estão de fora, remindo o tempo.", "Cl 4:5",
        intro("Colossenses 4 encerra com exortações práticas sobre oração, testemunho e relações, e uma lista de colaboradores que revela a natureza comunitária do ministério apostólico.") +
        bloco("🙏 Oração e Testemunho (4:2-6)", [
            ("Cl 4:2-4", "Perseverai em oração, vigiando nela com ação de graças; orando também juntamente por nós, para que Deus nos abra a porta da palavra, a fim de falarmos o mistério de Cristo, pelo qual também estou preso.",
             "Paulo na prisão pede oração não pela libertação, mas pela abertura de portas para o Evangelho. A oração é perseverante (<em>proskarterein</em>), vigilante (<em>gregorountes</em>) e grata (<em>eucharistia</em>)."),
            ("Cl 4:5-6", "Andai em sabedoria para com os que estão de fora, remindo o tempo. A vossa palavra seja sempre agradável, temperada com sal, para que saibais como haveis de responder a cada um.",
             "O testemunho cristão: (1) sabedoria nas relações com não-crentes; (2) 'remir o tempo' (<em>exagorazomenoi ton kairon</em>) — aproveitar cada oportunidade; (3) palavras 'temperadas com sal' — preservadoras, saborosas, honestas.")
        ])),
}

def gerar_colossenses():
    for num, (titulo, vk, rk, body) in caps_colossenses.items():
        html = page("Colossenses", num, 4, titulo, vk, rk, body, "colossenses", "../../../..")
        salvar("colossenses", num, html)
    print("✅ Colossenses: 4 capítulos gerados")

# ─── 1 TESSALONICENSES ─────────────────────────────────────────────────────────
caps_1ts = {
    1: ("A Igreja Modelo", "Porque deles se divulgou a palavra do Senhor, não somente na Macedônia e Acaia, mas em todo lugar.", "1Ts 1:8",
        intro("1 Tessalonicenses é provavelmente a carta mais antiga de Paulo (~50 d.C.). O cap. 1 descreve a Igreja de Tessalônica como modelo para todas as igrejas.") +
        bloco("🌟 A Igreja Modelo (1:2-10)", [
            ("1Ts 1:3", "Lembrando-nos sem cessar, diante de nosso Deus e Pai, da obra da vossa fé, e do trabalho do vosso amor, e da paciência da vossa esperança em nosso Senhor Jesus Cristo.",
             "A tríade fé-amor-esperança em sua forma mais original (anterior a 1Cor 13). Cada virtude tem sua expressão: fé = obra (<em>ergou</em>), amor = trabalho (<em>kopou</em>), esperança = paciência (<em>hypomones</em>). A esperança não é passiva — é perseverança ativa."),
            ("1Ts 1:9-10", "Porque eles mesmos anunciam de nós qual a entrada que tivemos para convosco, e como vos convertestes dos ídolos a Deus, para servirdes ao Deus vivo e verdadeiro; e esperardes dos céus a seu Filho, a quem ressuscitou dentre os mortos, Jesus, que nos livra da ira futura.",
             "O resumo do Evangelho tessalonicense: conversão dos ídolos ao Deus vivo, serviço ao Deus verdadeiro, espera pelo Filho dos céus. A escatologia é central desde o início: Jesus 'que nos livra da ira futura'.")
        ])),
    2: ("O Ministério Autêntico", "Antes, fomos brandos no meio de vós, como a ama que cria os seus próprios filhos.", "1Ts 2:7",
        intro("1 Tessalonicenses 2 é a defesa do ministério apostólico de Paulo — contra acusações de engano, impureza e adulação.") +
        bloco("💙 O Ministério como Mãe e Pai (2:7-12)", [
            ("1Ts 2:7-8", "Antes, fomos brandos no meio de vós, como a ama que cria os seus próprios filhos. Assim, tendo afeição por vós, tínhamos prazer em comunicar-vos não somente o evangelho de Deus, mas também as nossas próprias vidas.",
             "O ministério como maternidade: ternura (<em>epioi</em>), afeto (<em>homeiromai</em>), doação da própria vida. O Evangelho é comunicado por pessoas que se doam — não apenas mensagem, mas vida.")
        ])),
    3: ("A Fé dos Tessalonicenses", "Porque agora vivemos, se vós estais firmes no Senhor.", "1Ts 3:8",
        intro("1 Tessalonicenses 3 relata o envio de Timóteo para verificar a fé dos tessalonicenses e o alívio de Paulo ao receber boas notícias.") +
        bloco("🙏 Alegria pela Fé Firme (3:6-13)", [
            ("1Ts 3:8-10", "Porque agora vivemos, se vós estais firmes no Senhor. Pois que ação de graças podemos render a Deus por causa de vós, por toda a alegria com que nos alegramos por vossa causa diante do nosso Deus?",
             "A interdependência pastoral: Paulo 'vive' quando os tessalonicenses estão firmes. O pastor genuíno tem sua vida ligada ao bem-estar espiritual do rebanho.")
        ])),
    4: ("A Santidade e a Ressurreição dos Mortos", "Porque o Senhor mesmo, dada a sua palavra de ordem... descerá do céu.", "1Ts 4:16",
        intro("1 Tessalonicenses 4 ensina sobre santidade sexual e responde à preocupação dos tessalonicenses sobre os que morreram antes da vinda de Cristo.") +
        bloco("⭐ A Vinda do Senhor (4:13-18)", [
            ("1Ts 4:13-14", "Não queremos, porém, irmãos, que sejais ignorantes acerca dos que já dormem, para que não vos entristeçais como os demais, que não têm esperança. Porque, se cremos que Jesus morreu e ressuscitou, assim também aos que dormem em Jesus, Deus os tornará a trazer com ele.",
             "A esperança cristã diante da morte: não ausência de tristeza, mas tristeza com esperança. O fundamento: a ressurreição de Jesus garante a ressurreição dos que morreram em Cristo. 'Dormem' (<em>koimomenous</em>) é metáfora cristã para a morte — temporária, com despertar garantido."),
            ("1Ts 4:16-17", "Porque o Senhor mesmo, dada a sua palavra de ordem, ouvida a voz do arcanjo, e a trombeta de Deus, descerá do céu; e os mortos em Cristo ressuscitarão primeiro; depois nós, os vivos, os que ficarmos, seremos arrebatados juntamente com eles nas nuvens, a encontrar o Senhor nos ares.",
             "A parusia: a vinda pessoal, visível e audível de Cristo. A sequência: (1) palavra de ordem; (2) voz do arcanjo; (3) trombeta de Deus; (4) ressurreição dos mortos em Cristo; (5) arrebatamento dos vivos. 'Encontrar o Senhor nos ares' (<em>apantesis</em>) — o termo técnico para a saída de uma cidade para receber um dignitário.")
        ])),
    5: ("O Dia do Senhor e a Vida na Luz", "Porque todos vós sois filhos da luz e filhos do dia.", "1Ts 5:5",
        intro("1 Tessalonicenses 5 ensina sobre o Dia do Senhor e encerra com exortações práticas para a vida comunitária.") +
        bloco("☀️ Filhos da Luz (5:1-11)", [
            ("1Ts 5:2-4", "Porque vós mesmos sabeis muito bem que o dia do Senhor virá como o ladrão de noite. Porque, quando disserem: Paz e segurança! então lhes sobrevirá repentina destruição... mas vós, irmãos, não estais em trevas, para que esse dia vos surpreenda como ladrão.",
             "O Dia do Senhor virá inesperadamente para os que estão nas trevas. Mas os crentes são 'filhos da luz' — não serão surpreendidos. A preparação não é calcular datas, mas viver em vigilância e sobriedade.")
        ])),
}

def gerar_1tessalonicenses():
    for num, (titulo, vk, rk, body) in caps_1ts.items():
        html = page("1 Tessalonicenses", num, 5, titulo, vk, rk, body, "1tessalonicenses", "../../../..")
        salvar("1tessalonicenses", num, html)
    print("✅ 1 Tessalonicenses: 5 capítulos gerados")

# ─── 2 TESSALONICENSES ─────────────────────────────────────────────────────────
caps_2ts = {
    1: ("O Juízo Justo de Deus", "Quando o Senhor Jesus se manifestar do céu com os anjos do seu poder.", "2Ts 1:7",
        intro("2 Tessalonicenses corrige um mal-entendido: os tessalonicenses pensavam que o Dia do Senhor já havia chegado. Paulo ensina sobre o juízo justo e os sinais que precedem a vinda.") +
        bloco("⚖️ O Juízo Justo (1:5-10)", [
            ("2Ts 1:6-8", "Porquanto é justo diante de Deus retribuir com tribulação os que vos atribulam; e a vós, que sois atribulados, dar descanso conosco, na revelação do Senhor Jesus do céu com os anjos do seu poder, em chama de fogo, tomando vingança dos que não conhecem a Deus.",
             "O juízo de Deus é justo: os perseguidores serão retribuídos com tribulação; os perseguidos receberão descanso. A justiça divina não é vingança pessoal — é a restauração da ordem moral do universo.")
        ])),
    2: ("O Homem da Iniquidade", "O qual se opõe e se levanta contra tudo o que se chama Deus ou se adora.", "2Ts 2:4",
        intro("2 Tessalonicenses 2 é o texto mais apocalíptico de Paulo — descrevendo o 'homem da iniquidade' e o 'mistério da iniquidade' que precede a vinda de Cristo.") +
        bloco("🔥 O Homem da Iniquidade (2:1-12)", [
            ("2Ts 2:3-4", "Não vos deixeis enganar de maneira alguma; porque não será assim sem que antes venha a apostasia, e seja revelado o homem do pecado, o filho da perdição; o qual se opõe e se levanta contra tudo o que se chama Deus ou se adora.",
             "Dois eventos precedem o Dia do Senhor: (1) a apostasia (<em>apostasia</em>); (2) a revelação do 'homem do pecado' (<em>anthropos tes anomias</em>). Este personagem se entroniza no templo de Deus declarando-se Deus — o ápice da blasfêmia. Identificações históricas: Calígula, Nero, o Anticristo escatológico."),
            ("2Ts 2:7-8", "Porque o mistério da iniquidade já está em ação; somente há um que agora retém, até que seja tirado do meio. E então será revelado o iníquo, a quem o Senhor Jesus matará com o sopro de sua boca.",
             "O 'mistério da iniquidade' (<em>mysterion tes anomias</em>) já opera. O 'que retém' (<em>katechon</em>) — identidade debatida: o Espírito Santo, o Império Romano, a Igreja. Cristo destruirá o iníquo 'com o sopro de sua boca' — a palavra de Deus é suficiente para destruir qualquer poder do mal.")
        ])),
    3: ("Trabalho e Disciplina Comunitária", "Porque, quando ainda estávamos convosco, vos ordenávamos isto: se alguém não quiser trabalhar, também não coma.", "2Ts 3:10",
        intro("2 Tessalonicenses 3 corrige o problema dos 'ociosos' — membros que pararam de trabalhar esperando a iminente vinda de Cristo.") +
        bloco("💼 Trabalho e Ordem (3:6-15)", [
            ("2Ts 3:10-12", "Porque, quando ainda estávamos convosco, vos ordenávamos isto: se alguém não quiser trabalhar, também não coma. Porque ouvimos que alguns entre vós andam desordenadamente, não trabalhando, antes se intrometendo nos negócios alheios. A esses tais ordenamos e exortamos, pelo Senhor Jesus Cristo, que trabalhem sossegadamente e comam o seu próprio pão.",
             "O princípio do trabalho: a esperança escatológica não é desculpa para a ociosidade. Paulo mesmo trabalhava com as próprias mãos como exemplo. A disciplina comunitária: não se associar ao ocioso, mas não tratá-lo como inimigo — exortá-lo como irmão.")
        ])),
}

def gerar_2tessalonicenses():
    for num, (titulo, vk, rk, body) in caps_2ts.items():
        html = page("2 Tessalonicenses", num, 3, titulo, vk, rk, body, "2tessalonicenses", "../../../..")
        salvar("2tessalonicenses", num, html)
    print("✅ 2 Tessalonicenses: 3 capítulos gerados")

if __name__ == "__main__":
    gerar_2corintios()
    gerar_galatas()
    gerar_efesios()
    gerar_filipenses()
    gerar_colossenses()
    gerar_1tessalonicenses()
    gerar_2tessalonicenses()
    print("\n🎉 Fase 2 concluída: 2Cor + Gálatas + Efésios + Filipenses + Colossenses + 1-2Ts = 41 capítulos aprofundados")
