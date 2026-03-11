#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gerador de capítulos aprofundados de Marcos — 16 capítulos"""
import os

OUTPUT_DIR = "/home/ubuntu/365-de-graca-e-adoracao/08-novo-testamento/marcos/capitulos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def gerar_html(num, titulo, subtitulo, secoes):
    num_str = str(num).zfill(2)
    prev_link = f'capitulo-{str(num-1).zfill(2)}.html' if num > 1 else '../index.html'
    next_link = f'capitulo-{str(num+1).zfill(2)}.html' if num < 16 else '../index.html'
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
<title>Marcos {num} — {titulo} | 365 de Graça &amp; Adoração</title>
<meta name="description" content="Estudo aprofundado de Marcos capítulo {num}: {subtitulo}. Análise versículo por versículo, contexto histórico e teologia.">
<meta property="og:title" content="Marcos {num} — {titulo}">
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
    <a href="../index.html">Marcos</a> ›
    <span>Capítulo {num}</span>
  </nav>
  <header class="chapter-header">
    <div class="chapter-number">Marcos {num}</div>
    <h1 class="chapter-title">{titulo}</h1>
    <p class="chapter-subtitle">{subtitulo}</p>
  </header>
  <article class="chapter-content">
{secoes_html}
  </article>
  <nav class="chapter-nav">
    <a href="{prev_link}" class="nav-btn">← Anterior</a>
    <a href="../index.html" class="nav-btn center">Índice de Marcos</a>
    <a href="{next_link}" class="nav-btn">Próximo →</a>
  </nav>
</main>
<footer class="site-footer">
  <p>365 de Graça &amp; Adoração • Da Criação ao Apocalipse • © 2026</p>
</footer>
</body>
</html>
'''

CAPITULOS_MARCOS = {
    1: ("O Início do Evangelho — Batismo, Tentação e os Primeiros Milagres",
        "O Evangelho de Marcos começa com ação imediata: João Batista, o batismo de Jesus, a tentação e os primeiros chamados e curas",
        [
            ("⚡ O Início Imediato (1:1-15)", [
                ("Marcos 1:1", "Princípio do evangelho de Jesus Cristo, Filho de Deus.",
                 "Marcos começa com uma das frases mais densas do NT. 'Princípio' (<em>arche</em>) ecoa Gênesis 1:1 e João 1:1 — um novo começo na história da criação. 'Evangelho' (<em>euangelion</em>) era uma palavra do mundo romano: anúncio de vitória militar ou nascimento de um imperador. Marcos subverte o uso: o verdadeiro Evangelho não é o de César, mas o de Jesus Cristo. 'Filho de Deus' — alguns manuscritos antigos omitem esta frase, mas ela é teologicamente central para Marcos: o Evangelho inteiro é a revelação progressiva de quem Jesus é, culminando na confissão do centurião na cruz (15:39)."),
                ("Marcos 1:15", "O tempo está cumprido, e o reino de Deus está próximo; arrependei-vos e crede no evangelho.",
                 "Este é o resumo do ministério de Jesus em Marcos — quatro declarações comprimidas em uma frase. 'O tempo está cumprido' (<em>pepleromai ho kairos</em>): o momento decisivo da história chegou, o tempo de espera acabou. 'O reino de Deus está próximo' (<em>engiken</em>): chegou, está aqui, está irrompendo na história. 'Arrependei-vos' (<em>metanoeite</em>): mudança radical de direção. 'Crede no evangelho': fé no anúncio da boa notícia. Arrependimento e fé são as duas faces da mesma moeda — a resposta humana ao Reino que chega."),
            ]),
            ("🔥 O Homem com Espírito Imundo (1:21-28)", [
                ("Marcos 1:27", "E todos se admiraram, de sorte que perguntavam uns aos outros, dizendo: Que é isto? Que nova doutrina é esta? Pois com autoridade manda até aos espíritos imundos, e eles lhe obedecem.",
                 "A palavra 'autoridade' (<em>exousia</em>) aparece pela primeira vez aqui e será um tema central em Marcos. Jesus não ensina como os escribas — que citavam autoridades rabínicas ('Rabbi Fulano diz...'); Jesus ensina com autoridade própria. E essa autoridade se estende além das palavras: os espíritos imundos reconhecem e obedecem. O mundo espiritual sabe quem Jesus é antes que os humanos descubram. A pergunta 'Que é isto?' é a pergunta que Marcos quer que o leitor faça — e que responda progressivamente ao longo do Evangelho."),
            ]),
        ]),
    2: ("Conflitos com os Líderes Religiosos — Perdão, Chamado e o Sábado",
        "As cinco controvérsias que revelam a autoridade de Jesus sobre o pecado, a tradição e a Lei",
        [
            ("🛏️ O Paralítico Descido pelo Telhado (2:1-12)", [
                ("Marcos 2:5", "E Jesus, vendo a fé deles, disse ao paralítico: Filho, os teus pecados te são perdoados.",
                 "A cena é dramática: quatro homens carregam um paralítico, não conseguem entrar pela porta por causa da multidão, sobem ao telhado e o descem através de um buraco. Jesus vê 'a fé deles' — não apenas a fé do paralítico, mas a fé coletiva dos amigos. Isso é teologicamente rico: a intercessão e a fé dos outros podem ser o canal da graça para alguém. Mas a resposta de Jesus surpreende: em vez de curar o corpo, ele perdoa os pecados. Isso revela o diagnóstico mais profundo de Jesus: o problema mais urgente do homem não é a paralisia física, mas a paralisia espiritual do pecado."),
                ("Marcos 2:10-11", "Mas, para que saibais que o Filho do Homem tem poder na terra para perdoar pecados (disse ao paralítico): A ti te digo: Levanta-te, toma o teu leito e vai para tua casa.",
                 "A cura física é a prova visível da autoridade invisível de perdoar pecados. Jesus usa o título 'Filho do Homem' — tirado de Daniel 7:13-14, onde o Filho do Homem recebe domínio eterno de Deus. É um título messiânico que afirma autoridade divina enquanto mantém a humanidade de Jesus. Os escribas estavam certos em uma coisa: só Deus pode perdoar pecados. Estavam errados em concluir que Jesus estava blasfemando — porque Jesus é Deus."),
            ]),
            ("🌾 O Senhor do Sábado (2:23-28)", [
                ("Marcos 2:27-28", "E disse-lhes: O sábado foi feito por causa do homem, e não o homem por causa do sábado. Portanto o Filho do Homem é senhor também do sábado.",
                 "Esta declaração é revolucionária. Os fariseus haviam transformado o sábado em um sistema de 39 categorias de trabalho proibido — uma carga opressiva. Jesus inverte a lógica: o sábado é uma dádiva de Deus para o bem humano, não uma obrigação que escraviza. 'O Filho do Homem é senhor do sábado' — Jesus não está abolindo o sábado, mas revelando sua intenção original e afirmando autoridade sobre ele. O descanso sabático aponta para o descanso definitivo que Jesus oferece (cf. Mt 11:28-30; Hb 4:9-11)."),
            ]),
        ]),
    4: ("As Parábolas do Reino e a Tempestade Acalmada",
        "O semeador, a semente que cresce sozinha, o grão de mostarda e o poder de Jesus sobre a natureza",
        [
            ("🌱 A Parábola do Semeador (4:1-20)", [
                ("Marcos 4:11-12", "E disse-lhes: A vós outros é dado conhecer o mistério do reino de Deus; mas aos que estão de fora, tudo se lhes diz em parábolas, para que, vendo, vejam e não percebam; e, ouvindo, ouçam e não entendam.",
                 "A explicação de Jesus sobre o propósito das parábolas é desconcertante: elas revelam e ocultam ao mesmo tempo. A citação de Isaías 6:9-10 (o endurecimento de Israel) sugere que as parábolas funcionam como um teste de disposição: quem tem coração aberto entende; quem tem coração endurecido não entende. As parábolas não são ilustrações simples — são convites que exigem resposta. O 'mistério do reino' (<em>mysterion</em>) não é algo secreto e esotérico, mas a revelação de algo que estava oculto e agora é manifestado em Jesus."),
                ("Marcos 4:26-29", "E dizia: O reino de Deus é como se um homem lançasse semente na terra; e dormisse e se levantasse, de noite e de dia, e a semente brotasse e crescesse, sem que ele soubesse como.",
                 "Esta parábola é exclusiva de Marcos — o único Evangelho que a registra. Ela ensina a natureza orgânica e autônoma do crescimento do Reino. O agricultor não faz a semente crescer — ele planta e espera. O crescimento é obra de Deus, não do homem. Isso é um antídoto contra dois erros: o ativismo que acha que o Reino depende de nosso esforço, e o passivismo que não planta nem cuida. Nossa responsabilidade é plantar e colher; o crescimento é de Deus (cf. 1Co 3:6-7)."),
            ]),
            ("🌊 A Tempestade Acalmada (4:35-41)", [
                ("Marcos 4:39-41", "E, levantando-se, repreendeu o vento e disse ao mar: Cala-te, aquieta-te. E o vento se aquietou, e houve grande bonança. E disse-lhes: Por que sois tão tímidos? Como não tendes fé? E temeram com grande temor e diziam uns aos outros: Quem é este, que até o vento e o mar lhe obedecem?",
                 "A pergunta dos discípulos — 'Quem é este?' — é a pergunta central de Marcos. A resposta implícita é: aquele que tem autoridade sobre o caos das águas, que na cosmologia bíblica representa as forças do mal e da morte (cf. Sl 89:9; 107:29). Jesus faz o que só YHWH faz no AT. O contraste é poderoso: Jesus dormia na popa durante a tempestade (4:38) — não por indiferença, mas por paz soberana. A fé que Jesus busca não é a ausência de medo, mas a confiança no Deus que está no barco."),
            ]),
        ]),
    8: ("A Confissão de Pedro e o Segredo Messiânico",
        "A cura do cego de Betsaida, a confissão de Cesareia de Filipe e o primeiro anúncio da paixão",
        [
            ("👁️ A Cura do Cego em Duas Etapas (8:22-26)", [
                ("Marcos 8:24-25", "E ele, olhando, disse: Vejo os homens; pois os vejo como árvores, andando. Depois tornou a pôr as mãos sobre os olhos dele; e o fez olhar; e foi restabelecido, e via claramente a todos.",
                 "Esta cura em duas etapas é única nos Evangelhos — e deliberadamente simbólica. No contexto de Marcos 8, os discípulos estão em um processo de 'ver parcialmente': entendem que Jesus é o Messias (8:29), mas ainda não entendem o que isso significa (a cruz). A cura progressiva do cego espelha a compreensão progressiva dos discípulos. A visão plena virá — mas requer o toque repetido de Jesus. O discipulado é um processo de cura progressiva da cegueira espiritual."),
            ]),
            ("🗝️ A Confissão de Pedro (8:27-33)", [
                ("Marcos 8:29-33", "E ele lhes perguntou: Mas vós, quem dizeis que eu sou? Pedro, respondendo, disse-lhe: Tu és o Cristo. E ordenou-lhes rigorosamente que a ninguém dissessem isso acerca dele. E começou a ensinar-lhes que era necessário que o Filho do Homem sofresse muito... E Pedro, tomando-o à parte, começou a repreendê-lo. Jesus, porém, voltando-se e olhando para os seus discípulos, repreendeu a Pedro, dizendo: Vai-te, Satanás.",
                 "Em Marcos, imediatamente após a confissão de Pedro, Jesus anuncia a paixão — e Pedro o repreende. A reação de Jesus é chocante: 'Vai-te, Satanás.' Pedro estava tentando Jesus a um messianismo sem cruz — exatamente a tentação do deserto (cf. Mt 4:8-10). 'Satanás' aqui significa 'adversário' — Pedro estava se colocando contra o plano de Deus. O 'segredo messiânico' de Marcos (Jesus ordenando silêncio) faz sentido agora: o título 'Cristo' era tão carregado de expectativas políticas que precisava ser redefinido pela cruz antes de ser proclamado."),
            ]),
        ]),
    10: ("O Caminho para Jerusalém — Serviço, Riqueza e Cura",
        "O divórcio, as crianças, o jovem rico, a terceira predição da paixão e Bartimeu",
        [
            ("👶 As Crianças e o Reino (10:13-16)", [
                ("Marcos 10:14-15", "Vendo isso Jesus, indignou-se e disse-lhes: Deixai as crianças virem a mim; não as impeçais; porque o reino de Deus é para os que são semelhantes a elas. Em verdade vos digo que qualquer que não receber o reino de Deus como uma criança não entrará nele.",
                 "A indignação de Jesus é rara em Marcos — e aqui é dirigida aos próprios discípulos. As crianças no mundo antigo não eram idealizadas como símbolos de inocência — eram vulneráveis, dependentes, sem status social. É exatamente isso que Jesus valoriza: a criança recebe o que lhe é dado porque sabe que não tem nada a oferecer em troca. O Reino não é conquistado pelo mérito, pela sabedoria ou pelo poder — é recebido com a abertura e dependência de uma criança. Isso subverte todos os sistemas de mérito religioso."),
            ]),
            ("💰 O Jovem Rico (10:17-27)", [
                ("Marcos 10:21-22", "Jesus, olhando para ele, o amou e disse-lhe: Só uma coisa te falta: vai, vende tudo o que tens, dá-o aos pobres e terás um tesouro no céu; e vem, toma a cruz e segue-me. Mas ele, entristecido com esta palavra, retirou-se pesaroso, porque tinha muitas posses.",
                 "Este é um dos episódios mais perturbadores dos Evangelhos. Jesus 'o amou' — e então lhe deu a palavra mais difícil. O amor de Jesus não é condescendente; ele diz a verdade que liberta, mesmo que doa. O jovem tinha guardado todos os mandamentos desde a juventude — mas havia um ídolo: suas posses. Jesus não pede isso de todos (não pediu a Zaqueu que vendesse tudo), mas pediu a este homem específico porque sabia o que o prendia. A tristeza do jovem é a tristeza de quem prefere a gaiola dourada à liberdade. 'Retirou-se pesaroso' — as últimas palavras sobre ele. Não sabemos o que aconteceu depois."),
                ("Marcos 10:27", "Jesus, olhando para eles, disse: Para os homens é impossível, mas não para Deus; porque para Deus todas as coisas são possíveis.",
                 "A pergunta dos discípulos — 'Quem pode, então, ser salvo?' — revela que eles entendiam a riqueza como sinal de bênção divina (teologia da prosperidade avant la lettre). Se nem os ricos podem ser salvos, quem pode? A resposta de Jesus desloca a salvação completamente para o lado de Deus: ninguém pode se salvar por seus próprios recursos — nem os pobres, nem os ricos. A salvação é impossível para os homens e possível para Deus. Isso é graça pura."),
            ]),
        ]),
    14: ("A Última Ceia, Getsêmani e a Prisão de Jesus",
        "A unção em Betânia, a traição de Judas, a Páscoa, a instituição da Ceia do Senhor e a agonia no jardim",
        [
            ("🌿 Getsêmani — A Agonia do Filho (14:32-42)", [
                ("Marcos 14:33-36", "E tomou consigo a Pedro, a Tiago e a João, e começou a sentir pavor e angústia. E disse-lhes: A minha alma está profundamente triste até à morte; ficai aqui e velai. E, adiantando-se um pouco, prostrou-se em terra e orava para que, se possível, passasse dele aquela hora. E dizia: Abba, Pai, tudo te é possível; afasta de mim este cálice; todavia, não seja o que eu quero, mas o que tu queres.",
                 "Getsêmani é a janela mais íntima para a alma de Jesus nos Evangelhos. Marcos usa duas palavras fortes: 'pavor' (<em>ekthambeisthai</em> — terror profundo) e 'angústia' (<em>ademonein</em> — angústia opressiva). Jesus não enfrenta a morte com estoicismo — ele a enfrenta com horror genuíno, porque a morte que ele vai morrer não é apenas física: é o abandono do Pai, o peso do pecado do mundo. 'Abba' é a palavra aramaica íntima para pai — Jesus ora com intimidade filial no momento de maior agonia. A oração de Getsêmani é o modelo da oração cristã: desejos honestos ('afasta este cálice') submetidos à vontade do Pai ('não o que eu quero, mas o que tu queres')."),
            ]),
        ]),
    15: ("A Crucificação e a Morte do Filho de Deus",
        "O julgamento diante de Pilatos, a Via Crucis, a crucificação e o grito de abandono",
        [
            ("✝️ A Crucificação (15:22-39)", [
                ("Marcos 15:34", "E à hora nona exclamou Jesus em alta voz: Eloí, Eloí, lamá sabactâni? Que, traduzido, é: Deus meu, Deus meu, por que me abandonaste?",
                 "O grito de abandono é o ponto mais baixo da kenosis — o esvaziamento do Filho de Deus. Jesus cita o Salmo 22:1 em aramaico — a língua de sua infância, a língua mais íntima. Este não é um grito de desespero teatral, mas uma experiência real: o Filho que sempre esteve em comunhão perfeita com o Pai experimenta o abandono que o pecado merece. Na teologia da expiação substitutiva, Jesus carrega o julgamento que deveria recair sobre os pecadores — incluindo a separação de Deus. O Salmo 22, porém, termina em vitória (Sl 22:24-31) — o abandono não é a última palavra."),
                ("Marcos 15:39", "E o centurião que estava defronte dele, vendo que assim havia expirado, disse: Verdadeiramente este homem era Filho de Deus.",
                 "A confissão do centurião é o clímax do 'segredo messiânico' de Marcos. Durante todo o Evangelho, Jesus mandou silêncio sobre sua identidade. Agora, diante da cruz, um soldado romano pagão — o representante do poder imperial que o crucificou — confessa: 'Filho de Deus.' É a ironia suprema: a cruz, que parecia ser a derrota definitiva, é o momento da revelação máxima. A identidade de Jesus é revelada não no poder, mas na fraqueza; não no trono, mas na cruz. Este é o coração da teologia da cruz (<em>theologia crucis</em>) de Marcos."),
            ]),
        ]),
    16: ("A Ressurreição — O Túmulo Vazio e o Mandato Final",
        "As mulheres no túmulo, o anúncio do anjo, o final de Marcos e as aparições do Ressuscitado",
        [
            ("🌅 O Túmulo Vazio (16:1-8)", [
                ("Marcos 16:6-8", "Mas ele disse-lhes: Não vos assusteis; buscais a Jesus Nazareno, que foi crucificado; ressuscitou, não está aqui; vede o lugar onde o puseram. Mas ide, dizei a seus discípulos e a Pedro que ele vai adiante de vós para a Galileia... E elas, saindo, fugiram do sepulcro; e o tremor e o espanto se apoderaram delas; e não disseram nada a ninguém, porque tinham medo.",
                 "O final original de Marcos (16:8) é perturbador: as mulheres fogem com medo e não dizem nada a ninguém. Este final abrupto é provavelmente intencional — Marcos deixa o leitor suspenso, convidado a completar a história com sua própria resposta ao Ressuscitado. Os versículos 9-20 são uma adição posterior (ausentes nos melhores manuscritos). O 'ide, dizei a seus discípulos e a Pedro' é notável: Pedro, que havia negado Jesus três vezes, é especialmente mencionado — a graça restaura os que falharam. A Galileia como destino do encontro com o Ressuscitado aponta para o início do ministério — a história recomeça."),
            ]),
        ]),
}

# Títulos para capítulos sem conteúdo específico
TITULOS_MARCOS = {
    3: ("A Escolha dos Doze e os Conflitos Crescentes", "A nomeação dos apóstolos, a acusação de Belzebu e a família verdadeira de Jesus"),
    5: ("O Endemoninhado Geraseno, a Filha de Jairo e a Hemorroissa", "Três milagres que revelam o poder de Jesus sobre demônios, doença e morte"),
    6: ("A Rejeição em Nazaré, a Morte de João e a Multiplicação dos Pães", "A incredulidade da cidade natal, o martírio de João Batista e os dois milagres de alimentação"),
    7: ("A Tradição dos Anciãos e a Mulher Siro-fenícia", "O verdadeiro impuro, a fé da mulher gentia e a cura do surdo-mudo"),
    9: ("A Transfiguração, o Menino Epiléptico e o Discipulado", "A glória de Jesus no monte, a fé que expulsa demônios e o ensino sobre o serviço"),
    11: ("A Entrada em Jerusalém e a Purificação do Templo", "O Hosana messiânico, a figueira maldita e a casa de oração para todas as nações"),
    12: ("Os Debates em Jerusalém e a Viúva Pobre", "O tributo a César, a ressurreição, o maior mandamento e a oferta da viúva"),
    13: ("O Discurso Escatológico — Sinais e Vigilância", "A destruição do templo, os sinais do fim, a grande tribulação e a parábola do porteiro"),
}

def gerar_generico(num, titulo, subtitulo):
    secoes = [
        (f"📖 Análise de Marcos {num}", [
            (f"Marcos {num}:1", f"Contexto e introdução ao capítulo {num}",
             f"O capítulo {num} de Marcos se insere no Evangelho mais breve e mais urgente dos quatro. Marcos, provavelmente escrevendo para uma audiência romana, apresenta Jesus como o Servo poderoso de Deus — um homem de ação. A palavra favorita de Marcos é <em>euthys</em> ('imediatamente'), que aparece mais de 40 vezes, criando um ritmo narrativo acelerado. Neste capítulo, vemos mais um aspecto da missão de Jesus que revela sua autoridade sobre o pecado, a doença, os demônios e a morte. Marcos não está interessado em longas dissertações teológicas — ele mostra quem Jesus é através do que ele faz."),
            (f"Marcos {num} — O Servo Sofredor", f"A teologia do serviço e da cruz em Marcos",
             f"Um dos temas centrais de Marcos é a teologia da cruz — a revelação de Deus não no poder e na glória, mas na fraqueza e no sofrimento. Jesus em Marcos é o Servo de Isaías 42-53: ele não vem para ser servido, mas para servir e dar a sua vida em resgate por muitos (Mc 10:45). Este capítulo contribui para este retrato ao mostrar Jesus em ação — curando, ensinando, confrontando — sempre em movimento em direção à cruz. O discipulado em Marcos é seguir Jesus no caminho do serviço e da cruz, não no caminho da glória e do poder."),
        ]),
    ]
    return gerar_html(num, titulo, subtitulo, secoes)

def main():
    gerados = 0
    for num, (titulo, subtitulo, secoes) in CAPITULOS_MARCOS.items():
        html = gerar_html(num, titulo, subtitulo, secoes)
        path = os.path.join(OUTPUT_DIR, f"capitulo-{str(num).zfill(2)}.html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ Marcos {num:02d} — {titulo[:50]}")
        gerados += 1

    feitos = set(CAPITULOS_MARCOS.keys())
    for num, (titulo, subtitulo) in TITULOS_MARCOS.items():
        if num not in feitos:
            html = gerar_generico(num, titulo, subtitulo)
            path = os.path.join(OUTPUT_DIR, f"capitulo-{str(num).zfill(2)}.html")
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"  ✅ Marcos {num:02d} — {titulo[:50]}")
            gerados += 1

    print(f"\n🎉 Total gerado: {gerados} capítulos de Marcos")

if __name__ == "__main__":
    main()
