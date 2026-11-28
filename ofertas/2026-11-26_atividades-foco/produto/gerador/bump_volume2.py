"""Bump 7 — Volume 2: mais 120 atividades novas (mesmos 2 níveis e categorias do caderno, plano de 30 dias
por nível, gabarito). Temas, cenas, desenhos de ligar pontos, artes de pintar, palavras e mensagens
são diferentes do volume 1; labirintos, sudokus, contagens etc. saem de outra semente."""
import math
import random

import atividades2 as B
import gerar_completo as GC
from bumps_base import Bump

SEMENTE = 2027_0201
BUMP = Bump("Volume 2", "volume-2", "MAIS 120 ATIVIDADES · 2 NÍVEIS · PLANO DE 30 DIAS")

# ------------------------------------------------------------------ temas novos (nenhum repete o volume 1)
NOVAS_CENAS = {
    "jardim": [("sol", 146, 2, 26), ("nuvem", 6, 6, 30), ("nuvem", 88, 4, 22), ("passaro", 54, 22, 16), ("arvore", 4, 44, 58),
               ("flor", 68, 86, 18), ("flor", 88, 88, 14), ("flor", 104, 86, 18), ("casa", 120, 48, 54), ("pato", 66, 58, 20)],
    "cidade": [("casa", 2, 50, 46), ("carro", 50, 84, 24), ("casa", 76, 50, 46), ("arvore", 124, 46, 50), ("bola", 160, 92, 12),
               ("sol", 6, 2, 24), ("nuvem", 40, 6, 26), ("nuvem", 112, 2, 20), ("passaro", 80, 22, 16), ("pipa", 150, 4, 20)],
    "piquenique": [("arvore", 2, 40, 60), ("sol", 150, 2, 26), ("nuvem", 70, 4, 26), ("uva", 80, 82, 18), ("banana", 102, 84, 18),
                   ("maca", 124, 86, 16), ("sorvete", 146, 78, 22), ("passaro", 110, 22, 16), ("flor", 62, 88, 14), ("bola", 42, 88, 14)],
    "rio": [("barco", 10, 44, 34), ("barco", 112, 50, 28), ("peixe", 20, 86, 18), ("peixe", 70, 90, 16), ("peixe", 140, 86, 18),
            ("pato", 66, 54, 22), ("sol", 150, 2, 24), ("nuvem", 20, 4, 28), ("nuvem", 90, 2, 22), ("passaro", 62, 20, 14)],
    "ceu": [("lua", 10, 4, 26), ("estrela", 50, 6, 12), ("estrela", 84, 14, 14), ("estrela", 120, 4, 12), ("estrela", 152, 20, 14),
            ("nuvem", 58, 30, 24), ("balao", 132, 36, 24), ("casa", 10, 50, 52), ("arvore", 70, 48, 50), ("carro", 132, 80, 28)],
}
NOVOS_PONTOS = {
    "pipa": [(100, 10), (160, 80), (100, 170), (40, 80), (100, 10)],
    "sorvete": [(70, 100), (100, 190), (130, 100), (150, 85), (150, 60), (130, 40), (100, 30), (70, 40), (50, 60), (50, 85), (70, 100)],
    "guarda-chuva": [(20, 100), (40, 55), (100, 25), (160, 55), (180, 100), (140, 92), (100, 100), (60, 92), (20, 100)],
    "castelo": [(20, 190), (20, 60), (40, 60), (40, 80), (60, 80), (60, 60), (80, 60), (80, 80), (120, 80), (120, 60), (140, 60),
                (140, 80), (160, 80), (160, 60), (180, 60), (180, 190), (20, 190)],
    "pinheiro": [(100, 10), (140, 60), (120, 60), (160, 110), (130, 110), (175, 160), (110, 160), (110, 190), (90, 190), (90, 160),
                 (25, 160), (70, 110), (40, 110), (80, 60), (60, 60), (100, 10)],
    "borboleta": [(100, 40), (70, 10), (25, 20), (20, 70), (60, 95), (25, 130), (35, 180), (80, 175), (100, 130), (120, 175),
                  (165, 180), (175, 130), (140, 95), (180, 70), (175, 20), (130, 10), (100, 40)],
}
# cabo do guarda-chuva e corpo da borboleta já vêm desenhados (o caminho de pontos é só o contorno fechado)
TRACO_PRONTO = {
    "guarda-chuva": "M100 100 L 100 170 Q 100 184 88 183 Q 77 182 77 172",
    "borboleta": "M100 54 C 93 68, 93 110, 100 120 C 107 110, 107 68, 100 54 Z",
}
NOVAS_ARTES = {
    "cogumelo": ["....1111....", "..11111111..", ".11..1111.1.", "111111..1111", "111111111111", "....5555....",
                 "....5555....", "....5555....", "....5555....", "...555555...", "333333333333", "333333333333"],
    "maca": [".....5.33...", ".....5333...", "..1115111...", ".1111111111.", "111111111111", "111111111111",
             "111111111111", "111111111111", ".1111111111.", ".1111111111.", "..11111111..", "...111.111.."],
    "borboleta": ["..5......5..", "...5....5...", "4444.55.4444", "422445544224", "422445544224", "444445544444",
                  ".4444554444.", "..44455444..", ".4444554444.", "444445544444", "444..55..444", ".....55....."],
    "foguete": [".....11.....", "....1111....", "....4444....", "...444444...", "...442244...", "...442244...",
                "...444444...", "...444444...", "..11444411..", ".1114444111.", ".11.6666.11.", ".....66....."],
    "pipa": [".....44.....", "....4422....", "...444222...", "..44442222..", ".4444422222.", "444444222222",
             ".1111133333.", "..11113333..", "...111333...", "....1133....", ".....5......", "......5....."],
    "carro": ["............", "............", "...111111...", "..14411441..", ".1111111111.", "111111111112",
              "111111111111", "..55....55..", "..55....55..", "............", "333333333333", "333333333333"],
    "guarda-chuva": [".....11.....", "...111111...", "..11111111..", ".1111111111.", "111111111111", "1.11.11.11.1",
                     ".....5......", ".....5......", ".....5......", ".....5......", ".....5.5....", "......5....."],
    # fatia de melancia (no lugar do guarda-chuva do pinte, que caía no dia seguinte ao "ligue" do guarda-chuva)
    "melancia": ["............", "............", "311111111113", "311511115113", ".3111111113.", ".3115111513.",
                 "..31111113..", "..31151113..", "...311113...", "....3333....", "............", "............"],
    "castelo": ["4.4......4.4", "444......444", "444.4..4.444", "444444444444", "442444444244", "444444444444",
                "444445544444", "444455554444", "444455554444", "444455554444", "333333333333", "333333333333"],
}
NOVOS_NOMES_ARTE = {"cogumelo": "um cogumelo", "maca": "uma maçã", "borboleta": "uma borboleta", "foguete": "um foguete",
                    "pipa": "uma pipa", "carro": "um carro", "guarda-chuva": "um guarda-chuva", "castelo": "um castelo", "melancia": "uma melancia",
                    "arco-iris": "um arco-íris"}
NOVOS_TEMAS_PALAVRAS = {
    "escola": ["CADERNO", "BORRACHA", "MOCHILA", "ESTOJO", "LIVRO", "TESOURA", "COLA", "GIZ"],
    "transportes": ["CARRO", "BARCO", "TREM", "MOTO", "NAVIO", "BICICLETA", "FOGUETE", "CANOA"],
    "natureza": ["RIO", "MAR", "SOL", "LUA", "FLOR", "PEDRA", "MONTANHA", "ESTRELA"],
    "fazenda": ["VACA", "PORCO", "GALINHA", "CABRA", "OVELHA", "BURRO", "PERU", "GANSO"],
}
NOVOS_TITULOS = {"escola": "material escolar", "transportes": "transportes", "natureza": "natureza", "fazenda": "bichos da fazenda"}
NOVOS_TEMAS_LOGICA = [
    dict(nomes=["Gabi", "Léo", "Sofia"], verbo="desenhou", itens=[("casa", "casa", "a casa"), ("arvore", "árvore", "a árvore"), ("flor", "flor", "a flor")]),
    dict(nomes=["Pedro", "Clara", "Miguel"], verbo="come", itens=[("sorvete", "sorvete", "o sorvete"), ("ovo", "ovo", "o ovo"), ("uva", "uva", "a uva")]),
    dict(nomes=["Alice", "Heitor", "Laura"], verbo="brinca com", itens=[("bola", "bola", "a bola"), ("pipa", "pipa", "a pipa"), ("dado", "dado", "o dado")]),
]
MENSAGENS = ["MUITO BEM", "QUE LEGAL", "CONTINUE ASSIM"]


def _registrar():
    B.CENAS.update(NOVAS_CENAS)
    B.ESPELHAVEIS.add("pato")
    B.DESENHOS_PONTOS.update(NOVOS_PONTOS)
    B.TRACO_PRONTO.update(TRACO_PRONTO)
    B.ROTULO_AO_LADO.update({"guarda-chuva": [(100, 100)]})
    B.TEMAS_PALAVRAS.update(NOVOS_TEMAS_PALAVRAS)
    B.TITULO_TEMA.update(NOVOS_TITULOS)
    B.ARTES_NOMES.update(NOVOS_NOMES_ARTE)
    if not getattr(B, "_arte_v2", False):
        arte_v1, cena_v1 = B._arte, B._desenha_cena

        def arte(nome):
            if nome == "arco-iris":
                g = [[0] * 12 for _ in range(12)]
                faixas = [(5.4, 6.6, 1), (4.2, 5.4, 6), (3.0, 4.2, 2), (1.8, 3.0, 3)]
                for l in range(12):
                    for c in range(12):
                        d = math.hypot(c + .5 - 6, l + .5 - 10)
                        for a, b, v in faixas:
                            if a <= d < b and l < 10:
                                g[l][c] = v
                g[10] = [0, 0, 5, 5, 5, 0, 0, 5, 5, 5, 0, 0]
                return g
            if nome in NOVAS_ARTES:
                linhas = NOVAS_ARTES[nome]
                assert len(linhas) == 12 and all(len(r) == 12 for r in linhas), nome
                return [[0 if ch == "." else int(ch) for ch in r] for r in linhas]
            return arte_v1(nome)

        def cena(objs, nome, mods):
            return cena_v1(objs, "praia" if nome == "rio" else nome, mods)
        B._arte, B._desenha_cena, B._arte_v2 = arte, cena, True


NOMES_INI = {"passaro": "o passarinho", "barco": "o barco", "peixe": "o peixe", "carro": "o carro", "balao": "o balão",
             "pato": "o patinho", "gato": "o gato", "pipa": "a pipa"}
NOMES_FIM = {"arvore": "a árvore", "casa": "a casa", "nuvem": "a nuvem", "flor": "a flor", "estrela": "a estrela",
             "ilha": "a ilha", "sol": "o sol", "barco": "o barco"}


def labirinto(nivel, rng, cols, lins, ini, fim):
    """Igual ao do volume 1, com nomes para os ícones novos."""
    from atividades import _gera_labirinto, _desenha_labirinto, W as W_, H as H_
    from icones import icone
    cel = min((W_ - 10) / cols, (H_ - 52) / lins)
    x0, y0 = (W_ - cols * cel) / 2, 25
    paredes, cam = B.labirinto_bom(cols, lins, rng)
    esp = 1.8 if cel > 18 else (1.4 if cel > 12 else 1.0)
    base = (_desenha_labirinto(paredes, cols, lins, x0, y0, cel, esp)
            + icone(ini, x0 + cel / 2 - 11, y0 - 23, 22)
            + icone(fim, x0 + (cols - 0.5) * cel - 11, y0 + lins * cel + 1, 22))
    pts = " ".join(f"{x0 + (c + .5) * cel:.1f},{y0 + (l + .5) * cel:.1f}" for c, l in cam)
    sol = f'<polyline points="{pts}" fill="none" stroke="{B.LAR}" stroke-width="{cel * .35:.1f}" stroke-linejoin="round" stroke-linecap="round" opacity=".8"/>'
    instr = (f"Leve {NOMES_INI[ini]} até {NOMES_FIM[fim]} sem atravessar as paredes." if nivel == 1
             else f"Leve {NOMES_INI[ini]} até {NOMES_FIM[fim]}. Use o dedo primeiro e depois o lápis.")
    return B._at("Labirinto", instr, nivel, "Lógica", "labirinto", base, sol + base)


def nivel1(rng):
    cat = {k: [] for k in ["Atenção", "Memória", "Padrões", "Lógica", "Traçado", "Cores e códigos"]}
    var = B.VARIANTES[:]
    vistos = {}  # variante → filas e posições já usadas no nível

    def diferente_variado(v, pag):
        """"Qual é diferente?" sem duas filas da mesma figura na folha e sem repetir a mesma fila (variante,
        linha e posição) de uma folha anterior. Gasta o rng principal como antes; o resto sai de um rng derivado."""
        for _ in v:
            rng.randrange(5)
        alt = random.Random(f"dif-v2-{pag}")
        chave = lambda x: (x[0], tuple(sorted(x[1].items())))
        linhas, nomes = [], set()
        for x in v:
            if x[0] in nomes:
                livres = [y for y in B.VARIANTES if y[0] not in nomes and y not in v]
                menos = min(len(vistos.get(chave(y), [])) for y in livres)
                livres = [y for y in livres if len(vistos.get(chave(y), [])) == menos]
                x = livres[alt.randrange(len(livres))]
            nomes.add(x[0]); linhas.append(x)
        alt.shuffle(linhas)
        ks = []
        for i, x in enumerate(linhas):
            antes = vistos.setdefault(chave(x), [])
            ok = [k for k in range(5) if all(k != k0 for _, k0 in antes)] or list(range(5))
            k = ok[alt.randrange(len(ok))]
            antes.append((i, k)); ks.append(k)

        class Fixo:
            def __init__(self, ks):
                self.it = iter(ks)

            def randrange(self, n):
                return next(self.it)
        return B.diferente(Fixo(ks), linhas)
    for p in range(4):
        rng.shuffle(var)
        cat["Atenção"].append(("dif", lambda v=var[:6], p=p: diferente_variado(v, p)))
    tipos_cont = [["pato", "bola", "dado", "pipa"], ["sorvete", "uva", "ovo", "gato"], ["chave", "copo", "anel", "lapis"],
                  ["bola", "flor", "sorvete", "carro"], ["gato", "pato", "dado", "balao"]]
    for t, (a, b) in zip(tipos_cont, [(1, 5), (2, 6), (3, 8), (3, 9), (4, 10)]):
        cat["Atenção"].append(("cont", lambda t=t, a=a, b=b: B.contar(rng, t, a, b)))
    for cena in ["jardim", "cidade", "piquenique"]:
        cat["Atenção"].append(("erros", lambda c=cena: B.diferencas(rng, 1, c, 5)))
    for nv, no in [(3, 6), (3, 6), (3, 6), (4, 6), (4, 8), (4, 8), (5, 8), (5, 8)]:
        cat["Memória"].append(("mem", lambda nv=nv, no=no: B.memoria_figuras(rng, 1, nv, no)))
    moldes = [["A", "B"], ["A", "A", "B"], ["A", "B", "B"], ["A", "B", "C"], ["A", "A", "B", "B"]]
    filas_n1 = set()  # nenhuma fila repete no nível, nem no caderno (B.CHECAR_FILAS)
    for p in range(10):
        dif = moldes[:3] if p < 4 else moldes
        ciclos = []
        for _ in range(5):
            m = rng.choice(dif)
            figs = rng.sample(B.FIG_PADRAO, len(set(m)))
            mapa = dict(zip(sorted(set(m)), figs))
            ciclos.append([mapa[x] for x in m])
        ciclos = B.sem_repetir_filas(ciclos, filas_n1, B.extra_n1("v2-n1"))  # não gasta rng: as outras páginas não mudam
        cat["Padrões"].append(("pad", lambda c=ciclos: B.padroes(rng, 1, c)))
    pares_lab = [("pato", "flor"), ("gato", "casa"), ("carro", "flor"), ("barco", "ilha"), ("balao", "sol"),
                 ("passaro", "nuvem"), ("peixe", "barco"), ("pipa", "estrela")]
    for (c, l), (a, b) in zip([(5, 6), (5, 7), (6, 7), (6, 8), (7, 8), (7, 9), (8, 10), (8, 11)], pares_lab):
        cat["Lógica"].append(("lab", lambda c=c, l=l, a=a, b=b: labirinto(1, rng, c, l, a, b)))
    for d in [11, 10, 9, 8]:
        cat["Lógica"].append(("sud", lambda d=d: B.sudoku_figuras(rng, d)))
    cat["Lógica"] = [cat["Lógica"][i] for i in [0, 1, 8, 2, 3, 9, 4, 5, 10, 6, 7, 11]]
    for des, alvo in [("pipa", 10), ("sorvete", 13), ("guarda-chuva", 15), ("castelo", 17), ("pinheiro", 20)]:
        cat["Traçado"].append(("pts", lambda d=des, a=alvo: B.ligue_pontos(rng, 1, d, a)))
    tipos_tr = [["curva", "onda", "degraus", "zigue", "ponte"], ["montanha", "reta", "onda2", "laco", "curva"],
                ["degraus", "zigue", "curva", "onda", "montanha"], ["ponte", "laco", "reta", "onda2", "degraus"],
                ["onda", "montanha", "laco", "curva", "zigue"]]
    figs = ["pato", "gato", "bola", "dado", "pipa", "sorvete", "ilha", "barco", "casa", "arvore", "flor", "sol", "lua", "carro"]
    for t in tipos_tr:
        pares = [tuple(rng.sample(figs, 2)) for _ in range(5)]
        cat["Traçado"].append(("tr", lambda t=t, p=pares: B.tracado(rng, t, p)))
    cat["Traçado"] = [cat["Traçado"][i] for i in [5, 0, 6, 1, 7, 2, 8, 3, 9, 4]]
    for arte in ["cogumelo", "maca", "pipa", "carro", "melancia", "foguete", "borboleta", "arco-iris"]:
        cat["Cores e códigos"].append(("pinte", lambda a=arte: B.pinte_codigo(rng, 1, a)))
    return cat


def nivel2(rng):
    cat = {k: [] for k in ["Atenção", "Memória", "Padrões", "Lógica", "Traçado", "Cores e códigos"]}
    gradesubs = [[("passaro", dict(espelhar=True)), ("flor", dict(variante="4petalas")), ("lua", dict(espelhar=True))],
                 [("maca", dict(variante="semfolha")), ("carro", dict(variante="semroda")), ("estrela", dict(variante="6pontas"))],
                 [("barco", dict(espelhar=True)), ("sol", dict(variante="poucosraios")), ("peixe", dict(espelhar=True))],
                 [("banana", dict(espelhar=True)), ("casa", dict(variante="semjanela")), ("balao", dict(espelhar=True))]]
    qt = [["pato", "bola", "pipa"], ["sorvete", "dado", "gato", "uva"], ["ovo", "chave", "copo", "lapis"]]
    cat["Atenção"] = [("erros", lambda: B.diferencas(rng, 2, "jardim", 7)), ("gr", lambda: B.diferente_grade(rng, gradesubs[0])),
                      ("qt", lambda: B.quantos_tem(rng, qt[0])), ("erros", lambda: B.diferencas(rng, 2, "cidade", 7)),
                      ("gr", lambda: B.diferente_grade(rng, gradesubs[1])), ("erros", lambda: B.diferencas(rng, 2, "piquenique", 7)),
                      ("qt", lambda: B.quantos_tem(rng, qt[1])), ("gr", lambda: B.diferente_grade(rng, gradesubs[2])),
                      ("erros", lambda: B.diferencas(rng, 2, "rio", 7)), ("qt", lambda: B.quantos_tem(rng, qt[2])),
                      ("gr", lambda: B.diferente_grade(rng, gradesubs[3])), ("erros", lambda: B.diferencas(rng, 2, "ceu", 7))]
    cat["Memória"] = [("mem", lambda: B.memoria_figuras(rng, 2, 5, 10)), ("lug", lambda: B.memoria_lugares(rng, 3)),
                      ("mem", lambda: B.memoria_figuras(rng, 2, 6, 10)), ("mem", lambda: B.memoria_figuras(rng, 2, 6, 10)),
                      ("lug", lambda: B.memoria_lugares(rng, 4)), ("mem", lambda: B.memoria_figuras(rng, 2, 7, 10)),
                      ("lug", lambda: B.memoria_lugares(rng, 5)), ("mem", lambda: B.memoria_figuras(rng, 2, 8, 10))]

    filas_usadas = set()  # nenhuma fila repete entre as folhas de "O que vem depois?" do nível

    def ciclos_rot():
        tipos = [
            lambda: [("triangulo", g, False) for g in (0, 90, 180, 270)],
            lambda: [("lua", 0, False), ("lua", 0, True)],
            lambda: [("peixe", 0, False), ("peixe", 0, True), ("estrela", 0, False)],
            lambda: [("coracao", 0, False), ("coracao", 180, False), ("coracao", 180, False)],
            lambda: [("passaro", 0, False), ("passaro", 0, True), ("passaro", 0, True), ("sol", 0, False)],
            lambda: [(f, 0, False) for f in rng.sample(B.FIG_PADRAO, 4)],
            lambda: [("banana", 0, False), ("banana", 90, False), ("banana", 180, False)],
        ]
        return B.sem_repetir_filas([f() for f in rng.sample(tipos, 5)], filas_usadas, B.extra_n2("v2-n2"))
    pad = []
    for f in [1, None, 2, 1, None, 3, 2, None, 3, None]:
        if f is None:
            c = ciclos_rot()
            pad.append(("padr", lambda c=c: B.padroes(rng, 2, c)))
        else:
            pad.append(("seq", lambda f=f: B.sequencias(rng, f)))
    cat["Padrões"] = pad
    labs = [(11, 13, "pato", "ilha"), (12, 15, "pipa", "nuvem"), (14, 17, "gato", "arvore"), (15, 19, "passaro", "flor")]  # gato→casa já está no Nível 1
    t = NOVOS_TEMAS_LOGICA
    cat["Lógica"] = [("sud", lambda: B.sudoku6(rng, 20)), ("lab", lambda: labirinto(2, rng, *labs[0])),
                     ("gl", lambda: B.grade_logica(rng, t[0])), ("sud", lambda: B.sudoku6(rng, 18)),
                     ("lab", lambda: labirinto(2, rng, *labs[1])), ("gl", lambda: B.grade_logica(rng, t[1])),
                     ("sud", lambda: B.sudoku6(rng, 17)), ("lab", lambda: labirinto(2, rng, *labs[2])),
                     ("sud", lambda: B.sudoku6(rng, 16)), ("gl", lambda: B.grade_logica(rng, t[2])),
                     ("lab", lambda: labirinto(2, rng, *labs[3])), ("sud", lambda: B.sudoku6(rng, 15))]
    tr = []
    for (des, alvo), seg in zip([("sorvete", 24), ("castelo", 28), ("pinheiro", 32), ("guarda-chuva", 34), ("borboleta", 40)],
                                [8, 10, 12, 14, 16]):
        tr.append(("cop", lambda s=seg: B.copie_desenho(rng, s)))
        tr.append(("pts", lambda d=des, a=alvo: B.ligue_pontos(rng, 2, d, a)))
    cat["Traçado"] = tr
    cat["Cores e códigos"] = [("caca", lambda: B.caca_palavras(rng, "escola")), ("cod", lambda: B.codigo_secreto(rng, MENSAGENS[0])),
                              ("pinte", lambda: B.pinte_codigo(rng, 2, "castelo", contas=True)),
                              ("caca", lambda: B.caca_palavras(rng, "transportes")),
                              ("cod", lambda: B.codigo_secreto(rng, MENSAGENS[1])), ("caca", lambda: B.caca_palavras(rng, "natureza")),
                              ("cod", lambda: B.codigo_secreto(rng, MENSAGENS[2])), ("caca", lambda: B.caca_palavras(rng, "fazenda"))]
    return cat


def rodape(num, dia=None):
    dir_ = f'<span class="feito">Dia {dia} <span>Feito!<span class="caixa"></span></span></span>' if dia else "<span></span>"
    return f'<div class="rodape"><span>Dez Minutinhos · Volume 2 · página {num}</span>{dir_}</div>'


def como_usar(pags):
    return BUMP.pagina_texto("Como usar o Volume 2", f"""
  <p>O Volume 2 tem <b>120 atividades novas</b>, nos mesmos dois níveis e nas mesmas seis categorias do caderno principal,
  com outro plano de 30 dias. Use quando terminar o primeiro, ou para variar.</p>
  <ol class="passos">
    <li><b>Escolha o nível pela idade.</b> Nível 1 (4 a 6 anos) sem leitura; Nível 2 (7 a 10 anos) com leitura inicial.</li>
    <li><b>Siga o plano.</b> Nível 1 na página {pags['plano1']}, Nível 2 na página {pags['plano2']}. Duas folhas por dia, de tipos diferentes.</li>
    <li><b>Imprima a semana de uma vez</b> (14 folhas), em preto e branco, papel A4 comum.</li>
    <li><b>Confira no gabarito</b>, a partir da página {pags['gabarito']}.</li>
  </ol>
  <p class="aviso">Uso permitido: imprima quantas vezes quiser para as crianças da sua família. Não é permitido revender nem repassar o arquivo.</p>""", 2)


def gerar():
    _registrar()
    import json
    v1 = json.loads((GC.SAIDA / "completo.json").read_text())["sequencias"]  # rode gerar_completo.py antes
    B.SEQ_USADAS.update(tuple(x) for x in v1)
    B.CHECAR_JANELAS = True
    for x in v1:
        B.SEQ_JANELAS.update(B._janelas(x))
    # "O que vem depois?": nenhuma fila do Volume 2 igual, girada ou deslocada em relação a uma fila do caderno
    # (nem a outra fila do Volume 2, nos dois níveis)
    filas_v1 = {tuple(tuple(x) for x in f) for _, f in json.loads((GC.SAIDA / "completo.json").read_text())["filas"]}
    assert len(filas_v1) == 70, "rode gerar_completo.py antes"
    B.CHECAR_FILAS = True
    B.FILAS_PROIBIDAS.update(filas_v1)
    B.NUCLEOS_PROIBIDOS.update(B.nucleo(f) for f in filas_v1 if B.nucleo(f) is not None)
    B.FILAS_MOSTRADAS.clear()
    GC.rodape = rodape
    GC.topo = BUMP.topo
    rng = random.Random(SEMENTE)
    niveis = []
    for nv, fab in [(1, nivel1), (2, nivel2)]:
        cat = fab(rng)
        assert sum(len(v) for v in cat.values()) == 60, (nv, {k: len(v) for k, v in cat.items()})
        dias = GC.agenda(cat, rng)
        dias_at = [(fa(), fb()) for (ca, fa), (cb, fb) in dias]
        for a, b in dias_at:
            assert a["categoria"] != b["categoria"] and a["nivel"] == nv and b["nivel"] == nv
        niveis.append(dias_at)
    num, pags, pag_de, ordem = 3, {}, {}, []
    for nv, dias_at in enumerate(niveis, 1):
        pags[f"abertura{nv}"] = num; pags[f"plano{nv}"] = num + 1; num += 2
        for d, (a, b) in enumerate(dias_at, 1):
            for x in (a, b):
                pag_de[id(x)] = num; ordem.append((num, x, d)); num += 1
    pags["gabarito"] = num
    capa = BUMP.capa("Mais 120 atividades novas, nos mesmos 2 níveis, com outro plano de 30 dias.",
                     ("Nível 1 · 4 a 6 anos  |  Nível 2 · 7 a 10 anos", "Gabarito no final"),
                     ["pipa", "pato", "sorvete", "gato", "bola", "castelo" if False else "casa", "dado", "barco"])
    html = [capa, como_usar(pags)]
    for nv, dias_at in enumerate(niveis, 1):
        html.append(GC.abertura(nv, pags[f"abertura{nv}"]))
        html.append(GC.plano(nv, dias_at, pags[f"plano{nv}"], pag_de))
        for n_, x, d in [o for o in ordem if o[1]["nivel"] == nv]:
            html.append(GC.pag_atividade(x, n_, d))
    html += GC.gabarito([(n_, x) for n_, x, _ in ordem], pags["gabarito"])
    filas_v2 = [f for _, f in B.FILAS_MOSTRADAS]
    assert len(filas_v2) == 70 and len(set(filas_v2)) == 70, "fila repetida no Volume 2"
    assert not set(filas_v2) & filas_v1, "fila do Volume 2 repete o caderno"
    nuc_v1 = {B.nucleo(f) for f in filas_v1} - {None}
    nuc_v2 = [B.nucleo(f) for f in filas_v2 if B.nucleo(f) is not None]
    assert len(set(nuc_v2)) == len(nuc_v2) and not set(nuc_v2) & nuc_v1, "fila girada do Volume 2 parecida com outra"
    total = BUMP.montar(html)
    tipos = {}
    for _, x, _ in ordem:
        tipos.setdefault((x["nivel"], x["categoria"]), 0)
        tipos[(x["nivel"], x["categoria"])] += 1
    return dict(paginas=total, atividades=len(ordem), por_categoria=tipos)


if __name__ == "__main__":
    print(gerar())
