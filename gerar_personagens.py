#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera as 15 páginas individuais de personagens bíblicos com aprofundamento teológico.
Abraão, Moisés, Davi e Paulo recebem análise extra-aprofundada.
"""

import os

BASE = "/home/ubuntu/365-de-graca-e-adoracao/personagens"
os.makedirs(BASE, exist_ok=True)

TEMPLATE = """<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} · Personagens Bíblicos · 365 de Graça & Adoração</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="Wagner Alexandre Martins">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://365gracaeadoracao.com/personagens/{slug}.html">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://365gracaeadoracao.com/personagens/{slug}.html">
  <meta property="og:title" content="{title} · 365 de Graça & Adoração">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:image" content="https://365gracaeadoracao.com/assets/img/og-image.png">
  <meta property="og:site_name" content="365 de Graça & Adoração">
  <link rel="stylesheet" href="/assets/css/style.css">
  <link rel="stylesheet" href="/assets/css/bloco.css">
  <link rel="stylesheet" href="/assets/css/nav.css">
  <style>
    .person-hero {{ background: var(--panel); border: 1px solid var(--line); border-radius: 20px; padding: 2.5rem 2rem; margin-bottom: 2rem; display: flex; gap: 2rem; align-items: flex-start; flex-wrap: wrap; }}
    .person-icon-lg {{ width: 90px; height: 90px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2.8rem; flex-shrink: 0; border: 2px solid var(--line); }}
    .person-meta {{ flex: 1; min-width: 200px; }}
    .person-meta h1 {{ color: #fff; margin: 0 0 0.3rem; font-size: clamp(1.6rem, 3vw, 2.2rem); }}
    .person-meta .subtitle {{ color: var(--accent2); font-size: 1rem; margin: 0 0 0.75rem; }}
    .meta-grid {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.75rem; }}
    .meta-item {{ background: rgba(255,255,255,.06); border: 1px solid var(--line); border-radius: 8px; padding: 4px 10px; font-size: 0.78rem; color: var(--muted); }}
    .meta-item strong {{ color: var(--accent2); }}
    .section-card {{ background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 1.8rem; margin-bottom: 1.5rem; }}
    .section-card h2 {{ color: var(--accent2); margin: 0 0 1rem; font-size: 1.2rem; border-bottom: 1px solid var(--line); padding-bottom: 0.5rem; }}
    .section-card h3 {{ color: #fff; margin: 1.2rem 0 0.5rem; font-size: 1.05rem; }}
    .section-card p {{ color: var(--muted); line-height: 1.85; margin: 0 0 0.9rem; font-size: 1rem; }}
    .verse-highlight {{ background: rgba(0,168,225,.06); border-left: 4px solid var(--accent); border-radius: 0 12px 12px 0; padding: 1rem 1.5rem; margin: 1.2rem 0; }}
    .verse-highlight p {{ margin: 0; font-style: italic; color: var(--accent2); font-size: 1.05rem; }}
    .verse-highlight cite {{ display: block; margin-top: 0.4rem; font-size: 0.82rem; color: var(--muted); font-style: normal; }}
    .timeline-item {{ display: flex; gap: 1rem; padding: 0.9rem 0; border-bottom: 1px solid var(--line); }}
    .timeline-year {{ min-width: 80px; color: var(--accent); font-weight: 700; font-size: 0.9rem; }}
    .timeline-text {{ color: var(--muted); font-size: 0.95rem; line-height: 1.5; }}
    .theology-box {{ background: rgba(139,92,246,.06); border: 1px solid rgba(139,92,246,.2); border-radius: 12px; padding: 1.2rem 1.5rem; margin: 1.2rem 0; }}
    .theology-box h4 {{ color: #c4b5fd; margin: 0 0 0.5rem; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.5px; }}
    .theology-box p {{ margin: 0; color: var(--muted); font-size: 0.95rem; }}
    .nav-personagens {{ display: flex; gap: 1rem; justify-content: space-between; flex-wrap: wrap; margin-top: 2rem; }}
    .nav-personagens a {{ flex: 1; min-width: 140px; padding: 0.75rem 1rem; background: var(--panel); border: 1px solid var(--line); border-radius: 10px; text-decoration: none; color: var(--muted); font-size: 0.85rem; text-align: center; transition: all .15s; }}
    .nav-personagens a:hover {{ border-color: rgba(0,168,225,.35); color: #fff; }}
  </style>
</head>
<body>
  <div class="topbar">
    <div class="inner">
      <div class="brand">
        <a href="/" style="display:flex;align-items:center;gap:10px;text-decoration:none;color:inherit;">
          <span>365 de Graça &amp; Adoração</span>
        </a>
      </div>
      <button class="nav-toggle" id="nav-toggle" aria-label="Menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav" id="main-nav">
        <a href="/">Início</a>
        <a href="/personagens/index.html" class="active">Personagens</a>
        <a href="/como-estudar/index.html">Como Estudar</a>
        <a href="/busca/index.html" class="nav-busca">🔍 Buscar</a>
      </nav>
    </div>
  </div>

  <main class="wrap reading">
    <nav aria-label="Breadcrumb" style="margin-bottom:1.5rem;font-size:0.85rem;color:var(--muted);">
      <a href="/" style="color:var(--accent);text-decoration:none;">Início</a>
      <span style="margin:0 0.5rem;">›</span>
      <a href="/personagens/index.html" style="color:var(--accent);text-decoration:none;">Personagens</a>
      <span style="margin:0 0.5rem;">›</span>
      <span>{name}</span>
    </nav>

    <div class="panel">
      <!-- Hero do Personagem -->
      <div class="person-hero">
        <div class="person-icon-lg" style="background:{icon_bg};border-color:{icon_border};">{icon}</div>
        <div class="person-meta">
          <h1>{name}</h1>
          <p class="subtitle">{subtitle}</p>
          <p style="color:var(--muted);font-size:0.95rem;line-height:1.6;margin:0 0 0.75rem;">{intro}</p>
          <div class="meta-grid">
            {meta_items}
          </div>
        </div>
      </div>

{content}

      <!-- Navegação entre personagens -->
      <div class="nav-personagens">
        <a href="/personagens/index.html">← Todos os Personagens</a>
        {prev_link}
        {next_link}
      </div>
    </div>
  </main>

  <footer class="footer" style="padding:2rem;border-top:1px solid var(--line);margin-top:3rem;">
    <p>365 de Graça &amp; Adoração — Da Criação ao Apocalipse</p>
    <p><a href="/personagens/index.html" style="color:var(--accent);">← Voltar para Personagens</a></p>
  </footer>
  <script src="/assets/js/nav.js"></script>
</body>
</html>"""

def meta_item(label, value):
    return f'<span class="meta-item"><strong>{label}:</strong> {value}</span>'

def verse(text, ref):
    return f'''      <div class="verse-highlight"><p>"{text}"</p><cite>— {ref}</cite></div>'''

def theology(title, text):
    return f'''      <div class="theology-box"><h4>{title}</h4><p>{text}</p></div>'''

def section(title, body):
    return f'''      <div class="section-card"><h2>{title}</h2>\n{body}\n      </div>'''

def timeline_item(year, text):
    return f'        <div class="timeline-item"><span class="timeline-year">{year}</span><span class="timeline-text">{text}</span></div>'

# ============================================================
# PERSONAGENS
# ============================================================

personagens = {}

# ============================================================
# ABRAÃO — APROFUNDAMENTO MÁXIMO
# ============================================================
abraao_content = section("📖 Quem foi Abraão?", """
        <p>Abraão — originalmente chamado <strong>Abrão</strong> (pai exaltado) e depois renomeado por Deus para <strong>Abraão</strong> (pai de uma multidão) — é a figura mais fundamental de toda a história da salvação. Nascido em <strong>Ur dos Caldeus</strong>, uma das cidades mais sofisticadas do mundo antigo (atual sul do Iraque), por volta de 2000 a.C., ele vivia em uma sociedade politeísta e próspera quando recebeu o chamado que mudaria o curso da história humana.</p>
        <p>Sua família já havia iniciado uma migração em direção a Canaã, parando em Harã (Gênesis 11:31), quando Deus se revelou a ele com uma promessa sem precedentes: deixe tudo, vá para uma terra que eu te mostrarei, e eu farei de você uma grande nação. Não havia mapa, não havia contrato escrito, não havia garantias humanas. Apenas uma palavra divina — e Abraão foi.</p>
        <p>O apóstolo Paulo, em Romanos 4, usa Abraão como o argumento central para demonstrar que a justificação sempre foi pela fé, nunca pelas obras da lei. Abraão foi justificado antes da circuncisão (Gênesis 15:6) e séculos antes da lei mosaica — o que o torna o pai espiritual de todos os que creem, judeus e gentios. Esta é a razão pela qual Abraão é venerado pelas três maiores religiões monoteístas do mundo: judaísmo, cristianismo e islamismo.</p>
""") + "\n" + section("⏱️ Linha do Tempo de Abraão", """
        <div class="timeline-item"><span class="timeline-year">~2000 a.C.</span><span class="timeline-text">Nasce em Ur dos Caldeus, filho de Terá. Vive em uma cidade politeísta avançada com escrita cuneiforme, comércio e astronomia.</span></div>
        <div class="timeline-item"><span class="timeline-year">~1975 a.C.</span><span class="timeline-text">Terá parte com a família para Canaã, mas para em Harã. Abrão tem 75 anos quando Deus o chama a partir (Gênesis 12:1-4).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1975 a.C.</span><span class="timeline-text">Abrão chega a Canaã com Sarai e Ló. Deus aparece em Siquém e confirma a promessa da terra (Gênesis 12:7).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1965 a.C.</span><span class="timeline-text">Descida ao Egito por causa da fome. Episódio de Sarai e o Faraó — primeira de três cenas de "perigo da promessa" (Gênesis 12:10-20).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1960 a.C.</span><span class="timeline-text">Separação de Ló. Abrão escolhe a terra menos boa — generosidade que é recompensada com uma nova confirmação da promessa (Gênesis 13).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1955 a.C.</span><span class="timeline-text">Batalha dos reis: Abrão resgata Ló com 318 homens. Encontro com Melquisedeque, rei de Salém — prefiguração do sacerdócio eterno de Cristo (Gênesis 14).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1950 a.C.</span><span class="timeline-text">Aliança do Corte (Berith): Deus passa entre os animais cortados enquanto Abrão dorme — Deus assume sozinho o risco da aliança (Gênesis 15). Fé contada como justiça (v.6).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1946 a.C.</span><span class="timeline-text">Nascimento de Ismael por Agar, a serva egípcia — solução humana para o problema da promessa (Gênesis 16).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1913 a.C.</span><span class="timeline-text">Aliança da Circuncisão: Abrão (99 anos) recebe o nome Abraão. A circuncisão como sinal da aliança (Gênesis 17).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1912 a.C.</span><span class="timeline-text">Visita dos três anjos em Manre. Promessa do filho para o ano seguinte. Intercessão de Abraão por Sodoma (Gênesis 18).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1911 a.C.</span><span class="timeline-text">Nascimento de Isaque — o filho da promessa. Sara tem 90 anos, Abraão tem 100 (Gênesis 21).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1898 a.C.</span><span class="timeline-text">O Sacrifício de Isaque no Monte Moriá — o maior teste de fé da Bíblia. Deus provê o carneiro. "No monte do Senhor será provido" (Gênesis 22).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1860 a.C.</span><span class="timeline-text">Morte de Sara aos 127 anos. Abraão compra a caverna de Macpela — primeira posse da terra prometida (Gênesis 23).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1825 a.C.</span><span class="timeline-text">Morte de Abraão aos 175 anos. Sepultado em Macpela ao lado de Sara por Isaque e Ismael (Gênesis 25:7-10).</span></div>
""") + "\n" + section("🔥 As Três Grandes Alianças de Abraão", """
        <h3>1. A Aliança da Promessa (Gênesis 12 e 15)</h3>
        <p>Em Gênesis 12, Deus faz três promessas a Abrão: <strong>terra</strong> (Canaã), <strong>descendência</strong> (uma grande nação) e <strong>bênção universal</strong> (em você serão benditas todas as famílias da terra). Esta última promessa é citada por Paulo em Gálatas 3:8 como o "evangelho pregado de antemão" a Abraão — a boa notícia de que os gentios seriam justificados pela fé.</p>
        <p>Em Gênesis 15, a aliança é formalizada com o rito do corte dos animais. No mundo antigo, as partes de uma aliança passavam entre os animais cortados, simbolizando: "Que me aconteça o mesmo se eu quebrar esta aliança." Mas em Gênesis 15, apenas Deus — representado pela tocha de fogo — passa entre os animais enquanto Abraão dorme. Deus assume sozinho o risco. Esta é a graça incondicional em sua forma mais pura.</p>
""") + "\n" + verse("Ele creu no Senhor, e isso lhe foi imputado como justiça.", "Gênesis 15:6") + "\n" + section("🧠 Aprofundamento Teológico", """
        <h3>Abraão e a Doutrina da Justificação</h3>
        <p>A frase de Gênesis 15:6 — "creu no Senhor, e isso lhe foi imputado como justiça" — é o versículo mais citado do Antigo Testamento no Novo Testamento. Paulo o usa em Romanos 4 e Gálatas 3; Tiago o usa em Tiago 2:23. Cada um enfatiza um aspecto diferente: Paulo enfatiza que a fé precede as obras (Abraão foi justificado antes da circuncisão); Tiago enfatiza que a fé genuína produz obras (Abraão demonstrou sua fé ao oferecer Isaque).</p>
        <p>A aparente contradição entre Paulo e Tiago é resolvida quando se percebe que eles respondem a perguntas diferentes: Paulo responde "Como alguém é justificado diante de Deus?" (pela fé); Tiago responde "Como alguém demonstra que tem fé?" (pelas obras). Abraão é o exemplo perfeito de ambas as verdades.</p>
        <h3>O Sacrifício de Isaque como Tipologia de Cristo</h3>
        <p>Gênesis 22 é um dos textos mais teologicamente ricos de toda a Bíblia. Deus pede que Abraão ofereça seu filho único, amado, no Monte Moriá — o mesmo monte onde, séculos depois, Salomão construiria o Templo e onde Jesus seria crucificado. Os paralelos com a crucificação são impressionantes: o filho carrega a madeira do sacrifício (como Jesus carregou a cruz), o pai entrega o filho (como o Pai entregou o Filho), e no último momento Deus provê um substituto — o carneiro preso pelos chifres no mato.</p>
        <p>A declaração de Abraão — "Deus proverá para si o cordeiro para o holocausto" (Gênesis 22:8) — é uma profecia que ele mesmo não compreendia plenamente. O nome que ele deu ao lugar, "Jeová-Jirê" (O Senhor proverá), tornou-se um dos nomes mais preciosos de Deus na história da fé.</p>
""") + "\n" + theology("Abraão na Teologia Reformada", "Calvino e os reformadores usaram Abraão como prova central de que a eleição e a justificação pela fé são doutrinas do Antigo Testamento, não invenções paulinas. A aliança com Abraão é a mesma aliança da graça que se cumpre em Cristo — apenas com diferentes administrações.") + "\n" + theology("Abraão no Islamismo", "No Islã, Abraão (Ibrāhīm) é o 'Khalīl Allāh' — o Amigo de Deus — e é considerado o fundador do monoteísmo. A tradição islâmica identifica Ismael, e não Isaque, como o filho que seria sacrificado. A Caaba em Meca é atribuída a Abraão e Ismael. Esta diferença teológica é uma das mais significativas entre as três religiões abraâmicas.") + "\n" + section("💡 Legado e Relevância Hoje", """
        <p>Abraão é o pai de todos os que creem (Romanos 4:11-12). Sua vida ensina que a fé genuína é obediente — ele saiu sem saber para onde ia (Hebreus 11:8). Que a fé é paciente — esperou 25 anos pelo filho prometido. Que a fé é radical — estava disposto a oferecer o que mais amava. E que a fé é relacional — Abraão era chamado de "amigo de Deus" (Isaías 41:8; Tiago 2:23).</p>
        <p>Para o cristão, Abraão é o modelo de fé que precede e produz obras, que espera o impossível e que confia na fidelidade de Deus mesmo quando as circunstâncias contradizem a promessa. "Ele não fraquejou na fé... plenamente convencido de que Deus era poderoso para cumprir o que havia prometido" (Romanos 4:20-21).</p>
""")

personagens["abraao"] = {
    "slug": "abraao",
    "name": "Abraão",
    "title": "Abraão — O Pai da Fé",
    "subtitle": "Patriarca · ~2000 a.C. · Ur dos Caldeus → Canaã",
    "meta_desc": "Conheça Abraão, o pai da fé — sua vida, chamado, alianças com Deus, o sacrifício de Isaque e seu legado teológico no judaísmo, cristianismo e islamismo.",
    "keywords": "Abraão, pai da fé, Gênesis, aliança, justificação pela fé, sacrifício de Isaque, Jeová-Jirê, patriarca",
    "icon": "🏕️",
    "icon_bg": "rgba(217,119,6,.15)",
    "icon_border": "rgba(217,119,6,.4)",
    "intro": "O pai da fé e fundador espiritual das três religiões monoteístas. Chamado por Deus para deixar tudo, sua vida é o modelo definitivo de fé obediente, paciente e radical.",
    "meta_items": meta_item("Período", "~2000–1825 a.C.") + meta_item("Origem", "Ur dos Caldeus") + meta_item("Referência", "Gênesis 12–25") + meta_item("Categoria", "Patriarca") + meta_item("Citado no NT", "Romanos 4, Gálatas 3, Hebreus 11"),
    "content": abraao_content,
    "prev": None,
    "next": ("moises", "Moisés →")
}

# ============================================================
# MOISÉS — APROFUNDAMENTO MÁXIMO
# ============================================================
moises_content = section("📖 Quem foi Moisés?", """
        <p>Moisés é, sem dúvida, a figura mais importante do Antigo Testamento — o maior profeta de Israel, o libertador do Egito, o mediador da Lei e o fundador da nação hebraica. Sua vida, dividida em três períodos de 40 anos cada, é uma das narrativas mais dramáticas e teologicamente ricas de toda a Bíblia.</p>
        <p>Nascido em um momento de genocídio — o Faraó havia ordenado a morte de todos os meninos hebreus — Moisés foi salvo pelas águas do Nilo em uma cesta de junco, adotado pela filha do próprio Faraó e criado nos palácios do Egito. Esta ironia providencial — o libertador de Israel sendo criado pelo opressor de Israel — é um dos primeiros grandes exemplos da soberania de Deus operando através das circunstâncias humanas mais improváveis.</p>
        <p>Seu nome em hebraico, <em>Mosheh</em>, é explicado em Êxodo 2:10 como derivado do verbo "tirar das águas" — mas estudiosos observam que o nome pode ter origem egípcia (como em Tutmósis, Ramsés), significando "filho de" ou "nascido de". Esta ambiguidade linguística reflete a própria identidade dupla de Moisés: egípcio por criação, hebreu por nascimento, profeta por chamado.</p>
""") + "\n" + section("⏱️ Os Três Períodos de 40 Anos", """
        <h3>Primeiro Período (0–40 anos): O Príncipe do Egito</h3>
        <p>Moisés cresceu na corte do Faraó, recebendo a melhor educação do mundo antigo — escrita hieroglífica, matemática, astronomia, retórica e estratégia militar. Atos 7:22 diz que "Moisés foi instruído em toda a sabedoria dos egípcios e era poderoso em palavras e obras." Esta formação, que parecia um acidente histórico, seria providencialmente usada por Deus para que Moisés pudesse escrever os cinco primeiros livros da Bíblia.</p>
        <p>Aos 40 anos, ao ver um feitor egípcio espancando um hebreu, Moisés matou o egípcio e escondeu o corpo na areia. Quando o ato foi descoberto, fugiu para o deserto de Midiã — de príncipe a fugitivo em um dia.</p>
        <h3>Segundo Período (40–80 anos): O Pastor no Deserto</h3>
        <p>Por 40 anos, Moisés pastoreou ovelhas no deserto de Midiã, casado com Séfora, filha do sacerdote Jetro. O homem que havia sido criado para comandar exércitos agora cuidava de animais em uma terra árida. Este período de aparente fracasso e anonimato foi, na verdade, a escola de Deus — Moisés aprendeu a conhecer o deserto que guiaria Israel por décadas, aprendeu a humildade que o tornaria "o homem mais humilde da face da terra" (Números 12:3), e aprendeu a depender de Deus em vez de suas próprias forças.</p>
        <h3>Terceiro Período (80–120 anos): O Profeta e Libertador</h3>
        <p>Aos 80 anos, Moisés encontrou a sarça ardente no Monte Horebe — Deus se revelou como "EU SOU O QUE SOU" (YHWH) e o comissionou para libertar Israel. Moisés resistiu com cinco objeções (Êxodo 3–4), mas Deus respondeu cada uma. O que se seguiu foi a confrontação com o Faraó, as 10 pragas, o Êxodo, a travessia do Mar Vermelho, a revelação no Sinai, e 40 anos de peregrinação no deserto.</p>
""") + "\n" + verse("Eu sou o que sou. Assim dirás aos filhos de Israel: EU SOU me enviou a vós.", "Êxodo 3:14") + "\n" + section("🔥 As 10 Pragas e o Êxodo", """
        <p>As 10 pragas do Egito não eram apenas demonstrações de poder — eram um julgamento sistemático sobre os deuses egípcios. Cada praga atacava uma divindade específica do panteão egípcio: o Nilo transformado em sangue atacava Hápi (deus do Nilo); as trevas atacavam Rá (deus do sol); a morte dos primogênitos atacava o próprio Faraó, considerado filho de Rá. As pragas eram, portanto, uma proclamação teológica: o Deus de Israel é maior que todos os deuses do Egito.</p>
        <p>A Páscoa — instituída na noite da décima praga — tornou-se a festa central do judaísmo e o evento fundador da identidade nacional de Israel. O sangue do cordeiro nos umbrais das portas protegia as famílias israelitas da morte. Jesus, celebrando a Páscoa na Última Ceia, identificou-se como o Cordeiro Pascal definitivo — "este é o meu sangue da nova aliança" (Mateus 26:28).</p>
""") + "\n" + section("🧠 Aprofundamento Teológico", """
        <h3>Moisés e a Revelação do Nome Divino</h3>
        <p>A revelação do nome YHWH (geralmente traduzido como "Senhor" ou "Jeová") em Êxodo 3:14 é um dos momentos mais teologicamente densos de toda a Bíblia. O nome, derivado do verbo hebraico "ser" (hayah), pode ser traduzido como "Eu Sou o que Sou", "Eu Serei o que Serei" ou "Aquele que Faz Ser". Ele expressa a existência absoluta, a autossuficiência e a fidelidade de Deus — Ele é o mesmo ontem, hoje e para sempre.</p>
        <p>Jesus usou deliberadamente a fórmula "Eu Sou" (ego eimi em grego) em sete declarações no Evangelho de João (Eu Sou o pão da vida; a luz do mundo; a porta; o bom pastor; a ressurreição e a vida; o caminho, a verdade e a vida; a videira verdadeira). Em João 8:58, Jesus disse: "Antes que Abraão existisse, Eu Sou" — uma afirmação explícita de divindade que levou os judeus a tentarem apedrejá-lo por blasfêmia.</p>
        <h3>Moisés como Mediador e Tipo de Cristo</h3>
        <p>Moisés é o maior tipo (prefiguração) de Cristo no Antigo Testamento. Deuteronômio 18:15 registra sua própria profecia: "O Senhor teu Deus te suscitará um profeta do meio de ti, dos teus irmãos, semelhante a mim; a ele ouvireis." Pedro aplica esta profecia a Jesus em Atos 3:22. Os paralelos são impressionantes: ambos foram salvos de um massacre na infância; ambos passaram por um período de 40 anos de preparação; ambos mediaram uma aliança entre Deus e o povo; ambos libertaram seu povo de uma escravidão (Moisés do Egito, Jesus do pecado).</p>
        <h3>A Lei de Moisés e o Evangelho</h3>
        <p>A relação entre a Lei mosaica e o Evangelho é um dos temas mais complexos da teologia bíblica. Paulo em Gálatas 3 afirma que a Lei foi um "aio" (pedagogo) para conduzir a Cristo — ela revelava o pecado e a necessidade de um redentor, mas não tinha poder para salvar. O autor de Hebreus (caps. 3–4) compara Moisés e Jesus: Moisés foi fiel como servo na casa de Deus; Jesus é fiel como Filho sobre a casa de Deus. Moisés trouxe Israel à beira da terra prometida; Jesus nos conduz ao descanso eterno.</p>
""") + "\n" + theology("Moisés na Teologia da Aliança", "A teologia da aliança (Covenant Theology) vê a aliança mosaica como uma administração da aliança da graça — não uma aliança de obras, mas uma revelação mais completa da santidade de Deus e da necessidade de um mediador perfeito. A Lei não contradiz a promessa a Abraão; ela a prepara.") + "\n" + section("💡 Legado", """
        <p>Moisés morreu aos 120 anos no Monte Nebo, vendo a terra prometida de longe mas sem entrar nela — consequência de um momento de desobediência em Meribá (Números 20). Esta tragédia ensina que nem mesmo os maiores servos de Deus estão acima das consequências de suas escolhas. Mas Moisés não perdeu a salvação — ele apareceu na Transfiguração ao lado de Jesus (Mateus 17), representando a Lei que encontra seu cumprimento no Filho.</p>
        <p>Seu legado é incomensurável: os cinco livros que escreveu são o fundamento de toda a revelação bíblica; a Lei que mediou moldou a ética ocidental; e sua vida é o modelo de um líder que prefere a glória de Deus à sua própria — "Risca-me do livro que escreveste" (Êxodo 32:32), pediu ele, intercedendo pelo povo que havia pecado com o bezerro de ouro.</p>
""")

personagens["moises"] = {
    "slug": "moises",
    "name": "Moisés",
    "title": "Moisés — O Libertador e Profeta da Lei",
    "subtitle": "Profeta · ~1300 a.C. · Egito → Deserto → Monte Nebo",
    "meta_desc": "Conheça Moisés — o maior profeta do Antigo Testamento, libertador do Egito, mediador da Lei no Sinai e tipo de Cristo. Análise teológica aprofundada.",
    "keywords": "Moisés, Êxodo, dez pragas, Lei de Moisés, Monte Sinai, YHWH, Páscoa, profeta, libertador",
    "icon": "⚡",
    "icon_bg": "rgba(5,150,105,.15)",
    "icon_border": "rgba(5,150,105,.4)",
    "intro": "O maior profeta do Antigo Testamento. Libertou Israel do Egito, recebeu a Lei no Sinai e guiou o povo por 40 anos no deserto. Falou com Deus face a face como nenhum outro.",
    "meta_items": meta_item("Período", "~1393–1273 a.C.") + meta_item("Origem", "Egito (nascido hebreu)") + meta_item("Referência", "Êxodo–Deuteronômio") + meta_item("Categoria", "Profeta / Legislador") + meta_item("Citado no NT", "Atos 3:22, Hebreus 3–4, João 1:17"),
    "content": moises_content,
    "prev": ("abraao", "← Abraão"),
    "next": ("jose", "José →")
}

# ============================================================
# JOSÉ
# ============================================================
jose_content = section("📖 Quem foi José?", """
        <p>José, o décimo primeiro filho de Jacó e o primogênito de Raquel, é um dos personagens mais fascinantes e teologicamente ricos do Antigo Testamento. Sua história, narrada em Gênesis 37–50, é a narrativa mais longa e literariamente elaborada do Gênesis — uma novela de traição, sofrimento, ascensão e reconciliação que prefigura de maneira impressionante a vida de Jesus Cristo.</p>
        <p>Filho favorito de Jacó, presenteado com uma túnica especial (provavelmente de mangas compridas, símbolo de autoridade), José era também um sonhador — literalmente. Seus sonhos de que os irmãos se prostrariam diante dele geraram um ódio tão profundo que os irmãos planejaram matá-lo, depois o venderam como escravo por 20 peças de prata para mercadores ismaelitas que o levaram ao Egito.</p>
        <p>No Egito, José foi vendido para Potifar, oficial do Faraó. Prosperou sob a bênção de Deus, foi injustamente acusado pela mulher de Potifar e preso. Na prisão, interpretou sonhos de dois oficiais do Faraó. Dois anos depois, quando o próprio Faraó teve sonhos perturbadores, foi chamado para interpretá-los — e em um único dia passou de prisioneiro a segundo homem mais poderoso do Egito.</p>
""") + "\n" + verse("Vós, na verdade, intentastes o mal contra mim; porém Deus o tornou em bem.", "Gênesis 50:20") + "\n" + section("🧠 José como Tipo de Cristo", """
        <p>A tipologia entre José e Jesus é uma das mais completas da Bíblia. Os paralelos são tão numerosos e precisos que teólogos como Calvino e Matthew Henry dedicaram extensas análises ao tema:</p>
        <p><strong>Amado pelo pai:</strong> José era o filho amado de Jacó; Jesus é o Filho amado do Pai (Mateus 3:17). <strong>Enviado aos irmãos:</strong> José foi enviado por Jacó para verificar seus irmãos; Jesus foi enviado pelo Pai ao seu povo (João 1:11). <strong>Rejeitado pelos irmãos:</strong> os irmãos de José o odiaram sem causa; os líderes de Israel rejeitaram Jesus. <strong>Vendido por prata:</strong> José foi vendido por 20 peças de prata; Jesus foi traído por 30. <strong>Falsamente acusado:</strong> José foi acusado injustamente por Potifar; Jesus foi condenado injustamente por Pilatos. <strong>Exaltado após o sofrimento:</strong> José foi exaltado ao trono do Egito; Jesus foi exaltado à direita do Pai. <strong>Salva aqueles que o rejeitaram:</strong> José salvou seus irmãos da fome; Jesus salva os que o rejeitaram.</p>
        <p>A declaração de José em Gênesis 50:20 — "Vós intentastes o mal contra mim; porém Deus o tornou em bem" — é uma das afirmações mais profundas sobre a providência divina em toda a Escritura. Ela antecipa Romanos 8:28 e a teologia da cruz: o maior mal da história humana (a crucificação do Filho de Deus) foi transformado por Deus no maior bem (a redenção da humanidade).</p>
""") + "\n" + theology("Providência Divina", "A história de José é o texto fundacional da doutrina da providência — a crença de que Deus governa soberanamente todos os eventos, incluindo os mais dolorosos e injustos, para cumprir seus propósitos redentores. Deus não causou a maldade dos irmãos, mas a usou.")

personagens["jose"] = {
    "slug": "jose",
    "name": "José",
    "title": "José — O Sonhador e Tipo de Cristo",
    "subtitle": "Patriarca · ~1700 a.C. · Canaã → Egito",
    "meta_desc": "Conheça José, filho de Jacó — vendido como escravo pelos irmãos, tornou-se o segundo do Egito. Análise da tipologia com Cristo e da doutrina da providência.",
    "keywords": "José, Gênesis, sonhador, Egito, Potifar, providência divina, tipo de Cristo, reconciliação",
    "icon": "🌈",
    "icon_bg": "rgba(99,102,241,.15)",
    "icon_border": "rgba(99,102,241,.4)",
    "intro": "Vendido como escravo pelos próprios irmãos, tornou-se o segundo homem mais poderoso do Egito. Sua história é a tipologia mais completa de Cristo no Antigo Testamento.",
    "meta_items": meta_item("Período", "~1700 a.C.") + meta_item("Origem", "Canaã") + meta_item("Referência", "Gênesis 37–50") + meta_item("Categoria", "Patriarca") + meta_item("Tema Central", "Providência Divina"),
    "content": jose_content,
    "prev": ("moises", "← Moisés"),
    "next": ("josue", "Josué →")
}

# ============================================================
# JOSUÉ
# ============================================================
josue_content = section("📖 Quem foi Josué?", """
        <p>Josué (hebraico: <em>Yehoshua</em> — "O Senhor salva") é o sucessor de Moisés e o conquistador de Canaã. Seu nome é idêntico ao nome hebraico de Jesus, o que não é coincidência teológica — o autor de Hebreus (4:8) faz uma distinção explícita entre o descanso que Josué deu ao povo e o descanso eterno que Jesus oferece.</p>
        <p>Josué aparece pela primeira vez em Êxodo 17, liderando Israel na batalha contra os amalequitas enquanto Moisés orava no alto do monte. Tornou-se o assistente pessoal de Moisés e um dos doze espias enviados a Canaã. Enquanto dez espias trouxeram um relatório de medo, apenas Josué e Calebe disseram: "Subamos e tomemos posse da terra, porque certamente a conquistaremos" (Números 13:30).</p>
        <p>Após 40 anos de deserto — esperando que a geração do medo morresse — Josué liderou a nova geração na travessia do Jordão e na conquista sistemática de Canaã. A queda de Jericó (Josué 6), com a marcha em silêncio e o som das trombetas, tornou-se um dos relatos militares mais memoráveis da história sagrada.</p>
""") + "\n" + verse("Quanto a mim e à minha casa, serviremos ao Senhor.", "Josué 24:15") + "\n" + theology("Josué e a Teologia do Descanso", "Hebreus 3–4 usa a conquista de Canaã como tipo do descanso espiritual em Cristo. Josué deu ao povo um descanso físico e temporário; Jesus oferece o descanso eterno da alma — 'Vinde a mim, todos os que estais cansados' (Mateus 11:28).")

personagens["josue"] = {
    "slug": "josue",
    "name": "Josué",
    "title": "Josué — O Conquistador de Canaã",
    "subtitle": "Líder Militar · ~1250 a.C. · Deserto → Canaã",
    "meta_desc": "Conheça Josué, sucessor de Moisés e conquistador de Canaã. Análise de sua liderança, a queda de Jericó e a tipologia com Jesus Cristo.",
    "keywords": "Josué, conquista de Canaã, Jericó, sucessor de Moisés, terra prometida, liderança bíblica",
    "icon": "⚔️",
    "icon_bg": "rgba(16,185,129,.15)",
    "icon_border": "rgba(16,185,129,.4)",
    "intro": "Sucessor de Moisés e conquistador de Canaã. Seu nome em hebraico é a mesma raiz do nome Jesus — e sua vida prefigura o descanso eterno que Cristo oferece.",
    "meta_items": meta_item("Período", "~1250 a.C.") + meta_item("Origem", "Tribo de Efraim") + meta_item("Referência", "Josué 1–24") + meta_item("Categoria", "Líder Militar") + meta_item("Citado no NT", "Hebreus 4:8, Atos 7:45"),
    "content": josue_content,
    "prev": ("jose", "← José"),
    "next": ("davi", "Davi →")
}

# ============================================================
# DAVI — APROFUNDAMENTO MÁXIMO
# ============================================================
davi_content = section("📖 Quem foi Davi?", """
        <p>Davi é o rei mais amado de Israel e uma das figuras mais complexas, humanas e teologicamente significativas de toda a Bíblia. Pastor, guerreiro, músico, poeta, rei e pecador — sua vida é um mosaico de glórias e fracassos que o tornam simultaneamente o maior herói e um dos exemplos mais honestos de falha humana nas Escrituras.</p>
        <p>Nascido em Belém, o menor dos oito filhos de Jessé, Davi foi escolhido por Deus quando todos os critérios humanos apontavam para seus irmãos mais velhos e imponentes. A declaração de Deus ao profeta Samuel é um dos versículos mais citados da Bíblia: "O homem olha para as aparências, mas o Senhor olha para o coração" (1 Samuel 16:7). Davi era "ruivo, de belos olhos e boa aparência" — mas o que Deus via era um coração que o buscava.</p>
        <p>Sua ascensão ao poder foi gradual e marcada por perseguição: ungido secretamente por Samuel enquanto Saul ainda reinava, Davi passou anos como fugitivo nas cavernas do deserto, perseguido pelo rei que havia servido com lealdade. Neste período escreveu alguns dos Salmos mais profundos — lamentos, clamores de socorro, expressões de confiança radical em Deus mesmo no meio do abandono aparente.</p>
""") + "\n" + section("⏱️ As Fases da Vida de Davi", """
        <div class="timeline-item"><span class="timeline-year">~1040 a.C.</span><span class="timeline-text">Nasce em Belém. Trabalha como pastor — escola de coragem e dependência de Deus (matou leão e urso para proteger o rebanho).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1025 a.C.</span><span class="timeline-text">Ungido secretamente por Samuel como futuro rei. Começa a tocar harpa para Saul, aliviando seu tormento espiritual.</span></div>
        <div class="timeline-item"><span class="timeline-year">~1024 a.C.</span><span class="timeline-text">Mata Golias com uma pedra e uma funda. "Você vem contra mim com espada, lança e dardo; mas eu venho contra você em nome do Senhor" (1 Samuel 17:45).</span></div>
        <div class="timeline-item"><span class="timeline-year">~1020–1010 a.C.</span><span class="timeline-text">Anos de fuga de Saul. Escreve Salmos 57, 142 e outros nas cavernas. Recusa duas oportunidades de matar Saul — "Não estenderei a mão contra o ungido do Senhor."</span></div>
        <div class="timeline-item"><span class="timeline-year">~1010 a.C.</span><span class="timeline-text">Morte de Saul em Gilboa. Davi lamenta com o cântico do Arco (2 Samuel 1) — chora pelo inimigo que o perseguiu.</span></div>
        <div class="timeline-item"><span class="timeline-year">~1003 a.C.</span><span class="timeline-text">Ungido rei de todo Israel. Conquista Jerusalém e a torna a capital. Traz a Arca da Aliança para Jerusalém dançando com toda a força.</span></div>
        <div class="timeline-item"><span class="timeline-year">~1000 a.C.</span><span class="timeline-text">Aliança Davídica: Deus promete que o trono de Davi será eterno e que um de seus descendentes reinará para sempre (2 Samuel 7) — a promessa messiânica central do AT.</span></div>
        <div class="timeline-item"><span class="timeline-year">~990 a.C.</span><span class="timeline-text">O grande pecado: adultério com Bate-Seba e assassinato indireto de Urias. O profeta Natã confronta Davi com a parábola da ovelha. Davi confessa: "Pequei contra o Senhor" (2 Samuel 12:13).</span></div>
        <div class="timeline-item"><span class="timeline-year">~990 a.C.</span><span class="timeline-text">Escreve o Salmo 51 — o maior salmo de arrependimento da Bíblia. "Cria em mim, ó Deus, um coração puro."</span></div>
        <div class="timeline-item"><span class="timeline-year">~970 a.C.</span><span class="timeline-text">Morte de Davi. Reina 40 anos (7 em Hebrom, 33 em Jerusalém). Salomão sobe ao trono.</span></div>
""") + "\n" + verse("Cria em mim, ó Deus, um coração puro; renova em mim um espírito firme.", "Salmos 51:10") + "\n" + section("🧠 Aprofundamento Teológico", """
        <h3>A Aliança Davídica (2 Samuel 7)</h3>
        <p>A aliança que Deus fez com Davi em 2 Samuel 7 é um dos textos mais importantes de toda a Bíblia profética. Davi queria construir uma casa (templo) para Deus; Deus respondeu que não seria Davi quem construiria uma casa para Ele, mas Ele que construiria uma casa (dinastia) para Davi. As promessas são específicas: um descendente de Davi reinará para sempre; seu trono será estabelecido eternamente; Deus será seu pai e ele será filho de Deus.</p>
        <p>Esta aliança é o fundamento de toda a esperança messiânica do Antigo Testamento. Isaías 9:6-7 anuncia um filho que reinará no trono de Davi para sempre. Jeremias 23:5 fala de um "Ramo Justo" da linhagem de Davi. Ezequiel 34:23-24 promete um "pastor" da linhagem de Davi. O anjo Gabriel, ao anunciar o nascimento de Jesus a Maria, disse: "O Senhor Deus lhe dará o trono de seu pai Davi, e ele reinará para sempre sobre a casa de Jacó" (Lucas 1:32-33).</p>
        <h3>Davi e os Salmos</h3>
        <p>Davi é o autor de pelo menos 73 dos 150 Salmos. Através deles, ele nos ensina a orar com honestidade brutal — expressando não apenas louvor e gratidão, mas também dúvida, medo, raiva, abandono e desespero. Os "Salmos de lamento" (como o Salmo 22, que Jesus citou na cruz) mostram que a fé genuína não suprime as emoções negativas — ela as traz diante de Deus.</p>
        <p>O Salmo 22 começa com "Deus meu, Deus meu, por que me abandonaste?" — as palavras exatas que Jesus gritou na cruz (Mateus 27:46). Este salmo, escrito por Davi ~1000 anos antes, descreve com precisão assombrosa a crucificação: mãos e pés perfurados (v.16), ossos deslocados (v.14), divisão das vestes por sorteio (v.18), escárnio dos espectadores (v.7-8). O Salmo 22 é a profecia mais detalhada da Paixão de Cristo no Antigo Testamento.</p>
        <h3>Davi — Um Homem Segundo o Coração de Deus</h3>
        <p>A expressão "homem segundo o coração de Deus" (1 Samuel 13:14; Atos 13:22) não significa que Davi era perfeito — seus pecados são registrados com brutal honestidade. Significa que Davi tinha um coração que respondia a Deus: quando pecava, se arrependia genuinamente; quando era corrigido, se humilhava; quando adorava, o fazia com todo o ser. A diferença entre Davi e Saul não era a ausência de pecado — era a resposta ao pecado. Saul justificou, minimizou e culpou os outros; Davi confessou, chorou e buscou restauração.</p>
""") + "\n" + theology("Davi na Tipologia Cristã", "Davi é o tipo mais direto de Cristo como Rei. Jesus é chamado 'Filho de Davi' 17 vezes no NT. A entrada triunfal em Jerusalém evoca a chegada de Davi à cidade. O reinado eterno prometido a Davi encontra seu cumprimento no reino eterno de Cristo.") + "\n" + theology("O Salmo 51 e a Doutrina do Arrependimento", "O Salmo 51 é o texto bíblico mais completo sobre o arrependimento genuíno. Ele revela que o pecado é primariamente contra Deus (v.4), que a purificação requer intervenção divina (v.7), que o coração precisa ser renovado (v.10) e que o sacrifício que Deus aceita é 'o espírito quebrantado' (v.17) — não rituais externos.") + "\n" + section("💡 Legado", """
        <p>O legado de Davi é incomensurável. Como rei, unificou as tribos de Israel e estabeleceu Jerusalém como capital eterna. Como músico, criou a tradição dos Salmos que ainda hoje é o livro de oração e louvor da Igreja. Como profeta, recebeu e transmitiu as promessas messiânicas mais específicas do AT. E como pecador arrependido, tornou-se o modelo de que a graça de Deus é maior que qualquer falha humana.</p>
        <p>A genealogia de Jesus em Mateus 1 inclui Bate-Seba ("a mulher de Urias") — Deus não apagou o pecado de Davi da história, mas o incluiu na linhagem do Redentor. Esta é a graça radical do Evangelho: Deus não trabalha apesar de nossas falhas, mas através delas.</p>
""")

personagens["davi"] = {
    "slug": "davi",
    "name": "Davi",
    "title": "Davi — O Rei Segundo o Coração de Deus",
    "subtitle": "Rei de Israel · ~1040–970 a.C. · Belém → Jerusalém",
    "meta_desc": "Conheça Davi — pastor, guerreiro, músico e rei. Análise da Aliança Davídica, os Salmos, o pecado com Bate-Seba e o legado messiânico do maior rei de Israel.",
    "keywords": "Davi, rei de Israel, Salmos, Golias, Aliança Davídica, Bate-Seba, Salmo 51, messias, Filho de Davi",
    "icon": "🎵",
    "icon_bg": "rgba(234,179,8,.15)",
    "icon_border": "rgba(234,179,8,.4)",
    "intro": "O rei mais amado de Israel — pastor, guerreiro, músico e poeta. Homem 'segundo o coração de Deus', sua vida é um mosaico de glórias e fracassos que o tornam o mais humano dos heróis bíblicos.",
    "meta_items": meta_item("Período", "~1040–970 a.C.") + meta_item("Origem", "Belém") + meta_item("Referência", "1 Samuel 16 – 1 Reis 2") + meta_item("Categoria", "Rei / Profeta") + meta_item("Citado no NT", "17x como 'Filho de Davi'"),
    "content": davi_content,
    "prev": ("josue", "← Josué"),
    "next": ("salomao", "Salomão →")
}

# ============================================================
# SALOMÃO
# ============================================================
salomao_content = section("📖 Quem foi Salomão?", """
        <p>Salomão, filho de Davi e Bate-Seba, foi o terceiro rei de Israel e o mais glorioso em termos de riqueza, sabedoria e realizações arquitetônicas. Seu reinado de 40 anos (~970–930 a.C.) representa o apogeu do Reino Unido de Israel — e também o início de sua decadência.</p>
        <p>Em Gibeom, Deus apareceu a Salomão em sonho e disse: "Pede o que queres que eu te dê." Salomão pediu sabedoria para governar o povo — e Deus ficou tão agradado com este pedido que lhe deu também riqueza e glória. Esta sabedoria se manifestou em julgamentos famosos (como o das duas mães que disputavam um bebê), em provérbios (atribuiu-se a ele 3.000), em cânticos (1.005) e em conhecimento enciclopédico da natureza.</p>
        <p>Sua maior realização foi a construção do Templo de Jerusalém — a Casa de Deus que Davi havia desejado construir. O Templo levou 7 anos para ser concluído e foi dedicado com uma das orações mais belas da Bíblia (1 Reis 8). Mas a tragédia de Salomão é que a sabedoria sem fidelidade não é suficiente: seus 700 esposas e 300 concubinas (muitas de nações estrangeiras) desviaram seu coração para outros deuses na velhice.</p>
""") + "\n" + verse("Teme a Deus e guarda os seus mandamentos, porque isso é o dever de todo homem.", "Eclesiastes 12:13") + "\n" + theology("A Tragédia de Salomão", "Salomão é o exemplo bíblico mais poderoso de que dons extraordinários não garantem fidelidade. Ele tinha mais sabedoria, mais riqueza e mais revelação divina do que qualquer outro rei — e ainda assim se desviou. O Eclesiastes é o resultado desta experiência: 'Vaidade de vaidades, tudo é vaidade' — a confissão de um homem que buscou sentido em tudo exceto em Deus.")

personagens["salomao"] = {
    "slug": "salomao",
    "name": "Salomão",
    "title": "Salomão — O Rei da Sabedoria e da Tragédia",
    "subtitle": "Rei de Israel · ~970–930 a.C. · Jerusalém",
    "meta_desc": "Conheça Salomão — o rei mais sábio e rico de Israel, construtor do Templo, autor de Provérbios e Eclesiastes. A tragédia de um homem que tinha tudo e perdeu o essencial.",
    "keywords": "Salomão, sabedoria, Templo de Jerusalém, Provérbios, Eclesiastes, Cântico dos Cânticos, rei de Israel",
    "icon": "🏛️",
    "icon_bg": "rgba(245,158,11,.15)",
    "icon_border": "rgba(245,158,11,.4)",
    "intro": "O rei mais sábio e rico de Israel. Construiu o Templo de Jerusalém e escreveu Provérbios, Eclesiastes e Cântico dos Cânticos. Sua trajetória é uma tragédia espiritual.",
    "meta_items": meta_item("Período", "~970–930 a.C.") + meta_item("Origem", "Jerusalém") + meta_item("Referência", "1 Reis 1–11") + meta_item("Categoria", "Rei / Sábio") + meta_item("Obras", "Provérbios, Eclesiastes, Cântico"),
    "content": salomao_content,
    "prev": ("davi", "← Davi"),
    "next": ("elias", "Elias →")
}

# ============================================================
# ELIAS
# ============================================================
elias_content = section("📖 Quem foi Elias?", """
        <p>Elias o Tisbita é um dos profetas mais dramáticos e poderosos do Antigo Testamento. Aparece abruptamente em 1 Reis 17 sem genealogia ou introdução — simplesmente se apresenta diante do rei Acabe com uma declaração que mudaria o curso da história: "Vive o Senhor Deus de Israel, diante de quem estou, que não haverá orvalho nem chuva nestes anos, senão segundo a minha palavra."</p>
        <p>O confronto no Monte Carmelo (1 Reis 18) é um dos episódios mais dramáticos da Bíblia: 450 profetas de Baal contra um único profeta do Senhor. O fogo que desceu do céu consumindo o sacrifício encharcado de água foi a resposta divina à oração de Elias — e resultou na morte dos profetas de Baal e no fim de três anos de seca.</p>
        <p>Mas imediatamente após este triunfo, Elias fugiu para o deserto em depressão suicida: "Já basta, Senhor; tira a minha vida." A resposta de Deus não foi repreensão — foi pão quente e água fresca, descanso, e uma voz mansa e delicada no Monte Horebe. Esta narrativa é um dos textos mais compassivos da Bíblia sobre saúde mental e o cuidado de Deus com seus servos exaustos.</p>
""") + "\n" + verse("Depois do fogo, uma voz mansa e delicada. E foi assim que, ao ouvi-la, Elias cobriu o rosto com o manto.", "1 Reis 19:12-13") + "\n" + theology("Elias no Novo Testamento", "Elias aparece na Transfiguração ao lado de Moisés e Jesus (Mateus 17) — representando os Profetas ao lado da Lei. João Batista veio 'no espírito e poder de Elias' (Lucas 1:17). Tiago 5:17 usa Elias como exemplo de oração eficaz: 'Era um homem sujeito às mesmas paixões que nós' — a oração de um homem comum pode mover o céu.")

personagens["elias"] = {
    "slug": "elias",
    "name": "Elias",
    "title": "Elias — O Profeta do Fogo",
    "subtitle": "Profeta · ~875 a.C. · Israel do Norte",
    "meta_desc": "Conheça Elias — o profeta que confrontou Acabe, chamou fogo do céu no Monte Carmelo e foi arrebatado em carro de fogo. Análise de sua vida, depressão e legado.",
    "keywords": "Elias, Monte Carmelo, profeta, fogo do céu, Acabe, Jezabel, João Batista, arrebatamento",
    "icon": "🔥",
    "icon_bg": "rgba(239,68,68,.15)",
    "icon_border": "rgba(239,68,68,.4)",
    "intro": "O profeta do fogo. Confrontou o rei Acabe e 450 profetas de Baal. Fugiu ao deserto em depressão e foi restaurado por Deus. Arrebatado ao céu em carro de fogo.",
    "meta_items": meta_item("Período", "~875 a.C.") + meta_item("Origem", "Tisbe de Gileade") + meta_item("Referência", "1 Reis 17 – 2 Reis 2") + meta_item("Categoria", "Profeta") + meta_item("Citado no NT", "Mateus 17, Tiago 5:17"),
    "content": elias_content,
    "prev": ("salomao", "← Salomão"),
    "next": ("isaias", "Isaías →")
}

# ============================================================
# ISAÍAS
# ============================================================
isaias_content = section("📖 Quem foi Isaías?", """
        <p>Isaías, filho de Amós, profetizou em Jerusalém durante os reinados de Uzias, Jotão, Acaz e Ezequias (~740–700 a.C.) — um período de crise política e espiritual para Judá, com a ameaça assíria e a infidelidade crescente do povo. Seu chamado profético, narrado no capítulo 6, é uma das visões mais sublimes da Bíblia: o trono de Deus, os serafins clamando "Santo, santo, santo", e a confissão de indignidade que precede o envio.</p>
        <p>Isaías é frequentemente chamado de "o evangelista do Antigo Testamento" por causa da riqueza e precisão de suas profecias messiânicas. O livro de Isaías é citado no Novo Testamento mais do que qualquer outro livro do AT — mais de 65 citações diretas. Jesus iniciou seu ministério público lendo Isaías 61 na sinagoga de Nazaré: "O Espírito do Senhor está sobre mim, porque me ungiu para pregar boas novas aos pobres."</p>
""") + "\n" + verse("Ele foi ferido por causa das nossas transgressões, e moído por causa das nossas iniquidades; o castigo que nos traz a paz estava sobre ele, e pelas suas pisaduras fomos sarados.", "Isaías 53:5") + "\n" + theology("Isaías 53 — A Profecia da Cruz", "Escrita ~700 anos antes de Cristo, Isaías 53 descreve com precisão assombrosa a Paixão: desprezado e rejeitado (v.3), carregou nossas dores (v.4), ferido por nossas transgressões (v.5), como ovelha ao matadouro (v.7), sepultado com os ricos (v.9), verá a luz após a angústia de sua alma (v.11). É a profecia mais citada sobre Jesus no NT.")

personagens["isaias"] = {
    "slug": "isaias",
    "name": "Isaías",
    "title": "Isaías — O Evangelista do Antigo Testamento",
    "subtitle": "Profeta · ~740–700 a.C. · Jerusalém",
    "meta_desc": "Conheça Isaías — o profeta que descreveu a crucificação 700 anos antes em Isaías 53. Análise de seu chamado, profecias messiânicas e visão do trono de Deus.",
    "keywords": "Isaías, Isaías 53, servo sofredor, profecia messiânica, Santo Santo Santo, evangelista AT",
    "icon": "📜",
    "icon_bg": "rgba(139,92,246,.15)",
    "icon_border": "rgba(139,92,246,.4)",
    "intro": "O 'evangelista do Antigo Testamento'. Suas profecias sobre o Servo Sofredor (Isaías 53) são as mais detalhadas sobre a morte de Cristo — escritas 700 anos antes.",
    "meta_items": meta_item("Período", "~740–700 a.C.") + meta_item("Origem", "Jerusalém") + meta_item("Referência", "Isaías 1–66") + meta_item("Categoria", "Profeta Maior") + meta_item("Citado no NT", "65+ vezes"),
    "content": isaias_content,
    "prev": ("elias", "← Elias"),
    "next": ("jeremias", "Jeremias →")
}

# ============================================================
# JEREMIAS
# ============================================================
jeremias_content = section("📖 Quem foi Jeremias?", """
        <p>Jeremias, filho de Hilquias, foi chamado ao ministério profético antes mesmo de nascer: "Antes de te formar no ventre materno, eu te conheci; antes de saires da madre, eu te santifiquei; eu te constituí profeta às nações" (Jeremias 1:5). Profetizou por mais de 40 anos (~627–586 a.C.) durante o período mais sombrio da história de Judá — desde o reinado de Josias até a destruição de Jerusalém e o exílio babilônico.</p>
        <p>Chamado de "o profeta que chorou", Jeremias é o mais pessoal e emocionalmente transparente dos profetas. Suas "Confissões" (Jeremias 11–20) são lamentos de uma alma torturada — ele amaldiçoa o dia em que nasceu, questiona Deus, expressa raiva e desespero. E ainda assim continua profetizando. Sua vida é o modelo de fidelidade sem recompensa visível: pregou por décadas sem ver uma única conversão, foi preso, jogado em uma cisterna, e viu Jerusalém ser destruída exatamente como havia anunciado.</p>
""") + "\n" + verse("Farei uma nova aliança com a casa de Israel... Porei a minha lei no seu interior e a escreverei no seu coração.", "Jeremias 31:31-33") + "\n" + theology("A Nova Aliança de Jeremias 31", "A profecia da Nova Aliança em Jeremias 31:31-34 é citada integralmente em Hebreus 8 — a citação mais longa do AT no NT. Jesus, na Última Ceia, disse: 'Este cálice é a nova aliança no meu sangue' (Lucas 22:20). A Nova Aliança não é uma lei externa gravada em pedra, mas uma lei interna gravada no coração pelo Espírito Santo.")

personagens["jeremias"] = {
    "slug": "jeremias",
    "name": "Jeremias",
    "title": "Jeremias — O Profeta que Chorou",
    "subtitle": "Profeta · ~627–586 a.C. · Judá",
    "meta_desc": "Conheça Jeremias — o profeta que anunciou a destruição de Jerusalém e a Nova Aliança. Análise de sua vida, sofrimento e a profecia de Jeremias 31.",
    "keywords": "Jeremias, Nova Aliança, destruição de Jerusalém, profeta, lamentações, Jeremias 31",
    "icon": "😢",
    "icon_bg": "rgba(14,165,233,.15)",
    "icon_border": "rgba(14,165,233,.4)",
    "intro": "O 'profeta que chorou'. Chamado antes de nascer, profetizou a destruição de Jerusalém por décadas sem ser ouvido. Anunciou a Nova Aliança — cumprida em Cristo.",
    "meta_items": meta_item("Período", "~627–586 a.C.") + meta_item("Origem", "Anatote, Judá") + meta_item("Referência", "Jeremias 1–52") + meta_item("Categoria", "Profeta Maior") + meta_item("Citado no NT", "Hebreus 8:8-12"),
    "content": jeremias_content,
    "prev": ("isaias", "← Isaías"),
    "next": ("paulo", "Paulo →")
}

# ============================================================
# PAULO — APROFUNDAMENTO MÁXIMO
# ============================================================
paulo_content = section("📖 Quem foi Paulo?", """
        <p>Paulo de Tarso é, depois de Jesus Cristo, a figura mais influente da história do cristianismo. Suas 13 epístolas formam o núcleo da teologia cristã — da doutrina da justificação pela fé em Romanos à escatologia em 1 Tessalonicenses, da eclesiologia em Efésios à cristologia em Colossenses. Sem Paulo, o cristianismo provavelmente teria permanecido uma seita judaica restrita à Palestina.</p>
        <p>Nascido em Tarso da Cilícia (~5 d.C.), Paulo era cidadão romano por nascimento — um privilégio raro que usaria estrategicamente em seu ministério. Filho de fariseus, estudou em Jerusalém aos pés de Gamaliel, o maior rabino de sua geração, tornando-se um dos mais brilhantes estudiosos da Lei de sua época. Sua educação combinava o rigor do judaísmo farisaico com a cultura helenística de Tarso — uma combinação única que o tornaria o teólogo perfeito para comunicar o Evangelho ao mundo greco-romano.</p>
        <p>Antes de sua conversão, Paulo (então chamado Saulo) era o perseguidor mais fervoroso da Igreja nascente. Esteve presente e aprovou a lapidação de Estêvão, o primeiro mártir cristão (Atos 7:58). Obteve cartas do Sumo Sacerdote para prender cristãos em Damasco. Era, por suas próprias palavras, "quanto ao zelo, perseguidor da Igreja; quanto à justiça que há na lei, irrepreensível" (Filipenses 3:6).</p>
        <p>A conversão no caminho de Damasco (~34 d.C.) foi um dos eventos mais transformadores da história. Uma luz do céu o derrubou, e ele ouviu: "Saulo, Saulo, por que me persegues?" A resposta de Paulo — "Quem és tu, Senhor?" — e a resposta de Jesus — "Eu sou Jesus, a quem tu persegues" — mudaram não apenas a vida de Paulo, mas o curso do Evangelho no mundo.</p>
""") + "\n" + section("⏱️ As Três Viagens Missionárias", """
        <div class="timeline-item"><span class="timeline-year">~46–48 d.C.</span><span class="timeline-text"><strong>1ª Viagem:</strong> Chipre, Antioquia da Pisídia, Icônio, Listra, Derbe. Primeira pregação sistemática aos gentios. Escreveu Gálatas (~48 d.C.).</span></div>
        <div class="timeline-item"><span class="timeline-year">~49 d.C.</span><span class="timeline-text"><strong>Concílio de Jerusalém:</strong> Debate sobre a circuncisão dos gentios. Paulo defende a justificação pela fé sem obras da lei. Vitória do Evangelho da graça.</span></div>
        <div class="timeline-item"><span class="timeline-year">~49–52 d.C.</span><span class="timeline-text"><strong>2ª Viagem:</strong> Filipos, Tessalônica, Bereia, Atenas (discurso no Areópago), Corinto (18 meses). Escreveu 1 e 2 Tessalonicenses.</span></div>
        <div class="timeline-item"><span class="timeline-year">~53–57 d.C.</span><span class="timeline-text"><strong>3ª Viagem:</strong> Éfeso (3 anos — centro de toda a Ásia Menor), Macedônia, Grécia. Escreveu 1 e 2 Coríntios, Romanos, Gálatas (revisão).</span></div>
        <div class="timeline-item"><span class="timeline-year">~57–59 d.C.</span><span class="timeline-text"><strong>Prisão em Cesareia:</strong> Preso após tumulto em Jerusalém. Apela a César como cidadão romano. Escreveu possivelmente algumas epístolas da prisão.</span></div>
        <div class="timeline-item"><span class="timeline-year">~60–62 d.C.</span><span class="timeline-text"><strong>Prisão em Roma (1ª):</strong> Prisão domiciliar. Escreveu Efésios, Filipenses, Colossenses, Filemom — as "Epístolas da Prisão".</span></div>
        <div class="timeline-item"><span class="timeline-year">~62–67 d.C.</span><span class="timeline-text"><strong>Ministério final e 2ª prisão:</strong> Viagens à Espanha (possível), Creta, Éfeso. Escreveu 1 e 2 Timóteo, Tito. Preso novamente em Roma.</span></div>
        <div class="timeline-item"><span class="timeline-year">~67 d.C.</span><span class="timeline-text"><strong>Martírio:</strong> Decapitado em Roma sob Nero. Suas últimas palavras: "Combati o bom combate, terminei a corrida, guardei a fé" (2 Timóteo 4:7).</span></div>
""") + "\n" + verse("Porque para mim o viver é Cristo, e o morrer é lucro.", "Filipenses 1:21") + "\n" + section("🧠 Aprofundamento Teológico", """
        <h3>A Teologia da Justificação em Romanos</h3>
        <p>Romanos é a carta mais sistemática e teologicamente densa do Novo Testamento — o que Martinho Lutero chamou de "o mais puro Evangelho." Paulo desenvolve o argumento em quatro movimentos: (1) Todos os seres humanos são pecadores e estão sob o julgamento de Deus (caps. 1–3); (2) A justificação é pela fé em Cristo, não pelas obras da lei — e isto sempre foi assim, desde Abraão (caps. 3–4); (3) A vida na graça: paz com Deus, morte ao pecado, vida no Espírito (caps. 5–8); (4) O plano de Deus para Israel e os gentios (caps. 9–11); (5) A ética cristã como resposta à graça (caps. 12–16).</p>
        <p>O coração de Romanos é 3:21-26 — a "sala do trono" da teologia paulina: "Sendo justificados gratuitamente pela sua graça, pela redenção que há em Cristo Jesus, a quem Deus propôs como propiciação pela fé no seu sangue." Quatro palavras-chave definem a salvação: <strong>gratuitamente</strong> (é dom, não mérito), <strong>graça</strong> (favor imerecido), <strong>redenção</strong> (libertação mediante pagamento de preço) e <strong>propiciação</strong> (satisfação da ira justa de Deus).</p>
        <h3>Paulo e a Doutrina da Graça</h3>
        <p>Em Efésios 2:8-9, Paulo formula a doutrina da graça com precisão máxima: "Porque pela graça sois salvos, mediante a fé; e isto não vem de vós; é dom de Deus. Não vem das obras, para que ninguém se glorie." Esta declaração tem três partes: a causa da salvação é a graça; o meio é a fé; e a origem de ambas é Deus — não o ser humano. A fé em si mesma é descrita como "dom de Deus", o que significa que até a capacidade de crer é uma concessão divina.</p>
        <h3>Paulo e a Cristologia de Filipenses 2</h3>
        <p>O "hino cristológico" de Filipenses 2:5-11 é um dos textos mais sublimes do NT. Paulo descreve a kénosis (esvaziamento) de Cristo: "Sendo em forma de Deus, não teve por usurpação ser igual a Deus, mas esvaziou-se a si mesmo, tomando a forma de servo... humilhou-se a si mesmo, tornando-se obediente até à morte, e morte de cruz." E a exaltação consequente: "Pelo que também Deus o exaltou soberanamente e lhe deu um nome que é sobre todo o nome." Este texto é o fundamento da doutrina da encarnação e da exaltação de Cristo.</p>
        <h3>Paulo e a Escatologia</h3>
        <p>Em 1 Tessalonicenses 4:13-18, Paulo responde à preocupação dos tessalonicenses sobre os mortos em Cristo. Sua resposta introduz a doutrina da ressurreição dos mortos e da parousia (segunda vinda de Cristo). Em 1 Coríntios 15 — o capítulo mais extenso sobre a ressurreição no NT — Paulo argumenta que a ressurreição de Cristo é o fundamento de toda a fé cristã: "Se Cristo não ressuscitou, a nossa pregação é vã, e vã é também a vossa fé" (v.14).</p>
""") + "\n" + theology("Paulo e a Reforma Protestante", "Martinho Lutero, ao estudar Romanos 1:17 ('o justo viverá pela fé'), teve a experiência que desencadeou a Reforma Protestante. A redescoberta da justificação pela fé de Paulo — contra a teologia das obras da Igreja medieval — foi o evento mais transformador da história cristã desde o Pentecostes.") + "\n" + theology("Paulo e a Teologia da Cruz", "Em 1 Coríntios 1:18-25, Paulo declara que a cruz é 'loucura para os que se perdem, mas para nós que somos salvos é o poder de Deus.' A teologia da cruz (theologia crucis) de Paulo é o antídoto contra toda teologia da glória que busca Deus no poder, no sucesso e na prosperidade.") + "\n" + section("💡 Legado", """
        <p>Paulo escreveu 13 epístolas que formam quase metade do Novo Testamento. Fundou igrejas em pelo menos 4 países. Viajou mais de 15.000 km em suas missões. Sofreu naufrágio, prisão, açoitamento, apedrejamento e perseguição constante. E ainda assim escreveu: "Aprendi a estar contente em qualquer estado em que me encontre" (Filipenses 4:11).</p>
        <p>Seu legado teológico moldou o pensamento de Agostinho, Tomás de Aquino, Lutero, Calvino, Wesley e praticamente todos os grandes teólogos cristãos. A pergunta que ele fez no caminho de Damasco — "Quem és tu, Senhor?" — é a pergunta que cada ser humano precisa responder. E a resposta que ele recebeu — "Eu sou Jesus" — é o fundamento de toda a fé cristã.</p>
""")

personagens["paulo"] = {
    "slug": "paulo",
    "name": "Paulo de Tarso",
    "title": "Paulo de Tarso — O Apóstolo dos Gentios",
    "subtitle": "Apóstolo · ~5–67 d.C. · Tarso → Roma",
    "meta_desc": "Conheça Paulo de Tarso — o maior teólogo do NT, apóstolo dos gentios, autor de 13 epístolas. Análise de Romanos, Efésios, Filipenses e sua teologia da graça.",
    "keywords": "Paulo, Saulo, apóstolo, Romanos, Efésios, justificação pela fé, graça, viagens missionárias, Reforma Protestante",
    "icon": "✍️",
    "icon_bg": "rgba(0,168,225,.15)",
    "icon_border": "rgba(0,168,225,.4)",
    "intro": "O maior teólogo do Novo Testamento. Perseguidor da Igreja convertido por uma visão de Cristo, tornou-se o apóstolo dos gentios e autor de 13 epístolas que definiram a teologia cristã.",
    "meta_items": meta_item("Período", "~5–67 d.C.") + meta_item("Origem", "Tarso da Cilícia") + meta_item("Referência", "Atos 9–28 + 13 Epístolas") + meta_item("Categoria", "Apóstolo / Teólogo") + meta_item("Influência", "Reforma Protestante"),
    "content": paulo_content,
    "prev": ("jeremias", "← Jeremias"),
    "next": ("pedro", "Pedro →")
}

# ============================================================
# PEDRO
# ============================================================
pedro_content = section("📖 Quem foi Pedro?", """
        <p>Simão Pedro, filho de Jonas e irmão de André, era pescador do Mar da Galileia quando Jesus o chamou com as palavras: "Segue-me, e eu te farei pescador de homens" (Mateus 4:19). Jesus lhe deu o nome Cefas (aramaico) ou Pedro (grego) — ambos significando "rocha" — uma promessa de caráter que ele ainda precisaria desenvolver.</p>
        <p>Pedro é o discípulo mais proeminente dos doze — sempre o primeiro a falar, o primeiro a agir, o primeiro a cometer erros monumentais e o primeiro a ser restaurado. Ele caminhou sobre as águas e afundou. Confessou que Jesus era o Cristo e logo depois tentou impedir a cruz. Jurou que nunca negaria Jesus e o negou três vezes antes do amanhecer. Sua vida é um retrato honesto de um homem em processo de transformação — não um herói perfeito, mas um discípulo que caía e se levantava.</p>
        <p>A restauração de Pedro à beira do Mar da Galileia (João 21) é uma das cenas mais emocionantes dos Evangelhos. Três vezes Jesus perguntou: "Simão, filho de Jonas, tu me amas?" — uma pergunta para cada negação. E três vezes comissionou: "Apascenta as minhas ovelhas." A graça de Jesus não apenas perdoou Pedro — o reinstalou em seu chamado.</p>
""") + "\n" + verse("Senhor, para quem iremos? Tu tens as palavras da vida eterna.", "João 6:68") + "\n" + theology("Pedro e o Primado", "A Igreja Católica Romana interpreta Mateus 16:18 ('sobre esta pedra edificarei a minha Igreja') como o estabelecimento do primado de Pedro e da sucessão apostólica papal. A tradição protestante interpreta 'esta pedra' como a confissão de fé de Pedro ('Tu és o Cristo'), não Pedro em si. Este debate hermenêutico é um dos mais significativos da história cristã.")

personagens["pedro"] = {
    "slug": "pedro",
    "name": "Pedro",
    "title": "Pedro — A Rocha que Caiu e se Levantou",
    "subtitle": "Apóstolo · ~1–64 d.C. · Galileia → Roma",
    "meta_desc": "Conheça Pedro — o líder dos doze apóstolos, pescador que negou Jesus e foi restaurado. Análise de Pentecostes, as epístolas e o martírio em Roma.",
    "keywords": "Pedro, apóstolo, Pentecostes, negação de Jesus, restauração, 1 Pedro, 2 Pedro, papa",
    "icon": "🪨",
    "icon_bg": "rgba(59,130,246,.15)",
    "icon_border": "rgba(59,130,246,.4)",
    "intro": "O líder dos doze apóstolos. Pescador impulsivo que negou Jesus três vezes e foi restaurado com a mesma ternura que havia sido chamado. Pregou o primeiro sermão de Pentecostes.",
    "meta_items": meta_item("Período", "~1–64 d.C.") + meta_item("Origem", "Betsaida / Cafarnaum") + meta_item("Referência", "Evangelhos, Atos, 1-2 Pedro") + meta_item("Categoria", "Apóstolo") + meta_item("Martírio", "Crucificado de cabeça para baixo"),
    "content": pedro_content,
    "prev": ("paulo", "← Paulo"),
    "next": ("joao", "João →")
}

# ============================================================
# JOÃO
# ============================================================
joao_content = section("📖 Quem foi João?", """
        <p>João, filho de Zebedeu e irmão de Tiago, era pescador da Galileia quando foi chamado por Jesus. Junto com Pedro e Tiago, formou o círculo íntimo dos três discípulos que estiveram presentes na Transfiguração, na ressurreição da filha de Jairo e na agonia de Getsêmani. É identificado no quarto Evangelho como "o discípulo amado" — o único dos doze que permaneceu ao pé da cruz.</p>
        <p>João e Tiago eram chamados por Jesus de "Boanerges" — filhos do trovão — por causa de seu temperamento impetuoso. Em Lucas 9:54, pediram a Jesus permissão para chamar fogo do céu sobre uma aldeia samaritana. Mas João foi transformado pelo amor de Cristo em o apóstolo do amor — suas epístolas repetem a palavra "amor" (agape) mais do que qualquer outro escritor do NT.</p>
        <p>João foi o único dos doze apóstolos que não foi martirizado — morreu de velhice em Éfeso, possivelmente aos ~90 anos. Antes disso, foi exilado na ilha de Patmos pelo imperador Domiciano, onde recebeu as visões do Apocalipse. Seu Evangelho, escrito por último (~90 d.C.), é o mais teológico e contemplativo dos quatro — começa não com o nascimento de Jesus, mas com a eternidade: "No princípio era o Verbo."</p>
""") + "\n" + verse("Deus é amor; e quem permanece no amor permanece em Deus, e Deus nele.", "1 João 4:16") + "\n" + theology("O Prólogo de João e a Cristologia do Logos", "João 1:1-18 é o texto cristológico mais elevado do NT. 'No princípio era o Verbo (Logos), e o Verbo estava com Deus, e o Verbo era Deus' — uma afirmação explícita da preexistência e divindade de Cristo. O conceito de Logos era familiar tanto aos judeus (Sabedoria de Deus) quanto aos gregos (razão universal), tornando João o evangelista perfeito para o mundo helenístico.")

personagens["joao"] = {
    "slug": "joao",
    "name": "João",
    "title": "João — O Discípulo Amado",
    "subtitle": "Apóstolo · ~6–100 d.C. · Galileia → Éfeso → Patmos",
    "meta_desc": "Conheça João — o discípulo amado, autor do quarto Evangelho, das três epístolas e do Apocalipse. Análise do Logos, da teologia do amor e das visões de Patmos.",
    "keywords": "João, discípulo amado, Evangelho de João, Apocalipse, Logos, amor, Patmos, Éfeso",
    "icon": "❤️",
    "icon_bg": "rgba(236,72,153,.15)",
    "icon_border": "rgba(236,72,153,.4)",
    "intro": "O 'discípulo amado'. O único dos doze que não foi martirizado. Escreveu o quarto Evangelho, três epístolas e o Apocalipse. Sua teologia do amor é a mais profunda do NT.",
    "meta_items": meta_item("Período", "~6–100 d.C.") + meta_item("Origem", "Betsaida, Galileia") + meta_item("Referência", "João, 1-3 João, Apocalipse") + meta_item("Categoria", "Apóstolo") + meta_item("Exílio", "Ilha de Patmos"),
    "content": joao_content,
    "prev": ("pedro", "← Pedro"),
    "next": ("maria", "Maria →")
}

# ============================================================
# MARIA
# ============================================================
maria_content = section("📖 Quem foi Maria?", """
        <p>Maria de Nazaré é a figura feminina mais importante da história cristã — a mulher que disse "sim" a Deus e tornou possível a encarnação do Filho eterno. Jovem de uma família humilde de Nazaré, provavelmente com ~14-16 anos quando o anjo Gabriel a visitou, Maria é apresentada nos Evangelhos como uma mulher de fé profunda, coragem extraordinária e meditação constante: "Maria guardava todas estas coisas, meditando-as no seu coração" (Lucas 2:19).</p>
        <p>A Anunciação (Lucas 1:26-38) é um dos momentos mais sagrados da Bíblia. O anjo Gabriel saudou Maria como "cheia de graça" (kecharitomene — particípio perfeito passivo em grego, indicando um estado permanente de graça recebida). Maria perguntou: "Como se fará isso, pois não conheço homem?" — uma pergunta de fé, não de dúvida. E quando recebeu a resposta, disse: "Eis aqui a serva do Senhor; faça-se em mim segundo a tua palavra." Esta resposta é o modelo perfeito de disponibilidade a Deus.</p>
        <p>O Magnificat (Lucas 1:46-55) — o cântico de Maria ao visitar Isabel — é uma das composições poéticas mais belas do NT. Nele, Maria revela sua formação bíblica profunda (há ecos de Ana em 1 Samuel 2), sua consciência teológica (Deus que derruba poderosos e exalta humildes) e sua identidade como a "serva do Senhor" que se torna instrumento da maior intervenção divina da história.</p>
""") + "\n" + verse("Eis aqui a serva do Senhor; faça-se em mim segundo a tua palavra.", "Lucas 1:38") + "\n" + theology("Maria na Teologia Católica e Protestante", "A veneração de Maria é um dos pontos de maior divergência entre o catolicismo e o protestantismo. A Igreja Católica afirma a Imaculada Conceição (Maria nasceu sem pecado original), a Assunção (foi levada ao céu em corpo e alma) e a intercessão de Maria. O protestantismo honra Maria como a maior das mulheres e modelo de fé, mas rejeita as doutrinas que não têm base bíblica explícita. Ambas as tradições concordam que Maria é 'bendita entre as mulheres' (Lucas 1:42).")

personagens["maria"] = {
    "slug": "maria",
    "name": "Maria, Mãe de Jesus",
    "title": "Maria — A Serva do Senhor",
    "subtitle": "Mãe de Jesus · ~20 a.C. – ~50 d.C. · Nazaré",
    "meta_desc": "Conheça Maria, mãe de Jesus — a jovem de Nazaré que disse 'sim' a Deus. Análise da Anunciação, do Magnificat, da Cruz e de seu papel na história da salvação.",
    "keywords": "Maria, mãe de Jesus, Anunciação, Magnificat, Nazaré, Theotokos, encarnação, fé",
    "icon": "🌟",
    "icon_bg": "rgba(167,139,250,.15)",
    "icon_border": "rgba(167,139,250,.4)",
    "intro": "A jovem de Nazaré que disse 'sim' a Deus e mudou a história. Sua fé — 'Faça-se em mim segundo a tua palavra' — é o modelo de disponibilidade total. A primeira discípula de Jesus.",
    "meta_items": meta_item("Período", "~20 a.C. – ~50 d.C.") + meta_item("Origem", "Nazaré") + meta_item("Referência", "Lucas 1–2, João 2, Atos 1") + meta_item("Categoria", "Mãe de Jesus") + meta_item("Título", "Theotokos (Mãe de Deus)"),
    "content": maria_content,
    "prev": ("joao", "← João"),
    "next": ("rute", "Rute →")
}

# ============================================================
# RUTE
# ============================================================
rute_content = section("📖 Quem foi Rute?", """
        <p>Rute é uma das figuras mais amadas do Antigo Testamento — uma mulher moabita (de nação estrangeira e historicamente hostil a Israel) que escolheu o Deus de Israel e o povo de sua sogra Noemi, tornando-se um dos exemplos mais belos de lealdade, graça e providência divina na Bíblia.</p>
        <p>Após a morte de seu marido israelita em Moabe, Rute recusou-se a retornar à sua família e aos seus deuses. Suas palavras a Noemi são um dos textos mais citados da Bíblia em cerimônias de casamento e de amizade: "Para onde tu fores, eu irei; onde tu ficares, eu ficarei; o teu povo será o meu povo, e o teu Deus será o meu Deus" (Rute 1:16). Esta declaração não é apenas lealdade humana — é uma confissão de fé. Rute estava escolhendo o Deus de Israel.</p>
        <p>Em Belém, Rute foi ao campo de Boaz para respigar — recolher os grãos deixados pelos ceifeiros, um direito garantido pela lei mosaica aos pobres e estrangeiros (Levítico 19:9-10). Boaz, parente de Noemi, notou Rute e ordenou que os ceifeiros deixassem grãos extras para ela. Seu casamento com Boaz — que atuou como "goel" (resgatador, parente próximo) — tornou-se a história de amor mais pura do AT e uma prefiguração de Cristo como nosso Redentor.</p>
""") + "\n" + verse("Para onde tu fores, eu irei; onde tu ficares, eu ficarei; o teu povo será o meu povo, e o teu Deus será o meu Deus.", "Rute 1:16") + "\n" + theology("Rute e a Teologia da Inclusão", "O livro de Rute é uma resposta narrativa ao exclusivismo étnico — uma mulher moabita, de uma nação maldita (Deuteronômio 23:3), torna-se bisavó do rei Davi e ancestral de Jesus Cristo (Mateus 1:5). A graça de Deus não tem fronteiras étnicas. Rute é a prova de que a aliança de Deus sempre foi para 'todas as famílias da terra' (Gênesis 12:3).")

personagens["rute"] = {
    "slug": "rute",
    "name": "Rute",
    "title": "Rute — A Lealdade que Atravessa Fronteiras",
    "subtitle": "Moabita · ~1100 a.C. · Moabe → Belém",
    "meta_desc": "Conheça Rute — a moabita que escolheu o Deus de Israel. Análise de sua lealdade, o resgate de Boaz como tipo de Cristo e seu lugar na genealogia de Jesus.",
    "keywords": "Rute, Noemi, Boaz, goel, lealdade, Belém, genealogia de Jesus, inclusão, graça",
    "icon": "🌾",
    "icon_bg": "rgba(251,146,60,.15)",
    "icon_border": "rgba(251,146,60,.4)",
    "intro": "A moabita que escolheu o Deus de Israel e o povo de sua sogra Noemi. Sua lealdade é um dos mais belos retratos da graça na Bíblia. Bisavó do rei Davi e ancestral de Jesus.",
    "meta_items": meta_item("Período", "~1100 a.C.") + meta_item("Origem", "Moabe") + meta_item("Referência", "Livro de Rute") + meta_item("Categoria", "Mulher de Fé") + meta_item("Genealogia", "Mateus 1:5"),
    "content": rute_content,
    "prev": ("maria", "← Maria"),
    "next": ("ester", "Ester →")
}

# ============================================================
# ESTER
# ============================================================
ester_content = section("📖 Quem foi Ester?", """
        <p>Ester (hebraico: Hadassá — murta; persa: Ester — estrela) é a heroína do livro que leva seu nome — uma jovem judia órfã criada por seu primo Mardoqueu que se tornou rainha da Pérsia e salvou seu povo de um genocídio. Seu livro é um dos dois únicos livros da Bíblia que não mencionam explicitamente o nome de Deus (o outro é Cântico dos Cânticos), mas a providência divina permeia cada página.</p>
        <p>O contexto histórico é o reinado de Assuero (Xerxes I, ~486–465 a.C.) em Susa, capital da Pérsia. Após a destituição da rainha Vasti, Ester foi escolhida entre as jovens mais belas do império para ser a nova rainha — sem revelar sua identidade judaica. Quando Hamã, o primeiro-ministro, obteve do rei um decreto para exterminar todos os judeus do império, Mardoqueu desafiou Ester com as palavras que se tornaram o versículo central do livro: "Quem sabe se não foi para um momento como este que chegaste à posição de rainha?" (Ester 4:14).</p>
        <p>Ester convocou um jejum de três dias e então entrou sem convite na presença do rei — um ato punível com a morte. Sua coragem foi recompensada: o rei estendeu o cetro de ouro, Hamã foi enforcado na própria forca que havia preparado para Mardoqueu, e os judeus foram autorizados a se defender. A festa de Purim, celebrada até hoje no judaísmo, comemora esta libertação.</p>
""") + "\n" + verse("Quem sabe se não foi para um momento como este que chegaste à posição de rainha?", "Ester 4:14") + "\n" + theology("A Providência Oculta em Ester", "A ausência do nome de Deus em Ester não significa sua ausência — significa que Deus age através de eventos aparentemente naturais: a beleza de Ester, a insônia do rei, o orgulho de Hamã, o timing perfeito de cada evento. Lutero ficou desconfortável com o livro por esta razão, mas a teologia da providência oculta é precisamente o ponto: Deus governa a história mesmo quando não é visto.")

personagens["ester"] = {
    "slug": "ester",
    "name": "Ester",
    "title": "Ester — A Rainha que Salvou um Povo",
    "subtitle": "Rainha da Pérsia · ~480 a.C. · Susa",
    "meta_desc": "Conheça Ester — a rainha judia que arriscou a vida para salvar seu povo do genocídio. Análise de sua coragem, a providência divina e a festa de Purim.",
    "keywords": "Ester, Mardoqueu, Hamã, Purim, Pérsia, Xerxes, providência divina, coragem, genocídio",
    "icon": "👑",
    "icon_bg": "rgba(244,63,94,.15)",
    "icon_border": "rgba(244,63,94,.4)",
    "intro": "A rainha que arriscou a vida para salvar seu povo. Judia na corte persa, usou sua posição para impedir o genocídio de Israel. 'Para um momento como este' — Ester 4:14.",
    "meta_items": meta_item("Período", "~480 a.C.") + meta_item("Origem", "Susa, Pérsia") + meta_item("Referência", "Livro de Ester") + meta_item("Categoria", "Rainha / Heroína") + meta_item("Festa", "Purim"),
    "content": ester_content,
    "prev": ("rute", "← Rute"),
    "next": None
}

# ============================================================
# GERAR ARQUIVOS
# ============================================================
lista = list(personagens.keys())

for slug, p in personagens.items():
    prev_html = ""
    next_html = ""
    if p["prev"]:
        prev_html = f'<a href="/personagens/{p["prev"][0]}.html">{p["prev"][1]}</a>'
    if p["next"]:
        next_html = f'<a href="/personagens/{p["next"][0]}.html">{p["next"][1]}</a>'

    html = TEMPLATE.format(
        slug=p["slug"],
        name=p["name"],
        title=p["title"],
        subtitle=p["subtitle"],
        meta_desc=p["meta_desc"],
        keywords=p["keywords"],
        icon=p["icon"],
        icon_bg=p["icon_bg"],
        icon_border=p["icon_border"],
        intro=p["intro"],
        meta_items=p["meta_items"],
        content=p["content"],
        prev_link=prev_html,
        next_link=next_html
    )

    path = os.path.join(BASE, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [OK] {slug}.html — {len(html):,} chars")

print(f"\nTotal: {len(personagens)} páginas geradas em {BASE}")
