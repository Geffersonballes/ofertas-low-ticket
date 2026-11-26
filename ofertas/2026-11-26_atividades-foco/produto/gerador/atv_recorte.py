"""Atividades do bump "Recortar e colar" (área 182x228 mm): área de colar em cima, peças com linha de
corte embaixo. Respostas conferidas com assert; gabarito mostra o resultado montado."""
import itertools

from atividades import W, H, _txt
from bumps_base import at, caixa_corte, faixa_recorte, LAR
from icones import icone, TRACO

CAT = "Recortar e colar"
Y_CORTE = 122
_ids = itertools.count(1)


def _peca_icone(nome, x, y, tam, borda=True):
    return (caixa_corte(x, y, tam, tam, 3) if borda else "") + icone(nome, x + tam * .1, y + tam * .1, tam * .8)


def _rotulo(x, y, t, tam=5.4, cor=TRACO):
    return _txt(x, y, t, tam, 800, cor=cor)


# ------------------------------------------------------------------ quebra-cabeça
def _pedaco(nome, S, n, r, c, x, y, borda=True):
    w = S / n
    cid = f"cp{next(_ids)}"
    out = (f'<defs><clipPath id="{cid}"><rect x="{c * w:.2f}" y="{r * w:.2f}" width="{w:.2f}" height="{w:.2f}"/></clipPath></defs>'
           f'<g transform="translate({x:.2f},{y:.2f})">'
           f'<rect x="0" y="0" width="{w:.2f}" height="{w:.2f}" fill="#fff"/>'
           f'<g clip-path="url(#{cid})" transform="translate({-c * w:.2f},{-r * w:.2f})">{icone(nome, 0, 0, S, traco=3)}</g>')
    if borda:
        out += f'<rect x="0" y="0" width="{w:.2f}" height="{w:.2f}" fill="none" stroke="#888" stroke-width=".5" stroke-dasharray="2 1.4"/>'
    return out + "</g>"


def quebra_cabeca(rng, nome, n, nivel, guia=True):
    S = 96 if n == 2 else 99
    x0, y0 = ((W - S) / 2, 6) if guia else (18, 6)
    s, g = [], []
    if guia:
        s.append(f'<g opacity=".13">{icone(nome, x0, y0, S, traco=3)}</g>')
    w = S / n
    for k in range(n + 1):
        s.append(f'<line x1="{x0 + k * w}" y1="{y0}" x2="{x0 + k * w}" y2="{y0 + S}" stroke="#bbb" stroke-width=".5"/>')
        s.append(f'<line x1="{x0}" y1="{y0 + k * w}" x2="{x0 + S}" y2="{y0 + k * w}" stroke="#bbb" stroke-width=".5"/>')
    s.append(f'<rect x="{x0}" y="{y0}" width="{S}" height="{S}" fill="none" stroke="{TRACO}" stroke-width="1"/>')
    if not guia:
        mx = x0 + S + 14
        s.append(f'<rect x="{mx}" y="{y0 + 20}" width="40" height="40" rx="3" fill="#fff7f1" stroke="#bbb" stroke-width=".5"/>')
        s.append(icone(nome, mx + 4, y0 + 24, 32, traco=4))
        s.append(_txt(mx + 20, y0 + 66, "modelo", 5, 800, cor="#777"))
    s.append(faixa_recorte(Y_CORTE - 6))
    pecas = [(r, c) for r in range(n) for c in range(n)]
    ordem = pecas[:]
    while ordem == pecas:
        rng.shuffle(ordem)
    cols = 2 if n == 2 else 5
    gap = 8 if n == 2 else 3
    larg = cols * w + (cols - 1) * gap
    for i, (r, c) in enumerate(ordem):
        px = (W - larg) / 2 + (i % cols) * (w + gap)
        py = Y_CORTE + (i // cols) * (w + gap)
        assert py + w <= H + .5, (n, i)
        s.append(_pedaco(nome, S, n, r, c, px, py))
    g.append(f'<rect x="{x0}" y="{y0}" width="{S}" height="{S}" fill="#fff"/>' + icone(nome, x0, y0, S, traco=3)
             + f'<rect x="{x0}" y="{y0}" width="{S}" height="{S}" fill="none" stroke="{LAR}" stroke-width="1.4"/>')
    base = "".join(s)
    return at(f"Quebra-cabeça de {n * n} peças", "Recorte as peças de baixo e monte a figura colando cada uma no seu lugar no quadro de cima.",
              nivel, CAT, base, base + "".join(g))


# ------------------------------------------------------------------ sombras
def sombras(rng, nomes):
    s, g = [], []
    n = len(nomes)
    tam = 28
    esp = (W - n * tam) / (n + 1)
    alvo = nomes[:]
    rng.shuffle(alvo)
    for i, nome in enumerate(alvo):
        x = esp + i * (tam + esp)
        s.append(f'<rect x="{x - 3}" y="16" width="{tam + 6}" height="{tam + 6}" rx="4" fill="none" stroke="#bbb" stroke-width=".5"/>')
        s.append(icone(nome, x, 19, tam, cor=TRACO, traco=3))
        g.append(f'<rect x="{x - 3}" y="16" width="{tam + 6}" height="{tam + 6}" rx="4" fill="#fff"/>' + icone(nome, x, 19, tam)
                 + f'<rect x="{x - 3}" y="16" width="{tam + 6}" height="{tam + 6}" rx="4" fill="none" stroke="{LAR}" stroke-width="1.2"/>')
    s.append(_rotulo(W / 2, 70, "Cada figura tem a sua sombra.", 5.4, "#666"))
    s.append(faixa_recorte(Y_CORTE - 6))
    pecas = nomes[:]
    while pecas == alvo:
        rng.shuffle(pecas)
    tp = 32
    esp2 = (W - n * tp) / (n + 1)
    for i, nome in enumerate(pecas):
        s.append(_peca_icone(nome, esp2 + i * (tp + esp2), Y_CORTE + 10, tp))
    base = "".join(s)
    return at("Cada um na sua sombra", "Recorte as figuras de baixo e cole cada uma em cima da sua sombra.", 1, CAT, base, base + "".join(g))


# ------------------------------------------------------------------ tamanho
def do_menor_ao_maior(rng, nome):
    tams = [14, 20, 26, 32]
    s, g = [], []
    for i in range(4):
        x = 8 + i * 44
        s.append(f'<rect x="{x}" y="20" width="38" height="38" rx="4" fill="none" stroke="{TRACO}" stroke-width=".7"/>')
        s.append(_txt(x + 19, 66, str(i + 1), 8, 800, fonte="Baloo 2"))
        t = tams[i]
        g.append(icone(nome, x + 19 - t / 2, 39 - t / 2, t))
    s.append(_rotulo(W / 2, 80, "1 é o menor · 4 é o maior", 5.4, "#666"))
    s.append(faixa_recorte(Y_CORTE - 6))
    ordem = tams[:]
    while ordem == tams:
        rng.shuffle(ordem)
    for i, t in enumerate(ordem):
        x = 8 + i * 44
        s.append(caixa_corte(x, Y_CORTE + 10, 38, 38, 3))
        s.append(icone(nome, x + 19 - t / 2, Y_CORTE + 29 - t / 2, t))
    base = "".join(s)
    return at("Do menor ao maior", "Recorte as figuras e cole nos quadros em ordem: da menor (1) até a maior (4).", 1, CAT, base, base + "".join(g))


# ------------------------------------------------------------------ classificar
GRUPOS = {
    "ceu_agua": (("No céu", ["sol", "lua", "nuvem", "estrela", "pipa", "passaro", "balao"]), ("Na água", ["peixe", "barco", "pato", "ilha"])),
    "frutas_brinq": (("Frutas", ["maca", "banana", "uva"]), ("Brinquedos", ["bola", "dado", "pipa", "balao", "carro"])),
    "bichos_coisas": (("Bichos", ["gato", "pato", "peixe", "passaro"]), ("Coisas", ["copo", "chave", "lapis", "tesoura", "anel"])),
    "comer_brincar": (("De comer", ["maca", "banana", "uva", "sorvete", "ovo"]), ("De brincar", ["bola", "dado", "pipa", "carro", "balao"])),
    "casa_natureza": (("Na natureza", ["arvore", "flor", "sol", "nuvem", "ilha"]), ("Dentro de casa", ["copo", "lapis", "tesoura", "chave", "dado"])),
}


def classifique(rng, chave, por_grupo, nivel):
    (t1, l1), (t2, l2) = GRUPOS[chave]
    assert not set(l1) & set(l2), chave
    a = rng.sample(l1, por_grupo)
    b = rng.sample(l2, por_grupo)
    s, g = [], []
    for k, (t, itens) in enumerate([(t1, a), (t2, b)]):
        x = 2 + k * 91
        s.append(f'<rect x="{x}" y="2" width="87" height="104" rx="5" fill="none" stroke="{TRACO}" stroke-width=".8"/>')
        s.append(f'<rect x="{x}" y="2" width="87" height="14" rx="5" fill="#fff1e8"/>')
        s.append(_txt(x + 43.5, 9.5, t, 7, 800, fonte="Baloo 2"))
        for i, nome in enumerate(itens):
            g.append(icone(nome, x + 6 + (i % 3) * 27, 22 + (i // 3) * 28, 22))
    s.append(faixa_recorte(Y_CORTE - 6))
    pecas = a + b
    rng.shuffle(pecas)
    n = len(pecas)
    cols = min(n, 6)
    tp = 26
    esp = (W - cols * tp) / (cols + 1)
    for i, nome in enumerate(pecas):
        s.append(_peca_icone(nome, esp + (i % cols) * (tp + esp), Y_CORTE + 4 + (i // cols) * (tp + 8), tp))
    base = "".join(s)
    return at(f"{t1} ou {t2.lower()}?", "Recorte as figuras e cole cada uma no grupo certo.", nivel, CAT, base, base + "".join(g))


# ------------------------------------------------------------------ padrão
def padrao_cola(rng, ciclos):
    s, g = [], []
    respostas = []
    for i, ciclo in enumerate(ciclos):
        y = 4 + i * 36
        seq = (ciclo * 4)[:5]
        resp = (ciclo * 4)[5]
        respostas.append(resp)
        s.append(f'<rect x="1" y="{y}" width="{W - 2}" height="30" rx="5" fill="none" stroke="#bbb" stroke-width=".5"/>')
        for j, nome in enumerate(seq):
            s.append(icone(nome, 8 + j * 26, y + 4, 22))
        bx = 8 + 5 * 26
        s.append(f'<rect x="{bx}" y="{y + 3}" width="24" height="24" rx="3" fill="none" stroke="{TRACO}" stroke-width=".8" stroke-dasharray="2 1.5"/>')
        g.append(icone(resp, bx + 1, y + 4, 22))
    s.append(faixa_recorte(Y_CORTE - 6))
    todos = list({n for c in ciclos for n in c})
    distr = [n for n in todos if n not in respostas][:3]
    pecas = respostas + distr
    rng.shuffle(pecas)
    tp = 26
    cols = len(pecas)
    esp = (W - cols * tp) / (cols + 1)
    for i, nome in enumerate(pecas):
        s.append(_peca_icone(nome, esp + i * (tp + esp), Y_CORTE + 10, tp))
    s.append(_rotulo(W / 2, Y_CORTE + 50, "Sobram algumas peças: nem todas entram!", 5, "#666"))
    base = "".join(s)
    return at("Complete a fila", "Descubra o que se repete em cada fila, recorte a figura certa e cole no quadrinho pontilhado.", 1, CAT, base, base + "".join(g))


# ------------------------------------------------------------------ nível 2: sílabas
def silabas_cola(rng, chaves, palavras):
    s, g = [], []
    todas = []
    for i, k in enumerate(chaves):
        pal, sil = palavras[k]
        assert "".join(sil) == pal and len(sil) >= 2
        y = 4 + i * 36
        s.append(f'<rect x="1" y="{y}" width="{W - 2}" height="31" rx="5" fill="none" stroke="#bbb" stroke-width=".5"/>')
        s.append(icone(k, 6, y + 3, 25))
        for q, t in enumerate(sil):
            x = 44 + q * 30
            s.append(f'<rect x="{x}" y="{y + 5}" width="26" height="20" rx="3" fill="none" stroke="{TRACO}" stroke-width=".8" stroke-dasharray="2 1.5"/>')
            g.append(_txt(x + 13, y + 15, t, 7.5, 800, cor=LAR, fonte="Baloo 2"))
            todas.append(t)
    s.append(faixa_recorte(Y_CORTE - 6))
    pecas = todas[:]
    rng.shuffle(pecas)
    cols = 6
    for i, t in enumerate(pecas):
        x = 8 + (i % cols) * 29
        y = Y_CORTE + 2 + (i // cols) * 26
        assert y + 20 <= H
        s.append(caixa_corte(x, y, 26, 20, 3))
        s.append(_txt(x + 13, y + 10, t, 7.5, 800, fonte="Baloo 2"))
    base = "".join(s)
    return at("Monte as palavras", "Recorte as sílabas e cole nos quadrinhos para formar o nome de cada figura.", 2, CAT, base, base + "".join(g))


def ordem_numeros(rng, n=6, maxi=99):
    nums = rng.sample(range(1, maxi + 1), n)
    ordem = sorted(nums)
    s, g = [], []
    for i in range(n):
        x = 6 + i * 29
        s.append(f'<rect x="{x}" y="24" width="26" height="26" rx="4" fill="none" stroke="{TRACO}" stroke-width=".8" stroke-dasharray="2 1.5"/>')
        if i < n - 1:
            s.append(_txt(x + 27.5, 37, "<", 6, 800, cor="#999"))
        g.append(_txt(x + 13, 37, str(ordem[i]), 10, 800, cor=LAR, fonte="Baloo 2"))
    s.append(_rotulo(W / 2, 64, "do menor para o maior →", 5.4, "#666"))
    s.append(faixa_recorte(Y_CORTE - 6))
    for i, v in enumerate(nums):
        x = 6 + i * 29
        s.append(caixa_corte(x, Y_CORTE + 10, 26, 26, 3))
        s.append(_txt(x + 13, Y_CORTE + 23, str(v), 10, 800, fonte="Baloo 2"))
    assert sorted(nums) == ordem and len(set(nums)) == n
    base = "".join(s)
    return at("Coloque em ordem", "Recorte os números e cole nos quadrinhos do menor para o maior.", 2, CAT, base, base + "".join(g))


def contas_cola(rng, op, maxi):
    vistos, contas = set(), []
    while len(contas) < 5:
        if op == "+":
            a = rng.randint(1, maxi - 1); b = rng.randint(1, maxi - a); r = a + b
        else:
            a = rng.randint(2, maxi); b = rng.randint(1, a - 1); r = a - b
        if r in vistos:
            continue
        vistos.add(r); contas.append((a, b, r))
    s, g = [], []
    for i, (a, b, r) in enumerate(contas):
        y = 4 + i * 21
        s.append(_txt(70, y + 9, f"{a} {'+' if op == '+' else '−'} {b} =", 9, 800, anchor="end", fonte="Baloo 2"))
        s.append(f'<rect x="76" y="{y}" width="24" height="18" rx="3" fill="none" stroke="{TRACO}" stroke-width=".8" stroke-dasharray="2 1.5"/>')
        g.append(_txt(88, y + 9, str(r), 9, 800, cor=LAR, fonte="Baloo 2"))
    s.append(faixa_recorte(Y_CORTE - 6))
    extra = next(v for v in range(maxi + 1, 0, -1) if v not in vistos)
    pecas = [r for *_, r in contas] + [extra]
    rng.shuffle(pecas)
    for i, v in enumerate(pecas):
        x = 8 + i * 29
        s.append(caixa_corte(x, Y_CORTE + 10, 24, 18, 3))
        s.append(_txt(x + 12, Y_CORTE + 19, str(v), 9, 800, fonte="Baloo 2"))
    s.append(_rotulo(W / 2, Y_CORTE + 40, "Sobra uma peça.", 5, "#666"))
    base = "".join(s)
    return at("Cole o resultado", "Resolva cada conta, recorte o resultado certo e cole no quadrinho.", 2, CAT, base, base + "".join(g))
