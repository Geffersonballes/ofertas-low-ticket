# Criativos · rodada 2 (revisão completa dos 5) · Dez Minutinhos

- Data: 2026-11-28 · Revisor: subagente (técnica, verdade do produto, conformidade e texto) · Nenhum arquivo editado além deste.
- Base: rodada 1 (`conformidade-e-textos.md`, `tecnica-e-verdade.md`) e `correcoes.md`.

## Veredito: **NÃO LIMPA**: 6 pendências, todas cosméticas

| Gravidade | Quantidade |
|---|---|
| Bloqueia | 0 |
| Atrapalha | 0 |
| Cosmético | 6 (A2: 1 · A3: 1 · A4: 2 · comum aos 4 vídeos: 1 · roteiro: 1) |

- **Os 19 itens da rodada 1 estão corrigidos** (3 atrapalha e 16 cosméticos). A tabela abaixo dá a evidência de cada um.
- **Verdade do produto: 0 problemas.** **Conformidade: 0 problemas** (sem veto).
- Esta é a 2ª rodada. Pela R12, os cosméticos novos têm de ser corrigidos (ou aceitos pelo dono por escrito) e depois vem a rodada 3.
- **Quadros olhados: 194 quadros de vídeo.**
  - 178 a 2 por segundo: todos os quadros dos 4 vídeos (44 + 43 + 46 + 45), vistos em folhas de contato com o tempo de cada um.
  - 10 em tamanho grande: A1 14,5 e 20,0 s · A2 0,0, 3,5 e 15,0 s · A3 4,0 e 13,0 s · A4 5,0, 12,0 e 16,0 s.
  - 6 a 10 por segundo no corte do A3 entre 3,9 e 4,4 s.
- Também olhados: as 2 imagens estáticas inteiras e 15 páginas do PDF aprovado (renderizadas).
- Quadros e folhas: `/tmp/claude-0/-home-user/2250d25c-d581-568f-b4e4-6cb893f20944/scratchpad/cr2/`.

### Arquivos revisados (sha256, iguais ao `correcoes.md`)
```
998a9b4013d6d7d2289ce8da5006ae9e76e60b5931e83054f60107f76edc73bc  criativos/videos/anuncio-1-amandinha.mp4
6c27ae7832b811d2203d96f19afea128d00c6cdf325e6f5bb0dce159b4d95cfb  criativos/videos/anuncio-2-amandinha.mp4
bcf87fbc8aba2cda74f7857a59631df95e79a36eb2fca4a09b2e398947992346  criativos/videos/anuncio-3-amandinha.mp4
b84f051e6533638bc5d9e794f4b1c395911598b0fcd41dc4c4014c462fc027fd  criativos/videos/anuncio-4-amandinha.mp4
cf0e3dcbf01df084a59cb5628e0d87030390e6adce63a9ef904c02665dd43555  criativos/estatico/anuncio-5-ferias-1x1.jpg
73e0b0ee36dfa0166090c0fb87dea23e02873a56ec6ffdbb91ec4595fcdbfa88  criativos/estatico/anuncio-5-ferias-4x5.jpg
```
Pré-requisito: `conferir_material.py` → "MATERIAL APROVADO" (8 PDFs conferem). `conferir_criativos.py` → "CRIATIVOS NÃO APROVADOS" (ainda falta o `APROVACAO.md`, como esperado).

---

## Itens da rodada 1

| # | Item (origem · gravidade) | Corrigido? | Evidência |
|---|---|---|---|
| 1 | A1, texto principal: "4 atividades em 10 min" (conformidade · atrapalha) | sim | `roteiros.md`: "Um labirinto e um jogo de memória. É isso que cabe em uns 10 minutinhos de papel e lápis. No outro dia, outras duas folhas: …". A página diz "Duas folhas por dia, uns 10 minutinhos" |
| 2 | A2, descrição "R$ 1,23 por dia" sozinha (conformidade · atrapalha) | sim | Descrição: "R$ 37,00, uma vez só. Sem mensalidade." (a página tem "uma vez só" e "Sem mensalidade") |
| 3 | A4 sem "uma vez só" (conformidade · atrapalha) | sim | Última linha: "120 atividades · 4 a 10 anos · R$ 37,00, uma vez só · garantia de 7 dias." |
| 4 | A1, descrição "O PDF chega no seu e-mail" (conformidade · cosmético) | sim | "Acesso pelo e-mail após o pagamento" (frase literal da página) |
| 5 | Cartão final: roteiro × vídeo (conformidade · cosmético) | sim | "Garantia de 7 dias" está abaixo do preço no fecho dos 4: A1 a partir de 17,0 s, A2 de 19,5 s, A3 de 17,0 s e A4 de 19,0 s. O roteiro ("Cartão final (igual nos 4 vídeos)") e o `LEIA.md` descrevem o mesmo |
| 6 | A2, "sem separar por idade" (conformidade · cosmético) | sim | "…as folhas já vêm separadas em 2 níveis de idade. Cada dia do plano de 30 dias já tem as duas folhas escolhidas…" |
| 7 | A5 fora da temporada (conformidade · cosmético) | sim | `campanha.md` l. 55: "Janela do A5 (férias): rodar só de 2026-12-15 a 2027-02-28". Igual no roteiro ("Quando rodar") |
| 8 | A5: roteiro do leque diferente da peça (conformidade · cosmético) | sim | Roteiro: p. 7, p. 68 e p. 78. A peça 4:5 mostra exatamente o labirinto N1, o jogo dos 7 erros N2 e o código secreto N2 |
| 9 | A5, "Arquivo final" com o link 1:1 que não existia (conformidade · cosmético) | sim | Os 2 arquivos existem (1080×1080 e 1080×1350, sRGB) e estão listados no roteiro |
| 10 | A1, legenda ~0,3 s atrasada entre 8,5 e 11,7 s (técnica · cosmético) | sim | O bloco "de 4 a 10 anos." entra aos 11,33 s. A palavra "de" é falada aos 11,34 s (whisper small, no vídeo) e aos 11,38 s (medium). O quadro de 11,5 s já mostra o bloco novo |
| 11 | A1, legenda sobre o plano entre 13,1 e 16,7 s (técnica · cosmético) | sim | No quadro grande de 14,5 s, a página termina com fade em ~y 1404 e a legenda começa em ~y 1424. Nada da página fica por baixo |
| 12 | C3, duas pílulas escuras no fecho dos 4 (técnica · cosmético) | sim | No quadro grande de 20,0 s do A1, o botão escuro fica em ~y 1196–1300 e a legenda clara (fundo branco) em ~y 1500–1583. É igual nas folhas de contato dos 4 |
| 13 | A2, "imprime e entrega" (técnica · cosmético) | sim | Legenda: "Abre, imprime e entrega com um lápis." de 6,17 a 8,97 s. No recorte de 6,0 a 8,9 s, o medium e o large-v3 ouvem o "e" (probabilidade 0,80 e 0,83). O large-v3 no arquivo inteiro não ouve o "e", mas no recorte ouve. Mantido |
| 14 | A2, "dias" sozinho e quebra "no / plano" (técnica · cosmético) | sim | De 15,5 a 17,0 s o texto grande é "por dia no plano" / "de 30 dias". A legenda vem em 2 blocos: "R$ 1,23 por dia," e "no plano de 30 dias." |
| 15 | A3, "de 4 a / 6 anos" partido (técnica · cosmético) | sim | De 11,5 a 13,5 s: "2 níveis: de 4 a 6 anos," em 1 linha. Depois "sem precisar ler," e "e de 7 a 10." |
| 16 | A4, título "Memória" sobre o cabeçalho do cartão aos 4,9 s (técnica · cosmético) | sim | No quadro grande de 5,0 s, o título termina acima do cartão e o cabeçalho "Dez Minutinhos · Nível 1" fica inteiro abaixo dele, com margem lateral de ~60 px |
| 17 | A4, legenda sobre o pé das p. 5, 142 e 143 (técnica · cosmético) | sim | No quadro grande de 16,0 s, a p. 142 aparece inteira (rodapé "página 142" visível) acima da legenda. Nas folhas, a p. 5 (14,5–15,5 s) está dentro da janela e a p. 143 (17,0–18,0 s) inteira acima da legenda. Os blocos têm 1 linha |
| 18 | Estático: miniatura do plano ilegível (técnica · cosmético) | sim | No 4:5, a miniatura virou texto de 50 px: "Plano de 30 dias" / "2 folhas por dia", com marcadores |
| 19 | Estático: p. 8 e p. 78 escondidas no leque (técnica · cosmético) | sim | Leque aberto no 4:5: as 3 páginas aparecem com o título ("Labirinto", "Jogo dos 7 erros", "Código secreto"). As p. 7, 68 e 78 do `montador/cache/pdf/` são idênticas byte a byte a um `pdftoppm` novo do PDF aprovado |

---

## Técnica (os 4 vídeos)

| Vídeo | Formato | Duração | Pico (volumedetect / true peak) | Loudness integrada | Tela preta | Silêncios |
|---|---|---|---|---|---|---|
| anuncio-1 | 1080×1920, 30 fps, h264 yuv420p + aac 48 kHz mono | 22,10 s | −1,5 dB / −1,5 dBFS | −16,5 LUFS (LRA 2,8) | nenhuma | 0,30 s aos 16,6 s (pausa) e 1,10 s no fecho |
| anuncio-2 | idem | 21,63 s | −1,5 / −1,5 | −16,7 (2,5) | nenhuma | 1,10 s no fecho |
| anuncio-3 | idem | 22,90 s | −1,5 / −1,5 | −16,2 (2,0) | nenhuma | 0,44 s aos 16,1 s e 1,08 s no fecho |
| anuncio-4 | idem | 22,50 s | −1,5 / −1,5 | −16,7 (1,7) | nenhuma | 0,32 s aos 8,0 s e 0,99 s no fecho |

- **Fala × legenda × roteiro.**
  - Transcrição feita com faster-whisper sobre o áudio do próprio .mp4: small e large-v3 nos 4 vídeos inteiros, com tempo por palavra.
  - Os trechos com dúvida foram transcritos de novo com medium e large-v3, em recorte, com a probabilidade de cada palavra.
  - Resultado: o texto bate nos 4, salvo o item A4-1 abaixo. Números falados por extenso e escritos em algarismo na legenda: conforme.
- **Sincronia.**
  - Todos os 47 blocos entram entre 0,05 s antes e ~0,2 s depois da 1ª palavra.
  - A diferença entre os modelos de whisper é da mesma ordem (±0,2 s), então não há atraso perceptível.
- **Área segura.**
  - O título começa em y = 236 px nos 4 (o cartão final em 280–298 px).
  - A legenda vai de ~1424 px até, no máximo, 1511 px nas cenas e 1583 px no fecho. O ponto mais baixo fica 337 px acima da base.
  - Cumpre a skill (200 px no topo e 250 px na base). Ver o item comum C-1 sobre a margem do roteiro.
- **Nada cortado:** nenhum texto sai do quadro. As páginas que passam do quadro são zooms dentro da janela com fade, de propósito.
- **Legenda × conteúdo:** fora das entradas animadas (A2-1, A3-1), a legenda não tampa nenhuma página.
- **Fecho dos 4.** Cartão com:
  - capa;
  - "Dez Minutinhos";
  - "120 atividades para imprimir · 4 a 10 anos";
  - "R$ 37,00";
  - "Garantia de 7 dias";
  - botão escuro "Toque em Saiba mais", separado da legenda clara.

## Verdade do produto

- **PDF aprovado.** O sha256 `66cf687c6ab2…3eb01351` é igual à linha 9 do `revisoes/material-2026-11-28/APROVACAO.md` (149 páginas).
- **Páginas conferidas.** As 15 páginas que aparecem foram renderizadas do PDF e comparadas com os quadros: p. 5, 6, 7, 8, 11, 13, 15, 18, 68, 69, 75, 78, 128, 142 e 143. Todas conferem, tanto o conteúdo quanto o nível do selo.
  - O caminho do gabarito (p. 7 e p. 75), a memória (quadrado, lua e coração) e o sudoku de figuras (p. 18) batem com o PDF.
  - O sudoku 6×6 (p. 69) bate com o PDF.
  - O código secreto (BRINCAR / FAZ / BEM) bate com o PDF.
  - O ligue os pontos (p. 15, de 1 a 12) bate com o PDF.
  - O gabarito da p. 128 (com o coração colorido) bate com o PDF.
  - O quadro de 30 dias (p. 142) e os certificados das Semanas 1 e 2 (p. 143) batem com o PDF.
- **Cache do montador.** As páginas do cache são das 02:40 e o PDF é das 03:45. A rodada 3 do material só mudou as p. 20, 38, 129 e 131, e nenhuma delas aparece nos criativos (já registrado na rodada 1). As p. 7, 68 e 78 do estático são idênticas a uma renderização nova.
- **Números e textos na tela.** Todos estão no PDF e/ou na `pagina/index.html`:
  - 120 atividades; 2 níveis, 4 a 6 e 7 a 10 anos; "sem leitura"; plano de 30 dias; 2 folhas por dia; "Gabarito completo";
  - quadro de conquistas;
  - R$ 37,00 e "uma vez só";
  - R$ 1,23 por dia no plano de 30 dias;
  - Garantia de 7 dias;
  - "Imprime de novo quando quiser" (a página diz "imprime de novo para repetir o plano ou para o irmão").
- **"30 dias de atividades prontas para imprimir"** (4:5 e título do A5) não está literalmente na página, mas é verdadeiro: 30 dias × 2 folhas = 60 atividades por nível. Não é achado.

## Conformidade e texto dos anúncios (CLAUDE.md, regras 1 a 5)

- **Os 5 anúncios têm todos os campos:** Texto principal, Título, Descrição e CTA "Saiba mais". A URL https://ofertas.ballestech.com.br/dez-minutinhos/ está nas regras do `roteiros.md` e no `campanha.md`.
- **Nada na lista de vetos:** atributo pessoal, promessa de resultado, saúde, antes/depois, urgência, "de/por", prova social, depoimento ou palavra vetada. O vídeo não põe seta entre R$ 37,00 e R$ 1,23.
- **Preço e garantia.** R$ 37,00 com "uma vez só" e garantia de 7 dias aparecem nos 5 textos principais e nos 4 fechos.
- **Coerência com a página.** O que cada texto diz bate com a página:
  - 2 níveis, plano, gabarito, PDF A4 em preto e branco;
  - 3 bônus, 30 ideias "sem imprimir nada", quadro de conquistas e certificados;
  - "Imprime na segunda / gaveta", "para o irmão";
  - "Pediu o tablet? Entregue um labirinto." (o h1 da página).
- **Português:** correto nos 5.
- **Declaração de IA:** continua "não marcar" (sem pessoa nem evento realista).

---

## Achados por criativo

### Anúncio 1 · `anuncio-1-amandinha.mp4`
| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| — | — | Nenhum achado próprio (ver o item comum C-1) | — |

### Anúncio 2 · `anuncio-2-amandinha.mp4`
| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 0,0–0,9 s (A2-1) | cosmético | A legenda "Imprimiu, entregou, pronto." fica por cima da p. 6 enquanto a página sobe. No quadro 0,0 s, que é o 1º quadro e a miniatura do vídeo, a legenda tampa a instrução "Em cada fila…" logo abaixo do título "Qual é diferente?" | Começar a subida da página acima de y 1410 ou dentro da `janela`. Outra saída é segurar a legenda até a página parar (~1,0 s), mas aí a legenda fica atrasada. A 1ª opção é melhor |

### Anúncio 3 · `anuncio-3-amandinha.mp4`
| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 4,25–4,6 s (A3-1) | cosmético | A p. 75 entra por baixo e passa sob a legenda "Quer o mesmo tipo de desafio,", que fica por cima do labirinto por ~0,3 s | A mesma correção do A2-1: a entrada da página dentro da `janela` (acima de y 1410) |

### Anúncio 4 · `anuncio-4-amandinha.mp4`
| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 16,9–18,5 s (A4-1) | cosmético | A legenda e o roteiro dizem "com quadro de conquistas.", mas a voz parece dizer "com **o** quadro de conquistas". Ouvem o "o": medium no arquivo inteiro (cache `palavras/amandinha-4.json`), medium em recorte (0,76 e 0,87) e large-v3 em recorte (0,66 e 0,75). Não ouvem: small e large-v3 no arquivo inteiro. É o mesmo critério usado no "imprime e entrega" do A2. A rodada 1 não pegou | Ouvir de 16,8 a 17,5 s. Se a voz diz "o", trocar a legenda e o roteiro para "com o quadro de conquistas." (sem regravar). Se não diz, registrar "conferido de ouvido" no `correcoes.md` |
| 11,8–14,6 s (A4-2) | cosmético | O título quebra em "Sem saber ensinar ·" / "sem montar rotina", com o separador "·" pendurado no fim da 1ª linha. É também o único título que quase encosta nas bordas: a caixa vai de x 48 a 1039 (~41 px de margem), e os outros ficam a ≥150 px | Trocar por "Sem saber ensinar" / "nem montar rotina" (2 linhas sem "·", como a fala) ou diminuir a fonte para caber em 1 linha com ≥100 px de margem |

### Anúncio 5 · `anuncio-5-ferias-4x5.jpg` e `anuncio-5-ferias-1x1.jpg`
| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| — | — | Nenhum achado | — |

O que foi conferido no anúncio 5:
- **4:5:** título de ~92 px, leque com os 3 títulos legíveis, plano em texto de 50 px, rodapé "4 a 10 anos · 2 níveis · R$ 37,00". Pouco texto e nenhum selo, estrela, número de clientes ou pessoa.
- **1:1:** título, capa, p. 7 e p. 78 com título visível, rodapé "Plano de 30 dias · 4 a 10 anos · R$ 37,00".

### Comum aos 4 vídeos e ao roteiro
| Momento | Gravidade | Problema | Sugestão |
|---|---|---|---|
| Os 4 vídeos, título e fecho (C-1) | cosmético | A margem do `roteiros.md` ("250 px em cima e 340 px embaixo") não é cumprida, e é diferente da skill (200 px em cima e 250 px embaixo, que os vídeos cumprem). O título fica em y 236 (14 px dentro dos 250 px). A legenda do fecho vai até y 1583, ou seja, 337 px da base (3 px dentro dos 340 px) | Escolher uma regra só. A mais simples é corrigir o roteiro para a margem da skill (200/250 px). A outra é descer o título 14 px e subir a legenda do fecho 3 px |
| `criativos/roteiros.md` (R-1) | cosmético | O roteiro está desatualizado em relação aos vídeos montados (lista abaixo) | Atualizar as tabelas de cena, as durações e as pendências pelo que foi montado (o `videos/LEIA.md` já está certo) |

Onde o roteiro (R-1) não bate com os vídeos:
1. **Tabelas de cena:**
   - A1: falta o labirinto N2 (p. 75) aos 3,4 s.
   - A2: a tela ainda mostra "120 atividades · R$ 37,00 → R$ 1,23", com seta entre preços, que a conformidade mandou evitar. Os títulos montados, "Uma vez só" e "Faça a conta", não aparecem.
   - A3: diz "Tela dividida: `amostra-nivel1.jpg` / `amostra-nivel2.jpg`", mas o vídeo mostra a p. 6 e a p. 78.
2. **Coluna "Vídeo" do resumo:** 25 s, 25 s, 23 s e 22 s. Os vídeos têm 22,1 s, 21,6 s, 22,9 s e 22,5 s.
3. **Pendências já resolvidas que continuam no roteiro:**
   - em "Imagens": "(caminho a confirmar; supus `pagina/img/folheando.mp4`)";
   - em "Pendências": "confirmar o caminho de `folheando.mp4`" e "o título do criativo 4 depende da escolha final do título da página".

## Para a rodada 3
Corrigir os 6 cosméticos. A2-1, A3-1 e A4-2 são no `montador.py`, A4-1 depende de ouvir o trecho, C-1 e R-1 são no `roteiros.md`. Depois, revisar de novo os criativos que mudarem: pelo que está aqui, os vídeos 2, 3 e 4 e o texto do roteiro. O A1 e o A5 só mudam se a C-1 for resolvida mexendo no vídeo.
