"""Narração local e gratuita com Piper TTS (MIT), voz pt_BR-faber-medium.
Uso: python3 narrar.py <pasta-com-os-modelos-onnx>
As palavras em inglês e siglas são reescritas como se falam, porque o Piper lê com regras do português."""
import pathlib
import subprocess
import sys

from capitulos import CAPITULOS

AQUI = pathlib.Path(__file__).parent
NARR = AQUI.parent / "narracao"
VOZ = "pt_BR-faber-medium"

PRONUNCIA = [
    ("claude ponto ai barra code", "clóde ponto ai barra côude"),
    ("do Claude", "do Clóde"), ("o Claude", "o Clóde"), ("Claude", "Clóde"),
    ("GitHub", "guít rábi"), ("Facebook", "Feicibúqui"), ("Instagram", "Ínstagram"),
    ("low ticket", "lôu tíquet"), ("Chrome", "Crôume"),
    ("ebook, guide, planner, printable, template, spreadsheet, bundle", "í-buque, gaide, pláner, príntabou, têmpleit, sprédchit, bândou"),
    ("order bumps", "órder bâmps"), ("merge", "mérdji"), ("briefing", "brífin"),
    ("NeuroKids", "Neurokíds"), ("TDAH", "tê dê á agá"), ("pul ríquest", "pul ríquest"),
    ("Bora minerar!", "Bora minerar."),
]


def falado(t):
    for a, b in PRONUNCIA:
        t = t.replace(a, b)
    return t


def main(pasta_modelos):
    NARR.mkdir(exist_ok=True)
    modelo = pathlib.Path(pasta_modelos) / f"{VOZ}.onnx"
    for c in CAPITULOS:
        wav = NARR / f"cap{c['id']}.wav"
        subprocess.run(["piper", "-m", str(modelo), "-f", str(wav), "--length-scale", "1.06", "--sentence-silence", "0.32"],
                       input=falado(c["narracao"]), text=True, check=True, capture_output=True)
        mp3 = NARR / f"cap{c['id']}.mp3"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-ar", "48000", "-ac", "1", "-b:a", "128k", str(mp3)], check=True)
        wav.unlink()
        d = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)]).decode().strip()
        print(f"cap{c['id']}.mp3 {float(d):.1f}s")


if __name__ == "__main__":
    main(sys.argv[1])
