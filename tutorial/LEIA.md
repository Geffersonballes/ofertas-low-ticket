# Tutorial de mineração (para o Marcos Balles)

- Vídeo: `tutorial/mineracao-marcos.mp4` (1920×1080, 30 fps, 3 min 49 s). O `.mp4` não vai para o git; o vídeo é gerado de novo com os comandos abaixo.
- Roteiro: `tutorial/roteiro.md` · Capítulos com tempo: `tutorial/capitulos.txt`
- Narração: **Piper TTS** (open source, licença MIT), voz `pt_BR-faber-medium` (rhasspy/piper-voices). Local e gratuita.
  Amostras de outras vozes pt_BR para comparar: `narracao/testes-voz/` (faber, cadu, jeff).
- Telas: HTML/CSS fotografado com Playwright; maquetes marcadas como "ilustração".

## Gerar de novo
```bash
pip install piper-tts
# modelos: https://huggingface.co/rhasspy/piper-voices/tree/main/pt/pt_BR/faber/medium (.onnx + .onnx.json)
cd tutorial/montador
python3 telas.py && node render.cjs          # telas
python3 narrar.py <pasta-dos-modelos>         # narração (Piper)
python3 montar.py                             # vídeo final
```
Texto e telas ficam em `montador/capitulos.py`; pronúncia das palavras em inglês em `montador/narrar.py`.
