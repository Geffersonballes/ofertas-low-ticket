# Criativos · rodada 3 (vídeos 2, 3 e 4 e `roteiros.md`) · Dez Minutinhos

- Data: 2026-11-28 · Revisor: subagente (técnica, verdade do produto e texto) · Nenhum arquivo editado além deste.
- Base: `rodada2.md` (6 pendências) e `correcoes.md` (seção "## Rodada 2").

## Veredito: **NÃO LIMPA**: só 2 cosméticos novos, os 2 candidatos à versão 1.1

| Gravidade | Quantidade |
|---|---|
| Bloqueia | 0 |
| Atrapalha | 0 |
| Cosmético | 2 novos (A4: 1 · `roteiros.md`: 1). Nenhum vem da rodada 2 |

- **As 6 pendências da rodada 2 estão resolvidas** (A2-1, A3-1, A4-1, A4-2, C-1 e R-1). A evidência está na tabela abaixo.
- **Verdade do produto: 0 problemas.** **Textos dos 5 anúncios: completos e corretos.**
- **Pela regra de fechamento (R12),** só da 4ª rodada em diante o cosmético novo vai sozinho para a 1.1. Esta é a 3ª rodada, e ela
  só fica limpa com 0 cosmético. Por isso os 2 cosméticos ficam abaixo, em "Candidatos à versão 1.1". O dono tem dois caminhos:
  - aceitar os 2 por escrito (ou mandar para a 1.1), e aí esta rodada fecha;
  - mandar corrigir os 2, e aí vem a rodada 4, revisando só o que mudar.
  Os 2 são de 1 minuto: uma linha de CSS ou texto no `montador.py` e um número no roteiro.
- **Quadros olhados: 166 quadros de vídeo.**
  - 134 a 2 por segundo: os 3 vídeos inteiros (A2 43 · A3 46 · A4 45), vistos em folhas de contato com o tempo de cada quadro.
  - 30 em tamanho grande, nos trechos corrigidos:
    - A2 0,0 · 0,1 · 0,2 · 0,3 · 0,5 · 0,7 · 0,9 · 1,0 s (o de 0,0 s em 1080×1920);
    - A3 de 4,2 a 4,8 s, a cada 0,1 s;
    - A4 11,8 · 11,9 · 12,5 · 13,5 · 14,0 · 14,5 · 14,6 s;
    - A4 16,8 · 17,0 · 17,1 · 17,3 · 17,5 · 18,0 · 18,4 · 18,5 s.
  - 2 quadros de referência: `quadro-anuncio-2.jpg` e `quadro-anuncio-4.jpg`.
  - Também medidos por pixel: todos os quadros a 2 qps dos 4 vídeos (área segura e margem dos títulos).
  - Também olhadas: 6 páginas do PDF aprovado (p. 5, 6, 75, 128, 142 e 143), renderizadas.
- Quadros e folhas: `/tmp/claude-0/-home-user/2250d25c-d581-568f-b4e4-6cb893f20944/scratchpad/cr3/`.

### Arquivos (sha256)
```
998a9b4013d6d7d2289ce8da5006ae9e76e60b5931e83054f60107f76edc73bc  criativos/videos/anuncio-1-amandinha.mp4   (= rodada 1/2: não mudou)
f03be16d7f65185030708dfb6ff91d27c7aef87bf259609059d2b789ea0b97c5  criativos/videos/anuncio-2-amandinha.mp4   (= correcoes.md, rodada 2)
b5c8282993621f23f64b54c3c1cc4e746ee33a3b2778268123e400f94f77eadc  criativos/videos/anuncio-3-amandinha.mp4   (= correcoes.md, rodada 2)
f15b9f2958411505293ba440a2f0c2cbbeb71dacb94886f82a31ff3540e9c950  criativos/videos/anuncio-4-amandinha.mp4   (= correcoes.md, rodada 2)
6d92d52b50431447f257367f255a19763e8a60dc13c0aedb73dd5d8dfb5e4ab6  criativos/videos/quadro-anuncio-2.jpg      (começa com 6d92d52b5043, como no correcoes.md)
2be7a930fbfb265878deda8c6762cd4ee467141298d092d628d0bddf7955e21e  criativos/videos/quadro-anuncio-4.jpg      (começa com 2be7a930fbfb, como no correcoes.md)
cf0e3dcbf01df084a59cb5628e0d87030390e6adce63a9ef904c02665dd43555  criativos/estatico/anuncio-5-ferias-1x1.jpg (= rodada 2: não mudou)
73e0b0ee36dfa0166090c0fb87dea23e02873a56ec6ffdbb91ec4595fcdbfa88  criativos/estatico/anuncio-5-ferias-4x5.jpg (= rodada 2: não mudou)
bd84f3c5f66d01f9fe03ceba006d69d97c0b68e683514a5f0bbb82d6834d557c  criativos/roteiros.md
```
- **O A1 e as 2 imagens estáticas são os mesmos da rodada 2,** conferidos byte a byte pelo sha256. Por isso não foram revistos.
- **Pré-requisitos:**
  - `conferir_material.py` → "MATERIAL APROVADO" (8 PDFs).
  - O PDF `66cf687c…3eb01351` é igual à linha 9 do `material-2026-11-28/APROVACAO.md`.
  - `conferir_criativos.py` → "CRIATIVOS NÃO APROVADOS", porque ainda falta o `APROVACAO.md`, como esperado.

---

## Pendências da rodada 2

| # | Pendência | Resolvida? | Evidência |
|---|---|---|---|
| A2-1 | A legenda ficava sobre a p. 6 enquanto ela subia (0,0–0,9 s), inclusive na miniatura | sim | **No quadro de 0,0 s (1080×1920):** aparecem o título, o cabeçalho "Dez Minutinhos · Atenção · Nível 1", "Qual é diferente?" e a instrução "Em cada fila…" inteira, sem legenda (ela entra aos 0,02 s). **Medido por pixel de 0,0 a 1,0 s (8 quadros):** a página termina em y ≤ 1413 (fade) e a legenda começa em y 1424. Nada da página passa sob a legenda. O carimbo "PRONTO" fica inteiro (folha de 2,0 a 3,0 s) |
| A3-1 | A p. 75 passava sob a legenda (4,25–4,6 s) | sim | **De 4,2 a 4,8 s, a cada 0,1 s:** a página sobe dentro da janela. O fundo dela termina em y ≤ 1413, com fade, e a legenda "Quer o mesmo tipo de desafio," começa em y 1424. Aos 4,3 s, o labirinto já aparece saindo da linha acima da legenda |
| A4-1 | Legenda "com quadro" × voz "com o quadro" (16,9–18,5 s) | sim | **A legenda agora é "com o quadro de conquistas."** (1 linha, entra aos 17,05 s; vista nos quadros grandes de 17,1 a 18,5 s). O roteiro diz o mesmo, com a nota. **Nesta rodada, no próprio .mp4:** medium no arquivo inteiro ouve "com o quadro". large-v3 no recorte de 14,5 a 18,6 s, com beam 5 e com beam 1, ouve "com" aos 16,88 s, "o" aos 17,04 s (probabilidade 0,55) e "quadro" aos 17,10 s. Só o small no arquivo inteiro não ouve o "o", como na rodada 2. A decisão do `correcoes.md` se sustenta |
| A4-2 | Título "Sem saber ensinar ·" com o "·" pendurado e quase na borda (11,8–14,6 s) | sim | **Nos quadros de 11,8 a 14,6 s:** o título tem 2 linhas, "Sem saber ensinar" / "nem montar rotina", sem "·". **Medido:** a caixa vai de x 274 a 813 e de y 236 a 389, com margem lateral de 266 a 274 px. As 2 linhas cabem com folga, nada cortado. Ver o candidato 1.1-1 sobre outro título do A4 |
| C-1 | A margem do roteiro era diferente da regra da skill | sim | `roteiros.md`, "Texto na tela": "título abaixo de 200 px do topo e legenda acima de 250 px da base (a mesma regra da skill)". **Medido em todos os quadros a 2 qps dos 4 vídeos:** o conteúdo mais alto começa em y 236 e o mais baixo termina em y 1583 (336 px acima da base). Bate com o número escrito no roteiro |
| R-1 | Roteiro desatualizado | sim | As tabelas de cena do A2, A3 e A4 batem quadro a quadro com as folhas de contato (cenas, títulos e tempos com diferença de até 0,2 s). **A2:** sem seta entre os preços; "Uma vez só" de 10,9 a 14,0 s e "Faça a conta" de 14,0 a 17,3 s. **A3:** a p. 6 e a p. 78 lado a lado, com os rótulos. **A1:** inclui o labirinto N2 (p. 75) aos 3,4 s. Resumo com as durações certas (22,1 / 21,6 / 22,9 / 22,5 s). Saíram as pendências velhas, e ficou só "definir UTMs". Ver o candidato 1.1-2 (contagem de palavras do A2) |

---

## Técnica (vídeos 2, 3 e 4)

| Vídeo | Formato | Duração | Pico (volumedetect / true peak) | Loudness integrada | Tela preta | Silêncios (< −40 dB, ≥ 0,25 s) |
|---|---|---|---|---|---|---|
| anuncio-2 | 1080×1920, 30 fps, h264 yuv420p + aac 48 kHz mono | 21,63 s | −1,5 dB / −1,5 dBFS | −16,7 LUFS (LRA 2,5) | nenhuma | 1,10 s no fecho |
| anuncio-3 | idem | 22,90 s | −1,5 / −1,5 | −16,2 (2,0) | nenhuma | 0,44 s aos 16,1 s, 0,30 s aos 20,1 s (pausas) e 1,08 s no fecho |
| anuncio-4 | idem | 22,50 s | −1,5 / −1,5 | −16,7 (1,7) | nenhuma | 0,32 s aos 8,0 s, 0,27 s aos 18,5 s (pausas) e 0,99 s no fecho |

As durações, o loudness e o pico são iguais aos da rodada 2: o áudio não mudou.

- **Fala × legenda × roteiro.**
  - Transcrição com faster-whisper (small e medium) sobre o áudio do próprio .mp4, com tempo por palavra. O large-v3 foi usado no recorte do A4.
  - O texto das 37 legendas (A2 11, A3 12, A4 14) bate palavra por palavra com a fala e com a narração do `roteiros.md`. Os números falados por extenso estão em algarismo na legenda, como manda a regra.
  - Diferenças só de modelo, não do vídeo:
    - o small ouve "R $120" no lugar de "cento e vinte atividades" (o medium ouve certo);
    - "Ape"/"Labyrintho"/"sudoco" no lugar de "App"/"labirinto"/"sudoku";
    - "10 minutinhos" no lugar de "Dez Minutinhos".
  - Os "e" do A2 ("imprime e entrega") e o "o" do A4 ("com o quadro") estão conferidos.
- **Sincronia.** Cada bloco foi comparado com a 1ª palavra (whisper) e com o início da energia da voz.
  - Os 37 blocos entram entre 0,0 e 0,32 s **antes** da voz, sempre na pausa, e nenhum entra depois.
  - O mais adiantado é "120 atividades por R$ 37,00." do A2 (entra aos 10,94 s e a voz começa ~0,3 s depois, na pausa).
  - Não há atraso perceptível.
- **Área segura.**
  - O título começa em y 236 nos 3 vídeos; o cartão final, entre y 271 e 311.
  - A legenda termina, no máximo, em y 1511 nas cenas e em y 1583 no fecho, ou seja, 336 px acima da base.
  - Cumpre os 200 px do topo e os 250 px da base.
- **Nada cortado.**
  - Nenhum texto sai do quadro.
  - As páginas que somem embaixo são fades dentro da janela, de propósito.
  - O carimbo "PRONTO" e as 2 linhas do título novo do A4 ficam inteiros.
- **Legenda × conteúdo:** em nenhum dos 134 quadros, nem nos 30 grandes, a legenda fica por cima de uma página.
- **Fecho dos 3 vídeos.** Cartão com:
  - capa;
  - "Dez Minutinhos";
  - "120 atividades para imprimir · 4 a 10 anos";
  - "R$ 37,00";
  - **"Garantia de 7 dias"**: no A2 a partir de 19,5 s, no A3 de 17,0 s e no A4 de 19,0 s, até o último quadro;
  - botão escuro "Toque em Saiba mais";
  - legenda clara bem abaixo do botão.
- **Quadros de referência:**
  - `quadro-anuncio-2.jpg` (1080×1920) mostra "Imprimiu. Entregou. Pronto." com o carimbo, a p. 6 inteira e a legenda "Zero preparo.".
  - `quadro-anuncio-4.jpg` mostra "Traçado" com o ligue os pontos (p. 15) e a legenda "Ligue os pontos.".
  - Os 2 estão legíveis e sem sobreposição.

## Verdade do produto

- **Páginas que aparecem nos 3 vídeos**, iguais às do PDF aprovado:
  - A2: p. 5, 6, 7 e 128, `mockup-pacote`, `mockup-capa` e `folheando`;
  - A3: p. 6, 8, 68, 69, 75 e 78;
  - A4: p. 5, 8, 11, 13, 15, 18, 142 e 143 e `folheando`.
- **Conferência nesta rodada.** As p. 5, 6, 75, 128, 142 e 143 foram renderizadas de novo do PDF aprovado e comparadas com os quadros:
  - selo de nível;
  - título e instrução;
  - desenho do labirinto N2;
  - plano de 30 dias;
  - gabarito com o coração colorido;
  - quadro de 30 estrelas;
  - certificados das Semanas 1 e 2.
  Tudo confere. As outras páginas são as mesmas cenas conferidas na rodada 2, sem mudança de conteúdo: o `montador.py` só mudou a janela, a entrada, o título e a legenda.
- **Números e textos na tela, todos no PDF e/ou na `pagina/index.html`:**
  - 120 atividades;
  - 2 níveis, 4 a 6 e 7 a 10 anos, "sem leitura";
  - plano de 30 dias, 2 folhas por dia;
  - "Gabarito completo";
  - quadro de conquistas e certificados;
  - R$ 37,00 e "uma vez só";
  - R$ 1,23 por dia no plano de 30 dias;
  - Garantia de 7 dias;
  - "Imprime de novo quando quiser" (a página diz "imprime de novo").
- **"Sem saber ensinar / nem montar rotina":** é a fala e o texto do anúncio 4, e não é promessa de resultado.

## Texto dos anúncios (`roteiros.md`)

- **Os 5 anúncios continuam completos:** Texto principal, Título, Descrição, CTA "Saiba mais" e arquivo final.
  - A URL `https://ofertas.ballestech.com.br/dez-minutinhos/` está nas regras de produção.
  - Os textos são os mesmos da rodada 2, já aprovados pela conformidade.
  - R$ 37,00 com "uma vez só" e "Garantia de 7 dias" aparecem nos 5.
- **Coerência com a página:** "Acesso pelo e-mail após o pagamento", "Sem mensalidade", "preto e branco", "caça-palavras" e "Pediu o tablet?" existem na `pagina/index.html`.
- **A4:** o texto principal diz "com quadro de conquistas e certificados". É texto escrito, não legenda, e está correto em português. Não é achado.
- **Contagem de palavras das narrações** (contadas nesta rodada): A1 58, **A2 59** (o roteiro diz 57), A3 53 e A4 53. Ver 1.1-2.

---

## Achados por vídeo

### Anúncio 2 · `anuncio-2-amandinha.mp4`
| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| — | — | Nenhum achado | — |

### Anúncio 3 · `anuncio-3-amandinha.mp4`
| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| — | — | Nenhum achado | — |

### Anúncio 4 · `anuncio-4-amandinha.mp4`
| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 14,6–18,5 s (1.1-1) | cosmético (novo) | O título "Plano pronto · quadro de conquistas" é o mais largo dos vídeos: a caixa vai de x 62 a 1025, com 62 px de margem à esquerda e 54 px à direita, contando a sombra laranja. É o mesmo tipo de achado da A4-2 (lá eram ~41 px). A linha está inteira e o "·" fica no meio, não pendurado. **Não é novo no arquivo:** esta cena era igual na rodada 2, que mediu só o título da A4-2. A frase "os outros ficam a ≥ 150 px" da rodada 2 não vale para este título. Para comparar: o título do A1 de 13–16 s fica a 92–100 px e o do A2 de 17,3–19 s a 106–114 px | Diminuir o título desta cena até ≥ 100 px de margem, ou usar 2 linhas ("Plano pronto" / "quadro de conquistas"), como no A4-2 (`white-space: pre-line` já existe) |

### `criativos/roteiros.md`
| Trecho | Gravidade | Problema | Sugestão |
|---|---|---|---|
| Criativo 2, linha depois da "Narração completa" (1.1-2) | cosmético (novo) | Diz "57 palavras · 20,6 s de fala gravada", mas a narração tem **59** palavras. A tabela-resumo também diz "57 palavras" no A2. As outras 3 contagens batem (58, 53 e 53) | Trocar para "59 palavras" nas 2 linhas |

---

## Candidatos à versão 1.1

Os 2 são cosméticos. Não afetam a verdade do produto, a conformidade nem a leitura no celular.

| # | Arquivo | Problema | Correção |
|---|---|---|---|
| 1.1-1 | `anuncio-4-amandinha.mp4` (14,6–18,5 s) | Título "Plano pronto · quadro de conquistas" a 54–62 px das bordas | Quebrar em 2 linhas ou diminuir a fonte no `montador.py` e remontar só o A4 |
| 1.1-2 | `criativos/roteiros.md` | O A2 diz "57 palavras", mas a narração tem 59 | Corrigir o número (no resumo e embaixo da narração) |

**Para fechar:**
- **O dono aceita os 2 por escrito** (ou manda para `revisoes/melhorias-v1.1.md`): a rodada 3 fica limpa, e o próximo passo é o Portão C.
- **O dono manda corrigir:** a rodada 4 revisa só o A4 (14–19 s e o fecho) e as 2 linhas do roteiro.
