"""Mídias da página de vendas feitas SÓ com páginas do caderno VENDIDO: o PDF final (produto/final/dez-minutinhos.pdf)
rasterizado a 192 dpi (o mesmo tamanho das antigas vitrine-XX.png, que vinham do PDF de amostra e mostravam
páginas que não existem no caderno — corrigido em 2026-11-28).
Uso (depois de gerar o PDF final):
  python3 gerar_midia.py && node fotografar.cjs && python3 gerar_midia.py --finalizar
Saída: ../img/ (mockups PNG/WebP, vídeo MP4 + GIF do caderno sendo folheado, amostras JPG) e a imagem do produto
da Hotmart (../../hotmart/imagem-produto.png, que mostra a capa)."""
import json
import pathlib
import subprocess
import sys

from PIL import Image

AQUI = pathlib.Path(__file__).parent
PDF_FINAL = AQUI.parents[1] / "produto" / "final" / "dez-minutinhos.pdf"
PAGS = AQUI.parents[1] / "produto" / "gerador" / "saida" / "paginas-final"
CENAS = AQUI / "cenas"
IMG = AQUI.parent / "img"

# páginas do caderno final: 1 capa, 6 qual é diferente (N1), 7 labirinto (N1), 8 o que vem depois (N1),
# 39 ligue os pontos (N1), 68 jogo dos 7 erros (N2), 69 sudoku 6x6 (N2), 70 que número falta (N2),
# 73 caça-palavras (N2), 78 código secreto (N2), 104 labirinto desafio (N2)
FOLHEAR = [1, 7, 8, 39, 104, 69, 73, 68, 70]
LEQUE = [68, 69, 8, 7, 1]          # de baixo para cima
AMOSTRAS = {"amostra-nivel1": 8, "amostra-nivel2": 78, "dentro-1": 7, "dentro-2": 6, "dentro-3": 39,
            "dentro-4": 69, "dentro-5": 73, "dentro-6": 68}


def rasterizar():
    """Uma PNG por página do PDF final, 1587 px de largura (= A4 a 2x, como as vitrines antigas)."""
    PAGS.mkdir(parents=True, exist_ok=True)
    for n in sorted(set(FOLHEAR + LEQUE + list(AMOSTRAS.values()) + [1, 7, 78])):
        alvo = PAGS / f"pagina-{n:03d}.png"
        subprocess.run(["pdftoppm", "-r", "192", "-png", "-singlefile", "-f", str(n), "-l", str(n), str(PDF_FINAL),
                        str(alvo.with_suffix(""))], check=True)

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%dpx;height:%dpx;overflow:hidden;background:transparent}
.palco{position:relative;width:100%%;height:100%%;perspective:2200px}
.folha{position:absolute;width:420px;height:594px;background:#fff center/cover no-repeat;border-radius:4px;
  box-shadow:0 1px 2px rgba(0,0,0,.12),0 18px 40px rgba(60,30,10,.22)}
"""


def url(n):
    return (PAGS / f"pagina-{n:03d}.png").as_uri()


def lapis(x, y, ang, w=360):
    return f"""<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:rotate({ang}deg);filter:drop-shadow(0 10px 12px rgba(60,30,10,.25))"
 viewBox="0 0 360 30"><polygon points="0,15 34,3 34,27" fill="#f4d3a8"/><polygon points="0,15 12,11 12,19" fill="#333"/>
 <rect x="34" y="3" width="270" height="24" fill="#ff7a45"/><rect x="34" y="3" width="270" height="8" fill="#ff9468"/>
 <rect x="304" y="3" width="26" height="24" fill="#c9c9c9"/><rect x="330" y="3" width="30" height="24" rx="5" fill="#f29bb0"/></svg>"""


def cena(nome, w, h, corpo, fundo="transparent"):
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS % (w, h)}
body{{background:{fundo}}}</style></head><body><div class="palco">{corpo}</div></body></html>"""
    (CENAS / f"{nome}.html").write_text(html, encoding="utf-8")
    return {"nome": nome, "w": w, "h": h, "transparente": fundo == "transparent"}


def montar_cenas():
    rasterizar()
    CENAS.mkdir(exist_ok=True)
    lista = []
    # 1) capa em 3D com uma folha de atividade embaixo e um lápis
    corpo = (f'<div class="folha" style="left:330px;top:120px;transform:rotate(7deg);background-image:url({url(3)})"></div>'
             f'<div class="folha" style="left:220px;top:90px;transform:rotateY(-14deg) rotateX(4deg) rotate(-4deg);background-image:url({url(1)})"></div>'
             + lapis(500, 690, -18, 380))
    lista.append(cena("mockup-capa", 1000, 860, corpo))
    # 2) pacote em leque
    corpo = ""
    for i, n in enumerate(LEQUE):
        ang = (i - 2) * 9
        corpo += f'<div class="folha" style="left:{390 + (i - 2) * 95}px;top:{130 + abs(i - 2) * 22}px;transform:rotate({ang}deg);background-image:url({url(n)})"></div>'
    corpo += lapis(170, 760, 8, 340)
    lista.append(cena("mockup-pacote", 1200, 900, corpo))
    # imagem do produto na Hotmart (1200x1200, fundo laranja): capa do caderno com o labirinto embaixo e um lápis
    grande = "width:600px;height:849px;"
    corpo = (f'<div class="folha" style="{grande}left:380px;top:170px;transform:rotate(6deg);background-image:url({url(7)})"></div>'
             f'<div class="folha" style="{grande}left:150px;top:120px;transform:rotate(-3deg);background-image:url({url(1)})"></div>'
             + lapis(540, 960, -22, 560))
    lista.append(cena("hotmart-produto", 1200, 1200, corpo, fundo="#ff7a45"))
    # 3) quadros do "folheando": pilha fixa + página do topo trocando
    for k, n in enumerate(FOLHEAR):
        corpo = (f'<div class="folha" style="left:318px;top:96px;transform:rotate(4deg);background-image:url({url(FOLHEAR[(k + 2) % len(FOLHEAR)])})"></div>'
                 f'<div class="folha" style="left:306px;top:90px;transform:rotate(-2.5deg);background-image:url({url(FOLHEAR[(k + 1) % len(FOLHEAR)])})"></div>'
                 f'<div class="folha" style="left:300px;top:84px;background-image:url({url(n)})"></div>')
        lista.append(cena(f"quadro-{k:02d}", 1020, 780, corpo, fundo="#fff1e6"))
    (CENAS / "lista.json").write_text(json.dumps(lista, indent=1))
    print(f"{len(lista)} cenas em {CENAS}")


def finalizar():
    IMG.mkdir(exist_ok=True)
    for nome in ("mockup-capa", "mockup-pacote"):
        im = Image.open(CENAS / f"{nome}.png")
        im.save(IMG / f"{nome}.png", optimize=True)
        im.save(IMG / f"{nome}.webp", quality=88, method=6)
    HOTMART = AQUI.parents[1] / "hotmart"
    Image.open(CENAS / "hotmart-produto.png").convert("RGB").save(HOTMART / "imagem-produto.png", optimize=True)
    # vídeo e GIF do caderno sendo folheado (1,4 s por página + transição de 0,35 s)
    n = len(FOLHEAR)
    dur, tr = 1.4, 0.35
    entradas, filtros, ultimo = [], [], "0:v"
    for k in range(n):
        entradas += ["-loop", "1", "-framerate", "30", "-t", str(dur + tr), "-i", str(CENAS / f"quadro-{k:02d}.png")]
    for k in range(1, n):
        filtros.append(f"[{ultimo}][{k}:v]xfade=transition=slideleft:duration={tr}:offset={k * dur:.2f}[v{k}]")
        ultimo = f"v{k}"
    vid = IMG / "folheando.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *entradas, "-filter_complex", ";".join(filtros) + f";[{ultimo}]scale=720:-2,format=yuv420p[saida]",
                    "-map", "[saida]", "-r", "30", "-c:v", "libx264",
                    "-crf", "26", "-movflags", "+faststart", str(vid)], check=True)
    pal = CENAS / "paleta.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(vid), "-vf", "fps=12,scale=540:-1:flags=lanczos,palettegen=max_colors=96",
                    str(pal)], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(vid), "-i", str(pal), "-lavfi",
                    "fps=12,scale=540:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=4",
                    str(IMG / "folheando.gif")], check=True)
    Image.open(CENAS / "quadro-00.png").convert("RGB").resize((720, 551)).save(IMG / "folheando-poster.jpg", quality=82)
    # páginas reais em tamanho de tela
    for nome, n in AMOSTRAS.items():
        im = Image.open(PAGS / f"pagina-{n:03d}.png").convert("RGB")
        larg = 900 if nome.startswith("amostra") else 600
        im.resize((larg, round(larg * im.height / im.width)), Image.LANCZOS).save(IMG / f"{nome}.jpg", quality=84, optimize=True)
    for f in sorted(IMG.iterdir()):
        print(f"{f.name:28s} {f.stat().st_size // 1024:6d} KB")


if __name__ == "__main__":
    finalizar() if "--finalizar" in sys.argv else montar_cenas()
