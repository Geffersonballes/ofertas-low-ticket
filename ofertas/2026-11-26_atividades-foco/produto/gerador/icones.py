"""Ícones vetoriais do Dez Minutinhos. Cada ícone é desenhado numa caixa 100x100 e
posicionado/escalado em mm. Traço preto, preenchimento claro: imprime bem em P&B."""
import math

TRACO = "#1d1d1f"
CLARO = "#ffffff"


def _estrela(pontas=5, R=46, r=20, cx=50, cy=52):
    pts = []
    for i in range(pontas * 2):
        ang = -math.pi / 2 + i * math.pi / pontas
        rad = R if i % 2 == 0 else r
        pts.append(f"{cx + rad * math.cos(ang):.1f},{cy + rad * math.sin(ang):.1f}")
    return f'<polygon points="{" ".join(pts)}"/>'


def _hexagono():
    pts = [f"{50 + 44 * math.cos(math.pi / 6 + i * math.pi / 3):.1f},{50 + 44 * math.sin(math.pi / 6 + i * math.pi / 3):.1f}" for i in range(6)]
    return f'<polygon points="{" ".join(pts)}"/>'


def _sol(raios=8):
    s = '<circle cx="50" cy="50" r="20"/>'
    for i in range(raios):
        a = i * 2 * math.pi / 8
        s += f'<line x1="{50 + 28 * math.cos(a):.1f}" y1="{50 + 28 * math.sin(a):.1f}" x2="{50 + 43 * math.cos(a):.1f}" y2="{50 + 43 * math.sin(a):.1f}"/>'
    return s


def _flor(petalas=5):
    s = ""
    for i in range(petalas):
        a = -math.pi / 2 + i * 2 * math.pi / petalas
        s += f'<circle cx="{50 + 22 * math.cos(a):.1f}" cy="{50 + 22 * math.sin(a):.1f}" r="15"/>'
    return s + '<circle cx="50" cy="50" r="11" fill="#d9d9d9"/>'


DESENHOS = {
    "circulo": lambda v: '<circle cx="50" cy="50" r="40"/>',
    "quadrado": lambda v: '<rect x="12" y="12" width="76" height="76" rx="8"/>',
    "triangulo": lambda v: '<polygon points="50,10 92,86 8,86"/>',
    "estrela": lambda v: _estrela(6 if v == "6pontas" else 5),
    "coracao": lambda v: '<path d="M50 88 C 18 66, 4 46, 14 28 C 24 10, 44 13, 50 30 C 56 13, 76 10, 86 28 C 96 46, 82 66, 50 88 Z"/>',
    "losango": lambda v: '<polygon points="50,6 90,50 50,94 10,50"/>',
    "hexagono": lambda v: _hexagono(),
    "sol": lambda v: _sol(),
    "lua": lambda v: '<path d="M62 8 A42 42 0 1 0 62 92 A32 32 0 1 1 62 8 Z"/>',
    "nuvem": lambda v: '<path d="M24 74 C 8 74, 6 52, 22 50 C 20 32, 44 26, 52 40 C 58 26, 82 28, 80 48 C 96 48, 96 74, 80 74 Z"/>',
    "peixe": lambda v: '<ellipse cx="44" cy="50" rx="32" ry="20"/><polygon points="74,50 94,32 94,68"/><circle cx="28" cy="45" r="4" fill="#1d1d1f"/>'
    + ('' if v == "semboca" else '<path d="M14 54 Q 18 57 22 54" fill="none"/>'),
    "casa": lambda v: '<polygon points="8,46 50,10 92,46"/><rect x="18" y="46" width="64" height="46"/>'
    + ('' if v == "semporta" else '<rect x="42" y="64" width="16" height="28"/>')
    + '<rect x="24" y="54" width="12" height="12"/>',
    "maca": lambda v: '<path d="M50 30 C 30 14, 6 30, 14 58 C 20 82, 38 92, 50 84 C 62 92, 80 82, 86 58 C 94 30, 70 14, 50 30 Z"/><path d="M50 30 L 54 10" fill="none"/>'
    + ('' if v == "semfolha" else '<path d="M54 18 C 64 6, 78 10, 80 14 C 72 22, 60 22, 54 18 Z" fill="#d9d9d9"/>'),
    "flor": lambda v: _flor(4 if v == "4petalas" else 5),
    "arvore": lambda v: '<rect x="42" y="58" width="16" height="36"/><circle cx="50" cy="40" r="32"/>',
    "passaro": lambda v: '<polygon points="22,52 4,40 8,64"/><ellipse cx="44" cy="56" rx="28" ry="20"/><circle cx="70" cy="40" r="15"/>'
    '<polygon points="83,36 97,41 83,46" fill="#d9d9d9"/><circle cx="73" cy="37" r="3" fill="#1d1d1f"/>'
    '<path d="M28 54 Q 44 40 58 54 Q 44 64 28 54 Z" fill="#d9d9d9"/><path d="M40 76 L 38 90 M 52 76 L 54 90" fill="none"/>',
    "barco": lambda v: '<polygon points="10,62 90,62 76,84 24,84"/><line x1="50" y1="62" x2="50" y2="10"/><polygon points="50,14 82,56 50,56" fill="#d9d9d9"/>',
    "banana": lambda v: '<path d="M14 30 C 18 70, 60 92, 88 62 C 90 58, 86 54, 82 58 C 60 76, 30 62, 24 28 C 22 22, 14 24, 14 30 Z"/>',
    "uva": lambda v: "".join(f'<circle cx="{x}" cy="{y}" r="11"/>' for x, y in [(38, 34), (62, 34), (26, 54), (50, 54), (74, 54), (38, 74), (62, 74), (50, 92)]) + '<path d="M50 24 L 52 6" fill="none"/>',
    "balao": lambda v: '<ellipse cx="50" cy="40" rx="28" ry="34"/><path d="M50 74 L 46 80 L 54 80 Z"/><path d="M50 80 C 40 88, 60 92, 50 99" fill="none"/>',
    "carro": lambda v: '<path d="M8 66 L 8 50 L 26 48 L 38 30 L 70 30 L 82 48 L 92 52 L 92 66 Z"/><circle cx="28" cy="70" r="10"/><circle cx="72" cy="70" r="10"/>',
}


def icone(nome, x, y, tam, variante=None, girar=0, espelhar=False, cor=CLARO, traco=3.4):
    """Ícone com o canto superior esquerdo em (x, y) e lado `tam` (mm)."""
    s = tam / 100
    t = f"translate({x:.2f},{y:.2f}) scale({s:.4f})"
    if girar or espelhar:
        t += f" translate(50,50) rotate({girar}) scale({-1 if espelhar else 1},1) translate(-50,-50)"
    return (f'<g transform="{t}" fill="{cor}" stroke="{TRACO}" stroke-width="{traco}" '
            f'stroke-linejoin="round" stroke-linecap="round">{DESENHOS[nome](variante)}</g>')
