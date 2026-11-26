"""Bump 4 — Matemática brincando: 60 atividades (30 por nível) de contar, somar, diminuir, comparar e
brincar de mercadinho com fichas de desenho próprio. Gabarito no fim."""
import random

import atv_matematica as M
import gerar_amostra as GA
from bumps_base import Bump

SEMENTE = 4040
BUMP = Bump("Matemática brincando", "matematica-brincando", "60 ATIVIDADES · 2 NÍVEIS · GABARITO")


def intercalar(grupos):
    """Round-robin entre os tipos, mantendo a ordem de dificuldade dentro de cada tipo."""
    out, i = [], 0
    while any(grupos):
        g = grupos[i % len(grupos)]
        if g:
            out.append(g.pop(0))
        i += 1
    return out


def gerar():
    rng = random.Random(SEMENTE)
    n1 = intercalar([
        [M.conte_escreva(rng, f) for f in [(1, 5), (1, 6), (2, 8), (3, 9), (4, 10)]],
        [M.soma_figuras(rng, m) for m in [5, 5, 7, 9, 10]],
        [M.subtrai_figuras(rng, m) for m in [5, 6, 7, 9, 10]],
        [M.onde_mais(rng) for _ in range(4)],
        [M.ligue_quantidade(rng) for _ in range(4)],
        [M.complete_numeros(rng, a) for a in [10, 10, 20, 20]],
        [M.mercadinho1(rng) for _ in range(3)],
    ])
    n2 = intercalar([
        [M.contas(rng, "+", m) for m in [10, 15, 20, 20, 30]],
        [M.contas(rng, "-", m) for m in [10, 15, 20, 20, 30]],
        [M.compara(rng, m) for m in [20, 50, 50, 99]],
        [M.piramide(rng, m) for m in [3, 4, 5, 5]],
        [M.dezenas(rng) for _ in range(3)],
        [M.mercadinho2(rng) for _ in range(4)],
        [M.grupos_iguais(rng) for _ in range(3)],
        [M.adivinha(rng) for _ in range(2)],
    ])
    assert len(n1) == 30 and len(n2) == 30
    assert all(a["nivel"] == 1 for a in n1) and all(a["nivel"] == 2 for a in n2)
    capa = BUMP.capa("Contar, somar, diminuir, comparar e brincar de mercadinho com fichas de papel.",
                     ("Nível 1 · 4 a 6 anos  |  Nível 2 · 7 a 10 anos", "Gabarito no final"),
                     ["maca", "estrela", "dado", "balao", "bola", "pipa", "uva", "carro"])
    uso = BUMP.pagina_texto("Como usar", """
  <ol>
    <li><b>Nível 1 (4 a 6 anos):</b> páginas 4 a 33. Contar figuras, juntar, tirar, comparar e ligar ao número.</li>
    <li><b>Nível 2 (7 a 10 anos):</b> páginas 34 a 63. Contas até 30, maior e menor, pirâmide de somas, dezenas, grupos e problemas de mercadinho.</li>
    <li><b>Uma folha por dia</b> já é bastante. Imprima em preto e branco, papel A4 comum.</li>
    <li><b>Fichas de brincar</b> na página 3: recorte e use para "pagar" nas atividades de mercadinho. Não são dinheiro de verdade.</li>
    <li><b>Gabarito</b> no fim do arquivo.</li>
  </ol>
  <p>Vale contar nos dedos, desenhar bolinhas e usar feijões. O importante é a criança entender o que está fazendo, não decorar.</p>
  <p class="aviso">Uso permitido: imprima quantas vezes quiser para as crianças da sua família. Não é permitido revender nem repassar o arquivo.</p>""", 2)
    fichas = f"""<section class="pagina">{BUMP.topo('<span class="selo">Material</span>')}<h1>Fichas de brincar</h1>
  <p class="instrucao">Para as atividades de mercadinho. Recorte nas linhas tracejadas.</p>
  <div class="area">{GA.svg(M.dinheirinho())}</div>{BUMP.rodape(3)}</section>"""
    pags = [capa, uso, fichas]
    lista = []
    for a in n1 + n2:
        num = len(pags) + 1
        pags.append(BUMP.pagina_atividade(a, num))
        lista.append((num, a))
    pags += BUMP.gabarito(lista, len(pags) + 1)
    return dict(paginas=BUMP.montar(pags), atividades=len(lista))


if __name__ == "__main__":
    print(gerar())
