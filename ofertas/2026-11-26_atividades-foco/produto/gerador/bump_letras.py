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
    "brincadeiras": (["PIQUE", "PEGA", "PIPA", "CORDA", "RODA", "BOLINHA", "CIRANDA", "PETECA"], "brincadeiras"),
}


VOGAL_EXTRAS = {
    "livro": ("LIVRO", ["LI", "VRO"], lambda v: '<path d="M50 24 C 38 16, 20 16, 8 20 L 8 82 C 20 78, 38 78, 50 86 Z"/>'
              '<path d="M50 24 C 62 16, 80 16, 92 20 L 92 82 C 80 78, 62 78, 50 86 Z"/><path d="M18 34 L 40 32 M18 46 L 40 44 M60 32 L 82 34 M60 44 L 82 46" fill="none"/>'),
    "mesa": ("MESA", ["ME", "SA"], lambda v: '<rect x="6" y="36" width="88" height="12" rx="2"/><rect x="14" y="48" width="8" height="40"/><rect x="78" y="48" width="8" height="40"/>'),
    "faca": ("FACA", ["FA", "CA"], lambda v: '<path d="M8 56 L 60 40 C 70 38, 72 48, 64 52 L 8 60 Z" fill="#fff"/>'
             '<rect x="62" y="44" width="32" height="12" rx="5" transform="rotate(-8 62 50)" fill="#d9d9d9"/>'),
    "vela": ("VELA", ["VE", "LA"], lambda v: '<rect x="38" y="36" width="24" height="54" rx="3"/><path d="M50 32 L 50 36" fill="none"/>'
             '<path d="M50 8 Q 40 22 50 30 Q 60 22 50 8 Z" fill="#d9d9d9"/>'),
    "meia": ("MEIA", ["MEI", "A"], lambda v: '<path d="M34 8 L 62 8 L 62 58 L 82 72 C 92 80, 84 96, 70 92 L 38 76 C 30 72, 34 64, 34 58 Z"/><path d="M34 20 L 62 20" fill="none"/>'),
    "mala": ("MALA", ["MA", "LA"], lambda v: '<rect x="10" y="32" width="80" height="56" rx="6"/><path d="M38 32 L 38 20 L 62 20 L 62 32" fill="none"/><path d="M10 54 L 90 54" fill="none"/>'),
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
    for k, (pal, sil, desenho) in VOGAL_EXTRAS.items():
        icones.DESENHOS.setdefault(k, desenho)

    def vogal_sem_repetir(pool):
        """5 folhas de "Qual vogal falta?" sem repetir palavra. O sorteio original gasta o rng principal
        (as outras páginas não mudam); a palavra repetida é trocada usando um rng derivado."""
        folhas, usadas = [], set()
        for f in range(5):
            orig = amostra(pool, 6)
            L.complete_vogal(rng, orig)  # só gasta o rng como antes
            alt = random.Random(f"vogal-{f}")
            livres = [k for k in pool + list(VOGAL_EXTRAS) if k not in usadas and k not in orig]
            esc = [k if k not in usadas else livres.pop(alt.randrange(len(livres))) for k in orig]
            usadas.update(esc)
            extras = {k: (p_, s_) for k, (p_, s_, _) in VOGAL_EXTRAS.items()}
            L.PALAVRAS.update(extras)
            folhas.append(L.complete_vogal(alt, esc))
            for k in extras:
                del L.PALAVRAS[k]
        return folhas

    def misturar_silabas(esc, i):
        """Cada folha de "Quantas sílabas?" mistura palavras de 1, 2 e 3 sílabas (sem rng)."""
        esc = esc[:]
        n_sil = lambda k: len(L.PALAVRAS[k][1])
        for alvo, pos in [(1, 7), (3, 6)]:
            if not any(n_sil(k) == alvo for k in esc):
                cand = [k for k in todas if n_sil(k) == alvo and k not in esc]
                esc[pos] = cand[i % len(cand)]
        assert len(set(esc)) == 8 and {n_sil(k) for k in esc} >= {1, 2, 3}
        return esc

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
        [L.complete_silaba(rng, amostra(multi, 6)) for _ in range(5)],
        [L.conte_silabas(misturar_silabas(amostra(todas, 8), i)) for i in range(4)],
        [L.forme_palavra(rng, amostra([k for k in todas if len(L.PALAVRAS[k][0]) <= 7], 6)) for _ in range(4)],
        [B.caca_palavras(rng, t) for t in TEMAS],
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
