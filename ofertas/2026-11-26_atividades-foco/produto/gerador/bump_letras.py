"""Bump 5 — Letras e palavras: 60 atividades (30 por nível). Nível 1: vogais, letra inicial, achar e
comparar letras. Nível 2: sílabas, palavras, rimas, frases, caça-palavras e ordem alfabética."""
import random

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

    n1 = intercalar([
        [L.trace_letra(v) for v in "AEIOU"] + [L.trace_vogais()],
        [L.letra_inicial(rng, amostra(todas, 6)) for _ in range(6)],
        [L.ligue_letra(rng, amostra(todas, 5, True)) for _ in range(4)],
        [L.encontre_letra(rng, a) for a in "AEOB"],
        [L.complete_vogal(rng, amostra([k for k in todas if len(L.PALAVRAS[k][0]) <= 6], 6)) for _ in range(5)],
        [L.letras_iguais(rng, rng.sample(list(L.PARECIDAS), 6)) for _ in range(5)],
    ])
    rimas = L.RIMAS[:]
    rng.shuffle(rimas)
    frases = L.FRASES[:]
    rng.shuffle(frases)
    n2 = intercalar([
        [L.complete_silaba(rng, amostra(multi, 6)) for _ in range(5)],
        [L.conte_silabas(amostra(todas, 8)) for _ in range(4)],
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
