"""Folhas de contato para conferência: python3 contato.py <slug> [por_folha] → saida/contato-<slug>-N.png"""
import glob
import sys

from PIL import Image, ImageDraw

slug = sys.argv[1]
por = int(sys.argv[2]) if len(sys.argv) > 2 else 9
fs = sorted(glob.glob(f"saida/bump-{slug}-[0-9][0-9][0-9].png"))
cols = 3 if por <= 9 else 4
for k in range(0, len(fs), por):
    ims = [Image.open(f).convert("RGB") for f in fs[k:k + por]]
    w, h = ims[0].size
    esc = 520 / max(w, h)
    tw, th = int(w * esc), int(h * esc)
    linhas = -(-len(ims) // cols)
    folha = Image.new("RGB", (cols * tw, linhas * th), "white")
    d = ImageDraw.Draw(folha)
    for i, im in enumerate(ims):
        x, y = (i % cols) * tw, (i // cols) * th
        folha.paste(im.resize((tw, th), Image.LANCZOS), (x, y))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline="#999")
        d.text((x + 4, y + 2), str(k + i + 1), fill="red")
    folha.save(f"saida/contato-{slug}-{k // por + 1}.png")
print(len(fs), "páginas")
