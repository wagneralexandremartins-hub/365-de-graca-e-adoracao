#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera capítulos aprofundados:
Tiago (5), 1Pedro (5), 2Pedro (3), 1João (5), 2João (1), 3João (1), Judas (1), Apocalipse (22)
= 43 capítulos
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

# ─── TIAGO ─────────────────────────────────────────────────────────────────────
caps_tiago = {
    1: ("Fé Provada pelas Tribulações", "Meus irmãos, tende por motivo de toda a alegria o passardes por várias provações.", "Tg 1:2",
        intro("Tiago é a carta mais prática do NT — escrita por Tiago, irmão de Jesus, ~45-49 d.C. É a carta mais próxima da sabedoria judaica, com ênfase na ética do Reino.") +
        bloco("💪 Fé e Provações (1:2-12)", [
            ("Tg 1:2-4", "Meus irmãos, tende por motivo de toda a alegria o passardes por várias provações; sabendo que a prova da vossa fé produz a paciência. E a paciência deve ter uma obra perfeita, para que sejais perfeitos e completos, sem faltar em coisa alguma.",
             "O paradoxo cristão: alegria nas provações. A lógica: provações testam a fé, o teste produz paciência (<em>hypomone</em>), a paciência produz maturidade. A alegria não é negação da dor — é visão do propósito. O cristão maduro não evita as provações — as abraça como escola de caráter."),
            ("Tg 1:5-6", "E, se algum de vós tem falta de sabedoria, peça-a a Deus, que a todos dá liberalmente e não faz reprovação, e ser-lhe-á dada. Peça-a, porém, com fé, sem duvidar; porque o que duvida é semelhante à onda do mar, que o vento impele e agita.",
             "A promessa da sabedoria: Deus dá generosamente (<em>haplos</em> — sem reservas) e sem reprovar (<em>me oneidizontos</em>). A condição: pedir com fé, sem dividir-se (<em>diakrino</em>). O homem dividido (<em>dipsychos</em> — de duas almas) é instável em todos os seus caminhos.")
        ]) +
        bloco("🌟 Ouvir e Fazer (1:19-27)", [
            ("Tg 1:22-25", "Sede cumpridores da palavra, e não somente ouvintes, enganando-vos a vós mesmos. Porque, se alguém é ouvinte da palavra e não cumpridor dela, esse é semelhante ao homem que contempla no espelho o seu rosto natural; porque contemplou-se a si mesmo, e retirou-se, e logo se esqueceu de como era.",
             "A metáfora do espelho: ouvir a Palavra sem obedecer é como olhar no espelho e esquecer o que viu. A Palavra é espelho que revela quem somos; a obediência é a resposta ao que vemos. A lei perfeita da liberdade (<em>nomon teleion ton tes eleutherias</em>) liberta quando obedecida.")
        ])),
    2: ("A Fé sem Obras é Morta", "Assim também a fé, se não tiver as obras, é morta em si mesma.", "Tg 2:17",
        intro("Tiago 2 é o capítulo mais debatido da carta — a relação entre fé e obras. Tiago não contradiz Paulo: ambos concordam que a fé salvadora produz obras; Tiago combate a fé nominal sem transformação.") +
        bloco("⚖️ Sem Acepção de Pessoas (2:1-13)", [
            ("Tg 2:1-4", "Meus irmãos, não tenhais a fé de nosso Senhor Jesus Cristo, Senhor da glória, com acepção de pessoas. Porque, se na vossa sinagoga entrar algum homem com anel de ouro e com veste resplandecente, e entrar também algum pobre com roupa suja; e olhardes para o que traz a veste resplandecente e lhe disserdes: Assenta-te tu aqui num bom lugar; e disserdes ao pobre: Fica tu aí em pé, ou assenta-te aqui debaixo do meu estrado; não fizestes distinção entre vós mesmos?",
             "A acepção de pessoas (<em>prosopolempsia</em>) contradiz a fé em Cristo. O favorecimento dos ricos na assembleia é julgamento corrompido. O 'banco dos pobres' era literal nas sinagogas. A lei real (<em>nomon basilikon</em>) — amar o próximo — é violada pela discriminação.")
        ]) +
        bloco("💪 Fé e Obras (2:14-26)", [
            ("Tg 2:17-18", "Assim também a fé, se não tiver as obras, é morta em si mesma. Mas alguém dirá: Tu tens a fé, e eu tenho as obras. Mostra-me a tua fé sem as tuas obras, e eu te mostrarei a minha fé pelas minhas obras.",
             "Tiago não contradiz Paulo — combate um mal-entendido diferente. Paulo combate obras como meio de justificação; Tiago combate fé nominal sem transformação. A fé salvadora inevitavelmente produz obras — não para ganhar salvação, mas como evidência dela. 'Mostrar a fé' só é possível pelas obras."),
            ("Tg 2:21-23", "Não foi Abraão, nosso pai, justificado pelas obras, quando ofereceu seu filho Isaque sobre o altar? Vês que a fé cooperou com as suas obras, e que pelas obras a fé foi aperfeiçoada. E assim se cumpriu a Escritura que diz: E creu Abraão em Deus, e isso lhe foi imputado como justiça.",
             "Abraão foi justificado pela fé (Gn 15 — Paulo) E pelas obras (Gn 22 — Tiago). Não contradição: Gn 15 é a justificação diante de Deus; Gn 22 é a demonstração pública da fé. As obras de Abraão 'aperfeiçoaram' a fé — não a criaram, mas a completaram e demonstraram.")
        ])),
    3: ("O Poder da Língua e a Sabedoria do Alto", "Mas a sabedoria que do alto vem é, primeiramente, pura, depois pacífica, moderada, tratável, cheia de misericórdia e de bons frutos.", "Tg 3:17",
        intro("Tiago 3 contém o ensino mais extenso do NT sobre a língua — o órgão mais poderoso e mais perigoso do corpo humano.") +
        bloco("👅 O Poder da Língua (3:1-12)", [
            ("Tg 3:5-8", "Assim também a língua é um pequeno membro, e gloria-se de grandes coisas. Vede como um pequeno fogo abrasa um grande bosque! A língua também é um fogo; a língua, esse mundo de iniquidade, está posta entre os nossos membros, e contamina todo o corpo, e inflama o curso da natureza, e é inflamada pelo inferno.",
             "Quatro metáforas da língua: freio no cavalo, leme no navio, faísca no bosque, fogo do inferno. A língua é desproporcional ao seu tamanho — pequena, mas com poder de destruição cósmico. 'Inflamada pelo inferno' (<em>phlogizomene hypo tes geennes</em>) — a língua descontrolada tem origem diabólica.")
        ]) +
        bloco("🌿 A Sabedoria do Alto (3:13-18)", [
            ("Tg 3:17-18", "Mas a sabedoria que do alto vem é, primeiramente, pura, depois pacífica, moderada, tratável, cheia de misericórdia e de bons frutos, sem parcialidade e sem hipocrisia. E o fruto da justiça semeia-se na paz, para os que promovem a paz.",
             "A sabedoria celestial vs. terrena: a terrena é amarga, invejosa, contenciosa, demoníaca; a celestial é pura, pacífica, moderada, tratável, misericordiosa, frutífera, imparcial, sem hipocrisia. A sabedoria verdadeira se reconhece pelo fruto — especialmente a paz.")
        ])),
    4: ("A Humildade diante de Deus", "Humilhai-vos perante o Senhor, e ele vos exaltará.", "Tg 4:10",
        intro("Tiago 4 diagnostica a raiz dos conflitos (desejos carnais), chama ao arrependimento e à humildade, e adverte contra o julgamento dos irmãos.") +
        bloco("⚔️ A Raiz dos Conflitos (4:1-6)", [
            ("Tg 4:1-3", "Donde vêm as guerras e os combates entre vós? Porventura não vêm das vossas concupiscências, que guerreiam nos vossos membros? Cobiçais, e não tendes; matais, e tendes inveja, e não podeis alcançar; combateis e guerreais, e não tendes, porque não pedis. Pedis, e não recebeis, porque pedis mal, para o gastardes em vossos prazeres.",
             "A anatomia dos conflitos: desejos (<em>hedonon</em>) que guerreiam internamente produzem conflitos externos. A oração egoísta não é respondida — pedir para gastar em prazeres é usar Deus como fornecedor de desejos carnais.")
        ]) +
        bloco("🙏 Humildade e Arrependimento (4:7-10)", [
            ("Tg 4:7-10", "Sujeitai-vos, pois, a Deus; resisti ao diabo, e ele fugirá de vós. Chegai-vos a Deus, e ele se chegará a vós. Limpai as mãos, pecadores; e purificai os corações, vós que sois de ânimo dobre. Afligí-vos, e lamentai, e chorai; converta-se o vosso riso em pranto, e o vosso gozo em tristeza. Humilhai-vos perante o Senhor, e ele vos exaltará.",
             "Dez imperativos em quatro versículos: sujeitar, resistir, aproximar-se, limpar, purificar, afligir-se, lamentar, chorar, humilhar — e a promessa: Deus exaltará. A sequência: sujeição a Deus → resistência ao diabo → aproximação de Deus. A humildade não é auto-depreciação — é posicionamento correto diante de Deus.")
        ])),
    5: ("A Paciência de Jó e a Oração Eficaz", "A oração feita com fé salvará o enfermo, e o Senhor o levantará.", "Tg 5:15",
        intro("Tiago 5 encerra com advertências aos ricos opressores, o exemplo de paciência de Jó e Elias, e o poder da oração do justo.") +
        bloco("🙏 A Oração Eficaz (5:13-20)", [
            ("Tg 5:16-18", "Confessai, pois, os vossos pecados uns aos outros, e orai uns pelos outros, para que sareis; porque muito pode, por sua eficácia, a súplica do justo. Elias era um homem sujeito às mesmas paixões que nós, e orou fervorosamente para que não chovesse, e não choveu sobre a terra por três anos e seis meses.",
             "A oração eficaz (<em>energoumene</em> — que opera, que age) do justo tem grande poder. Elias como exemplo: homem de 'paixões semelhantes' (<em>homoiopathes</em>) — não super-herói, mas homem comum. A oração de fé pode mudar o clima — quanto mais pode mudar corações."),
            ("Tg 5:19-20", "Irmãos, se algum de entre vós se desviar da verdade, e alguém o converter, saiba que aquele que converter o pecador do erro do seu caminho salvará da morte uma alma, e cobrirá uma multidão de pecados.",
             "O ministério da restauração: trazer de volta o desviado é salvar uma alma da morte. A Igreja é responsável pelos que se desviam — não apenas pelos que estão dentro. A cobertura de pecados (<em>kalypsei plethos hamartion</em>) é o resultado da restauração.")
        ])),
}

def gerar_tiago():
    for num, (titulo, vk, rk, body) in caps_tiago.items():
        html = page("Tiago", num, 5, titulo, vk, rk, body, "tiago", "../../../..")
        salvar("tiago", num, html)
    print("✅ Tiago: 5 capítulos gerados")

# ─── 1 PEDRO ───────────────────────────────────────────────────────────────────
caps_1pedro = {
    1: ("Esperança Viva pela Ressurreição", "Bendito seja o Deus e Pai de nosso Senhor Jesus Cristo, que segundo a sua muita misericórdia nos regenerou para uma esperança viva.", "1Pe 1:3",
        intro("1 Pedro é a carta do sofrimento com esperança — escrita por Pedro a cristãos dispersos na Ásia Menor (~63-64 d.C.) que enfrentavam perseguição. O cap. 1 apresenta a esperança viva da ressurreição.") +
        bloco("🌟 Esperança Viva (1:3-12)", [
            ("1Pe 1:3-5", "Bendito seja o Deus e Pai de nosso Senhor Jesus Cristo, que segundo a sua muita misericórdia nos regenerou para uma esperança viva, pela ressurreição de Jesus Cristo dentre os mortos, para uma herança incorruptível, incontaminável, e que não se pode murchar, guardada nos céus para vós.",
             "A esperança cristã é 'viva' (<em>zosan</em>) — não esperança morta de uma religião morta, mas esperança fundamentada na ressurreição. A herança tem três atributos negativos: incorruptível (<em>aphtharton</em>), incontaminável (<em>amianton</em>), imurchável (<em>amaranton</em>). Guardada por Deus nos céus — nenhum poder pode roubá-la."),
            ("1Pe 1:6-7", "Nisto exultais, embora agora, por um pouco de tempo, se necessário, sejais contristados por várias provações; para que o valor da vossa fé, muito mais preciosa do que o ouro que perece, mas que pelo fogo se prova, seja achado para louvor, e glória, e honra na revelação de Jesus Cristo.",
             "O sofrimento como refinamento: o ouro é purificado pelo fogo, mas perece; a fé purificada pelo sofrimento é mais preciosa que o ouro e dura para a eternidade. A perspectiva escatológica transforma o sofrimento presente.")
        ]) +
        bloco("🌿 Santidade como Resposta à Graça (1:13-25)", [
            ("1Pe 1:15-16", "Mas, como é santo aquele que vos chamou, sede vós também santos em toda a vossa maneira de viver; porquanto está escrito: Sede santos, porque eu sou santo.",
             "A santidade como imitação de Deus: 'sede santos porque eu sou santo' (Lv 11:44). A santidade não é opção — é a natureza do chamado divino. O imperativo é baseado no indicativo: Deus é santo, portanto sejamos santos.")
        ])),
    2: ("Pedras Vivas e o Sacerdócio Real", "Mas vós sois a geração eleita, o sacerdócio real, a nação santa, o povo adquirido.", "1Pe 2:9",
        intro("1 Pedro 2 apresenta a identidade da Igreja como novo povo de Deus — pedras vivas, sacerdócio real, nação santa — e o exemplo de Cristo no sofrimento injusto.") +
        bloco("🏛️ Pedras Vivas (2:4-10)", [
            ("1Pe 2:4-5", "Chegando-vos a ele, pedra viva, reprovada pelos homens, mas escolhida e preciosa diante de Deus; vós também, como pedras vivas, sois edificados casa espiritual para um sacerdócio santo, para oferecer sacrifícios espirituais agradáveis a Deus por Jesus Cristo.",
             "Cristo é a Pedra Viva — reprovada pelos homens (crucificado), preciosa diante de Deus (ressuscitado). Os crentes são pedras vivas (<em>lithoi zontes</em>) — não pedras mortas de um templo físico, mas membros vivos de um templo espiritual. O sacerdócio é de todos os crentes — não apenas de uma classe clerical."),
            ("1Pe 2:9-10", "Mas vós sois a geração eleita, o sacerdócio real, a nação santa, o povo adquirido, para que anuncieis as virtudes daquele que vos chamou das trevas para a sua maravilhosa luz; vós que antes não éreis povo, mas agora sois povo de Deus.",
             "Quatro títulos do AT aplicados à Igreja (cf. Ex 19:5-6): geração eleita, sacerdócio real, nação santa, povo adquirido. O propósito: anunciar as virtudes (<em>aretas</em>) de Deus. A Igreja é o novo Israel — não substituindo Israel, mas cumprindo o propósito original de Israel como 'reino de sacerdotes'.")
        ])),
    3: ("O Sofrimento Injusto e o Espírito Manso", "Mas santificai ao Senhor Deus em vossos corações, e estai sempre preparados para responder com mansidão e temor a qualquer que vos pedir razão da esperança que há em vós.", "1Pe 3:15",
        intro("1 Pedro 3 ensina sobre o relacionamento conjugal, o sofrimento injusto como seguimento de Cristo, e a defesa da fé com mansidão.") +
        bloco("💍 Relacionamentos (3:1-7)", [
            ("1Pe 3:3-4", "O enfeite delas não seja o exterior, no frisado dos cabelos, no uso de joias de ouro, na compostura dos vestidos; mas o homem encoberto do coração, no incorruptível adorno de um espírito manso e quieto, que é precioso diante de Deus.",
             "O adorno verdadeiro: não externo (cabelos, joias, roupas), mas interno — o 'homem encoberto do coração' (<em>ho kryptos tes kardias anthropos</em>). O espírito manso e quieto (<em>prays kai hesychios pneuma</em>) é precioso diante de Deus — o valor eterno contrasta com o ornamento perecível.")
        ]) +
        bloco("🙏 Defesa da Esperança (3:13-22)", [
            ("1Pe 3:15-16", "Mas santificai ao Senhor Deus em vossos corações, e estai sempre preparados para responder com mansidão e temor a qualquer que vos pedir razão da esperança que há em vós; tendo boa consciência, para que naquilo em que falam mal de vós, como de malfeitores, fiquem envergonhados os que maldizem o vosso bom comportamento em Cristo.",
             "O fundamento da apologética cristã: santificar Cristo no coração. A defesa (<em>apologia</em>) deve ser com mansidão (<em>prautetos</em>) e temor (<em>phobou</em>) — não arrogância intelectual. A boa consciência é o contexto: a vida íntegra confirma a defesa verbal.")
        ])),
    4: ("Sofrendo como Cristão", "Se alguém sofre como cristão, não se envergonhe; antes, glorifique a Deus por isso.", "1Pe 4:16",
        intro("1 Pedro 4 chama os crentes a armar-se com a mente de Cristo no sofrimento, e apresenta o sofrimento como cristão como privilégio, não vergonha.") +
        bloco("💪 A Mente de Cristo no Sofrimento (4:1-11)", [
            ("1Pe 4:1-2", "Visto, pois, que Cristo padeceu na carne, armai-vos também vós com o mesmo pensamento; porque aquele que padeceu na carne acabou com o pecado; para que o tempo que ainda resta na carne não o vivais nas concupiscências dos homens, mas na vontade de Deus.",
             "Armar-se com a mente de Cristo: a disposição de sofrer pela vontade de Deus em vez de ceder ao pecado. O sofrimento de Cristo foi o caminho da obediência; nosso sofrimento pode ser o mesmo caminho.")
        ]) +
        bloco("🌟 Sofrendo como Cristão (4:12-19)", [
            ("1Pe 4:12-14", "Amados, não estranheis o fogo ardente que se acendeu entre vós para vos tentar, como se alguma coisa extraordinária vos sucedesse; antes, regozijai-vos, na medida em que sois participantes dos sofrimentos de Cristo, para que também na revelação da sua glória vos regozijeis com exultação.",
             "O sofrimento não é exceção — é a norma da vida cristã neste século. 'Não estranheis' (<em>me xenizesthe</em>) — não sejais estranhos ao sofrimento. Participar dos sofrimentos de Cristo é participar de sua glória futura. A parusia transformará o sofrimento presente em alegria eterna.")
        ])),
    5: ("O Pastor dos Pastores e a Humildade", "Humilhai-vos, pois, debaixo da potente mão de Deus, para que ele vos exalte em tempo oportuno.", "1Pe 5:6",
        intro("1 Pedro 5 encerra com instruções para os presbíteros, o chamado à humildade e vigilância, e a promessa da graça de Deus no sofrimento.") +
        bloco("👑 O Pastor dos Pastores (5:1-4)", [
            ("1Pe 5:2-4", "Apascentai o rebanho de Deus que está entre vós, tendo cuidado dele, não por força, mas voluntariamente; nem por torpe ganância, mas de ânimo pronto; nem como tendo domínio sobre a herança de Deus, mas sendo exemplos do rebanho. E, quando aparecer o supremo Pastor, recebereis a incorruptível coroa da glória.",
             "O modelo pastoral de Pedro: voluntário (não forçado), generoso (não ganancioso), exemplar (não dominador). O supremo Pastor (<em>archipoimenos</em>) — Cristo — é o modelo e o juiz de todos os pastores. A coroa da glória é a recompensa do pastor fiel.")
        ]) +
        bloco("🦁 Vigilância contra o Adversário (5:8-11)", [
            ("1Pe 5:8-9", "Sede sóbrios e vigilantes. O diabo, vosso adversário, anda em derredor, como leão que ruge, procurando alguém para devorar; ao qual resistí, firmes na fé, sabendo que os mesmos sofrimentos se cumprem na vossa irmandade que está no mundo.",
             "O diabo como leão rugindo: imagem de poder e ameaça real. A resistência: sobriedade (<em>nepsate</em>), vigilância (<em>gregoreuete</em>), firmeza na fé. A solidariedade: os mesmos sofrimentos são experimentados pela irmandade mundial — o sofrimento individual é parte de uma experiência coletiva.")
        ])),
}

def gerar_1pedro():
    for num, (titulo, vk, rk, body) in caps_1pedro.items():
        html = page("1 Pedro", num, 5, titulo, vk, rk, body, "1pedro", "../../../..")
        salvar("1pedro", num, html)
    print("✅ 1 Pedro: 5 capítulos gerados")

# ─── 2 PEDRO ───────────────────────────────────────────────────────────────────
caps_2pedro = {
    1: ("A Divina Natureza e a Profecia da Escritura", "Pois nunca jamais qualquer profecia foi dada por vontade humana; antes, os homens santos falaram da parte de Deus, movidos pelo Espírito Santo.", "2Pe 1:21",
        intro("2 Pedro é a última carta de Pedro (~67 d.C.) — um testamento espiritual que combate falsos mestres e afirma a certeza da parusia.") +
        bloco("🌟 Participantes da Divina Natureza (1:3-11)", [
            ("1Pe 1:3-4", "Como o seu divino poder nos deu tudo o que diz respeito à vida e à piedade, pelo conhecimento daquele que nos chamou para a sua própria glória e virtude; pelas quais ele nos deu as suas preciosas e grandíssimas promessas, para que por elas fôsseis participantes da natureza divina.",
             "<em>Theias koinonoi physeos</em> — participantes da natureza divina: a afirmação mais ousada sobre a salvação no NT. Não divinização no sentido panteísta, mas participação na vida e caráter de Deus. O meio: as 'preciosas e grandíssimas promessas' — a Palavra de Deus como veículo da transformação.")
        ]) +
        bloco("📖 A Profecia Inspirada (1:19-21)", [
            ("2Pe 1:20-21", "Sabendo primeiramente isto: que nenhuma profecia da Escritura é de particular interpretação; porque nunca jamais qualquer profecia foi dada por vontade humana; antes, os homens santos falaram da parte de Deus, movidos pelo Espírito Santo.",
             "<em>Pheromeni hypo pneumatos hagiou</em> — movidos pelo Espírito Santo: a inspiração como movimento divino. Os profetas não inventaram as profecias — foram 'carregados' pelo Espírito como um barco pelo vento. A interpretação não é 'particular' (<em>idias epilyseos</em>) — a Escritura não é propriedade privada do intérprete.")
        ])),
    2: ("Os Falsos Profetas", "Houve também falsos profetas entre o povo, como entre vós haverá falsos mestres.", "2Pe 2:1",
        intro("2 Pedro 2 é o capítulo mais severo sobre falsos mestres no NT — descrevendo seu caráter, seus métodos e seu julgamento inevitável.") +
        bloco("⚠️ Os Falsos Mestres (2:1-22)", [
            ("2Pe 2:1-3", "Houve também falsos profetas entre o povo, como entre vós haverá falsos mestres, os quais introduzirão encobertamente heresias destruidoras, e negarão o Senhor que os resgatou, trazendo sobre si mesmos repentina destruição. E muitos seguirão as suas dissoluções, pelo que o caminho da verdade será blasfemado; e por avareza, com palavras fingidas, farão mercadoria de vós.",
             "Os falsos mestres: (1) introduzem heresias 'encobertamente' (<em>pareisaxousin</em>); (2) negam o Senhor que os resgatou; (3) atraem seguidores pela dissolução; (4) blasfemam o caminho da verdade; (5) exploram por avareza. O julgamento é certo — três exemplos históricos: anjos caídos, geração do dilúvio, Sodoma e Gomorra.")
        ])),
    3: ("O Dia do Senhor e a Nova Criação", "Mas, conforme a sua promessa, esperamos novos céus e nova terra, nos quais habita a justiça.", "2Pe 3:13",
        intro("2 Pedro 3 responde aos que zombam da parusia e apresenta a certeza do Dia do Senhor e a esperança da nova criação.") +
        bloco("🔥 O Dia do Senhor (3:3-13)", [
            ("2Pe 3:8-10", "Mas, amados, não ignoreis uma coisa: que para o Senhor um dia é como mil anos, e mil anos como um dia. O Senhor não retarda a sua promessa, ainda que alguns a têm por tardança; antes, é longânimo para convosco, não querendo que nenhum pereça, mas que todos se convertam ao arrependimento. Mas o dia do Senhor virá como ladrão.",
             "A resposta ao problema do 'atraso': Deus não está em nosso tempo linear. A demora é longanimidade (<em>makrothymei</em>) — Deus quer que todos se arrependam. O Dia virá como ladrão — inesperadamente. A certeza não é sobre o quando, mas sobre o que: o julgamento e a renovação são certos."),
            ("2Pe 3:13", "Mas, conforme a sua promessa, esperamos novos céus e nova terra, nos quais habita a justiça.",
             "A esperança final: novos céus e nova terra (<em>kainous ouranous kai gen kainen</em>) — não destruição, mas renovação. A característica da nova criação: 'nos quais habita a justiça' (<em>dikaiosyne katoikei</em>). A nova criação é o lar da justiça — o que este mundo nunca foi.")
        ])),
}

def gerar_2pedro():
    for num, (titulo, vk, rk, body) in caps_2pedro.items():
        html = page("2 Pedro", num, 3, titulo, vk, rk, body, "2pedro", "../../../..")
        salvar("2pedro", num, html)
    print("✅ 2 Pedro: 3 capítulos gerados")

# ─── 1 JOÃO ────────────────────────────────────────────────────────────────────
caps_1joao = {
    1: ("A Comunhão com o Deus de Luz", "Mas, se andarmos na luz, como ele está na luz, temos comunhão uns com os outros, e o sangue de Jesus Cristo, seu Filho, nos purifica de todo o pecado.", "1Jo 1:7",
        intro("1 João é a carta do amor — escrita por João (~90-95 d.C.) para combater o proto-gnosticismo e afirmar a realidade da encarnação e do amor fraternal.") +
        bloco("☀️ Deus é Luz (1:5-10)", [
            ("1Jo 1:5-7", "E esta é a mensagem que dele ouvimos, e vos anunciamos: que Deus é luz, e não há nele trevas nenhumas. Se dissermos que temos comunhão com ele, e andarmos nas trevas, mentimos, e não praticamos a verdade. Mas, se andarmos na luz, como ele está na luz, temos comunhão uns com os outros, e o sangue de Jesus Cristo, seu Filho, nos purifica de todo o pecado.",
             "Deus é luz (<em>phos</em>) — não apenas tem luz, mas é luz. A comunhão com Deus exige andar na luz. A purificação pelo sangue de Cristo é contínua (<em>katharizei</em> — presente) — não evento único, mas processo permanente. Andar na luz não é perfeição, mas transparência e honestidade diante de Deus."),
            ("1Jo 1:9", "Se confessarmos os nossos pecados, ele é fiel e justo para nos perdoar os pecados, e nos purificar de toda a injustiça.",
             "A promessa do perdão: confissão (<em>homologomen</em> — concordar com Deus sobre o pecado) → perdão (<em>aphie</em>) + purificação (<em>katharize</em>). Deus é fiel (<em>pistos</em>) — seu caráter garante o perdão; e justo (<em>dikaios</em>) — o perdão é baseado na justiça satisfeita em Cristo.")
        ])),
    2: ("O Mandamento Novo e o Anticristo", "Filhinhos, esta é a última hora; e, como ouvistes que o anticristo há de vir, também agora muitos anticristos têm surgido.", "1Jo 2:18",
        intro("1 João 2 apresenta Cristo como nosso Advogado, o mandamento novo do amor, e a advertência sobre os anticristos.") +
        bloco("💙 Cristo nosso Advogado (2:1-2)", [
            ("1Jo 2:1-2", "Filhinhos meus, estas coisas vos escrevo para que não pequeis; e, se alguém pecar, temos um Advogado junto do Pai, Jesus Cristo, o justo. E ele é a propiciação pelos nossos pecados, e não somente pelos nossos, mas também pelos de todo o mundo.",
             "<em>Parakletos</em> — Advogado: o mesmo título dado ao Espírito Santo em João 14-16. Cristo é nosso Advogado celestial que intercede com base em sua propiciação (<em>hilasmos</em>). A propiciação satisfaz a justiça de Deus — não apenas cobre o pecado, mas remove a ira divina.")
        ]) +
        bloco("⚠️ Os Anticristos (2:18-27)", [
            ("1Jo 2:22-23", "Quem é o mentiroso, senão aquele que nega que Jesus é o Cristo? Este é o anticristo, que nega o Pai e o Filho. Todo aquele que nega o Filho também não tem o Pai; mas aquele que confessa o Filho também tem o Pai.",
             "O anticristo (<em>antichristos</em>) é definido cristologicamente: quem nega que Jesus é o Cristo. A negação do Filho implica a negação do Pai — não se pode ter Deus sem Cristo. A cristologia é o divisor de águas da verdadeira fé.")
        ])),
    3: ("Filhos de Deus e o Amor Fraternal", "Vede que amor nos concedeu o Pai, que fôssemos chamados filhos de Deus.", "1Jo 3:1",
        intro("1 João 3 desenvolve a identidade dos filhos de Deus e o amor fraternal como evidência da vida eterna.") +
        bloco("👑 Filhos de Deus (3:1-3)", [
            ("1Jo 3:1-3", "Vede que amor nos concedeu o Pai, que fôssemos chamados filhos de Deus; e somos. Por isso o mundo não nos conhece, porque não o conheceu a ele. Amados, agora somos filhos de Deus, e ainda não é manifesto o que haveremos de ser; mas sabemos que, quando ele se manifestar, seremos semelhantes a ele, porque o veremos como ele é.",
             "A identidade presente e futura: somos filhos de Deus agora (<em>tekna theou esmen</em>). O futuro: seremos semelhantes a Cristo (<em>homoioi auto esometha</em>) quando o virmos como ele é. A visão de Cristo nos transformará à sua imagem — a glorificação como contemplação."),
        ]) +
        bloco("💙 O Amor como Evidência (3:14-18)", [
            ("1Jo 3:14-16", "Nós sabemos que já passamos da morte para a vida, porque amamos os irmãos. Quem não ama o irmão permanece na morte... Nisto conhecemos o amor: que ele deu a sua vida por nós; e nós devemos dar a vida pelos irmãos.",
             "O amor fraternal como evidência da vida eterna: quem ama passou da morte para a vida. O padrão do amor: Cristo deu sua vida (<em>psuchen autou etheken</em>) — o amor que se doa até a morte. O amor cristão não é sentimento — é ação sacrificial.")
        ])),
    4: ("Deus é Amor", "Deus é amor; e quem permanece no amor permanece em Deus, e Deus nele.", "1Jo 4:16",
        intro("1 João 4 é o capítulo do amor — a afirmação mais profunda sobre a natureza de Deus no NT: Deus é amor.") +
        bloco("🌟 Deus é Amor (4:7-21)", [
            ("1Jo 4:8-10", "Aquele que não ama não conhece a Deus; porque Deus é amor. Nisto se manifestou o amor de Deus para conosco: que Deus enviou seu Filho unigênito ao mundo, para que por ele vivêssemos. Nisto está o amor: não em que nós tenhamos amado a Deus, mas em que ele nos amou a nós, e enviou seu Filho como propiciação pelos nossos pecados.",
             "<em>Ho theos agape estin</em> — Deus é amor: não apenas que Deus tem amor ou age com amor, mas que amor é sua natureza essencial. A prova: a encarnação e a cruz. O amor não foi iniciado por nós — Deus amou primeiro (<em>autos protos egapesen hemas</em>). A iniciativa é sempre de Deus."),
            ("1Jo 4:18-19", "No amor não há medo; antes, o perfeito amor lança fora o medo, porque o medo tem pena; e o que teme não é perfeito no amor. Nós amamos a Deus porque ele nos amou primeiro.",
             "O amor perfeito expulsa o medo (<em>ekballei ton phobon</em>). O medo tem 'pena' (<em>kolasin</em> — punição) — é o medo do julgamento. Quando sabemos que somos amados por Deus, o medo do julgamento desaparece. Amamos porque fomos amados — o amor é resposta, não iniciativa.")
        ])),
    5: ("A Vitória da Fé e a Vida Eterna", "Porque tudo o que é nascido de Deus vence o mundo; e esta é a vitória que vence o mundo: a nossa fé.", "1Jo 5:4",
        intro("1 João 5 encerra com a vitória da fé, o testemunho do Espírito, e a certeza da vida eterna.") +
        bloco("🏆 A Vitória da Fé (5:1-12)", [
            ("1Jo 5:4-5", "Porque tudo o que é nascido de Deus vence o mundo; e esta é a vitória que vence o mundo: a nossa fé. Quem é que vence o mundo, senão aquele que crê que Jesus é o Filho de Deus?",
             "A vitória (<em>nike</em>) sobre o mundo: não vitória política ou militar, mas vitória sobre o sistema de valores mundano. O instrumento: a fé em Jesus como Filho de Deus. A fé vence o mundo porque conecta o crente ao Vencedor do mundo (Jo 16:33)."),
            ("1Jo 5:11-12", "E este é o testemunho: que Deus nos deu a vida eterna, e esta vida está no seu Filho. Quem tem o Filho tem a vida; quem não tem o Filho de Deus não tem a vida.",
             "A vida eterna está no Filho — não em rituais, não em méritos, não em experiências. Ter o Filho = ter a vida. Não ter o Filho = não ter a vida. A simplicidade radical do Evangelho: tudo depende do relacionamento com Cristo.")
        ])),
}

def gerar_1joao():
    for num, (titulo, vk, rk, body) in caps_1joao.items():
        html = page("1 João", num, 5, titulo, vk, rk, body, "1joao", "../../../..")
        salvar("1joao", num, html)
    print("✅ 1 João: 5 capítulos gerados")

# ─── 2 JOÃO ────────────────────────────────────────────────────────────────────
caps_2joao = {
    1: ("Amor e Verdade", "E agora rogo-te, senhora, não como escrevendo um novo mandamento, mas o que temos tido desde o princípio: que nos amemos uns aos outros.", "2Jo 1:5",
        intro("2 João é a carta mais curta do NT — 13 versículos. Escrita a uma 'senhora eleita' (provavelmente uma Igreja local), combina amor e verdade como os dois pilares da vida cristã.") +
        bloco("💙 Amor e Verdade (1:4-11)", [
            ("2Jo 1:4-6", "Muito me alegrei por ter encontrado alguns dos teus filhos andando na verdade, como recebemos o mandamento do Pai. E agora rogo-te, senhora, não como escrevendo um novo mandamento, mas o que temos tido desde o princípio: que nos amemos uns aos outros.",
             "O mandamento antigo/novo: amar uns aos outros. Não novo em conteúdo — o mesmo desde o princípio — mas sempre novo em sua aplicação. Amor e verdade são inseparáveis em João: o amor sem verdade é sentimentalismo; a verdade sem amor é legalismo."),
            ("2Jo 1:9-11", "Todo aquele que prevarica e não permanece na doutrina de Cristo não tem a Deus; aquele que permanece na doutrina de Cristo tem tanto o Pai como o Filho. Se alguém vier a vós e não trouxer esta doutrina, não o recebais em casa, nem lhe digais: Bem-vindo!",
             "A doutrina de Cristo como linha divisória: quem permanece nela tem o Pai e o Filho; quem se desvia não tem a Deus. A instrução sobre não receber falsos mestres em casa é sobre hospitalidade como endosso — não sobre hostilidade pessoal.")
        ])),
}

def gerar_2joao():
    for num, (titulo, vk, rk, body) in caps_2joao.items():
        html = page("2 João", num, 1, titulo, vk, rk, body, "2joao", "../../../..")
        salvar("2joao", num, html)
    print("✅ 2 João: 1 capítulo gerado")

# ─── 3 JOÃO ────────────────────────────────────────────────────────────────────
caps_3joao = {
    1: ("Gaio, Diótrefes e Demétrio", "Amado, em tudo desejo que te vá bem, e que tenhas saúde, assim como bem vai à tua alma.", "3Jo 1:2",
        intro("3 João é a carta mais pessoal de João — endereçada a Gaio, um cristão fiel. Contrasta três personagens: Gaio (hospitaleiro), Diótrefes (dominador) e Demétrio (testemunhado).") +
        bloco("💙 Três Personagens (1:1-14)", [
            ("3Jo 1:2", "Amado, em tudo desejo que te vá bem, e que tenhas saúde, assim como bem vai à tua alma.",
             "A saudação mais pessoal do NT: o desejo de prosperidade física e saúde ligado ao bem-estar da alma. A saúde espiritual é o padrão para a saúde total. João deseja que o exterior corresponda ao interior de Gaio."),
            ("3Jo 1:9-11", "Escrevi algumas palavras à Igreja; mas Diótrefes, que quer ser o primeiro entre eles, não nos recebe. Por isso, se eu for, trarei à memória as obras que ele faz, propalando com palavras maliciosas contra nós; e, não contente com isso, não recebe os irmãos, e proíbe os que querem recebê-los, e os expulsa da Igreja.",
             "Diótrefes — o primeiro caso documentado de autoritarismo eclesiástico. Características: (1) quer ser o primeiro (<em>philoproteuon</em>); (2) não recebe a autoridade apostólica; (3) fala maliciosamente; (4) não hospeda os irmãos; (5) expulsa os que o fazem. O amor ao poder é incompatível com o amor aos irmãos.")
        ])),
}

def gerar_3joao():
    for num, (titulo, vk, rk, body) in caps_3joao.items():
        html = page("3 João", num, 1, titulo, vk, rk, body, "3joao", "../../../..")
        salvar("3joao", num, html)
    print("✅ 3 João: 1 capítulo gerado")

# ─── JUDAS ─────────────────────────────────────────────────────────────────────
caps_judas = {
    1: ("Contender pela Fé", "Amados, senti a necessidade de vos escrever exortando-vos a combater pela fé que uma vez foi dada aos santos.", "Jd 1:3",
        intro("Judas é a carta mais urgente do NT — um chamado apaixonado a defender a fé contra falsos mestres que infiltraram a Igreja.") +
        bloco("⚔️ Contender pela Fé (1:3-23)", [
            ("Jd 1:3-4", "Amados, senti a necessidade de vos escrever exortando-vos a combater pela fé que uma vez foi dada aos santos. Porque se introduziram furtivamente alguns homens, que já antes estavam destinados para esta condenação, ímpios, que convertem a graça do nosso Deus em dissolução, e negam o único Soberano Deus e nosso Senhor Jesus Cristo.",
             "A fé 'uma vez dada' (<em>hapax paradotheise</em>) — o depósito imutável do Evangelho. Contender (<em>epagonizesthai</em>) — lutar agonisticamente pela fé. Os falsos mestres: (1) infiltrados furtivamente; (2) convertem a graça em libertinagem; (3) negam Cristo. A graça não é licença para o pecado — é poder para a santidade."),
            ("Jd 1:20-21", "Mas vós, amados, edificando-vos sobre a vossa santíssima fé, orando no Espírito Santo, conservai-vos no amor de Deus, esperando a misericórdia de nosso Senhor Jesus Cristo para a vida eterna.",
             "A resposta positiva à ameaça: (1) edificar-se na fé; (2) orar no Espírito Santo; (3) permanecer no amor de Deus; (4) esperar a misericórdia de Cristo. A vida cristã é ativa — não apenas evitar o erro, mas crescer na fé."),
            ("Jd 1:24-25", "Ora, àquele que é poderoso para vos guardar de tropeçar, e apresentar-vos irrepreensíveis perante a sua glória com grande alegria, ao único Deus sábio, nosso Salvador, seja glória e majestade, domínio e poder, agora e em todos os séculos. Amém.",
             "A doxologia final de Judas é uma das mais belas do NT. Deus é 'poderoso para guardar de tropeçar' (<em>dynato phylaxai aptaistous</em>) — a perseverança é obra de Deus, não apenas do crente. A apresentação final: irrepreensíveis, com grande alegria, diante da glória de Deus.")
        ])),
}

def gerar_judas():
    for num, (titulo, vk, rk, body) in caps_judas.items():
        html = page("Judas", num, 1, titulo, vk, rk, body, "judas", "../../../..")
        salvar("judas", num, html)
    print("✅ Judas: 1 capítulo gerado")

# ─── APOCALIPSE ────────────────────────────────────────────────────────────────
def gerar_apocalipse():
    caps_apoc = {
        1: ("A Revelação de Jesus Cristo", "Eu sou o Alfa e o Ômega, o primeiro e o último, o princípio e o fim.", "Ap 1:8",
            intro("Apocalipse é o livro mais simbólico do NT — uma revelação (<em>apokalypsis</em>) dada a João em Patmos (~95 d.C.). O cap. 1 apresenta a visão inaugural de Cristo glorificado.") +
            bloco("👑 A Visão de Cristo Glorificado (1:12-20)", [
                ("Ap 1:12-16", "E voltei-me para ver a voz que falava comigo; e, voltando-me, vi sete candeeiros de ouro; e no meio dos sete candeeiros um semelhante ao Filho do Homem, vestido até aos pés, e cingido pelos peitos com um cinto de ouro. E a sua cabeça e cabelos eram brancos como lã branca, como neve; e os seus olhos como chama de fogo.",
                 "A visão de Cristo glorificado combina imagens de Daniel 7 (Filho do Homem), Daniel 10 (o ser celestial) e Ezequiel 1 (a glória divina). Cada elemento é simbólico: vestes sacerdotais, cabelos brancos (eternidade/sabedoria), olhos de fogo (onisciência penetrante), pés de bronze (julgamento), voz de muitas águas (majestade irresistível), espada da boca (Palavra de Deus)."),
                ("Ap 1:17-18", "E quando o vi, caí a seus pés como morto; e ele pôs sobre mim a sua mão direita, dizendo-me: Não temas; eu sou o primeiro e o último, e o que vivo, e fui morto; e eis que estou vivo pelos séculos dos séculos. Amém. E tenho as chaves da morte e do inferno.",
                 "A reação de João (cair como morto) é a resposta adequada à visão da glória divina (cf. Is 6, Ez 1, Dn 10). Cristo se identifica: Primeiro e Último (divindade eterna), Vivo que foi morto (encarnação e crucificação), Vivo para sempre (ressurreição e exaltação), Detentor das chaves da morte e do Hades (soberania sobre a morte).")
            ])),
        2: ("Cartas às Sete Igrejas I", "Ao que vencer, dar-lhe-ei que coma da árvore da vida, que está no meio do paraíso de Deus.", "Ap 2:7",
            intro("Apocalipse 2-3 contém as sete cartas às igrejas da Ásia Menor — cada uma com diagnóstico, elogio/repreensão, chamado e promessa ao vencedor. O cap. 2 cobre Éfeso, Esmirna, Pérgamo e Tiatira.") +
            bloco("📜 Éfeso, Esmirna, Pérgamo, Tiatira (2:1-29)", [
                ("Ap 2:4-5", "Tenho, porém, contra ti que abandonaste o teu primeiro amor. Lembra-te, pois, de onde caíste, e arrepende-te, e pratica as primeiras obras; e, se não fizeres isso, virei a ti e moverei o teu candeeiro do seu lugar, se não te arrependeres.",
                 "Éfeso: ortodoxa mas sem amor. O 'primeiro amor' (<em>ten agapen sou ten proten</em>) — o amor inicial pela Cristo e pelos irmãos. A perda do amor é queda espiritual mesmo com doutrina correta. O remédio: lembrar, arrepender, retornar às primeiras obras."),
                ("Ap 2:10", "Não temas as coisas que tens de sofrer. Eis que o diabo há de lançar alguns de vós na prisão, para serdes tentados; e tereis tribulação de dez dias. Sê fiel até à morte, e dar-te-ei a coroa da vida.",
                 "Esmirna: a Igreja perseguida sem repreensão. 'Sê fiel até à morte' (<em>ginou pistos achri thanatou</em>) — não 'até o fim da vida', mas 'mesmo que custe a vida'. A coroa da vida (<em>stephanos tes zoes</em>) é a recompensa do mártir.")
            ])),
        3: ("Cartas às Sete Igrejas II", "Eis que estou à porta e bato; se alguém ouvir a minha voz e abrir a porta, entrarei em sua casa.", "Ap 3:20",
            intro("Apocalipse 3 conclui as sete cartas com Sardes, Filadélfia e Laodiceia — a mais famosa sendo Laodiceia, a Igreja morna.") +
            bloco("📜 Sardes, Filadélfia, Laodiceia (3:1-22)", [
                ("Ap 3:1-2", "Conheço as tuas obras, que tens nome de que vives, e estás morto. Sê vigilante, e confirma as coisas restantes, que estão a ponto de morrer; porque não achei as tuas obras perfeitas diante de Deus.",
                 "Sardes: a Igreja morta com reputação de viva. O diagnóstico mais severo: nome de vida, realidade de morte. O remédio: vigilância, confirmação do que resta, memória do que recebeu, arrependimento."),
                ("Ap 3:15-17", "Conheço as tuas obras, que nem és frio nem quente. Quem dera fosses frio ou quente! Assim, porque és morno, e não és frio nem quente, estou a ponto de te vomitar da minha boca. Porque dizes: Sou rico, e estou enriquecido, e não tenho necessidade de coisa alguma; e não sabes que és um infeliz, miserável, pobre, cego e nu.",
                 "Laodiceia: a Igreja morna. A mornidão é mais repulsiva que o frio ou o quente — a indiferença espiritual é o pior estado. A autopercepção (rica, sem necessidade) contrasta com a realidade divina (miserável, pobre, cega, nua). A riqueza material pode mascarar a pobreza espiritual."),
                ("Ap 3:20", "Eis que estou à porta e bato; se alguém ouvir a minha voz e abrir a porta, entrarei em sua casa, e cearei com ele, e ele comigo.",
                 "O versículo mais famoso do Apocalipse — frequentemente usado evangelisticamente. No contexto, é dirigido à Igreja, não a não-crentes: Cristo está do lado de fora de sua própria Igreja! A ceia (<em>deipneson</em>) é imagem de comunhão íntima. A porta é aberta de dentro — a iniciativa humana responde ao chamado divino.")
            ])),
        4: ("O Trono de Deus no Céu", "Santo, Santo, Santo é o Senhor Deus Todo-Poderoso, que era, e que é, e que há de vir.", "Ap 4:8",
            intro("Apocalipse 4 é a visão do trono celestial — o fundamento de toda a profecia do Apocalipse. Antes de revelar os julgamentos da terra, João vê a soberania absoluta de Deus.") +
            bloco("👑 O Trono Celestial (4:1-11)", [
                ("Ap 4:2-3", "E logo fui arrebatado em espírito; e eis que um trono estava posto no céu, e um assentado sobre o trono. E aquele que estava assentado era semelhante, no aspecto, a uma pedra de jaspe e de sardônica; e o arco-íris ao redor do trono era semelhante, no aspecto, a uma esmeralda.",
                 "A visão do trono: Deus não é descrito diretamente — apenas por comparações de pedras preciosas e luz. O arco-íris (aliança, Gn 9) envolve o trono do Juiz — o julgamento é sempre enquadrado pela misericórdia da aliança."),
                ("Ap 4:8-11", "E os quatro animais tinham cada um seis asas, e ao redor e por dentro estavam cheios de olhos; e não descansam nem de dia nem de noite, dizendo: Santo, Santo, Santo é o Senhor Deus Todo-Poderoso, que era, e que é, e que há de vir.",
                 "O Trisagion (<em>hagios hagios hagios</em>) — o hino mais antigo da adoração celestial (cf. Is 6:3). A adoração é contínua, sem descanso. Os 24 anciãos lançam suas coroas — reconhecendo que toda autoridade é delegada, toda glória pertence a Deus.")
            ])),
        5: ("O Cordeiro que foi Morto", "Digno és tu de tomar o livro e de abrir os seus selos; porque foste morto, e com o teu sangue compraste para Deus homens de toda tribo, língua, povo e nação.", "Ap 5:9",
            intro("Apocalipse 5 é o capítulo mais adorável do livro — a exaltação do Cordeiro que foi morto como o único digno de abrir o livro dos destinos.") +
            bloco("🐑 O Cordeiro Exaltado (5:1-14)", [
                ("Ap 5:5-6", "E um dos anciãos me disse: Não chores; eis que o Leão da tribo de Judá, a Raiz de Davi, venceu para abrir o livro e os seus sete selos. E eu vi, e eis que no meio do trono e dos quatro animais, e no meio dos anciãos, estava um Cordeiro como se tivesse sido morto.",
                 "O paradoxo central do Apocalipse: o Leão é o Cordeiro. João ouve 'Leão' (<em>leon</em>) e vê 'Cordeiro' (<em>arnion</em>). A vitória de Cristo não foi por força leonina, mas por sacrifício cordeiro. O Cordeiro 'como se tivesse sido morto' (<em>hos esphagmenon</em>) — as marcas da crucificação são eternas."),
                ("Ap 5:9-10", "E cantavam um novo cântico, dizendo: Digno és tu de tomar o livro e de abrir os seus selos; porque foste morto, e com o teu sangue compraste para Deus homens de toda tribo, língua, povo e nação; e fizeste deles para o nosso Deus um reino e sacerdotes; e eles reinarão sobre a terra.",
                 "O novo cântico (<em>oden kainen</em>) — novo porque baseado na redenção, não apenas na criação. A redenção é universal: toda tribo, língua, povo e nação. O resultado: um reino de sacerdotes — o cumprimento de Ex 19:6 em escala cósmica.")
            ])),
        6: ("Os Seis Primeiros Selos", "E dizia-se a eles que descansassem ainda um pouco de tempo.", "Ap 6:11",
            intro("Apocalipse 6 abre os seis primeiros selos — os quatro cavaleiros do Apocalipse e os mártires sob o altar.") +
            bloco("🐴 Os Quatro Cavaleiros (6:1-8)", [
                ("Ap 6:1-2", "E eu vi quando o Cordeiro abriu um dos selos; e ouvi um dos quatro animais dizer, como em voz de trovão: Vem e vê. E olhei, e eis um cavalo branco; e o que estava assentado sobre ele tinha um arco; e foi-lhe dada uma coroa, e saiu vencendo, e para vencer.",
                 "Os quatro cavaleiros representam forças históricas recorrentes: branco (conquista/falsa paz), vermelho (guerra), preto (fome/escassez), amarelo/pálido (morte e Hades). Não são eventos únicos futuros — são realidades que marcam toda a era entre as duas vindas de Cristo."),
                ("Ap 6:9-11", "E quando abriu o quinto selo, vi debaixo do altar as almas dos que tinham sido mortos por causa da palavra de Deus, e por causa do testemunho que sustentavam. E clamavam com grande voz, dizendo: Até quando, ó Soberano Senhor, santo e verdadeiro, não julgas e vingas o nosso sangue sobre os que habitam na terra?",
                 "Os mártires sob o altar: a morte dos santos é um sacrifício (<em>thysiasterion</em> — altar de sacrifício). O clamor 'até quando?' é a oração dos mártires por justiça. A resposta: descanso e espera — o julgamento virá no tempo de Deus.")
            ])),
        7: ("Os 144.000 e a Grande Multidão", "Estes são os que vieram da grande tribulação, e lavaram as suas vestes, e as alvejaram no sangue do Cordeiro.", "Ap 7:14",
            intro("Apocalipse 7 é o interlúdio entre o sexto e sétimo selos — a visão dos 144.000 selados e da multidão incontável de todas as nações.") +
            bloco("🌟 A Grande Multidão (7:9-17)", [
                ("Ap 7:9-10", "Depois destas coisas olhei, e eis uma grande multidão, que ninguém podia contar, de todas as nações, e tribos, e povos, e línguas, que estavam diante do trono e diante do Cordeiro, vestidos de vestiduras brancas, e com palmas nas suas mãos; e clamavam com grande voz, dizendo: A salvação pertence ao nosso Deus, que está assentado no trono, e ao Cordeiro.",
                 "A multidão incontável (<em>ochlos polys hon arithmesai auton oudeis edynato</em>) — o cumprimento da promessa a Abraão (Gn 15:5). De todas as nações, tribos, povos e línguas — a universalidade da redenção. Vestidos de branco (justiça de Cristo), com palmas (vitória). A adoração: 'A salvação pertence ao nosso Deus e ao Cordeiro' — soberania compartilhada.")
            ])),
        8: ("O Sétimo Selo e as Quatro Primeiras Trombetas", "E houve silêncio no céu por quase meia hora.", "Ap 8:1",
            intro("Apocalipse 8 abre o sétimo selo com silêncio solene, e as primeiras quatro trombetas trazem julgamentos sobre a natureza.") +
            bloco("🎺 As Primeiras Trombetas (8:1-13)", [
                ("Ap 8:1", "E quando abriu o sétimo selo, houve silêncio no céu por quase meia hora.",
                 "O silêncio de meia hora é o momento mais dramático do Apocalipse — o universo prende a respiração antes do julgamento final. O silêncio contrasta com a adoração contínua dos caps. 4-5. A expectativa solene precede a revelação."),
                ("Ap 8:6-7", "E os sete anjos que tinham as sete trombetas se prepararam para as tocar. E o primeiro tocou a sua trombeta, e houve saraiva e fogo misturados com sangue, e foram lançados sobre a terra; e a terça parte da terra se queimou.",
                 "As quatro primeiras trombetas afetam a natureza em 'terças partes' — julgamentos parciais, não totais. Ecoam as pragas do Egito: saraiva (Ex 9), mar em sangue (Ex 7), água amargada, trevas (Ex 10). O padrão do Êxodo: Deus julga os opressores e liberta seu povo.")
            ])),
        9: ("A Quinta e Sexta Trombetas", "E naqueles dias os homens buscarão a morte, e não a acharão.", "Ap 9:6",
            intro("Apocalipse 9 descreve as trombetas mais aterrorizantes — os gafanhotos do abismo e os exércitos de cavalaria demoníaca.") +
            bloco("🦂 A Quinta Trombeta (9:1-12)", [
                ("Ap 9:3-6", "E do fumo saíram gafanhotos sobre a terra, e foi-lhes dado poder, como têm poder os escorpiões da terra. E foi-lhes dito que não danificassem a erva da terra, nem coisa verde alguma, nem árvore alguma, mas somente os homens que não têm o selo de Deus nas suas testas.",
                 "Os gafanhotos do abismo: criaturas híbridas que atormentam mas não matam. Afetam apenas os que não têm o selo de Deus — os selados (cap. 7) são protegidos. O tormento é tão intenso que os homens desejam morrer mas não podem — a morte foge deles.")
            ])),
        10: ("O Anjo Poderoso e o Livrinho", "E tomei o livrinho da mão do anjo, e o comi; e era na minha boca doce como mel, mas, depois que o comi, o meu ventre se tornou amargo.", "Ap 10:10",
            intro("Apocalipse 10 é o segundo interlúdio — João recebe o livrinho e é comissionado para profetizar novamente.") +
            bloco("📖 O Livrinho (10:8-11)", [
                ("Ap 10:9-11", "E fui ter com o anjo, dizendo-lhe que me desse o livrinho. E ele me disse: Toma-o e come-o; e ele te amarguará o ventre, mas na tua boca será doce como mel. E tomei o livrinho da mão do anjo, e o comi; e era na minha boca doce como mel, mas, depois que o comi, o meu ventre se tornou amargo.",
                 "O livrinho comido ecoa Ezequiel 3:1-3. A Palavra de Deus é doce na boca (promessas, consolo, glória) mas amarga no ventre (julgamento, sofrimento, perseguição). A profecia verdadeira não é apenas confortante — inclui o julgamento que amarga.")
            ])),
        11: ("As Duas Testemunhas e o Sétimo Trombeta", "O reino do mundo passou a ser de nosso Senhor e do seu Cristo.", "Ap 11:15",
            intro("Apocalipse 11 apresenta as duas testemunhas (Moisés e Elias redivivos?), seu martírio e ressurreição, e o sétimo trombeta que proclama o reino de Cristo.") +
            bloco("🌟 O Sétimo Trombeta (11:15-19)", [
                ("Ap 11:15", "E o sétimo anjo tocou a sua trombeta; e houve no céu grandes vozes, dizendo: O reino do mundo passou a ser de nosso Senhor e do seu Cristo, e ele reinará pelos séculos dos séculos.",
                 "A proclamação mais gloriosa do Apocalipse: o reino do mundo tornou-se do Senhor e de seu Cristo. O tempo verbal (<em>egeneto</em> — aoristo) indica certeza profética: já aconteceu na perspectiva celestial, embora ainda se desdobre na história. A soberania de Cristo é a realidade fundamental do universo.")
            ])),
        12: ("A Mulher, o Dragão e o Filho", "E eles o venceram pelo sangue do Cordeiro e pela palavra do seu testemunho.", "Ap 12:11",
            intro("Apocalipse 12 é o capítulo mais dramático — a guerra cósmica entre a mulher (Israel/Igreja), o dragão (Satanás) e o Filho (Cristo).") +
            bloco("🐉 A Guerra Cósmica (12:7-12)", [
                ("Ap 12:7-9", "E houve batalha no céu: Miguel e os seus anjos batalharam contra o dragão; e o dragão e os seus anjos batalharam, mas não prevaleceram, e já não se achou lugar para eles no céu. E foi precipitado o grande dragão, a antiga serpente, que se chama Diabo e Satanás, o sedutor de todo o mundo.",
                 "A guerra no céu: Miguel vs. o dragão. A derrota de Satanás no céu é resultado da vitória de Cristo na cruz (cf. Jo 12:31 — 'agora o príncipe deste mundo será expulso'). A queda de Satanás do céu é consequência da ascensão de Cristo."),
                ("Ap 12:11", "E eles o venceram pelo sangue do Cordeiro e pela palavra do seu testemunho; e não amaram as suas vidas até à morte.",
                 "A fórmula da vitória cristã: sangue do Cordeiro (a obra de Cristo) + palavra do testemunho (a proclamação fiel) + não amar a vida até à morte (disposição martirial). A vitória sobre Satanás é alcançada não por poder militar, mas por fidelidade ao Evangelho.")
            ])),
        13: ("As Duas Bestas", "Aqui está a sabedoria. Quem tem entendimento, calcule o número da besta; porque é o número de um homem, e o seu número é seiscentos e sessenta e seis.", "Ap 13:18",
            intro("Apocalipse 13 apresenta as duas bestas — o Anticristo político (do mar) e o Falso Profeta religioso (da terra) — a tríade satânica que imita a Trindade.") +
            bloco("🐉 As Duas Bestas (13:1-18)", [
                ("Ap 13:1-4", "E vi subir do mar uma besta que tinha sete cabeças e dez chifres, e sobre os seus chifres dez diademas, e sobre as suas cabeças um nome blasfemo... E toda a terra se maravilhou e seguiu a besta; e adoraram o dragão que tinha dado o poder à besta.",
                 "A besta do mar: poder político totalitário que exige adoração. Combina as quatro bestas de Daniel 7 — síntese de todos os impérios opressores. As sete cabeças são sete reis/impérios; os dez chifres são dez reis futuros. A adoração da besta é adoração do dragão — o poder político sem Deus é poder satânico."),
                ("Ap 13:18", "Aqui está a sabedoria. Quem tem entendimento, calcule o número da besta; porque é o número de um homem, e o seu número é seiscentos e sessenta e seis.",
                 "666 — o número mais famoso da Bíblia. Em gematria hebraica, 'Nero César' = 666. Mas o significado é mais profundo: 7 é o número da perfeição divina; 6 é o número humano (criado no sexto dia). 666 é a humanidade exaltada ao máximo sem Deus — a perfeição falsa, a divindade usurpada.")
            ])),
        14: ("O Cordeiro e os 144.000 — A Colheita", "Bem-aventurados os mortos que daqui em diante morrem no Senhor.", "Ap 14:13",
            intro("Apocalipse 14 é o contraponto ao cap. 13 — os 144.000 com o Cordeiro, os três anjos com o Evangelho eterno, e a colheita do mundo.") +
            bloco("🌾 A Colheita do Mundo (14:14-20)", [
                ("Ap 14:14-16", "E olhei, e eis uma nuvem branca, e sobre a nuvem estava assentado um semelhante ao Filho do Homem, que tinha sobre a sua cabeça uma coroa de ouro, e na sua mão uma foice afiada. E outro anjo saiu do templo, clamando com grande voz ao que estava assentado sobre a nuvem: Lança a tua foice e ceifa.",
                 "A colheita dupla: a ceifa (salvação dos santos) e a vindima (julgamento dos ímpios). Cristo como ceifeiro — a imagem de Mt 13:39-43 expandida. A colheita é o fim da história — a separação final entre os que pertencem a Cristo e os que pertencem ao mundo.")
            ])),
        15: ("O Cântico de Moisés e do Cordeiro", "Grandes e maravilhosas são as tuas obras, Senhor Deus Todo-Poderoso; justos e verdadeiros são os teus caminhos.", "Ap 15:3",
            intro("Apocalipse 15 é o prelúdio das sete taças — os vencedores cantam o cântico de Moisés e do Cordeiro antes do julgamento final.") +
            bloco("🎵 O Cântico dos Vencedores (15:2-4)", [
                ("Ap 15:3-4", "E cantavam o cântico de Moisés, servo de Deus, e o cântico do Cordeiro, dizendo: Grandes e maravilhosas são as tuas obras, Senhor Deus Todo-Poderoso; justos e verdadeiros são os teus caminhos, ó Rei dos santos. Quem não te temerá, ó Senhor, e não glorificará o teu nome?",
                 "O cântico de Moisés (Êxodo 15 — vitória no Mar Vermelho) + cântico do Cordeiro = o Êxodo definitivo. Os vencedores cantam antes do julgamento — a certeza da vitória é tão grande que a adoração precede o cumprimento. Os atributos de Deus: obras maravilhosas, caminhos justos e verdadeiros, Rei dos santos.")
            ])),
        16: ("As Sete Taças da Ira de Deus", "Eis que venho como ladrão. Bem-aventurado o que vigia e guarda as suas vestes.", "Ap 16:15",
            intro("Apocalipse 16 descreve as sete taças da ira de Deus — o julgamento mais intenso do Apocalipse, ecoando as pragas do Egito em escala global.") +
            bloco("🏺 As Sete Taças (16:1-21)", [
                ("Ap 16:1-2", "E ouvi uma grande voz do templo, que dizia aos sete anjos: Ide e derramai sobre a terra as sete taças da ira de Deus. E foi o primeiro, e derramou a sua taça sobre a terra; e veio uma chaga maligna e dolorosa sobre os homens que tinham o sinal da besta.",
                 "As sete taças são o julgamento completo e final — diferente dos selos e trombetas (que eram parciais, 'terças partes'), as taças são totais. Ecoam as pragas do Egito: chagas, mar em sangue, rios em sangue, calor do sol, trevas, Eufrates seco, grande terremoto."),
                ("Ap 16:9", "E os homens foram queimados com grande calor, e blasfemaram o nome de Deus, que tem poder sobre estas pragas; e não se arrependeram para lhe dar glória.",
                 "A resposta humana ao julgamento: não arrependimento, mas blasfêmia. O julgamento não produz automaticamente arrependimento — o coração endurecido blasfema mesmo diante da ira de Deus. A liberdade humana persiste mesmo no julgamento.")
            ])),
        17: ("A Grande Prostituta", "E na sua testa estava escrito um nome: Mistério, Babilônia, a Grande, a Mãe das Prostitutas.", "Ap 17:5",
            intro("Apocalipse 17 apresenta a Grande Prostituta — Babilônia, símbolo de todo sistema político-religioso que seduz os povos com poder e riqueza.") +
            bloco("🌆 Babilônia a Grande (17:1-18)", [
                ("Ap 17:3-5", "E levou-me em espírito ao deserto; e vi uma mulher assentada sobre uma besta de cor de escarlate, cheia de nomes de blasfêmia, e que tinha sete cabeças e dez chifres... E na sua testa estava escrito um nome: Mistério, Babilônia, a Grande, a Mãe das Prostitutas e das Abominações da Terra.",
                 "Babilônia é o símbolo de Roma imperial para os primeiros leitores, mas transcende qualquer identificação histórica única. É o sistema de poder humano que se opõe a Deus: sedutora (prostituta), embriagada com sangue dos santos, sustentada pelo poder político (a besta). Todo sistema que exige lealdade absoluta é Babilônia.")
            ])),
        18: ("A Queda de Babilônia", "Saí dela, povo meu, para que não sejais participantes dos seus pecados.", "Ap 18:4",
            intro("Apocalipse 18 é o lamento pela queda de Babilônia — os reis, mercadores e marinheiros choram a destruição do sistema econômico mundial.") +
            bloco("💔 O Lamento pela Queda (18:9-20)", [
                ("Ap 18:11-13", "E os mercadores da terra chorarão e se lamentarão sobre ela, porque já ninguém compra as suas mercadorias; mercadorias de ouro, e de prata, e de pedras preciosas, e de pérolas, e de linho fino, e de púrpura, e de seda, e de escarlate... e corpos e almas de homens.",
                 "A lista de mercadorias de Babilônia termina com 'corpos e almas de homens' — o sistema econômico que trata pessoas como mercadoria. A escravidão é o símbolo máximo da desumanização do sistema babilônico. O lamento dos mercadores é pelo lucro perdido, não pelas pessoas.")
            ])),
        19: ("As Bodas do Cordeiro e o Cavaleiro Branco", "Porque o Senhor nosso Deus Todo-Poderoso reina. Alegremo-nos e regozijemo-nos, e demos-lhe glória.", "Ap 19:6-7",
            intro("Apocalipse 19 é o capítulo da vitória — as bodas do Cordeiro e a vinda de Cristo como Rei dos reis e Senhor dos senhores.") +
            bloco("🎊 As Bodas do Cordeiro (19:6-10)", [
                ("Ap 19:6-8", "E ouvi como a voz de uma grande multidão, e como a voz de muitas águas, e como a voz de grandes trovões, dizendo: Aleluia! porque já o Senhor nosso Deus Todo-Poderoso reina. Alegremo-nos e regozijemo-nos, e demos-lhe glória; porque já são chegadas as bodas do Cordeiro, e a sua esposa já se aprontou.",
                 "O Aleluia quádruplo (19:1,3,4,6) — o único uso de 'Aleluia' no NT, e aparece quatro vezes em sequência. As bodas do Cordeiro: a consumação da história da redenção. A noiva (a Igreja) se aprontou — vestida de linho fino, brilhante e puro (as obras justas dos santos).")
            ]) +
            bloco("👑 O Cavaleiro Branco (19:11-21)", [
                ("Ap 19:11-13", "E vi o céu aberto, e eis um cavalo branco, e o que estava assentado sobre ele se chama Fiel e Verdadeiro, e julga e peleja com justiça. E os seus olhos eram como chama de fogo, e na sua cabeça havia muitos diademas; e tinha um nome escrito que ninguém sabia, senão ele mesmo. E estava vestido de uma veste tingida em sangue, e o seu nome é chamado o Verbo de Deus.",
                 "O Cavaleiro Branco é Cristo — identificado por quatro nomes: Fiel e Verdadeiro, o nome desconhecido, o Verbo de Deus, Rei dos reis e Senhor dos senhores. A veste tingida em sangue é seu próprio sangue (a cruz), não o sangue dos inimigos. Ele vence pelo sacrifício, não pela violência.")
            ])),
        20: ("O Milênio e o Juízo Final", "E vi os mortos, grandes e pequenos, que estavam diante do trono; e os livros foram abertos.", "Ap 20:12",
            intro("Apocalipse 20 é o capítulo mais debatido do Apocalipse — o milênio, a soltura de Satanás, e o Grande Trono Branco do Juízo Final.") +
            bloco("👑 O Milênio (20:1-10)", [
                ("Ap 20:1-3", "E vi descer do céu um anjo, que tinha a chave do abismo e uma grande cadeia na mão. E prendeu o dragão, a antiga serpente, que é o Diabo e Satanás, e amarrou-o por mil anos; e lançou-o no abismo, e o fechou, e pôs selo sobre ele, para que não enganasse mais as nações.",
                 "O milênio (mil anos) é o período mais debatido da escatologia cristã. Três posições: pré-milenismo (Cristo vem antes do milênio), pós-milenismo (Cristo vem depois), amilenismo (o milênio é simbólico, a era atual). O que é certo: Satanás será definitivamente derrotado, Cristo reinará, os santos participarão do reino."),
            ]) +
            bloco("⚖️ O Grande Trono Branco (20:11-15)", [
                ("Ap 20:12-15", "E vi os mortos, grandes e pequenos, que estavam diante do trono; e os livros foram abertos; e abriu-se outro livro, que é o da vida; e os mortos foram julgados pelas coisas que estavam escritas nos livros, segundo as suas obras. E o mar deu os mortos que nele havia; e a morte e o inferno deram os mortos que neles havia; e foram julgados cada um segundo as suas obras.",
                 "O Juízo Final: todos os mortos ressuscitam para o julgamento. Dois livros: os livros das obras (registro de toda ação humana) e o Livro da Vida (os redimidos). O critério: obras — mas a salvação é pelo Livro da Vida (graça). O lago de fogo é a 'segunda morte' — separação eterna de Deus.")
            ])),
        21: ("A Nova Criação", "E vi um novo céu e uma nova terra; porque já o primeiro céu e a primeira terra tinham passado.", "Ap 21:1",
            intro("Apocalipse 21 é o capítulo mais esperançoso da Bíblia — a visão da nova criação, da Nova Jerusalém e da habitação eterna de Deus com os homens.") +
            bloco("🌟 A Nova Criação (21:1-8)", [
                ("Ap 21:3-5", "E ouvi uma grande voz do céu, dizendo: Eis aqui o tabernáculo de Deus com os homens, pois ele habitará com eles, e eles serão o seu povo, e o mesmo Deus estará com eles, e será o seu Deus. E Deus limpará de seus olhos toda a lágrima; e não haverá mais morte, nem pranto, nem clamor, nem dor; porque já as primeiras coisas são passadas.",
                 "O cumprimento de toda a história da redenção: Deus habitando com os homens. A fórmula da aliança ('eu serei o seu Deus, eles serão meu povo') finalmente cumprida em plenitude. Cinco negações: não mais morte, pranto, clamor, dor, primeiras coisas. A nova criação é definida pelo que não haverá mais.")
            ]) +
            bloco("🏙️ A Nova Jerusalém (21:9-27)", [
                ("Ap 21:22-23", "E não vi nenhum templo nela; porque o seu templo é o Senhor Deus Todo-Poderoso e o Cordeiro. E a cidade não tem necessidade de sol nem de lua para luzir nela; porque a glória de Deus a ilumina, e o seu candeeiro é o Cordeiro.",
                 "A Nova Jerusalém não tem templo — porque Deus mesmo é o templo. A ausência do templo é a presença total de Deus. Não há sol nem lua — a glória de Deus é a luz eterna. O Cordeiro é o candeeiro (<em>lychnos</em>) — Cristo ilumina a nova criação com sua própria glória.")
            ])),
        22: ("O Rio da Vida e o Convite Final", "Vem! E o que tem sede venha; e quem quiser, receba de graça a água da vida.", "Ap 22:17",
            intro("Apocalipse 22 é o capítulo final da Bíblia — o rio da vida, as últimas promessas de Cristo, e o convite eterno ao Evangelho.") +
            bloco("🌊 O Rio da Vida (22:1-5)", [
                ("Ap 22:1-2", "E mostrou-me um rio puro de água da vida, brilhante como cristal, que procedia do trono de Deus e do Cordeiro. No meio da sua praça, e de um e de outro lado do rio, estava a árvore da vida, que produz doze frutos, dando seu fruto de mês em mês; e as folhas da árvore são para a saúde das nações.",
                 "O rio da vida ecoa Ez 47 e Gn 2 — a nova criação restaura o Éden e o supera. A árvore da vida (negada em Gn 3:24) agora está acessível a todos. Os doze frutos mensais — abundância contínua, nunca escassez. As folhas para a saúde das nações — a cura de toda divisão e conflito humano.")
            ]) +
            bloco("🔔 O Convite Final (22:12-21)", [
                ("Ap 22:12-13", "E eis que venho sem demora, e o meu galardão está comigo, para recompensar a cada um segundo as suas obras. Eu sou o Alfa e o Ômega, o primeiro e o último, o princípio e o fim.",
                 "Cristo se identifica como Alfa e Ômega — o mesmo título dado a Deus em 1:8. A vinda é iminente (<em>tachy</em> — sem demora). O galardão é proporcional às obras — não como mérito de salvação, mas como recompensa de fidelidade."),
                ("Ap 22:17-20", "E o Espírito e a esposa dizem: Vem! E o que ouve, diga: Vem! E o que tem sede venha; e quem quiser, receba de graça a água da vida... Aquele que testifica estas coisas diz: Certamente venho sem demora. Amém! Vem, Senhor Jesus!",
                 "O convite final da Bíblia: o Espírito e a Igreja convidam o mundo. A água da vida é gratuita (<em>dorean</em>) — o Evangelho não tem preço. A última oração da Bíblia: 'Vem, Senhor Jesus!' (<em>Erchou Kyrie Iesou</em>) — a oração da Igreja através dos séculos. A Bíblia termina com um convite e uma promessa.")
            ])),
    }
    for num, (titulo, vk, rk, body) in caps_apoc.items():
        html = page("Apocalipse", num, 22, titulo, vk, rk, body, "apocalipse", "../../../..")
        salvar("apocalipse", num, html)
    print("✅ Apocalipse: 22 capítulos gerados")

if __name__ == "__main__":
    gerar_tiago()
    gerar_1pedro()
    gerar_2pedro()
    gerar_1joao()
    gerar_2joao()
    gerar_3joao()
    gerar_judas()
    gerar_apocalipse()
    print("\n🎉 Fase 4 concluída: Tiago + 1-2Pedro + 1-3João + Judas + Apocalipse = 43 capítulos aprofundados")
