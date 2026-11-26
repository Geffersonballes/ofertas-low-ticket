"""Base comum dos order bumps do Dez Minutinhos: ícones extras, capa, topo, rodapé com o nome do bump,
páginas de atividade e de gabarito, montagem do HTML. Cada bump usa a mesma identidade do caderno."""
import math
import pathlib

import gerar_amostra as GA
import gerar_completo as GC
import icones
from icones import icone, TRACO
from atividades import W, H, _txt

AQUI = pathlib.Path(__file__).parent
SAIDA = AQUI / "saida"
LAR = "#ff7a45"

# ------------------------------------------------------------------ ícones extras (caixa 100x100)
EXTRAS = {
    "ovo": lambda v: '<ellipse cx="50" cy="54" rx="30" ry="38"/>',
    "ilha": lambda v: '<path d="M8 82 Q 50 58 92 82 Z"/><path d="M52 70 Q 50 44 58 22" fill="none"/>'
                      '<path d="M58 22 Q 40 14 26 26 Q 42 22 56 26 Z" fill="#d9d9d9"/><path d="M58 22 Q 76 12 90 26 Q 74 22 60 26 Z" fill="#d9d9d9"/>'
                      '<path d="M58 22 Q 64 36 60 48" fill="none"/><path d="M4 90 q 8 -4 16 0 t 16 0 t 16 0 t 16 0 t 16 0 t 16 0" fill="none"/>',
    "gato": lambda v: '<polygon points="22,40 28,10 44,30"/><polygon points="78,40 72,10 56,30"/><circle cx="50" cy="52" r="32"/>'
                      '<circle cx="38" cy="46" r="4" fill="#1d1d1f"/><circle cx="62" cy="46" r="4" fill="#1d1d1f"/>'
                      '<polygon points="46,58 54,58 50,63" fill="#1d1d1f"/><path d="M50 63 Q 44 70 38 66 M50 63 Q 56 70 62 66" fill="none"/>'
                      '<path d="M30 60 L 8 56 M30 64 L 8 68 M70 60 L 92 56 M70 64 L 92 68" fill="none"/>',
    "bola": lambda v: '<circle cx="50" cy="50" r="40"/><path d="M14 36 Q 50 56 86 36 M14 64 Q 50 44 86 64" fill="none"/>'
                      '<path d="M50 10 Q 36 50 50 90" fill="none"/>',
    "dado": lambda v: '<rect x="12" y="12" width="76" height="76" rx="12"/>' + "".join(
        f'<circle cx="{x}" cy="{y}" r="6" fill="#1d1d1f"/>' for x, y in [(32, 32), (68, 32), (50, 50), (32, 68), (68, 68)]),
    "pipa": lambda v: '<polygon points="50,6 82,40 50,74 18,40"/><path d="M50 6 L 50 74 M18 40 L 82 40" fill="none"/>'
                      '<path d="M50 74 Q 40 82 50 88 Q 60 94 50 99" fill="none"/>'
                      '<polygon points="44,82 50,79 48,86" fill="#d9d9d9"/><polygon points="52,91 58,88 56,95" fill="#d9d9d9"/>',
    "sorvete": lambda v: '<polygon points="30,48 70,48 50,96" fill="#d9d9d9"/><circle cx="50" cy="34" r="22"/>'
                         '<circle cx="34" cy="46" r="8"/><circle cx="50" cy="48" r="8"/><circle cx="66" cy="46" r="8"/>',
    "pato": lambda v: '<path d="M14 60 C 14 46, 34 44, 46 52 L 54 52 C 50 40, 54 22, 70 22 C 84 22, 88 36, 82 46 L 94 48 L 84 56 '
                      'C 90 74, 70 88, 46 86 C 26 84, 14 76, 14 60 Z"/><circle cx="74" cy="34" r="3" fill="#1d1d1f"/>'
                      '<path d="M30 64 Q 46 58 58 68" fill="none"/>',
    "chave": lambda v: '<circle cx="28" cy="50" r="18"/><circle cx="28" cy="50" r="7"/><path d="M46 50 L 92 50 L 92 62 M80 50 L 80 60 M68 50 L 68 58" fill="none"/>',
    "anel": lambda v: '<ellipse cx="50" cy="62" rx="30" ry="22"/><ellipse cx="50" cy="62" rx="20" ry="13"/><polygon points="40,40 60,40 66,30 50,20 34,30" fill="#d9d9d9"/>',
    "tesoura": lambda v: '<circle cx="24" cy="30" r="12"/><circle cx="24" cy="70" r="12"/><path d="M34 36 L 92 64 M34 64 L 92 36" fill="none"/>',
    "lapis": lambda v: '<polygon points="10,50 26,40 26,60" fill="#d9d9d9"/><rect x="26" y="40" width="54" height="20"/><rect x="80" y="40" width="12" height="20" fill="#d9d9d9"/>',
    "copo": lambda v: '<polygon points="26,18 74,18 66,90 34,90"/><path d="M28 34 L 72 34" fill="none"/>',
}
for _k, _f in EXTRAS.items():
    icones.DESENHOS.setdefault(_k, _f)

# ------------------------------------------------------------------ CSS
CSS_BUMP = """
.capa .titulo { font-size: 50pt; }
.autor { font-family: 'Nunito'; font-weight: 700; font-size: 11pt; color: var(--cinza); margin-top: 2mm; }
.capa .bump { font-family: 'Baloo 2'; font-weight: 800; font-size: 13pt; color: var(--laranja); letter-spacing: .6pt; margin-top: 2mm; }
.corte-v { border-left: .35mm dashed #999; position: absolute; top: 8mm; bottom: 8mm; left: 50%; }
.aviso-adulto { display: inline-flex; gap: 2mm; align-items: center; font-weight: 800; font-size: 9.5pt; background: #fff1e8;
  border: .3mm solid var(--laranja); border-radius: 10mm; padding: .6mm 3mm; margin-top: 1mm; }
.cartas { display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: repeat(3, 1fr); flex: 1; margin-top: 4mm; border: .35mm dashed #999; }
.carta { border: .35mm dashed #999; padding: 6mm 7mm; display: flex; flex-direction: column; position: relative; }
.carta .cat { font-family: 'Baloo 2'; font-weight: 800; font-size: 10pt; letter-spacing: .6pt; color: var(--laranja); }
.carta .q { font-family: 'Baloo 2'; font-weight: 700; font-size: 21pt; line-height: 1.12; flex: 1; display: flex; align-items: center; position: relative; z-index: 1; padding-bottom: 6mm; }
.carta .fundo { position: absolute; right: 2mm; bottom: 5mm; width: 24mm; height: 24mm; opacity: .09; top: auto; }
.carta .num { position: absolute; right: 5mm; bottom: 3mm; font-size: 8pt; color: var(--cinza); }
.carta svg { position: absolute; right: 5mm; top: 4mm; width: 12mm; height: 12mm; }
.regras { font-size: 12pt; line-height: 1.5; }
.regras h2 { font-family: 'Baloo 2'; font-weight: 800; font-size: 15pt; margin: 4mm 0 1mm; }
.regras ol, .regras ul { padding-left: 6mm; }
"""


def css_base():
    return (AQUI / "fontes" / "fontes.css").read_text() + GA.CSS + GC.CSS_EXTRA + CSS_BUMP


# ------------------------------------------------------------------ peças de página
class Bump:
    def __init__(self, nome, slug, tag):
        self.nome, self.slug, self.tag = nome, slug, tag

    def topo(self, *selos):
        return f'<div class="topo"><div class="marca">Dez <b>Minutinhos</b></div><div class="selos">{"".join(selos)}</div></div>'

    def rodape(self, num, dia=None):
        dir_ = f'<span class="feito">Feito!<span class="caixa"></span></span>' if dia else "<span></span>"
        return f'<div class="rodape"><span>Dez Minutinhos · {self.nome} · página {num}</span>{dir_}</div>'

    def capa(self, subtitulo, linhas_base, icones_capa):
        fig = ""
        for i, n in enumerate(icones_capa[:8]):
            cx, cy = 24 + (i % 4) * 45, 22 + (i // 4) * 44 + (12 if i % 2 else 0)
            fig += f'<circle cx="{cx}" cy="{cy}" r="19" fill="#ffe1cf"/>' + icone(n, cx - 15, cy - 15, 30)
        return f"""<section class="pagina capa"><div class="faixa"></div>
  <div class="miolo">
    <div class="marca" style="font-size:13pt">Dez <b>Minutinhos</b></div>
    <div class="bump">{"CONTINUAÇÃO" if self.slug == "volume-2" else "COMPLEMENTO"} DO DEZ MINUTINHOS</div>
    <div class="titulo">{self.nome}</div>
    <p class="autor">por Gefferson Balles</p>
    <p class="sub">{subtitulo}</p>
    <div><span class="tag">{self.tag}</span></div>
    <div class="figuras">{GA.svg(fig, 182, 112)}</div>
  </div>
  <div class="base"><span>{linhas_base[0]}</span><span>{linhas_base[1]}</span></div>
</section>"""

    def pagina_texto(self, titulo, corpo_html, num, selo="Para o adulto"):
        return f"""<section class="pagina">{self.topo(f'<span class="selo">{selo}</span>')}<h1>{titulo}</h1>
  <div class="texto regras">{corpo_html}</div>{self.rodape(num)}</section>"""

    def pagina_atividade(self, at, num, extra=""):
        selos = [f'<span class="selo">{at["categoria"]}</span>']
        if at.get("nivel"):
            selos.append(GA.selo(at["nivel"]))
        return f"""<section class="pagina">{self.topo(*selos)}
  <h1>{at['titulo']}</h1><p class="instrucao">{at['instrucao']}</p>{extra}
  <div class="area">{GA.svg(at['svg'])}</div>{self.rodape(num, True)}</section>"""

    def gabarito(self, lista, num_ini, por_pag=9):
        cards = []
        for num, at in lista:
            if not at.get("gabarito_svg") and not at.get("gabarito_txt"):
                continue
            corpo = GA.svg(at["gabarito_svg"]) if at.get("gabarito_svg") else f"<p>{at['gabarito_txt']}</p>"
            nv = f'N{at["nivel"]} · ' if at.get("nivel") else ""
            cards.append(f'<div class="card"><h3>Pág. {num} · {nv}{at["titulo"]}</h3>{corpo}</div>')
        pags = []
        for i in range(0, len(cards), por_pag):
            pags.append(f"""<section class="pagina">{self.topo('<span class="selo">Gabarito</span>')}
  <div class="gab9">{''.join(cards[i:i + por_pag])}</div>{self.rodape(num_ini + len(pags))}</section>""")
        return pags

    def montar(self, paginas, css_extra=""):
        html = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Dez Minutinhos — {self.nome}</title><style>{css_base()}{css_extra}</style></head>
<body>{''.join(paginas)}</body></html>"""
        low = html.lower()
        for proibida in ("tdah", "cérebro", "cerebro", "neuro", "potencial", "cognitiv", "amostra"):
            assert proibida not in low, f"{self.slug}: palavra proibida '{proibida}'"
        SAIDA.mkdir(exist_ok=True)
        (SAIDA / f"bump-{self.slug}.html").write_text(html, encoding="utf-8")
        return len(paginas)


def at(titulo, instrucao, nivel, categoria, svg, gab=None, gab_txt=None):
    d = dict(titulo=titulo, instrucao=instrucao, nivel=nivel, categoria=categoria, svg=svg)
    if gab is not None:
        d["gabarito_svg"] = gab
    elif gab_txt is not None:
        d["gabarito_txt"] = gab_txt
    return d


def circ(cx, cy, r, esp=1.6):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" stroke="{LAR}" stroke-width="{esp}"/>'


def caixa_corte(x, y, w, h, rx=2):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="#fff" stroke="#888" stroke-width=".5" stroke-dasharray="2 1.4"/>'


def faixa_recorte(y, texto="RECORTE AS PEÇAS"):
    return (f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#888" stroke-width=".5" stroke-dasharray="2.5 1.6"/>'
            + icone("tesoura", 2, y - 5, 10, traco=5) + _txt(15, y - 3.2, texto, 4.4, 800, anchor="start", cor="#777"))
