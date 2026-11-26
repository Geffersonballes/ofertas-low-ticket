"""Bump 2 — Tesoura e cola: 40 atividades de recortar e colar (20 por nível), com gabarito."""
import random

import atv_letras as L
import atv_recorte as R
from bump_matematica import intercalar
from bumps_base import Bump

SEMENTE = 2020
BUMP = Bump("Recortar e colar", "recortar-e-colar", "40 ATIVIDADES · 2 NÍVEIS · GABARITO")


def gerar():
    rng = random.Random(SEMENTE)
    n1 = intercalar([
        [R.quebra_cabeca(rng, n, 2, 1) for n in ["peixe", "casa", "gato", "sol", "barco"]],
        [R.sombras(rng, rng.sample(["sol", "lua", "estrela", "coracao", "peixe", "maca", "casa", "arvore", "gato", "pato", "pipa", "balao"], 5))
         for _ in range(5)],
        [R.do_menor_ao_maior(rng, n) for n in ["estrela", "balao", "flor", "carro"]],
        [R.classifique(rng, k, 3, 1) for k in ["ceu_agua", "frutas_brinq", "bichos_coisas", "comer_brincar"]],
        [R.padrao_cola(rng, [["sol", "lua"], ["maca", "maca", "uva"], ["estrela", "coracao", "flor"]]),
         R.padrao_cola(rng, [["peixe", "barco"], ["bola", "dado", "dado"], ["casa", "arvore", "arvore"]])],
    ])
    multi = [k for k in L.PALAVRAS if len(L.PALAVRAS[k][1]) >= 2 and len(L.PALAVRAS[k][1]) <= 3]
    n2 = intercalar([
        [R.quebra_cabeca(rng, n, k, 2, guia=False) for n, k in [("pato", 3), ("arvore", 3), ("balao", 3), ("pipa", 3), ("gato", 3)]],
        [R.silabas_cola(rng, rng.sample(multi, 3), L.PALAVRAS) for _ in range(5)],
        [R.classifique(rng, k, 4, 2) for k in ["comer_brincar", "casa_natureza", "bichos_coisas"]],
        [R.ordem_numeros(rng, 6, m) for m in [30, 60, 99]],
        [R.contas_cola(rng, op, m) for op, m in [("+", 10), ("-", 10), ("+", 20), ("-", 20)]],
    ])
    assert len(n1) == 20 and len(n2) == 20
    assert all(a["nivel"] == 1 for a in n1) and all(a["nivel"] == 2 for a in n2)
    capa = BUMP.capa("Quebra-cabeças, sombras, grupos, sílabas e contas para recortar e colar. Com tesoura sem ponta e cola branca.",
                     ("Nível 1 · 4 a 6 anos  |  Nível 2 · 7 a 10 anos", "Gabarito no final"),
                     ["tesoura", "estrela", "peixe", "gato", "balao", "casa", "flor", "pipa"])
    uso = BUMP.pagina_texto("Como usar", """
  <p class="aviso-adulto">✂ Atividades para fazer com um adulto por perto</p>
  <ol>
    <li><b>Use tesoura sem ponta</b> e cola branca ou em bastão. Forre a mesa com jornal.</li>
    <li><b>Cada folha tem duas partes:</b> em cima, a área de colar; embaixo, as peças com linha tracejada para recortar.</li>
    <li><b>Para os pequenos,</b> o adulto pode recortar as peças e a criança só monta e cola.</li>
    <li><b>Nível 1 (4 a 6 anos):</b> páginas 3 a 22. <b>Nível 2 (7 a 10 anos):</b> páginas 23 a 42.</li>
    <li><b>Gabarito</b> no fim do arquivo, com as figuras montadas.</li>
  </ol>
  <p>Papel um pouco mais grosso (90 g) deixa as peças mais firmes, mas o papel comum funciona.</p>
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
