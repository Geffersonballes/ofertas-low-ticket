"""Atividades parametrizadas do caderno completo (variedade + dificuldade crescente).
Mesmo contrato do atividades.py: cada função devolve dict com titulo, instrucao, nivel, categoria,
tipo, svg e gabarito_svg (ou gabarito_txt). Toda resposta é calculada e conferida com assert."""
import math
import random
from itertools import permutations, product

from icones import icone, TRACO
from atividades import W, H, _txt, _gera_labirinto, _desenha_labirinto

LAR = "#ff7a45"


def _circ(cx, cy, r, esp=1.6):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" stroke="{LAR}" stroke-width="{esp}"/>'


def _at(titulo, instrucao, nivel, categoria, tipo, svg, gab=None, gab_txt=None):
    d = dict(titulo=titulo, instrucao=instrucao, nivel=nivel, categoria=categoria, tipo=tipo, svg=svg)
    if gab is not None:
        d["gabarito_svg"] = gab
    else:
        d["gabarito_txt"] = gab_txt
    return d


# ======================================================================= LÓGICA
def _curvas(cam):
    dirs = [(b[0] - a[0], b[1] - a[1]) for a, b in zip(cam, cam[1:])]
    return sum(1 for d1, d2 in zip(dirs, dirs[1:]) if d1 != d2)


def labirinto_bom(cols, lins, rng):
    """Gera com o rng principal (a sequência das outras páginas não muda). Se o caminho sair trivial
    (quase reto, com menos de 3 curvas, sem usar o miolo), gera de novo com um rng derivado até ter desafio."""
    paredes, cam = _gera_labirinto(cols, lins, rng)
    k = 0
    while _curvas(cam) < 3:  # ex.: descer a coluna da esquerda e seguir a última linha
        k += 1
        assert k < 200, "labirinto sem desafio"
        paredes, cam = _gera_labirinto(cols, lins, random.Random(f"lab-{cols}x{lins}-{len(cam)}-{k}"))
    return paredes, cam


def labirinto(nivel, rng, cols, lins, ini="passaro", fim="arvore"):
    cel = min((W - 10) / cols, (H - 52) / lins)
    x0 = (W - cols * cel) / 2
    y0 = 25
    paredes, cam = labirinto_bom(cols, lins, rng)
    esp = 1.8 if cel > 18 else (1.4 if cel > 12 else 1.0)
    base = (_desenha_labirinto(paredes, cols, lins, x0, y0, cel, esp)
            + icone(ini, x0 + cel / 2 - 11, y0 - 23, 22)
            + icone(fim, x0 + (cols - 0.5) * cel - 11, y0 + lins * cel + 1, 22))
    pts = " ".join(f"{x0 + (c + .5) * cel:.1f},{y0 + (l + .5) * cel:.1f}" for c, l in cam)
    sol = f'<polyline points="{pts}" fill="none" stroke="{LAR}" stroke-width="{cel * .35:.1f}" stroke-linejoin="round" stroke-linecap="round" opacity=".8"/>'
    nomes = {"passaro": "o passarinho", "barco": "o barco", "peixe": "o peixe", "carro": "o carro", "balao": "o balão"}
    destinos = {"arvore": "a árvore", "casa": "a casa", "nuvem": "a nuvem", "flor": "a flor", "estrela": "a estrela"}
    instr = (f"Leve {nomes[ini]} até {destinos[fim]} sem atravessar as paredes." if nivel == 1
             else f"Leve {nomes[ini]} até {destinos[fim]}. Use o dedo primeiro e depois o lápis.")
    return _at("Labirinto", instr, nivel, "Lógica", "labirinto", base, sol + base)


def _resolve_n(g, n, bl, bc, limite=2):
    """Conta soluções (até `limite`) de um sudoku n x n com caixas bl x bc. g é lista (0 = vazio)."""
    sols = [0]

    def ok(i, v):
        l, c = divmod(i, n)
        if any(g[l * n + k] == v for k in range(n)) or any(g[k * n + c] == v for k in range(n)):
            return False
        a, b = l // bl * bl, c // bc * bc
        return all(g[(a + x) * n + b + y] != v for x in range(bl) for y in range(bc))

    def bt():
        try:
            i = g.index(0)
        except ValueError:
            sols[0] += 1
            return sols[0] >= limite
        for v in range(1, n + 1):
            if ok(i, v):
                g[i] = v
                if bt():
                    g[i] = 0
                    return True
                g[i] = 0
        return False

    bt()
    return sols[0]


def _sudoku_gera(rng, n, bl, bc, dicas):
    g = [0] * (n * n)

    def preenche(i=0):
        if i == n * n:
            return True
        l, c = divmod(i, n)
        for v in rng.sample(range(1, n + 1), n):
            a, b = l // bl * bl, c // bc * bc
            if (all(g[l * n + k] != v for k in range(n)) and all(g[k * n + c] != v for k in range(n))
                    and all(g[(a + x) * n + b + y] != v for x in range(bl) for y in range(bc))):
                g[i] = v
                if preenche(i + 1):
                    return True
                g[i] = 0
        return False

    assert preenche()
    sol = g[:]
    puz = sol[:]
    for i in rng.sample(range(n * n), n * n):
        if sum(1 for x in puz if x) <= dicas:
            break
        v, puz[i] = puz[i], 0
        if _resolve_n(puz[:], n, bl, bc) != 1:
            puz[i] = v
    assert _resolve_n(puz[:], n, bl, bc) == 1
    return puz, sol


def sudoku_figuras(rng, dicas=9):
    """Nível 1: 4x4 com figuras (sem números)."""
    figs = rng.sample(["circulo", "estrela", "coracao", "quadrado", "triangulo", "sol"], 4)
    puz, sol = _sudoku_gera(rng, 4, 2, 2, dicas)
    cel, x0, y0 = 36, (W - 144) / 2, 34

    def desenha(vals, gab=False):
        s = []
        for i, v in enumerate(vals):
            l, c = divmod(i, 4)
            x, y = x0 + c * cel, y0 + l * cel
            if puz[i]:
                s.append(f'<rect x="{x}" y="{y}" width="{cel}" height="{cel}" fill="#eeeeee"/>')
            if v:
                s.append(icone(figs[v - 1], x + 6, y + 6, cel - 12, cor=(LAR if gab and not puz[i] else "#fff")))
        for k in range(5):
            e = 1.6 if k in (0, 2, 4) else .5
            s.append(f'<line x1="{x0 + k * cel}" y1="{y0}" x2="{x0 + k * cel}" y2="{y0 + 4 * cel}" stroke="{TRACO}" stroke-width="{e}"/>')
            s.append(f'<line x1="{x0}" y1="{y0 + k * cel}" x2="{x0 + 4 * cel}" y2="{y0 + k * cel}" stroke="{TRACO}" stroke-width="{e}"/>')
        return "".join(s)

    leg = "".join(icone(f, 34 + k * 30, 2, 22) for k, f in enumerate(figs))
    leg += _txt(W / 2, y0 + 4 * cel + 16, "Em cada linha, coluna e quadradão de 4 casinhas, cada figura aparece uma vez só.", 4.8, 700)
    return _at("Sudoku de figuras", "Desenhe as figuras que faltam: nenhuma pode repetir na linha, na coluna nem no quadradão.",
               1, "Lógica", "sudoku", leg + desenha(puz), desenha(sol, True))


def sudoku6(rng, dicas=17):
    puz, sol = _sudoku_gera(rng, 6, 2, 3, dicas)
    cel, x0, y0 = 26, (W - 156) / 2, 20

    def desenha(valores, gab=False):
        s = []
        for i, v in enumerate(valores):
            l, c = divmod(i, 6)
            x, y = x0 + c * cel, y0 + l * cel
            if puz[i]:
                s.append(f'<rect x="{x}" y="{y}" width="{cel}" height="{cel}" fill="#eeeeee"/>')
            if v:
                s.append(_txt(x + cel / 2, y + cel / 2 + .5, str(v), 13, 800, cor=(LAR if gab and not puz[i] else TRACO), fonte="Baloo 2"))
        for k in range(7):
            e = 1.4 if k in (0, 6) else (1.2 if k % 3 == 0 else .4)
            s.append(f'<line x1="{x0 + k * cel}" y1="{y0}" x2="{x0 + k * cel}" y2="{y0 + 6 * cel}" stroke="{TRACO}" stroke-width="{e}"/>')
            e = 1.4 if k in (0, 6) else (1.2 if k % 2 == 0 else .4)
            s.append(f'<line x1="{x0}" y1="{y0 + k * cel}" x2="{x0 + 6 * cel}" y2="{y0 + k * cel}" stroke="{TRACO}" stroke-width="{e}"/>')
        return "".join(s)

    dica = _txt(W / 2, y0 + 6 * cel + 16, "Cada linha, coluna e bloco de linha grossa (2 linhas x 3 colunas) tem 1 a 6.", 4.6, 600)
    return _at("Sudoku 6x6", "Complete com números de 1 a 6 sem repetir na linha, na coluna nem no bloco de 6 casinhas.",
               2, "Lógica", "sudoku", desenha(puz) + dica, desenha(sol, True))


TEMAS_LOGICA = [
    dict(nomes=["Ana", "Beto", "Caio"], verbo="come", itens=[("maca", "maçã", "a maçã"), ("banana", "banana", "a banana"), ("uva", "uva", "a uva")]),
    dict(nomes=["Lia", "Téo", "Rui"], verbo="brinca com", itens=[("balao", "balão", "o balão"), ("carro", "carrinho", "o carrinho"), ("barco", "barquinho", "o barquinho")]),
    dict(nomes=["Duda", "Enzo", "Bia"], verbo="desenhou", itens=[("sol", "sol", "o sol"), ("lua", "lua", "a lua"), ("estrela", "estrela", "a estrela")]),
    dict(nomes=["Malu", "Davi", "Nina"], verbo="cuida", itens=[("peixe", "peixe", "do peixe"), ("passaro", "passarinho", "do passarinho"), ("flor", "flor", "da flor")]),
]


def grade_logica(rng, tema):
    nomes, itens, verbo = tema["nomes"], tema["itens"], tema["verbo"]
    cand = list(permutations(range(3)))
    sol = rng.choice(cand)

    def frase(tipo, a, b):
        art = itens[b][2]
        if verbo == "cuida":
            return f"{nomes[a]} {'não ' if tipo == 'nao' else ''}cuida {art}."
        return f"{nomes[a]} {'não ' if tipo == 'nao' else ''}{verbo} {art}."

    pistas_poss = [("nao", a, b) for a in range(3) for b in range(3) if sol[a] != b] + \
                  [("sim", a, sol[a]) for a in range(3)]
    for _ in range(500):
        k = rng.choice([2, 2, 3])
        pistas = rng.sample(pistas_poss, k)
        if not any(p[0] == "nao" for p in pistas):
            continue
        validas = [p for p in cand if all((p[a] == b) == (t == "sim") for t, a, b in pistas)]
        if len(validas) == 1:
            break
    else:
        raise AssertionError("sem pistas")
    assert validas[0] == sol
    cel, x0, y0 = 30, 50, 80
    s = [_txt(8, 6, "Pistas:", 6.5, 800, anchor="start", fonte="Baloo 2")]
    for i, p in enumerate(pistas):
        s.append(_txt(12, 16 + i * 9, f"{i + 1}. {frase(*p)}", 6, 700, anchor="start"))
    s.append(_txt(12, 16 + len(pistas) * 9 + 2, "Cada criança tem uma resposta diferente.", 5.4, 700, anchor="start", cor="#555"))
    for j, it in enumerate(itens):
        s.append(icone(it[0], x0 + j * cel + 5, y0 - 26, 20))
    for i, n in enumerate(nomes):
        s.append(_txt(x0 - 6, y0 + i * cel + cel / 2, n, 7.5, 800, anchor="end", fonte="Baloo 2"))
    for k in range(4):
        s.append(f'<line x1="{x0}" y1="{y0 + k * cel}" x2="{x0 + 3 * cel}" y2="{y0 + k * cel}" stroke="{TRACO}" stroke-width=".8"/>')
        s.append(f'<line x1="{x0 + k * cel}" y1="{y0}" x2="{x0 + k * cel}" y2="{y0 + 3 * cel}" stroke="{TRACO}" stroke-width=".8"/>')
    s.append(_txt(W / 2, y0 + 3 * cel + 10, "Marque X onde não pode e ● onde é certo.", 5.6, 700))
    yb = y0 + 3 * cel + 22
    rot = {"come": "come", "brinca com": "brinca com", "desenhou": "desenhou", "cuida": "cuida"}[verbo]
    for i, n in enumerate(nomes):
        s.append(_txt(30, yb + i * 13, f"{n} {rot}", 6.3, 700, anchor="start"))
        s.append(f'<line x1="86" y1="{yb + i * 13 + 3}" x2="140" y2="{yb + i * 13 + 3}" stroke="{TRACO}" stroke-width=".6"/>')
    base = "".join(s)
    gab = []
    for i in range(3):
        for j in range(3):
            cx, cy = x0 + j * cel + cel / 2, y0 + i * cel + cel / 2
            gab.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{LAR}"/>' if sol[i] == j else _txt(cx, cy, "X", 10, 800, cor=LAR))
        gab.append(_txt(90, yb + i * 13, itens[sol[i]][1], 6.3, 800, anchor="start", cor=LAR))
    tit = {"come": "Quem come o quê?", "brinca com": "Quem brinca com o quê?", "desenhou": "Quem desenhou o quê?", "cuida": "Quem cuida de quem?"}[verbo]
    return _at(tit, "Leia as pistas e descubra a resposta de cada criança.", 2, "Lógica", "grade lógica", base, base + "".join(gab))


# ======================================================================= PADRÕES
FIG_PADRAO = ["circulo", "quadrado", "estrela", "coracao", "sol", "lua", "nuvem", "peixe", "maca",
              "triangulo", "losango", "flor", "balao", "casa", "arvore"]


def _item(it):
    return it if isinstance(it, tuple) else (it, 0, False)


def padroes(rng, nivel, ciclos):
    s, gab = [], []
    alt = 45
    for i, ciclo in enumerate(ciclos):
        rng_opc = rng
        if isinstance(ciclo, dict):
            # fila trocada: gasta o rng principal como a fila original e sorteia as opções num rng derivado
            orig = [_item(c) for c in ciclo["sorteio"]]
            r0 = (orig * 4)[6]
            ex0 = [(f, 0, False) for f in FIG_PADRAO if f not in {c[0] for c in orig}]
            pool0 = [c for c in dict.fromkeys(orig) if c != r0] + rng.sample(ex0, 3)
            o0 = [r0] + rng.sample([p for p in pool0 if p != r0], 2)
            rng.shuffle(o0)
            ciclo = ciclo["mostrar"]
            rng_opc = random.Random(f"fila-{ciclo}")
        ciclo = [_item(c) for c in ciclo]
        y = 2 + i * alt
        seq = (ciclo * 4)[:6]
        resp = (ciclo * 4)[6]
        tam = 18
        s.append(f'<rect x="1" y="{y}" width="{W - 2}" height="{alt - 5}" rx="4" fill="none" stroke="#bdbdbd" stroke-width=".5"/>')
        for j, (nome, g, e) in enumerate(seq):
            s.append(icone(nome, 6 + j * 22, y + 3, tam, girar=g, espelhar=e))
        bx = 6 + 6 * 22
        s.append(f'<rect x="{bx}" y="{y + 3}" width="{tam}" height="{tam}" rx="3" fill="none" stroke="{TRACO}" stroke-width=".8" stroke-dasharray="2 1.5"/>')
        s.append(_txt(bx + tam / 2, y + 3 + tam / 2, "?", 11, 800, fonte="Baloo 2"))
        # opções: a certa + 2 erradas (outras do ciclo com outra rotação, ou figuras novas)
        erradas = [c for c in dict.fromkeys(ciclo) if c != resp]
        extra = [(f, 0, False) for f in FIG_PADRAO if f not in {c[0] for c in ciclo}]
        pool = erradas + rng_opc.sample(extra, 3)
        opc = [resp] + rng_opc.sample([p for p in pool if p != resp], 2)
        rng_opc.shuffle(opc)
        oy = y + 24
        s.append(f'<rect x="68" y="{oy - 1}" width="{W - 72}" height="15" rx="3" fill="#f3f3f3"/>')
        s.append(_txt(64, oy + 6.5, "circule:", 4.8, 700, anchor="end", cor="#666"))
        for k, (nome, g, e) in enumerate(opc):
            ox = 80 + k * 32
            s.append(icone(nome, ox, oy, 13, girar=g, espelhar=e))
            if (nome, g, e) == resp:
                gab.append(_circ(ox + 6.5, oy + 6.5, 9))
    base = "".join(s)
    return _at("O que vem depois?", "Olhe a fila, descubra o que se repete e circule embaixo a figura que entra no quadrinho do ponto de interrogação.",
               nivel, "Padrões", "padrões", base, base + "".join(gab))


# filas extras (girar/espelhar) para trocar filas repetidas do "O que vem depois?" do Nível 2, sem usar o rng
CICLOS_EXTRAS = [
    [("triangulo", 0, False), ("triangulo", 180, False)],
    [("peixe", 0, False), ("peixe", 0, False), ("peixe", 0, True)],
    [("banana", 0, False), ("banana", 180, False)],
    [("lua", 0, False), ("lua", 0, True), ("estrela", 0, False)],
    [("coracao", g, False) for g in (0, 90, 180, 270)],
    [("barco", 0, False), ("barco", 0, True), ("barco", 0, True)],
    [("triangulo", 0, False), ("triangulo", 90, False), ("circulo", 0, False)],
    [("banana", g, False) for g in (0, 90, 180, 270)],
    [("coracao", 0, False), ("coracao", 0, False), ("coracao", 180, False)],  # (era a casa de cabeça para baixo: irreconhecível)
    [("passaro", 0, True), ("passaro", 0, False), ("nuvem", 0, False)],
    [("lua", 0, True), ("lua", 0, True), ("lua", 0, False)],
    [("peixe", 0, True), ("estrela", 0, False), ("peixe", 0, False), ("estrela", 0, False)],
]


# filas extras do Nível 1 (sem girar nem espelhar: só figuras em pé, como as outras filas do Nível 1)
CICLOS_EXTRAS_N1 = [
    ["sol", "nuvem"], ["peixe", "peixe", "flor"], ["coracao", "estrela", "estrela"], ["maca", "balao"],
    ["arvore", "arvore", "casa"], ["lua", "sol", "sol"], ["losango", "circulo"], ["triangulo", "triangulo", "quadrado"],
    ["balao", "flor", "flor"], ["casa", "nuvem"], ["estrela", "estrela", "peixe"], ["quadrado", "coracao"],
]


def _sig(c):
    return tuple(_item(x) for x in (c["mostrar"] if isinstance(c, dict) else c))


def sem_repetir_filas(ciclos, usadas, extras=None):
    """Troca as filas que já apareceram no nível (`usadas`, guardado por quem chama) por filas extras."""
    extras = CICLOS_EXTRAS if extras is None else extras
    out = []
    for c in ciclos:
        sig = tuple(_item(x) for x in c)
        if sig in usadas:
            c = next(e for e in extras if _sig(e) not in usadas and _sig(e) not in {_sig(o) for o in out})
            usadas.add(_sig(c))
            out.append({"mostrar": c, "sorteio": list(sig)})  # o sorteio das opções segue a fila original
            continue
        usadas.add(sig)
        out.append(c)
    return out


REGRAS_SEQ = [
    ("soma", lambda a, k: a + k, lambda k: f"soma {k}"),
    ("tira", lambda a, k: a - k, lambda k: f"tira {k}"),
    ("dobra", lambda a, k: a * 2, lambda k: "dobra"),
]


# Filas de "Que número falta?" já usadas no caderno (e, no Volume 2, também as do volume 1).
# A fila nunca repete: se o sorteio principal cair numa fila usada, sorteia de novo com um rng
# derivado (a sequência do rng principal não muda, então as outras páginas continuam iguais).
SEQ_USADAS = set()
# Volume 2: também não pode sair a mesma progressão deslocada uma casa (2 4 6 8 10 × 4 6 8 10 12): compara as
# janelas de 4 termos seguidos. Só o Volume 2 liga isto (no caderno as filas já foram revisadas e não mudam).
CHECAR_JANELAS = False
SEQ_JANELAS = set()


def _janelas(seq):
    return {tuple(seq[i:i + 4]) for i in range(len(seq) - 3)}


def _sorteia_seq(rng, faixa, dobras=(1, 2, 3, 5)):
    tipo = rng.choice(["soma", "soma", "tira"] + (["dobra"] if faixa >= 2 else []) + (["alterna"] if faixa >= 3 else []))
    if tipo == "soma":
        k = rng.choice([2, 3, 5, 10] if faixa == 1 else [3, 4, 5, 6, 9, 10, 11]); a = rng.randint(0, 20 if faixa == 1 else 40)
        seq = [a + k * t for t in range(5)]; regra = f"soma {k}"
    elif tipo == "tira":
        k = rng.choice([2, 3, 5, 10] if faixa == 1 else [3, 4, 6, 7, 8]); a = rng.randint(4 * k, 4 * k + 30)
        seq = [a - k * t for t in range(5)]; regra = f"tira {k}"
    elif tipo == "dobra":
        a = rng.choice(list(dobras)); seq = [a * 2 ** t for t in range(5)]; regra = "dobra"
    else:
        p, q = rng.sample([1, 2, 3, 4, 5], 2); a = rng.randint(1, 10)
        seq = [a]
        for t in range(4):
            seq.append(seq[-1] + (p if t % 2 == 0 else q))
        regra = f"+{p}, +{q}"
    return tipo, seq, regra


def sequencias(rng, faixa):
    """faixa: 1 (fácil) a 3 (difícil)."""
    s, gab = [], []
    usadas = set()       # sorteio principal (mesma regra de sempre: mantém a sequência do rng)
    na_pagina = set()    # filas que de fato vão para a página
    for i in range(6):
        for _ in range(200):
            tipo, seq, regra = _sorteia_seq(rng, faixa)
            if max(seq) <= 99 and min(seq) >= 0 and tuple(seq) not in usadas:
                usadas.add(tuple(seq)); break
        k_alt = 0
        while (tuple(seq) in na_pagina or tuple(seq) in SEQ_USADAS or max(seq) > 99 or min(seq) < 0
               or (CHECAR_JANELAS and _janelas(seq) & SEQ_JANELAS)):
            k_alt += 1
            assert k_alt < 500, "sem fila nova"
            tipo, seq, regra = _sorteia_seq(random.Random(f"seq-{faixa}-{i}-{seq}-{k_alt}"), faixa, (1, 2, 3, 4, 5, 6))
        na_pagina.add(tuple(seq)); SEQ_USADAS.add(tuple(seq)); SEQ_JANELAS.update(_janelas(seq))
        y = 6 + i * 36
        falta = rng.choice([2, 3, 4]) if faixa >= 2 else 4
        if tipo == "alterna":
            falta = 4  # regra alternada com o buraco no meio admite duas leituras (ex.: 1 5 _ 12 15)
        for k, v in enumerate(seq):
            x = 8 + k * 30
            tr = 'stroke-dasharray="2 1.5"' if k == falta else ""
            s.append(f'<circle cx="{x + 11}" cy="{y + 11}" r="11" fill="#fff" stroke="{TRACO}" stroke-width=".8" {tr}/>')
            if k != falta:
                s.append(_txt(x + 11, y + 11.5, str(v), 10, 800, fonte="Baloo 2"))
            else:
                gab.append(_txt(x + 11, y + 11.5, str(v), 10, 800, cor=LAR, fonte="Baloo 2"))
            if k < 4:
                s.append(_txt(x + 26, y + 11, "›", 9, 800, cor="#999"))
        s.append(_txt(160, y + 11, "regra:", 4.6, 700, cor="#666"))
        s.append(f'<line x1="150" y1="{y + 19}" x2="180" y2="{y + 19}" stroke="{TRACO}" stroke-width=".5"/>')
        gab.append(_txt(165, y + 15.5, regra, 6, 800, cor=TRACO))
    base = "".join(s)
    return _at("Que número falta?", "Descubra a regra de cada fila e escreva o número que falta no círculo pontilhado.",
               2, "Padrões", "sequência numérica", base, base + "".join(gab))


# ======================================================================= ATENÇÃO
VARIANTES = [("peixe", dict(espelhar=True)), ("estrela", dict(variante="6pontas")), ("casa", dict(variante="semporta")),
             ("flor", dict(variante="4petalas")), ("triangulo", dict(girar=180)), ("maca", dict(variante="semfolha")),
             ("passaro", dict(espelhar=True)), ("casa", dict(variante="semjanela")), ("sol", dict(variante="poucosraios")),
             ("lua", dict(espelhar=True)), ("carro", dict(variante="semroda")), ("coracao", dict(girar=180)),
             ("barco", dict(espelhar=True)), ("banana", dict(espelhar=True))]


def diferente(rng, linhas):
    s, gab = [], []
    for i, (nome, mud) in enumerate(linhas):
        y = 4 + i * 37
        k = rng.randrange(5)
        for j in range(5):
            x = 6 + j * 35
            s.append(icone(nome, x, y, 28, **(mud if j == k else {})))
            if j == k:
                gab.append(_circ(x + 14, y + 14, 17))
        if i < len(linhas) - 1:
            s.append(f'<line x1="2" y1="{y + 33}" x2="{W - 2}" y2="{y + 33}" stroke="#ccc" stroke-width=".3"/>')
    base = "".join(s)
    return _at("Qual é diferente?", "Em cada fila, uma figura está um pouquinho diferente. Encontre e circule.",
               1, "Atenção", "qual é diferente", base, base + "".join(gab))


def diferente_grade(rng, blocos):
    """Nível 2: 3 quadros com 12 figuras iguais e 1 diferente (mais sutil)."""
    s, gab = [], []
    for b, (nome, mud) in enumerate(blocos):
        y0 = 2 + b * 75
        s.append(f'<rect x="1" y="{y0}" width="{W - 2}" height="70" rx="4" fill="none" stroke="#bdbdbd" stroke-width=".5"/>')
        k = rng.randrange(14)
        for j in range(14):
            c, l = j % 7, j // 7
            x, y = 6 + c * 25, y0 + 6 + l * 32
            g = 0
            if j == k:
                s.append(icone(nome, x, y, 21, **mud))
                gab.append(_circ(x + 10.5, y + 10.5, 13))
            else:
                s.append(icone(nome, x, y, 21, girar=g))
    base = "".join(s)
    return _at("Encontre a diferente", "Em cada quadro há uma figura diferente das outras. Encontre e circule as três.",
               2, "Atenção", "qual é diferente", base, base + "".join(gab))


def contar(rng, tipos, qmin=3, qmax=10):
    s, gab = [], []
    qtds = rng.sample(range(qmin, qmax + 1), 4)
    for i, (nome, n) in enumerate(zip(tipos, qtds)):
        px, py = (i % 2) * 92, (i // 2) * 112
        s.append(f'<rect x="{px + 1}" y="{py + 1}" width="88" height="106" rx="5" fill="none" stroke="{TRACO}" stroke-width=".7"/>')
        casas = [(c, l) for c in range(4) for l in range(3)]
        for c, l in rng.sample(casas, n):
            x, y = px + 4 + c * 20 + rng.uniform(-1.5, 1.5), py + 5 + l * 23 + rng.uniform(-2, 2)
            s.append(icone(nome, x, y, 18, girar=rng.choice([-12, 0, 10])))
        for k in range(10):
            cx, cy = px + 9 + (k % 5) * 17.5, py + 81 + (k // 5) * 12
            s.append(_txt(cx, cy, str(k + 1), 7, 800, fonte="Baloo 2"))
            if k + 1 == n:
                gab.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="none" stroke="{LAR}" stroke-width="1.4"/>')
    base = "".join(s)
    return _at("Conte e circule", "Conte as figuras de cada quadro e circule o número certo embaixo.",
               1, "Atenção", "conte e circule", base, base + "".join(gab))


def quantos_tem(rng, tipos):
    """Nível 2: figuras misturadas numa cena; contar cada tipo."""
    qtds = [rng.randint(3, 9) for _ in tipos]
    total = sum(qtds)
    casas = [(c, l) for c in range(8) for l in range(6)]
    assert total <= len(casas)
    esc = rng.sample(casas, total)
    s = [f'<rect x="1" y="1" width="{W - 2}" height="150" rx="5" fill="none" stroke="{TRACO}" stroke-width=".7"/>']
    i = 0
    for nome, n in zip(tipos, qtds):
        for _ in range(n):
            c, l = esc[i]; i += 1
            s.append(icone(nome, 5 + c * 21.5 + rng.uniform(-1.5, 1.5), 5 + l * 24 + rng.uniform(-1.5, 1.5), 17, girar=rng.choice([-15, 0, 12])))
    gab = []
    for k, (nome, n) in enumerate(zip(tipos, qtds)):
        x = 8 + (k % 2) * 92; y = 162 + (k // 2) * 30
        s.append(icone(nome, x, y, 20))
        s.append(_txt(x + 26, y + 11, "=", 9, 800))
        s.append(f'<rect x="{x + 34}" y="{y + 1}" width="22" height="18" rx="3" fill="none" stroke="{TRACO}" stroke-width=".7"/>')
        gab.append(_txt(x + 45, y + 11, str(n), 10, 800, cor=LAR, fonte="Baloo 2"))
    base = "".join(s)
    return _at("Quantos tem?", "Conte quantas figuras de cada tipo há no quadro e escreva o número nas caixinhas.",
               2, "Atenção", "conte e circule", base, base + "".join(gab))


# ---- jogo das diferenças: cenas montadas com ícones
CENAS = {
    "quintal": [("sol", 6, 4, 28), ("nuvem", 52, 4, 30), ("nuvem", 128, 2, 22), ("passaro", 98, 26, 18),
                ("casa", 14, 46, 58), ("arvore", 82, 44, 54), ("flor", 140, 84, 18), ("flor", 158, 88, 14),
                ("maca", 142, 52, 14), ("carro", 130, 64, 0)],
    "parque": [("arvore", 2, 40, 56), ("arvore", 118, 38, 54), ("balao", 66, 6, 26), ("balao", 90, 14, 22),
               ("sol", 148, 2, 26), ("passaro", 38, 10, 18), ("carro", 62, 72, 34), ("flor", 8, 92, 14),
               ("flor", 160, 92, 14), ("estrela", 112, 4, 12)],
    "praia": [("sol", 6, 4, 30), ("nuvem", 70, 4, 28), ("passaro", 120, 8, 18), ("passaro", 146, 22, 14),
              ("barco", 18, 42, 40), ("barco", 108, 48, 30), ("peixe", 30, 88, 18), ("peixe", 96, 90, 16),
              ("peixe", 148, 84, 18), ("estrela", 70, 86, 16)],
    "noite": [("lua", 140, 4, 28), ("estrela", 10, 8, 14), ("estrela", 40, 22, 12), ("estrela", 80, 4, 14),
              ("estrela", 110, 24, 10), ("nuvem", 56, 28, 24), ("casa", 16, 48, 56), ("arvore", 92, 46, 52),
              ("carro", 134, 76, 30), ("flor", 76, 92, 12)],
    "festa": [("balao", 6, 6, 26), ("balao", 28, 2, 24), ("balao", 150, 6, 26), ("coracao", 74, 8, 18),
              ("estrela", 104, 14, 16), ("casa", 52, 44, 58), ("arvore", 118, 46, 52), ("flor", 8, 90, 16),
              ("maca", 30, 92, 12), ("sol", 120, 0, 0)],
}
ESPELHAVEIS = {"peixe", "passaro", "barco", "carro", "lua", "banana", "balao"}
# espelhar objeto quase simétrico (balão, carro) quase não muda o desenho: vira "menor" (ou "remover" se for pequeno)
QUASE_SIMETRICOS = {"balao", "carro"}
VAR_DIF = {"estrela": "6pontas", "casa": "semporta", "flor": "4petalas", "sol": "poucosraios", "maca": "semfolha"}


def _objetos(nome_cena, rng):
    objs = []
    for nome, x, y, t in CENAS[nome_cena]:
        if t == 0:
            continue
        objs.append(dict(nome=nome, x=x + rng.uniform(-2, 2), y=y + rng.uniform(-1.5, 1.5), t=t))
    return objs


def _desenha_cena(objs, cena, mods):
    s = []
    if cena == "praia":
        s.append(f'<path d="M0 82 q 11 -4 22 0 t 22 0 t 22 0 t 22 0 t 22 0 t 22 0 t 22 0 t 22 0" fill="none" stroke="{TRACO}" stroke-width=".8"/>')
    else:
        s.append(f'<line x1="2" y1="104" x2="174" y2="104" stroke="{TRACO}" stroke-width=".9"/>')
    for i, o in enumerate(objs):
        m = mods.get(i)
        if m == "remover":
            continue
        t, x, y, kw = o["t"], o["x"], o["y"], {}
        if m == "menor":
            x, y, t = x + t * .175, y + t * .175, t * .65
        elif m == "espelhar":
            kw["espelhar"] = True
        elif m == "variante":
            kw["variante"] = VAR_DIF[o["nome"]]
        elif m == "cinza":
            kw["cor"] = "#a8a8a8"
        s.append(icone(o["nome"], x, y, t, **kw))
    return "".join(s)


def diferencas(rng, nivel, cena, n):
    objs = _objetos(cena, rng)
    idx = rng.sample(range(len(objs)), n)
    mods = {}
    for i in idx:
        o = objs[i]
        poss = ["remover", "cinza"] + (["menor"] if o["t"] >= 16 else []) + (["espelhar"] if o["nome"] in ESPELHAVEIS else []) \
            + (["variante", "variante"] if o["nome"] in VAR_DIF else [])
        mods[i] = rng.choice(poss)
    assert len(mods) == n
    # ajustes depois do sorteio (o rng principal segue igual): diferença tem de ser visível para a idade
    for i, m in mods.items():
        o = objs[i]
        if m == "espelhar" and o["nome"] in QUASE_SIMETRICOS:
            mods[i] = "menor" if o["t"] >= 16 else "remover"
        elif m == "variante" and (o["t"] < 16 or (nivel == 1 and o["t"] < 20)):
            mods[i] = "cinza"  # 4 pétalas / maçã sem folha num objeto pequeno some na folha impressa
    esc = 1.0 if nivel == 2 else 1.0
    pw, ph = 176, 108

    def painel(y, m, marcar=False):
        g = f'<g transform="translate({(W - pw * esc) / 2},{y}) scale({esc})"><rect x="0" y="0" width="{pw}" height="{ph}" rx="4" fill="none" stroke="{TRACO}" stroke-width=".6"/>'
        g += f'<g transform="translate(0,1)">{_desenha_cena(objs, cena, m)}</g>'
        if marcar:
            for i in m:
                o = objs[i]
                r = min(o["t"] * .62 + 3, 17)
                cx = min(max(o["x"] + o["t"] / 2, r + .8), pw - r - .8)
                cy = min(max(o["y"] + 1 + o["t"] / 2, r + .8), ph - r - .8)
                g += _circ(cx, cy, r, 1.3)
        return g + "</g>"

    base = painel(0, {}) + painel(114, mods)
    tit = "Jogo dos 7 erros" if n == 7 else f"Ache as {n} diferenças"
    instr = f"Compare os dois desenhos e circule, no de baixo, as {n} diferenças."
    return _at(tit, instr, nivel, "Atenção", "jogo dos erros", base, painel(0, {}) + painel(114, mods, True))


# ======================================================================= MEMÓRIA
def memoria_figuras(rng, nivel, n_ver, n_opc):
    pool = ["circulo", "quadrado", "estrela", "coracao", "sol", "lua", "nuvem", "peixe", "maca", "triangulo",
            "losango", "flor", "balao", "casa", "arvore", "carro", "barco", "passaro", "uva", "banana"]
    escolhidas = rng.sample(pool, n_opc)
    vistas = escolhidas[:n_ver]
    s = [f'<rect x="1" y="1" width="{W - 2}" height="92" rx="6" fill="#fff7f1" stroke="{TRACO}" stroke-width=".7"/>',
         _txt(8, 9, "OLHE BEM", 5.5, 800, anchor="start", cor=TRACO, fonte="Baloo 2")]
    tam = 30 if n_ver <= 4 else 24
    cols = n_ver if n_ver <= 4 else math.ceil(n_ver / 2)
    linhas = 1 if n_ver <= 4 else 2
    for k, nome in enumerate(vistas):
        c, l = k % cols, k // cols
        larg = cols * (tam + 10)
        x = (W - larg) / 2 + c * (tam + 10) + 5
        y = (92 - linhas * (tam + 6)) / 2 + l * (tam + 6) + 5
        g = rng.choice([0, 0, -8, 8])  # sorteio mantido para não mudar a sequência do rng
        s.append(icone(nome, x, y, tam, girar=g if nivel == 2 else 0))  # Nível 1: igual em cima e embaixo
    s.append(f'<line x1="0" y1="101" x2="{W}" y2="101" stroke="{TRACO}" stroke-width=".7" stroke-dasharray="3 2"/>')
    s.append(_txt(W / 2, 97, "dobre aqui para esconder a parte de cima", 4.6, 700, cor="#777"))
    s.append(_txt(8, 112, "Quais figuras estavam lá em cima? Circule.", 6.2, 800, anchor="start"))
    opc = escolhidas[:]
    rng.shuffle(opc)
    gab = []
    cols2 = 4 if n_opc <= 8 else 5
    for k, nome in enumerate(opc):
        c, l = k % cols2, k // cols2
        x = 12 + c * (160 / cols2) + (160 / cols2 - 24) / 2
        y = 122 + l * 34
        s.append(icone(nome, x, y, 24))
        if nome in vistas:
            gab.append(_circ(x + 12, y + 12, 15))
    if nivel == 2:
        yq = 122 + math.ceil(n_opc / cols2) * 34 + 6
        s.append(_txt(8, yq, "Quantas figuras havia lá em cima?", 6, 800, anchor="start"))
        s.append(f'<rect x="120" y="{yq - 7}" width="20" height="14" rx="3" fill="none" stroke="{TRACO}" stroke-width=".7"/>')
        gab.append(_txt(130, yq, str(n_ver), 9, 800, cor=LAR, fonte="Baloo 2"))
    base = "".join(s)
    instr = ("Mostre a parte de cima por 20 segundos. Dobre a folha na linha e peça para circular as figuras que estavam lá."
             if nivel == 1 else "Olhe a parte de cima por 30 segundos. Dobre a folha na linha, sem espiar, e responda.")
    return _at("Olhe e lembre", instr, nivel, "Memória", "memória", base, base + "".join(gab))


def memoria_lugares(rng, n):
    """Nível 2: lembrar onde estava cada figura numa grade 3x3."""
    figs = rng.sample(["estrela", "coracao", "sol", "lua", "peixe", "maca", "flor", "balao", "casa"], n)
    lugares = rng.sample(range(9), n)
    cel = 26

    def grade(x0, y0, mostrar):
        g = []
        for k in range(4):
            g.append(f'<line x1="{x0 + k * cel}" y1="{y0}" x2="{x0 + k * cel}" y2="{y0 + 3 * cel}" stroke="{TRACO}" stroke-width=".8"/>')
            g.append(f'<line x1="{x0}" y1="{y0 + k * cel}" x2="{x0 + 3 * cel}" y2="{y0 + k * cel}" stroke="{TRACO}" stroke-width=".8"/>')
        if mostrar:
            for f, p in zip(figs, lugares):
                c, l = p % 3, p // 3
                g.append(icone(f, x0 + c * cel + 4, y0 + l * cel + 4, cel - 8, cor=mostrar))
        return "".join(g)

    s = [f'<rect x="1" y="1" width="{W - 2}" height="92" rx="6" fill="#fff7f1" stroke="{TRACO}" stroke-width=".7"/>',
         _txt(8, 9, "OLHE BEM", 5.5, 800, anchor="start", cor=TRACO, fonte="Baloo 2"),
         grade((W - 3 * cel) / 2, 8, "#fff"),
         f'<line x1="0" y1="101" x2="{W}" y2="101" stroke="{TRACO}" stroke-width=".7" stroke-dasharray="3 2"/>',
         _txt(W / 2, 97, "dobre aqui para esconder a parte de cima", 4.6, 700, cor="#777"),
         _txt(8, 112, "Desenhe cada figura no lugar onde ela estava:", 6.2, 800, anchor="start")]
    for k, f in enumerate(figs):
        s.append(icone(f, (W - n * 26) / 2 + k * 26 + 4, 120, 18))
    s.append(grade((W - 3 * cel) / 2, 146, None))
    base = "".join(s)
    gab = grade((W - 3 * cel) / 2, 146, LAR)
    return _at("Onde estava?", "Olhe a grade por 30 segundos. Dobre a folha na linha, sem espiar, e desenhe as figuras no lugar certo.",
               2, "Memória", "memória", base, base + gab)


# ======================================================================= TRAÇADO
def _coracao():
    pts = []
    for k in range(25):
        t = math.pi * 2 * k / 24
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((100 + x * 5.2, 95 - y * 5.2))
    return pts


def _estrela5():
    pts = []
    for i in range(11):
        a = -math.pi / 2 + i * math.pi / 5
        r = 85 if i % 2 == 0 else 36
        pts.append((100 + r * math.cos(a), 105 + r * math.sin(a)))
    return pts


def _peixe():
    return [(30, 100), (50, 70), (85, 58), (120, 62), (145, 80), (178, 55), (170, 100), (178, 145),
            (145, 120), (120, 138), (85, 142), (50, 130), (30, 100)]


DESENHOS_PONTOS = {
    "barquinho": [(30, 150), (55, 185), (150, 185), (172, 150), (100, 25), (100, 150), (30, 150)],
    "casinha": [(50, 190), (50, 100), (22, 100), (100, 30), (178, 100), (150, 100), (150, 190), (50, 190)],
    "foguete": [(100, 10), (130, 60), (130, 140), (158, 178), (126, 166), (116, 186), (84, 186), (74, 166), (42, 178), (70, 140), (70, 60), (100, 10)],
    "coração": None, "estrela": None, "peixe": None,
}


# partes do desenho que já vêm traçadas (não fazem parte do caminho de pontos), no mesmo sistema 0..200
# barquinho: o convés entre o pé do mastro e a ponta da direita já vem traçado (separa a vela do casco)
TRACO_PRONTO = {"barquinho": "M100 150 L 172 150"}
# pontos onde o traço pronto encosta: o número vai para o lado (não fica em cima do traço)
ROTULO_AO_LADO = {}


def _pontos_de(nome):
    if nome == "coração":
        return _coracao()
    if nome == "estrela":
        return _estrela5()
    if nome == "peixe":
        return _peixe()
    return DESENHOS_PONTOS[nome]


def ligue_pontos(rng, nivel, desenho, alvo):
    cantos = _pontos_de(desenho)
    if desenho == "coração":
        densa = []
        for (ax, ay), (bx, by) in zip(cantos, cantos[1:]):
            for t in range(20):
                densa.append((ax + (bx - ax) * t / 20, ay + (by - ay) * t / 20))
        comp = [0.0]
        for a, b in zip(densa, densa[1:]):
            comp.append(comp[-1] + math.dist(a, b))
        tot = comp[-1] + math.dist(densa[-1], densa[0])
        pts, j = [], 0
        for k in range(alvo):
            alvo_d = tot * k / alvo
            while j < len(comp) - 1 and comp[j + 1] < alvo_d:
                j += 1
            pts.append(densa[j])
    else:
        total = sum(math.dist(a, b) for a, b in zip(cantos, cantos[1:]))
        passo = total / alvo
        pts = []
        for (ax, ay), (bx, by) in zip(cantos, cantos[1:]):
            n = max(1, round(math.dist((ax, ay), (bx, by)) / passo))
            for t in range(n):
                pts.append((ax + (bx - ax) * t / n, ay + (by - ay) * t / n))
        if math.dist(cantos[0], cantos[-1]) > 1:
            pts.append(cantos[-1])
    limpos = []
    for p in pts:
        if not limpos or math.dist(p, limpos[-1]) >= 9:
            limpos.append(p)
    if len(limpos) > 2 and math.dist(limpos[-1], limpos[0]) < 9:
        limpos.pop()
    pts = limpos
    assert all(math.dist(a, b) >= 9 for a, b in zip(pts, pts[1:])), desenho
    # escala para a área (o desenho cabe em 0..200 x 0..200)
    e = 0.9
    pts = [(x * e, 8 + y * e) for x, y in pts]
    cx = sum(p[0] for p in pts) / len(pts); cy = sum(p[1] for p in pts) / len(pts)
    s = []
    tl = 5.5 if len(pts) <= 25 else 4.6
    rotulos = []
    for i, (x, y) in enumerate(pts):
        dx, dy = x - cx, y - cy; d = math.hypot(dx, dy) or 1
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.5" fill="{TRACO}"/>')
        lx, ly = x + dx / d * 5.5, y + dy / d * 5.5
        ao_lado = False
        for ax, ay in ROTULO_AO_LADO.get(desenho, []):
            if math.dist((x, y), (ax * e, 8 + ay * e)) < 4:
                lx, ly = x + 5, y - 3.5
                ao_lado = True

        def folga(px, py, i=i):
            outros = [q for j, q in enumerate(pts) if j != i] + rotulos
            return min(math.dist((px, py), q) for q in outros)
        if folga(lx, ly) < 4.5:  # número colado no ponto vizinho: procura o lado com mais espaço
            cands = [(x + 5.5 * math.cos(k * math.pi / 4), y + 5.5 * math.sin(k * math.pi / 4)) for k in range(8)
                     if not (ao_lado and k in (1, 2, 3))]  # ponto onde encosta o traço pronto (cabo): nunca por cima dele
            lx, ly = max(cands, key=lambda c: folga(*c))
        rotulos.append((lx, ly))
        s.append(_txt(lx, ly, str(i + 1), tl, 800))
    if desenho == "barquinho":
        for k in range(3):
            yy = 196 + k * 6
            s.append(f'<path d="M6 {yy} q 11 -5 22 0 t 22 0 t 22 0 t 22 0 t 22 0 t 22 0 t 22 0 t 22 0" fill="none" stroke="{TRACO}" stroke-width=".7"/>')
    if desenho in TRACO_PRONTO:
        s.append(f'<path d="{TRACO_PRONTO[desenho]}" transform="translate(0,8) scale({e})" fill="none" stroke="{TRACO}" '
                 f'stroke-width="{1.4 / e:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
    base = "".join(s)
    linha = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    fechado = math.dist(cantos[0], cantos[-1]) <= 1
    tag = "polygon" if fechado else "polyline"
    gab = f'<{tag} points="{linha}" fill="none" stroke="{LAR}" stroke-width="1.6" stroke-linejoin="round"/>'
    instr = (f"Ligue do 1 ao {len(pts)}, na ordem, e volte ao 1 para fechar o desenho. Depois pinte!" if fechado
             else f"Ligue do 1 ao {len(pts)}, na ordem, e descubra o desenho. Depois pinte!")
    if nivel == 1 and len(pts) > 15:
        instr += " Se precisar, o adulto ajuda a achar os números depois do 10."
    return _at("Ligue os pontos", instr, nivel, "Traçado", "ligue os pontos", base, gab + base)


def tracado(rng, tipos, pares):
    s = []
    for i, (tipo, (a, b)) in enumerate(zip(tipos, pares)):
        y = 22 + i * 44
        x1 = 30
        if tipo == "reta":
            d = f"M{x1} {y} L150 {y}"
        elif tipo == "onda":
            d = f"M{x1} {y} " + " ".join(f"q 7.5 {'-' if k % 2 == 0 else ''}14 15 0" for k in range(8))
        elif tipo == "onda2":
            d = f"M{x1} {y} " + " ".join(f"q 5 {'-' if k % 2 == 0 else ''}10 10 0" for k in range(12))
        elif tipo == "zigue":
            d = f"M{x1} {y} " + " ".join(f"l 10 {'-' if k % 2 == 0 else ''}12" for k in range(12))
        elif tipo == "degraus":
            d = f"M{x1} {y} " + " ".join("l 0 -12 l 10 0 l 0 12 l 10 0" for _ in range(6))
        elif tipo == "ponte":
            d = f"M{x1} {y} " + " ".join("a 10 10 0 0 1 20 0" for _ in range(6))
        elif tipo == "montanha":
            d = f"M{x1} {y} " + " ".join("l 15 -14 l 15 14" for _ in range(4))
        elif tipo == "curva":
            d = f"M{x1} {y} C 70 {y - 30}, 110 {y + 30}, 150 {y}"
        else:  # laços
            d = f"M{x1} {y} " + " ".join("c 6 -16, 14 -16, 10 0 c -2 6, 6 6, 10 0" for _ in range(6))
        s.append(f'<path d="{d}" fill="none" stroke="#6b6b6b" stroke-width="1.6" stroke-dasharray="2.2 1.8" stroke-linecap="round" stroke-linejoin="round"/>')
        s.append(f'<circle cx="{x1}" cy="{y}" r="2" fill="{LAR}"/>')
        s.append(icone(a, 2, y - 12, 24))
        s.append(icone(b, 156, y - 12, 24))
    return _at("Siga o caminho", "Comece na bolinha e passe o lápis por cima do pontilhado, sem tirar do papel.",
               1, "Traçado", "caminho", "".join(s), gab_txt="Atividade livre: vale qualquer traço que siga o pontilhado.")


def copie_desenho(rng, n_seg):
    """Nível 2: copiar um desenho de uma grade de pontos para outra."""
    N = 7
    # caminho aleatório conexo em grade 7x7, sem repetir aresta
    for _ in range(200):
        p = (rng.randrange(N), rng.randrange(N))
        arestas = set(); caminho = [p]
        while len(arestas) < n_seg:
            viz = [(p[0] + dx, p[1] + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                   if 0 <= p[0] + dx < N and 0 <= p[1] + dy < N]
            viz = [q for q in viz if frozenset((p, q)) not in arestas]
            if not viz:
                break
            q = rng.choice(viz); arestas.add(frozenset((p, q))); caminho.append(q); p = q
        if len(arestas) == n_seg:
            break
    assert len(arestas) == n_seg
    xs, ys = [a for a, _ in caminho], [b for _, b in caminho]
    dx = (N - 1 - max(xs) - min(xs)) // 2
    dy = (N - 1 - max(ys) - min(ys)) // 2
    caminho = [(a + dx, b + dy) for a, b in caminho]  # centraliza o modelo na grade
    passo = 12

    def grade(x0, y0, desenhar, cor=TRACO):
        g = "".join(f'<circle cx="{x0 + i * passo}" cy="{y0 + j * passo}" r=".9" fill="#777"/>' for i in range(N) for j in range(N))
        if desenhar:
            pts = " ".join(f"{x0 + a * passo},{y0 + b * passo}" for a, b in caminho)
            g += f'<polyline points="{pts}" fill="none" stroke="{cor}" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/>'
        return g

    lado = (N - 1) * passo
    xa = (W - lado) / 2
    s = [_txt(xa - 6, 6, "Modelo", 6, 800, anchor="start", fonte="Baloo 2"), grade(xa, 14, True),
         _txt(xa - 6, 110, "Sua cópia", 6, 800, anchor="start", fonte="Baloo 2"), grade(xa, 118, False)]
    base = "".join(s)
    return _at("Copie o desenho", "Copie o desenho do modelo na grade de baixo, ligando os mesmos pontos.",
               2, "Traçado", "copiar desenho", base, base + grade(xa, 118, True, LAR))


# ======================================================================= CORES E CÓDIGOS
CORES = {1: ("vermelho", "#e53935"), 2: ("amarelo", "#fdd835"), 3: ("verde", "#43a047"), 4: ("azul", "#1e88e5"),
         5: ("marrom", "#8d6e63"), 6: ("laranja", "#fb8c00")}


def _arte(nome):
    n = 12
    if nome == "coracao":
        g = [[0] * n for _ in range(n)]
        for l in range(n):
            for c in range(n):
                x = (c + .5 - 6) / 5.2; y = (6 - (l + .5)) / 5.2 + .25
                if (x * x + y * y - 1) ** 3 - x * x * y ** 3 <= 0:
                    g[l][c] = 1
        return g
    if nome == "sol":
        g = [[0] * n for _ in range(n)]
        for l in range(n):
            for c in range(n):
                d = math.hypot(c + .5 - 6, l + .5 - 6)
                if d <= 3.2:
                    g[l][c] = 6
                elif (c in (5, 6) or l in (5, 6) or abs(c - l) == 0 or abs(c + l - 11) == 0) and 4.2 <= d <= 5.9:
                    g[l][c] = 2
        return g
    if nome == "estrela":
        pol = [(6 + 6.4 * math.cos(-math.pi / 2 + i * math.pi / 5) * (1 if i % 2 == 0 else .42),
                6.6 + 6.4 * math.sin(-math.pi / 2 + i * math.pi / 5) * (1 if i % 2 == 0 else .42)) for i in range(10)]

        def dentro(px, py):
            r = False
            for i in range(10):
                (x1, y1), (x2, y2) = pol[i], pol[(i + 1) % 10]
                if (y1 > py) != (y2 > py) and px < (x2 - x1) * (py - y1) / (y2 - y1) + x1:
                    r = not r
            return r
        return [[2 if dentro(c + .5, l + .5) else 0 for c in range(n)] for l in range(n)]
    artes = {
        "casa": ["....11......", "...1111.....", "..111111....", ".11111111...", "1111111111..", ".22222222...",
                 ".24422222...", ".24422552...", ".22222552...", ".22222552...", "333333333333", "333333333333"],
        "arvore": ["....3333....", "..33333333..", ".3331333133.", ".3333333333.", "333133333313", ".3333331333.",
                   "..33333333..", "....3333....", ".....55.....", ".....55.....", ".....55.....", "...555555..."],
        "sorvete": [".....11.....", "....4444....", "...444444...", "..44444444..", "..44444444..", "..66666666..",
                    "...555555...", "...555555...", "....5555....", "....5555....", ".....55.....", ".....55....."],
        "barco": ["............", ".....1......", ".....11.....", ".....111....", ".....1111...", ".....11111..",
                  ".....5......", ".5555555555.", "..55555555..", "...555555...", "444444444444", ".4444444444."],
        "flor": ["....11......", "...1111.....", "..112211....", "..112211....", "...1111.....", "....11......",
                 "....33...33.", "....33..333.", "..3333333...", ".33333......", "....33......", "....33......"],
        "peixe": ["............", "............", "....6666....", "..66666666.6", ".6.666666666", "666666666666",
                  "666666666666", ".66666666666", "..66666666.6", "....6666....", "............", "............"],
        # o mesmo peixe com 4 cores: nadadeiras vermelhas, listra amarela, rabo azul, corpo laranja
        "peixe_cores": ["............", "............", "....1111....", "..66662666.4", ".6.666266644", "666666266644", "666666266644", ".66666266644", "..66662666.4", "....1111....", "............", "............"],
    }
    linhas = artes[nome]
    assert len(linhas) == n and all(len(r) == n for r in linhas), nome
    return [[0 if ch == "." else int(ch) for ch in r] for r in linhas]


ARTES_NOMES = {"coracao": "um coração", "sol": "um sol", "estrela": "uma estrela", "casa": "uma casa", "arvore": "uma árvore",
               "sorvete": "um sorvete", "barco": "um barco", "flor": "uma flor", "peixe": "um peixe", "peixe_cores": "um peixe"}


def pinte_codigo(rng, nivel, arte, contas=False, sorteio_como=None):
    """sorteio_como: nome da arte antiga com as mesmas casas, para sortear as contas do mesmo jeito
    (assim a troca de cores de uma arte não muda as outras páginas, que vêm do mesmo rng)."""
    g = _arte(arte)
    gs = _arte(sorteio_como) if sorteio_como else g
    assert all((a > 0) == (b > 0) for ra, rb in zip(g, gs) for a, b in zip(ra, rb)), "arte e sorteio_como com casas diferentes"
    usados = sorted({v for r in g for v in r if v})
    cel = 12.5
    x0, y0 = (W - 12 * cel) / 2, 34
    s, gab = [], []
    for k, v in enumerate(usados):
        x = (W - len(usados) * 34) / 2 + k * 34 + 2
        s.append(f'<rect x="{x}" y="2" width="30" height="17" rx="3" fill="#fff" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(_txt(x + 8, 10.5, str(v), 9, 800, fonte="Baloo 2"))
        s.append(f'<rect x="{x + 15}" y="5" width="10" height="11" rx="1.5" fill="{CORES[v][1]}" stroke="{TRACO}" stroke-width=".4"/>')
        s.append(_txt(x + 15, 24.5, CORES[v][0].upper(), 5.2, 800, cor=TRACO))  # em P&B a cor vira cinza: o nome escrito resolve
    for l in range(12):
        for c in range(12):
            v = g[l][c]
            x, y = x0 + c * cel, y0 + l * cel
            s.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{cel}" height="{cel}" fill="#fff" stroke="#777" stroke-width=".45"/>')
            if v:
                if contas:
                    vs = gs[l][c]
                    a = rng.randint(0, vs) * v // vs; rot = f"{a}+{v - a}"
                    assert a + (v - a) == v
                    s.append(_txt(x + cel / 2, y + cel / 2, rot, 3.6, 700, cor="#444"))
                else:
                    s.append(_txt(x + cel / 2, y + cel / 2 + .3, str(v), 5.6, 700, cor="#444"))
                gab.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{cel}" height="{cel}" fill="{CORES[v][1]}" stroke="#777" stroke-width=".45"/>')
    base = "".join(s)
    # gabarito: as casas pintadas vão POR CIMA da grade branca (antes ficavam por baixo e sumiam)
    instr = ("Pinte cada quadradinho com a cor do número. Deixe em branco os que não têm número."
             if not contas else "Faça a conta de cada quadradinho e pinte com a cor do resultado. Os sem conta ficam em branco.")
    return _at("Pinte pelo código", instr + f" Vai aparecer {ARTES_NOMES[arte]}!", nivel, "Cores e códigos", "pinte pelo código",
               base, base + "".join(gab))


TEMAS_PALAVRAS = {
    "frutas": ["UVA", "MANGA", "PERA", "BANANA", "CAJU", "GOIABA", "AMORA", "MELANCIA"],
    "brinquedos": ["BOLA", "PIPA", "BONECA", "PETECA", "DADO", "PATINETE", "CARRINHO", "TAMBOR"],
    "cozinha": ["PANELA", "GARFO", "COLHER", "PRATO", "COPO", "FACA", "TIGELA", "CANECA"],
    "cores": ["AZUL", "VERDE", "ROXO", "ROSA", "PRETO", "BRANCO", "CINZA", "VERMELHO"],
    "bichos": ["GATO", "CAVALO", "MACACO", "TATU", "PATO", "ZEBRA", "COELHO", "TUCANO"],
}
TITULO_TEMA = {"frutas": "frutas", "brinquedos": "brinquedos", "cozinha": "coisas da cozinha", "cores": "cores", "bichos": "bichos"}


def caca_palavras(rng, tema):
    palavras = TEMAS_PALAVRAS[tema]
    n = 12
    letras = "AAAABCDEEEEFGHIIILMNOOOPRRSSTTUUV"
    dirs8 = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
    for _ in range(400):
        g = [[""] * n for _ in range(n)]
        pos, okall = {}, True
        for p in palavras:
            for _ in range(300):
                dl, dc = rng.choice([(0, 1), (1, 0), (1, 1)])
                if dl * (len(p) - 1) >= n or dc * (len(p) - 1) >= n:
                    continue
                l = rng.randrange(n - dl * (len(p) - 1)); c = rng.randrange(n - dc * (len(p) - 1))
                cel = [(l + dl * k, c + dc * k) for k in range(len(p))]
                if all(g[a][b] in ("", p[k]) for k, (a, b) in enumerate(cel)):
                    for k, (a, b) in enumerate(cel):
                        g[a][b] = p[k]
                    pos[p] = cel
                    break
            else:
                okall = False; break
        if not okall:
            continue
        for a in range(n):
            for b in range(n):
                if not g[a][b]:
                    g[a][b] = rng.choice(letras)
        unico = True
        for p in palavras:
            achou = sum(1 for a in range(n) for b in range(n) for dl, dc in dirs8
                        if all(0 <= a + dl * k < n and 0 <= b + dc * k < n and g[a + dl * k][b + dc * k] == p[k] for k in range(len(p))))
            if achou != 1:
                unico = False; break
        if unico:
            break
    else:
        raise AssertionError("caça-palavras sem solução única")
    cel, x0, y0 = 13, (W - 156) / 2, 2
    s = [f'<rect x="{x0}" y="{y0}" width="{n * cel}" height="{n * cel}" rx="3" fill="none" stroke="{TRACO}" stroke-width="1"/>']
    for a in range(n):
        for b in range(n):
            s.append(_txt(x0 + b * cel + cel / 2, y0 + a * cel + cel / 2 + .4, g[a][b], 7.5, 800))
    ly = y0 + n * cel + 12
    for i, p in enumerate(palavras):
        x = 14 + (i % 4) * 43; y = ly + (i // 4) * 12
        s.append(f'<rect x="{x - 7}" y="{y - 2.5}" width="5" height="5" rx="1" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(_txt(x, y, p, 5.6, 800, anchor="start"))
    base = "".join(s)
    gab = []
    for p, c_ in pos.items():
        (a1, b1), (a2, b2) = c_[0], c_[-1]
        gab.append(f'<line x1="{x0 + b1 * cel + cel / 2}" y1="{y0 + a1 * cel + cel / 2}" x2="{x0 + b2 * cel + cel / 2}" y2="{y0 + a2 * cel + cel / 2}" stroke="{LAR}" stroke-width="8" stroke-linecap="round" opacity=".45"/>')
    return _at(f"Caça-palavras: {TITULO_TEMA[tema]}", "Encontre as 8 palavras escondidas. Elas estão em linha reta: para o lado, para baixo ou na diagonal.",
               2, "Cores e códigos", "caça-palavras", base, "".join(gab) + base)


def codigo_secreto(rng, msg):
    letras = sorted(set(msg.replace(" ", "")))
    extras = [l for l in "OTLSUMAEIRBCDP" if l not in letras][:max(0, 12 - len(letras))]
    letras = sorted(letras + extras)
    simbolos = ["circulo", "quadrado", "triangulo", "estrela", "coracao", "losango", "lua", "nuvem", "peixe", "flor",
                "sol", "maca", "balao", "casa", "arvore", "carro", "barco", "passaro"]
    assert len(letras) <= len(simbolos)
    chave = dict(zip(letras, rng.sample(simbolos, len(letras))))
    s = []
    for i, (le, si) in enumerate(sorted(chave.items())):
        x = 6 + (i % 6) * 29; y = 2 + (i // 6) * 30
        s.append(f'<rect x="{x}" y="{y}" width="26" height="27" rx="3" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(icone(si, x + 6, y + 2, 14))
        s.append(_txt(x + 13, y + 21.5, le, 7.5, 800, fonte="Baloo 2"))
    linhas_tab = math.ceil(len(chave) / 6)
    y = 12 + linhas_tab * 30
    gab = []
    for p in msg.split():
        larg = len(p) * 21
        x = (W - larg) / 2
        for k, ch in enumerate(p):
            cx = x + k * 21
            s.append(icone(chave[ch], cx + 3, y, 15))
            s.append(f'<line x1="{cx + 1}" y1="{y + 28}" x2="{cx + 19}" y2="{y + 28}" stroke="{TRACO}" stroke-width=".7"/>')
            gab.append(_txt(cx + 10, y + 22, ch, 9, 800, cor=LAR, fonte="Baloo 2"))
        y += 42
    assert y < H
    base = "".join(s)
    return _at("Código secreto", "Use a tabela para trocar cada figura por uma letra e descubra a mensagem.",
               2, "Cores e códigos", "código secreto", base, base + "".join(gab))
