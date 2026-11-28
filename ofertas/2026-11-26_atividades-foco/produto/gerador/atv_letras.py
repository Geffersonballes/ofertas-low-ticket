"""Atividades do bump "Letras e palavras" (área 182x228 mm). Palavras, sílabas e rimas conferidas com assert."""
import unicodedata

from atividades import W, H, _txt
from bumps_base import at, circ, LAR
from icones import icone, TRACO

CAT = "Letras"
PALAVRAS = {
    "sol": ("SOL", ["SOL"]), "lua": ("LUA", ["LU", "A"]), "nuvem": ("NUVEM", ["NU", "VEM"]), "peixe": ("PEIXE", ["PEI", "XE"]),
    "casa": ("CASA", ["CA", "SA"]), "maca": ("MAÇÃ", ["MA", "ÇÃ"]), "flor": ("FLOR", ["FLOR"]),
    "arvore": ("ÁRVORE", ["ÁR", "VO", "RE"]), "passaro": ("PÁSSARO", ["PÁS", "SA", "RO"]), "barco": ("BARCO", ["BAR", "CO"]),
    "banana": ("BANANA", ["BA", "NA", "NA"]), "uva": ("UVA", ["U", "VA"]), "balao": ("BALÃO", ["BA", "LÃO"]),
    "carro": ("CARRO", ["CAR", "RO"]), "estrela": ("ESTRELA", ["ES", "TRE", "LA"]), "coracao": ("CORAÇÃO", ["CO", "RA", "ÇÃO"]),
    "ovo": ("OVO", ["O", "VO"]), "ilha": ("ILHA", ["I", "LHA"]), "gato": ("GATO", ["GA", "TO"]), "bola": ("BOLA", ["BO", "LA"]),
    "dado": ("DADO", ["DA", "DO"]), "pipa": ("PIPA", ["PI", "PA"]), "sorvete": ("SORVETE", ["SOR", "VE", "TE"]),
    "pato": ("PATO", ["PA", "TO"]), "chave": ("CHAVE", ["CHA", "VE"]), "anel": ("ANEL", ["A", "NEL"]),
    "tesoura": ("TESOURA", ["TE", "SOU", "RA"]), "lapis": ("LÁPIS", ["LÁ", "PIS"]), "copo": ("COPO", ["CO", "PO"]),
}
for _k, (_p, _s) in PALAVRAS.items():
    assert "".join(_s) == _p, _k


def sem_acento(t):
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")


def inicial(k):
    return sem_acento(PALAVRAS[k][0])[0]


def tracejada(x, y, letra, tam, cor="#9a9a9a", esp=.55):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="Nunito" font-size="{tam}" font-weight="800" text-anchor="middle" '
            f'fill="none" stroke="{cor}" stroke-width="{esp}" stroke-dasharray="1.6 1.1" dominant-baseline="central">{letra}</text>')


def caixa(x, y, w=16, h=14):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" rx="3" fill="#fff" stroke="{TRACO}" stroke-width=".8"/>'


def resp(x, y, v, tam=7):
    return _txt(x, y, str(v), tam, 800, cor=LAR, fonte="Baloo 2")


# ======================================================================= NÍVEL 1
EXEMPLOS = {"A": ["anel", "arvore"], "E": ["estrela"], "I": ["ilha"], "O": ["ovo"], "U": ["uva"]}


def trace_letra(letra):
    s = []
    s.append(tracejada(46, 46, letra, 80, "#b5b5b5", .9))
    s.append(f'<circle cx="30" cy="12" r="3" fill="{LAR}"/>')
    ex = EXEMPLOS[letra]
    for i, k in enumerate(ex):
        x = 100 + i * 42
        s.append(icone(k, x, 14, 34))
        s.append(_txt(x + 17, 56, PALAVRAS[k][0], 6.5, 800, fonte="Baloo 2"))
    for l in range(4):
        y = 98 + l * 33
        s.append(f'<line x1="2" y1="{y + 11}" x2="{W - 2}" y2="{y + 11}" stroke="#ddd" stroke-width=".4"/>')
        for c in range(7):
            x = 14 + c * 25
            if c == 0:
                s.append(_txt(x, y, letra, 22, 800, fonte="Nunito"))
            else:
                s.append(tracejada(x, y, letra, 22))
    base = "".join(s)
    return at(f"Letra {letra}", f"Passe o dedo por cima da letra grande. Depois cubra as letras pontilhadas com o lápis.", 1, CAT, base,
              gab_txt="Atividade livre: vale qualquer traço que siga o pontilhado.")


def trace_vogais():
    s = []
    for l, v in enumerate("AEIOU"):
        y = 14 + l * 44
        s.append(f'<line x1="2" y1="{y + 11}" x2="{W - 2}" y2="{y + 11}" stroke="#ddd" stroke-width=".4"/>')
        k = EXEMPLOS[v][0]
        s.append(icone(k, 2, y - 12, 24))
        for c in range(6):
            x = 44 + c * 23
            s.append(_txt(x, y, v, 22, 800) if c == 0 else tracejada(x, y, v, 22))
    base = "".join(s)
    return at("As cinco vogais", "A, E, I, O, U. Diga o nome de cada figura e cubra as vogais pontilhadas.", 1, CAT, base,
              gab_txt="Atividade livre: vale qualquer traço que siga o pontilhado.")


def letra_inicial(rng, chaves):
    s, g = [], []
    letras = sorted({inicial(k) for k in PALAVRAS})
    for i, k in enumerate(chaves):
        x, y = (i % 2) * 92, (i // 2) * 74
        s.append(f'<rect x="{x + 2}" y="{y + 2}" width="86" height="68" rx="5" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(icone(k, x + 27, y + 6, 34))
        certa = inicial(k)
        opc = [certa] + rng.sample([l for l in letras if l != certa], 2)
        rng.shuffle(opc)
        for j, l in enumerate(opc):
            cx = x + 20 + j * 25
            s.append(_txt(cx, y + 56, l, 14, 800, fonte="Baloo 2"))
            if l == certa:
                g.append(circ(cx, y + 56, 8))
    base = "".join(s)
    return at("Com que letra começa?", "Diga o nome da figura em voz alta e circule a letra com que ela começa.", 1, CAT, base, base + "".join(g))


def ligue_letra(rng, chaves):
    assert len({inicial(k) for k in chaves}) == len(chaves)
    direita = [inicial(k) for k in chaves]
    rng.shuffle(direita)
    s, g = [], []
    for i, k in enumerate(chaves):
        y = 6 + i * 44
        s.append(icone(k, 8, y, 34))
        s.append(f'<circle cx="58" cy="{y + 17}" r="1.8" fill="{TRACO}"/>')
        j = direita.index(inicial(k))
        g.append(f'<line x1="58" y1="{y + 17}" x2="132" y2="{6 + j * 44 + 17}" stroke="{LAR}" stroke-width="1.4"/>')
    for j, l in enumerate(direita):
        y = 6 + j * 44
        s.append(f'<circle cx="132" cy="{y + 17}" r="1.8" fill="{TRACO}"/>')
        s.append(_txt(156, y + 17, l, 22, 800, fonte="Baloo 2"))
    base = "".join(s)
    return at("Ligue à primeira letra", "Diga o nome de cada figura e ligue à letra com que ela começa.", 1, CAT, base, base + "".join(g))


PARECIDAS = {"A": "VHN", "B": "DPR", "E": "FBL", "O": "QCD", "M": "NWV", "P": "BRF", "S": "ZCG", "U": "VNJ", "C": "OGQ", "L": "TIJ"}


def encontre_letra(rng, alvo):
    cols, lins = 8, 7
    n_alvo = rng.randint(8, 12)
    pos = set(rng.sample(range(cols * lins), n_alvo))
    outras = PARECIDAS[alvo] + "ARTOSMLIEN".replace(alvo, "")
    grade = [alvo if i in pos else rng.choice(outras) for i in range(cols * lins)]
    assert grade.count(alvo) == n_alvo
    s, g = [], []
    s.append(_txt(20, 8, "Procure:", 6, 800, anchor="start"))
    s.append(f'<rect x="48" y="0" width="16" height="16" rx="3" fill="#fff1e8" stroke="{TRACO}" stroke-width=".8"/>')
    s.append(_txt(56, 8.3, alvo, 11, 800, fonte="Baloo 2"))
    for i, l in enumerate(grade):
        cx, cy = 16 + (i % cols) * 21.4, 30 + (i // cols) * 23
        s.append(_txt(cx, cy, l, 13, 800, fonte="Baloo 2"))
        if l == alvo:
            g.append(circ(cx, cy, 7.5))
    s.append(_txt(60, 200, f"Quantas letras {alvo} você achou?", 6, 800))
    s.append(caixa(118, 193, 20, 14))
    g.append(resp(128, 200, n_alvo, 9))
    base = "".join(s)
    return at(f"Ache a letra {alvo}", f"Circule todas as letras {alvo} que encontrar. Depois conte quantas são.", 1, CAT, base, base + "".join(g))


def complete_vogal(rng, chaves):
    s, g = [], []
    for i, k in enumerate(chaves):
        palavra = PALAVRAS[k][0]
        idx = [j for j, c in enumerate(palavra) if c in "AEIOU"]
        assert idx, k
        j = rng.choice(idx)
        x, y = (i % 2) * 92, (i // 2) * 74
        s.append(f'<rect x="{x + 2}" y="{y + 2}" width="86" height="68" rx="5" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(icone(k, x + 29, y + 6, 30))
        larg = len(palavra) * 11
        x0 = x + 45 - larg / 2 + 5.5
        for q, ch in enumerate(palavra):
            cx = x0 + q * 11
            if q == j:
                s.append(f'<rect x="{cx - 5}" y="{y + 44}" width="10" height="14" rx="2" fill="#fff" stroke="{TRACO}" stroke-width=".7"/>')
                g.append(resp(cx, y + 51, ch, 9))
            else:
                s.append(_txt(cx, y + 51, ch, 10, 800, fonte="Baloo 2"))
    s.append(_txt(W / 2, 224, "Vogais: A  E  I  O  U", 6, 800, cor="#666"))
    base = "".join(s)
    return at("Qual vogal falta?", "O adulto lê a palavra em voz alta. A criança escreve na caixinha a vogal que está faltando.", 1, CAT, base, base + "".join(g))


def letras_iguais(rng, modelos):
    s, g = [], []
    for i, m in enumerate(modelos):
        y = 6 + i * 36
        s.append(f'<rect x="2" y="{y}" width="24" height="26" rx="4" fill="#fff1e8" stroke="{TRACO}" stroke-width=".8"/>')
        s.append(_txt(14, y + 13, m, 15, 800, fonte="Baloo 2"))
        n_igual = rng.randint(2, 3)
        linha = [m] * n_igual + [rng.choice(PARECIDAS.get(m, "ABCDEFG").replace(m, "") or "X") for _ in range(7 - n_igual)]
        rng.shuffle(linha)
        for j, l in enumerate(linha):
            cx = 40 + j * 20.5
            s.append(_txt(cx, y + 13, l, 15, 800, fonte="Baloo 2"))
            if l == m:
                g.append(circ(cx, y + 13, 8))
        s.append(f'<line x1="2" y1="{y + 31}" x2="{W - 2}" y2="{y + 31}" stroke="#ddd" stroke-width=".4"/>')
    base = "".join(s)
    return at("Letras iguais", "Olhe a letra do quadradinho e circule, na mesma linha, as letras iguais a ela.", 1, CAT, base, base + "".join(g))


# ======================================================================= NÍVEL 2
def complete_silaba(rng, chaves):
    s, g = [], []
    faltando = []
    for i, k in enumerate(chaves):
        palavra, sil = PALAVRAS[k]
        assert len(sil) >= 2, k
        j = rng.randrange(len(sil))
        faltando.append(sil[j])
        x, y = (i % 2) * 92, 30 + (i // 2) * 66
        s.append(f'<rect x="{x + 2}" y="{y}" width="86" height="60" rx="5" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(icone(k, x + 31, y + 4, 26))
        larg = sum(max(13, len(t) * 6.5) for t in sil) + 3 * (len(sil) - 1)
        cx = x + 45 - larg / 2
        for q, t in enumerate(sil):
            w = max(13, len(t) * 6.5)
            if q == j:
                s.append(f'<rect x="{cx}" y="{y + 36}" width="{w}" height="15" rx="2" fill="#fff" stroke="{TRACO}" stroke-width=".7"/>')
                g.append(resp(cx + w / 2, y + 43.5, t, 7))
            else:
                s.append(_txt(cx + w / 2, y + 43.5, t, 8, 800, fonte="Baloo 2"))
            cx += w + 3
    banco = sorted(set(faltando + rng.sample(["MA", "TE", "LO", "RU", "BE", "FI", "NO", "PE"], 2)))
    s.append(_txt(4, 8, "Sílabas:", 6, 800, anchor="start"))
    for q, t in enumerate(banco):
        s.append(f'<rect x="{36 + q * 18}" y="1" width="16" height="13" rx="3" fill="#fff1e8" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(_txt(44 + q * 18, 7.8, t, 5.8, 800, fonte="Baloo 2"))
    assert 36 + len(banco) * 18 <= W, banco
    base = "".join(s)
    return at("Complete com a sílaba", "Escolha nas sílabas de cima a que completa cada palavra e escreva no espaço vazio.", 2, CAT, base, base + "".join(g))


def conte_silabas(chaves):
    s, g = [], []
    for i, k in enumerate(chaves):
        palavra, sil = PALAVRAS[k]
        x, y = (i % 2) * 92, (i // 2) * 56
        s.append(f'<rect x="{x + 2}" y="{y + 2}" width="86" height="50" rx="5" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(icone(k, x + 6, y + 8, 26))
        s.append(_txt(x + 60, y + 16, palavra, 7.6 if len(palavra) > 5 else 8.5, 800, fonte="Baloo 2"))
        for q in range(4):
            s.append(f'<circle cx="{x + 40 + q * 9}" cy="{y + 34}" r="3.2" fill="#fff" stroke="{TRACO}" stroke-width=".5"/>')
            if q < len(sil):
                g.append(f'<circle cx="{x + 40 + q * 9}" cy="{y + 34}" r="3.2" fill="{LAR}"/>')
        s.append(caixa(x + 74, y + 28, 12, 12))
        g.append(resp(x + 80, y + 34, len(sil), 7))
    base = "".join(s)
    return at("Quantas sílabas?", "Fale a palavra batendo palmas em cada pedacinho. Pinte uma bolinha por palma e escreva o número.", 2, CAT, base, base + "".join(g))


# embaralhados que formam outra palavra (a criança acha que já está certo): sorteia de novo
EMBARALHADAS_PROIBIDAS = {"TOGA", "SACA", "ACAS", "VAU", "VOO", "AMOR", "ROMA", "MORA", "OMAR", "RAMO", "LOBA", "ALBO",
                          "PAPI", "DOAD", "SOLA", "ALAS", "LAMA", "MALA", "SALA", "OPCO", "POCO", "COPO", "TAPO",
                          "TOPA", "POTA", "PATO", "OVO", "SOL", "LUA", "MESA", "MEAS", "SEMA", "AMES", "VALE",
                          "LEVA", "VELA", "AVEL", "ALVE", "FACA", "CAFA", "BOLA", "LOBA", "ABLO", "DADO", "GATO",
                          "CASA", "PIPA", "ILHA", "ANEL", "LENA", "ELAN", "PEIXE", "TREM", "PAO", "PÃO"}


def forme_palavra(rng, chaves, evitar=()):
    s, g = [], []
    for i, k in enumerate(chaves):
        palavra = PALAVRAS[k][0]
        letras = list(palavra)
        for _ in range(200):
            rng.shuffle(letras)
            if "".join(letras) != palavra and "".join(letras) not in evitar:
                break
        assert "".join(letras) != palavra and "".join(letras) not in evitar and sorted(letras) == sorted(palavra)
        x, y = (i % 2) * 92, (i // 2) * 74
        s.append(f'<rect x="{x + 2}" y="{y + 2}" width="86" height="68" rx="5" fill="none" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(icone(k, x + 6, y + 8, 28))
        for q, ch in enumerate(letras):
            s.append(f'<rect x="{x + 37 + q * 6.6}" y="{y + 12}" width="6" height="9" rx="1.5" fill="#fff1e8" stroke="{TRACO}" stroke-width=".4"/>')
            s.append(_txt(x + 40 + q * 6.6, y + 16.7, ch, 5.2, 800))
        for q in range(len(palavra)):
            s.append(f'<line x1="{x + 10 + q * 10}" y1="{y + 58}" x2="{x + 17 + q * 10}" y2="{y + 58}" stroke="{TRACO}" stroke-width=".7"/>')
            g.append(_txt(x + 13.5 + q * 10, y + 53, palavra[q], 6.5, 800, cor=LAR, fonte="Baloo 2"))
    base = "".join(s)
    return at("Desembaralhe", "As letras estão misturadas. Olhe a figura e escreva a palavra certa, uma letra em cada risquinho.", 2, CAT, base, base + "".join(g))


# Cada par tem uma rima diferente dos outros 19 (famílias abaixo): numa folha, cada palavra só rima com o seu par.
# Antes havia BALÃO/AVIÃO + FOGÃO/MAMÃO (+ PÃO/MÃO), GATO/PATO + SAPATO/RATO e JANELA/PANELA + VELA/TELA.
RIMAS = [("GATO", "PATO"), ("BOLA", "COLA"), ("CASA", "ASA"), ("DADO", "LADO"), ("JANELA", "PANELA"), ("LUA", "RUA"),
         ("UVA", "LUVA"), ("CAMA", "LAMA"), ("BALÃO", "AVIÃO"), ("MEIA", "AREIA"), ("CHAVE", "NAVE"), ("FLOR", "CALOR"),
         ("PIPOCA", "MINHOCA"), ("CANECA", "BONECA"), ("SAPO", "PAPO"), ("DEDO", "MEDO"), ("NARIZ", "GIZ"), ("MEL", "PAPEL"),
         ("COPO", "TOPO"), ("MALA", "SALA")]
FAMILIAS_RIMA = ["ATO", "OLA", "ASA", "ADO", "ELA", "UA", "UVA", "AMA", "ÃO", "EIA", "AVE", "OR",
                 "OCA", "ECA", "APO", "EDO", "IZ", "EL", "OPO", "ALA"]
assert len(set(FAMILIAS_RIMA)) == len(RIMAS)
for (_a, _b), _f in zip(RIMAS, FAMILIAS_RIMA):
    assert _a[-2:] == _b[-2:] and _a != _b, (_a, _b)
    assert _a.endswith(_f) and _b.endswith(_f), (_a, _b, _f)
    # nenhuma palavra do par termina com a família de outro par
    assert not any(o != _f and len(o) >= 3 and (_a.endswith(o) or _b.endswith(o)) for o in FAMILIAS_RIMA), (_a, _b)


def rimas(rng, pares):
    esq = [a for a, _ in pares]
    dir_ = [b for _, b in pares]
    rng.shuffle(dir_)
    s, g = [], []
    for i, a in enumerate(esq):
        y = 10 + i * 42
        s.append(f'<rect x="4" y="{y}" width="58" height="22" rx="5" fill="#fff" stroke="{TRACO}" stroke-width=".7"/>')
        s.append(_txt(33, y + 11, a, 8, 800, fonte="Baloo 2"))
        s.append(f'<circle cx="66" cy="{y + 11}" r="1.8" fill="{TRACO}"/>')
    for j, b in enumerate(dir_):
        y = 10 + j * 42
        s.append(f'<rect x="120" y="{y}" width="58" height="22" rx="5" fill="#fff" stroke="{TRACO}" stroke-width=".7"/>')
        s.append(_txt(149, y + 11, b, 8, 800, fonte="Baloo 2"))
        s.append(f'<circle cx="116" cy="{y + 11}" r="1.8" fill="{TRACO}"/>')
    for i, (a, b) in enumerate(pares):
        j = dir_.index(b)
        g.append(f'<line x1="66" y1="{10 + i * 42 + 11}" x2="116" y2="{10 + j * 42 + 11}" stroke="{LAR}" stroke-width="1.4"/>')
    base = "".join(s)
    return at("Palavras que rimam", "Leia em voz alta e ligue cada palavra à que rima com ela (o final soa igual).", 2, CAT, base, base + "".join(g))


FRASES = [("O ___ vive na água e tem escamas.", "peixe"), ("A ___ brilha no céu à noite.", "lua"), ("Eu chutei a ___ no gol.", "bola"),
          ("A ___ voa alto com o vento.", "pipa"), ("O ___ mia em cima do muro.", "gato"), ("Comi uma ___ vermelha no lanche.", "maca"),
          ("O ___ navega no mar.", "barco"), ("Abri a porta com a ___.", "chave"), ("O ___ é quente e amarelo.", "sol"),
          ("O ___ faz quá-quá no lago.", "pato"), ("Bebi água no ___.", "copo"), ("Recortei o papel com a ___.", "tesoura"),
          ("Escrevi meu nome com o ___.", "lapis"), ("A ___ tem pétalas coloridas.", "flor"), ("O ___ derreteu no calor.", "sorvete"),
          ("A galinha botou um ___.", "ovo"), ("O ___ tem quatro rodas.", "carro"), ("A ___ cinza trouxe chuva.", "nuvem"),
          ("O ___ canta no galho da árvore.", "passaro"), ("Joguei o ___ e tirei seis.", "dado")]


def complete_frase(rng, frases):
    s, g = [], []
    banco = [k for _, k in frases]
    extra = rng.choice([k for k in PALAVRAS if k not in banco and k in {"uva", "casa", "anel", "ilha", "banana", "estrela"}])
    banco = banco + [extra]
    rng.shuffle(banco)
    s.append(_txt(4, 6, "Palavras:", 6, 800, anchor="start"))
    for q, k in enumerate(banco):
        x = 4 + q * 35.5
        s.append(f'<rect x="{x}" y="12" width="33" height="34" rx="4" fill="#fff1e8" stroke="{TRACO}" stroke-width=".6"/>')
        s.append(icone(k, x + 8.5, 13, 16))
        s.append(_txt(x + 16.5, 39, PALAVRAS[k][0], 4.8, 800))
    lb, lg = [], []
    for i, (f, k) in enumerate(frases):
        y = 66 + i * 40
        p0, p1 = f.split("___")
        txt = (f'<text x="4" y="{y}" font-family="Nunito" font-size="6.4" font-weight="800" fill="{TRACO}" dominant-baseline="central">'
               f'{i + 1}. {p0}{{meio}}{p1}</text>')
        lb.append(txt.replace("{meio}", "____________"))
        lg.append(txt.replace("{meio}", f'<tspan fill="{LAR}" text-decoration="underline">{PALAVRAS[k][0]}</tspan>'))
    comum = "".join(s)
    return at("Complete a frase", "Leia cada frase e escreva no risquinho a palavra que completa, escolhendo entre as de cima.", 2, CAT,
              comum + "".join(lb), comum + "".join(lg))


def ordem_alfabetica(rng, chaves):
    ordem = sorted(chaves, key=lambda k: sem_acento(PALAVRAS[k][0]))
    s, g = [], []
    s.append(_txt(W / 2, 6, "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z", 6, 800, cor="#777"))
    for i, k in enumerate(chaves):
        y = 18 + i * 41
        s.append(f'<rect x="2" y="{y}" width="{W - 4}" height="35" rx="5" fill="none" stroke="#bbb" stroke-width=".5"/>')
        s.append(icone(k, 8, y + 4, 27))
        s.append(_txt(44, y + 17.5, PALAVRAS[k][0], 9, 800, anchor="start", fonte="Baloo 2"))
        s.append(caixa(150, y + 9, 20, 17))
        g.append(resp(160, y + 17.5, ordem.index(k) + 1, 9))
    base = "".join(s)
    return at("Ordem alfabética", "Numere as palavras de 1 a 5 na ordem do alfabeto. Use o alfabeto de cima para ajudar.", 2, CAT, base, base + "".join(g))
