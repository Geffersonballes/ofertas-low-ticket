"""Controle de qualidade de um vídeo: ffprobe (duração, resolução, fps, áudio), pico de volume e
folha de contato com quadros no meio de cada frase + início e fecho. Uso: python3 qc.py anuncio-1-laynner"""
import json, pathlib, subprocess, sys
from PIL import Image, ImageDraw
AQUI = pathlib.Path(__file__).resolve().parent
VID = AQUI.parents[0] / "videos"
nome = sys.argv[1]
mp4 = VID / f"{nome}.mp4"
info = json.loads((AQUI / "tmp" / f"{nome}.json").read_text())
pr = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(mp4)],
                               capture_output=True, text=True).stdout)
v = [s for s in pr["streams"] if s["codec_type"] == "video"][0]
a = [s for s in pr["streams"] if s["codec_type"] == "audio"]
vol = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(mp4), "-af", "volumedetect", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
pico = [l.split(":")[1].strip() for l in vol.splitlines() if "max_volume" in l]
print(nome, f"{v['width']}x{v['height']}", v["r_frame_rate"], v["codec_name"], "| dur", pr["format"]["duration"][:5],
      "| áudio", a[0]["codec_name"] if a else "NENHUM", "| pico", pico)
ts = [0.15] + [round((f["t0"] + f["t1"]) / 2, 2) for f in info["frases"]] + [info["duracao"] - 0.3]
out = AQUI / "tmp" / "qc"
out.mkdir(exist_ok=True)
ims = []
for i, t in enumerate(ts):
    f = out / f"{nome}-{i:02d}.jpg"
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(t), "-i", str(mp4), "-frames:v", "1", "-vf", "scale=270:480", str(f)], check=True)
    im = Image.open(f).convert("RGB"); ImageDraw.Draw(im).text((4, 4), f"{t:.1f}s", fill=(255, 0, 0)); ims.append(im)
cols = 6
rows = -(-len(ims) // cols)
sheet = Image.new("RGB", (270 * cols, 480 * rows), "white")
for k, im in enumerate(ims):
    sheet.paste(im, ((k % cols) * 270, (k // cols) * 480))
sheet.save(out / f"{nome}-contato.jpg", quality=85)
print("contato:", out / f"{nome}-contato.jpg")
