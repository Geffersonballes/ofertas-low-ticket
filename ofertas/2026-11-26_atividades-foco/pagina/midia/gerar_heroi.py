"""Mockup do topo (rodada 1 de design): caderno impresso em perspectiva sobre fundo laranja, com folhas
soltas reais (labirinto e código secreto) e um lápis. Só páginas reais do caderno (produto/gerador/saida/vitrine-XX.png).
Uso:  python3 gerar_heroi.py && node fotografar.cjs lista-heroi.json && python3 gerar_heroi.py --finalizar
Saída: ../img/heroi.webp (fundo #ff7a45 nas bordas, igual ao fundo do topo da página)."""
import json
import pathlib
import sys

from PIL import Image

AQUI = pathlib.Path(__file__).parent
PAGS = AQUI.parents[1] / "produto" / "gerador" / "saida"
CENAS = AQUI / "cenas"
IMG = AQUI.parent / "img"
W, H = 1200, 900
LARANJA = "#ff7a45"


def url(n):
    return (PAGS / f"vitrine-{n:02d}.png").as_uri()


def lapis(x, y, ang, w):
    return f"""<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:rotate({ang}deg);filter:drop-shadow(0 14px 14px rgba(110,35,0,.35))"
 viewBox="0 0 360 30"><polygon points="0,15 34,3 34,27" fill="#f4d3a8"/><polygon points="0,15 12,11 12,19" fill="#333"/>
 <rect x="34" y="3" width="270" height="24" fill="#ffc93c"/><rect x="34" y="3" width="270" height="8" fill="#ffe08a"/>
 <rect x="34" y="19" width="270" height="8" fill="#f0b21f"/>
 <rect x="304" y="3" width="26" height="24" fill="#c9c9c9"/><rect x="330" y="3" width="30" height="24" rx="5" fill="#f29bb0"/></svg>"""


def montar():
    fl = "position:absolute;width:380px;height:537px;background:#fff center/cover no-repeat;border-radius:4px;"
    sombra = "box-shadow:0 2px 3px rgba(110,35,0,.18),0 26px 50px rgba(110,35,0,.32);"
    # folhas do caderno (grossura): várias camadas atrás da capa
    camadas = "".join(
        f'<div class="pg" style="transform:translateZ({-k * 2.4:.1f}px);background:{"#fff" if k % 2 else "#efe7df"}"></div>'
        for k in range(14, 0, -1))
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{LARANJA}}}
.palco{{position:relative;width:100%;height:100%;perspective:1700px;
  background:radial-gradient(closest-side at 52% 50%,#ffb08a,rgba(255,122,69,0) 100%)}}
.caderno{{position:absolute;left:400px;top:150px;width:430px;height:608px;transform-style:preserve-3d;
  transform:rotateX(30deg) rotateY(-30deg) rotateZ(7deg)}}
.pg,.capa{{position:absolute;inset:0;border-radius:3px}}
.pg{{box-shadow:0 0 0 1px rgba(0,0,0,.05)}}
.capa{{background:#fff url({url(1)}) center/cover no-repeat;transform:translateZ(1px);
  box-shadow:inset 0 0 0 1px rgba(0,0,0,.04)}}
.chao{{position:absolute;left:380px;top:600px;width:470px;height:150px;border-radius:50%;
  background:rgba(120,38,0,.38);filter:blur(30px);transform:rotate(-4deg)}}
.pg:first-child{{box-shadow:0 30px 60px rgba(110,35,0,.35)}}
</style></head><body><div class="palco">
<div style="{fl}{sombra}left:120px;top:190px;transform:rotate(-15deg)">
  <div style="position:absolute;inset:0;background:url({url(3)}) center/cover"></div></div>
<div style="{fl}{sombra}left:720px;top:150px;transform:rotate(13deg);background-image:url({url(12)})"></div>
<div class="chao"></div>
<div class="caderno">{camadas}<div class="capa"></div></div>
{lapis(70, 770, -6, 440)}
</div></body></html>"""
    CENAS.mkdir(exist_ok=True)
    (CENAS / "heroi.html").write_text(html, encoding="utf-8")
    (CENAS / "lista-heroi.json").write_text(json.dumps([{"nome": "heroi", "w": W, "h": H, "transparente": False}]))
    print("cena heroi.html pronta")


def finalizar():
    im = Image.open(CENAS / "heroi.png").convert("RGB").resize((960, 720), Image.LANCZOS)
    for q in (80, 74, 68, 62, 56):
        im.save(IMG / "heroi.webp", quality=q, method=6)
        kb = (IMG / "heroi.webp").stat().st_size / 1024
        if kb <= 90:
            break
    print(f"heroi.webp {kb:.0f} KB (qualidade {q})")


if __name__ == "__main__":
    finalizar() if "--finalizar" in sys.argv else montar()
