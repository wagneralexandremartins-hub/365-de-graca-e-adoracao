#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera capítulos aprofundados das Epístolas Gerais e Apocalipse.
Foco nos capítulos mais importantes de cada livro.
"""

import os

def make_css(color, hero_bg, tag_bg, tag_border, tag_hover):
    return f"""
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: #0f172a; color: #e2e8f0; font-family: 'Georgia', serif; line-height: 1.7; }}
    a {{ color: inherit; text-decoration: none; }}
    .topbar {{ background: rgba(15,23,42,0.97); border-bottom: 1px solid rgba(255,255,255,0.07); padding: 14px 0; position: sticky; top: 0; z-index: 100; }}
    .topbar .inner {{ max-width: 900px; margin: 0 auto; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }}
    .topbar a {{ font-size: 0.85rem; color: #94a3b8; font-weight: 600; transition: color 0.2s; }}
    .topbar a:hover {{ color: {color}; }}
    .hero {{ background: linear-gradient(135deg, #0f172a 0%, {hero_bg} 50%, #0f172a 100%); padding: 64px 24px 48px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.07); }}
    .tag {{ display: inline-block; background: {tag_bg}; border: 1px solid {tag_border}; color: {color}; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 999px; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 1px; }}
    .hero h1 {{ font-size: 2.4rem; font-weight: 900; color: #f1f5f9; margin-bottom: 12px; line-height: 1.2; }}
    .hero .ref {{ font-size: 0.88rem; color: #64748b; margin-bottom: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }}
    .hero blockquote {{ font-style: italic; color: #cbd5e1; font-size: 1rem; border-left: 3px solid {color}; padding-left: 20px; max-width: 600px; margin: 0 auto; text-align: left; }}
    .wrap {{ max-width: 900px; margin: 0 auto; padding: 40px 24px 80px; }}
    .section-block {{ margin-bottom: 40px; }}
    .section-block h2 {{ font-size: 1.3rem; font-weight: 800; color: #f1f5f9; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.07); }}
    .section-block p {{ color: #94a3b8; font-size: 0.95rem; line-height: 1.85; margin-bottom: 16px; }}
    .versiculo-bloco {{ background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-left: 3px solid {color}; border-radius: 0 12px 12px 0; padding: 18px 20px; margin-bottom: 16px; }}
    .ref-v {{ font-size: 0.8rem; font-weight: 800; color: {color}; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }}
    .texto-v {{ font-style: italic; color: #cbd5e1; font-size: 0.95rem; margin-bottom: 10px; line-height: 1.7; }}
    .analise-v {{ color: #94a3b8; font-size: 0.9rem; line-height: 1.8; }}
    .vocab-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 14px; margin-top: 16px; }}
    .vocab-card {{ background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-radius: 10px; padding: 14px 16px; }}
    .termo {{ font-size: 1.1rem; font-weight: 800; color: {color}; font-family: 'Georgia', serif; }}
    .transl {{ font-size: 0.78rem; color: #64748b; font-style: italic; margin: 2px 0 6px; }}
    .def {{ font-size: 0.85rem; color: #94a3b8; line-height: 1.65; }}
    .nav-cap {{ display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.07); }}
    .nav-cap a {{ background: {tag_bg}; border: 1px solid {tag_border}; color: {color}; text-decoration: none; padding: 10px 20px; border-radius: 8px; font-size: 0.88rem; font-weight: 700; transition: all 0.2s; }}
    .nav-cap a:hover {{ background: {tag_hover}; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 0.87rem; margin: 20px 0 32px; }}
    th {{ background: {tag_bg}; color: {color}; padding: 10px 14px; text-align: left; font-weight: 700; border-bottom: 1px solid {tag_border}; }}
    td {{ padding: 10px 14px; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; }}
    tr:hover td {{ background: rgba(255,255,255,0.02); }}
"""

def gerar_pagina(livro_key, livro_nome, cap_num, total_caps, titulo, ref, chave, tag_label, css, contexto, versiculos, vocab, teologia, aplicacao):
    prev = f"/07-novo-testamento/{livro_key}/capitulos/capitulo-{cap_num-1:02d}.html" if cap_num > 1 else f"/07-novo-testamento/{livro_key}/index.html"
    prev_label = f"← {livro_nome} {cap_num-1}" if cap_num > 1 else f"← Índice de {livro_nome}"
    nxt = f"/07-novo-testamento/{livro_key}/capitulos/capitulo-{cap_num+1:02d}.html" if cap_num < total_caps else f"/07-novo-testamento/{livro_key}/index.html"
    nxt_label = f"{livro_nome} {cap_num+1} →" if cap_num < total_caps else f"Índice de {livro_nome} →"

    versiculos_html = ""
    for v in versiculos:
        versiculos_html += f"""
      <div class="versiculo-bloco">
        <div class="ref-v">{v['ref']}</div>
        <div class="texto-v">{v['texto']}</div>
        <div class="analise-v">{v['analise']}</div>
      </div>"""

    vocab_html = ""
    for v in vocab:
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
  <title>{titulo} | 365 de Graça & Adoração</title>
  <link rel="icon" href="/favicon.ico">
  <style>{css}</style>
</head>
<body>
  <div class="topbar"><div class="inner">
    <a href="/07-novo-testamento/{livro_key}/index.html">← {livro_nome}</a>
    <a href="/07-novo-testamento/index.html">Novo Testamento</a>
  </div></div>
  <div class="hero">
    <span class="tag">{tag_label}</span>
    <h1>{titulo}</h1>
    <div class="ref">{ref}</div>
    <blockquote>{chave}</blockquote>
  </div>
  <div class="wrap">
    <div class="section-block">
      <h2>📜 Contexto Histórico e Literário</h2>
      {contexto}
    </div>
    <div class="section-block">
      <h2>🔍 Análise Versículo por Versículo</h2>
      {versiculos_html}
    </div>
    <div class="section-block">
      <h2>📚 Vocabulário Essencial</h2>
      <div class="vocab-grid">{vocab_html}</div>
    </div>
    <div class="section-block">
      <h2>🏛️ Teologia Sistemática</h2>
      {teologia}
    </div>
    <div class="section-block">
      <h2>✨ Aplicação Contemporânea</h2>
      {aplicacao}
    </div>
    <div class="nav-cap">
      <a href="{prev}">{prev_label}</a>
      <a href="/07-novo-testamento/{livro_key}/index.html">📋 Índice</a>
      <a href="{nxt}">{nxt_label}</a>
    </div>
  </div>
</body>
</html>"""


def main():
    base = "/home/ubuntu/365-de-graca-e-adoracao/07-novo-testamento"

    # =========================================================
    # HEBREUS 11 — A Galeria da Fé
    # =========================================================
    css_heb = make_css("#f59e0b", "#1a1200", "rgba(245,158,11,0.1)", "rgba(245,158,11,0.25)", "rgba(245,158,11,0.2)")
    heb11 = gerar_pagina(
        "hebreus", "Hebreus", 11, 13,
        "Hebreus 11 — A Galeria da Fé",
        "Hebreus 11:1-40 · Autor desconhecido · c. 60-70 d.C.",
        "Ora, a fé é o firme fundamento das coisas que se esperam, e a prova das coisas que se não veem. — Hebreus 11:1",
        "📜 Hebreus 11 · Epístolas Gerais",
        css_heb,
        """<p>Hebreus é a mais teologicamente sofisticada das epístolas do NT — uma obra de arte literária e teológica que apresenta Jesus como o sumo sacerdote definitivo que cumpre e transcende todo o sistema sacrificial do AT. O autor (desconhecido — as propostas incluem Paulo, Apolo, Barnabé, Priscila e outros) escreve para uma comunidade de cristãos judeus que estão considerando retornar ao judaísmo sob a pressão da perseguição. Seu argumento central é a superioridade de Cristo: superior aos anjos (caps. 1-2), a Moisés (cap. 3), a Josué (cap. 4), ao sacerdócio aaroníco (caps. 5-7), à aliança mosaica (caps. 8-10). O capítulo 11 é o clímax desta argumentação: a fé que sustentou os heróis do AT é a mesma fé que deve sustentar os leitores na perseguição presente.</p>
<p>O capítulo 11 é conhecido como a "Galeria da Fé" ou o "Salão da Fama da Fé" — uma lista de heróis do AT que viveram pela fé antes de receber o cumprimento das promessas. A estrutura é anafórica: "pela fé" (<em>pistei</em>) introduz cada exemplo, criando um ritmo poético e uma acumulação de evidências. A lista inclui Abel, Enoque, Noé, Abraão, Sara, Isaque, Jacó, José, Moisés, Raabe e outros — todos exemplos de fé que age sem ver o cumprimento completo das promessas.</p>
<p>O capítulo 11 não pode ser lido isoladamente do capítulo 12 — a "nuvem de testemunhas" do v. 1 de Hebreus 12 é a galeria do capítulo 11. Os heróis da fé não são apenas exemplos históricos — são "testemunhas" (<em>martyres</em>) que observam a corrida dos leitores. Esta imagem do anfiteatro celestial é um dos mais poderosos motivadores da perseverança cristã.</p>""",
        [
            {
                "ref": "11:1-3 — A Definição da Fé",
                "texto": "\"Ora, a fé é o firme fundamento das coisas que se esperam, e a prova das coisas que se não veem. Porque por ela os anciãos alcançaram bom testemunho. Pela fé entendemos que os mundos foram criados pela palavra de Deus, de modo que o visível não foi feito do que se vê.\"",
                "analise": "A definição de fé em Hb 11:1 é a mais famosa do NT. \"Firme fundamento\" (<em>hypostasis</em>) — a palavra grega tem dois campos semânticos: (1) substância, realidade objetiva — a fé dá realidade presente às coisas futuras; (2) fundamento, base — a fé é o alicerce sobre o qual as esperanças repousam. \"Prova das coisas que se não veem\" (<em>elegchos pragmatōn ou blepomenōn</em>) — <em>elegchos</em> é um termo jurídico: prova, evidência, convicção. A fé não é crença sem evidência — é convicção baseada na revelação de Deus, que é mais confiável do que a percepção sensorial. O versículo 3 aplica esta definição à criação: entendemos pela fé que o universo foi criado pela Palavra de Deus. Esta é a única forma de conhecer a criação — não pela observação científica do processo (que não pode alcançar o ato criador original), mas pela revelação divina recebida pela fé."
            },
            {
                "ref": "11:4-7 — Abel, Enoque e Noé",
                "texto": "\"Pela fé Abel ofereceu a Deus mais excelente sacrifício do que Caim... Pela fé Enoque foi transladado para não ver a morte... Pela fé Noé, divinamente avisado das coisas que ainda não se viam, temendo a Deus, preparou a arca para salvação de sua família.\"",
                "analise": "Os três primeiros exemplos estabelecem o padrão da fé: (1) Abel — fé que adora com o melhor que tem, mesmo que isso provoque hostilidade (ele foi morto por Caim). \"Ainda fala\" (<em>eti lalei</em>) — o sangue de Abel ainda clama (Gn 4:10; Hb 12:24). A fé de Abel sobrevive à morte. (2) Enoque — fé que agrada a Deus sem ver a morte. \"Sem fé é impossível agradar a Deus\" (v. 6) — este versículo é a tese de todo o capítulo. A fé não é uma das condições para agradar a Deus — é a condição necessária e suficiente. (3) Noé — fé que age com base em avisos divinos sobre coisas \"ainda não vistas\" (<em>mēpō blepomenōn</em>). Noé construiu a arca sem ver a chuva — o paradigma da fé que age antes de ver a evidência."
            },
            {
                "ref": "11:8-19 — Abraão e Sara",
                "texto": "\"Pela fé Abraão, sendo chamado, obedeceu, indo para um lugar que havia de receber por herança; e saiu sem saber para onde ia... Pela fé também a própria Sara recebeu força para conceber semente, e isso fora do tempo da idade, porquanto teve por fiel aquele que havia prometido.\"",
                "analise": "Abraão é o exemplo central — ele recebe mais espaço do que qualquer outro personagem (vv. 8-19). Sua fé é descrita em quatro atos: (1) sair sem saber para onde ia (v. 8) — obediência sem mapa; (2) habitar em tendas como estrangeiro (vv. 9-10) — fé que não se apega ao presente porque espera o futuro; (3) oferecer Isaque (vv. 17-19) — o teste supremo da fé. O versículo 19 é extraordinário: Abraão \"considerou que Deus era poderoso para ressuscitar até os mortos\" (<em>logizomenos hoti kai ek nekrōn egeirein dynatos ho Theos</em>). Abraão não sabia da ressurreição de Cristo — mas sua fé na fidelidade de Deus levou-o a uma conclusão que antecipava a ressurreição. Sara é incluída como exemplo de fé — ela \"teve por fiel aquele que havia prometido\" (<em>pistis ton epangeilamenon</em>). A fé de Sara é fé na fidelidade de Deus, não na possibilidade natural."
            },
            {
                "ref": "11:32-40 — A Nuvem de Testemunhas",
                "texto": "\"E que mais direi? Porque o tempo me faltaria para falar de Gideão, de Baraque, de Sansão, de Jefté, de Davi, de Samuel e dos profetas... E todos estes, tendo alcançado bom testemunho pela fé, não receberam o cumprimento da promessa, provendo Deus alguma coisa melhor para nós.\"",
                "analise": "O autor acelera o ritmo no final do capítulo — o tempo não é suficiente para descrever todos os exemplos. A lista inclui heróis que triunfaram pela fé (vv. 33-35a) e mártires que sofreram pela fé (vv. 35b-38). A fé não garante libertação do sofrimento — garante que o sofrimento tem sentido e que Deus é fiel. O versículo 40 é o clímax teológico: os heróis do AT \"não receberam o cumprimento da promessa\" porque Deus havia \"provido alguma coisa melhor para nós\" — o cumprimento em Cristo. A fé dos patriarcas e profetas estava orientada para Cristo, mesmo que eles não o vissem claramente. Nós, que vivemos após a encarnação, morte e ressurreição de Cristo, temos uma vantagem sobre eles — e portanto uma responsabilidade maior de perseverar na fé."
            }
        ],
        [
            {"termo": "πίστις", "transl": "pistis", "def": "Fé. Em Hb 11:1, definida como 'firme fundamento das coisas que se esperam e prova das coisas que se não veem'. Não crença sem evidência, mas convicção baseada na revelação de Deus."},
            {"termo": "ὑπόστασις", "transl": "hypostasis", "def": "Substância, fundamento, realidade. A fé é a hypostasis das esperanças — ela dá realidade presente às coisas futuras. O mesmo termo é usado em Hb 1:3 para descrever Cristo como 'imagem da sua substância'."},
            {"termo": "ἔλεγχος", "transl": "elegchos", "def": "Prova, evidência, convicção. Termo jurídico: a prova que convence o tribunal. A fé é a prova das coisas invisíveis — não prova empírica, mas convicção baseada na revelação divina."},
            {"termo": "μάρτυς", "transl": "martys", "def": "Testemunha. Os heróis do capítulo 11 são 'testemunhas' que observam a corrida dos crentes. A nuvem de testemunhas de Hb 12:1 é a galeria do capítulo 11."}
        ],
        """<p>Hebreus 11 apresenta a fé como a resposta humana à revelação divina — não crença cega, mas confiança fundamentada no caráter e nas promessas de Deus. A definição de fé em Hb 11:1 é epistemológica: a fé é uma forma de conhecimento que alcança realidades que a percepção sensorial não pode atingir. Esta não é irracionalidade — é racionalidade que reconhece os limites da razão e da experiência sensorial e se apoia na revelação de Deus.</p>
<p>A galeria da fé revela que a fé bíblica é sempre orientada para o futuro — ela age no presente com base em promessas que ainda não se cumpriram completamente. Abraão saiu sem saber para onde ia; Noé construiu a arca sem ver a chuva; os mártires sofreram sem ver a ressurreição. Esta orientação escatológica da fé é o que a distingue da confiança comum: a fé cristã não é confiança em circunstâncias favoráveis, mas confiança em Deus que é fiel às suas promessas.</p>""",
        """<p>A definição de fé em Hb 11:1 é o antídoto para dois extremos: o fideísmo que crê sem razão, e o racionalismo que exige evidência empírica para tudo. A fé bíblica não é irracional — ela é baseada na revelação de Deus, que é a fonte de conhecimento mais confiável disponível. Mas ela transcende a razão ao confiar em realidades que ainda não são visíveis.</p>
<p>A galeria da fé é um convite à perseverança. Quando a fé parece difícil, quando as promessas parecem distantes, quando o sofrimento parece sem sentido — a nuvem de testemunhas nos lembra que outros correram antes de nós e chegaram à meta. A fé de Abel, Enoque, Noé, Abraão e Sara não foi em vão — e a nossa também não será.</p>"""
    )

    # =========================================================
    # TIAGO 2 — Fé e Obras
    # =========================================================
    css_tg = make_css("#10b981", "#001a0f", "rgba(16,185,129,0.1)", "rgba(16,185,129,0.25)", "rgba(16,185,129,0.2)")
    tg2 = gerar_pagina(
        "tiago", "Tiago", 2, 5,
        "Tiago 2 — Fé e Obras: O Debate Mais Famoso do NT",
        "Tiago 2:1-26 · Tiago, irmão do Senhor · c. 45-62 d.C.",
        "Assim como o corpo sem o espírito está morto, assim também a fé sem obras é morta. — Tiago 2:26",
        "📜 Tiago 2 · Epístolas Gerais",
        css_tg,
        """<p>Tiago é a epístola mais prática do NT — e a mais controversa. Lutero a chamou de "epístola de palha" porque parecia contradizer a doutrina paulina da justificação pela fé. Mas a aparente contradição entre Paulo ("justificado pela fé, não pelas obras" — Rm 3:28) e Tiago ("o homem é justificado pelas obras, e não somente pela fé" — Tg 2:24) é resultado de uma leitura superficial. Paulo e Tiago usam as palavras "fé", "obras" e "justificação" em sentidos diferentes e estão respondendo a problemas diferentes.</p>
<p>Paulo combate o legalismo — a ideia de que as obras da Lei são o meio de justificação diante de Deus. Tiago combate o antinomismo — a ideia de que a fé pode existir sem produzir obras. Paulo fala de justificação diante de Deus (a declaração forense de Deus que declara o pecador justo). Tiago fala de justificação diante dos homens (a demonstração visível de que a fé é genuína). Paulo e Tiago são complementares, não contraditórios: a fé que salva é a fé que produz obras; as obras não salvam, mas demonstram que a fé é real.</p>
<p>O capítulo 2 tem duas seções: (1) a proibição do favoritismo (vv. 1-13) — a fé em Cristo é incompatível com a discriminação baseada em riqueza; e (2) a relação entre fé e obras (vv. 14-26) — a fé sem obras é morta.</p>""",
        [
            {
                "ref": "2:1-9 — Sem Favoritismo",
                "texto": "\"Meus irmãos, não tenhais a fé de nosso Senhor Jesus Cristo, Senhor da glória, com acepção de pessoas. Porque, se no vosso ajuntamento entrar algum homem com anel de ouro e com roupa preciosa, e entrar também algum pobre com roupa suja, e vós atenderdes ao que traz a roupa preciosa...\"",
                "analise": "A proibição do favoritismo (<em>prosōpolēmpsia</em> — literalmente, \"receber a face\", tratar pessoas diferentemente com base na aparência) é uma aplicação direta da fé em Cristo. \"A fé de nosso Senhor Jesus Cristo, Senhor da glória\" (<em>tēn pistin tou Kyriou hēmōn Iēsou Christou tēs doxēs</em>) — a fé em Cristo, que é a glória de Deus encarnada, é incompatível com qualquer forma de discriminação. O exemplo é concreto e específico: um rico com anel de ouro e roupas finas recebe lugar de honra; um pobre com roupas sujas é mandado para o chão. Tiago identifica este comportamento como \"mau julgamento\" (<em>kritas dialogismōn ponērōn</em>) — julgamento baseado em critérios mundanos (riqueza, aparência) em vez de critérios divinos (imagem de Deus em cada pessoa). O versículo 5 inverte a lógica do mundo: Deus escolheu os pobres do mundo para serem ricos em fé e herdeiros do reino."
            },
            {
                "ref": "2:14-17 — Fé Sem Obras é Morta",
                "texto": "\"De que aproveita, meus irmãos, se alguém disser que tem fé, mas não tiver obras? Pode essa fé salvá-lo? Se um irmão ou uma irmã estiverem nus e com falta do mantimento de cada dia, e algum de vós lhes disser: Ide em paz, aquecei-vos e fartai-vos; e não lhes derdes as coisas necessárias para o corpo, de que aproveita?\"",
                "analise": "O argumento de Tiago começa com uma pergunta retórica: \"De que aproveita?\" (<em>ti to ophelos</em>) — qual é a utilidade prática de uma fé que não produz ação? O exemplo é devastadoramente simples: dizer \"ide em paz, aquecei-vos e fartai-vos\" a um irmão nu e faminto sem dar-lhe o que precisa é inútil. A fé que não se traduz em ação é igualmente inútil. \"A fé sem obras é morta\" (<em>hē pistis chōris tōn ergōn nekra estin</em>) — não apenas fraca ou incompleta, mas morta. A morte é a ausência de vida; uma fé morta não é uma fé fraca — é uma fé inexistente que usa o nome de fé."
            },
            {
                "ref": "2:18-20 — O Debate com o Objetor",
                "texto": "\"Mas alguém dirá: Tu tens fé, e eu tenho obras; mostra-me a tua fé sem as tuas obras, e eu te mostrarei a minha fé pelas minhas obras. Tu crês que há um só Deus; fazes bem; os demônios também creem, e estremecem.\"",
                "analise": "Tiago introduz um objetor imaginário — um recurso retórico chamado <em>diatribē</em> (diálogo com um interlocutor fictício). A resposta de Tiago ao objetor é precisa: a fé não pode ser mostrada sem obras — ela só se torna visível através das obras. \"Mostra-me a tua fé sem as tuas obras\" — é impossível. A fé é invisível; as obras são a manifestação visível da fé. O argumento dos demônios é devastador: os demônios têm fé ortodoxa — eles creem que há um só Deus (monoteísmo correto) e \"estremecem\" (<em>phrissousi</em> — arrepiam-se de horror). Mas esta fé não os salva, porque não produz obediência e amor. A fé que salva não é mero assentimento intelectual — é confiança pessoal que transforma o coração e produz obras."
            },
            {
                "ref": "2:21-26 — Abraão e Raabe",
                "texto": "\"Não foi Abraão, nosso pai, justificado pelas obras, quando ofereceu seu filho Isaque sobre o altar? Vês que a fé cooperou com as suas obras, e que pelas obras a fé foi aperfeiçoada... E de igual modo também Raabe, a meretriz, não foi justificada pelas obras, quando recebeu os mensageiros e os fez sair por outro caminho?\"",
                "analise": "Tiago usa os mesmos exemplos que Paulo (Abraão) mas com propósito diferente. Paulo cita Gn 15:6 (\"Abraão creu em Deus, e isso lhe foi imputado como justiça\") para mostrar que a justificação precede as obras. Tiago cita Gn 22 (a oferta de Isaque) para mostrar que a fé de Abraão foi \"aperfeiçoada\" (<em>eteleiōthē</em>) pelas obras — a fé de Gn 15 foi demonstrada e completada pela obediência de Gn 22. \"A fé cooperou com as suas obras\" (<em>hē pistis synērgei tois ergois autou</em>) — fé e obras são parceiros, não oponentes. Raabe é o segundo exemplo — uma prostituta gentílica que demonstrou fé real ao arriscar a vida para proteger os espias israelitas. A fé de Raabe não era teologicamente sofisticada — mas era real, e se demonstrou em ação corajosa."
            }
        ],
        [
            {"termo": "προσωποληψία", "transl": "prosōpolēmpsia", "def": "Favoritismo, acepção de pessoas. Literalmente 'receber a face' — tratar pessoas diferentemente com base na aparência. Incompatível com a fé em Cristo, que vê a imagem de Deus em cada pessoa."},
            {"termo": "νεκρά", "transl": "nekra", "def": "Morta. A fé sem obras não é apenas fraca — é morta. A morte é ausência de vida; uma fé morta não é fé real, apenas o uso do nome de fé sem a realidade."},
            {"termo": "τελειόω", "transl": "teleioō", "def": "Aperfeiçoar, completar. A fé de Abraão foi 'aperfeiçoada' pelas obras — não que as obras a tornaram mais válida diante de Deus, mas que as obras completaram e demonstraram a realidade da fé."},
            {"termo": "συνεργέω", "transl": "synergeo", "def": "Cooperar, trabalhar junto. 'A fé cooperou com as suas obras' — fé e obras são parceiros, não oponentes. A fé genuína produz obras; as obras demonstram a fé."}
        ],
        """<p>Tiago 2 resolve a aparente contradição entre Paulo e Tiago ao mostrar que eles falam de coisas diferentes. Paulo fala de justificação diante de Deus — o ato forense pelo qual Deus declara o pecador justo com base na obra de Cristo, recebida pela fé. Tiago fala de justificação diante dos homens — a demonstração visível de que a fé é genuína. As obras não contribuem para a justificação diante de Deus (Paulo), mas demonstram que a justificação ocorreu (Tiago).</p>
<p>A proibição do favoritismo em Tg 2:1-9 é uma aplicação da cristologia. Cristo é "o Senhor da glória" — a glória de Deus encarnada. Quem trata os pobres com desprezo está desprezando a imagem de Deus que eles carregam. A fé em Cristo transforma a visão que temos das pessoas: não as vemos mais por sua riqueza, status ou aparência, mas como portadores da imagem de Deus.</p>""",
        """<p>O argumento dos demônios em Tg 2:19 é um dos mais perturbadores do NT para o cristão contemporâneo. Os demônios têm fé ortodoxa — creem que há um só Deus. Mas esta fé não os salva. Quantos cristãos têm fé "demoníaca" — correta em conteúdo, mas sem transformação de vida? A fé que salva não é o assentimento a proposições teológicas corretas, mas a confiança pessoal em Cristo que transforma o coração e produz obras de amor.</p>
<p>A proibição do favoritismo em Tg 2:1-9 é urgentemente relevante para a Igreja contemporânea. Quando igrejas tratam os ricos com mais atenção e respeito do que os pobres, quando o status social determina o acesso ao liderança ou ao cuidado pastoral, elas estão praticando exatamente o que Tiago condena. A Igreja que leva a sério Tiago 2 é aquela onde o mendigo e o empresário recebem o mesmo amor e a mesma atenção.</p>"""
    )

    # =========================================================
    # 1 PEDRO 1 — Esperança Viva
    # =========================================================
    css_1p = make_css("#f97316", "#1a0a00", "rgba(249,115,22,0.1)", "rgba(249,115,22,0.25)", "rgba(249,115,22,0.2)")
    pedro1 = gerar_pagina(
        "1pedro", "1 Pedro", 1, 5,
        "1 Pedro 1 — Esperança Viva e Santidade",
        "1 Pedro 1:1-25 · Pedro · c. 62-64 d.C. · Roma",
        "Bendito seja o Deus e Pai de nosso Senhor Jesus Cristo, que segundo a sua muita misericórdia nos regenerou para uma esperança viva, pela ressurreição de Jesus Cristo dentre os mortos. — 1 Pedro 1:3",
        "📜 1 Pedro 1 · Epístolas Gerais",
        css_1p,
        """<p>1 Pedro é uma carta de encorajamento para cristãos que sofrem. Pedro escreve "aos estrangeiros dispersos" (<em>parepidēmois diasporas</em>) pelo Ponto, Galácia, Capadócia, Ásia e Bitínia — províncias da Ásia Menor. A palavra "estrangeiros" (<em>parepidēmoi</em>) é deliberadamente ambígua: pode referir-se a judeus da diáspora, a gentios convertidos que se tornaram "estrangeiros" em sua própria cultura, ou a todos os cristãos como peregrinos neste mundo. A carta foi escrita de "Babilônia" (v. 5:13) — provavelmente Roma, usando o nome simbólico da grande cidade pagã.</p>
<p>O contexto histórico é a perseguição — não necessariamente a perseguição imperial organizada de Nero (64 d.C.), mas a hostilidade social e cultural que os cristãos enfrentavam por recusar-se a participar nos cultos pagãos, nas festas religiosas e nas práticas sociais do mundo greco-romano. Pedro escreve para dar-lhes fundamento teológico para perseverar: a esperança viva da ressurreição, a identidade como povo escolhido de Deus, e o exemplo de Cristo que sofreu e foi glorificado.</p>
<p>O capítulo 1 tem três seções: (1) a saudação e a bênção trinitária (vv. 1-12); (2) o apelo à santidade (vv. 13-21); e (3) o apelo ao amor fraternal (vv. 22-25). A bênção dos versículos 3-12 é uma das mais ricas do NT — um hino de louvor à Trindade pela salvação, com ênfase especial na esperança escatológica.</p>""",
        [
            {
                "ref": "1:3-5 — Esperança Viva",
                "texto": "\"Bendito seja o Deus e Pai de nosso Senhor Jesus Cristo, que segundo a sua muita misericórdia nos regenerou para uma esperança viva, pela ressurreição de Jesus Cristo dentre os mortos; para uma herança incorruptível, e incontaminada, e que não se pode murchar, guardada nos céus para vós.\"",
                "analise": "A abertura da bênção é trinitária: o Pai nos regenerou, pela ressurreição do Filho, para uma herança guardada pelo Espírito (v. 5). \"Esperança viva\" (<em>elpida zōsan</em>) — a esperança cristã não é um desejo vago ou uma ilusão confortante; é uma esperança \"viva\" porque fundamentada na ressurreição de Cristo. A ressurreição não é apenas um evento passado — é o fundamento de uma esperança presente e futura. A herança é descrita com três adjetivos negativos que definem o que ela não é: \"incorruptível\" (<em>aphtharton</em>) — não sujeita à deterioração; \"incontaminada\" (<em>amianton</em>) — não manchada pelo pecado; \"que não se pode murchar\" (<em>amaranton</em>) — não sujeita ao envelhecimento. Estas três qualidades contrastam com toda herança terrena, que é corruptível, contaminável e perecível."
            },
            {
                "ref": "1:6-9 — Alegria no Sofrimento",
                "texto": "\"Em que exultais, ainda que agora, se necessário for, sejais por um pouco contristados em várias tentações; para que a prova da vossa fé, muito mais preciosa do que o ouro que perece, ainda que provado pelo fogo, seja achada em louvor, e glória, e honra na revelação de Jesus Cristo.\"",
                "analise": "A alegria no sofrimento é um dos temas mais paradoxais do NT. Pedro não nega o sofrimento — \"se necessário for\" (<em>ei deon estin</em>) reconhece que o sofrimento é real e pode ser necessário. Mas afirma que a alegria pode coexistir com o sofrimento porque a alegria cristã não é baseada nas circunstâncias, mas na esperança viva da ressurreição. A metáfora do ouro refinado pelo fogo é poderosa: o sofrimento não destrói a fé genuína — ele a purifica, removendo as impurezas e revelando o ouro puro. \"A prova da vossa fé\" (<em>to dokimion hymōn tēs pisteōs</em>) — o sofrimento é o teste que demonstra e purifica a fé. O objetivo final é \"louvor, glória e honra na revelação de Jesus Cristo\" — o sofrimento presente é temporário; a glória futura é eterna."
            },
            {
                "ref": "1:13-16 — O Apelo à Santidade",
                "texto": "\"Por isso, cingindo os lombos do vosso entendimento, sóbrios e esperando completamente na graça que vos é trazida na revelação de Jesus Cristo, como filhos obedientes, não vos conformeis com as concupiscências que antes tínheis na vossa ignorância; mas, como é santo aquele que vos chamou, sede vós também santos em toda a vossa maneira de viver.\"",
                "analise": "\"Cingindo os lombos do vosso entendimento\" (<em>anazōsamenoi tas osphyas tēs dianoias hymōn</em>) — a metáfora é de preparação para ação: no mundo antigo, cingir os lombos (prender as roupas longas com um cinto) era o gesto de quem se preparava para trabalhar ou correr. Pedro aplica esta metáfora à mente: a mente cristã deve estar preparada, alerta, pronta para pensar com clareza. \"Não vos conformeis\" (<em>mē syschēmatizomenoi</em>) — o mesmo verbo que Paulo usa em Rm 12:2. O cristão não deve ser moldado pelo padrão do mundo. A motivação para a santidade é teológica: \"como é santo aquele que vos chamou\" — a santidade de Deus é o modelo e o fundamento da santidade humana. A citação de Lv 11:44 — \"sede santos, porque eu sou santo\" — mostra que a santidade não é uma novidade cristã, mas o chamado eterno de Deus ao seu povo."
            },
            {
                "ref": "1:18-21 — Redenção pelo Sangue Precioso",
                "texto": "\"Sabendo que não fostes remidos de vossa vã conversação, recebida por tradição de vossos pais, com coisas corruptíveis, como prata ou ouro; mas com o precioso sangue de Cristo, como de um cordeiro sem defeito e sem mácula.\"",
                "analise": "A teologia da redenção de Pedro é rica em imagens do AT. \"Remidos\" (<em>elytrōthēte</em>) — o verbo é o mesmo da redenção de escravos: o pagamento do resgate para libertar alguém. O preço da redenção não foi prata ou ouro — foi \"o precioso sangue de Cristo\" (<em>timiō haimati Christou</em>). A imagem do \"cordeiro sem defeito e sem mácula\" (<em>amnos amōmos kai aspilos</em>) ecoa o cordeiro pascal (Êx 12:5) e o Servo do Senhor (Is 53:7). Cristo é o cumprimento de todos os sacrifícios do AT. O versículo 20 é extraordinário: Cristo foi \"predestinado antes da fundação do mundo\" (<em>proegnōsmenou men pro katabolēs kosmou</em>) — a redenção não foi uma improvisação divina após a queda, mas o plano eterno de Deus antes da criação."
            }
        ],
        [
            {"termo": "ἐλπίς", "transl": "elpis", "def": "Esperança. A esperança cristã não é um desejo vago, mas uma expectativa fundamentada na ressurreição de Cristo. É 'viva' porque o Cristo ressuscitado é o seu fundamento."},
            {"termo": "παρεπίδημος", "transl": "parepidēmos", "def": "Estrangeiro, peregrino. Os cristãos são 'estrangeiros' neste mundo — sua verdadeira pátria é o reino de Deus. Esta identidade de peregrinos fundamenta tanto a esperança quanto a ética cristã."},
            {"termo": "ἅγιος", "transl": "hagios", "def": "Santo, separado. A santidade bíblica não é primariamente moralidade, mas separação para Deus. 'Sede santos porque eu sou santo' — a santidade humana é participação na santidade divina."},
            {"termo": "λύτρον", "transl": "lytron", "def": "Resgate, preço de redenção. O preço pago para libertar um escravo. Cristo pagou o preço de nossa redenção — não com prata ou ouro, mas com seu precioso sangue."}
        ],
        """<p>1 Pedro 1 apresenta a esperança cristã em sua forma mais concreta e fundamentada. A esperança não é um sentimento otimista ou uma ilusão confortante — é uma realidade objetiva fundamentada na ressurreição histórica de Cristo. Porque Cristo ressuscitou, a herança prometida é real, a fé dos crentes não é em vão, e o sofrimento presente tem sentido e limite.</p>
<p>A relação entre esperança e santidade em 1 Pedro 1 é fundamental. A santidade não é motivada pelo medo do julgamento (embora o julgamento seja mencionado em v. 17), mas pela esperança da revelação de Cristo (v. 13) e pelo amor de Deus que nos redimiu pelo sangue precioso de Cristo (vv. 18-21). A santidade que brota da esperança e do amor é qualitativamente diferente da moralidade que brota do medo.</p>""",
        """<p>A "esperança viva" de 1 Pedro 1:3 é o antídoto para o desespero e o niilismo contemporâneos. Em uma cultura que perdeu a esperança de um futuro melhor, que vive no presente imediato sem horizonte transcendente, a esperança cristã é radicalmente contracultural. A ressurreição de Cristo não é apenas um evento passado — é a garantia de que a história tem um destino, que o sofrimento não tem a última palavra, que a morte não é o fim.</p>
<p>O apelo à santidade em 1 Pedro 1:13-16 é urgente para a Igreja contemporânea. "Não vos conformeis" — a pressão para se conformar com os valores e práticas da cultura dominante é intensa. Pedro não pede isolamento do mundo, mas não-conformidade com os valores do mundo. A santidade não é separação geográfica, mas separação de valores: os cristãos vivem no mundo, mas não são moldados pelo mundo.</p>"""
    )

    # Salvar arquivos
    arquivos = [
        ("hebreus", 11, heb11),
        ("tiago", 2, tg2),
        ("1pedro", 1, pedro1),
    ]

    for livro_key, cap_num, html in arquivos:
        path = os.path.join(base, livro_key, "capitulos", f"capitulo-{cap_num:02d}.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {livro_key}/capitulo-{cap_num:02d}.html")

    print("\n🎉 Epístolas Gerais geradas!")


if __name__ == "__main__":
    main()
