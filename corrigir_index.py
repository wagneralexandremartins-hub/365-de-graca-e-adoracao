#!/usr/bin/env python3
"""
Corrige os cards do index.html principal com a numeração correta.
06b → 07, e os seguintes sobem um número até 13.
"""

path = '/home/ubuntu/365-de-graca-e-adoracao/index.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

antigo = '''        <!-- Bloco 6b -->
        <article class="card block-card" data-bloco="08">
          <div class="poster">
            <span class="block-number">06b</span>
            <span class="tag">Ponte</span>
          </div>
          <div class="body">
            <h3>Período Intertestamentário</h3>
            <p>Os 400 anos entre Malaquias e Mateus. Impérios, grupos judaicos e expectativa messiânica.</p>
            <a href="/07-intertestamentario/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 7 -->
        <article class="card block-card" data-bloco="09">
          <div class="poster">
            <span class="block-number">07</span>
            <span class="tag">Revelação</span>
          </div>
          <div class="body">
            <h3>Novo Testamento</h3>
            <p>Cristo como revelação plena da graça. A Igreja nascente e a vida prática da fé.</p>
            <a href="/08-novo-testamento/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 8 -->
        <article class="card block-card" data-bloco="10">
          <div class="poster">
            <span class="block-number">08</span>
            <span class="tag">Perseguição</span>
          </div>
          <div class="body">
            <h3>Igreja Primitiva</h3>
            <p>Perseguições por causa do nome de Jesus. Formação doutrinária e tensões entre fé e poder.</p>
            <a href="/09-igreja-primitiva/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 9 -->
        <article class="card block-card" data-bloco="11">
          <div class="poster">
            <span class="block-number">09</span>
            <span class="tag">Organização</span>
          </div>
          <div class="body">
            <h3>Concílios e História da Igreja</h3>
            <p>Organização institucional, liturgia, doutrina e autoridade. Mudanças na forma de adorar.</p>
            <a href="/10-concilios/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 10 -->
        <article class="card block-card" data-bloco="12">
          <div class="poster">
            <span class="block-number">10</span>
            <span class="tag">Conflito</span>
          </div>
          <div class="body">
            <h3>Cruzadas e Guerras Religiosas</h3>
            <p>Fé misturada com conquista. Consequências históricas e espirituais.</p>
            <a href="/11-cruzadas/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 11 -->
        <article class="card block-card" data-bloco="13">
          <div class="poster">
            <span class="block-number">11</span>
            <span class="tag">Reflexão</span>
          </div>
          <div class="body">
            <h3>Conflitos Religiosos Contemporâneos</h3>
            <p>Heranças históricas, feridas abertas. Reflexão à luz do Reino de Deus.</p>
            <a href="/12-conflitos-contemporaneos/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 12 -->
        <article class="card block-card" data-bloco="13">
          <div class="poster">
            <span class="block-number">12</span>
            <span class="tag">Esperança</span>
          </div>
          <div class="body">
            <h3>Apocalipse</h3>
            <p>Esperança, responsabilidade e consumação da história.</p>
            <a href="/13-apocalipse/index.html">Explorar →</a>
          </div>
        </article>'''

novo = '''        <!-- Bloco 07 -->
        <article class="card block-card" data-bloco="07">
          <div class="poster">
            <span class="block-number">07</span>
            <span class="tag">Ponte</span>
          </div>
          <div class="body">
            <h3>Período Intertestamentário</h3>
            <p>Os 400 anos entre Malaquias e Mateus. Impérios, grupos judaicos e expectativa messiânica.</p>
            <a href="/07-intertestamentario/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 08 -->
        <article class="card block-card" data-bloco="08">
          <div class="poster">
            <span class="block-number">08</span>
            <span class="tag">Revelação</span>
          </div>
          <div class="body">
            <h3>Novo Testamento</h3>
            <p>Cristo como revelação plena da graça. A Igreja nascente e a vida prática da fé.</p>
            <a href="/08-novo-testamento/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 09 -->
        <article class="card block-card" data-bloco="09">
          <div class="poster">
            <span class="block-number">09</span>
            <span class="tag">Perseguição</span>
          </div>
          <div class="body">
            <h3>Igreja Primitiva</h3>
            <p>Perseguições por causa do nome de Jesus. Formação doutrinária e tensões entre fé e poder.</p>
            <a href="/09-igreja-primitiva/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 10 -->
        <article class="card block-card" data-bloco="10">
          <div class="poster">
            <span class="block-number">10</span>
            <span class="tag">Organização</span>
          </div>
          <div class="body">
            <h3>Concílios e História da Igreja</h3>
            <p>Organização institucional, liturgia, doutrina e autoridade. Mudanças na forma de adorar.</p>
            <a href="/10-concilios/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 11 -->
        <article class="card block-card" data-bloco="11">
          <div class="poster">
            <span class="block-number">11</span>
            <span class="tag">Conflito</span>
          </div>
          <div class="body">
            <h3>Cruzadas e Guerras Religiosas</h3>
            <p>Fé misturada com conquista. Consequências históricas e espirituais.</p>
            <a href="/11-cruzadas/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 12 -->
        <article class="card block-card" data-bloco="12">
          <div class="poster">
            <span class="block-number">12</span>
            <span class="tag">Reflexão</span>
          </div>
          <div class="body">
            <h3>Conflitos Religiosos Contemporâneos</h3>
            <p>Heranças históricas, feridas abertas. Reflexão à luz do Reino de Deus.</p>
            <a href="/12-conflitos-contemporaneos/index.html">Explorar →</a>
          </div>
        </article>
        <!-- Bloco 13 -->
        <article class="card block-card" data-bloco="13">
          <div class="poster">
            <span class="block-number">13</span>
            <span class="tag">Esperança</span>
          </div>
          <div class="body">
            <h3>Apocalipse</h3>
            <p>Esperança, responsabilidade e consumação da história.</p>
            <a href="/13-apocalipse/index.html">Explorar →</a>
          </div>
        </article>'''

if antigo in html:
    html = html.replace(antigo, novo)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('✅ index.html corrigido com sucesso!')
else:
    print('❌ Trecho não encontrado — verificando o que existe...')
    # Mostrar o trecho atual
    import re
    m = re.search(r'Bloco 6b.*?Bloco 12.*?</article>', html, re.DOTALL)
    if m:
        print('Trecho encontrado:', m.group(0)[:200])
    else:
        print('Nenhum trecho encontrado com "Bloco 6b"')
