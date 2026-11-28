"""Bump 6 — Jogos de mesa para imprimir: bingo de figuras, dominó de figuras, jogo da memória, trilha com
dado de papel e jogo da velha. Jogos de domínio público, peças e tabuleiros desenhados por nós."""
import itertools
import random

import gerar_amostra as GA
from atividades import W, H, _txt
from bumps_base import Bump, caixa_corte, LAR
from icones import icone, TRACO

SEMENTE = 6060
BUMP = Bump("Jogos de mesa", "jogos-de-mesa", "5 JOGOS PARA IMPRIMIR E JOGAR EM FAMÍLIA")
FIGS16 = ["sol", "lua", "estrela", "coracao", "peixe", "flor", "casa", "arvore", "maca", "balao", "barco", "carro",
          "nuvem", "passaro", "uva", "banana"]
NOMES = {"sol": "sol", "lua": "lua", "estrela": "estrela", "coracao": "coração", "peixe": "peixe", "flor": "flor",
         "casa": "casa", "arvore": "árvore", "maca": "maçã", "balao": "balão", "barco": "barco", "carro": "carro",
         "nuvem": "nuvem", "passaro": "passarinho", "uva": "uva", "banana": "banana"}


def pagina(titulo, instrucao, svg, num, selo):
    return f"""<section class="pagina">{BUMP.topo(f'<span class="selo">{selo}</span>')}
  <h1>{titulo}</h1><p class="instrucao">{instrucao}</p>
  <div class="area">{GA.svg(svg)}</div>{BUMP.rodape(num)}</section>"""


def tesoura_txt(y):
    return (f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#999" stroke-width=".4" stroke-dasharray="2 1.5"/>'
            + _txt(W / 2, y + 3.5, "✂ recorte nas linhas tracejadas", 4, 700, cor="#888"))


# ------------------------------------------------------------------ bingo
def bingo(rng):
    while True:
        cartelas = set()
        while len(cartelas) < 6:
            cartelas.add(tuple(sorted(rng.sample(range(16), 9))))
        if set(itertools.chain(*cartelas)) == set(range(16)):
            break
    cartelas = [list(c) for c in sorted(cartelas)]
    for c in cartelas:
        rng.shuffle(c)
    # cada figura aparece em pelo menos uma cartela
    assert set(itertools.chain(*cartelas)) == set(range(16)) and len({tuple(sorted(c)) for c in cartelas}) == 6
    pags = []
    for p in range(3):
        s = []
        for k in range(2):
            c = cartelas[p * 2 + k]
            y0 = 2 + k * 118
            s.append(f'<rect x="20" y="{y0}" width="142" height="108" rx="5" fill="#fff" stroke="{TRACO}" stroke-width="1"/>')
            s.append(_txt(W / 2, y0 + 8, f"BINGO DE FIGURAS · CARTELA {p * 2 + k + 1}", 5.6, 800, fonte="Baloo 2"))
            for i, f in enumerate(c):
                cx, cy = 34 + (i % 3) * 38, y0 + 16 + (i // 3) * 30
                s.append(f'<rect x="{cx - 2}" y="{cy}" width="36" height="28" rx="3" fill="none" stroke="#888" stroke-width=".6"/>')
                s.append(icone(FIGS16[f], cx + 7, cy + 2, 20))
                s.append(_txt(cx + 16, cy + 25, NOMES[FIGS16[f]], 3.6, 700, cor="#555"))
            if k == 0:
                s.append(tesoura_txt(113))
        pags.append(("Bingo de figuras", "Uma cartela para cada jogador. Recorte as cartelas na linha do meio.", "".join(s)))
    # fichas de sorteio
    s = []
    for i, f in enumerate(FIGS16):
        x, y = 6 + (i % 4) * 43, 4 + (i // 4) * 52
        s.append(caixa_corte(x, y, 40, 48, 3))
        s.append(icone(f, x + 6, y + 5, 28))
        s.append(_txt(x + 20, y + 41, NOMES[f], 5, 800))
    pags.append(("Bingo: fichas para sortear", "Recorte as 16 fichas, dobre e coloque num potinho. Use feijões ou tampinhas para marcar a cartela.", "".join(s)))
    return pags, cartelas


# ------------------------------------------------------------------ dominó
def domino():
    figs = ["sol", "lua", "estrela", "coracao", "peixe", "flor", "casa"]
    pecas = [(a, b) for a in range(7) for b in range(a, 7)]
    assert len(pecas) == 28 and len(set(pecas)) == 28
    pags = []
    for p in range(2):
        s = []
        for i, (a, b) in enumerate(pecas[p * 14:(p + 1) * 14]):
            x, y = 8 + (i % 2) * 86, 3 + (i // 2) * 31.5
            s.append(f'<rect x="{x}" y="{y}" width="80" height="29" rx="4" fill="#fff" stroke="#888" stroke-width=".6" stroke-dasharray="2 1.4"/>')
            s.append(f'<line x1="{x + 40}" y1="{y + 4}" x2="{x + 40}" y2="{y + 25}" stroke="{TRACO}" stroke-width=".8"/>')
            s.append(icone(figs[a], x + 9, y + 3.5, 22))
            s.append(icone(figs[b], x + 49, y + 3.5, 22))
        pags.append(("Dominó de figuras" + (" (continuação)" if p else ""),
                     "28 peças. Recorte nas linhas tracejadas. Papel mais grosso deixa as peças mais firmes.", "".join(s)))
    return pags


# ------------------------------------------------------------------ memória
def memoria(rng):
    figs = FIGS16[:12]
    cartas = figs * 2
    rng.shuffle(cartas)
    assert all(cartas.count(f) == 2 for f in figs)
    s = []
    for i, f in enumerate(cartas):
        x, y = 3 + (i % 4) * 44.5, 2 + (i // 4) * 37.5
        s.append(caixa_corte(x, y, 42, 35, 4))
        s.append(icone(f, x + 9, y + 4, 24))
        s.append(_txt(x + 21, y + 31, NOMES[f], 4.2, 800, cor="#555"))
    return [("Jogo da memória", "24 cartas (12 pares). Recorte nas linhas tracejadas. Para não ver através, cole num papel colorido antes de recortar.", "".join(s))]


# ------------------------------------------------------------------ trilha
ESPECIAIS = {5: "avance", 13: "avance", 22: "avance", 9: "volte", 18: "volte", 26: "volte", 15: "espere"}


def trilha():
    s = []
    cel, gap = 24, 5.5
    pos = []
    for n in range(30):
        l, c = divmod(n, 6)
        if l % 2:
            c = 5 - c
        pos.append((10 + c * (cel + gap), 8 + l * (cel + 12)))
    for (x1, y1), (x2, y2) in zip(pos, pos[1:]):
        s.append(f'<line x1="{x1 + cel / 2}" y1="{y1 + cel / 2}" x2="{x2 + cel / 2}" y2="{y2 + cel / 2}" stroke="#777" stroke-width="4" stroke-linecap="round"/>')
    for n, (x, y) in enumerate(pos, 1):
        fundo = "#fff1e8" if n in ESPECIAIS else "#fff"
        borda = 2 if n in ESPECIAIS else .9  # casa especial com borda grossa: aparece mesmo em P&B
        s.append(f'<rect x="{x}" y="{y}" width="{cel}" height="{cel}" rx="5" fill="{fundo}" stroke="{TRACO}" stroke-width="{borda}"/>')
        s.append(_txt(x + 4, y + 4.5, str(n), 4.6, 800, anchor="start", fonte="Baloo 2"))
        ic = {"avance": "estrela", "volte": "nuvem", "espere": "lua"}.get(ESPECIAIS.get(n))
        if ic:
            s.append(icone(ic, x + 7, y + 7, 14))
    x, y = pos[0]
    s.append(_txt(x + cel / 2, y + cel + 4, "INÍCIO", 4.4, 800, cor=LAR))
    x, y = pos[-1]
    s.append(_txt(x + cel / 2, y + cel + 4, "CHEGADA", 4.4, 800, cor=LAR))
    ly = 8 + 5 * (cel + 12) + 6
    for i, (ic, txt) in enumerate([("estrela", "avance 2 casas"), ("nuvem", "volte 2 casas"), ("lua", "espere uma rodada")]):
        x = 8 + i * 58
        s.append(icone(ic, x, ly, 12))
        s.append(_txt(x + 15, ly + 6, txt, 4.6, 700, anchor="start"))
    tab = "".join(s)
    # peões e dado de papel
    d = []
    for i, ic in enumerate(["estrela", "coracao", "sol", "lua"]):
        x = 10 + i * 42
        d.append(f'<circle cx="{x + 16}" cy="20" r="16" fill="#fff" stroke="#888" stroke-width=".6" stroke-dasharray="2 1.4"/>')
        d.append(icone(ic, x + 6, 10, 20))
    d.append(_txt(W / 2, 43, "Peões: recorte, pinte cada um de uma cor e cole numa tampinha.", 4.6, 700, cor="#555"))
    f, x0, y0 = 30, 30, 62
    faces = {(1, 0): 3, (0, 1): 2, (1, 1): 1, (2, 1): 5, (3, 1): 6, (1, 2): 4}
    pontos = {1: [(.5, .5)], 2: [(.25, .25), (.75, .75)], 3: [(.25, .25), (.5, .5), (.75, .75)],
              4: [(.25, .25), (.75, .25), (.25, .75), (.75, .75)], 5: [(.25, .25), (.75, .25), (.5, .5), (.25, .75), (.75, .75)],
              6: [(.25, .25), (.75, .25), (.25, .5), (.75, .5), (.25, .75), (.75, .75)]}
    assert faces[(1, 0)] + faces[(1, 2)] == 7 and faces[(0, 1)] + faces[(2, 1)] == 7 and faces[(1, 1)] + faces[(3, 1)] == 7

    def aba(xa, ya, xb, yb, dx, dy):
        k = 7
        return (f'<polygon points="{xa},{ya} {xb},{yb} {xb + dx * k + (xa - xb) * .2},{yb + dy * k + (ya - yb) * .2} '
                f'{xa + dx * k + (xb - xa) * .2},{ya + dy * k + (yb - ya) * .2}" fill="#f2f2f2" stroke="#888" stroke-width=".5" stroke-dasharray="2 1.4"/>')
    for (c, l) in [(0, 1), (2, 1), (3, 1)]:
        x, y = x0 + c * f, y0 + l * f
        d.append(aba(x, y, x + f, y, 0, -1))
        d.append(aba(x, y + f, x + f, y + f, 0, 1))
    x, y = x0 + 3 * f, y0 + f
    d.append(aba(x + f, y, x + f, y + f, 1, 0))
    for (c, l), v in faces.items():
        x, y = x0 + c * f, y0 + l * f
        d.append(f'<rect x="{x}" y="{y}" width="{f}" height="{f}" fill="#fff" stroke="{TRACO}" stroke-width=".8"/>')
        for px, py in pontos[v]:
            d.append(f'<circle cx="{x + px * f}" cy="{y + py * f}" r="2.6" fill="{TRACO}"/>')
    d.append(_txt(W / 2, y0 + 3 * f + 14, "Dado: recorte pela borda de fora, dobre em todas as linhas e cole as abas cinzas.", 4.6, 700, cor="#555"))
    d.append(_txt(W / 2, y0 + 3 * f + 22, "Se preferir, use um dado comum.", 4.6, 700, cor="#555"))
    return [("Trilha das figuras", "Tabuleiro para 2 a 4 jogadores. As regras estão na página de regras.", tab),
            ("Trilha: peões e dado de papel", "Monte com a ajuda de um adulto. Use tesoura sem ponta e cola branca.", "".join(d))]


# ------------------------------------------------------------------ jogo da velha
def velha():
    s = []
    for k in range(2):
        x0, y0 = 6 + k * 90, 4
        for i in (1, 2):
            s.append(f'<line x1="{x0 + i * 26}" y1="{y0}" x2="{x0 + i * 26}" y2="{y0 + 78}" stroke="{TRACO}" stroke-width="2" stroke-linecap="round"/>')
            s.append(f'<line x1="{x0}" y1="{y0 + i * 26}" x2="{x0 + 78}" y2="{y0 + i * 26}" stroke="{TRACO}" stroke-width="2" stroke-linecap="round"/>')
    s.append(tesoura_txt(92))
    for k, ic in enumerate(["estrela", "coracao"]):
        y = 104 + k * 56
        s.append(_txt(8, y, f"Peças de {'estrela' if ic == 'estrela' else 'coração'}:", 5.2, 800, anchor="start"))
        for i in range(5):
            x = 8 + i * 34
            s.append(caixa_corte(x + 5, y + 8, 20, 20, 3))  # peça menor que a casa do tabuleiro (26 mm)
            s.append(icone(ic, x + 7.5, y + 10.5, 15))
    return [("Jogo da velha das figuras", "Dois tabuleiros e 10 peças para recortar: 5 estrelas e 5 corações. Também dá para jogar desenhando com lápis.", "".join(s))]


REGRAS = """
  <h2>Bingo de figuras (2 a 6 jogadores)</h2>
  <p>Cada um pega uma cartela. Um adulto sorteia uma ficha do potinho e fala o nome da figura. Quem tiver a figura marca com um feijão.
  Ganha quem marcar uma linha inteira (ou a cartela toda, se combinarem antes).</p>
  <h2>Dominó de figuras (2 a 4 jogadores)</h2>
  <p>Vire as peças para baixo e cada um pega 7 (com 3 ou 4 jogadores, 5 cada). Quem tiver uma peça com a mesma figura dos dois lados começa. Se ninguém tiver, ou se mais de um tiver, começa o mais novo.
  Na sua vez, encaixe uma peça que tenha a mesma figura de uma das pontas. Sem peça para jogar, compre do monte ou passe a vez. Ganha quem acabar as peças primeiro.</p>
  <h2>Jogo da memória (2 ou mais jogadores)</h2>
  <p>Espalhe as cartas viradas para baixo. Na sua vez, vire duas. Se forem iguais, fique com o par e jogue de novo. Se não, desvire e passe a vez. Ganha quem tiver mais pares.
  Para os pequenos, comece com 6 pares.</p>
  <h2>Trilha das figuras (2 a 4 jogadores)</h2>
  <p>Todos começam no INÍCIO. Na sua vez, jogue o dado e ande as casas. Estrela: avance 2. Nuvem: volte 2. Lua: fique uma rodada sem jogar. Não precisa tirar o número exato: quem passar da casa 30 também chega. Ganha quem chegar primeiro.</p>
  <h2>Jogo da velha (2 jogadores)</h2>
  <p>Um fica com as estrelas e o outro com os corações. Cada um coloca uma peça por vez. Ganha quem fizer uma linha de 3: em pé, deitada ou na diagonal.</p>
  <p class="aviso">Uso permitido: imprima quantas vezes quiser para a sua família. Não é permitido revender nem repassar o arquivo.</p>"""


def gerar():
    rng = random.Random(SEMENTE)
    capa = BUMP.capa("Bingo, dominó, memória, trilha e jogo da velha. Tudo com figuras, para jogar junto na mesa.",
                     ("Para crianças de 4 a 10 anos e a família toda", "Regras na página 2"),
                     ["dado", "estrela", "coracao", "sol", "lua", "peixe", "flor", "casa"])
    pags = [capa, BUMP.pagina_texto("Regras dos 5 jogos", REGRAS, 2, selo="Regras")]
    bpags, _ = bingo(rng)
    todas = bpags + domino() + memoria(rng) + trilha() + velha()
    for titulo, instr, svg in todas:
        selo = titulo.split(":")[0].replace(" (continuação)", "")
        pags.append(pagina(titulo, instr, svg, len(pags) + 1, selo))
    return dict(paginas=BUMP.montar(pags), jogos=5)


if __name__ == "__main__":
    print(gerar())
