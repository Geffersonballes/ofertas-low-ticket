"""Atividades do bump "Matemática brincando" (área 182x228 mm). Tudo que tem resposta é calculado e
conferido com assert. Dinheiro só como "fichas" de desenho próprio (nada de cédula ou moeda do Real)."""
import random
import math

from atividades import W, H, _txt
from bumps_base import at, circ, LAR
from icones import icone, TRACO

FIGS = ["maca", "estrela", "peixe", "balao", "flor", "carro", "coracao", "sol", "uva", "barco", "pato", "bola", "pipa", "gato", "lua", "casa"]
PRODUTOS = [("maca", "maçã"), ("banana", "banana"), ("uva", "uva"), ("sorvete", "sorvete"), ("bola", "bola"), ("pipa", "pipa"),
            ("dado", "dado"), ("balao", "balão"), ("lapis", "lápis"), ("copo", "copo"), ("carro", "carrinho"), ("barco", "barquinho")]
CAT = "Números"


def caixa(x, y, w=16, h=14):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" rx="3" fill="#fff" stroke="{TRACO}" stroke-width=".8"/>'


def resp(x, y, v, tam=8):
    return _txt(x, y, str(v), tam, 800, cor=LAR, fonte="Baloo 2")


def ficha(x, y, v, r=7):
    """Ficha de brincar: círculo com estrela e o valor. Desenho próprio, não lembra moeda real."""
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{TRACO}" stroke-width=".7"/>'
            f'<circle cx="{x}" cy="{y}" r="{r - 1.6}" fill="none" stroke="{TRACO}" stroke-width=".3" stroke-dasharray="1 .8"/>'
            + _txt(x, y + .3, str(v), r * .95, 800, fonte="Baloo 2"))


def grupo(nome, n, x, y, larg, tam=11, cols=5):
    s = ""
    for i in range(n):
        s += icone(nome, x + (i % cols) * (tam + 1.5), y + (i // cols) * (tam + 1.5), tam)
    return s


# ======================================================================= NÍVEL 1
def conte_escreva(rng, faixa):
    a, b = faixa
    s, g = [], []
    qs = [rng.randint(a, b) for _ in range(6)]
    figs = rng.sample(FIGS, 6)
    for i, (q, f) in enumerate(zip(qs, figs)):
        x, y = (i % 2) * 92, (i // 2) * 74
        s.append(f'<rect x="{x + 1}" y="{y + 1}" width="88" height="70" rx="5" fill="none" stroke="{TRACO}" stroke-width=".7"/>')
        s.append(grupo(f, q, x + 6, y + 6, 76, 13.5))
        s.append(_txt(x + 44, y + 55, "quantos?", 4.6, 700, cor="#666"))
        s.append(caixa(x + 60, y + 50))
        g.append(resp(x + 68, y + 57, q))
    base = "".join(s)
    return at("Conte e escreva", "Conte as figuras de cada quadro e escreva o número na caixinha.", 1, CAT, base, base + "".join(g))


def soma_figuras(rng, maxi):
    s, g = [], []
    for i in range(4):
        a = rng.randint(1, maxi - 1); b = rng.randint(1, maxi - a)
        assert a + b <= maxi
        f = rng.choice(FIGS)
        y = 4 + i * 56
        s.append(f'<rect x="1" y="{y}" width="{W - 2}" height="50" rx="5" fill="none" stroke="#bbb" stroke-width=".5"/>')
        s.append(grupo(f, a, 6, y + 8, 60, 10, 5))
        s.append(_txt(70, y + 20, "+", 12, 800, fonte="Baloo 2"))
        s.append(grupo(f, b, 78, y + 8, 60, 10, 5))
        s.append(_txt(142, y + 20, "=", 12, 800, fonte="Baloo 2"))
        s.append(caixa(152, y + 12, 22, 18))
        s.append(_txt(36, y + 42, str(a), 7, 800, cor="#999", fonte="Baloo 2"))
        s.append(_txt(108, y + 42, str(b), 7, 800, cor="#999", fonte="Baloo 2"))
        g.append(resp(163, y + 21, a + b, 10))
    base = "".join(s)
    return at("Quantos ao todo?", "Junte os dois grupos, conte tudo e escreva o total na caixinha.", 1, CAT, base, base + "".join(g))


def subtrai_figuras(rng, maxi):
    s, g = [], []
    for i in range(4):
        a = rng.randint(3, maxi); b = rng.randint(1, a - 1)
        f = rng.choice(FIGS)
        y = 4 + i * 56
        s.append(f'<rect x="1" y="{y}" width="{W - 2}" height="50" rx="5" fill="none" stroke="#bbb" stroke-width=".5"/>')
        for k in range(a):
            x, yy = 8 + (k % 5) * 16, y + 6 + (k // 5) * 18
            s.append(icone(f, x, yy, 13))
            if k >= a - b:
                s.append(f'<path d="M{x - 1} {yy - 1} L{x + 14} {yy + 14} M{x + 14} {yy - 1} L{x - 1} {yy + 14}" stroke="{TRACO}" stroke-width="1.2"/>')
        s.append(_txt(120, y + 25, f"{a} − {b} =", 9, 800, fonte="Baloo 2"))
        s.append(caixa(150, y + 16, 22, 18))
        g.append(resp(161, y + 25, a - b, 10))
    base = "".join(s)
    return at("Quantos sobram?", "As figuras com X foram embora. Conte as que sobraram e escreva na caixinha.", 1, CAT, base, base + "".join(g))


def onde_mais(rng):
    s, g = [], []
    for i in range(4):
        a, b = rng.sample(range(2, 10), 2)
        f1, f2 = rng.sample(FIGS, 2)
        y = 4 + i * 56
        for k, (n, f) in enumerate([(a, f1), (b, f2)]):
            x = 2 + k * 92
            s.append(f'<rect x="{x}" y="{y}" width="86" height="50" rx="5" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
            s.append(grupo(f, n, x + 6, y + 6, 70, 12, 5))
            if n == max(a, b):
                g.append(f'<rect x="{x - 1.5}" y="{y - 1.5}" width="89" height="53" rx="6" fill="none" stroke="{LAR}" stroke-width="1.6"/>')
    base = "".join(s)
    return at("Onde tem mais?", "Em cada linha, conte os dois quadros e circule o que tem mais figuras.", 1, CAT, base, base + "".join(g))


def ligue_quantidade(rng):
    nums = rng.sample(range(1, 10), 5)
    direita = nums[:]
    rng.shuffle(direita)
    s, g = [], []
    for i, n in enumerate(nums):
        y = 6 + i * 44
        f = rng.choice(FIGS)
        s.append(f'<rect x="2" y="{y}" width="80" height="38" rx="5" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(grupo(f, n, 8, y + 5, 70, 11, 5))
        s.append(f'<circle cx="88" cy="{y + 19}" r="1.8" fill="{TRACO}"/>')
    for j, n in enumerate(direita):
        y = 6 + j * 44
        s.append(f'<circle cx="142" cy="{y + 19}" r="1.8" fill="{TRACO}"/>')
        s.append(_txt(160, y + 19, str(n), 16, 800, fonte="Baloo 2"))
    for i, n in enumerate(nums):
        j = direita.index(n)
        g.append(f'<line x1="88" y1="{6 + i * 44 + 19}" x2="142" y2="{6 + j * 44 + 19}" stroke="{LAR}" stroke-width="1.4"/>')
    base = "".join(s)
    return at("Ligue ao número", "Conte cada grupo e ligue com uma linha ao número certo.", 1, CAT, base, base + "".join(g))


def complete_numeros(rng, ate):
    s, g = [], []
    linhas = 2 if ate <= 10 else 4
    por = 10
    for l in range(linhas):
        ini = 1 + l * por
        faltam = set(rng.sample(range(por), 3 if ate <= 10 else 4))
        y = 14 + l * 52
        for k in range(por):
            v = ini + k
            x = 3 + k * 17.7
            s.append(f'<rect x="{x}" y="{y}" width="15" height="15" rx="3" fill="#fff" stroke="{TRACO}" stroke-width=".7" {"stroke-dasharray=\"2 1.3\"" if k in faltam else ""}/>')
            if k in faltam:
                g.append(resp(x + 7.5, y + 7.8, v, 7))
            else:
                s.append(_txt(x + 7.5, y + 7.8, str(v), 7, 800, fonte="Baloo 2"))
        s.append(icone(rng.choice(["passaro", "pato", "gato", "carro"]), 2, y - 13, 11))
    if ate <= 10:
        s.append(_txt(W / 2, 143, "Terminou? Pinte as figuras:", 6, 800))
        for k, f in enumerate(rng.sample(FIGS, 5)):
            s.append(icone(f, 15 + k * 34, 150, 22))
    base = "".join(s)
    ultimo = linhas * por  # a instrução diz até onde a folha vai de verdade (antes dizia 10 numa folha até 20)
    return at("Complete os números", f"Escreva os números que faltam nas casinhas pontilhadas, de 1 até {ultimo}.", 1, CAT, base, base + "".join(g))


def mercadinho1(rng):
    s, g = [], []
    itens = rng.sample(PRODUTOS, 4)
    for i, (ic, nome) in enumerate(itens):
        preco = rng.randint(1, 6)
        y = 4 + i * 56
        s.append(f'<rect x="1" y="{y}" width="{W - 2}" height="50" rx="5" fill="none" stroke="#bbb" stroke-width=".5"/>')
        s.append(icone(ic, 6, y + 8, 30))
        s.append(f'<rect x="40" y="{y + 14}" width="26" height="16" rx="3" fill="#fff1e8" stroke="{TRACO}" stroke-width=".7"/>')
        s.append(_txt(53, y + 22, f"{preco} fichas" if preco > 1 else "1 ficha", 4.4, 800))
        for k in range(7):
            cx = 82 + k * 13.5
            s.append(ficha(cx, y + 25, 1, 6))
            if k < preco:
                g.append(circ(cx, y + 25, 7.4, 1.3))
    base = "".join(s)
    return at("Brincando de mercadinho", "Veja o preço de cada coisa e circule as fichas que você precisa para pagar.", 1, CAT, base, base + "".join(g))


# ======================================================================= NÍVEL 2
CONTAS_USADAS = set()  # nenhuma conta repete entre as folhas de contas do bump


def contas(rng, op, maxi):
    s, g = [], []
    vistos = set()
    while len(vistos) < 12:
        if op == "+":
            a = rng.randint(1, maxi - 1); b = rng.randint(1, maxi - a); r = a + b
        else:
            a = rng.randint(2, maxi); b = rng.randint(1, a - 1); r = a - b
        vistos.add((a, b, r))
    ordem = sorted(vistos, key=lambda t: rng.random())  # gasta o rng principal como antes (as outras páginas não mudam)
    if maxi > 10:
        # folhas depois do aquecimento: toda conta tem um número de 10 para cima (soma: uma parcela >= 10;
        # diminuir: o primeiro número >= 11). Sorteadas num rng derivado, sem repetir conta no bump.
        alt = random.Random(f"contas-{op}-{maxi}-{len(CONTAS_USADAS)}")
        novas = []
        while len(novas) < 12:
            if op == "+":
                a = alt.randint(1, maxi - 1); b = alt.randint(1, maxi - a)
                ok = max(a, b) >= 10
            else:
                a = alt.randint(11, maxi); b = alt.randint(2, a - 1)
                ok = True
            r = a + b if op == "+" else a - b
            if ok and (op, a, b) not in CONTAS_USADAS and r not in {x[2] for x in novas if x[:2] == (a, b)}:
                CONTAS_USADAS.add((op, a, b)); novas.append((a, b, r))
        ordem = novas
    for i, (a, b, r) in enumerate(ordem):
        x, y = (i % 2) * 92, (i // 2) * 37
        s.append(f'<rect x="{x + 2}" y="{y + 2}" width="86" height="31" rx="5" fill="none" stroke="#bbb" stroke-width=".5"/>')
        s.append(_txt(x + 36, y + 17.5, f"{a} {'+' if op == '+' else '−'} {b} =", 9.5, 800, fonte="Baloo 2"))
        s.append(caixa(x + 62, y + 9, 22, 17))
        g.append(resp(x + 73, y + 17.5, r, 10))
        assert r == (a + b if op == "+" else a - b)
    base = "".join(s)
    tit = "Contas de somar" if op == "+" else "Contas de diminuir"
    instr = "Resolva cada conta e escreva o resultado na caixinha. Pode usar os dedos ou desenhar bolinhas."
    if maxi <= 10:
        tit += " (aquecimento)"
        instr = "Aquecimento com contas até 10. " + instr
    return at(tit, instr, 2, CAT, base, base + "".join(g))


def compara(rng, maxi):
    s, g = [], []
    for i in range(10):
        if rng.random() < .15:
            a = b = rng.randint(2, maxi)
        else:
            a, b = rng.sample(range(1, maxi + 1), 2)
        x, y = (i % 2) * 92, (i // 2) * 44
        s.append(f'<rect x="{x + 2}" y="{y + 2}" width="86" height="38" rx="5" fill="none" stroke="#bbb" stroke-width=".5"/>')
        s.append(_txt(x + 22, y + 21, str(a), 12, 800, fonte="Baloo 2"))
        s.append(f'<circle cx="{x + 45}" cy="{y + 21}" r="8" fill="#fff" stroke="{TRACO}" stroke-width=".8"/>')
        s.append(_txt(x + 68, y + 21, str(b), 12, 800, fonte="Baloo 2"))
        sinal = ">" if a > b else ("<" if a < b else "=")
        g.append(_txt(x + 45, y + 21.5, sinal, 10, 800, cor=LAR, fonte="Baloo 2"))
    s.append(_txt(W / 2, 224, "> maior que     < menor que     = igual", 5.4, 800, cor="#555"))
    base = "".join(s)
    return at("Maior, menor ou igual?", "Escreva no círculo o sinal certo: > (maior), < (menor) ou = (igual).", 2, CAT, base, base + "".join(g))


def piramide(rng, maxbase):
    s, g = [], []
    for p in range(2):
        base4 = [rng.randint(1, maxbase) for _ in range(4)]
        niveis = [base4]
        while len(niveis[-1]) > 1:
            ant = niveis[-1]
            niveis.append([ant[k] + ant[k + 1] for k in range(len(ant) - 1)])
        assert niveis[-1][0] == base4[0] + 3 * base4[1] + 3 * base4[2] + base4[3]
        bw, bh = 34, 18
        y0 = 4 + p * 112
        for n, linha in enumerate(niveis):
            y = y0 + (3 - n) * (bh + 2)
            x0 = (W - len(linha) * bw) / 2
            for k, v in enumerate(linha):
                x = x0 + k * bw
                s.append(f'<rect x="{x}" y="{y}" width="{bw - 2}" height="{bh}" rx="3" fill="{"#fff7f1" if n == 0 else "#fff"}" stroke="{TRACO}" stroke-width=".8"/>')
                if n == 0:
                    s.append(_txt(x + bw / 2 - 1, y + bh / 2 + .5, str(v), 8, 800, fonte="Baloo 2"))
                else:
                    g.append(resp(x + bw / 2 - 1, y + bh / 2 + .5, v, 8))
        if p == 0:
            s.append(f'<line x1="10" y1="{y0 + 4 * (bh + 2) + 12}" x2="{W - 10}" y2="{y0 + 4 * (bh + 2) + 12}" stroke="#ddd" stroke-width=".5"/>')
    base = "".join(s)
    return at("Pirâmide de somas", "Cada tijolo é a soma dos dois tijolos de baixo. Comece pela base e suba até o topo.", 2, CAT, base, base + "".join(g))


def dezenas(rng):
    s, g = [], []
    for i in range(6):
        d, u = rng.randint(1, 4), rng.randint(0, 9)
        x, y = (i % 2) * 92, (i // 2) * 74
        s.append(f'<rect x="{x + 2}" y="{y + 2}" width="86" height="68" rx="5" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
        for k in range(d):
            bx = x + 8 + k * 7
            for q in range(10):
                s.append(f'<rect x="{bx}" y="{y + 6 + q * 3.8}" width="5" height="3.8" fill="#fff" stroke="{TRACO}" stroke-width=".4"/>')
        for q in range(u):
            s.append(f'<rect x="{x + 50 + (q % 3) * 6}" y="{y + 16 + (q // 3) * 6}" width="5" height="5" fill="#fff" stroke="{TRACO}" stroke-width=".4"/>')
        s.append(_txt(x + 15, y + 50, "dezenas", 4.2, 700, cor="#666"))
        s.append(caixa(x + 6, y + 53, 18, 12))
        s.append(_txt(x + 39, y + 50, "unidades", 4.2, 700, cor="#666"))
        s.append(caixa(x + 30, y + 53, 18, 12))
        s.append(_txt(x + 70, y + 50, "número", 4.2, 700, cor="#666"))
        s.append(caixa(x + 58, y + 53, 24, 12))
        g.append(resp(x + 15, y + 59.3, d, 7)); g.append(resp(x + 39, y + 59.3, u, 7)); g.append(resp(x + 70, y + 59.3, 10 * d + u, 8))
    base = "".join(s)
    return at("Dezenas e unidades", "Cada barra tem 10 quadradinhos (uma dezena). Cada quadradinho solto é uma unidade. Escreva quantas tem e o número.",
              2, CAT, base, base + "".join(g))


NOMES_KIDS = ["Ana", "Léo", "Bia", "Davi", "Lia", "Rui", "Nina", "Théo", "Malu", "Caio"]


def mercadinho2(rng):
    itens = rng.sample(PRODUTOS, 6)
    precos = {nome: rng.randint(2, 9) for _, nome in itens}
    s, g = [], []
    for i, (ic, nome) in enumerate(itens):
        x, y = 4 + (i % 3) * 59, 2 + (i // 3) * 36
        s.append(f'<rect x="{x}" y="{y}" width="56" height="32" rx="4" fill="#fff" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(icone(ic, x + 3, y + 4, 22))
        s.append(_txt(x + 40, y + 11, nome, 4.6, 800))
        s.append(_txt(x + 40, y + 21, f"{precos[nome]} fichas", 5.4, 800, cor=TRACO))  # preço em preto: em P&B o laranja ficava claro
    probs = []
    nomes = [n for _, n in itens]
    a, b = rng.sample(nomes, 2)
    probs.append((f"{rng.choice(NOMES_KIDS)} comprou {_art(a)} e {_art(b)}. Quantas fichas gastou?", precos[a] + precos[b]))
    c = rng.choice(nomes); tinha = rng.randint(precos[c] + 1, 20)
    probs.append((f"{rng.choice(NOMES_KIDS)} tinha {tinha} fichas e comprou {_art(c)}. Quantas sobraram?", tinha - precos[c]))
    d = rng.choice(nomes)
    probs.append((f"Quanto custam 2 {_plural(d)}?", 2 * precos[d]))
    pares = [(e, f) for e in nomes for f in nomes if precos[e] > precos[f]]
    assert pares
    e, f = rng.choice(pares)
    probs.append((f"Quantas fichas {_art(e)} custa a mais que {_art(f)}?", precos[e] - precos[f]))
    h1, h2, h3 = rng.sample(nomes, 3)
    probs.append((f"Quanto custam {_art(h1)}, {_art(h2)} e {_art(h3)} juntos?", precos[h1] + precos[h2] + precos[h3]))
    for i, (q, r) in enumerate(probs):
        y = 82 + i * 29
        s.append(_txt(4, y, f"{i + 1}. {q}", 5.2, 700, anchor="start"))
        s.append(caixa(150, y + 4, 26, 13))
        s.append(_txt(146, y + 10.5, "=", 6, 800))
        g.append(resp(163, y + 10.5, r, 8))
        assert r >= 0
    base = "".join(s)
    return at("Mercadinho das fichas", "Use a tabela de preços para responder. Pode fazer as contas num cantinho da folha.", 2, CAT, base, base + "".join(g))


FEM = {"maçã", "banana", "uva", "bola", "pipa"}


def _art(nome):
    return ("a " if nome in FEM else "o ") + nome


def _plural(nome):
    return {"maçã": "maçãs", "banana": "bananas", "uva": "cachos de uva", "sorvete": "sorvetes", "bola": "bolas", "pipa": "pipas",
            "dado": "dados", "balão": "balões", "lápis": "lápis", "copo": "copos", "carrinho": "carrinhos", "barquinho": "barquinhos"}[nome]


def grupos_iguais(rng):
    s, g = [], []
    for i in range(3):
        n, k = rng.randint(2, 5), rng.randint(2, 5)
        f = rng.choice(FIGS)
        y = 4 + i * 74
        s.append(f'<rect x="1" y="{y}" width="{W - 2}" height="68" rx="5" fill="none" stroke="#bbb" stroke-width=".5"/>')
        for gi in range(n):
            gx = 6 + gi * 33
            s.append(f'<ellipse cx="{gx + 14}" cy="{y + 24}" rx="15" ry="19" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
            for j in range(k):
                s.append(icone(f, gx + 4 + (j % 2) * 10, y + 8 + (j // 2) * 10, 9))
        s.append(_txt(6, y + 54, f"{n} grupos de {k} =", 7, 800, anchor="start", fonte="Baloo 2"))
        s.append(caixa(64, y + 46, 22, 15))
        s.append(_txt(110, y + 54, f"{n} × {k} =", 7, 800, fonte="Baloo 2"))
        s.append(caixa(130, y + 46, 22, 15))
        g.append(resp(75, y + 54, n * k)); g.append(resp(141, y + 54, n * k))
    base = "".join(s)
    return at("Grupos iguais", "Conte quantos tem em cada grupo e quantos grupos são. Escreva o total.", 2, CAT, base, base + "".join(g))


def adivinha(rng):
    s, g = [], []
    usados = set()
    pistas = []
    while len(pistas) < 6:
        tipo = rng.choice(["dobro", "depois", "antes", "mais", "menos", "entre", "dezena"])
        if tipo == "dobro":
            x = rng.randint(2, 10); r = 2 * x; t = f"Sou o dobro de {x}."
        elif tipo == "depois":
            x = rng.randint(5, 40); r = x + 1; t = f"Venho logo depois do {x}."
        elif tipo == "antes":
            x = rng.randint(5, 40); r = x - 1; t = f"Venho logo antes do {x}."
        elif tipo == "mais":
            x, k = rng.randint(3, 20), rng.randint(2, 9); r = x + k; t = f"Sou {k} a mais que {x}."
        elif tipo == "menos":
            x, k = rng.randint(10, 30), rng.randint(2, 9); r = x - k; t = f"Sou {k} a menos que {x}."
        elif tipo == "entre":
            x = rng.randint(3, 40); r = x + 1; t = f"Estou entre o {x} e o {x + 2}."
        else:
            d, u = rng.randint(1, 5), rng.randint(1, 9); r = 10 * d + u; t = f"Tenho {d} dezena{'s' if d > 1 else ''} e {u} unidade{'s' if u > 1 else ''}."
        if r in usados:
            continue
        usados.add(r); pistas.append((t, r))
    for i, (t, r) in enumerate(pistas):
        y = 4 + i * 37
        s.append(f'<rect x="1" y="{y}" width="{W - 2}" height="32" rx="5" fill="#fff" stroke="#bbb" stroke-width=".5"/>')
        s.append(icone(rng.choice(["balao", "estrela", "pipa", "bola"]), 5, y + 6, 18))
        s.append(_txt(28, y + 16, t, 6.2, 800, anchor="start"))
        s.append(caixa(150, y + 8, 26, 16))
        g.append(resp(163, y + 16, r, 9))
    base = "".join(s)
    return at("Que número sou eu?", "Leia cada pista e descubra o número. Escreva na caixinha.", 2, CAT, base, base + "".join(g))


def dinheirinho():
    """Folha de fichas de brincar para recortar (não é atividade)."""
    s = []
    for i, v in enumerate([1] * 12 + [2] * 8 + [5] * 6 + [10] * 4):
        x, y = 8 + (i % 6) * 29, 6 + (i // 6) * 32
        s.append(f'<rect x="{x - 2}" y="{y - 2}" width="28" height="28" rx="3" fill="none" stroke="#aaa" stroke-width=".4" stroke-dasharray="2 1.4"/>')
        s.append(ficha(x + 12, y + 12, v, 11))
    s.append(_txt(W / 2, 172, "Fichas de brincar. Não são dinheiro de verdade.", 5.2, 800, cor="#666"))
    s.append(_txt(W / 2, 182, "Recorte, separe por valor e use nas atividades de mercadinho.", 5.2, 700, cor="#666"))
    return "".join(s)
