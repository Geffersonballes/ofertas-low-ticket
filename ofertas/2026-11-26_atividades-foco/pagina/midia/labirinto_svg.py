"""SVG compacto do labirinto da pág. 7 do caderno vendido (o mesmo de img/dentro-1.jpg), com o caminho do
gabarito como <path> separado para animar na página. Lê o gerador do produto sem gravar nada lá.
(Até 2026-11-28 vinha do PDF de amostra, que tinha outro labirinto.)
Uso: python3 -B labirinto_svg.py > cenas/labirinto.svg   (o conteúdo vai inline em index.html)"""
import pathlib
import random
import re
import sys

sys.dont_write_bytecode = True
GER = pathlib.Path(__file__).parents[2] / "produto" / "gerador"
sys.path.insert(0, str(GER))
import gerar_completo as GC  # noqa: E402

# mesma sequência do gerar_completo.main(): o dia 1 do Nível 1 é a pág. 6 (folha 1) e a pág. 7 (folha 2)
rng = random.Random(GC.SEMENTE)
dias = GC.agenda(GC.nivel1(rng), rng)
(_, fa), (_, fb) = dias[0]
fa()
d = fb()
assert d["titulo"] == "Labirinto", d["titulo"]
gab = d["gabarito_svg"]
pts = re.search(r'<polyline points="([^"]+)"', gab).group(1).split()
f = lambda v: f"{float(v):.1f}".rstrip("0").rstrip(".")
cam = "M" + " L".join(",".join(f(c) for c in p.split(",")) for p in pts)
linhas = re.findall(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"/>', d["svg"])
paredes = "".join(f"M{f(a)} {f(b)}L{f(c)} {f(e)}" for a, b, c, e in linhas)
esp = re.search(r'<g stroke="#1d1d1f" stroke-width="([\d.]+)" stroke-linecap="round">', d["svg"]).group(1)
icones = re.sub(r'<g stroke="#1d1d1f" stroke-width="[\d.]+" stroke-linecap="round">.*?</g>', "", d["svg"], count=1, flags=re.S)
icones = re.sub(r"(\d+\.\d{2})\d+", r"\1", icones)
larg_sol = re.search(r'<polyline[^>]*stroke-width="([\d.]+)"', gab).group(1)
xs = [float(v) for a, b, c, e in linhas for v in (a, c)]
ys = [float(v) for a, b, c, e in linhas for v in (b, e)]
vb = f"{min(xs) - 4:.0f} {0} {max(xs) - min(xs) + 8:.0f} {max(ys) + 26:.0f}"  # inclui os ícones de início e fim
print(f'<svg viewBox="{vb}" role="img" aria-label="Labirinto do Nível 1 com o caminho do gabarito">'
      f'<path class="sol" d="{cam}" pathLength="1" fill="none" stroke="#ff7a45" stroke-width="{larg_sol}" stroke-linejoin="round" stroke-linecap="round"/>'
      f'<path d="{paredes}" stroke="#1d1d1f" stroke-width="{esp}" stroke-linecap="round"/>{icones}</svg>')
