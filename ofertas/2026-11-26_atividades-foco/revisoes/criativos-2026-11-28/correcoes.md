# Criativos · correções da rodada 1 · Dez Minutinhos

- Data: 2026-11-28 · Base: `conformidade-e-textos.md` (3 atrapalha + 6 cosméticos) e `tecnica-e-verdade.md` (10 cosméticos).
- Tudo corrigido, inclusive os cosméticos. Nenhum item ficou "aceito como está".
- Material intocado: `python3 ferramentas/conferir_material.py ofertas/2026-11-26_atividades-foco` → "MATERIAL APROVADO"
  (8 PDFs iguais ao `revisoes/material-2026-11-28/APROVACAO.md`), antes e depois.
- Nada publicado e nada enviado à Meta nem à Hotmart. Sem commit e sem push.
- **Áudio:** o mesmo, sem regravar. Os 4 vídeos têm a mesma duração de antes (22,10 / 21,63 / 22,90 / 22,50 s) e as mesmas
  fronteiras de frase em pausas (8/8, 8/8, 6/6, 8/8).
- **Nenhum ajuste exige regravar.** A frase dita que difere do roteiro é "Abre, imprime **e** entrega", e só no A2: a legenda e o
  roteiro passaram a seguir o áudio. As outras correções de texto são do anúncio (texto principal, descrição), e nenhuma
  corresponde a uma frase narrada.

## Tabela

| Item | Arquivo | O que foi feito | Conferido |
|---|---|---|---|
| A1 texto principal ("4 atividades em 10 min") | `criativos/roteiros.md` | 1º parágrafo trocado pelo texto pronto da conformidade: "Um labirinto e um jogo de memória. É isso que cabe em uns 10 minutinhos de papel e lápis. No outro dia, outras duas folhas: sudoku, padrões, ligue os pontos, código secreto…". A narração "Isto é o que cabe em dez minutinhos…" fica como está, porque aponta para uma folha só (conformidade: conforme) | "uns 10 minutinhos" e "Duas folhas por dia" estão na `pagina/index.html` |
| A1 descrição | `roteiros.md` | "Acesso pelo e-mail após o pagamento" | frase literal da página |
| A2 descrição | `roteiros.md` | "R$ 37,00, uma vez só. Sem mensalidade." | página: "R$ 37,00, uma vez só", "sem mensalidade" |
| A2 "sem separar por idade" | `roteiros.md` | 2º parágrafo: "Sem procurar folhinha na internet e sem comprar material: as folhas já vêm separadas em 2 níveis de idade. Cada dia do plano…" | sim |
| A4 "uma vez só" | `roteiros.md` | Última linha: "120 atividades · 4 a 10 anos · R$ 37,00, uma vez só · garantia de 7 dias." | sim |
| Cartão final: roteiro × vídeo | `montador/montador.py` (cena `final`), `roteiros.md`, `videos/LEIA.md` | "Garantia de 7 dias" entrou no cartão dos 4 vídeos (abaixo do preço). Roteiro e LEIA descrevem o fecho montado | Quadros do fecho dos 4 (folhas de contato); "Garantia de 7 dias" está na página (preço e garantia não estão no PDF, como nos outros criativos) |
| C3 fecho: 2 pílulas escuras empilhadas (os 4) | `montador.py` | Botão "Toque em Saiba mais" em y 598–650 (540 px de base). No fecho, a legenda fica clara (fundo branco, letra escura) e desce para y 748: são 98 px (196 px no 1080) entre os dois, e o único elemento escuro é o botão | Quadros 16,75–22,75 s dos 4 vídeos, mais o A1 aos 20,0 s em tamanho grande |
| A1 legenda ~0,3 s atrasada (8,5–11,7 s) | `montador/palavras.py` (novo), `montador.py` (`tempos_palavras`, `blocos_legenda`) | A legenda agora é cortada pelo tempo real das palavras. `palavras.py` transcreve os 4 mp3 com faster-whisper **medium** (tempo por palavra) e grava `cache/palavras/amandinha-N.json`. O montador casa a narração escrita com a transcrição (difflib; "cento e vinte" ↔ "120") e cada bloco entra 0,05 s antes da 1ª palavra. Os blocos são marcados com "\|" no roteiro do montador (máx. 7 palavras, com trava). "120 atividades prontas para imprimir," sai aos 11,33 s e "de" é falado aos 11,38 s | Tempos dos blocos em `tmp/anuncio-N-amandinha.json` ("legenda") comparados com a transcrição, nos 4 vídeos |
| A2 "imprime e entrega" | `montador.py`, `roteiros.md` | O medium confirmou o "e" (7,46 s), igual ao small. Legenda e roteiro: "Abre, imprime e entrega com um lápis." Áudio sem mudança | Quadros 6,25–8,75 s |
| A2 "dias" sozinho e quebra "no / plano" | `montador.py` | Texto grande em 2 linhas fixas: "por dia no plano" / "de 30 dias". Legenda em 2 blocos: "R$ 1,23 por dia," / "no plano de 30 dias." Espaços que não quebram em "4 a 10 anos", "30 dias", "R$ 37,00" etc. (`nb()`), e `text-wrap: balance` no título e na legenda | Quadros 14,25–17,25 s; A2 aos 15,5 s em tamanho grande |
| A3 "de 4 a / 6 anos" | `montador.py` | Blocos: "2 níveis: de 4 a 6 anos," / "sem precisar ler," / "e de 7 a 10." (mais o `nb()`) | Quadros 11,25–16,25 s; A3 aos 12,0 s em tamanho grande |
| A1 legenda sobre o plano (13–16,7 s) | `montador.py` (opção `janela`) | O zoom da página roda dentro de uma janela que termina em y 708 (1416 px), com um fade de 24 px. A página ampliada não passa mais por baixo da legenda (y 712+). A mesma janela foi usada no plano e no gabarito do A2 (mesmo layout) | A1 13,25–16,25 s; A1 aos 14,6 s em tamanho grande |
| A4 legenda sobre o pé das p. 5, 142 e 143 (14,6–18,5 s) | `montador.py` | p. 5 dentro da janela. p. 142 e 143 com zoom 1,04× no centro: a página inteira fica entre y 186 e 704. Legenda em 3 blocos de 1 linha ("O plano de 30 dias" / "já vem pronto," / "com quadro de conquistas.") | A4 14,75–18,25 s; A4 aos 16,6 s em tamanho grande |
| A4 título "Memória" sobre o cabeçalho do cartão e cartão na borda (4,9–5,6 s) | `montador.py` | Zoom 1,25→1,0 com foco no topo do cartão (o cabeçalho fica parado em y 195, abaixo do título, que termina por volta de y 163) e dentro da janela. Margem lateral no início: cerca de 50 px (100 px no 1080) | A4 4,75–6,25 s; A4 aos 5,0 s em tamanho grande |
| Estático: plano ilegível | `criativos/estatico/gerar.cjs` | A miniatura da p. 5 saiu, porque nenhuma ampliação que cabe na peça deixa a tabela legível: o texto da linha tem cerca de 7 pt. Ela virou texto grande (50 px) com marcadores: "Plano de 30 dias" / "2 folhas por dia" | Imagem olhada inteira; frases da página e do PDF (p. 5, "Como usar") |
| Estático: leque escondia p. 8/p. 78 e fugia do roteiro | `gerar.cjs` | Leque aberto com as páginas do roteiro: p. 7 (labirinto N1), p. 68 (7 erros N2) e p. 78 (código secreto N2). O `gerar.cjs` rasteriza essas páginas do **PDF aprovado** com `pdftoppm` (150 dpi, `montador/cache/pdf/`). As 3 aparecem inteiras, cada uma com o título | Imagem olhada. Numeração conferida: rodapé "página 7/68/78" |
| Estático 1:1 (não existia) | `gerar.cjs` → `anuncio-5-ferias-1x1.jpg` (1080×1080) | Layout do roteiro: pergunta no topo, capa e p. 7 e p. 78 em leque, rodapé laranja. O rodapé ficou "Plano de 30 dias · 4 a 10 anos · R$ 37,00" porque "30 dias prontos para imprimir", do roteiro antigo, não existe na página. Roteiro atualizado | Imagem olhada inteira |
| Roteiro A5: leque e "Arquivo final" | `roteiros.md` | Peça 4:5 e 1:1 descritas como montadas. "Arquivo final" com os 2 arquivos; os A1–A4 também com o caminho do .mp4 | sim |
| A5 só na temporada | `campanha.md`, `roteiros.md` | "Janela do A5 (férias): rodar só de 2026-12-15 a 2027-02-28". Até lá o A5 fica pausado mesmo com a C2 ativa | sim |
| IDs de vídeo × anúncios | `campanha.md` | Aviso: os IDs das duas tabelas não batem e **os dois conjuntos são de vídeos antigos**. Os anúncios pausados estão marcados "antigo: trocar após o Portão C". Mídia nova só no local. Passo a passo depois de "CRIATIVOS APROVADOS". Nada mexido na Meta | sim |

## Arquivos regenerados

- `criativos/videos/anuncio-1-amandinha.mp4` · `anuncio-2-amandinha.mp4` · `anuncio-3-amandinha.mp4` · `anuncio-4-amandinha.mp4`
  (1080×1920, 30 fps, h264 + aac, pico −1,5 dB, durações iguais às de antes; `qc.py` rodado nos 4)
- `criativos/videos/quadro-anuncio-1.jpg` … `quadro-anuncio-4.jpg` (nos mesmos instantes de antes: 2,0 / 3,2 / 1,4 / 11,1 s, `-q:v 3`)
- `criativos/estatico/anuncio-5-ferias-4x5.jpg` (refeito) e `criativos/estatico/anuncio-5-ferias-1x1.jpg` (novo)
- Regeneráveis (fora do git): `montador/cache/palavras/amandinha-1..4.json`, `montador/cache/pdf/pag-007|068|078.png`,
  `montador/tmp/anuncio-N-amandinha.{html,json}`, `montador/tmp/qc/*`

sha256 (início): mp4 1 `998a9b40…`, 2 `6c27ae78…`, 3 `bcf87fbc…`, 4 `b84f051e…` · 1x1 `cf0e3dcb…` · 4x5 `73e0b0ee…`

## Código e textos alterados

- `criativos/montador/montador.py`: blocos "|" e tempo real das palavras; `nb()`; `text-wrap: balance`; opção `janela`;
  zooms da memória (A4) e das p. 142/143; texto grande do A2 em 2 linhas; cartão final com garantia; legenda clara no fecho;
  "imprime e entrega"; alvo padrão só Amandinha.
- `criativos/montador/palavras.py` (novo): faster-whisper com tempo por palavra; decodifica com o ffmpeg, porque o PyAV
  instalado não aceita o `decode_audio` do faster-whisper.
- `criativos/estatico/gerar.cjs`: páginas do PDF aprovado; leque p. 7/68/78; plano em texto; peça 1:1.
- `criativos/roteiros.md`, `criativos/videos/LEIA.md`, `campanha.md`, `status.md`, `aprendizados/processo.md`.

## Como foi olhado

- **Folhas de contato a 2 quadros por segundo** dos 4 vídeos inteiros (44 + 43 + 46 + 45 quadros), depois da montagem final.
- **8 quadros em tamanho grande:** A1 14,6 e 20,0 s; A4 5,0, 13,0 e 16,6 s; A2 4,3 e 15,5 s; A3 12,0 s.
- **Os 4 `quadro-anuncio-*.jpg`** e **as 2 imagens estáticas inteiras.**
- **Tempos dos blocos de legenda** (`tmp/anuncio-N-amandinha.json`) conferidos com a transcrição palavra por palavra.

**Fica para a revisão da rodada 2:** pela skill, todos os criativos que mudaram (os 4 vídeos, as 2 imagens e os textos dos
anúncios 1, 2, 4 e 5) têm de ser revisados de novo. Esta correção não substitui essa revisão. Só depois vem o Portão C.

## Rodada 2

- Data: 2026-11-28 · Base: `rodada2.md` (6 cosméticos: A2-1, A3-1, A4-1, A4-2, C-1, R-1). Os 6 corrigidos; nenhum "aceito como está".
- Material intocado: `python3 ferramentas/conferir_material.py ofertas/2026-11-26_atividades-foco` → "MATERIAL APROVADO" (8 PDFs).
- Nada publicado, nada enviado à Meta nem à Hotmart. Sem commit e sem push.
- **Remontados só os vídeos 2, 3 e 4**, com o mesmo áudio e a mesma duração (21,63 / 22,90 / 22,50 s) e as mesmas fronteiras
  em pausas (8/8, 6/6, 8/8). O A1 e o A5 (estáticos) não mudaram: a C-1 foi resolvida no roteiro, porque os 4 vídeos já cumprem a regra da skill.

| Item | Arquivo | O que foi feito | Conferido |
|---|---|---|---|
| A2-1 · página do A2 sobe por baixo da legenda (0,0–0,9 s) e miniatura | `criativos/montador/montador.py` (cena `carimbo`: opções `janela` e `sobe`) | A p. 6 sobe **dentro da `janela`** (termina em y 1416 com fade, acima da legenda em y 1424) e parte de 260 px abaixo da posição final (era 760 px, fora da tela). No 1º quadro (miniatura) já aparecem o título "Imprimiu. Entregou. Pronto.", o cabeçalho, "Qual é diferente?" e a instrução "Em cada fila…", sem nada por cima; a legenda só entra aos 0,02 s, também abaixo da página. O carimbo "PRONTO" fica fora da janela (não é cortado) | Quadros de 0,0 a 1,2 s a cada 0,1 s; quadro 0,0 s em tamanho grande; folha do A2 a 2 qps |
| A3-1 · p. 75 passa sob a legenda (4,25–4,6 s) | `montador.py` (cena do A3 com `entrada: "baixo"` agora com `janela`) | A entrada de baixo roda dentro da `janela`: o labirinto aparece saindo da linha acima da legenda e nunca passa por baixo dela | Quadros de 4,20 a 4,80 s a cada 1/15 s (10 quadros); folha do A3 a 2 qps |
| A4-1 · "com quadro" × "com o quadro" (16,9–18,5 s) | `montador.py` (narração e legenda), `criativos/roteiros.md` | **Legenda passou a "com o quadro de conquistas."** (5 palavras, 1 linha, entra aos 17,05 s). O roteiro também. Áudio sem mudança. Decisão e evidência abaixo | Quadro 17,5 s em tamanho grande; folha do A4 a 2 qps; tempos em `montador/tmp/anuncio-4-amandinha.json` |
| A4-2 · título com "·" pendurado e sem margem (11,8–14,6 s) | `montador.py` (título da cena `folheando` do A4 e CSS do `#titulo`) | Título em 2 linhas fixas, sem "·": "Sem saber ensinar" / "nem montar rotina" (como a fala). O `#titulo` aceita quebra explícita (`white-space: pre-line`); nenhum outro título tem quebra, então nada mais muda. A caixa vai de x ≈ 274 a 806 px: margem lateral de ~274 px (os outros ficam a ≥ 150 px) | Quadro 12,5 s em tamanho grande; folha do A4 (12,0–14,5 s) |
| C-1 · margem do roteiro ≠ skill | `criativos/roteiros.md` (Regras de produção, "Texto na tela") | Regra única, a da skill `revisar-criativos`: título abaixo de 200 px do topo e legenda acima de 250 px da base | Medido por pixel em **todos** os quadros a 2 qps dos 4 vídeos (44 + 43 + 46 + 45): o conteúdo mais alto começa em y 236 nos 4 e o mais baixo termina em y 1583 nos 4 (336 px acima da base). Os 4 cumprem |
| R-1 · roteiro desatualizado | `criativos/roteiros.md` | Tabelas de cena refeitas pelo vídeo montado, com os tempos reais das frases (`montador/tmp/anuncio-N-amandinha.json`): **A1** com uma linha por corte, incluindo o labirinto N2 (p. 75) aos 3,4 s; **A2** sem a seta entre preços, com os títulos "Uma vez só" (10,9–14,0 s) e "Faça a conta" (14,0–17,3 s) e a página subindo dentro da janela; **A3** com a p. 6 e a p. 78 lado a lado (sem `amostra-nivel1/2.jpg`) e as duas telas de tipografia separadas; **A4** com o título novo, a fala "com o quadro" e sem o "som de clique" (os vídeos não têm efeito sonoro). Resumo: vídeos de 22,1 / 21,6 / 22,9 / 22,5 s e fala gravada de 21,1 / 20,6 / 21,9 / 21,5 s. Saíram as pendências resolvidas (caminho do `folheando.mp4`, título do criativo 4) e as amostras que não aparecem em nenhum criativo; ficou só "definir UTMs" | Roteiro relido inteiro contra as folhas de contato dos 4 vídeos e o `videos/LEIA.md` |

### Decisão do item A4-1: "com **o** quadro"

Trecho ouvido: 16,5–18,0 s (e recortes de 16,3–18,3 s e 15,5–18,5 s), no `audio/amandinha-4.mp3` e no áudio do próprio `.mp4`.

- **Leituras do faster-whisper com tempo por palavra (beam 5 e beam 1, sem contexto anterior):**
  - large-v3: 12 de 12 leituras ouvem "com **o** quadro" (probabilidade do "o" entre 0,73 e 0,96).
  - medium: 12 de 12 ouvem o "o" (0,72 a 0,86).
  - Total: **24 de 24** em recorte. Na rodada 2, só o small e o large-v3 no arquivo inteiro não ouviram.
- **Análise do sinal** (energia e periodicidade a cada 5 ms e espectrograma de 16,7 a 17,4 s; trabalho em
  `/tmp/claude-0/-home-user/2250d25c-d581-568f-b4e4-6cb893f20944/scratchpad/r3/espectro*.png`):
  - "pronto" termina em ~16,92 s;
  - estouro do /k/ de "com" em ~17,00 s;
  - vogal nasal forte de 17,04 a 17,13 s (~90 ms, cerca de −20 dB);
  - **segmento sonoro fraco de ~60 ms (17,14–17,20 s, cerca de −40 dB)**;
  - fechamento e estouro do /k/ de "quadro" em 17,21–17,25 s.
  - Para comparar, o "com" de "com labirinto" (9,04–9,20 s, mesmo áudio) tem ~160 ms de vogal forte contínua. Aqui o
    trecho sonoro entre os dois /k/ também tem ~160 ms, mas em duas partes, e a segunda é fraca.
- **Leitura da análise:**
  - Não aparece uma vogal "o" plena e separada (60–120 ms com a força de uma vogal).
  - O segmento de ~60 ms entre a vogal nasal e o /k/ é compatível com o "o" átono fundido ao "com" ([kõũ], o
    "co'o" do português falado). Também seria compatível com o fim nasal do "com". O sinal sozinho não decide.
- **Decisão:** legenda e roteiro passam a **"com o quadro de conquistas."**
  - Todas as leituras de modelo ouvem o "o", e o sinal tem a duração mínima de um "o" fundido.
  - Quem assiste tende a ouvir "com o", como o whisper. A legenda "com o" não fica errada nem se a voz tiver dito "com"
    fundido, porque o "o" átono fundido é a pronúncia normal de "com o".
  - Mesmo critério do "imprime e entrega" do A2: a legenda segue o áudio, sem regravar.
  - O texto enviado ao ElevenLabs foi "com quadro" (`roteiros.md` antigo).
  - Se o dono ouvir 17,0–17,3 s e preferir "com quadro", basta voltar o texto no `montador.py` e remontar só o A4.

### Arquivos regenerados (rodada 2)

| Arquivo | sha256 |
|---|---|
| `criativos/videos/anuncio-2-amandinha.mp4` (21,63 s) | `f03be16d7f65185030708dfb6ff91d27c7aef87bf259609059d2b789ea0b97c5` |
| `criativos/videos/anuncio-3-amandinha.mp4` (22,90 s) | `b5c8282993621f23f64b54c3c1cc4e746ee33a3b2778268123e400f94f77eadc` |
| `criativos/videos/anuncio-4-amandinha.mp4` (22,50 s) | `f15b9f2958411505293ba440a2f0c2cbbeb71dacb94886f82a31ff3540e9c950` |
| `criativos/videos/quadro-anuncio-2.jpg` (3,2 s, `-q:v 3`) | `6d92d52b5043…` |
| `criativos/videos/quadro-anuncio-4.jpg` (11,1 s, `-q:v 3`) | `2be7a930fbfb…` |

- `qc.py` rodou nos 3 vídeos: 1080×1920, 30 fps, h264 + aac, pico −1,5 dB, durações iguais às de antes.
- Sem mudança:
  - `anuncio-1-amandinha.mp4` (`998a9b40…`) e `quadro-anuncio-1.jpg`;
  - `quadro-anuncio-3.jpg`: o quadro de 1,4 s do vídeo novo é idêntico pixel a pixel ao anterior;
  - as 2 imagens estáticas.
- Os quadros 2 e 4 mostram a mesma cena de antes. Foram refeitos porque o .mp4 mudou.

### Como foi olhado (rodada 2)

- **Folhas de contato a 2 qps** dos vídeos 2, 3 e 4 inteiros (44 + 47 + 46 quadros), depois da montagem final.
- **Entradas em alta frequência:**
  - A2 de 0,0 a 1,2 s (13 quadros, a cada 0,1 s);
  - A3 de 4,20 a 4,80 s (10 quadros, a cada 1/15 s).
- **Quadros grandes (1080×1920):** A2 0,0 s (miniatura), A4 12,5 s (título novo) e A4 17,5 s (legenda "com o quadro de conquistas.").
- **Os 2 quadros de referência novos.**
- **Medição por pixel da área segura** em todos os quadros a 2 qps dos 4 vídeos (item C-1).

**Fica para a rodada 3:**
- revisar os vídeos 2, 3 e 4 e o `roteiros.md`;
- o A1 e o A5 não mudaram (pela R12, da 4ª rodada em diante só o que mudou).
