"""Tempo real de cada palavra da narração (faster-whisper, tempo por palavra). O montador corta as legendas
por esses tempos (antes: proporção de caracteres, que atrasava ou adiantava blocos).
Uso: python3 palavras.py [amandinha] [modelo]   → cache/palavras/<voz>-<n>.json  (uma vez por áudio)"""
import json
import pathlib
import subprocess
import sys

import numpy as np

from faster_whisper import WhisperModel

AQUI = pathlib.Path(__file__).resolve().parent
AUDIO = AQUI.parents[0] / "audio"
SAIDA = AQUI / "cache" / "palavras"
voz = sys.argv[1] if len(sys.argv) > 1 else "amandinha"
modelo = WhisperModel(sys.argv[2] if len(sys.argv) > 2 else "medium", device="cpu", compute_type="int8")
SAIDA.mkdir(parents=True, exist_ok=True)
for n in (1, 2, 3, 4):
    # decodifica com o ffmpeg (o PyAV instalado não aceita o decode_audio do faster-whisper)
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(AUDIO / f"{voz}-{n}.mp3"), "-ac", "1", "-ar", "16000",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    segs, _ = modelo.transcribe(np.frombuffer(pcm, np.float32), language="pt", word_timestamps=True, beam_size=5)
    pal = [{"w": w.word.strip(), "t0": round(w.start, 3), "t1": round(w.end, 3)} for s in segs for w in s.words]
    (SAIDA / f"{voz}-{n}.json").write_text(json.dumps(pal, ensure_ascii=False, indent=0), encoding="utf-8")
    print(n, " ".join(f'{p["w"]}@{p["t0"]:.2f}' for p in pal))
