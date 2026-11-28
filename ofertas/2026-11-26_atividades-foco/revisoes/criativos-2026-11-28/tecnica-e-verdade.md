# Criativos: técnica (1.1) e verdade do produto (1.2), rodada 1

Data: 2026-11-28 · Revisor: controle de qualidade (subagente) · Nenhum arquivo editado além deste relatório.

## Veredito: **NÃO LIMPA** (só por cosméticos)

- **Bloqueia 0 · atrapalha 0 · cosmético 10.**
- **Verdade do produto: 0 problemas.** Todas as páginas, atividades, números e preços que aparecem existem e
  conferem no PDF aprovado (`produto/final/dez-minutinhos.pdf`, sha256 `66cf687c…`, igual ao `APROVACAO.md`
  do material) e na `pagina/index.html`. Nada da amostra antiga.
- A rodada só fica limpa depois de corrigir os 10 cosméticos ou de o dono aceitá-los por escrito (regra 7 do CLAUDE.md).

**Quadros olhados: 178 quadros (todos os quadros a 2 por segundo dos 4 vídeos, em folhas de contato; 44 + 43 + 46 + 45)**, mais
8 quadros em tamanho grande (1-002, 1-029, 1-031, 1-038, 2-032, 3-024, 4-011, 4-033), 19 quadros do `folheando.mp4`
e a imagem estática inteira. Isso cobre todas as frases e todo o fecho de cada vídeo.
Quadros e folhas de contato: `/tmp/claude-0/-home-user/2250d25c-d581-568f-b4e4-6cb893f20944/scratchpad/cr/`.

### Como foi conferido
- `ffprobe`, `volumedetect`, `ebur128` (pico real), `blackdetect`, `silencedetect`.
- **Áudio transcrito** com faster-whisper (modelo small, nos 4 vídeos inteiros, com tempo por palavra). Os trechos com dúvida
  foram transcritos de novo com o modelo medium. O tempo de cada palavra foi comparado com os blocos de legenda
  (`criativos/montador/tmp/anuncio-N-amandinha.html`, LEG).
- **Páginas:** as do PDF aprovado foram renderizadas com `pdftoppm` e comparadas lado a lado com:
  - o cache do montador (p. 5, 6, 7, 8, 78, 128, 142, 143);
  - os cartões de atividade do vídeo (p. 7, 8, 11, 13, 15, 18, 68, 69, 75, 78);
  - os quadros do `folheando.mp4` (p. 1, 7, 8, 39, 104, 69, 73, 68, 70);
  - os mockups.
- **Gabaritos animados conferidos à mão:**
  - sudoku 6×6 (p. 69): as 6 linhas, 6 colunas e 6 blocos estão certos;
  - sudoku de figuras (p. 18): certo;
  - memória (p. 11): coração, lua e quadrado;
  - código secreto (p. 78): BRINCAR / FAZ / BEM.
- **O PDF mudou depois dos vídeos 3 e 4.** O PDF é das 03:45. Os vídeos 3 e 4 são das 02:43 e o cache de páginas é das 02:40.
  A rodada 3 do material só mudou as p. 20, 38, 129 e 131 do caderno, e nenhuma delas aparece nos criativos. O cache e o
  `folheando` (md5 dos quadros igual ao `pagina/img/folheando.mp4`) conferem com o PDF atual.

## Resumo técnico

| Vídeo | Resolução | fps | Codecs | Duração | Pico (volumedetect / true peak) | Loudness | Tela preta | Fala × roteiro |
|---|---|---|---|---|---|---|---|---|
| anuncio-1 | 1080×1920 | 30 | h264 yuv420p + aac 48 kHz mono | 22,10 s | −1,5 dB / −1,5 dBFS | −16,5 LUFS | nenhuma | igual |
| anuncio-2 | 1080×1920 | 30 | idem | 21,63 s | −1,5 / −1,5 | −16,7 | nenhuma | 1 palavra a mais na fala ("imprime **e** entrega") |
| anuncio-3 | 1080×1920 | 30 | idem | 22,90 s | −1,5 / −1,5 | −16,2 | nenhuma | igual |
| anuncio-4 | 1080×1920 | 30 | idem | 22,50 s | −1,5 / −1,5 | −16,7 | nenhuma | igual |

**Área segura e início**
- **Área segura (os 4 vídeos):**
  - o título começa em y = 236 px, abaixo dos 200 px pedidos (o `roteiros.md` fala em 250 px, então fica 14 px acima dessa margem mais rígida);
  - a legenda vai de 1424 px a, no máximo, cerca de 1576 px quando tem 2 linhas, ou seja, pelo menos 344 px acima da base;
  - o cartão final começa em y = 300 px.
- **Nada cortado:** nenhum texto sai do quadro.
- **Sem estouro:** o pico real é −1,5 dBFS.
- **Silêncio:** só no fecho (cerca de 1 s de cartão final) e numa pausa natural de 0,44 s no vídeo 3, aos 16,1 s.
- **Início forte nos 4:** nos primeiros 3 s aparecem a atividade ou o gancho tipográfico, com título e legenda.
  - 1: labirinto com o caminho se desenhando;
  - 2: a folha subindo + carimbo PRONTO aos 1,8 s;
  - 3: "App ~~educativo~~ = tela";
  - 4: "10 min de tela", depois um corte seco para a folha.

**Problema comum aos 4 vídeos:** ver o item C3.

---

## Anúncio 1 · `anuncio-1-amandinha.mp4` (curiosidade)

| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 8,5–11,7 s | cosmético | O bloco "120 atividades prontas para imprimir," fica na tela até 11,66 s, mas "de quatro…" começa a ser falado em 11,34 s: a legenda chega cerca de 0,3 s atrasada | Cortar os blocos pelo tempo real das palavras (whisper/forced alignment) em vez de pela proporção de caracteres (`blocos_legenda`) |
| 13,1–16,7 s | cosmético | No zoom do plano (p. 5), a legenda fica por cima das linhas 25 a 27 do plano. Dá para ler, mas tampa parte da página | Subir o cartão ou limitar a altura do zoom para a página terminar acima de y = 1410 px |
| 16,7–20,9 s (fecho) | cosmético (C3, igual nos 4 vídeos) | Duas pílulas escuras empilhadas: o botão desenhado "Toque em Saiba mais" (y ≈ 1232 px) e, logo abaixo, a legenda ("Dez Minutinhos, R$ 37,00." / "Toque em Saiba mais."). No fecho do 1 e do 4 a legenda repete o que já está escrito no cartão | No cartão final, afastar a legenda do botão (ou deixá-la clara/sem caixa) para o botão continuar sendo o único elemento escuro |

**Páginas do PDF mostradas**

| Momento | Página / mídia | Confere? |
|---|---|---|
| 0–3,4 s | p. 7 Labirinto N1 (passarinho → árvore) + caminho do gabarito | sim |
| 3,4–4,5 s | p. 75 Labirinto N2 (barco → casa) + caminho | sim |
| 4,5–5,8 s | p. 11 Olhe e lembre (quadrado, lua, coração) + resposta | sim |
| 5,8–6,8 s | p. 18 Sudoku de figuras + resposta | sim |
| 6,8–8,5 s | p. 78 Código secreto + BRINCAR / FAZ / BEM | sim |
| 8,5–13,1 s | `folheando`: capa (p. 1, "Gabarito completo"), p. 7, p. 8 | sim |
| 13,1–14,9 s | p. 5 Plano de 30 dias N1 | sim |
| 14,9–16,7 s | p. 6 e p. 7 ("Dia 1 · folha 1/2"; no plano, o Dia 1 é p. 6 + p. 7) | sim |
| 16,7–22,1 s | cartão final: `mockup-capa.png` (capa do PDF final) | sim |

**Números e textos na tela**
- 10 minutinhos; 120 atividades; 4 a 10 anos; plano de 30 dias; 2 folhas por dia; R$ 37,00; "Nível 1 · 4 a 6 anos" e "Nível 2 · 7 a 10 anos" nos selos.
- Todos conferem no PDF (capa, "Como usar", p. 5) e na página.

---

## Anúncio 2 · `anuncio-2-amandinha.mp4` (zero preparo)

| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 6,2–9,0 s | cosmético | A narração diz "Abre, imprime **e** entrega com um lápis". Os dois modelos de transcrição (small e medium) ouvem o "e". A legenda diz "Abre, imprime, entrega com um lápis." | Ouvir e confirmar. Se a voz diz "e", trocar a legenda para "Abre, imprime e entrega com um lápis." (ou regerar a fala sem o "e") |
| 14,0–17,3 s | cosmético | No texto grande, "por dia no plano de 30 / **dias**" deixa a palavra "dias" sozinha na 2ª linha. A legenda também quebra mal: "R$ 1,23 por dia, no" / "plano de 30 dias." | Quebrar em "por dia no plano" / "de 30 dias" (ou diminuir a fonte). Na legenda: "R$ 1,23 por dia," / "no plano de 30 dias." |
| 19,2–21,6 s | cosmético (C3) | Botão e legenda empilhados no fecho | Ver o anúncio 1 |

**Páginas do PDF mostradas**

| Momento | Página / mídia | Confere? |
|---|---|---|
| 0–3,5 s | p. 6 "Qual é diferente?" subindo + carimbo PRONTO (o carimbo é desenhado sobre a página; não está no PDF, e isso é esperado) | sim |
| 3,5–4,8 s | p. 5 Plano N1 | sim |
| 4,8–6,2 s | p. 6 e p. 7 (Dia 1) | sim |
| 6,2–9,0 s | `mockup-pacote.png`: capa final + p. 68, p. 69, p. 8 e p. 7 em leque | sim |
| 9,0–10,9 s | p. 128 Gabarito (o título "Gabarito completo" bate com a capa) | sim |
| 10,9–17,3 s | `mockup-capa.png` + "120 atividades", "R$ 37,00", "R$ 1,23 por dia no plano de 30 dias" | sim (página: "R$ 1,23 por dia no plano de 30 dias"; R$ 37,00 ÷ 30 = R$ 1,23) |
| 17,3–19,2 s | `folheando`: capa | sim |
| 19,2–21,6 s | cartão final | sim |

**Textos na tela**
- "Uma vez só": a página diz "R$ 37,00, uma vez só".
- "Imprime de novo quando quiser": a página diz "O arquivo é seu: imprima…".
- "Gabarito completo": está na capa do PDF.
- Os 3 conferem.

---

## Anúncio 3 · `anuncio-3-amandinha.mp4` (app também é tela)

| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 11,2–16,3 s | cosmético | A legenda separa a faixa de idade: "2 níveis: de 4 a" / "6 anos, sem precisar ler," / "e de 7 a 10." Por cerca de 1,5 s, a tela mostra "de 4 a" sem o fim | Blocos: "2 níveis: de 4 a 6 anos," / "sem precisar ler," / "e de 7 a 10." (nunca quebrar no meio de "X a Y") |
| 16,3–22,9 s | cosmético (C3) | Botão e legenda (2 linhas) empilhados no fecho | Ver o anúncio 1 |

**Páginas do PDF mostradas**

| Momento | Página / mídia | Confere? |
|---|---|---|
| 0–4,2 s | só tipografia (sem página) | n/a |
| 4,2–8,1 s | p. 75 Labirinto N2 (entra por baixo; depois, o caminho) | sim |
| 8,1–9,1 s | p. 69 Sudoku 6×6 + números (solução conferida) | sim |
| 9,1–10,1 s | p. 8 "O que vem depois?" N1 + círculos | sim |
| 10,1–11,2 s | p. 68 Jogo dos 7 erros N2 + círculos | sim |
| 11,2–16,3 s | p. 6 (N1, "Nível 1 · 4 a 6 anos · sem leitura") e p. 78 (N2, "Nível 2 · 7 a 10 anos") | sim (os níveis batem com os selos do PDF; "Como usar": N1 "não pede leitura") |
| 16,3–22,9 s | cartão final | sim |

---

## Anúncio 4 · `anuncio-4-amandinha.mp4` (troca de tela)

| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 4,9–5,6 s | cosmético | No começo do zoom da memória (p. 11, escala 1,55), o selo do título "Memória" fica por cima do cabeçalho do cartão ("Dez Minutinhos · Nível 1"), e o cartão quase encosta nas bordas da tela (cerca de 24 px) | Começar o zoom mais baixo (cerca de 1,35) ou com o foco mais para baixo, para o cabeçalho do cartão ficar abaixo do título |
| 14,6–18,5 s | cosmético | A legenda de 2 linhas ("vem pronto, com quadro de conquistas.") tampa o rodapé e a última fileira das p. 5, 142 e 143 | Encurtar o bloco (ex.: "O plano de 30 dias" / "já vem pronto," / "com quadro de conquistas.") ou subir as páginas |
| 18,5–22,5 s | cosmético (C3) | Botão e legenda empilhados no fecho | Ver o anúncio 1 |

**Páginas do PDF mostradas**

| Momento | Página / mídia | Confere? |
|---|---|---|
| 0–1,65 s | tipografia "10 min de tela" | n/a |
| 1,65–4,9 s | p. 8 "O que vem depois?" N1 (primeiro sem resposta, depois com círculos) | sim |
| 4,9–8,1 s | p. 11 Olhe e lembre (texto "Dobre a folha na linha" igual ao PDF) + resposta | sim |
| 8,1–9,3 s | p. 13 Labirinto N1 (peixe → flor) + caminho | sim |
| 9,3–10,5 s | p. 18 Sudoku de figuras + resposta | sim |
| 10,5–11,8 s | p. 15 Ligue os pontos 1–12 (a casa fecha no 1) | sim |
| 11,8–14,6 s | `folheando`: capa, p. 7 | sim |
| 14,6–15,9 s | p. 5 Plano N1 | sim |
| 15,9–17,2 s | p. 142 Meu quadro de conquistas (Bônus 1) | sim |
| 17,2–18,5 s | p. 143 Certificados Semana 1 e 2 (Bônus 1) | sim |
| 18,5–22,5 s | cartão final | sim |

**Textos na tela**
- "Sem saber ensinar · sem montar rotina": a página diz "Preciso… saber ensinar? Não. Cada folha já diz o que fazer".
- "Plano pronto · quadro de conquistas": a página diz "Bônus 1 Quadro de conquistas + 6 certificados".
- Os 2 conferem.

---

## Anúncio 5 · `estatico/anuncio-5-ferias-4x5.jpg` (férias)

**Técnica:** 1080×1350 (4:5), JPEG sRGB.
- **Pouco texto:** cerca de 20 palavras.
- **Título:** em letra de cerca de 92 px, legível no celular.
- **Rodapé:** "4 a 10 anos · 2 níveis · R$ 37,00" em 46 px.

| Ponto | Gravidade | Problema | Sugestão |
|---|---|---|---|
| Miniatura do plano (canto inferior esquerdo) | cosmético | A p. 5 tem 170 px de largura, então nada nela é legível no celular. Funciona só como forma, porque a legenda ao lado explica | Ampliar um recorte das linhas Dia 1 a Dia 3, ou aceitar como ilustração |
| Leque de páginas (direita) | cosmético | A p. 8 e a p. 78 ficam quase todas escondidas atrás da p. 7, e só aparecem tiras ("?", F/T/Z). O `roteiros.md` pedia um leque com labirinto, 7 erros (p. 68) e código secreto, e a imagem usa a p. 8 no lugar da p. 68 | Abrir mais o leque (mais rotação/afastamento) para cada página mostrar pelo menos o título da atividade. Se quiser seguir o roteiro, trocar a p. 8 pela p. 68 |

**Páginas do PDF mostradas:**
- `mockup-capa.png` (capa final, com "Gabarito completo");
- p. 7 Labirinto N1;
- p. 8 "O que vem depois?" N1 (parcial);
- p. 78 Código secreto N2 (parcial);
- p. 5 Plano de 30 dias.

Todas conferem.

**Números e textos:**
- "30 dias de atividades prontas para imprimir", "Plano de 30 dias", "2 folhas por dia", "4 a 10 anos", "2 níveis" e "R$ 37,00" conferem.
- "Férias": a página também fala de férias.

**Observação (não conta como achado):** o `roteiros.md` prevê também a peça 1:1 (1080×1080) e um "(link 1:1)" no anúncio. A peça 1:1 não existe na pasta `criativos/estatico/`.

---

## Verdade do produto: números conferidos

| Na tela | PDF aprovado | `pagina/index.html` |
|---|---|---|
| 120 atividades | capa: "120 ATIVIDADES · 2 NÍVEIS · PLANO DE 30 DIAS" | sim (10×) |
| 2 níveis · 4 a 6 / 7 a 10 anos | capa e "Como usar"; selos de nível nas páginas | sim |
| 4 a 10 anos | capa (N1 4 a 6 + N2 7 a 10) | sim |
| Plano de 30 dias · 2 folhas por dia | p. 5 (N1) e p. 67 (N2); "Como usar" item 2 | sim |
| Sem precisar ler (N1) | "Nível 1 (4 a 6 anos) não pede leitura" | sim |
| R$ 37,00 · uma vez só | n/a (preço) | sim ("R$ 37,00, uma vez só") |
| R$ 1,23 por dia no plano de 30 dias | 37 ÷ 30 = 1,233 | sim (literal) |
| Gabarito completo | capa e p. 128 em diante | sim |
| Quadro de conquistas · certificados | p. 142 e 143 (Bônus 1) | sim ("Quadro de conquistas + 6 certificados") |
| 3 bônus | não aparece na tela de nenhum criativo (só no texto do anúncio 5, fora deste bloco) | sim ("E mais 3 bônus") |

Nenhuma página, atividade ou número da amostra antiga. Os 4 vídeos e a imagem usam só o PDF final, os mockups
refeitos dele e o `folheando.mp4` refeito dele.

## Lista de correções (para o montador)

1. **A1:** cortar as legendas pelo tempo real das palavras (resolve o atraso de 0,3 s e ajuda nos itens 5 e 6).
2. **A1:** a legenda tampa o plano (p. 5) no zoom.
3. **Todos:** separar a legenda do botão "Toque em Saiba mais" no cartão final.
4. **A2:** legenda "imprime e entrega" (confirmar de ouvido).
5. **A2:** "dias" sozinho na linha e a quebra "no / plano".
6. **A3:** não quebrar "de 4 a / 6 anos".
7. **A4:** título "Memória" sobre o cabeçalho do cartão no começo do zoom.
8. **A4:** a legenda de 2 linhas tampa o pé das p. 5, 142 e 143.
9. **Estático:** a miniatura do plano fica ilegível.
10. **Estático:** as p. 8 e 78 ficam escondidas no leque.
