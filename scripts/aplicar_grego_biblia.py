"""Grego koiné em todos os versículos de um capítulo da Bíblia ACF (biblia/<sigla>/<sigla>-NN.html).

Decisões do Wagner (14/10/2026, redesign/PLANO.md, "Grego em todos os versículos do NT"):
  • uma linha de grego abaixo de cada versículo, visível por padrão, com um botão por capítulo para
    ocultar/mostrar; crédito da licença uma vez por capítulo, no fim dos versículos (texto do piloto);
  • dados num JSON por livro com todos os versículos (scripts/dados/grego-nt/<livro>.json); os JSON dos
    estudos (scripts/dados/grego-tr-*.json) não mudam;
  • Fase 1 = piloto em PT só em biblia/jo/jo-03.html (no ar desde 15/10/2026, PR #20);
  • Fase 2, lote 1 (15/10/2026) = 2 João, 3 João e Judas, em PT.

Fonte: a mesma dos estudos (scripts/extrair_grego_door43.py) — Door43 STR/el-x-koine_trs, commit
4107626c, Textus Receptus 1894 Scrivener, CC BY-SA 4.0; conferência no byztxt 6049a43b.

O que muda (só com --apply):
  • scripts/dados/grego-nt/<livro>.json — novo (gravado com 'xb');
  • assets/js/grego-biblia.js — novo (botão ocultar/mostrar; sem JS o botão fica escondido e o grego visível);
  • assets/css/grego.css — regras novas acrescentadas no fim (classes que nenhuma outra página usa);
  • a página do capítulo: 1 bloco no <head>, o botão antes de <div class="verses">, 1 linha
    <span class="verso-grego" lang="grc"> depois de cada <span class="verse-text">, o crédito depois
    do fim de .verses. Nenhum byte do texto existente muda.
  • livros com "notas" (ex.: 3 Jo 15, numeração): 1 linha <span class="verso-nota"> abaixo do grego do
    versículo, e o bloco CSS grego-biblia-nota:v1 no fim do grego.css (só na 1ª vez).

Provas (se qualquer uma falhar, nada é gravado):
  • SHA-256 das fontes = fixados; USFM sem marcadores desconhecidos;
  • o livro inteiro sem palavra vazia nos capítulos aplicados; numeração ACF = Door43 = byztxt no capítulo
    (quando o byztxt junta versículos — 3 Jo 14-15 —, as palavras do Door43 juntas = as do byztxt);
  • no capítulo, Door43 = byztxt (só diferenças de grafia);
  • os versículos já publicados nos estudos (grego-tr-<livro>.json) saem idênticos;
  • página: novo menos os trechos inseridos = original, byte a byte; quebra de linha preservada;
    36 de 36 versículos com grego e na ordem; grego lido de volta da página = JSON;
  • nova simulação depois de gravar = 0 mudanças (idempotente).

Uso:
  python -X utf8 scripts/aplicar_grego_biblia.py --livro joao --caps 3 --fontes PASTA            # simulação
  python -X utf8 scripts/aplicar_grego_biblia.py --livro joao --caps 3 --fontes PASTA --apply    # grava (com backup)
  (PASTA = a mesma do extrair_grego_door43.py --baixar, fora do repositório)
"""
import datetime, html, json, os, re, sys, unicodedata, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import extrair_grego_door43 as ex
import aplicar_grego_jo3 as piloto

# autorizados = capítulos liberados pelo Wagner; juncoes_byz = versículos que o byztxt junta num só
# (a prova passa a ser: as palavras do Door43 nos versículos juntos = as do byztxt no versículo único);
# pendente = decisão do Wagner ainda em aberto (a simulação roda, o --apply é recusado).
LIVROS = {
    "joao": dict(sigla="jo", nome="João", usfm="44-JHN.usfm", byz="JOH.SCV", caps=21, autorizados=[3]),
    # Fase 2, lote 1 (15/10/2026): 2 João, 3 João e Judas, em PT
    "2jo": dict(sigla="2jo", nome="2 João", usfm="64-2JN.usfm", byz="2JO.SCV", caps=1, autorizados=[1],
                correcoes={(1, 7): [("εἰσῆλθόν εἰς", "εἰσῆλθον εἰς", "agudo de enclítica antes de εἰς, que não é enclítica")]}),
    "3jo": dict(sigla="3jo", nome="3 João", usfm="65-3JN.usfm", byz="3JO.SCV", caps=1, autorizados=[1],
                juncoes_byz={(1, 14): [14, 15]},
                # decisão do Wagner (15/10/2026): o grego segue a numeração da ACF, com nota discreta
                notas={(1, 15): "Nota: no Textus Receptus de Scrivener (1894), estas palavras fazem parte do "
                                "v. 14; aqui o grego segue a numeração da ACF."},  # texto aprovado em 15/10/2026
                correcoes={
                    (1, 9): [("Ἔγραψά τῇ", "Ἔγραψα τῇ", "agudo de enclítica antes de τῇ, que não é enclítica")],
                    (1, 15): [("εἰρήνῃ σοί ἀσπάζονταί σε οἵ φίλοι ἀσπάζου τούς φίλους κατ’ ὄνομα",
                               "εἰρήνη σοι. ἀσπάζονταί σε οἱ φίλοι. ἀσπάζου τοὺς φίλους κατ’ ὄνομα.",
                               "versículo sem pontuação e com acentos fora do padrão: εἰρήνῃ→εἰρήνη (nominativo), "
                               "σοί→σοι (enclítica), οἵ→οἱ (artigo), τούς→τοὺς (grave antes de palavra); 3 pontos acrescentados "
                               "(o versículo vinha sem pontuação)")],
                }),
    "jd": dict(sigla="jd", nome="Judas", usfm="66-JUD.usfm", byz="JUDE.SCV", caps=1, autorizados=[1],
               correcoes={
                   (1, 20): [("Πνεύματι Ἁγίω", "Πνεύματι Ἁγίῳ", "falta o iota subscrito do dativo")],
                   (1, 22): [("διακρινομένοι", "διακρινόμενοι", "acento na sílaba errada (particípio -όμενοι)")],
               }),
    # Fase 2, lote 2 (15/10/2026): Tiago, em PT
    # numeração ACF = Door43 = byztxt nos 5 capítulos (sem nota); lista de correções conferida e aprovada pelo
    # Wagner em 15/10/2026, incluindo 1:26 (mudança de sílaba do acento)
    "tg": dict(sigla="tg", nome="Tiago", usfm="60-JAS.usfm", byz="JAS.SCV", caps=5, autorizados=[1, 2, 3, 4, 5],
               correcoes={
                   (1, 12): [("λήψεταί τὸν", "λήψεται τὸν", "agudo de enclítica antes de τόν, que não é enclítica")],
                   (1, 26): [("θρησκὸς", "θρῆσκος", "acento na sílaba errada (forma dos léxicos: θρῆσκος)")],
                   (2, 2): [("τήν συναγωγὴν", "τὴν συναγωγὴν", "agudo final antes de palavra (grave)")],
                   (2, 18): [("κἀγώ δείξω", "κἀγὼ δείξω", "agudo final antes de palavra (grave)")],
                   (3, 5): [("μεγάλαυχεῖ", "μεγαλαυχεῖ", "dois acentos na mesma palavra")],
                   (3, 12): [("οὐδεμια", "οὐδεμία", "palavra sem acento")],
                   (4, 13): [("τήν πόλιν", "τὴν πόλιν", "agudo final antes de palavra (grave)"),
                             ("κερδήσομεν", "κερδήσομεν·", "versículo sem pontuação no fim (a frase continua no v. 14)")],
               }),
    # Fase 2, lote 3 (15/10/2026): 1 Pedro, em PT
    # numeração ACF = Door43 = byztxt nos 5 capítulos (sem nota); lista de correções conferida e aprovada pelo
    # Wagner em 15/10/2026 (1:7 confirmado: grave, antes de τιμιώτερον)
    "1pe": dict(sigla="1pe", nome="1 Pedro", usfm="61-1PE.usfm", byz="1PE.SCV", caps=5, autorizados=[1, 2, 3, 4, 5],
                correcoes={
                    (1, 4): [("οὐρανοῖς εἰς ὑμᾶς", "οὐρανοῖς εἰς ὑμᾶς,", "versículo sem pontuação no fim (a frase continua no v. 5)")],
                    (1, 7): [("πολυ τιμιώτερον", "πολὺ τιμιώτερον", "palavra sem acento (oxítona antes de palavra: grave)")],
                    (1, 16): [("ἅγιος εἰμι", "ἅγιός εἰμι", "proparoxítona antes de enclítica ganha 2º acento")],
                    (2, 6): [("ἐκλεκτόν ἔντιμον", "ἐκλεκτὸν ἔντιμον", "agudo final antes de palavra (grave)"),
                             ("ἐπ αὐτῷ", "ἐπ’ αὐτῷ", "falta o apóstrofo da elisão")],
                    (3, 1): [("κερδηθήσωνται", "κερδηθήσωνται,", "versículo sem pontuação no fim (a frase continua no v. 2)")],
                    (3, 12): [("οἵ ὀφθαλμοὶ", "οἱ ὀφθαλμοὶ", "artigo não leva acento")],
                    (3, 13): [("γένησθε", "γένησθε;", "pergunta sem ponto de interrogação grego")],
                    (3, 15): [("μετά πραΰτητος καί φόβου", "μετὰ πραΰτητος καὶ φόβου·",
                               "agudo final antes de palavra (grave), 2 vezes; versículo sem pontuação no fim")],
                    (3, 16): [("ἀγαθήν ἵνα", "ἀγαθὴν ἵνα", "agudo final antes de palavra (grave)"),
                              ("κακοποιων", "κακοποιῶν", "palavra sem acento"),
                              ("ἀναστροφήν", "ἀναστροφήν.", "versículo sem pontuação no fim (o v. 17 abre frase nova)")],
                    (4, 1): [("ἕν σαρκὶ", "ἐν σαρκὶ", "é a preposição ἐν, não o numeral ἕν")],
                    (4, 8): [("ἥ ἀγάπη", "ἡ ἀγάπη", "artigo não leva acento")],
                }),
    # Fase 2, lote 4 (16/10/2026): 2 Pedro, em PT
    # numeração ACF = Door43 = byztxt nos 3 capítulos (sem nota); lista de correções conferida e aprovada pelo
    # Wagner em 16/10/2026 (1:17 só o grave, sem vírgula; 2:7 sem pontuação no fim, como na fonte)
    "2pe": dict(sigla="2pe", nome="2 Pedro", usfm="62-2PE.usfm", byz="2PE.SCV", caps=3, autorizados=[1, 2, 3],
                correcoes={
                    (1, 12): [("ἀει ὑπομιμνήσκειν", "ἀεὶ ὑπομιμνήσκειν", "palavra sem acento (oxítona antes de palavra: grave)")],
                    (1, 17): [("Οὕτος ἐστιν", "Οὗτός ἐστιν", "οὗτος leva circunflexo; antes de enclítica ganha 2º acento"),
                              ("ἀγαπητός εἰς", "ἀγαπητὸς εἰς", "agudo final antes de palavra (grave)")],
                    (1, 21): [("ποτέ προφητεία", "ποτὲ προφητεία", "agudo final antes de palavra (grave)")],
                    (2, 2): [("δἰ οὓς", "δι’ οὓς", "elisão grafada com espírito em vez de apóstrofo")],
                    (2, 7): [("Λὼτ,", "Λώτ,", "grave antes de vírgula (agudo)")],
                    (2, 22): [("κὺλισμα", "κύλισμα", "grave no meio da frase em palavra paroxítona (agudo)")],
                    (3, 3): [("ἐμπαικται", "ἐμπαῖκται", "palavra sem acento")],
                    (3, 7): [("εἰσὶ,", "εἰσί,", "grave antes de vírgula (agudo)"),
                             ("πυρί τηρούμενοι", "πυρὶ τηρούμενοι", "agudo final antes de palavra (grave)")],
                    (3, 10): [("νυκτὶ,", "νυκτί,", "grave antes de vírgula (agudo)")],
                    (3, 11): [("οὺν", "οὖν", "οὖν leva circunflexo, não grave")],
                    (3, 16): [("γραφὰς,", "γραφάς,", "grave antes de vírgula (agudo)")],
                }),
    # Fase 2, lote 5 (16/10/2026): 1 João, em PT
    # numeração ACF = Door43 = byztxt nos 5 capítulos (sem nota); 5:7 (Comma Johanneum) está no Door43, no byztxt
    # (greektext-scrivener) e na ACF. Lista de correções conferida e aprovada pelo Wagner em 16/10/2026. Decisões:
    # 1:1 e 3:13 ficam como na fonte; pontuação de 2:13-15, θεοῦ minúsculo em 2:14 e ἀγαπᾷν em 4:20 ficam como na
    # fonte, porque o byztxt (textonly, sem acentos, pontuação nem maiúsculas) não confirma a forma proposta.
    "1jo": dict(sigla="1jo", nome="1 João", usfm="63-1JN.usfm", byz="1JO.SCV", caps=5, autorizados=[1, 2, 3, 4, 5],
                correcoes={
                    (1, 5): [("αὕτη ἔστιν", "αὕτη ἐστὶν", "enclítica depois de paroxítona: acento na última (ἔστιν só no uso enfático)")],
                    (1, 10): [("αὐτὸν,", "αὐτόν,", "grave antes de vírgula (agudo)")],
                    (2, 7): [("παλαιὰν,", "παλαιάν,", "grave antes de vírgula (agudo)")],
                    (2, 11): [("ἐστὶ,", "ἐστί,", "grave antes de vírgula (agudo)")],
                    (2, 14): [("ἀπ ἀρχῆς", "ἀπ’ ἀρχῆς", "falta o apóstrofo da elisão")],
                    (2, 16): [("σαρκὸς,", "σαρκός,", "grave antes de vírgula (agudo)")],
                    (2, 24): [("οὐν", "οὖν", "palavra sem acento")],
                    (2, 28): [("ἔχῶμεν", "ἔχωμεν", "dois acentos na mesma palavra")],
                    (3, 3): [("ἑαυτὸν,", "ἑαυτόν,", "grave antes de vírgula (agudo)")],
                    (3, 6): [("αὐτὸν,", "αὐτόν,", "grave antes de vírgula (agudo)")],
                    (3, 14): [("ἀδελφόν μένει", "ἀδελφὸν μένει", "agudo final antes de palavra (grave)")],
                    (3, 16): [("εκεῖνος", "ἐκεῖνος", "falta o espírito brando")],
                    (3, 17): [("ὅς δ’", "ὃς δ’", "agudo final antes de palavra (grave), como em 2:5")],
                    (4, 6): [("Θεὸν,", "Θεόν,", "grave antes de vírgula (agudo)")],
                    (4, 12): [("τετελειωμένη ἐστιν", "τετελειωμένη ἐστὶν", "enclítica dissílaba depois de paroxítona mantém o acento")],
                    (4, 19): [("αὐτὸν,", "αὐτόν,", "grave antes de vírgula (agudo)")],
                    (4, 21): [("Θεὸν,", "Θεόν,", "grave antes de vírgula (agudo)")],
                    (5, 7): [("μαρτυροῦντες εν τῷ", "μαρτυροῦντες ἐν τῷ", "preposição ἐν sem espírito brando")],
                    (5, 9): [("ἥν μεμαρτύρηκε", "ἣν μεμαρτύρηκε", "agudo final antes de palavra (grave)")],
                    (5, 12): [("υἱὸν,", "υἱόν,", "grave antes de vírgula (agudo)")],
                    (5, 13): [("ὑιοῦ", "υἱοῦ", "espírito e acento na vogal errada do ditongo υι")],
                    (5, 18): [("ἐαυτὸν,", "ἑαυτόν,", "espírito brando no lugar do áspero; grave antes de vírgula (agudo)")],
                    (5, 20): [("Θεὸς,", "Θεός,", "grave antes de vírgula (agudo)"),
                              ("ἥ ζωὴ", "ἡ ζωὴ", "artigo não leva acento")],
                }),
    # Fase 3, Apocalipse em 3 lotes (16/10/2026); lote 1 = capítulos 1 a 7, em PT
    # numeração ACF = Door43 = byztxt nos capítulos 1 a 7 (sem nota). Decisões do Wagner (16/10/2026):
    # D1 a keraia dos números (ιβʹ) sai só da comparação com o byztxt, o texto fica como na fonte;
    # D2 em 7:4 o numeral ρμδʹ (144) tem duas linhas vazias de lema, aceitas (o texto não muda);
    # D3 em 5:8 troca de letra, separada das de acento (εἴκοσιιτέσσαρες, com ι a mais; letras = byztxt).
    # 67 correções de acento e espírito em 49 versículos, aprovadas pelo Wagner. Ficam como na fonte, para revisão
    # futura: 3:3 (ἐπὶ σε, 2x); pontuação de 1:3, 1:20, 2:13, 2:27, 2:28, 3:12 e 7:7. O JSON só leva os
    # capítulos autorizados (json_por_lote).
    # Lote 2 = capítulos 8 a 14, aprovado pelo Wagner em 19/10/2026: lista A (acento e espírito), lista B (acento que
    # muda a palavra), D4 a D6 e o texto da nota de 13:1.
    # D4 ignorar_estigma: χξϛʹ (13:18) × byztxt cxv, só na comparação. D5/D6 fronteiras_ignoradas: τεσσαράκοντατέσσαρες
    # (14:1, 14:3; byztxt separa) e ἀπ’ ἄρτι (14:13; byztxt junta), só na comparação; o texto fica como na fonte.
    # mover: 12:18 do Door43 → início de 13:1 (ACF e byztxt), com nota (decisão do Wagner de 14/10/2026).
    # Ficam como na fonte, para revisão futura: 9:4 θεοῦ minúsculo; 9:19 falta pontuação antes de αἱ γὰρ; 13:4 τίς
    # minúsculo; 13:13 ponto em γῆν. ἐνώπιον; 14:8 pontuação; 14:13 pontuação entre ἄρτι e ναί; 14:3 ζώων sem iota subscrito.
    # Lote 3 = capítulos 15 a 22, aprovado pelo Wagner em 19/10/2026: lista A (acento, espírito e enclíticas), lista B
    # (20:14 οὗτός ἐστιν) e D7 (21:17 τεσσαράκοντατεσσάρων junto; byztxt separa; só na comparação). Numeração ACF =
    # Door43 = byztxt, sem nota. Ficam como na fonte, para revisão futura: 15:3 θεοῦ, κύριε, θεὸς minúsculos e sem
    # pontuação; 15:4 τίς minúsculo; 15:7 ζώων sem iota subscrito; 17:1 e 17:10 sem pontuação; 17:9 εἰσίν ἑπτὰ;
    # 18:23 φάνῃ (RP φανῇ); 19:4 θεῷ minúsculo e sem pontuação; 19:5 vírgula depois de αὐτόν; 19:10 pontuação antes de
    # τῷ Θεῷ; 20:12 θεοῦ minúsculo e vírgula depois de νεκρούς; 21:6 Ὦ (1:8, 1:11 e 22:13 têm Ω); 21:25 pontuação
    # entre ἡμέρας e νὺξ; 22:6 ponto alto em προφητῶν·; 22:20 vírgula em Ναί ἔρχου.
    "ap": dict(sigla="ap", nome="Apocalipse", usfm="67-REV.usfm", byz="RE.SCV", caps=22, autorizados=list(range(1, 23)),
               json_por_lote=True, ignorar_keraia=True,
               ignorar_estigma=True,
               fronteiras_ignoradas=[("tessarakonta", "tessarev"), ("ap", "arti"), ("tessarakonta", "tessarwn")],
               mover={(12, 18): (13, 1)},
               notas={(13, 1): "Nota: no Textus Receptus de Scrivener (1894), as primeiras palavras deste versículo "
                               "formam o v. 18 do capítulo 12; aqui o grego segue a numeração da ACF."},
               vazios_aceitos={(7, 4): "numeral ρμδʹ (144) em três partes; o Door43 deixa duas linhas vazias de lema"},
               correcoes_de_letra={(5, 8): [("εἴκοσιιτέσσαρες", "εἴκοσιτέσσαρες",
                                             "ι a mais (forma de 5:14; letras = byztxt eikositessarev)")]},
               correcoes={
                    (1, 4): [("ἃ ἐστιν", "ἅ ἐστιν", "oxítona antes de enclítica mantém o agudo")],
                    (1, 7): [("ὀφθαλμὸς,", "ὀφθαλμός,", "grave antes de pontuação (agudo)")],
                    (1, 11): [("Ἐγώ ἐιμι", "Ἐγώ εἰμι", "espírito e acento na vogal errada do ditongo ει")],
                    (1, 13): [("ὑιῷ", "υἱῷ", "espírito e acento na vogal errada do ditongo υι")],
                    (1, 14): [("ὡσει ἔριον", "ὡσεὶ ἔριον", "palavra sem acento (oxítona antes de palavra: grave)")],
                    (1, 18): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)")],
                    (1, 19): [("εἰσὶ,", "εἰσί,", "grave antes de pontuação (agudo)")],
                    (1, 20): [("ὦν εἶδες", "ὧν εἶδες", "relativo ὧν: espírito áspero"),
                              ("ἅς εἶδες", "ἃς εἶδες", "agudo final antes de palavra (grave)")],
                    (2, 1): [("Ἐφέσίνης", "Ἐφεσίνης", "dois acentos na mesma palavra")],
                    (2, 3): [("ἐβὰστασας", "ἐβάστασας", "grave no meio da palavra (agudo)")],
                    (2, 7): [("μέσῶ", "μέσῳ", "dois acentos e falta o iota subscrito do dativo")],
                    (2, 9): [("εἰσὶν,", "εἰσίν,", "grave antes de pontuação (agudo)")],
                    (2, 10): [("φυλακὴν,", "φυλακήν,", "grave antes de pontuação (agudo)")],
                    (2, 15): [("ὅ μισῶ", "ὃ μισῶ", "agudo final antes de palavra (grave)")],
                    (2, 17): [("λευκὴν,", "λευκήν,", "grave antes de pontuação (agudo)")],
                    (2, 21): [("εκ’ τῆς", "ἐκ τῆς", "preposição ἐκ sem espírito e com apóstrofo indevido (não há elisão)")],
                    (2, 27): [("κἀγώ εἴληφα", "κἀγὼ εἴληφα", "agudo final antes de palavra (grave)"),
                              ("παρά τοῦ", "παρὰ τοῦ", "agudo final antes de palavra (grave)")],
                    (3, 2): [("μὲλλει", "μέλλει", "grave no meio da palavra (agudo)")],
                    (3, 5): [("οὕτος", "οὗτος", "οὗτος leva circunflexo")],
                    (3, 9): [("διδωμι", "δίδωμι", "palavra sem acento"),
                             ("εἰσὶν,", "εἰσίν,", "grave antes de pontuação (agudo)"),
                             ("αὐτοὺς,", "αὐτούς,", "grave antes de pontuação (agudo)")],
                    (3, 12): [("ἡ καταβαίνει", "ἣ καταβαίνει", "é o relativo ἥ (grave antes de palavra), não o artigo")],
                    (3, 18): [("πυρὸς,", "πυρός,", "grave antes de pontuação (agudo)"),
                              ("λευκὰ,", "λευκά,", "grave antes de pontuação (agudo)")],
                    (3, 20): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)"),
                              ("αὐτὸν,", "αὐτόν,", "grave antes de pontuação (agudo)")],
                    (4, 1): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)")],
                    (4, 2): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)")],
                    (4, 3): [("ὅμοία", "ὁμοία", "dois acentos na mesma palavra (ὁμοία, como em 4:6)")],
                    (4, 4): [("εἴδον", "εἶδον", "εἶδον leva circunflexo")],
                    (4, 5): [("βρονταί καὶ", "βρονταὶ καὶ", "agudo final antes de palavra (grave)"),
                             ("φωναὶ.", "φωναί.", "grave antes de pontuação (agudo)")],
                    (4, 8): [("εἴχον", "εἶχον", "εἶχον leva circunflexo"),
                             ("ἕξ κυκλόθεν", "ἓξ κυκλόθεν", "agudo final antes de palavra (grave)"),
                             ("νυκτὸς,", "νυκτός,", "grave antes de pontuação (agudo)")],
                    (4, 10): [("βαλλοῦσι", "βάλλουσι", "presente βάλλουσι (com λλ); acento fora do lugar")],
                    (4, 11): [("ἐισὶ", "εἰσὶ", "espírito e acento na vogal errada do ditongo ει")],
                    (5, 4): [("πολλὰ,", "πολλά,", "grave antes de pontuação (agudo)")],
                    (5, 5): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)")],
                    (5, 9): [("καινὴν,", "καινήν,", "grave antes de pontuação (agudo)")],
                    (5, 11): [("κύκλοθεν", "κυκλόθεν", "acento na sílaba errada (κυκλόθεν, como em 4:3)")],
                    (5, 13): [("ὃ ἐστιν", "ὅ ἐστιν", "oxítona antes de enclítica mantém o agudo"),
                              ("θρόνοῦ", "θρόνου", "dois acentos na mesma palavra")],
                    (5, 14): [("αἰωνας", "αἰῶνας", "palavra sem acento")],
                    (6, 1): [("φωνὴς", "φωνῆς", "genitivo φωνῆς leva circunflexo")],
                    (6, 2): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)")],
                    (6, 5): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)")],
                    (6, 11): [("λευκαὶ,", "λευκαί,", "grave antes de pontuação (agudo)"),
                              ("πληρωσονται", "πληρώσονται", "palavra sem acento")],
                    (6, 15): [("δυνατοὶ,", "δυνατοί,", "grave antes de pontuação (agudo)")],
                    (7, 5): [("Ῥουβήν, ιβʹ χιλιάδες εσφραγισμένοι", "Ῥουβήν, ιβʹ χιλιάδες ἐσφραγισμένοι", "falta o espírito brando"),
                             ("Γάδ, ιβʹ χιλιάδες εσφραγισμένοι", "Γάδ, ιβʹ χιλιάδες ἐσφραγισμένοι", "falta o espírito brando")],
                    (7, 6): [("Ἀσὴρ, ιβʹ χιλιάδες εσφραγισμένοι", "Ἀσήρ, ιβʹ χιλιάδες ἐσφραγισμένοι", "grave antes de pontuação (agudo); falta o espírito brando"),
                             ("Νεφθαλείμ, ιβʹ χιλιάδες εσφραγισμένοι", "Νεφθαλείμ, ιβʹ χιλιάδες ἐσφραγισμένοι", "falta o espírito brando"),
                             ("Μανασσῆ, ιβʹ χιλιάδες εσφραγισμένοι", "Μανασσῆ, ιβʹ χιλιάδες ἐσφραγισμένοι", "falta o espírito brando")],
                    (7, 7): [("Συμεών, ιβʹ χιλιάδες εσφραγισμένοι", "Συμεών, ιβʹ χιλιάδες ἐσφραγισμένοι", "falta o espírito brando"),
                             ("Λευΐ, ιβʹ χιλιάδες, εσφραγισμένοι", "Λευΐ, ιβʹ χιλιάδες, ἐσφραγισμένοι", "falta o espírito brando"),
                             ("Ἰσαχάρ, ιβʹ χιλιάδες εσφραγισμένοι", "Ἰσαχάρ, ιβʹ χιλιάδες ἐσφραγισμένοι", "falta o espírito brando")],
                    (7, 8): [("Ζαβουλών, ιβʹ χιλιάδες εσφραγισμένοι", "Ζαβουλών, ιβʹ χιλιάδες ἐσφραγισμένοι", "falta o espírito brando"),
                             ("Ἰωσήφ, ιβʹ χιλιάδες εσφραγισμένοι", "Ἰωσήφ, ιβʹ χιλιάδες ἐσφραγισμένοι", "falta o espírito brando")],
                    (7, 9): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)")],
                    (7, 13): [("λευκὰς,", "λευκάς,", "grave antes de pontuação (agudo)"),
                              ("εἰσὶ,", "εἰσί,", "grave antes de pontuação (agudo)")],
                    (7, 14): [("Κύριέ,", "Κύριε,", "acento a mais antes de vírgula (vocativo Κύριε)")],
                    # lote 2, lista A: acento e espírito
                    (8, 3): [("πολλὰ,", "πολλά,", "grave antes de pontuação (agudo)")],
                    (8, 6): [("εαὐτοὺς", "ἑαυτοὺς", "espírito e acento na vogal errada do ditongo ευ")],
                    (8, 13): [("Οὐαὶ,", "Οὐαί,", "grave antes de pontuação (agudo)"),
                              ("οὐαὶ, οὐαὶ τοῖς", "οὐαί, οὐαὶ τοῖς", "grave antes de pontuação (agudo)")],
                    (9, 4): [("χλωρὸν,", "χλωρόν,", "grave antes de pontuação (agudo)")],
                    (9, 11): [("Ἀβαδδὼν,", "Ἀβαδδών,", "grave antes de pontuação (agudo)")],
                    (9, 14): [("ὅς εἴχε", "ὃς εἴχε", "agudo final antes de palavra (grave)"),
                              ("εἴχε", "εἶχε", "εἶχε leva circunflexo")],
                    (9, 19): [("κεφαλάς καὶ", "κεφαλὰς καὶ", "agudo final antes de palavra (grave)")],
                    (10, 4): [("βρονταί τὰς", "βρονταὶ τὰς", "agudo final antes de palavra (grave)"),
                              ("ταὐτὰ", "ταῦτα", "lista B: ταῦτα (estas coisas), não ταὐτά (as mesmas coisas)")],
                    (10, 5): [("οὐρανὸν,", "οὐρανόν,", "grave antes de pontuação (agudo)")],
                    (10, 6): [("έτι·", "ἔτι·", "falta o espírito brando")],
                    (11, 7): [("αὐτοὺς,", "αὐτούς,", "grave antes de pontuação (agudo)")],
                    (11, 9): [("τὰ πτῶματα", "τὰ πτώματα", "proparoxítona leva agudo (como no mesmo versículo)")],
                    (11, 14): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)")],
                    (12, 10): [("κατἐβλήθη", "κατεβλήθη", "espírito no meio da palavra"),
                               ("αυτῶν", "αὐτῶν", "falta o espírito brando")],
                    (12, 14): [("καιρὸν,", "καιρόν,", "grave antes de pontuação (agudo)")],
                    (12, 15): [("εκ’", "ἐκ", "preposição ἐκ sem espírito e com apóstrofo indevido (como em 2:21)"),
                               ("ταὐτὴν", "ταύτην", "lista B: ταύτην (esta), não ταὐτήν (a mesma)")],
                    (13, 1): [("ἑπτά καὶ", "ἑπτὰ καὶ", "agudo final antes de palavra (grave)"),
                              ("ὀνόμα", "ὄνομα", "acento na sílaba errada")],
                    (13, 4): [("τόν δράκοντα", "τὸν δράκοντα", "agudo final antes de palavra (grave)"),
                              ("ὅς ἔδωκεν", "ὃς ἔδωκεν", "agudo final antes de palavra (grave)")],
                    (13, 10): [("ἀποκτενει,", "ἀποκτενεῖ,", "palavra sem acento"),
                               ("αὐτον", "αὐτὸν", "palavra sem acento")],
                    (13, 13): [("γην.", "γῆν.", "palavra sem acento")],
                    (13, 17): [("ἤ τὸ", "ἢ τὸ", "agudo final antes de palavra (grave)")],
                    (14, 1): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)")],
                    (14, 3): [("ᾠδὴν,", "ᾠδήν,", "grave antes de pontuação (agudo)")],
                    (14, 4): [("οὗτοι εἰσιν οἱ", "οὗτοί εἰσιν οἱ", "lista B: properispómena antes de enclítica (como no início do versículo)")],
                    (14, 5): [("ἄμωμοί γάρ", "ἄμωμοι γάρ", "acento a mais (γάρ não é enclítica)")],
                    (14, 7): [("Θεὸν,", "Θεόν,", "grave antes de pontuação (agudo)")],
                    (14, 11): [("νυκτός οἱ", "νυκτὸς οἱ", "agudo final antes de palavra (grave)")],
                    (14, 13): [("ἄρτί", "ἄρτι", "dois acentos na mesma palavra")],
                    (14, 14): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)"),
                               ("υιῷ", "υἱῷ", "falta o espírito áspero")],
                    (14, 15): [("ἦλθε σοι", "ἦλθέ σοι", "lista B: properispómena antes de enclítica")],
                    (14, 18): [("τὸ ὀξὺ, λέγων", "τὸ ὀξύ, λέγων", "grave antes de pontuação (agudo)"),
                               ("τὸ ὀξὺ, καὶ", "τὸ ὀξύ, καὶ", "grave antes de pontuação (agudo)")],
                    # lote 3, listas A e B (aprovadas pelo Wagner em 19/10/2026)
                    (15, 2): [("ἀυτοῦ,", "αὐτοῦ,", "espírito e acento na vogal errada do ditongo αυ")],
                    (15, 6): [("λαμπρὸν,", "λαμπρόν,", "grave antes de pontuação (agudo)")],
                    (15, 8): [("ναὸν,", "ναόν,", "grave antes de pontuação (agudo)")],
                    (16, 6): [("έδωκας", "ἔδωκας", "falta o espírito brando"),
                              ("ἄξιοί γάρ", "ἄξιοι γάρ", "acento a mais (γάρ não é enclítica; como 14:5)")],
                    (16, 15): [("Ἰδοὺ,", "Ἰδού,", "grave antes de pontuação (agudo)")],
                    (16, 18): [("βρονταί καὶ", "βρονταὶ καὶ", "agudo final antes de palavra (grave)"),
                               ("ἀστραπαὶ,", "ἀστραπαί,", "grave antes de pontuação (agudo)")],
                    (17, 7): [("Διὰτί", "Διατί", "dois acentos na mesma palavra (τί interrogativo mantém o agudo)"),
                              ("ἐγὼ σοι", "ἐγώ σοι", "oxítona antes de enclítica mantém o agudo"),
                              ("γυναικὸς,", "γυναικός,", "grave antes de pontuação (agudo)")],
                    (17, 8): [("βλεπόντες", "βλέποντες", "acento na sílaba errada (particípio βλέποντες)"),
                              ("καὶπερ", "καίπερ", "grave no meio da palavra (agudo)")],
                    (17, 15): [("εἰσὶ,", "εἰσί,", "grave antes de pontuação (agudo)")],
                    (17, 17): [("ῥήματά τοῦ", "ῥήματα τοῦ", "acento a mais (τοῦ não é enclítica)")],
                    (17, 18): [("γυνὴ,", "γυνή,", "grave antes de pontuação (agudo)")],
                    (18, 7): [("ἑαυτὴν,", "ἑαυτήν,", "grave antes de pontuação (agudo)")],
                    (18, 9): [("ἀυτην,", "αὐτήν,", "espírito na vogal errada do ditongo αυ e palavra sem acento")],
                    (18, 10): [("Οὐαὶ,", "Οὐαί,", "grave antes de pontuação (agudo)"),
                               ("Βαβυλὼν,", "Βαβυλών,", "grave antes de pontuação (agudo)")],
                    (18, 14): [("αὐτὰ.", "αὐτά.", "grave antes de pontuação (agudo)")],
                    (18, 16): [("Οὐαὶ,", "Οὐαί,", "grave antes de pontuação (agudo)")],
                    (19, 7): [("ἀγαλλιῶμεθα", "ἀγαλλιώμεθα", "agudo, não circunflexo (ἀγαλλιώμεθα)")],
                    (19, 8): [("καθαρόν καὶ", "καθαρὸν καὶ", "agudo final antes de palavra (grave)"),
                              ("λαμπρὸν·", "λαμπρόν·", "grave antes de pontuação (agudo)"),
                              ("δικαιώματα ἐστι", "δικαιώματά ἐστι", "proparoxítona antes de enclítica ganha agudo na final")],
                    (19, 9): [("ἀληθινοὶ εἰσί τοῦ", "ἀληθινοί εἰσι τοῦ", "oxítona antes de enclítica mantém o agudo; enclítica sem acento")],
                    (19, 10): [("σού εἰμὶ", "σού εἰμι", "enclítica sem acento depois de σού")],
                    (19, 14): [("λεὺκοῖς,", "λευκοῖς,", "dois acentos na mesma palavra")],
                    (19, 20): [("τοὐτοῦ", "τούτου", "espírito e acento errados (τούτου)"),
                               ("ζωντες", "ζῶντες", "palavra sem acento"),
                               ("τῆν", "τὴν", "artigo τὴν com grave, não circunflexo")],
                    (20, 12): [("μικρούς καὶ", "μικροὺς καὶ", "agudo final antes de palavra (grave)"),
                               ("ἠνεῳχθησαν", "ἠνεῴχθησαν", "palavra sem acento"),
                               ("ἠνεῳχθη,", "ἠνεῴχθη,", "palavra sem acento")],
                    (20, 13): [("νεκροὺς,", "νεκρούς,", "grave antes de pontuação (agudo)"),
                               ("νεκροὺς·", "νεκρούς·", "grave antes de pontuação (agudo)")],
                    (20, 14): [("οὗτος ἐστιν", "οὗτός ἐστιν", "lista B: properispómena antes de enclítica (como 14:4)"),
                               ("δεύτερός θάνατος", "δεύτερος θάνατος", "acento a mais (θάνατος não é enclítica)")],
                    (21, 2): [("καινὴν,", "καινήν,", "grave antes de pontuação (agudo)")],
                    (21, 3): [("Ἰδοὺ,", "Ἰδού,", "grave antes de pontuação (agudo)"),
                              ("Θεός αὐτῶν", "Θεὸς αὐτῶν", "agudo final antes de palavra (grave)")],
                    (21, 4): [("κραυγὴ,", "κραυγή,", "grave antes de pontuação (agudo)")],
                    (21, 5): [("Ἰδοὺ,", "Ἰδού,", "grave antes de pontuação (agudo)"),
                              ("ἀληθινοί καὶ πιστοὶ εἰσι", "ἀληθινοὶ καὶ πιστοί εἰσι", "agudo final antes de palavra (grave); oxítona antes de enclítica mantém o agudo")],
                    (21, 7): [("Θεὸς,", "Θεός,", "grave antes de pontuação (agudo)")],
                    (21, 8): [("φαρμάκεῦσι", "φαρμακεῦσι", "dois acentos na mesma palavra")],
                    (21, 9): [("πρὸς με", "πρός με", "oxítona antes de enclítica mantém o agudo")],
                    (21, 10): [("Ἰερουσαλὴμ,", "Ἰερουσαλήμ,", "grave antes de pontuação (agudo)")],
                    (21, 12): [("ἔχουσαν τε", "ἔχουσάν τε", "proparoxítona antes de enclítica ganha agudo na final")],
                    (21, 18): [("καθαρὸν,", "καθαρόν,", "grave antes de pontuação (agudo)")],
                    (21, 21): [("καθαρὸν,", "καθαρόν,", "grave antes de pontuação (agudo)")],
                    (21, 24): [("φωτί αὐτῆς", "φωτὶ αὐτῆς", "agudo final antes de palavra (grave)")],
                    (22, 5): [("ἐκει,", "ἐκεῖ,", "palavra sem acento")],
                    (22, 7): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)")],
                    (22, 9): [("σύνδουλός σού γὰρ εἰμι", "σύνδουλός σου γάρ εἰμι", "enclítica σου sem acento; oxítona antes de enclítica mantém o agudo")],
                    (22, 12): [("ἰδοὺ,", "ἰδού,", "grave antes de pontuação (agudo)"),
                               ("ἐσται.", "ἔσται.", "palavra sem acento")],
                    (22, 13): [("ἐγὼ εἰμί", "ἐγώ εἰμι", "oxítona antes de enclítica mantém o agudo; enclítica sem acento")],
                    (22, 17): [("λέγουσιν, Ἐλθε.", "λέγουσιν, Ἐλθέ.", "palavra sem acento (imperativo ἐλθέ, oxítono como εἰπέ)"),
                               ("εἰπάτω, Ἐλθε.", "εἰπάτω, Ἐλθέ.", "palavra sem acento (imperativo ἐλθέ, oxítono como εἰπέ)")],
                    (22, 18): [("ταὐτά,", "ταῦτα,", "lista B: ταῦτα, estas coisas, não ταὐτά, as mesmas coisas; como 10:4")],
                    (22, 21): [("ημῶν", "ἡμῶν", "falta o espírito áspero")],
               }),
}
# opção B do Wagner (15/10/2026): corrigir só acentos e pontuação desses versículos, com a lista para conferência.
# Enquanto ele não conferir a lista, o --apply é recusado. Lista conferida e aprovada pelo Wagner em 15/10/2026.
CORRECOES_CONFERIDAS = True
# SHA-256 dos arquivos-fonte que o extrator dos estudos não fixa (baixados em 15/10/2026 das URLs por commit)
SHA256 = dict(ex.SHA256, **{
    "64-2JN.usfm": "510ffd6920ddb662eb8247d82b3994474b8c803e86ae4ef7e3c1bb7e8bae824e",
    "65-3JN.usfm": "6bcd5d449d18158360e61234cdaa95eb845b0e160eec072afe5f569b6d0f2da1",
    "66-JUD.usfm": "cdfe4c52fb603aff854d6ff16a2464ecc40ee3712948727e837b96a4044be80a",
    "2JO.SCV": "a1209c57cd8f58b40387edc3cb05f5684d8462f1d7159abf1a7cd2dd346de867",
    "3JO.SCV": "a53f4b694798fbe7280370721c32d29341236285fcebdf122f849b9b01825239",
    "JUDE.SCV": "dcb4d44026cf725f834af94158c936d0f422ab6fd465a1c383d25de7c313c480",
    # lote 2 (15/10/2026); hash git conferido no Door43 (114dcf7a) e no GitHub (984262b0)
    "60-JAS.usfm": "a8ef92440a13fed410ecb5233e914e015bee91f6b48aa197dc227fbec7fada17",
    "JAS.SCV": "a3147f8c8e585428012b187c0cc8195b61a71374023b47831bbb1499585a332f",
    # lote 3 (15/10/2026); hash git conferido no Door43 (a618528d) e no GitHub (563dab07)
    "61-1PE.usfm": "6722ad5aee512b3ff271a5151bb38dc54fb2bc19a3fbdf814e184baff5790160",
    "1PE.SCV": "de8c039b285b92f639b63bfc68ffe7181e6e1fda20e220ce5fc2e26bc37f203f",
    # lote 4 (16/10/2026); hash git conferido no Door43 (cc4f3a89) e no GitHub (3f9b1b9b)
    "62-2PE.usfm": "d1642c113122bf778f82c64470edcecbe8563199190df8050cbb6d1cce93428e",
    "2PE.SCV": "205c5f82d62cb44c557021b01330f748c001002173394ec6b657fdd21982bfcf",
    # lote 5 (16/10/2026); hash git conferido no Door43 (ce19ad36) e no GitHub (91e1f86b)
    "63-1JN.usfm": "a4be44f25c079d9004a81c79d7d05b9e37195d4cce8f324038555df4563a318b",
    "1JO.SCV": "7699f58795392da58a1fa5b434bbc0857d5e5a59f9c872fb3c612cc2f7f3064d",
    # Apocalipse (16/10/2026); hash git conferido no Door43 (e12499e8) e no GitHub (ab9e32e6)
    "67-REV.usfm": "3254b03513a5e6b4e7bd8a8c2a83b13fa6120828bf9be3a20d2fd3473d199510",
    "RE.SCV": "fdaef7bc014830b5d82596eef5a27cf0d1dc174d2a1b9825d7a2bdf696ad562b",
})

MARCA_INI, MARCA_FIM = "<!-- grego-biblia:v1 -->", "<!-- /grego-biblia:v1 -->"
HEAD = [
    MARCA_INI,
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gentium+Plus&amp;display=swap">',
    '<link rel="stylesheet" href="/assets/css/grego.css">',
    '<script src="/assets/js/grego-biblia.js" defer></script>',
    MARCA_FIM,
]
# rótulos do botão (regras-365: rótulo novo passa pelo Wagner) — aprovados em 15/10/2026
ROTULO_OCULTAR, ROTULO_MOSTRAR = "Ocultar o grego", "Mostrar o grego"
ROTULOS_APROVADOS = True
CREDITO = piloto.PAGINAS["pt"]["credito"]  # aprovado em 13/10/2026

CSS_MARCA = "/* grego-biblia:v1"
CSS_NOVO = """/* grego-biblia:v1 — grego em todos os versículos da Bíblia ACF (biblia/), inserido por scripts/aplicar_grego_biblia.py.
   Linha abaixo de cada versículo, visível por padrão; o botão (assets/js/grego-biblia.js) só aparece com JS. */
.verso-grego { display: block; text-indent: 0; margin: 0.2rem 0 0; font-family: "Gentium Plus", "Noto Serif", "Times New Roman", serif; font-size: 1.08em; line-height: 1.7; color: #b4c0d3; }
.verses.sem-grego .verso-grego { display: none; }
.grego-alternar { display: block; margin: 0 0 1.4rem auto; padding: 0.4rem 0.9rem; font-family: var(--font-ui, system-ui, sans-serif); font-size: 0.85rem; font-weight: 600; color: #5dade2; background: transparent; border: 1px solid #5dade2; border-radius: 5px; cursor: pointer; }
.grego-alternar:hover { background: rgba(93,173,226,0.12); }
.grego-alternar:focus-visible { outline: 2px solid #5dade2; outline-offset: 2px; }
.grego-alternar[hidden] { display: none; }
.grego-credito.grego-capitulo { margin: 1.6rem 0 0; padding: 0.8rem 0 0; border-top: 1px solid #2a3f5f; }
"""
# nota de numeração (só entra no grego.css quando um livro tem nota; o piloto de João não muda)
CSS_NOTA_MARCA = "/* grego-biblia-nota:v1"
CSS_NOTA = """/* grego-biblia-nota:v1 — nota discreta abaixo do grego (numeração/subscrição), some junto com o grego. */
.verso-nota { display: block; text-indent: 0; margin: 0.15rem 0 0; font-family: var(--font-ui, system-ui, sans-serif); font-size: 0.75rem; line-height: 1.5; color: #7d8ba1; }
.verses.sem-grego .verso-nota { display: none; }
"""

JS_NOVO = """/* grego-biblia:v1 — botão ocultar/mostrar o grego nos capítulos da Bíblia ACF (scripts/aplicar_grego_biblia.py).
   Sem JS o botão fica escondido e o grego visível. */
(function () {
  var b = document.querySelector('[data-grego-alternar]');
  var v = b && document.getElementById(b.getAttribute('aria-controls'));
  if (!v) return;
  b.hidden = false;
  b.addEventListener('click', function () {
    var oculto = v.classList.toggle('sem-grego');
    b.setAttribute('aria-pressed', oculto ? 'true' : 'false');
    b.textContent = oculto ? b.getAttribute('data-mostrar') : b.getAttribute('data-ocultar');
  });
})();
"""

RX_VERSO = re.compile(rb'(<div class="verse">\s*<span class="verse-number">(\d+)</span>\s*<span class="verse-text">.*?</span>)(\s*</div>)', re.S)
ABRE_VERSES = b'<div class="verses">'


def caminho_json(livro):
    return os.path.join(ROOT, "scripts", "dados", "grego-nt", f"{livro}.json")


def gera_json(livro, cfg, fontes, provas):
    arquivos = [cfg["usfm"], cfg["byz"]]
    for f in arquivos:
        provas[f"SHA-256 de {f} = fixado"] = ex.sha(os.path.join(fontes, f)) == SHA256[f]
    texto, vazios, estranhas, compostos = ex.le_usfm(os.path.join(fontes, cfg["usfm"]))
    provas["USFM só com marcadores esperados"] = not estranhas
    byz = ex.le_scv(os.path.join(fontes, cfg["byz"]))
    # ignorar_keraia (D1, Apocalipse): o Door43 escreve números com keraia (ιβʹ, U+0374) e o byztxt sem (ib);
    # a keraia sai só da comparação, o texto publicado fica como na fonte
    tl = (lambda s: ex.translit(s.replace("\u0374", "").replace("\u02b9", ""))) if cfg.get("ignorar_keraia") else ex.translit
    # ignorar_estigma (D4, Ap 13:18): o Door43 escreve 666 com estigma (χξϛʹ) e o byztxt com sigma final (cxv);
    # o estigma vira sigma final só na comparação, o texto publicado fica como na fonte
    if cfg.get("ignorar_estigma"):
        tl0 = tl
        tl = lambda s: tl0(s.replace("ϛ", "ς"))
    # fronteiras_ignoradas (D5 e D6, Ap 14:1, 14:3 e 14:13): pares de palavras que uma fonte escreve junto e a
    # outra separado; o par é juntado nos dois lados só na comparação, o texto publicado fica como na fonte
    pares = [tuple(p) for p in cfg.get("fronteiras_ignoradas", [])]

    def junta(ws):
        ws, out, i = list(ws), [], 0
        while i < len(ws):
            if i + 1 < len(ws) and (ws[i], ws[i + 1]) in pares:
                out.append(ws[i] + ws[i + 1]); i += 2
            else:
                out.append(ws[i]); i += 1
        return out

    compara = (lambda a, b: ex.compara(junta(a), junta(b))) if pares else ex.compara
    # json_por_lote (Apocalipse, em 3 lotes): o JSON só leva os capítulos autorizados
    if cfg.get("json_por_lote"):
        no_lote = set(cfg["autorizados"])
        texto = {k: t for k, t in texto.items() if k[0] in no_lote}
        vazios = {k for k in vazios if k[0] in no_lote}
        compostos = {k for k in compostos if k[0] in no_lote}
    # mover (Ap 12:18 → 13:1, decisão do Wagner de 14/10/2026): o grego segue a numeração da ACF; as palavras que
    # o Door43 numera à parte vão para o início do versículo seguinte, e o versículo junto tem de bater com o byztxt
    movidos = {}
    for (c, v), (c2, v2) in sorted(cfg.get("mover", {}).items()):
        if (c, v) not in texto or (c2, v2) not in texto:
            continue
        provas[f"mover {c}:{v} → {c2}:{v2}: o byztxt não tem o {c}:{v}"] = (c, v) not in byz
        texto[(c2, v2)] = texto.pop((c, v)) + " " + texto[(c2, v2)]
        r = compara(tl(texto[(c2, v2)]), byz.get((c2, v2), []))
        provas[f"mover {c}:{v} → {c2}:{v2}: versículo junto = byztxt {c2}:{v2} ({r})"] = r != "leitura"
        movidos[f"{c}:{v}"] = f"{c2}:{v2}"
    # vazios_aceitos (D2): linhas vazias de numeral aceitas por decisão do Wagner, versículo a versículo
    for (c, v), motivo in cfg.get("vazios_aceitos", {}).items():
        provas[f"{c}:{v}: linhas vazias aceitas por decisão ({motivo}) estão no USFM"] = (c, v) in vazios
    vazios = vazios - set(cfg.get("vazios_aceitos", {}))
    versos = {f"{c}:{v}": unicodedata.normalize("NFC", t) for (c, v), t in sorted(texto.items())}
    provas["NFC só troca por equivalentes canônicos"] = all(
        unicodedata.normalize("NFD", versos[f"{c}:{v}"]) == unicodedata.normalize("NFD", t) for (c, v), t in texto.items())
    provas["sem &, < ou > no grego"] = all(not set(t) & set("&<>") for t in versos.values())
    cmp = {k: compara(tl(t), byz.get(k, [])) for k, t in texto.items()}
    fmt = lambda ks: [f"{c}:{v}" for c, v in sorted(ks)]
    # correcoes_de_letra (D3): troca de letra autorizada pelo Wagner, separada das de acento; prova: o versículo
    # diferia do byztxt e passa a bater com ele
    correcoes_letra = {}
    for (c, v), trocas in sorted(cfg.get("correcoes_de_letra", {}).items()):
        k = f"{c}:{v}"; antes = versos[k]; depois = antes
        for velho, novo, motivo in trocas:
            velho, novo = unicodedata.normalize("NFC", velho), unicodedata.normalize("NFC", novo)
            provas[f"correção de letra {k}: forma do Door43 «{velho}» ocorre 1 vez"] = depois.count(velho) == 1
            depois = depois.replace(velho, novo, 1)
        r = compara(tl(depois), byz.get((c, v), []))
        provas[f"correção de letra {k}: antes ≠ byztxt, depois = byztxt ({r})"] = cmp[(c, v)] == "leitura" and r != "leitura"
        provas[f"correção de letra {k}: versículo sem correção de acento na mesma lista"] = (c, v) not in cfg.get("correcoes", {})
        correcoes_letra[k] = {"door43": antes, "publicado": depois, "motivo": "; ".join(m for _, _, m in trocas)}
        versos[k] = depois; cmp[(c, v)] = r
    # versículos que o byztxt junta num só: compara as palavras do Door43 juntas com o versículo do byztxt
    juncoes = {}
    for (c, vb), partes in cfg.get("juncoes_byz", {}).items():
        junto = tl(" ".join(texto[(c, v)] for v in partes))
        r = compara(junto, byz.get((c, vb), []))
        ok = r != "leitura" and all((c, v) not in byz for v in partes if v != vb)
        provas[f"byztxt junta {c}:{partes[0]}-{partes[-1]} em {c}:{vb}: palavras do Door43 juntas = byztxt ({r})"] = ok
        for v in partes: cmp[(c, v)] = "juncao" if ok else "leitura"
        juncoes[f"{c}:{vb}"] = [f"{c}:{v}" for v in partes]
    dados = {
        "livro": livro,
        "fonte": {"texto": "Textus Receptus 1894 Scrivener", "edicao": "Door43 STR/el-x-koine_trs",
                  "licenca": "CC BY-SA 4.0", "url": "https://git.door43.org/STR/el-x-koine_trs",
                  "commit": ex.DOOR43_COMMIT, "arquivo": cfg["usfm"], "sha256": SHA256[cfg["usfm"]]},
        "conferencia": {"texto": "byztxt greektext-scrivener (Robinson, domínio público)",
                        "commit": ex.BYZ_COMMIT, "arquivo": "textonly/" + cfg["byz"], "sha256": SHA256[cfg["byz"]],
                        "versiculos": len(cmp), "iguais": sum(r == "igual" for r in cmp.values()),
                        "so_grafia": sum(r == "grafia" for r in cmp.values()),
                        "outros": fmt(k for k, r in cmp.items() if r == "leitura")},
        "adaptacao": "só as palavras e a pontuação da fonte (sem lema, Strong e morfologia), Unicode NFC",
        "normalizados_nfc": fmt(k for k, t in texto.items() if unicodedata.normalize("NFC", t) != t),
        "itens_vazios_aceitos": fmt(compostos),
        "palavras_vazias": fmt(vazios),
        "versiculos": versos,
    }
    if juncoes:  # só aparece quando há junção (o JSON de João não muda)
        dados["conferencia"]["juncoes_byztxt"] = juncoes
    if movidos:  # só aparece quando há versículo movido (Ap 12:18 → 13:1)
        dados["conferencia"]["movidos_para_a_numeracao_acf"] = movidos
    # correções de acentuação/pontuação (opção B): só diacríticos e pontuação, letras idênticas
    letras = lambda s: "".join(c for c in unicodedata.normalize("NFD", s.lower()) if c.isalpha() and not unicodedata.combining(c))
    correcoes = {}
    for (c, v), trocas in sorted(cfg.get("correcoes", {}).items()):
        k = f"{c}:{v}"; antes = versos[k]; depois = antes
        for velho, novo, motivo in trocas:
            velho, novo = unicodedata.normalize("NFC", velho), unicodedata.normalize("NFC", novo)
            provas[f"correção {k}: forma do Door43 «{velho}» ocorre 1 vez"] = depois.count(velho) == 1
            depois = depois.replace(velho, novo, 1)
        provas[f"correção {k}: só acentos e pontuação (letras idênticas)"] = letras(antes) == letras(depois) and antes != depois
        correcoes[k] = {"door43": antes, "publicado": depois, "motivo": "; ".join(m for _, _, m in trocas)}
        versos[k] = depois
    for vb, partes in juncoes.items():  # versículo corrigido continua = byztxt (também nos versículos juntos)
        c = int(vb.split(":")[0])
        if any(p in correcoes for p in partes):
            r = compara(tl(" ".join(versos[p] for p in partes)), byz.get((c, int(vb.split(":")[1])), []))
            provas[f"corrigidos {partes} juntos = byztxt {vb} ({r})"] = r != "leitura"
    for k in correcoes:
        c, v = map(int, k.split(":"))
        if not any(k in ps for ps in juncoes.values()):
            r = compara(tl(versos[k]), byz.get((c, v), []))
            provas[f"corrigido {k} = byztxt ({r})"] = r != "leitura"
    if correcoes:  # só aparece quando há correção (o JSON de João não muda)
        dados = {k: x for k, x in dados.items() if k != "versiculos"} | {"correcoes_de_acentuacao": correcoes, "versiculos": versos}
    # D3 e D2: só aparecem quando existem (os JSON dos livros já publicados não mudam)
    extras = {}
    if correcoes_letra:
        extras["correcoes_de_letra"] = correcoes_letra
    if cfg.get("vazios_aceitos"):
        extras["vazios_aceitos_por_decisao"] = {f"{c}:{v}": m for (c, v), m in sorted(cfg["vazios_aceitos"].items())}
    if extras:
        dados = {k: x for k, x in dados.items() if k != "versiculos"} | extras | {"versiculos": versos}
    # os versículos já publicados nos estudos saem idênticos (só nos livros que têm estudo com grego)
    p_est = os.path.join(ROOT, "scripts", "dados", f"grego-tr-{livro}.json")
    if os.path.exists(p_est):
        estudos = json.load(open(p_est, encoding="utf-8"))["versiculos"]
        provas[f"os {len(estudos)} versículos publicados nos estudos = JSON novo"] = all(versos.get(k) == t for k, t in estudos.items())
    return dados, texto, byz, cmp, vazios


def aplica_pagina(antigo, cap, versos_cap, pv, notas=None):
    """Devolve (novo, insercoes, ordem). insercoes = [(posição no original, bytes)]."""
    nl = b"\r\n" if antigo.count(b"\r\n") == antigo.count(b"\n") else b"\n"
    pv["quebra de linha uniforme"] = antigo.count(b"\r\n") in (0, antigo.count(b"\n"))
    ins = []
    i_head = antigo.find(nl + b"</head>")
    pv["</head> único"] = antigo.count(b"</head>") == 1 and i_head > 0
    ins.append((i_head + len(nl), nl.join(h.encode() for h in HEAD) + nl))
    pv['<div class="verses"> único'] = antigo.count(ABRE_VERSES) == 1
    i_vs = antigo.find(ABRE_VERSES)
    recuo = antigo[antigo.rfind(b"\n", 0, i_vs) + 1:i_vs]
    botao = (f'<button type="button" class="grego-alternar" data-grego-alternar aria-controls="versiculos" '
             f'aria-pressed="false" data-ocultar="{ROTULO_OCULTAR}" data-mostrar="{ROTULO_MOSTRAR}" hidden>'
             f'{ROTULO_OCULTAR}</button>').encode()
    ins.append((i_vs, botao + nl + recuo))
    ins.append((i_vs + len(b'<div class="verses"'), b' id="versiculos"'))
    ordem = []
    for m in RX_VERSO.finditer(antigo):
        v = int(m.group(2)); ordem.append(v)
        linha_txt = antigo[antigo.rfind(b"\n", 0, m.end(1)) + 1:m.end(1)]
        recuo_v = re.match(rb"[ \t]*", linha_txt).group(0)
        g = versos_cap.get(v)
        if g is None: continue
        linha = nl + recuo_v + f'<span class="verso-grego" lang="grc">{g}</span>'.encode()
        if notas and (cap, v) in notas:
            linha += nl + recuo_v + f'<span class="verso-nota">{notas[(cap, v)]}</span>'.encode()
        ins.append((m.end(1), linha))
    # crédito: logo depois do </div> que fecha .verses (o 1º "</div>" de mesma indentação depois do último versículo)
    fim_ult = [m.end(3) for m in RX_VERSO.finditer(antigo)][-1]
    fecha = nl + recuo + b"</div>"
    i_fecha = antigo.find(fecha, fim_ult)
    pv["fim de .verses encontrado logo depois do último versículo"] = i_fecha > 0 and antigo[fim_ult:i_fecha].strip() == b""
    cred = nl + recuo + f'<p class="grego-credito grego-capitulo">{CREDITO}</p>'.encode()
    ins.append((i_fecha + len(fecha), cred))
    ins.sort(key=lambda t: t[0])
    novo, pos = b"", 0
    for p, b in ins:
        novo += antigo[pos:p] + b; pos = p
    novo += antigo[pos:]
    # prova: no novo, cada trecho está onde deveria; tirando-os, volta o original byte a byte
    partes, pos, desloc, no_lugar = [], 0, 0, True
    for p, b in ins:
        q = p + desloc
        no_lugar &= novo[q:q + len(b)] == b
        partes.append(novo[pos:q]); pos = q + len(b); desloc += len(b)
    partes.append(novo[pos:])
    pv["novo menos os trechos inseridos = original, byte a byte"] = no_lugar and b"".join(partes) == antigo
    pv["quebra de linha preservada (sem CR novo fora do padrão)"] = (novo.count(b"\r\n") == novo.count(b"\n")) == (nl == b"\r\n") \
        and (nl == b"\r\n" or novo.count(b"\r") == 0)
    return novo, ins, ordem


def main():
    a = sys.argv
    if "--livro" not in a or a[a.index("--livro") + 1] not in LIVROS or "--caps" not in a or "--fontes" not in a:
        print("uso: --livro " + "|".join(LIVROS) + " --caps N[,N...] --fontes PASTA [--apply]"); return 2
    livro = a[a.index("--livro") + 1]; cfg = LIVROS[livro]
    caps = [int(c) for c in a[a.index("--caps") + 1].split(",")]
    if not set(caps) <= set(cfg["autorizados"]):
        print(f"{cfg['nome']}: só os capítulos {cfg['autorizados']} estão autorizados."); return 2
    fontes = os.path.abspath(a[a.index("--fontes") + 1])
    apply = "--apply" in a
    provas = {}
    dados, texto, byz, cmp, vazios = gera_json(livro, cfg, fontes, provas)
    saida_json = (json.dumps(dados, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    dest_json = caminho_json(livro)
    atual_json = open(dest_json, "rb").read().replace(b"\r\n", b"\n") if os.path.exists(dest_json) else None
    cresce_json = False
    if cfg.get("json_por_lote") and atual_json not in (None, saida_json):
        # Apocalipse em lotes: o JSON cresce (ex.: 1–7 → 1–14); prova que tudo o que já está publicado fica idêntico
        velho, novo_j = json.loads(atual_json), dados
        vv, vn = velho["versiculos"], novo_j["versiculos"]
        provas[f"JSON cresce: os {len(vv)} versículos já publicados ficam idênticos"] = all(vn.get(k) == t for k, t in vv.items())
        provas["JSON cresce: só acrescenta versículos"] = set(vv) < set(vn)
        for campo in ("correcoes_de_acentuacao", "correcoes_de_letra", "vazios_aceitos_por_decisao"):
            antes, depois = velho.get(campo, {}), novo_j.get(campo, {})
            provas[f"JSON cresce: {campo} do lote anterior ({len(antes)}) idênticos"] = all(depois.get(k) == x for k, x in antes.items())
        provas["JSON cresce: itens_vazios_aceitos do lote anterior mantidos"] = set(velho["itens_vazios_aceitos"]) <= set(novo_j["itens_vazios_aceitos"])
        provas["JSON cresce: fonte e livro iguais"] = velho["fonte"] == novo_j["fonte"] and velho["livro"] == novo_j["livro"]
        cresce_json = True
    else:
        provas["JSON do livro novo ou idêntico ao existente"] = atual_json in (None, saida_json)

    css_path = os.path.join(ROOT, "assets", "css", "grego.css")
    css = open(css_path, "rb").read()
    css_nl = b"\r\n" if css.count(b"\r\n") == css.count(b"\n") else b"\n"
    css_novo = css
    if CSS_MARCA.encode() not in css_novo: css_novo += CSS_NOVO.replace("\n", css_nl.decode()).encode("utf-8")
    if cfg.get("notas") and CSS_NOTA_MARCA.encode() not in css_novo:
        css_novo += CSS_NOTA.replace("\n", css_nl.decode()).encode("utf-8")
    css_tem = css_novo == css
    provas["grego.css: só acréscimo no fim (original = prefixo)"] = css_novo.startswith(css) and css.endswith(css_nl)
    js_path = os.path.join(ROOT, "assets", "js", "grego-biblia.js")
    js_atual = open(js_path, "rb").read().replace(b"\r\n", b"\n") if os.path.exists(js_path) else None
    provas["grego-biblia.js novo ou idêntico"] = js_atual in (None, JS_NOVO.encode())

    paginas, relatorio = {}, []
    for cap in caps:
        rel = f"biblia/{cfg['sigla']}/{cfg['sigla']}-{cap:02d}.html"
        p = os.path.join(ROOT, rel)
        antigo = open(p, "rb").read()
        if MARCA_INI.encode() in antigo:
            relatorio.append((rel, "já tem", 0, 0)); continue
        acf = [int(n) for n in re.findall(rb'<span class="verse-number">(\d+)</span>', antigo)]
        d43 = sorted(v for c, v in texto if c == cap); bz = sorted(v for c, v in byz if c == cap)
        # o byztxt pode juntar versículos (juncoes_byz): conta como os versículos do Door43 que ele junta
        bz_exp = sorted({v for v in bz} | {v for (c, vb), ps in cfg.get("juncoes_byz", {}).items() if c == cap for v in ps})
        juntos = "" if bz == d43 else f"; byztxt com {len(bz)}, junções declaradas"
        provas[f"{rel}: numeração ACF = Door43 = byztxt ({len(acf)} versículos{juntos})"] = acf == d43 == bz_exp
        provas[f"{rel}: nenhuma palavra vazia no capítulo"] = not any(c == cap for c, _ in vazios)
        provas[f"{rel}: Door43 = byztxt no capítulo (0 diferenças de leitura)"] = all(
            cmp[(c, v)] != "leitura" for c, v in texto if c == cap)
        vc = {v: dados["versiculos"][f"{cap}:{v}"] for v in d43}
        pv = {}
        notas = {k: t for k, t in cfg.get("notas", {}).items() if k[0] == cap}
        novo, ins, ordem = aplica_pagina(antigo, cap, vc, pv, notas)
        lidas = re.findall(rb'<span class="verso-grego" lang="grc">[^<]*</span>\s*<span class="verso-nota">(.*?)</span>', novo)
        provas[f"{rel}: {len(notas)} nota(s), logo abaixo do grego do versículo certo"] = \
            [t.decode() for t in lidas] == [notas[k] for k in sorted(notas)] and novo.count(b'class="verso-nota"') == len(notas) \
            and all(re.search(rb'<span class="verse-number">%d</span>\s*<span class="verse-text">.*?</span>\s*<span class="verso-grego"[^>]*>[^<]*</span>\s*<span class="verso-nota">'
                              % v, novo, re.S) for (_, v) in notas)
        for k, ok in pv.items(): provas[f"{rel}: {k}"] = ok
        lidos = [(int(n), html.unescape(g.decode())) for n, g in re.findall(
            rb'<span class="verse-number">(\d+)</span>\s*<span class="verse-text">.*?</span>\s*<span class="verso-grego" lang="grc">(.*?)</span>', novo, re.S)]
        provas[f"{rel}: {len(lidos)} de {len(acf)} versículos com grego, na ordem, = JSON"] = \
            [v for v, _ in lidos] == ordem == acf and all(g == vc[v] for v, g in lidos)
        provas[f"{rel}: 1 bloco no head, 1 botão, 1 crédito"] = (novo.count(MARCA_INI.encode()), novo.count(b"data-grego-alternar"),
                                                                 novo.count(b"grego-capitulo")) == (1, 1, 1)
        paginas[rel] = (antigo, novo)
        relatorio.append((rel, "alvo", len(ins), len(novo) - len(antigo)))

    print(f"Livro: {livro} — JSON com {len(dados['versiculos'])} versículos; byztxt: {dados['conferencia']['iguais']} iguais, "
          f"{dados['conferencia']['so_grafia']} só grafia, outros (fronteira/variante, só informativo): {dados['conferencia']['outros']}")
    print(f"  itens vazios aceitos: {dados['itens_vazios_aceitos']}; palavras vazias: {dados['palavras_vazias']}")
    for k, ok in provas.items():
        print(f"  [{'ok' if ok else 'FALHOU'}] {k}")
    print(f"\n{os.path.relpath(dest_json, ROOT)}: {len(saida_json)} B, " + ("idêntico" if atual_json == saida_json else
          f"CRESCE ({len(atual_json)} → {len(saida_json)} B)" if cresce_json else "NOVO"))
    print(f"assets/css/grego.css: " + ("já tem as regras" if css_tem else f"+{len(css_novo) - len(css)} B no fim"))
    print(f"assets/js/grego-biblia.js: " + ("idêntico" if js_atual == JS_NOVO.encode() else f"NOVO, {len(JS_NOVO.encode())} B"))
    for rel, tipo, n, d in relatorio:
        print(f"{rel}: {tipo}" + (f", {n} inserções, +{d} B" if tipo == "alvo" else ""))
    if not all(provas.values()):
        print("Prova falhou: nada gravado."); return 1
    mudancas = (atual_json is None) + cresce_json + (not css_tem) + (js_atual is None) + len(paginas)
    if not apply:
        print(f"\nSimulação: {mudancas} arquivo(s) mudariam; nada gravado."); return 0
    if not ROTULOS_APROVADOS:
        print("\n--apply recusado: rótulos do botão ainda não aprovados (ROTULOS_APROVADOS = False)."); return 1
    if cfg.get("pendente"):
        print(f"\n--apply recusado: decisão pendente em {cfg['nome']}: {cfg['pendente']}."); return 1
    if cfg.get("correcoes") and not CORRECOES_CONFERIDAS:
        print(f"\n--apply recusado: a lista de correções de {cfg['nome']} ainda não foi conferida pelo Wagner."); return 1
    if mudancas == 0:
        print("Nada a fazer."); return 0
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    zp = os.path.join(ROOT, "_backups", f"grego-biblia-{livro}-{ts}.zip")
    with zipfile.ZipFile(zp, "x", zipfile.ZIP_DEFLATED) as z:
        for rel, (antigo, _) in paginas.items(): z.writestr(rel, antigo)
        if not css_tem: z.writestr("assets/css/grego.css", css)
        if cresce_json: z.writestr(os.path.relpath(dest_json, ROOT).replace(os.sep, "/"), open(dest_json, "rb").read())
    print(f"Backup: {os.path.relpath(zp, ROOT)}")
    if atual_json is None:
        os.makedirs(os.path.dirname(dest_json), exist_ok=True)
        with open(dest_json, "xb") as f: f.write(saida_json)
    if cresce_json:
        with open(dest_json, "wb") as f: f.write(saida_json)
    if js_atual is None:
        with open(js_path, "xb") as f: f.write(JS_NOVO.encode())
    if not css_tem:
        with open(css_path, "wb") as f: f.write(css_novo)
    for rel, (_, novo) in paginas.items():
        with open(os.path.join(ROOT, rel), "wb") as f: f.write(novo)
    with zipfile.ZipFile(zp) as z:
        ok = all(z.read(rel) == antigo and open(os.path.join(ROOT, rel), "rb").read() == novo for rel, (antigo, novo) in paginas.items())
    print("Gravado; conferido contra o backup: " + ("ok" if ok else "FALHOU"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
