# Vídeos dos anúncios — Dez Minutinhos

Montados em 2026-11-27 por `criativos/montador/` (o código vai para o git; os .mp4 não).
**Remontados em 2026-11-28** com o mesmo áudio e a mesma duração, depois da correção do material
(`revisoes/material-2026-11-28/correcoes.md`): o `folheando.mp4` agora vem do PDF final (antes era da amostra),
e as páginas 8, 11, 15, 69, 128, 142 e 143 mudaram (ligue os pontos fechando, gabarito do pinte colorido etc.).
As versões já enviadas à Meta (IDs em `campanha.md`) são as ANTIGAS: precisam ser trocadas pelo dono.
**Remontados de novo em 2026-11-28 (rodada 2)**, mesmo áudio e mesma duração: a capa do caderno agora diz
"Gabarito completo" (aparece no mockup e no cartão final dos 4) e a tela do gabarito no anúncio 2 também diz
"Gabarito completo" (antes "Gabarito no fim"). O `folheando.mp4` foi refeito do PDF novo (capa e p. 39).
**Anúncios 1 e 2 remontados de novo em 2026-11-28 (rodada 3)**, mesmo áudio e mesma duração: o zoom no plano (p. 5)
e no gabarito (p. 128) agora para com a página inteira dentro do quadro (opção `caber` do montador). `quadro-anuncio-2.jpg` refeito.
Formato: 1080×1920 (9:16), 30 fps, H.264 + AAC 48 kHz, áudio normalizado (−16 LUFS, pico ≤ −1,4 dB).
Sem música (não temos trilha licenciada). Legenda queimada em blocos de até 6 palavras, sincronizada
pelas pausas reais da fala. Só mídia real do produto: atividades do caderno completo (com o gabarito
animado), páginas do PDF, mockups e o vídeo do caderno folheando. Sem pessoas, sem rosto de criança.

| Arquivo | Roteiro | Voz | Duração | Fronteiras de frase em pausas reais |
|---|---|---|---|---|
| `anuncio-1-amandinha.mp4` | 1 | Amandinha | 22.1 s | 8/8 |
| `anuncio-2-amandinha.mp4` | 2 | Amandinha | 21.6 s | 8/8 |
| `anuncio-3-amandinha.mp4` | 3 | Amandinha | 22.9 s | 6/6 |
| `anuncio-4-amandinha.mp4` | 4 | Amandinha | 22.5 s | 8/8 |

## O que cada roteiro mostra
- **Anúncio 1:** Labirinto N1 (p. 7) com o caminho do gabarito se desenhando → cortes com a resposta aparecendo: labirinto N2 (p. 75), memória (p. 11), sudoku de figuras (p. 18), código secreto (p. 78) → caderno sendo folheado → plano de 30 dias (p. 5) com zoom no Dia 1 → folhas do Dia 1 (p. 6 e 7) → cartão final.
- **Anúncio 2:** Página "Qual é diferente?" (p. 6) subindo + carimbo PRONTO → plano (p. 5) e folhas do Dia 1 → folhas espalhadas + lápis → gabarito (p. 128) → "120 atividades · R$ 37,00" → "R$ 1,23 por dia no plano de 30 dias" → caderno folheando → cartão final.
- **Anúncio 3:** Tipografia em fundo escuro: "App educativo" com "educativo" riscado → "= tela"; "Vídeo de desenho também." → labirinto N2 (p. 75) subindo → cortes com resposta: labirinto, sudoku 6x6 (p. 69), sequência (p. 8), 7 erros (p. 68) → dois níveis lado a lado (p. 6 e p. 78) → cartão final.
- **Anúncio 4:** "10 min de tela" em fundo escuro → corte para "O que vem depois?" (p. 8) → padrões com a resposta → memória (p. 11, zoom do quadro de cima para a página toda) → labirinto (p. 13) e sudoku (p. 18) → ligue os pontos (p. 15) se ligando → caderno folheando → plano (p. 5), quadro de conquistas (p. 142), certificado (p. 143) → cartão final.

Fecho de todos: capa do caderno + "Dez Minutinhos · 120 atividades para imprimir · 4 a 10 anos ·
R$ 37,00 · Toque em Saiba mais", fundo laranja.

Quadros de referência: `quadro-anuncio-1.jpg` … `quadro-anuncio-4.jpg`.

## Conferido (controle de qualidade)
- ffprobe: 1080×1920, 30 fps, h264 + aac, duração = fala + ~1 s.
- volumedetect: pico entre −1,4 e −1,5 dB em todos.
- 10–11 quadros por vídeo (início, meio de cada frase, fecho): sem tela preta, sem texto cortado ou
  sobreposto, título abaixo dos 200 px do topo, legenda acima dos 250 px da base, legenda igual à fala.

## Refazer
```
cd criativos/montador
node paginas2x.cjs 5 6 7 8 78 128 142 143
ffmpeg -i ../../pagina/img/folheando.mp4 -vf fps=30 -q:v 3 cache/folheando/%04d.jpg
python3 montador.py            # os 8 (≈ 7 min)
python3 qc.py anuncio-1-amandinha
```


Decisão do dono (2026-11-27): só a voz Amandinha; os vídeos com a Laynner foram retirados.
