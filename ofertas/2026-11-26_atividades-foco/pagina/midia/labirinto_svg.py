"""SVG compacto do labirinto da amostra (o mesmo de img/dentro-1.jpg), com o caminho do gabarito
como <path> separado para animar na página. Lê o gerador do produto sem gravar nada lá.
Uso: python3 -B labirinto_svg.py > cenas/labirinto.svg   (o conteúdo vai inline em index.html)"""
import pathlib
import random
import re
import sys

sys.dont_write_bytecode = True
GER = pathlib.Path(__file__).parents[2] / "produto" / "gerador"
sys.path.insert(0, str(GER))
import atividades as A  # noqa: E402
import gerar_amostra as G  # noqa: E402

d = A.labirinto(1, random.Random(G.SEMENTE))  # 1ª atividade da amostra = página 3 do PDF
gab = d["gabarito_svg"]
pts = re.search(r'<polyline points="([^"]+)"', gab).group(1).split()
f = lambda v: f"{float(v):.1f}".rstrip("0").rstrip(".")
cam = "M" + " L".join(",".join(f(c) for c in p.split(",")) for p in pts)
linhas = re.findall(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"/>', d["svg"])
paredes = "".join(f"M{f(a)} {f(b)}L{f(c)} {f(e)}" for a, b, c, e in linhas)
icones = re.sub(r'<g stroke="#1d1d1f" stroke-width="1.6" stroke-linecap="round">.*?</g>', "", d["svg"], count=1, flags=re.S)
icones = re.sub(r"(\d+\.\d{2})\d+", r"\1", icones)
print(f'<svg viewBox="14 0 154 222" role="img" aria-label="Labirinto do Nível 1 com o caminho do gabarito">'
      f'<path class="sol" d="{cam}" pathLength="1" fill="none" stroke="#ff7a45" stroke-width="6.9" stroke-linejoin="round" stroke-linecap="round"/>'
      f'<path d="{paredes}" stroke="#1d1d1f" stroke-width="1.6" stroke-linecap="round"/>{icones}</svg>')
