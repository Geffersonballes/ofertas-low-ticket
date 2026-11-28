"""Bump 5 — Letras e palavras: 60 atividades (30 por nível). Nível 1: vogais, letra inicial, achar e
comparar letras. Nível 2: sílabas, palavras, rimas, frases, caça-palavras e ordem alfabética."""
import random

import icones

import atividades2 as B
import atv_letras as L
from bump_matematica import intercalar
from bumps_base import Bump

SEMENTE = 5050
BUMP = Bump("Letras e palavras", "letras-e-palavras", "60 ATIVIDADES · 2 NÍVEIS · GABARITO")
TEMAS = {
    "casa": (["SALA", "QUARTO", "COZINHA", "PORTA", "JANELA", "TELHADO", "ESCADA", "BANHEIRO"], "partes da casa"),
    "roupas": (["SAIA", "MEIA", "BLUSA", "SAPATO", "CASACO", "VESTIDO", "BERMUDA", "LUVA"], "roupas"),
    "doces": (["BOLO", "PUDIM", "BALA", "PIRULITO", "SORVETE", "BISCOITO", "GELATINA", "BRIGADEIRO"], "doces"),
    # antes: PIQUE, PEGA e BOLINHA (pedaços de pique-esconde, pega-pega e bolinha de gude). O sorteio da grade
    # antiga gasta o rng principal e a grade nova sai de um rng derivado (as outras páginas não mudam).
    "brincadeiras": (["XADREZ", "QUEIMADA", "PIPA", "AMARELINHA", "RODA", "CORDA", "CIRANDA", "PETECA"], "brincadeiras"),
}
BRINCADEIRAS_ANTIGO = ["PIQUE", "PEGA", "PIPA", "CORDA", "RODA", "BOLINHA", "CIRANDA", "PETECA"]


VOGAL_EXTRAS = {
    "livro": ("LIVRO", ["LI", "VRO"], lambda v: '<path d="M50 24 C 38 16, 20 16, 8 20 L 8 82 C 20 78, 38 78, 50 86 Z"/>'
              '<path d="M50 24 C 62 16, 80 16, 92 20 L 92 82 C 80 78, 62 78, 50 86 Z"/><path d="M18 34 L 40 32 M18 46 L 40 44 M60 32 L 82 34 M60 44 L 82 46" fill="none"/>'),
    "mesa": ("MESA", ["ME", "SA"], lambda v: '<rect x="6" y="36" width="88" height="12" rx="2"/><rect x="14" y="48" width="8" height="40"/><rect x="78" y="48" width="8" height="40"/>'),
    # faca de mesa: lâmina larga com ponta arredondada e cabo com rebites (a fina parecia um palito)
    "faca": ("FACA", ["FA", "CA"], lambda v: '<path d="M6 56 C 6 40, 22 32, 60 32 L 60 60 L 12 60 C 8 60, 6 59, 6 56 Z" fill="#fff"/>'
             '<rect x="60" y="36" width="34" height="20" rx="7" fill="#d9d9d9"/>'
             '<circle cx="70" cy="46" r="2.6" fill="#1d1d1f" stroke="none"/><circle cx="84" cy="46" r="2.6" fill="#1d1d1f" stroke="none"/>'),
    "vela": ("VELA", ["VE", "LA"], lambda v: '<rect x="38" y="36" width="24" height="54" rx="3"/><path d="M50 32 L 50 36" fill="none"/>'
             '<path d="M50 8 Q 40 22 50 30 Q 60 22 50 8 Z" fill="#d9d9d9"/>'),
    "meia": ("MEIA", ["MEI", "A"], lambda v: '<path d="M34 8 L 62 8 L 62 58 L 82 72 C 92 80, 84 96, 70 92 L 38 76 C 30 72, 34 64, 34 58 Z"/><path d="M34 20 L 62 20" fill="none"/>'),
    # mala de viagem com rodinhas e alça de puxar (a antiga parecia uma pasta)
    "mala": ("MALA", ["MA", "LA"], lambda v: '<path d="M40 26 L 40 6 L 60 6 L 60 26" fill="none"/>'
             '<rect x="22" y="26" width="56" height="60" rx="7"/><path d="M36 34 L 36 78 M50 34 L 50 78 M64 34 L 64 78" fill="none"/>'
             '<circle cx="33" cy="91" r="5" fill="#1d1d1f"/><circle cx="67" cy="91" r="5" fill="#1d1d1f"/>'),
}
# palavras só com E, I, O ou U, para variar a vogal que falta numa folha em que quase tudo dava A (ficam fora dos
# outros sorteios: as outras folhas não mudam)
VOGAL_VARIEDADE = {
    "sino": ("SINO", ["SI", "NO"], lambda v: '<path d="M50 14 C 30 14, 24 30, 24 50 L 24 68 L 12 80 L 88 80 L 76 68 L 76 50 C 76 30, 70 14, 50 14 Z"/>'
             '<circle cx="50" cy="88" r="7" fill="#d9d9d9"/><path d="M50 4 L 50 14 M36 30 C 32 40, 32 52, 32 62" fill="none"/>'),
    "pente": ("PENTE", ["PEN", "TE"], lambda v: '<rect x="6" y="28" width="88" height="18" rx="5" fill="#d9d9d9"/>'
              + '<path d="' + " ".join(f"M{x} 46 L {x} 76" for x in range(13, 92, 7)) + '" fill="none"/>'),
    "bule": ("BULE", ["BU", "LE"], lambda v: '<path d="M24 40 L 76 40 C 84 60, 80 84, 66 90 L 34 90 C 20 84, 16 60, 24 40 Z"/>'
             '<path d="M24 50 C 8 50, 6 34, 4 26" fill="none" stroke-width="7"/><path d="M76 48 C 96 48, 96 78, 76 80" fill="none"/>'
             '<path d="M30 40 C 32 28, 68 28, 70 40 Z" fill="#d9d9d9"/><circle cx="50" cy="24" r="5" fill="#d9d9d9"/>'),
    "milho": ("MILHO", ["MI", "LHO"], lambda v: '<path d="M50 6 C 66 6, 72 30, 70 58 C 68 78, 60 88, 50 88 C 40 88, 32 78, 30 58 C 28 30, 34 6, 50 6 Z" fill="#d9d9d9"/>'
              '<path d="M36 22 L 64 22 M32 36 L 68 36 M31 50 L 69 50 M32 64 L 68 64 M36 76 L 64 76 M43 10 L 41 84 M57 10 L 59 84" fill="none" stroke-width="2.4"/>'
              '<path d="M50 96 C 30 92, 18 74, 20 48 C 30 62, 38 76, 48 88 Z" fill="#fff"/><path d="M50 96 C 70 92, 82 74, 80 48 C 70 62, 62 76, 52 88 Z" fill="#fff"/>'),
}
# palavras de 1 sílaba com ícone próprio: o "Quantas sílabas?" precisa de uma por folha sem repetir (só havia SOL e FLOR)
NOVAS_1SIL = {
    "pao": ("PÃO", ["PÃO"], lambda v: '<path d="M8 62 C 8 34, 92 34, 92 62 C 92 76, 8 76, 8 62 Z"/>'
            '<path d="M28 46 L 38 60 M46 42 L 56 58 M64 44 L 74 58" fill="none"/>'),
    "trem": ("TREM", ["TREM"], lambda v: '<rect x="8" y="42" width="54" height="32" rx="3"/><rect x="56" y="22" width="34" height="52" rx="3"/>'
             '<rect x="63" y="29" width="20" height="15" fill="#d9d9d9"/><rect x="18" y="22" width="12" height="20"/>'
             '<path d="M4 88 L 96 88" fill="none"/><circle cx="24" cy="80" r="8"/><circle cx="48" cy="80" r="8"/><circle cx="74" cy="80" r="8"/>'),
}


def gerar():
    for k, (pal, tit) in TEMAS.items():
        assert all(len(p) <= (10 if p == pal[3] or p == pal[7] else 9) and p.isalpha() and p == L.sem_acento(p) for p in pal), k
        B.TEMAS_PALAVRAS[k] = pal
        B.TITULO_TEMA[k] = tit
    rng = random.Random(SEMENTE)
    todas = list(L.PALAVRAS)
    multi = [k for k in todas if len(L.PALAVRAS[k][1]) >= 2]

    def amostra(pool, n, iniciais_distintas=False):
        while True:
            esc = rng.sample(pool, n)
            if not iniciais_distintas or len({L.inicial(k) for k in esc}) == n:
                return esc

    # palavras extras só para trocar repetidas no "Qual vogal falta?" (entram depois dos sorteios: o rng não muda)
    # (só entram no L.PALAVRAS durante a montagem dessas folhas: outras atividades sorteiam do dicionário inteiro)
    for k, (pal, sil, desenho) in {**VOGAL_EXTRAS, **NOVAS_1SIL, **VOGAL_VARIEDADE}.items():
        icones.DESENHOS[k] = desenho
    extras_pal = {k: (p_, s_) for k, (p_, s_, _) in {**VOGAL_EXTRAS, **NOVAS_1SIL}.items()}

    def com_extras(f):
        """Roda f() com as palavras extras no dicionário (só durante a montagem da folha)."""
        L.PALAVRAS.update(extras_pal)
        try:
            return f()
        finally:
            for k in extras_pal:
                del L.PALAVRAS[k]

    usadas_n2 = {"silaba": set(), "conte": set(), "forme": set()}

    def trocar_repetidas(orig, usadas, pool, alt):
        livres = [k for k in pool if k not in usadas and k not in orig]
        esc = [k if k not in usadas else livres.pop(alt.randrange(len(livres))) for k in orig]
        usadas.update(esc)
        return esc

    def silaba_sem_repetir(i):
        """"Complete com a sílaba" sem repetir palavra no nível (sorteio original no rng principal, troca no derivado)."""
        orig = amostra(multi, 6)
        L.complete_silaba(rng, orig)  # só gasta o rng como antes
        alt = random.Random(f"silaba-{i}")
        pool = multi + [k for k, (p_, s_) in extras_pal.items() if len(s_) >= 2]
        esc = trocar_repetidas(orig, usadas_n2["silaba"], pool, alt)
        return com_extras(lambda: L.complete_silaba(alt, esc))

    def conte_sem_repetir(i):
        """"Quantas sílabas?" sem repetir palavra no nível e com palavras de 1, 2 e 3 sílabas em toda folha."""
        orig = amostra(todas, 8)
        alt = random.Random(f"conte-{i}")
        L.PALAVRAS.update(extras_pal)
        try:
            n_sil = lambda k: len(L.PALAVRAS[k][1])
            pool = todas + list(extras_pal)
            usadas = usadas_n2["conte"]
            esc = [k for k in orig]
            for pos, k in enumerate(esc):
                if k in usadas:
                    livres = [x for x in pool if x not in usadas and x not in esc and n_sil(x) == n_sil(k)] or \
                             [x for x in pool if x not in usadas and x not in esc]
                    esc[pos] = livres[alt.randrange(len(livres))]
            for alvo, pos in [(1, 7), (3, 6)]:
                if not any(n_sil(k) == alvo for k in esc):
                    cand = [x for x in pool if n_sil(x) == alvo and x not in usadas and x not in esc]
                    esc[pos] = cand[alt.randrange(len(cand))]
            assert len(set(esc)) == 8 and {n_sil(k) for k in esc} >= {1, 2, 3} and not set(esc) & usadas, esc
            usadas.update(esc)
            return L.conte_silabas(esc)
        finally:
            for k in extras_pal:
                del L.PALAVRAS[k]

    def forme_sem_repetir(i):
        """"Desembaralhe" sem repetir palavra no nível e sem embaralhado que forme outra palavra (TOGA, SACA)."""
        pool7 = [k for k in todas if len(L.PALAVRAS[k][0]) <= 7]
        orig = amostra(pool7, 6)
        L.forme_palavra(rng, orig)  # só gasta o rng como antes
        alt = random.Random(f"forme-{i}")
        pool = pool7 + [k for k, (p_, s_) in extras_pal.items() if len(p_) >= 4]
        esc = trocar_repetidas(orig, usadas_n2["forme"], pool, alt)
        return com_extras(lambda: L.forme_palavra(alt, esc, L.EMBARALHADAS_PROIBIDAS))

    def caca_brincadeiras():
        B.TEMAS_PALAVRAS["brincadeiras"] = BRINCADEIRAS_ANTIGO
        B.caca_palavras(rng, "brincadeiras")  # só gasta o rng como antes
        B.TEMAS_PALAVRAS["brincadeiras"] = TEMAS["brincadeiras"][0]
        return B.caca_palavras(random.Random("caca-brincadeiras"), "brincadeiras")

    def vogal_sem_repetir(pool):
        """5 folhas de "Qual vogal falta?" sem repetir palavra. O sorteio original gasta o rng principal
        (as outras páginas não mudam); a palavra repetida é trocada usando um rng derivado."""
        folhas, usadas, escolhas = [], set(), []
        extras = {k: (p_, s_) for k, (p_, s_, _) in VOGAL_EXTRAS.items()}
        for f in range(5):
            orig = amostra(pool, 6)
            L.complete_vogal(rng, orig)  # só gasta o rng como antes
            alt = random.Random(f"vogal-{f}")
            livres = [k for k in pool + list(VOGAL_EXTRAS) if k not in usadas and k not in orig]
            esc = [k if k not in usadas else livres.pop(alt.randrange(len(livres))) for k in orig]
            usadas.update(esc)
            escolhas.append(esc)
            L.PALAVRAS.update(extras)
            folhas.append(L.complete_vogal(alt, esc))
            for k in extras:
                del L.PALAVRAS[k]
        # pelo menos 3 vogais diferentes nas respostas de cada folha (antes uma folha tinha 5 A em 6). Depois de todas
        # as folhas: as palavras novas vêm das que nenhuma folha usou (as outras folhas não mudam)
        variedade = {k: (p_, s_) for k, (p_, s_, _) in VOGAL_VARIEDADE.items()}
        L.PALAVRAS.update({**extras, **variedade})
        try:
            for f, esc in enumerate(escolhas):
                resp = folhas[f]["_respostas"]
                mais = max(sorted(set(resp)), key=resp.count)
                k_tent = 0
                while len(set(folhas[f]["_respostas"])) < 3:
                    alt = random.Random(f"vogal-var-{f}-{k_tent}")
                    livres = sorted(k for k in pool + list(VOGAL_EXTRAS) + list(VOGAL_VARIEDADE) if k not in usadas
                                    and set(L.sem_acento(L.PALAVRAS[k][0])) & (set("AEIOU") - {mais}))
                    nova = esc[:]
                    for pos in alt.sample([i for i, v in enumerate(resp) if v == mais], 2):
                        nova[pos] = livres.pop(alt.randrange(len(livres)))
                    folhas[f] = L.complete_vogal(random.Random(f"vogal-{f}-{k_tent}"), nova)
                    k_tent += 1
                    assert k_tent < 200, f
                    if len(set(folhas[f]["_respostas"])) >= 3:
                        usadas.update(nova)
                assert len(set(folhas[f]["_respostas"])) >= 3, f
        finally:
            for k in {**extras, **variedade}:
                del L.PALAVRAS[k]
        return folhas

    n1 = intercalar([
        [L.trace_letra(v) for v in "AEIOU"] + [L.trace_vogais()],
        [L.letra_inicial(rng, amostra(todas, 6)) for _ in range(6)],
        [L.ligue_letra(rng, amostra(todas, 5, True)) for _ in range(4)],
        [L.encontre_letra(rng, a) for a in "AEOB"],
        vogal_sem_repetir([k for k in todas if len(L.PALAVRAS[k][0]) <= 6]),
        [L.letras_iguais(rng, rng.sample(list(L.PARECIDAS), 6)) for _ in range(5)],
    ])
    rimas = L.RIMAS[:]
    rng.shuffle(rimas)
    frases = L.FRASES[:]
    rng.shuffle(frases)
    n2 = intercalar([
        [silaba_sem_repetir(i) for i in range(5)],
        [conte_sem_repetir(i) for i in range(4)],
        [forme_sem_repetir(i) for i in range(4)],
        [B.caca_palavras(rng, t) if t != "brincadeiras" else caca_brincadeiras() for t in TEMAS],
        [L.rimas(rng, rimas[i * 5:(i + 1) * 5]) for i in range(4)],
        [L.complete_frase(rng, frases[i * 4:(i + 1) * 4]) for i in range(5)],
        [L.ordem_alfabetica(rng, amostra(todas, 5, i < 2)) for i in range(4)],
    ])
    for a in n2:
        if a["categoria"] != L.CAT:
            a["categoria"] = L.CAT
    assert len(n1) == 30 and len(n2) == 30
    assert all(a["nivel"] == 1 for a in n1) and all(a["nivel"] == 2 for a in n2)
    capa = BUMP.capa("Vogais, primeira letra, sílabas, rimas e frases curtas. Nível 1 com letras e sons; Nível 2 com palavras.",
                     ("Nível 1 · 4 a 6 anos  |  Nível 2 · 7 a 10 anos", "Gabarito no final"),
                     ["lapis", "estrela", "uva", "ovo", "ilha", "anel", "gato", "pipa"])
    uso = BUMP.pagina_texto("Como usar", """
  <ol>
    <li><b>Nível 1 (4 a 6 anos):</b> páginas 3 a 32. Vogais, primeira letra das palavras, achar e comparar letras. O adulto lê as instruções e os nomes das figuras.</li>
    <li><b>Nível 2 (7 a 10 anos):</b> páginas 33 a 62. Sílabas, desembaralhar palavras, rimas, frases, caça-palavras e ordem alfabética.</li>
    <li><b>Uma folha por dia</b> já é bastante. Imprima em preto e branco, papel A4 comum.</li>
    <li><b>Gabarito</b> no fim do arquivo.</li>
  </ol>
  <p>Fale as palavras em voz alta, bata palmas nas sílabas e brinque com as rimas. Ninguém precisa acertar tudo de primeira.</p>
  <p class="aviso">Uso permitido: imprima quantas vezes quiser para as crianças da sua família. Não é permitido revender nem repassar o arquivo.</p>""", 2)
    pags = [capa, uso]
    lista = []
    for a in n1 + n2:
        num = len(pags) + 1
        pags.append(BUMP.pagina_atividade(a, num))
        lista.append((num, a))
    pags += BUMP.gabarito(lista, len(pags) + 1)
    return dict(paginas=BUMP.montar(pags), atividades=len(lista))


if __name__ == "__main__":
    print(gerar())
