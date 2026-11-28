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
