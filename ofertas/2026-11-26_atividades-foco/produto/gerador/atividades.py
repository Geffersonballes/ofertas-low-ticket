"""Geradores das atividades. Cada função devolve um dict:
  titulo, instrucao, nivel (1 ou 2), categoria, svg (conteúdo da área 182x228 mm),
  gabarito_svg (miniatura 182x228 com a resposta) ou gabarito_txt.
Tudo que tem resposta é calculado e conferido aqui (assert), nunca 'chutado'."""
import math
import random
from collections import deque
from itertools import permutations

from icones import icone, TRACO

W, H = 182, 228  # área útil da atividade em mm


def _txt(x, y, s, tam=6, peso=700, anchor="middle", cor=TRACO, fonte="Nunito"):
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{fonte}" font-size="{tam}" font-weight="{peso}" '
            f'text-anchor="{anchor}" fill="{cor}" dominant-baseline="central">{s}</text>')


# ---------------------------------------------------------------- labirinto
def _gera_labirinto(cols, lins, rng):
    paredes = {(c, l): {"N", "S", "L", "O"} for c in range(cols) for l in range(lins)}
    viz = {"N": (0, -1, "S"), "S": (0, 1, "N"), "L": (1, 0, "O"), "O": (-1, 0, "L")}
    pilha, vis = [(0, 0)], {(0, 0)}
    while pilha:
        c, l = pilha[-1]
        opc = [(d, c + dc, l + dl, op) for d, (dc, dl, op) in viz.items()
               if 0 <= c + dc < cols and 0 <= l + dl < lins and (c + dc, l + dl) not in vis]
        if not opc:
            pilha.pop(); continue
        d, nc, nl, op = rng.choice(opc)
        paredes[(c, l)].discard(d); paredes[(nc, nl)].discard(op)
        vis.add((nc, nl)); pilha.append((nc, nl))
    # caminho da solução (BFS)
    fim = (cols - 1, lins - 1)
    ant, fila = {(0, 0): None}, deque([(0, 0)])
    while fila:
        c, l = fila.popleft()
        for d, (dc, dl, _) in viz.items():
            n = (c + dc, l + dl)
            if d not in paredes[(c, l)] and n not in ant:
                ant[n] = (c, l); fila.append(n)
    assert fim in ant, "labirinto sem saída"
    cam, p = [], fim
    while p:
        cam.append(p); p = ant[p]
    return paredes, cam[::-1]


def _desenha_labirinto(paredes, cols, lins, x0, y0, cel, esp=0.9):
    s = []
    for (c, l), ps in paredes.items():
        x, y = x0 + c * cel, y0 + l * cel
        if "N" in ps and not (c == 0 and l == 0):
            s.append(f'<line x1="{x}" y1="{y}" x2="{x + cel}" y2="{y}"/>')
        if "O" in ps:
            s.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + cel}"/>')
        if c == cols - 1 and "L" in ps:
            s.append(f'<line x1="{x + cel}" y1="{y}" x2="{x + cel}" y2="{y + cel}"/>')
        if l == lins - 1 and "S" in ps and not (c == cols - 1):
            s.append(f'<line x1="{x}" y1="{y + cel}" x2="{x + cel}" y2="{y + cel}"/>')
    return f'<g stroke="{TRACO}" stroke-width="{esp}" stroke-linecap="round">{"".join(s)}</g>'


def labirinto(nivel, rng):
    cols, lins = (7, 9) if nivel == 1 else (15, 19)
    cel = min((W - 10) / cols, (H - 50) / lins)
    x0 = (W - cols * cel) / 2
    y0 = 25
    paredes, cam = _gera_labirinto(cols, lins, rng)
    ini, fim = ("passaro", "arvore") if nivel == 1 else ("barco", "casa")
    esp = 1.6 if nivel == 1 else 1.0
    base = (_desenha_labirinto(paredes, cols, lins, x0, y0, cel, esp)
            + icone(ini, x0 + cel / 2 - 11, y0 - 23, 22)
            + icone(fim, x0 + (cols - 0.5) * cel - 11, y0 + lins * cel + 1, 22))
    pts = " ".join(f"{x0 + (c + .5) * cel:.1f},{y0 + (l + .5) * cel:.1f}" for c, l in cam)
    sol = f'<polyline points="{pts}" fill="none" stroke="#ff7a45" stroke-width="{cel * .35:.1f}" stroke-linejoin="round" stroke-linecap="round" opacity=".8"/>'
    return dict(
        titulo="Labirinto" if nivel == 1 else "Labirinto desafio",
        instrucao=("Leve o passarinho até a árvore sem atravessar as paredes." if nivel == 1
                   else "Leve o barco até a casa. Use o dedo primeiro e depois o lápis."),
        nivel=nivel, categoria="Atenção",
        svg=base, gabarito_svg=sol + base)


# ---------------------------------------------------------------- padrões
def padroes(rng):
    linhas = [["circulo", "quadrado"], ["estrela", "estrela", "coracao"], ["sol", "lua", "nuvem"],
              ["peixe", "peixe", "maca", "maca"], ["triangulo", "losango", "losango"]]
    todos = ["circulo", "quadrado", "estrela", "coracao", "sol", "lua", "nuvem", "peixe", "maca",
             "triangulo", "losango", "flor"]
    s, gab, respostas = [], [], []
    alt = 45
    for i, ciclo in enumerate(linhas):
        y = 2 + i * alt
        seq = (ciclo * 4)[: 6]
        resp = (ciclo * 4)[6]
        tam = 18
        s.append(f'<rect x="1" y="{y}" width="{W - 2}" height="{alt - 5}" rx="4" fill="none" stroke="#bdbdbd" stroke-width=".5"/>')
        for j, nome in enumerate(seq):
            s.append(icone(nome, 6 + j * 22, y + 3, tam))
        bx = 6 + 6 * 22
        s.append(f'<rect x="{bx}" y="{y + 3}" width="{tam}" height="{tam}" rx="3" fill="none" stroke="{TRACO}" stroke-width=".8" stroke-dasharray="2 1.5"/>')
        s.append(_txt(bx + tam / 2, y + 3 + tam / 2, "?", 11, 800, fonte="Baloo 2"))
        opc = [resp] + rng.sample([t for t in todos if t != resp], 2)
        rng.shuffle(opc)
        respostas.append(opc.index(resp))
        oy = y + 24
        s.append(f'<rect x="68" y="{oy - 1}" width="{W - 72}" height="15" rx="3" fill="#f3f3f3"/>')
        s.append(_txt(64, oy + 6.5, "circule:", 4.8, 700, anchor="end", cor="#666"))
        for k, nome in enumerate(opc):
            ox = 80 + k * 32
            s.append(icone(nome, ox, oy, 13))
            if k == opc.index(resp):
                gab.append(f'<circle cx="{ox + 6.5}" cy="{oy + 6.5}" r="9" fill="none" stroke="#ff7a45" stroke-width="1.6"/>')
    base = "".join(s)
    return dict(titulo="O que vem depois?", nivel=1, categoria="Padrões",
                instrucao="Olhe a fila, descubra o que se repete e circule embaixo a figura que entra no ?.",
                svg=base, gabarito_svg=base + "".join(gab))


# ---------------------------------------------------------------- qual é diferente
def diferente(rng):
    linhas = [("peixe", dict(espelhar=True)), ("estrela", dict(variante="6pontas")),
              ("casa", dict(variante="semporta")), ("flor", dict(variante="4petalas")),
              ("triangulo", dict(girar=180)), ("maca", dict(variante="semfolha"))]
    s, gab = [], []
    for i, (nome, mud) in enumerate(linhas):
        y = 4 + i * 37
        k = rng.randrange(5)
        for j in range(5):
            x = 6 + j * 35
            s.append(icone(nome, x, y, 28, **(mud if j == k else {})))
            if j == k:
                gab.append(f'<circle cx="{x + 14}" cy="{y + 14}" r="17" fill="none" stroke="#ff7a45" stroke-width="1.6"/>')
        if i < len(linhas) - 1:
            s.append(f'<line x1="2" y1="{y + 33}" x2="{W - 2}" y2="{y + 33}" stroke="#ccc" stroke-width=".3"/>')
    base = "".join(s)
    return dict(titulo="Qual é diferente?", nivel=1, categoria="Atenção",
                instrucao="Em cada fila, uma figura está um pouquinho diferente. Encontre e circule.",
                svg=base, gabarito_svg=base + "".join(gab))


# ---------------------------------------------------------------- contar
def contar(rng):
    tipos = ["maca", "estrela", "peixe", "balao"]
    s, gab = [], []
    qtds = rng.sample(range(3, 11), 4)
    for i, (nome, n) in enumerate(zip(tipos, qtds)):
        px, py = (i % 2) * 92, (i // 2) * 112
        s.append(f'<rect x="{px + 1}" y="{py + 1}" width="88" height="106" rx="5" fill="none" stroke="{TRACO}" stroke-width=".7"/>')
        casas = [(c, l) for c in range(4) for l in range(3)]
        pos = [(px + 4 + c * 20 + rng.uniform(-1.5, 1.5), py + 5 + l * 23 + rng.uniform(-2, 2))
               for c, l in rng.sample(casas, n)]
        for x, y in pos:
            s.append(icone(nome, x, y, 18, girar=rng.choice([-12, 0, 10])))
        for k in range(10):
            cx, cy = px + 9 + (k % 5) * 17.5, py + 81 + (k // 5) * 12
            s.append(_txt(cx, cy, str(k + 1), 7, 800, fonte="Baloo 2"))
            if k + 1 == n:
                gab.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="none" stroke="#ff7a45" stroke-width="1.4"/>')
    base = "".join(s)
    return dict(titulo="Conte e circule", nivel=1, categoria="Atenção",
                instrucao="Conte as figuras de cada quadro e circule o número certo embaixo.",
                svg=base, gabarito_svg=base + "".join(gab))


# ---------------------------------------------------------------- ligue os pontos
def ligue_pontos(rng):
    # barquinho: casco + mastro + vela, num traçado só
    cantos = [(30, 150), (55, 185), (150, 185), (172, 150), (100, 150), (100, 25), (160, 135), (100, 135)]
    pts = []
    for (ax, ay), (bx, by) in zip(cantos, cantos[1:]):
        n = max(1, round(math.dist((ax, ay), (bx, by)) / 30))
        for t in range(n):
            pts.append((ax + (bx - ax) * t / n, ay + (by - ay) * t / n))
    pts.append(cantos[-1])
    cx = sum(p[0] for p in pts) / len(pts); cy = sum(p[1] for p in pts) / len(pts)
    s = []
    for i, (x, y) in enumerate(pts):
        dx, dy = x - cx, y - cy; d = math.hypot(dx, dy) or 1
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.6" fill="{TRACO}"/>')
        s.append(_txt(x + dx / d * 6, y + dy / d * 6, str(i + 1), 5.5, 800))
    s.append(icone("sol", 14, 14, 34))
    s.append(icone("nuvem", 120, 6, 36))
    for k in range(4):
        y = 203 + k * 6
        s.append(f'<path d="M6 {y} q 11 -5 22 0 t 22 0 t 22 0 t 22 0 t 22 0 t 22 0 t 22 0 t 22 0" fill="none" stroke="{TRACO}" stroke-width=".7"/>')
    base = "".join(s)
    linha = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    gab = f'<polyline points="{linha}" fill="none" stroke="#ff7a45" stroke-width="1.6"/>'
    return dict(titulo="Ligue os pontos", nivel=1, categoria="Traçado",
                instrucao=f"Ligue do 1 ao {len(pts)}, na ordem, e descubra o desenho. Depois pinte!",
                svg=base, gabarito_svg=gab + base)


# ---------------------------------------------------------------- traçado
def tracado(rng):
    pares = [("passaro", "arvore", "reta"), ("peixe", "barco", "onda"), ("sol", "nuvem", "zigue"),
             ("estrela", "lua", "laco"), ("maca", "casa", "ponte")]
    s = []
    for i, (a, b, tipo) in enumerate(pares):
        y = 22 + i * 44
        x1, x2 = 30, 150
        if tipo == "reta":
            d = f"M{x1} {y} L{x2} {y}"
        elif tipo == "onda":
            d = f"M{x1} {y} " + " ".join(f"q 7.5 {'-' if k % 2 == 0 else ''}14 15 0" for k in range(8))
        elif tipo == "zigue":
            d = f"M{x1} {y} " + " ".join(f"l 10 {'-' if k % 2 == 0 else ''}12" for k in range(12))
        elif tipo == "laco":
            d = f"M{x1} {y} " + " ".join("l 0 -12 l 10 0 l 0 12 l 10 0" for _ in range(6))
        else:
            d = f"M{x1} {y} " + " ".join("a 10 10 0 0 1 20 0" for _ in range(6))
        s.append(f'<path d="{d}" fill="none" stroke="#9a9a9a" stroke-width="1.3" stroke-dasharray="2.2 1.8" stroke-linecap="round"/>')
        s.append(f'<circle cx="{x1}" cy="{y}" r="2" fill="#ff7a45"/>')
        s.append(icone(a, 2, y - 12, 24))
        s.append(icone(b, 156, y - 12, 24))
    base = "".join(s)
    return dict(titulo="Siga o caminho", nivel=1, categoria="Traçado",
                instrucao="Comece na bolinha e passe o lápis por cima do pontilhado, sem tirar do papel.",
                svg=base, gabarito_txt="Atividade livre: vale qualquer traço que siga o pontilhado.")


# ---------------------------------------------------------------- sudoku 6x6
def _resolve(grade, conta=False, limite=2):
    """Backtracking 6x6 (caixas 2x3). Com conta=True devolve o nº de soluções (até `limite`)."""
    sols = [0]

    def ok(g, i, v):
        l, c = divmod(i, 6)
        if any(g[l * 6 + k] == v for k in range(6)) or any(g[k * 6 + c] == v for k in range(6)):
            return False
        bl, bc = l // 2 * 2, c // 3 * 3
        return all(g[(bl + a) * 6 + bc + b] != v for a in range(2) for b in range(3))

    def bt(g, ordem):
        try:
            i = g.index(0)
        except ValueError:
            sols[0] += 1
            return not conta or sols[0] >= limite
        for v in ordem():
            if ok(g, i, v):
                g[i] = v
                if bt(g, ordem):
                    return True
                g[i] = 0
        return False

    return bt, sols


def sudoku(rng):
    g = [0] * 36
    bt, _ = _resolve(g)
    bt(g, lambda: rng.sample(range(1, 7), 6))
    sol = g[:]
    puz = sol[:]
    for i in rng.sample(range(36), 36):
        v, puz[i] = puz[i], 0
        teste = puz[:]
        bt2, sols = _resolve(teste, conta=True)
        bt2(teste, lambda: range(1, 7))
        if sols[0] != 1:
            puz[i] = v
        if sum(1 for x in puz if x) <= 16:
            break
    t2 = puz[:]; bt3, s3 = _resolve(t2, conta=True); bt3(t2, lambda: range(1, 7))
    assert s3[0] == 1, "sudoku sem solução única"
    cel, x0, y0 = 26, (W - 156) / 2, 20

    def desenha(valores, destaque=None):
        s = []
        for i, v in enumerate(valores):
            l, c = divmod(i, 6)
            x, y = x0 + c * cel, y0 + l * cel
            if puz[i]:
                s.append(f'<rect x="{x}" y="{y}" width="{cel}" height="{cel}" fill="#eeeeee"/>')
            if v:
                cor = "#ff7a45" if (destaque and not puz[i]) else TRACO
                s.append(_txt(x + cel / 2, y + cel / 2 + .5, str(v), 13, 800, cor=cor, fonte="Baloo 2"))
        for k in range(7):
            e = 1.4 if k in (0, 6) else (1.2 if k % 3 == 0 else .4)
            s.append(f'<line x1="{x0 + k * cel}" y1="{y0}" x2="{x0 + k * cel}" y2="{y0 + 6 * cel}" stroke="{TRACO}" stroke-width="{e}"/>')
            e = 1.4 if k in (0, 6) else (1.2 if k % 2 == 0 else .4)
            s.append(f'<line x1="{x0}" y1="{y0 + k * cel}" x2="{x0 + 6 * cel}" y2="{y0 + k * cel}" stroke="{TRACO}" stroke-width="{e}"/>')
        return "".join(s)

    dica = _txt(W / 2, y0 + 6 * cel + 16, "Cada linha, cada coluna e cada quadradão de 6 casinhas tem 1, 2, 3, 4, 5 e 6.", 4.6, 600)
    return dict(titulo="Sudoku 6x6", nivel=2, categoria="Lógica",
                instrucao="Complete com números de 1 a 6 sem repetir na linha, na coluna nem no quadradão.",
                svg=desenha(puz) + dica, gabarito_svg=desenha(sol, True))


# ---------------------------------------------------------------- caça-palavras
def caca_palavras(rng):
    palavras = ["GATO", "CAVALO", "MACACO", "TATU", "PATO", "ZEBRA", "COELHO", "TUCANO"]
    n = 12
    for _ in range(500):
        g = [[""] * n for _ in range(n)]
        pos = {}
        okall = True
        for p in palavras:
            for _ in range(300):
                dl, dc = rng.choice([(0, 1), (1, 0), (1, 1)])
                l = rng.randrange(n - dl * (len(p) - 1)); c = rng.randrange(n - dc * (len(p) - 1))
                cel = [(l + dl * k, c + dc * k) for k in range(len(p))]
                if all(g[a][b] in ("", p[k]) for k, (a, b) in enumerate(cel)):
                    for k, (a, b) in enumerate(cel):
                        g[a][b] = p[k]
                    pos[p] = cel
                    break
            else:
                okall = False; break
        if okall:
            break
    letras = "AAAABCDEEEEFGHIIILMNOOOPRRSSTTUUV"
    for a in range(n):
        for b in range(n):
            if not g[a][b]:
                g[a][b] = rng.choice(letras)
    # cada palavra aparece exatamente uma vez
    for p in palavras:
        achou = 0
        for a in range(n):
            for b in range(n):
                for dl, dc in [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]:
                    if all(0 <= a + dl * k < n and 0 <= b + dc * k < n and g[a + dl * k][b + dc * k] == p[k] for k in range(len(p))):
                        achou += 1
        assert achou == 1, f"{p} aparece {achou} vezes"
    cel, x0, y0 = 13, (W - 156) / 2, 2
    s = [f'<rect x="{x0}" y="{y0}" width="{n * cel}" height="{n * cel}" rx="3" fill="none" stroke="{TRACO}" stroke-width="1"/>']
    for a in range(n):
        for b in range(n):
            s.append(_txt(x0 + b * cel + cel / 2, y0 + a * cel + cel / 2 + .4, g[a][b], 7.5, 800))
    ly = y0 + n * cel + 12
    for i, p in enumerate(palavras):
        x = 20 + (i % 4) * 42; y = ly + (i // 4) * 12
        s.append(f'<rect x="{x - 7}" y="{y - 2.5}" width="5" height="5" rx="1" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(_txt(x, y, p, 6, 800, anchor="start"))
    base = "".join(s)
    gab = []
    for p, cel_ in pos.items():
        (a1, b1), (a2, b2) = cel_[0], cel_[-1]
        gab.append(f'<line x1="{x0 + b1 * cel + cel / 2}" y1="{y0 + a1 * cel + cel / 2}" x2="{x0 + b2 * cel + cel / 2}" y2="{y0 + a2 * cel + cel / 2}" stroke="#ff7a45" stroke-width="8" stroke-linecap="round" opacity=".45"/>')
    return dict(titulo="Caça-palavras: bichos", nivel=2, categoria="Atenção",
                instrucao="Encontre os 8 bichos escondidos. Eles estão em linha reta: para o lado, para baixo ou na diagonal.",
                svg=base, gabarito_svg="".join(gab) + base)


# ---------------------------------------------------------------- código secreto
def codigo_secreto(rng):
    msg = "BRINCAR FAZ BEM"
    letras = sorted(set(msg.replace(" ", ""))) + ["O", "T"]
    simbolos = ["circulo", "quadrado", "triangulo", "estrela", "coracao", "losango", "lua",
                "nuvem", "peixe", "flor", "sol", "maca"]
    rng.shuffle(simbolos)
    chave = dict(zip(letras, simbolos))
    s = []
    # tabela-chave
    for i, (le, si) in enumerate(sorted(chave.items(), key=lambda kv: kv[0])):
        x = 6 + (i % 6) * 29; y = 2 + (i // 6) * 30
        s.append(f'<rect x="{x}" y="{y}" width="26" height="27" rx="3" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(icone(si, x + 6, y + 2, 14))
        s.append(_txt(x + 13, y + 21.5, le, 7.5, 800, fonte="Baloo 2"))
    # mensagem
    palavras = msg.split()
    y = 84
    gab = []
    for p in palavras:
        larg = len(p) * 22
        x = (W - larg) / 2
        for k, ch in enumerate(p):
            cx = x + k * 22
            s.append(icone(chave[ch], cx + 3, y, 16))
            s.append(f'<line x1="{cx + 1}" y1="{y + 30}" x2="{cx + 21}" y2="{y + 30}" stroke="{TRACO}" stroke-width=".7"/>')
            gab.append(_txt(cx + 11, y + 24, ch, 9, 800, cor="#ff7a45", fonte="Baloo 2"))
        y += 46
    base = "".join(s)
    return dict(titulo="Código secreto", nivel=2, categoria="Lógica",
                instrucao="Use a tabela para trocar cada figura por uma letra e descubra a mensagem.",
                svg=base, gabarito_svg=base + "".join(gab))


# ---------------------------------------------------------------- 7 erros
def _cena(dif):
    s = [f'<line x1="2" y1="70" x2="86" y2="70" stroke="{TRACO}" stroke-width=".8"/>']
    # sol
    raios = 7 if "sol" in dif else 8
    s.append(f'<circle cx="14" cy="13" r="5" fill="#fff" stroke="{TRACO}" stroke-width=".7"/>')
    for i in range(raios):
        a = i * 2 * math.pi / 8
        s.append(f'<line x1="{14 + 7 * math.cos(a):.1f}" y1="{13 + 7 * math.sin(a):.1f}" x2="{14 + 10 * math.cos(a):.1f}" y2="{13 + 10 * math.sin(a):.1f}" stroke="{TRACO}" stroke-width=".7"/>')
    # nuvem
    s.append(icone("nuvem", 46, 2 if "nuvem" not in dif else 5, 20 if "nuvem" not in dif else 14, traco=3.5))
    # casa
    s.append(f'<polygon points="20,40 36,26 52,40" fill="#fff" stroke="{TRACO}" stroke-width=".8"/>')
    if "chamine" not in dif:
        s.append(f'<rect x="42" y="27" width="5" height="9" fill="#fff" stroke="{TRACO}" stroke-width=".7"/>')
        s.append(f'<polygon points="20,40 36,26 52,40" fill="#fff" stroke="{TRACO}" stroke-width=".8"/>')
    s.append(f'<rect x="22" y="40" width="28" height="30" fill="#fff" stroke="{TRACO}" stroke-width=".8"/>')
    s.append(f'<rect x="32" y="54" width="8" height="16" fill="#fff" stroke="{TRACO}" stroke-width=".7"/>')
    if "macaneta" not in dif:
        s.append(f'<circle cx="38" cy="62" r=".8" fill="{TRACO}"/>')
    for wx, nome in [(25, "janela1"), (42, "janela2")]:
        s.append(f'<rect x="{wx}" y="44" width="6" height="6" fill="#fff" stroke="{TRACO}" stroke-width=".6"/>')
        if not (nome == "janela2" and "janela" in dif):
            s.append(f'<line x1="{wx + 3}" y1="44" x2="{wx + 3}" y2="50" stroke="{TRACO}" stroke-width=".4"/><line x1="{wx}" y1="47" x2="{wx + 6}" y2="47" stroke="{TRACO}" stroke-width=".4"/>')
    # árvore com maçãs
    s.append(f'<rect x="66" y="52" width="5" height="18" fill="#fff" stroke="{TRACO}" stroke-width=".7"/>')
    s.append(f'<circle cx="68.5" cy="42" r="13" fill="#fff" stroke="{TRACO}" stroke-width=".8"/>')
    macas = [(63, 38), (72, 36), (69, 46)]
    if "macas" in dif:
        macas = macas[:2]
    for mx, my in macas:
        s.append(f'<circle cx="{mx}" cy="{my}" r="1.8" fill="#d0d0d0" stroke="{TRACO}" stroke-width=".5"/>')
    # flores
    flores = [6, 12, 18] if "flor" not in dif else [6, 12]
    for fx in flores:
        s.append(f'<line x1="{fx}" y1="70" x2="{fx}" y2="63" stroke="{TRACO}" stroke-width=".5"/>')
        s.append(icone("flor", fx - 3, 58, 6, traco=6))
    # pássaro
    if "passaro" not in dif:
        s.append(icone("passaro", 66, 12, 11, traco=5))
    return "".join(s)


def sete_erros(rng):
    difs = ["sol", "nuvem", "chamine", "macaneta", "janela", "macas", "flor"]
    marcas = {"sol": (14, 13, 11), "nuvem": (54, 10, 10), "chamine": (44.5, 31, 6), "macaneta": (38, 62, 4),
              "janela": (45, 47, 5), "macas": (69, 46, 4), "flor": (18, 62, 6)}
    esc = 1.45
    def painel(y, dif, marcar=False):
        g = f'<g transform="translate({(W - 88 * esc) / 2},{y}) scale({esc})"><rect x="0" y="0" width="88" height="74" rx="3" fill="none" stroke="{TRACO}" stroke-width=".5"/>{_cena(dif)}'
        if marcar:
            g += "".join(f'<circle cx="{x}" cy="{yy}" r="{r}" fill="none" stroke="#ff7a45" stroke-width="1"/>' for x, yy, r in marcas.values())
        return g + "</g>"
    base = painel(0, set()) + painel(114, set(difs))
    assert len(difs) == 7
    return dict(titulo="Jogo dos 7 erros", nivel=2, categoria="Atenção",
                instrucao="Compare os dois desenhos e circule, no de baixo, as 7 diferenças.",
                svg=base, gabarito_svg=painel(0, set()) + painel(114, set(difs), True))


# ---------------------------------------------------------------- grade lógica
def grade_logica(rng):
    nomes = ["Ana", "Beto", "Caio"]
    frutas = [("maca", "maçã"), ("banana", "banana"), ("uva", "uva")]
    pistas = ["Ana não come banana.", "Beto adora uva."]
    regras = [lambda a: a["Ana"] != "banana", lambda a: a["Beto"] == "uva"]
    sols = [dict(zip(nomes, p)) for p in permutations([f[1] for f in frutas]) if all(r(dict(zip(nomes, p))) for r in regras)]
    assert len(sols) == 1, "grade lógica sem solução única"
    sol = sols[0]
    cel, x0, y0 = 30, 50, 76
    s = [_txt(8, 6, "Pistas:", 6.5, 800, anchor="start", fonte="Baloo 2")]
    for i, p in enumerate(pistas):
        s.append(_txt(12, 16 + i * 10, f"{i + 1}. {p}", 6, 700, anchor="start"))
    s.append(_txt(12, 36, "Cada criança come uma fruta diferente.", 5.6, 700, anchor="start"))
    for j, (ic, nm) in enumerate(frutas):
        s.append(icone(ic, x0 + j * cel + 5, y0 - 26, 20))
    for i, n in enumerate(nomes):
        s.append(_txt(x0 - 6, y0 + i * cel + cel / 2, n, 7.5, 800, anchor="end", fonte="Baloo 2"))
    for k in range(4):
        s.append(f'<line x1="{x0}" y1="{y0 + k * cel}" x2="{x0 + 3 * cel}" y2="{y0 + k * cel}" stroke="{TRACO}" stroke-width=".8"/>')
        s.append(f'<line x1="{x0 + k * cel}" y1="{y0}" x2="{x0 + k * cel}" y2="{y0 + 3 * cel}" stroke="{TRACO}" stroke-width=".8"/>')
    s.append(_txt(W / 2, y0 + 3 * cel + 10, "Marque X onde não pode e ● onde é certo.", 5.6, 700))
    yb = y0 + 3 * cel + 22
    for i, n in enumerate(nomes):
        s.append(_txt(36, yb + i * 13, f"{n} come", 6.5, 700, anchor="start"))
        s.append(f'<line x1="72" y1="{yb + i * 13 + 3}" x2="130" y2="{yb + i * 13 + 3}" stroke="{TRACO}" stroke-width=".6"/>')
    base = "".join(s)
    gab = []
    for i, n in enumerate(nomes):
        for j, (_, nm) in enumerate(frutas):
            cx, cy = x0 + j * cel + cel / 2, y0 + i * cel + cel / 2
            gab.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="#ff7a45"/>' if sol[n] == nm else _txt(cx, cy, "X", 10, 800, cor="#ff7a45"))
        gab.append(_txt(76, yb + i * 13, sol[n], 6.5, 800, anchor="start", cor="#ff7a45"))
    return dict(titulo="Quem come o quê?", nivel=2, categoria="Lógica",
                instrucao="Leia as pistas e descubra a fruta de cada criança.",
                svg=base, gabarito_svg=base + "".join(gab))


# ---------------------------------------------------------------- sequências numéricas
def sequencias(rng):
    seqs = [([2, 4, 6, 8, 10], "de 2 em 2"), ([5, 10, 15, 20, 25], "de 5 em 5"), ([1, 3, 5, 7, 9], "só os ímpares"),
            ([20, 18, 16, 14, 12], "diminui 2"), ([1, 2, 4, 8, 16], "dobra"), ([3, 6, 9, 12, 15], "de 3 em 3")]
    s, gab = [], []
    for i, (seq, regra) in enumerate(seqs):
        y = 6 + i * 36
        falta = 4 if i < 3 else rng.choice([1, 2, 3, 4])
        for k, v in enumerate(seq):
            x = 8 + k * 30
            s.append(f'<circle cx="{x + 11}" cy="{y + 11}" r="11" fill="{"#fff" if k != falta else "none"}" stroke="{TRACO}" stroke-width="{.8 if k != falta else .8}" {"stroke-dasharray=\"2 1.5\"" if k == falta else ""}/>')
            if k != falta:
                s.append(_txt(x + 11, y + 11.5, str(v), 10, 800, fonte="Baloo 2"))
            else:
                gab.append(_txt(x + 11, y + 11.5, str(v), 10, 800, cor="#ff7a45", fonte="Baloo 2"))
            if k < 4:
                s.append(_txt(x + 26, y + 11, "›", 9, 800, cor="#999"))
        s.append(_txt(160, y + 11, "regra:", 4.6, 700, cor="#666"))
        s.append(f'<line x1="150" y1="{y + 19}" x2="180" y2="{y + 19}" stroke="{TRACO}" stroke-width=".5"/>')
        gab.append(_txt(165, y + 16, regra, 4.2, 800, cor="#ff7a45"))
    base = "".join(s)
    return dict(titulo="Que número falta?", nivel=2, categoria="Padrões",
                instrucao="Descubra a regra de cada fila e escreva o número que falta no círculo pontilhado.",
                svg=base, gabarito_svg=base + "".join(gab))
