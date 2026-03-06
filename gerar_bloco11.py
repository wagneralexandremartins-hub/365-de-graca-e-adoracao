#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera os 7 módulos restantes do Bloco 11 — Conflitos Religiosos Contemporâneos.
"""

import os

BASE = "/home/ubuntu/365-de-graca-e-adoracao/11-conflitos-contemporaneos"

CSS_BASE = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: #0f172a; color: #e2e8f0; font-family: 'Georgia', serif; line-height: 1.7; }
    a { color: inherit; text-decoration: none; }
    .topbar { background: rgba(15,23,42,0.97); border-bottom: 1px solid rgba(255,255,255,0.07); padding: 14px 0; position: sticky; top: 0; z-index: 100; }
    .topbar .inner { max-width: 900px; margin: 0 auto; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
    .topbar a { font-size: 0.85rem; color: #94a3b8; font-weight: 600; transition: color 0.2s; }
    .hero { padding: 64px 24px 48px; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.07); }
    .tag { display: inline-block; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 999px; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 1px; }
    .hero h1 { font-size: 2.4rem; font-weight: 900; color: #f1f5f9; margin-bottom: 12px; line-height: 1.2; }
    .hero .ref { font-size: 0.88rem; color: #64748b; margin-bottom: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .hero blockquote { font-style: italic; color: #cbd5e1; font-size: 1rem; padding-left: 20px; max-width: 600px; margin: 0 auto; text-align: left; }
    .wrap { max-width: 900px; margin: 0 auto; padding: 40px 24px 80px; }
    .section-block { margin-bottom: 40px; }
    .section-block h2 { font-size: 1.3rem; font-weight: 800; color: #f1f5f9; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.07); }
    .section-block p { color: #94a3b8; font-size: 0.95rem; line-height: 1.85; margin-bottom: 16px; }
    .bloco { border-left-width: 3px; border-left-style: solid; border-radius: 0 12px 12px 0; padding: 18px 20px; margin-bottom: 16px; background: rgba(255,255,255,0.02); border-top: 1px solid rgba(255,255,255,0.07); border-right: 1px solid rgba(255,255,255,0.07); border-bottom: 1px solid rgba(255,255,255,0.07); }
    .bloco-titulo { font-size: 0.85rem; font-weight: 800; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
    .bloco-texto { color: #94a3b8; font-size: 0.92rem; line-height: 1.82; }
    table { width: 100%; border-collapse: collapse; font-size: 0.87rem; margin: 20px 0 32px; }
    td { padding: 10px 14px; border-bottom: 1px solid rgba(255,255,255,0.05); color: #cbd5e1; }
    tr:hover td { background: rgba(255,255,255,0.02); }
    .nav-mod { display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.07); }
    .reflexao { border-radius: 12px; padding: 22px 26px; margin-top: 32px; }
    .reflexao h3 { color: #22c55e; font-size: 0.95rem; font-weight: 800; margin-bottom: 10px; }
    .reflexao p { color: #94a3b8; font-size: 0.9rem; line-height: 1.8; margin-bottom: 10px; }
    .reflexao p:last-child { margin-bottom: 0; }
    .personagem-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px; margin: 20px 0 32px; }
    .pers-card { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; padding: 18px 16px; }
    .pers-nome { font-size: 1rem; font-weight: 800; margin-bottom: 4px; }
    .pers-datas { font-size: 0.75rem; color: #64748b; margin-bottom: 8px; font-weight: 600; }
    .pers-desc { font-size: 0.85rem; color: #94a3b8; line-height: 1.65; }
    .dado-destaque { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 16px 20px; margin-bottom: 14px; display: flex; gap: 16px; align-items: flex-start; }
    .dado-num { font-size: 1.6rem; font-weight: 900; min-width: 60px; }
    .dado-info { font-size: 0.88rem; color: #94a3b8; line-height: 1.7; }
    .dado-label { font-size: 0.75rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }
"""


def modulo(pasta, cor, hero_bg, titulo, subtitulo, ref, citacao, autor_citacao, conteudo_html, nav_prev, nav_prev_label, nav_next, nav_next_label):
    css_cor = f"""
    .topbar a:hover {{ color: {cor}; }}
    .hero {{ background: linear-gradient(135deg, #0f172a 0%, {hero_bg} 50%, #0f172a 100%); }}
    .tag {{ background: rgba(0,0,0,0.2); border: 1px solid {cor}40; color: {cor}; }}
    .hero blockquote {{ border-left: 3px solid {cor}; }}
    .bloco {{ border-left-color: {cor}; }}
    .bloco-titulo {{ color: {cor}; }}
    table th {{ background: {cor}18; color: {cor}; border-bottom: 1px solid {cor}30; }}
    .nav-mod a {{ background: {cor}18; border: 1px solid {cor}30; color: {cor}; }}
    .nav-mod a:hover {{ background: {cor}30; }}
    .reflexao {{ background: rgba(34,197,94,0.05); border: 1px solid rgba(34,197,94,0.15); }}
    .pers-nome {{ color: {cor}; }}
    .dado-num {{ color: {cor}; }}
    .dado-label {{ color: {cor}; }}
    """
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titulo} | Bloco 11 — 365 de Graça & Adoração</title>
  <link rel="icon" href="/favicon.ico">
  <style>{CSS_BASE}{css_cor}</style>
</head>
<body>
  <div class="topbar"><div class="inner">
    <a href="/11-conflitos-contemporaneos/index.html">← Bloco 11</a>
    <a href="/">365 de Graça & Adoração</a>
  </div></div>
  <div class="hero">
    <span class="tag">{subtitulo}</span>
    <h1>{titulo}</h1>
    <div class="ref">{ref}</div>
    <blockquote>{citacao}<br><small style="color:#64748b;font-size:0.8rem;font-style:normal;">— {autor_citacao}</small></blockquote>
  </div>
  <div class="wrap">
    {conteudo_html}
    <div class="nav-mod">
      <a href="{nav_prev}">{nav_prev_label}</a>
      <a href="/11-conflitos-contemporaneos/index.html">📋 Índice</a>
      <a href="{nav_next}">{nav_next_label}</a>
    </div>
  </div>
</body>
</html>"""


# ================================================================
# MÓDULO: REFORMA PROTESTANTE
# ================================================================
reforma_html = """
<div class="section-block">
  <h2>📜 O Que Foi a Reforma Protestante?</h2>
  <p>A Reforma Protestante foi o movimento de renovação religiosa que, iniciado por Martinho Lutero em 1517, resultou na fragmentação do Ocidente cristão e no surgimento das tradições protestantes. O estopim foi a publicação das 95 Teses de Lutero em 31 de outubro de 1517 — uma lista de proposições para debate acadêmico sobre as indulgências, afixada (segundo a tradição) na porta da Igreja do Castelo de Wittenberg. O que Lutero pretendia como um debate interno da Igreja tornou-se, graças à imprensa de Gutenberg, um incêndio que se alastrou pela Europa.</p>
  <p>A Reforma não foi apenas um evento religioso — foi uma revolução cultural, política e social que transformou a Europa Ocidental e, por extensão, o mundo moderno. Ela contribuiu para o surgimento do individualismo moderno (a consciência individual como árbitro da fé), para o desenvolvimento da educação pública (Lutero defendia escolas para todos), para a formação dos Estados nacionais (a Reforma enfraqueceu a autoridade supranacional do Papado) e para o nascimento do capitalismo (a ética protestante do trabalho, segundo Max Weber).</p>
</div>

<div class="section-block">
  <h2>🔥 As Causas da Reforma</h2>
  <div class="bloco">
    <div class="bloco-titulo">1. A Corrupção da Igreja Medieval</div>
    <div class="bloco-texto">A Igreja do século XVI estava profundamente corrompida. O comércio de indulgências — documentos que prometiam redução do tempo no purgatório em troca de dinheiro — havia se tornado um negócio lucrativo. O Papa Leão X usava as receitas das indulgências para financiar a construção da Basílica de São Pedro em Roma. O dominicano João Tetzel pregava na Alemanha com o slogan "Assim que a moeda no cofre soa, a alma do purgatório logo voa." Para Lutero, este comércio era uma perversão do Evangelho da graça. Além das indulgências, o clero era frequentemente ignorante, imoral e absenteísta. Bispos acumulavam múltiplos bispados sem nunca visitar suas dioceses. O nepotismo e a simonia (compra e venda de cargos eclesiásticos) eram práticas comuns.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">2. A Redescoberta do Evangelho da Graça</div>
    <div class="bloco-texto">A causa teológica central da Reforma foi a redescoberta da doutrina paulina da justificação pela fé. Lutero, ao estudar a Epístola aos Romanos, chegou à convicção de que "o justo viverá pela fé" (Rm 1:17) significava que a salvação era recebida pela fé, não conquistada pelas obras. Esta descoberta — que ele chamou de "torre de experiência" (<em>Turmerlebnis</em>) — foi para ele uma libertação pessoal e o fundamento de toda a Reforma. As quatro <em>solae</em> da Reforma sintetizam esta redescoberta: <em>Sola Scriptura</em> (somente a Escritura), <em>Sola Fide</em> (somente a fé), <em>Sola Gratia</em> (somente a graça), <em>Solus Christus</em> (somente Cristo), <em>Soli Deo Gloria</em> (somente a Deus a glória).</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">3. O Humanismo Renascentista e a Imprensa</div>
    <div class="bloco-texto">O humanismo renascentista, com seu retorno às fontes (<em>ad fontes</em>), preparou o terreno para a Reforma ao promover o estudo dos textos originais em grego e hebraico. Erasmo de Roterdã publicou o Novo Testamento grego em 1516 — um ano antes das 95 Teses — revelando discrepâncias entre o texto original e a Vulgata latina. A imprensa de Gutenberg (c. 1450) foi o acelerador da Reforma: as 95 Teses de Lutero foram traduzidas para o alemão e distribuídas por toda a Alemanha em poucas semanas. Sem a imprensa, a Reforma provavelmente teria sido sufocada como tantos movimentos anteriores de reforma.</div>
  </div>
</div>

<div class="section-block">
  <h2>👤 Os Reformadores Principais</h2>
  <div class="personagem-grid">
    <div class="pers-card">
      <div class="pers-nome">Martinho Lutero</div>
      <div class="pers-datas">1483–1546 · Wittenberg, Alemanha</div>
      <div class="pers-desc">Monge agostiniano e professor de teologia. Autor das 95 Teses (1517), da tradução alemã da Bíblia (1534) e do Catecismo Menor. Fundador do Luteranismo. Sua doutrina central: justificação pela fé somente.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">João Calvino</div>
      <div class="pers-datas">1509–1564 · Genebra, Suíça</div>
      <div class="pers-desc">Teólogo e reformador francês. Autor das <em>Institutas da Religião Cristã</em> (1536). Fundador do Calvinismo/Presbiterianismo. Sua contribuição: a soberania de Deus, a predestinação e a teocracia de Genebra.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Ulrico Zuínglio</div>
      <div class="pers-datas">1484–1531 · Zurique, Suíça</div>
      <div class="pers-desc">Reformador suíço. Discordou de Lutero sobre a Ceia do Senhor (Colóquio de Marburg, 1529): para Zuínglio, a Ceia é memorial simbólico; para Lutero, há presença real de Cristo. Esta divisão marcou o protestantismo.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Henrique VIII</div>
      <div class="pers-datas">1491–1547 · Inglaterra</div>
      <div class="pers-desc">Rei da Inglaterra que se separou de Roma por razões políticas (anulação de casamento) e criou a Igreja Anglicana (1534). A Reforma inglesa foi inicialmente política, não teológica, mas depois adquiriu conteúdo reformado.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">João Knox</div>
      <div class="pers-datas">1514–1572 · Escócia</div>
      <div class="pers-desc">Reformador escocês, discípulo de Calvino. Fundou a Igreja Presbiteriana da Escócia. Sua pregação apaixonada transformou a Escócia em um dos países mais profundamente reformados da Europa.</div>
    </div>
    <div class="pers-card">
      <div class="pers-nome">Erasmo de Roterdã</div>
      <div class="pers-datas">1466–1536 · Países Baixos</div>
      <div class="pers-desc">Humanista católico que criticou os abusos da Igreja mas recusou a ruptura com Roma. Seu debate com Lutero sobre o livre-arbítrio (1524-25) revelou a diferença fundamental entre o humanismo e a Reforma.</div>
    </div>
  </div>
</div>

<div class="section-block">
  <h2>⚖️ As Quatro <em>Solae</em> da Reforma</h2>
  <div class="bloco">
    <div class="bloco-titulo">Sola Scriptura — Somente a Escritura</div>
    <div class="bloco-texto">A Escritura é a autoridade suprema e suficiente para a fé e a prática cristã. A tradição da Igreja tem valor, mas deve ser submetida ao julgamento da Escritura — não o contrário. Esta doutrina foi o fundamento da crítica de Lutero às indulgências e ao papado: ele desafiou o Papa e os Concílios a refutá-lo com a Escritura. A <em>Sola Scriptura</em> não significa que a Escritura é a única autoridade (isso seria <em>nuda Scriptura</em>), mas que é a autoridade suprema à qual todas as outras autoridades devem se submeter.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">Sola Fide — Somente a Fé</div>
    <div class="bloco-texto">A justificação — a declaração de Deus de que o pecador é justo — é recebida pela fé somente, não pelas obras. Esta foi a descoberta central de Lutero em Romanos 1:17 e o coração da Reforma. A fé que justifica não é mero assentimento intelectual, mas confiança pessoal em Cristo. As obras não contribuem para a justificação, mas são o fruto inevitável da fé genuína. Lutero disse: "Somos salvos pela fé somente, mas a fé que salva nunca está sozinha."</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">Sola Gratia — Somente a Graça</div>
    <div class="bloco-texto">A salvação é inteiramente dom de Deus — não mérito humano. A graça não é apenas o auxílio que Deus oferece ao livre-arbítrio humano (posição semi-pelagiana), mas a iniciativa soberana de Deus que cria a fé no coração do pecador. Esta doutrina foi o fundamento do debate entre Lutero e Erasmo sobre o livre-arbítrio: Lutero argumentou que o livre-arbítrio humano está escravizado pelo pecado e incapaz de se voltar para Deus sem a graça irresistível.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">Solus Christus — Somente Cristo</div>
    <div class="bloco-texto">Cristo é o único mediador entre Deus e os homens (1 Tm 2:5). A salvação é encontrada somente nele — não nos santos, não na Virgem Maria, não nos sacramentos como meios automáticos de graça, não no Papa. A Reforma rejeitou a mediação sacerdotal e sacramental como necessária para a salvação, afirmando o sacerdócio universal de todos os crentes (1 Pe 2:9): todo cristão tem acesso direto a Deus através de Cristo.</div>
  </div>
</div>

<div class="section-block">
  <h2>🔄 A Reforma Católica (Contrarreforma)</h2>
  <p>A resposta da Igreja Católica à Reforma foi dupla: reforma interna genuína e reafirmação doutrinária. O Concílio de Trento (1545-1563) foi o instrumento principal desta resposta. Trento reafirmou as doutrinas contestadas pelos protestantes (justificação pelas obras e pela fé, os sete sacramentos, o purgatório, a autoridade da tradição ao lado da Escritura), mas também promoveu reformas disciplinares significativas: fim do comércio de indulgências, melhoria da formação do clero, criação de seminários, combate ao nepotismo e à simonia.</p>
  <p>A Companhia de Jesus (Jesuítas), fundada por Inácio de Loyola em 1540, foi o instrumento mais eficaz da Reforma Católica. Os jesuítas combinavam rigor intelectual, espiritualidade profunda e dedicação missionária para reconquistar territórios perdidos para o protestantismo e evangelizar as Américas, a África e a Ásia.</p>

  <div class="reflexao">
    <h3>🙏 Reflexão: Legado e Desafio da Reforma</h3>
    <p>A Reforma Protestante foi um dos eventos mais importantes da história do Ocidente — e um dos mais ambíguos. Ela restaurou o Evangelho da graça que havia sido obscurecido pela tradição medieval; mas também fragmentou a Igreja em centenas de denominações, contribuiu para as Guerras de Religião que devastaram a Europa, e gerou um individualismo que pode tornar-se sectarismo.</p>
    <p>Em 2017, no quinto centenário da Reforma, o Papa Francisco e representantes luteranos assinaram uma declaração conjunta reconhecendo que "o que nos une é maior do que o que nos divide." Esta afirmação é verdadeira — mas as divisões são reais e não devem ser minimizadas. O caminho para a unidade passa pela honestidade sobre as diferenças e pela disposição de aprender uns com os outros.</p>
  </div>
</div>
"""

# ================================================================
# MÓDULO: GUERRAS DE RELIGIÃO
# ================================================================
guerras_html = """
<div class="section-block">
  <h2>⚔️ Quando a Fé se Tornou Justificativa para a Violência</h2>
  <p>As Guerras de Religião dos séculos XVI e XVII representam um dos capítulos mais sombrios da história cristã — o período em que cristãos mataram cristãos em nome de Cristo. Estas guerras não foram simplesmente conflitos religiosos: foram conflitos políticos, sociais e econômicos nos quais a religião serviu como identidade tribal, justificativa ideológica e mobilizador de massas. Mas o fato de que a religião foi instrumentalizada para fins políticos não elimina a responsabilidade da Igreja — ela deveria ter sido a voz da paz, não o estandarte da guerra.</p>
  <p>O contexto histórico é crucial: a Reforma Protestante fragmentou a cristandade ocidental em um momento em que a religião era inseparável da identidade política. Ser católico ou protestante não era apenas uma questão de crença pessoal — era uma questão de lealdade política, de pertencimento social, de identidade nacional. Quando príncipes abraçavam o protestantismo, suas populações eram forçadas a converter-se ou a emigrar (o princípio <em>cuius regio, eius religio</em> — "de quem é o território, é a religião"). Esta fusão de religião e política tornou os conflitos religiosos inevitavelmente violentos.</p>
</div>

<div class="section-block">
  <h2>🩸 Os Principais Conflitos</h2>
  <div class="bloco">
    <div class="bloco-titulo">As Guerras Huguenotes (1562–1598) — França</div>
    <div class="bloco-texto">Oito guerras civis religiosas entre católicos e protestantes (huguenotes) na França. O conflito mais famoso foi a Noite de São Bartolomeu (23-24 de agosto de 1572): o massacre de protestantes em Paris e nas províncias, ordenado pela rainha-mãe Catarina de Médici e pelo rei Carlos IX. As estimativas de mortos variam de 5.000 a 30.000. O Papa Gregório XIII celebrou o massacre com um <em>Te Deum</em> e mandou cunhar uma medalha comemorativa — um dos momentos mais vergonhosos da história papal. As guerras terminaram com o Édito de Nantes (1598), que garantiu liberdade religiosa aos huguenotes — revogado por Luís XIV em 1685, provocando a emigração de 200.000 protestantes.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">A Guerra dos Trinta Anos (1618–1648) — Europa Central</div>
    <div class="bloco-texto">O maior conflito religioso da história europeia, que devastou o Sacro Império Romano-Germânico. Começou como conflito entre príncipes católicos e protestantes na Boêmia (a Defenestração de Praga, 1618) e tornou-se uma guerra europeia envolvendo a Suécia, a França, a Espanha, os Países Baixos e o Império. Estima-se que a população da Alemanha diminuiu em 25-40% durante a guerra — por combates, fome e doenças. A Paz de Vestfália (1648) encerrou a guerra e estabeleceu o princípio da soberania estatal e da tolerância religiosa — o fundamento do sistema internacional moderno. Paradoxalmente, a guerra mais devastadora da Europa foi encerrada por um tratado que separou religião e política.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">As Guerras dos Países Baixos (1568–1648) — Espanha vs. Holanda</div>
    <div class="bloco-texto">A revolta das Províncias Unidas (Holanda) contra o domínio espanhol foi simultaneamente uma guerra de independência nacional e uma guerra religiosa — os holandeses eram majoritariamente calvinistas, os espanhóis eram católicos. O Duque de Alba, governador espanhol, estabeleceu o "Tribunal de Sangue" que executou milhares de protestantes. A guerra terminou com o reconhecimento da independência holandesa na Paz de Vestfália. A Holanda tornou-se o país mais tolerante religiosamente da Europa — um refúgio para judeus, huguenotes e outras minorias religiosas.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">As Guerras dos Três Reinos (1639–1651) — Ilhas Britânicas</div>
    <div class="bloco-texto">Uma série de conflitos interligados na Inglaterra, Escócia e Irlanda que combinaram guerra civil, conflito religioso e revolução política. A Guerra Civil Inglesa (1642-51) opôs os Cavaleiros (realistas, anglicanos) aos Cabeças Redondas (parlamentaristas, puritanos). O rei Carlos I foi executado em 1649 — o primeiro monarca europeu a ser julgado e executado por seus próprios súditos. Oliver Cromwell estabeleceu o Commonwealth puritano (1649-60). Na Irlanda, o massacre de Drogheda (1649) por Cromwell resultou na morte de milhares de católicos e permanece uma ferida histórica na memória irlandesa.</div>
  </div>
</div>

<div class="section-block">
  <h2>📊 O Custo Humano das Guerras de Religião</h2>
  <div class="dado-destaque">
    <div class="dado-num">8M</div>
    <div class="dado-info"><div class="dado-label">Mortos na Guerra dos Trinta Anos</div>Estimativa de mortos diretos e indiretos (combates, fome, doenças) no conflito mais devastador da Europa pré-moderna.</div>
  </div>
  <div class="dado-destaque">
    <div class="dado-num">30.000</div>
    <div class="dado-info"><div class="dado-label">Mortos na Noite de São Bartolomeu</div>Estimativa máxima de protestantes massacrados em Paris e nas províncias em agosto de 1572.</div>
  </div>
  <div class="dado-destaque">
    <div class="dado-num">200.000</div>
    <div class="dado-info"><div class="dado-label">Huguenotes exilados</div>Protestantes franceses que emigraram após a revogação do Édito de Nantes em 1685, enriquecendo a Prússia, a Holanda e a Inglaterra com seu capital e habilidades.</div>
  </div>
  <div class="dado-destaque">
    <div class="dado-num">40%</div>
    <div class="dado-info"><div class="dado-label">Redução populacional na Alemanha</div>Estimativa da redução da população em algumas regiões alemãs durante a Guerra dos Trinta Anos — o maior desastre demográfico da Alemanha antes do século XX.</div>
  </div>
</div>

<div class="section-block">
  <h2>🏛️ Consequências: O Nascimento da Tolerância Religiosa</h2>
  <p>Paradoxalmente, as Guerras de Religião produziram a tolerância religiosa. Após décadas de violência em nome de Deus, pensadores como John Locke (<em>Carta sobre a Tolerância</em>, 1689) argumentaram que o Estado não tem autoridade sobre a consciência religiosa dos cidadãos — que a religião é uma questão entre o indivíduo e Deus, não entre o indivíduo e o Estado. Esta ideia, radicalmente nova no século XVII, tornou-se o fundamento das democracias liberais modernas.</p>
  <p>A Paz de Vestfália (1648) estabeleceu o princípio da soberania estatal — os Estados têm o direito de governar seus territórios sem interferência externa, incluindo interferência religiosa. Este princípio separou religião e política de uma forma que os reformadores do século XVI nunca haviam imaginado. O custo foi enorme: a secularização da política europeia, que eventualmente levaria ao ateísmo de Estado da Revolução Francesa e ao totalitarismo do século XX.</p>

  <div class="reflexao">
    <h3>🙏 Reflexão: Violência em Nome de Cristo</h3>
    <p>As Guerras de Religião são um lembrete permanente de que a religião pode ser instrumentalizada para fins de violência e dominação. Quando a fé se torna identidade tribal — "nós" contra "eles" — ela perde sua capacidade de transformar e passa a legitimar a destruição. Jesus disse "amai vossos inimigos" (Mt 5:44) — mas os cristãos das Guerras de Religião matavam seus irmãos em Cristo.</p>
    <p>A lição não é que a religião é intrinsecamente violenta — é que a religião, como qualquer força humana poderosa, pode ser corrompida e instrumentalizada. A resposta não é a secularização que elimina a religião da esfera pública, mas a formação de cristãos que internalizaram o Evangelho da paz e da reconciliação profundamente o suficiente para resistir à tentação da violência religiosa.</p>
  </div>
</div>
"""

# ================================================================
# MÓDULO: SECULARISMO
# ================================================================
seculo_html = """
<div class="section-block">
  <h2>🏛️ O Que é o Secularismo?</h2>
  <p>O secularismo é, em sua forma mais básica, a separação entre religião e Estado — a ideia de que o governo civil não deve ser governado por princípios religiosos e que as instituições religiosas não devem exercer poder político. Em sua forma mais ampla, é uma visão de mundo que afirma que a realidade pode ser adequadamente compreendida e gerida sem referência ao sobrenatural ou ao divino.</p>
  <p>É fundamental distinguir entre o secularismo como arranjo político (a laicidade do Estado) e o secularismo como ideologia (a afirmação de que a religião é falsa, irrelevante ou prejudicial). O primeiro é compatível com uma sociedade profundamente religiosa — os Estados Unidos são um exemplo de Estado laico com alta religiosidade popular. O segundo é uma posição filosófica que compete com a fé religiosa. Muitos cristãos apoiam a laicidade do Estado enquanto rejeitam o secularismo como ideologia.</p>
</div>

<div class="section-block">
  <h2>📅 As Raízes Históricas do Secularismo</h2>
  <div class="bloco">
    <div class="bloco-titulo">O Iluminismo (Séc. XVII–XVIII)</div>
    <div class="bloco-texto">O Iluminismo europeu foi o movimento intelectual que colocou a razão humana no centro do conhecimento e da organização social, deslocando a revelação divina e a autoridade eclesiástica. Filósofos como Descartes, Locke, Voltaire, Rousseau e Kant argumentaram que a razão humana é suficiente para descobrir a verdade moral e organizar a sociedade justa. A religião, para muitos iluministas, era superstição, fanatismo e obstáculo ao progresso. Para outros (os deístas), era uma crença em um Deus criador que não intervém na história — um "relojoeiro cósmico" que criou o universo e o deixou funcionar por suas próprias leis.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">A Revolução Francesa (1789)</div>
    <div class="bloco-texto">A Revolução Francesa foi o momento em que o secularismo passou da teoria à prática política. A Igreja Católica, aliada ao Antigo Regime, foi atacada como instituição de opressão: igrejas foram fechadas ou transformadas em "Templos da Razão", sacerdotes foram executados ou forçados a abjurar, o calendário cristão foi substituído por um calendário republicano. O princípio da laicidade (<em>laïcité</em>) — a separação estrita entre Estado e religião — tornou-se um dos valores fundamentais da República Francesa e foi inscrito na Constituição em 1905. A <em>laïcité</em> francesa é mais radical do que a separação Igreja-Estado americana: ela exclui a religião não apenas do governo, mas do espaço público.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">O Marxismo e o Ateísmo de Estado (Séc. XIX–XX)</div>
    <div class="bloco-texto">Karl Marx chamou a religião de "ópio do povo" — um anestésico que impede os oprimidos de reconhecer e combater sua opressão. Para o marxismo, a religião é uma superestrutura ideológica que reflete e legitima as relações de produção capitalistas. Os regimes marxistas do século XX — a União Soviética, a China de Mao, Cuba, a Coreia do Norte — implementaram o ateísmo de Estado: a perseguição sistemática das religiões como obstáculos à construção do socialismo. Estima-se que mais cristãos foram mortos por perseguição no século XX do que em todos os séculos anteriores combinados.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">A Secularização Contemporânea</div>
    <div class="bloco-texto">O sociólogo Peter Berger, que havia previsto a secularização inevitável do mundo moderno, reconheceu no final do século XX que estava errado: o mundo moderno é "furiosamente religioso." O que ocorreu foi uma dessecularização em muitas partes do mundo (crescimento do Islã, do Pentecostalismo na América Latina e África, do Hinduísmo político na Índia) e uma secularização acelerada na Europa Ocidental. O "Ocidente Global" — Europa Ocidental, Canadá, Austrália, Nova Zelândia — é a exceção, não a regra, no panorama religioso mundial.</div>
  </div>
</div>

<div class="section-block">
  <h2>⚖️ Fé e Esfera Pública — O Debate Contemporâneo</h2>
  <p>O debate sobre o papel da religião na esfera pública é um dos mais importantes da democracia contemporânea. Há duas posições extremas: (1) o secularismo estrito, que exige que os cidadãos deixem suas convicções religiosas fora do debate público e usem apenas argumentos "neutros" e racionais; e (2) o teocracionismo, que busca impor a lei religiosa como lei civil. Entre estes extremos, há um espectro de posições que reconhecem tanto a legitimidade da voz religiosa no debate público quanto os limites da imposição religiosa em uma sociedade pluralista.</p>
  <p>O filósofo Jürgen Habermas, um dos mais importantes defensores do secularismo, reconheceu que as tradições religiosas carregam "potenciais semânticos" — recursos morais e espirituais — que a razão secular não pode substituir. Ele argumenta que uma democracia saudável precisa da contribuição das tradições religiosas, desde que elas traduzam suas convicções em linguagem acessível a todos os cidadãos. Esta posição — o "secularismo pós-secular" — é uma abertura significativa ao diálogo entre fé e razão.</p>

  <div class="reflexao">
    <h3>🙏 Reflexão: Fé no Mundo Secular</h3>
    <p>O desafio do secularismo para a Igreja não é primariamente político — é espiritual. A questão não é apenas "como a Igreja deve se relacionar com o Estado secular?", mas "como os cristãos podem viver uma fé autêntica em uma cultura que trata a religião como irrelevante ou privada?" A resposta não é a nostalgia de uma cristandade que não existe mais, nem a capitulação ao secularismo que dissolve a fé em valores culturais. É a construção de comunidades de discipulado que demonstrem, pela qualidade de sua vida comum, que o Evangelho é a boa notícia que o mundo secular precisa ouvir.</p>
    <p>O apóstolo Pedro escreveu a cristãos que viviam como "estrangeiros e peregrinos" em uma cultura hostil (1 Pe 2:11). Esta é a condição permanente da Igreja — não apenas no mundo secular moderno, mas em qualquer cultura que não seja o Reino de Deus. A resposta de Pedro não é o isolamento nem a capitulação, mas o testemunho: "mantendo boa conduta entre os gentios, para que, naquilo em que falam contra vós como malfeitores, observando as vossas boas obras, glorifiquem a Deus no dia da visitação" (1 Pe 2:12).</p>
  </div>
</div>
"""

# ================================================================
# MÓDULO: ECUMENISMO
# ================================================================
ecum_html = """
<div class="section-block">
  <h2>🕊️ O Que é o Ecumenismo?</h2>
  <p>O ecumenismo é o movimento que busca a unidade visível dos cristãos divididos — a superação das divisões denominacionais em direção à unidade que Cristo orou em João 17:21. A palavra vem do grego <em>oikoumenē</em> — "o mundo habitado" — e reflete a visão de uma Igreja que abrange toda a humanidade. O ecumenismo moderno nasceu no início do século XX, impulsionado pela percepção de que a divisão da Igreja era um obstáculo à missão cristã: como o mundo poderia crer que Cristo é o Senhor se seus seguidores não conseguiam viver em unidade?</p>
  <p>É importante distinguir entre diferentes formas de ecumenismo: (1) o ecumenismo espiritual — a oração conjunta e a busca de uma espiritualidade comum; (2) o ecumenismo prático — a cooperação em projetos de serviço social, defesa dos direitos humanos e missão; (3) o ecumenismo teológico — o diálogo sobre as diferenças doutrinárias com o objetivo de superá-las; e (4) o ecumenismo institucional — a busca de formas de unidade organizacional. Cada forma tem seus defensores e críticos, e cada uma enfrenta desafios específicos.</p>
</div>

<div class="section-block">
  <h2>📅 História do Movimento Ecumênico</h2>
  <div class="bloco">
    <div class="bloco-titulo">A Conferência de Edimburgo (1910) — O Nascimento</div>
    <div class="bloco-texto">A Conferência Missionária Mundial de Edimburgo (1910) é considerada o marco fundador do ecumenismo moderno. Reuniu 1.200 delegados de sociedades missionárias protestantes de todo o mundo. O missionário John Mott, presidente da conferência, proclamou o objetivo de "evangelizar o mundo nesta geração." A conferência revelou que a divisão denominacional era um obstáculo à missão: os missionários nas "terras pagãs" percebiam que exportar as divisões europeias para a África e a Ásia era contraproducente. O movimento ecumênico nasceu da missão.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">O Conselho Mundial de Igrejas (1948)</div>
    <div class="bloco-texto">O Conselho Mundial de Igrejas (CMI) foi fundado em Amsterdã em 1948, reunindo 147 igrejas de 44 países. Hoje conta com mais de 350 igrejas membros, representando mais de 580 milhões de cristãos em 110 países. O CMI inclui igrejas protestantes, anglicanas e ortodoxas — mas não a Igreja Católica Romana (que participa como observadora). O CMI tem sido ativo em questões de paz, justiça e direitos humanos, mas tem sido criticado por alguns por priorizar o engajamento social em detrimento da unidade teológica.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">O Concílio Vaticano II (1962–1965)</div>
    <div class="bloco-texto">O Concílio Vaticano II foi o evento mais importante da história católica do século XX e um marco para o ecumenismo. O decreto <em>Unitatis Redintegratio</em> (1964) reconheceu que as comunidades cristãs separadas de Roma "não estão de modo algum desprovidas de significado e de importância no mistério da salvação" — uma mudança radical em relação à posição anterior de que fora da Igreja Católica não há salvação. O Vaticano II abriu o caminho para o diálogo teológico oficial entre a Igreja Católica e as igrejas protestantes e ortodoxas.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">A Declaração Conjunta sobre a Justificação (1999)</div>
    <div class="bloco-texto">Em 31 de outubro de 1999 — aniversário das 95 Teses de Lutero — a Igreja Católica Romana e a Federação Luterana Mundial assinaram a Declaração Conjunta sobre a Doutrina da Justificação. O documento afirma um consenso básico sobre a justificação: "pela graça somente, pela fé na obra salvífica de Cristo, e não por mérito nosso, somos aceitos por Deus e recebemos o Espírito Santo." As condenações mútuas do século XVI sobre a justificação foram declaradas inaplicáveis às posições atuais das duas igrejas. Este foi o maior avanço ecumênico do século XX.</div>
  </div>
</div>

<div class="section-block">
  <h2>⚖️ Limites e Críticas do Ecumenismo</h2>
  <p>O ecumenismo enfrenta críticas de dois lados opostos. Da direita teológica, é criticado por diluir as diferenças doutrinárias em nome de uma unidade superficial — o chamado "ecumenismo de falsa paz" que ignora questões teológicas genuínas. Da esquerda teológica, é criticado por ser lento demais e por priorizar o consenso institucional em detrimento da unidade espiritual que já existe entre os crentes.</p>
  <p>As questões que permanecem sem resolução são significativas: a autoridade papal (para os católicos e ortodoxos), a ordenação de mulheres (que divide protestantes de católicos e ortodoxos), a ética sexual (que divide igrejas liberais de igrejas conservadoras), e a natureza dos sacramentos (especialmente a Eucaristia). Estas não são questões secundárias — elas tocam na identidade mais profunda de cada tradição.</p>

  <div class="reflexao">
    <h3>🙏 Reflexão: A Unidade que Cristo Quer</h3>
    <p>A oração de Jesus em João 17 — "para que todos sejam um, como tu, ó Pai, és em mim, e eu em ti" — é o fundamento e o critério do ecumenismo. A unidade que Cristo quer não é uma unidade organizacional que apaga as diferenças, nem uma unidade espiritual que ignora as divisões institucionais. É uma unidade que reflete a unidade trinitária — uma unidade na diversidade, onde a diferença não é obstáculo à comunhão, mas expressão da riqueza do único corpo de Cristo.</p>
    <p>O ecumenismo autêntico começa com a oração — a oração conjunta de cristãos de diferentes tradições que reconhecem que pertencem ao mesmo Senhor. Ele avança através do diálogo honesto — a disposição de ouvir as razões do outro e de reconhecer os próprios erros. E ele se concretiza na cooperação prática — o trabalho conjunto em favor dos pobres, dos perseguidos e dos marginalizados, que demonstra que a unidade em Cristo é mais forte do que as divisões históricas.</p>
  </div>
</div>
"""

# ================================================================
# MÓDULO: PERSEGUIÇÃO ATUAL
# ================================================================
perseg_html = """
<div class="section-block">
  <h2>🔥 A Perseguição Cristã no Século XXI</h2>
  <p>A perseguição de cristãos não é apenas um fenômeno histórico — é uma realidade presente que afeta centenas de milhões de pessoas em todo o mundo. Segundo o relatório anual da organização Open Doors, em 2024 aproximadamente 365 milhões de cristãos vivem em países onde enfrentam alto nível de perseguição — 1 em cada 7 cristãos no mundo. A perseguição assume formas variadas: desde a discriminação social e econômica até o encarceramento, a tortura e o martírio.</p>
  <p>É importante distinguir entre diferentes formas de perseguição: (1) perseguição estatal — governos que proíbem ou restringem a prática cristã (Coreia do Norte, China, Eritreia); (2) perseguição por grupos extremistas — organizações como o Estado Islâmico, o Boko Haram e o Al-Shabaab que atacam comunidades cristãs; (3) perseguição social — discriminação e violência por parte de famílias, comunidades e grupos religiosos majoritários; e (4) perseguição cultural — pressão para abandonar a fé cristã em contextos onde a identidade religiosa é inseparável da identidade étnica ou nacional.</p>
</div>

<div class="section-block">
  <h2>📊 Os Dados da Perseguição</h2>
  <div class="dado-destaque">
    <div class="dado-num">365M</div>
    <div class="dado-info"><div class="dado-label">Cristãos Perseguidos</div>Número estimado de cristãos que vivem em países com alto nível de perseguição em 2024, segundo o relatório da Open Doors.</div>
  </div>
  <div class="dado-destaque">
    <div class="dado-num">4.998</div>
    <div class="dado-info"><div class="dado-label">Mortos por sua Fé (2023)</div>Cristãos mortos por causa de sua fé em 2023, segundo a Open Doors. A maioria na África Subsaariana (Nigéria, Etiópia, Moçambique).</div>
  </div>
  <div class="dado-destaque">
    <div class="dado-num">14.766</div>
    <div class="dado-info"><div class="dado-label">Igrejas Atacadas (2023)</div>Igrejas e outros edifícios cristãos atacados, fechados ou destruídos em 2023.</div>
  </div>
  <div class="dado-destaque">
    <div class="dado-num">3.906</div>
    <div class="dado-info"><div class="dado-label">Presos por sua Fé (2023)</div>Cristãos detidos, presos ou sentenciados em 2023 por causa de sua fé.</div>
  </div>
</div>

<div class="section-block">
  <h2>🌍 Os Países Mais Perigosos para Cristãos</h2>
  <table>
    <tr><th>País</th><th>Tipo de Perseguição</th><th>Situação</th></tr>
    <tr><td>🇰🇵 Coreia do Norte</td><td>Ditadura totalitária ateia</td><td>O país mais perigoso do mundo para cristãos. Praticar o cristianismo pode resultar em execução ou campo de trabalho forçado. Estimam-se 50.000-70.000 cristãos em campos de concentração.</td></tr>
    <tr><td>🇸🇴 Somália</td><td>Extremismo islâmico (Al-Shabaab)</td><td>Converter-se do Islã ao Cristianismo é punível com a morte. A Igreja cristã praticamente não existe publicamente.</td></tr>
    <tr><td>🇾🇪 Iêmen</td><td>Extremismo islâmico, guerra civil</td><td>Cristãos enfrentam perseguição extrema em um país devastado pela guerra civil entre facções islâmicas.</td></tr>
    <tr><td>🇪🇷 Eritreia</td><td>Ditadura, perseguição estatal</td><td>Apenas quatro denominações são legais. Membros de igrejas não registradas são presos e torturados. Milhares de cristãos estão em prisões subterrâneas.</td></tr>
    <tr><td>🇱🇾 Líbia</td><td>Extremismo islâmico, instabilidade</td><td>Após a queda de Gaddafi, grupos islâmicos extremistas perseguem cristãos. Em 2015, o Estado Islâmico executou 21 cristãos coptas egípcios na praia.</td></tr>
    <tr><td>🇳🇬 Nigéria</td><td>Boko Haram, conflitos pastorais</td><td>O país com maior número de cristãos mortos por sua fé. O Boko Haram e os pastores fulani muçulmanos atacam comunidades cristãs no norte e no centro do país.</td></tr>
    <tr><td>🇨🇳 China</td><td>Controle estatal da religião</td><td>Igrejas não registradas são fechadas, pastores são presos, cruzes são removidas de igrejas. A Igreja doméstica (underground) é perseguida, mas cresce.</td></tr>
    <tr><td>🇮🇳 Índia</td><td>Nacionalismo hindu (Hindutva)</td><td>Grupos nacionalistas hindus atacam igrejas e cristãos, especialmente nas conversões. Leis anti-conversão em vários estados.</td></tr>
  </table>
</div>

<div class="section-block">
  <h2>✝️ A Teologia do Martírio</h2>
  <p>O martírio — dar a vida pela fé — é uma realidade que a Igreja enfrenta desde seus primórdios. A palavra "mártir" (<em>martys</em> em grego) significa "testemunha" — o mártir é aquele cujo testemunho de Cristo é tão radical que inclui a disposição de morrer por ele. O Apocalipse apresenta os mártires como heróis da fé que "venceram por causa do sangue do Cordeiro e por causa da palavra do seu testemunho, e não amaram as suas vidas até à morte" (Ap 12:11).</p>
  <p>A teologia do martírio não glorifica a morte — glorifica a fidelidade. O mártir não busca a morte; ele busca a fidelidade a Cristo, e aceita a morte como consequência. Tertuliano, o teólogo norte-africano do século II, afirmou que "o sangue dos mártires é a semente da Igreja" (<em>sanguis martyrum semen Christianorum</em>) — a perseguição não destrói a Igreja, mas a fortalece. Esta afirmação é confirmada pela história: a Igreja cresceu mais rapidamente nos períodos de perseguição do que nos períodos de conforto.</p>

  <div class="reflexao">
    <h3>🙏 Reflexão: Nossa Responsabilidade</h3>
    <p>A perseguição de cristãos em todo o mundo é uma realidade que a Igreja no Ocidente frequentemente ignora. Paulo escreveu: "Se um membro sofre, todos os membros sofrem com ele" (1 Co 12:26). A solidariedade com os cristãos perseguidos não é opcional — é uma obrigação do corpo de Cristo. Esta solidariedade pode tomar formas concretas: oração, doação a organizações de apoio (como Open Doors, Portas Abertas, Vozes Mártires), advocacia política, e acolhimento de refugiados cristãos.</p>
    <p>A perseguição também é um convite à reflexão sobre nossa própria fé. Os cristãos perseguidos que se recusam a negar Cristo diante da ameaça de morte nos perguntam: o que Cristo significa para nós? Estamos dispostos a pagar qualquer preço por nossa fé? A resposta honesta a estas perguntas pode ser o início de um discipulado mais profundo e mais radical.</p>
  </div>
</div>
"""

# ================================================================
# MÓDULO: ISLAMISMO E CRISTANDADE
# ================================================================
islam_html = """
<div class="section-block">
  <h2>🌙 Quatorze Séculos de Encontro</h2>
  <p>O Islamismo e o Cristianismo são as duas maiores religiões do mundo, com 1,9 bilhão e 2,4 bilhões de seguidores respectivamente. Elas compartilham raízes abraâmicas comuns — ambas veneram Abraão, Moisés e os profetas do AT; ambas reconhecem Jesus como profeta (o Islã) ou como Senhor e Salvador (o Cristianismo). Mas suas diferenças são fundamentais: o Islã nega a Trindade, a divindade de Cristo e a crucificação como evento salvífico. Para o Islã, o Alcorão é a revelação final e definitiva de Deus, que corrige as distorções dos textos judaicos e cristãos.</p>
  <p>A história das relações entre o Islamismo e o Cristianismo é uma história de encontro, conflito e coexistência — às vezes simultâneos. Houve séculos de guerra (as Cruzadas, a Reconquista, as conquistas otomanas) e séculos de coexistência pacífica e fecunda (a Espanha muçulmana, o Império Otomano em seus melhores momentos). A relação atual é marcada pela memória histórica de ambos os lados e pelos desafios do fundamentalismo contemporâneo.</p>
</div>

<div class="section-block">
  <h2>📅 Os Momentos Decisivos da Relação</h2>
  <div class="bloco">
    <div class="bloco-titulo">A Expansão Islâmica (632–750 d.C.)</div>
    <div class="bloco-texto">Em um século após a morte de Muhammad (632 d.C.), o Islã havia conquistado a Península Arábica, o Oriente Médio, o Norte da África, a Pérsia e a Península Ibérica. Regiões que haviam sido cristãs por séculos — o Egito, a Síria, a Palestina, o Norte da África — tornaram-se muçulmanas. As antigas igrejas de Alexandria, Antioquia, Cartago e Hipona (onde Agostinho havia sido bispo) foram absorvidas pelo mundo islâmico. Esta expansão não foi apenas militar — foi também missionária: o Islã oferecia uma fé simples, igualitária e sem a complexidade teológica da Trindade, e muitos cristãos converteram-se voluntariamente.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">As Cruzadas (1095–1291)</div>
    <div class="bloco-texto">As Cruzadas foram expedições militares organizadas pelo Papado para recuperar a Terra Santa do controle muçulmano. O Papa Urbano II lançou a Primeira Cruzada em 1095 com o grito de guerra "Deus lo vult!" ("Deus quer!"). A conquista de Jerusalém em 1099 foi acompanhada de um massacre de muçulmanos e judeus que manchou permanentemente a memória cristã no mundo islâmico. As Cruzadas produziram momentos de brutalidade extrema (o Saque de Constantinopla em 1204, o massacre de Acre em 1191) e também momentos de diálogo surpreendente (Francisco de Assis visitou o sultão Al-Kamil em 1219 em busca de paz). As Cruzadas fracassaram militarmente — Jerusalém foi reconquistada por Saladino em 1187 e os cruzados foram expulsos do Oriente Médio em 1291. Mas seu legado de violência em nome de Cristo permanece vivo na memória islâmica.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">A Espanha Muçulmana (711–1492) — Al-Andalus</div>
    <div class="bloco-texto">A Espanha muçulmana (Al-Andalus) foi, em seus melhores momentos, um exemplo de coexistência entre muçulmanos, cristãos e judeus — a chamada <em>convivencia</em>. Córdoba, no século X, era a cidade mais avançada da Europa Ocidental: com 500.000 habitantes, 300 mesquitas, 50 hospitais e uma biblioteca de 400.000 volumes. Filósofos como Averróis (islâmico) e Maimônides (judeu) floresceram neste ambiente de tolerância relativa. A Reconquista cristã (722-1492) foi gradualmente reconquistando a Península Ibérica, culminando com a queda de Granada em 1492 — o mesmo ano em que Colombo chegou às Américas e os judeus foram expulsos da Espanha.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">O Fundamentalismo Islâmico Contemporâneo</div>
    <div class="bloco-texto">O fundamentalismo islâmico contemporâneo — representado por movimentos como os Irmãos Muçulmanos, o Wahabismo saudita, o Talibã e o Estado Islâmico (ISIS) — é um fenômeno do século XX que reage à modernização e à influência ocidental com um retorno a uma interpretação literal e militante do Islã. O Estado Islâmico, em seu apogeu (2014-2019), perseguiu cristãos no Iraque e na Síria com uma brutalidade que evocava as piores perseguições da história: execuções em massa, escravidão de mulheres yazidis, destruição de igrejas e sítios arqueológicos. O resultado foi o quase desaparecimento das comunidades cristãs do Iraque — que haviam existido desde o século I d.C.</div>
  </div>
</div>

<div class="section-block">
  <h2>🤝 O Diálogo Islamo-Cristão</h2>
  <p>Apesar da história de conflitos, há uma tradição significativa de diálogo islamo-cristão. O documento <em>Uma Palavra Comum entre Nós e Vós</em> (2007), assinado por 138 líderes muçulmanos de todo o mundo, propôs como base para o diálogo os dois grandes mandamentos: o amor a Deus e o amor ao próximo. O Papa Francisco e o Grande Imã de Al-Azhar, Ahmad Al-Tayyeb, assinaram em 2019 o <em>Documento sobre a Fraternidade Humana</em> em Abu Dhabi — um apelo conjunto à paz, à coexistência e à rejeição da violência em nome de Deus.</p>
  <p>O diálogo islamo-cristão enfrenta desafios teológicos reais: a natureza de Jesus (Filho de Deus para os cristãos, profeta para os muçulmanos), a Trindade (rejeitada pelo Islã como politeísmo), a crucificação (negada pelo Alcorão), a autoridade das Escrituras (o Alcorão afirma que a Bíblia foi corrompida). Estas diferenças não podem ser minimizadas em nome de uma unidade superficial. Mas o diálogo honesto que reconhece as diferenças enquanto busca a cooperação em questões de interesse comum — paz, justiça, cuidado dos pobres — é possível e necessário.</p>

  <div class="reflexao">
    <h3>🙏 Reflexão: Como os Cristãos Devem Relacionar-se com os Muçulmanos?</h3>
    <p>Jesus mandou amar os inimigos e orar pelos que nos perseguem (Mt 5:44). Esta instrução não é fácil de aplicar quando cristãos são perseguidos por muçulmanos — mas é o coração do Evangelho. O amor cristão pelos muçulmanos não é ingenuidade que ignora o perigo real do fundamentalismo islâmico; é a disposição de ver em cada muçulmano um ser humano criado à imagem de Deus, amado por Cristo, e para quem o Evangelho é boa notícia.</p>
    <p>A missão cristã entre muçulmanos é um dos campos mais desafiadores e mais frutíferos do século XXI. Milhares de muçulmanos estão se convertendo ao Cristianismo em todo o mundo — muitos através de sonhos e visões de Jesus, como documentado por pesquisadores e missionários. A Igreja é chamada a receber estes novos crentes com amor, a acompanhá-los no discipulado e a interceder pelos muçulmanos que ainda não conhecem Cristo.</p>
  </div>
</div>
"""

# ================================================================
# MÓDULO: RECONCILIAÇÃO
# ================================================================
recon_html = """
<div class="section-block">
  <h2>🤝 A Teologia da Reconciliação</h2>
  <p>A reconciliação é o coração do Evangelho. O apóstolo Paulo afirma que "Deus estava em Cristo reconciliando consigo o mundo" (2 Co 5:19) e que Cristo "reconciliou consigo mesmo todas as coisas, quer as que estão na terra, quer as que estão nos céus, fazendo a paz pelo sangue da sua cruz" (Cl 1:20). A reconciliação não é apenas um benefício da salvação — é a missão da Igreja: "Deus nos reconciliou consigo mesmo por meio de Cristo e nos deu o ministério da reconciliação" (2 Co 5:18).</p>
  <p>A reconciliação bíblica tem três dimensões inseparáveis: (1) a reconciliação vertical — a restauração da relação entre o ser humano e Deus, quebrada pelo pecado; (2) a reconciliação horizontal — a restauração das relações entre os seres humanos, divididos por pecado, injustiça e violência; e (3) a reconciliação cósmica — a restauração da criação inteira, que "geme e sofre as dores do parto" (Rm 8:22). Estas três dimensões são inseparáveis: quem é reconciliado com Deus é chamado a ser agente de reconciliação entre os seres humanos e com a criação.</p>
</div>

<div class="section-block">
  <h2>✨ Iniciativas Concretas de Reconciliação</h2>
  <div class="bloco">
    <div class="bloco-titulo">A Declaração Conjunta sobre a Justificação (1999)</div>
    <div class="bloco-texto">Em 31 de outubro de 1999, a Igreja Católica Romana e a Federação Luterana Mundial assinaram a Declaração Conjunta sobre a Doutrina da Justificação — o maior avanço ecumênico do século XX. O documento afirma um consenso básico sobre a justificação e declara que as condenações mútuas do século XVI não se aplicam às posições atuais das duas igrejas. Em 2006, a Comunhão Mundial de Igrejas Metodistas aderiu à declaração; em 2017, a Comunhão Mundial de Igrejas Reformadas também aderiu. Esta declaração não resolve todas as diferenças entre católicos e protestantes, mas demonstra que o diálogo teológico honesto pode superar divisões históricas.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">A Reconciliação Alemão-Polonesa (1965)</div>
    <div class="bloco-texto">Em novembro de 1965, os bispos católicos poloneses enviaram uma carta histórica aos bispos alemães com as palavras: "Perdoamos e pedimos perdão." Esta carta, escrita 20 anos após o fim da Segunda Guerra Mundial e as atrocidades nazistas na Polônia, foi um ato de coragem e fé extraordinário. Ela foi controversa na Polônia — muitos poloneses achavam que era cedo demais para perdoar. Mas ela abriu o caminho para a reconciliação alemão-polonesa que se tornaria um dos fundamentos da integração europeia.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">A Comissão de Verdade e Reconciliação da África do Sul (1996–1998)</div>
    <div class="bloco-texto">A Comissão de Verdade e Reconciliação (CVR) da África do Sul, presidida pelo Arcebispo Desmond Tutu, foi um dos experimentos mais ousados de reconciliação pós-conflito da história. Em vez de julgamentos de Nuremberg (punição) ou anistia geral (impunidade), a CVR ofereceu anistia condicional em troca de confissão pública e completa dos crimes. O processo foi doloroso e imperfeito — muitas vítimas sentiram que a justiça não foi feita. Mas ele demonstrou que a reconciliação é possível mesmo após crimes horrendos, e que a verdade — por mais dolorosa que seja — é o fundamento da paz duradoura.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">A Comunidade de Taizé — Reconciliação Vivida</div>
    <div class="bloco-texto">A Comunidade de Taizé, fundada pelo irmão Roger Schutz em 1940 na Borgonha francesa, é um dos mais poderosos sinais de reconciliação ecumênica do século XX. A comunidade reúne irmãos de diferentes tradições cristãs (católicos, protestantes, ortodoxos) em uma vida comum de oração, silêncio e serviço. Centenas de milhares de jovens de todo o mundo visitam Taizé anualmente. A espiritualidade de Taizé — marcada pela simplicidade, pela beleza litúrgica e pela busca da unidade — demonstra que a reconciliação não é apenas um projeto teológico, mas uma forma de vida.</div>
  </div>
</div>

<div class="section-block">
  <h2>🔑 Os Elementos da Reconciliação</h2>
  <div class="bloco">
    <div class="bloco-titulo">1. Verdade — O Fundamento da Reconciliação</div>
    <div class="bloco-texto">A reconciliação começa com a verdade — o reconhecimento honesto do que aconteceu, sem minimização, sem justificação, sem relativização. Para a Igreja, isso significa reconhecer os erros históricos: as Cruzadas, a Inquisição, o apoio a regimes coloniais e escravistas, a colaboração com o nazismo e o fascismo, o silêncio diante do Holocausto. O Papa João Paulo II pediu perdão por estes erros no Grande Jubileu de 2000 — um gesto histórico que foi recebido com gratidão por muitos e com ceticismo por outros. A verdade sem perdão é acusação; o perdão sem verdade é impunidade. A reconciliação requer ambos.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">2. Arrependimento — A Condição da Reconciliação</div>
    <div class="bloco-texto">O arrependimento (<em>metanoia</em>) é a mudança de mente e direção que torna a reconciliação possível. Não é apenas o remorso pelo passado — é a disposição de mudar o presente e o futuro. O arrependimento institucional é mais difícil do que o individual: como uma Igreja pode se arrepender dos crimes cometidos por seus antepassados? A resposta não é a culpa coletiva (que é injusta), mas o reconhecimento histórico (que é honesto) e o compromisso de não repetir os erros (que é construtivo).</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">3. Perdão — O Coração da Reconciliação</div>
    <div class="bloco-texto">O perdão é o ato pelo qual a vítima libera o agressor da dívida do mal cometido — não porque o mal não foi real, mas porque a vítima se recusa a ser definida pelo mal sofrido. O perdão cristão não é fraqueza — é força. Não é esquecimento — é a recusa de deixar o passado determinar o futuro. Não é reconciliação automática — é a condição que torna a reconciliação possível. Jesus disse: "Se não perdoardes aos homens as suas ofensas, também vosso Pai não vos perdoará as vossas ofensas" (Mt 6:15). O perdão não é opcional para o cristão — é o coração do Evangelho que ele recebeu e é chamado a transmitir.</div>
  </div>
  <div class="bloco">
    <div class="bloco-titulo">4. Justiça — A Garantia da Reconciliação</div>
    <div class="bloco-texto">A reconciliação sem justiça é impunidade disfarçada. A reconciliação bíblica não ignora a justiça — ela a inclui. O Salmo 85:10 afirma que "a misericórdia e a verdade se encontraram; a justiça e a paz se beijaram." A reconciliação autêntica inclui a reparação do dano causado (quando possível), a punição dos culpados (quando necessário) e a transformação das estruturas que tornaram o mal possível. A Comissão de Verdade e Reconciliação da África do Sul lutou com esta tensão: como equilibrar a necessidade de justiça das vítimas com a necessidade de reconciliação da nação?</div>
  </div>
</div>

<div class="section-block">
  <h2>🌟 A Esperança da Reconciliação</h2>
  <p>A reconciliação é possível porque Cristo reconciliou todas as coisas. Esta não é uma afirmação otimista sobre a bondade humana — é uma afirmação teológica sobre a obra de Deus em Cristo. A cruz é o lugar onde a justiça e a misericórdia se encontraram: Deus não ignorou o pecado (justiça), mas o absorveu em si mesmo (misericórdia). A reconciliação que a Igreja é chamada a promover no mundo é participação nesta obra de Deus — não uma conquista humana, mas uma resposta à iniciativa divina.</p>
  <p>O Apocalipse apresenta a visão final da reconciliação: "as nações andarão na sua luz, e os reis da terra trarão para ela a sua glória" (Ap 21:24). A Nova Jerusalém não é um lugar de uniformidade — é um lugar de diversidade reconciliada, onde as nações trazem sua glória e sua honra para a cidade de Deus. Esta visão é o horizonte que orienta o trabalho de reconciliação no presente: não a eliminação das diferenças, mas a transformação dos conflitos em comunhão.</p>

  <div class="reflexao">
    <h3>🙏 Reflexão Final: Somos Embaixadores da Reconciliação</h3>
    <p>"Portanto, somos embaixadores em nome de Cristo, como se Deus exortasse por nosso intermédio. Em nome de Cristo, pois, rogamos que vos reconcilieis com Deus" (2 Co 5:20). Paulo descreve os cristãos como "embaixadores da reconciliação" — representantes de Deus em um mundo dividido, portadores da mensagem de que a reconciliação é possível porque Cristo pagou o preço.</p>
    <p>Este bloco — Conflitos Religiosos Contemporâneos — termina não com um diagnóstico pessimista, mas com uma esperança fundamentada. Os conflitos são reais, as feridas são profundas, as divisões são históricas. Mas Cristo é mais poderoso do que qualquer divisão humana. A Igreja que leva a sério sua vocação de embaixadora da reconciliação pode ser, no mundo fragmentado do século XXI, um sinal do Reino de Deus — onde "não há judeu nem grego, nem escravo nem livre, nem homem nem mulher; porque todos vós sois um em Cristo Jesus" (Gl 3:28).</p>
  </div>
</div>
"""

MODULOS = [
    {
        "pasta": "reforma-protestante",
        "cor": "#f59e0b",
        "hero_bg": "#1a0e00",
        "titulo": "A Reforma Protestante",
        "subtitulo": "📜 Reforma Protestante · 1517 d.C.",
        "ref": "Martinho Lutero · João Calvino · Ulrico Zuínglio · 1517–1648",
        "citacao": "A consciência está cativa à Palavra de Deus. Não posso nem quero revogar coisa alguma, pois não é seguro nem honesto agir contra a própria consciência. Aqui estou; não posso fazer de outro modo.",
        "autor_citacao": "Martinho Lutero, Dieta de Worms, 1521",
        "conteudo": reforma_html,
        "nav_prev": "/11-conflitos-contemporaneos/cisma-oriente",
        "nav_prev_label": "← Cisma do Oriente",
        "nav_next": "/11-conflitos-contemporaneos/guerras-religiao",
        "nav_next_label": "Guerras de Religião →",
    },
    {
        "pasta": "guerras-religiao",
        "cor": "#ef4444",
        "hero_bg": "#1a0000",
        "titulo": "Guerras de Religião",
        "subtitulo": "⚔️ Guerras de Religião · Séc. XVI–XVII",
        "ref": "França · Alemanha · Inglaterra · 1562–1648",
        "citacao": "Assim que a moeda no cofre soa, a alma do purgatório logo voa.",
        "autor_citacao": "João Tetzel, vendedor de indulgências — a frase que provocou as 95 Teses de Lutero",
        "conteudo": guerras_html,
        "nav_prev": "/11-conflitos-contemporaneos/reforma-protestante",
        "nav_prev_label": "← Reforma Protestante",
        "nav_next": "/11-conflitos-contemporaneos/secularismo",
        "nav_next_label": "Secularismo →",
    },
    {
        "pasta": "secularismo",
        "cor": "#94a3b8",
        "hero_bg": "#0a0f1a",
        "titulo": "Secularismo e Laicidade",
        "subtitulo": "🏛️ Secularismo · Séc. XVIII–XXI",
        "ref": "Iluminismo · Revolução Francesa · Modernidade",
        "citacao": "A religião é o suspiro da criatura oprimida, o coração de um mundo sem coração, o espírito de condições sem espírito. É o ópio do povo.",
        "autor_citacao": "Karl Marx, Crítica da Filosofia do Direito de Hegel, 1844",
        "conteudo": seculo_html,
        "nav_prev": "/11-conflitos-contemporaneos/guerras-religiao",
        "nav_prev_label": "← Guerras de Religião",
        "nav_next": "/11-conflitos-contemporaneos/ecumenismo",
        "nav_next_label": "Ecumenismo →",
    },
    {
        "pasta": "ecumenismo",
        "cor": "#22d3ee",
        "hero_bg": "#001a1f",
        "titulo": "Ecumenismo e Diálogo Inter-Cristão",
        "subtitulo": "🕊️ Ecumenismo · Séc. XX–XXI",
        "ref": "Conselho Mundial de Igrejas · Vaticano II · Declaração Conjunta",
        "citacao": "Para que todos sejam um, como tu, ó Pai, és em mim, e eu em ti; que também eles sejam um em nós, para que o mundo creia que tu me enviaste.",
        "autor_citacao": "Jesus Cristo, João 17:21",
        "conteudo": ecum_html,
        "nav_prev": "/11-conflitos-contemporaneos/secularismo",
        "nav_prev_label": "← Secularismo",
        "nav_next": "/11-conflitos-contemporaneos/perseguicao-atual",
        "nav_next_label": "Perseguição Atual →",
    },
    {
        "pasta": "perseguicao-atual",
        "cor": "#f87171",
        "hero_bg": "#1a0000",
        "titulo": "Perseguição Cristã Contemporânea",
        "subtitulo": "🔥 Perseguição · Hoje",
        "ref": "365 Milhões de Cristãos Perseguidos · 2024",
        "citacao": "Bem-aventurados os que são perseguidos por causa da justiça, porque deles é o reino dos céus.",
        "autor_citacao": "Jesus Cristo, Mateus 5:10",
        "conteudo": perseg_html,
        "nav_prev": "/11-conflitos-contemporaneos/ecumenismo",
        "nav_prev_label": "← Ecumenismo",
        "nav_next": "/11-conflitos-contemporaneos/islamismo-cristandade",
        "nav_next_label": "Islamismo e Cristandade →",
    },
    {
        "pasta": "islamismo-cristandade",
        "cor": "#10b981",
        "hero_bg": "#001a0e",
        "titulo": "Islamismo e Cristandade",
        "subtitulo": "🌙 Islamismo e Cristandade · Séc. VII–XXI",
        "ref": "Cruzadas · Al-Andalus · Diálogo Contemporâneo",
        "citacao": "Não há compulsão na religião. O caminho reto se distingue claramente do erro.",
        "autor_citacao": "Alcorão, Surata 2:256 — frequentemente citado no diálogo islamo-cristão",
        "conteudo": islam_html,
        "nav_prev": "/11-conflitos-contemporaneos/perseguicao-atual",
        "nav_prev_label": "← Perseguição Atual",
        "nav_next": "/11-conflitos-contemporaneos/reconciliacao",
        "nav_next_label": "Reconciliação →",
    },
    {
        "pasta": "reconciliacao",
        "cor": "#22c55e",
        "hero_bg": "#001a08",
        "titulo": "Reconciliação e Esperança",
        "subtitulo": "🤝 Reconciliação · Esperança",
        "ref": "2 Coríntios 5:18-20 · Colossenses 1:20 · João 17:21",
        "citacao": "Deus estava em Cristo reconciliando consigo o mundo, não imputando aos homens as suas transgressões, e nos confiou a palavra da reconciliação.",
        "autor_citacao": "2 Coríntios 5:19",
        "conteudo": recon_html,
        "nav_prev": "/11-conflitos-contemporaneos/islamismo-cristandade",
        "nav_prev_label": "← Islamismo e Cristandade",
        "nav_next": "/11-conflitos-contemporaneos/index.html",
        "nav_next_label": "Índice do Bloco 11 →",
    },
]


def main():
    for m in MODULOS:
        html = modulo(
            m["pasta"], m["cor"], m["hero_bg"],
            m["titulo"], m["subtitulo"], m["ref"],
            m["citacao"], m["autor_citacao"],
            m["conteudo"],
            m["nav_prev"], m["nav_prev_label"],
            m["nav_next"], m["nav_next_label"]
        )
        path = os.path.join(BASE, m["pasta"], "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {m['pasta']}/index.html")
    print("\n🎉 Bloco 11 completo!")


if __name__ == "__main__":
    main()
