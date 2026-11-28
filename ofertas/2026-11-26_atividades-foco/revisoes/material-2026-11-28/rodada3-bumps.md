# Revisão dos order bumps — rodada 3 (final) — 2026-11-28

Base: `rodada2-bumps-1-a-6.md` e `correcoes.md` ("## Rodada 2"). Arquivos: `produto/bumps/<n>_<slug>/<slug>.pdf`.
Nenhum arquivo do material foi editado.

## Resumo

- **Veredito: NÃO LIMPA (só cosméticos).** Nenhum achado bloqueia ou atrapalha o uso. Os **13 cosméticos da rodada 2
  estão corrigidos**. Sobram **9 cosméticos**: 3 vêm das correções da rodada 2 (bump 3, carta 35; bump 5, págs. 54 e
  61) e 6 já existiam e as rodadas anteriores não tinham apontado. Pela regra do dono ("corrigir todos os
  cosméticos"), a revisão ainda não sai limpa.
- **Páginas olhadas em imagem: 211 de 211** dos bumps que mudaram. Bump 2: 47/47 · Bump 3: 10/10 · Bump 4: 73/73 ·
  Bump 5: 69/69 · Bump 6: 12/12. Renderizei tudo a 55 dpi (`pdftoppm -r 55`) e olhei em folhas de 4 páginas. Ampliei
  a 130–150 dpi estes pontos: bump 2, pág. 35 e gabarito pág. 46 (polvo); bump 5, págs. 13 e 29 (faca e mala). Também
  conferi todo o texto com `pdftotext -layout`.
- **Bump 1:** não olhei de novo. O PDF não mudou desde o commit `03dfcc6`, de antes da rodada 2: o commit das
  correções (`3feb6cb`) não mexeu nele e a árvore está limpa. O `.zip` traz o mesmo PDF (md5 `22684be01f85…`).
- **Conferido por script:**
  - bump 4: 140 contas do gabarito, sem erro. As 120 contas das págs. 36–63 seguem a regra nova (soma com uma
    parcela ≥ 10, diminuir com o primeiro número ≥ 11), com resultados de 1 a 30 e nenhuma conta repetida no bump;
  - bump 4: 8 pirâmides, 4 mercadinhos (20 problemas), 18 "dezenas e unidades" (contadas na imagem) e
    20 comparações;
  - bump 2: as 20 contas e a peça que sobra nas 4 folhas de "Cole o resultado";
  - bump 5: os 4 caça-palavras nas 8 direções, com cada palavra uma vez só;
  - bump 5: os 24 "Desembaralhe", que usam as mesmas letras da palavra, são 24 palavras diferentes e nenhum
    embaralhado forma outra palavra;
  - bump 6: as 6 cartelas de bingo (juntas, cobrem as 16 fichas), as 28 peças do dominó e os 12 pares da memória;
  - os 5 `.zip` têm 1 PDF cada, igual (md5) ao PDF da pasta.
- **Português:** não achei erro de ortografia, acento nem concordância. Li o bump 5 palavra por palavra: instruções,
  30 palavras do "Qual vogal falta?", 30 de "Complete com a sílaba", 32 de "Quantas sílabas?", 24 de "Desembaralhe",
  rimas, 20 frases, ordens alfabéticas e gabaritos.

| Bump | Prometido (`bumps/bumps.md`) | Real | Págs. prometidas × reais | Bloqueia | Atrapalha | Cosmético |
|---|---|---|---|---|---|---|
| 2 Recortar e colar | 40, nos dois níveis | 40 (20 N1 págs. 3–22 + 20 N2 págs. 23–42) + 5 de gabarito | 47 × 47 | 0 | 0 | 0 |
| 3 Cartas de conversa | 48 perguntas, 4 categorias de 12 | 48 (12 Meu dia, 12 Imaginação, 12 E se…?, 12 Preferidos), 6 por folha | 10 × 10 | 0 | 0 | 1 |
| 4 Matemática brincando | 60, nos dois níveis + fichas | 60 (30 N1 págs. 4–33 + 30 N2 págs. 34–63) + fichas (pág. 3) + 10 de gabarito | 73 × 73 | 0 | 0 | 2 |
| 5 Letras e palavras | 60 (N1 vogais/1ª letra; N2 sílabas, palavras, rimas, frases) | 60 (30 N1 págs. 3–32 + 30 N2 págs. 33–62) + 7 de gabarito | 69 × 69 | 0 | 0 | 3 |
| 6 Jogos de mesa | 5 jogos, regras numa página | bingo 6 cartelas + 16 fichas; dominó 28 peças; memória 24 cartas (12 pares); trilha 30 casas + 4 peões + dado; velha 2 tabuleiros + 10 peças; regras na pág. 2 | 12 × 12 | 0 | 0 | 1 |
| **Total** | | | 211 × 211 | **0** | **0** | **7 linhas (9 itens)** |

(O bump 4 tem 2 linhas de achados, mas a primeira junta 4 folhas; por isso dá 9 itens em 7 linhas.)

---

## Itens da rodada 2

| Item | Corrigido? | Evidência |
|---|---|---|
| B2 · págs. 27, 32, 37, 40: a peça que sobra é sempre 21 | Sim | As peças que sobram são 10 (pág. 27), 11 (32), 9 (37) e 15 (40). Cada uma fica a ± 1 ou ± 2 de um resultado da folha, e nenhuma se repete. O gabarito (págs. 45–47) confere. |
| B2 · pág. 40 (e 32): contas fáceis, 2 − 1 repetida | Sim | Pág. 32: 13 − 7, 20 − 10, 18 − 10, 15 − 1, 20 − 11. Pág. 40: 12 − 3, 15 − 8, 16 − 2, 13 − 1, 13 − 12. Por script: todas as somas dão mais de 10, todas as contas de diminuir começam em 12 ou mais, e nenhuma das 20 contas se repete |
| B2 · págs. 16, 35: pato ambíguo em "Bichos ou coisas?" | Sim | O pato saiu e entrou o polvo, desenhado com cabeça, olhos e tentáculos (ampliado na pág. 35). O gabarito (págs. 44 e 46) põe o polvo em "Bichos". Pág. 16: gato, polvo, passarinho / lápis, tesoura, anel. |
| B3 · carta 35 fora do tom | Sim | "E se o jantar caísse do céu como chuva? O que você queria que caísse?" (pág. 8). Ver o achado novo abaixo. |
| B3 · pág. 2 "pensar junto" | Sim | "E se…? situações malucas para pensar juntos." |
| B4 · contas normais mais fáceis que o aquecimento | Sim | Págs. 42, 43, 50, 51, 57, 58, 62, 63: por script, nenhuma soma tem as duas parcelas abaixo de 10 e nenhuma conta de diminuir começa abaixo de 11. Ex.: pág. 43 com 13 − 4, 12 − 10, 13 − 12…; pág. 51 com 11 − 10, 16 − 11…. Não há conta repetida no bump. Os aquecimentos (págs. 34–35) ficaram iguais. |
| B5 · "Desembaralhe" com palavras repetidas | Sim | 24 palavras diferentes nas págs. 35, 42, 49 e 56 (entraram FACA, TREM, MESA, MEIA, MALA, BOLA, BARCO, ANEL…) |
| B5 · anagramas TOGA e SACA | Sim | Agora são OTGA (GATO) e ACSA (CASA). Li os 24 embaralhados e nenhum forma palavra. |
| B5 · "Complete com a sílaba" com palavras repetidas | Sim | 30 palavras diferentes nas págs. 33, 40, 47, 54 e 61. Ver o achado novo da pág. 54. |
| B5 · "Quantas sílabas?" com palavras repetidas | Sim | 32 palavras diferentes nas págs. 34, 41, 48 e 55. Cada folha mistura 1, 2 e 3 sílabas (1 sílaba: FLOR, TREM, SOL, PÃO). Os ícones novos de TREM (locomotiva) e PÃO (pão de forma) são reconhecíveis. |
| B5 · pág. 59 com duas respostas | Sim | "4. O ______ vive na água e tem escamas." Só o PEIXE serve; o gabarito (pág. 69) confere |
| B5 · ícones de FACA e MALA | Sim | Págs. 13 e 29, ampliadas a 150 dpi. A faca tem lâmina larga, ponta arredondada e cabo cinza com 2 rebites. A mala tem alça de puxar, listras e rodinhas e se lê como mala de viagem. |
| B5 · PEGA, PIQUE, BOLINHA | Sim | Pág. 57: XADREZ, QUEIMADA, PIPA, AMARELINHA, RODA, CORDA, CIRANDA, PETECA. Por script, cada palavra aparece 1 vez, só para a direita, para baixo ou na diagonal, como diz a instrução. |
| B6 · estrela que leva à lua | Sim | Pág. 2: "A figura só vale na casa onde o dado parou: se a estrela ou a nuvem levar a outra figura, essa não vale." A trilha (pág. 10) não mudou: estrelas nas casas 5, 13 e 22, nuvens nas 9, 18 e 26, lua na 15. |

Os 13 itens da rodada 2 estão corrigidos.

---

## Por bump

### 2. Recortar e colar — 40 de 40 (47 de 47 págs.)

Contagem real:
- **N1 (20):** quebra-cabeça de 4 peças ×5 (págs. 3, 8, 13, 17, 21), sombra ×5, do menor ao maior ×4,
  classificar ×4, complete a fila ×2.
- **N2 (20):** quebra-cabeça de 9 peças ×5 (9 peças em cada, contadas), monte as palavras ×5, classificar ×3,
  ordem ×3, cole o resultado ×4.

Conferidos sem problema:
- as 15 palavras de sílabas;
- as 3 ordens (26, 31, 36);
- as filas de "Complete a fila" (págs. 7 e 12), que têm resposta única;
- os grupos no gabarito;
- a figura-guia cinza, que continua visível em P&B.

**Achados:** nenhum.

### 3. Cartas de conversa — 48 de 48 (10 de 10 págs.)

Contagem real: 48 cartas numeradas de 1/48 a 48/48, 12 por categoria, 6 por folha nas págs. 3–10, com linha
tracejada em todas.

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 8 (carta 35) × 7 (carta 28) | cosmético | É efeito da correção: a carta 35 nova ("E se o jantar caísse do céu como chuva? O que você queria que caísse?") repete a ideia da carta 28 da mesma categoria ("E se chovesse pipoca?"). Ficam duas cartas de "comida caindo do céu" em folhas seguidas. | Trocar a 35 por outra situação maluca sem comida e sem pedido para o dia. Ex.: "E se as nuvens fossem de algodão-doce e desse para subir nelas?" ou "E se a sua sombra saísse para passear sozinha?" |

### 4. Matemática brincando — 60 de 60 (73 de 73 págs.)

Contagem real:
- **N1 (30):** conte e escreva 5, quantos ao todo 5, quantos sobram 5, onde tem mais 4, ligue ao número 4,
  complete os números 4, mercadinho 3.
- **N2 (30):** somar 5, diminuir 5, maior/menor 4, pirâmide 4, dezenas 3, mercadinho 4, grupos iguais 3,
  que número sou eu 2.
- **Fichas (pág. 3):** 30 fichas (12 de 1, 8 de 2, 6 de 5, 4 de 10).

Conferidos sem problema:
- as contas, pirâmides, mercadinhos, comparações e dezenas (script e imagem);
- os 3 "grupos iguais";
- os 2 "que número sou eu";
- as contagens das figuras do N1 e os "ligue ao número", conferidos na imagem contra o gabarito.

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 4, 5, 6, 12 (N1) | cosmético | A mesma resposta ou a mesma conta se repete na folha, e a criança acaba "adivinhando":<br>• pág. 4: 4 dos 6 quadros dão 5 (corações, luas, maçãs, casas);<br>• pág. 12: as linhas 1 e 4 são iguais (4 bolas + 1 bola), e 3 dos 4 totais dão 5;<br>• pág. 5: 2 + 1 duas vezes;<br>• pág. 6: 3 − 2 duas vezes. | No N1, sortear sem repetir a conta dentro da folha e com no máximo 2 respostas iguais por folha (o mesmo "sem repetir" já usado no N2, com rng derivado). |
| 47 | cosmético | No "Mercadinho das fichas", o copo aparece nos 5 problemas da folha (nos itens 1, 2, 3, 4 e 5). As outras folhas variam os itens. | Sortear os itens dos problemas sem usar o mesmo item mais de 2 vezes por folha. |

### 5. Letras e palavras — 60 de 60 (69 de 69 págs.)

Contagem real:
- **N1 (30):** letra A/E/I/O/U 5, com que letra começa 6, ligue à primeira letra 4, ache a letra 4, qual vogal
  falta 5, letras iguais 5, as cinco vogais 1.
- **N2 (30):** complete com a sílaba 5, quantas sílabas 4, desembaralhe 4, caça-palavras 4, rimas 4, complete a
  frase 5, ordem alfabética 4.

Conferidos sem problema:
- as 36 letras iniciais e os 20 "ligue";
- as contagens de "ache a letra" (A 10, E 11, O 10, B 11), contadas na imagem;
- as 30 vogais;
- as 30 sílabas;
- as 32 contagens de sílabas (4 bolinhas por palavra, máximo de 3 sílabas);
- os 24 desembaralhes;
- as 20 rimas, sem rima cruzada;
- as 20 frases, todas com uma resposta só;
- as 4 ordens alfabéticas (CHAVE antes de CORAÇÃO certo na pág. 60);
- os 4 caça-palavras.

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 54 (gabarito 68) | cosmético | É efeito da correção: CASA e MESA precisam as duas de **SA**, mas a fileira tem só 7 sílabas (BE LU MA NO SA TE XE), com um SA. Nas outras 4 folhas são 8 sílabas: as 6 respostas e 2 que sobram, cada uma usada uma vez. A criança que risca a sílaba usada fica sem SA para a segunda palavra. | Repetir SA na fileira (fica com 8 sílabas, como as outras), ou trocar CASA ou MESA por uma palavra com ícone, ainda não usada nas 30, cuja sílaba que falta não esteja na fileira. Vale um assert novo: as 6 sílabas que faltam são diferentes, ou a fileira traz cada uma quantas vezes for preciso. |
| 61 (gabarito 69) | cosmético | É efeito da correção: a sílaba que sobra **MA** completa "__LA" e forma **MALA**, uma palavra que tem figura no próprio bump (págs. 29, 55 e 56). A figura ali é a vela, então a resposta certa é VE, mas a sobra forma uma palavra real e conhecida da criança. | Trocar a sobra MA por uma sílaba que não forme palavra com nenhuma das 6 metades (ex.: PU, JU). Vale testar por script: sobra + metade ≠ palavra da lista do bump. |
| 13 (gabarito 64) | cosmético | "Qual vogal falta?": 5 das 6 respostas são **A** (FAC_, UV_, C_SA, BOL_, M_ÇÃ; só BALÃ_ é O). Na terceira palavra a criança já escreve A sem pensar. As outras folhas variam (ex.: pág. 19: E, O, O, E, A, O). | Na troca, exigir pelo menos 3 vogais diferentes por folha. Ex.: trocar BOLA/CASA por palavras cuja vogal que falta seja E, I ou U (ex.: _NHA→UNHA, DED_→DEDO). |

### 6. Jogos de mesa — 5 de 5 (12 de 12 págs.)

Contagem real:
- bingo: 6 cartelas 3x3, todas diferentes, sem figura repetida dentro da cartela; juntas, cobrem as 16 fichas;
- dominó: 28 peças das 7 figuras, sem repetição nem falta (contadas nas págs. 7–8);
- memória: 24 cartas, 12 pares exatos;
- trilha: 30 casas, com estrela em 5, 13 e 22, nuvem em 9, 18 e 26, e lua em 15;
- 4 peões;
- dado com faces opostas 1–6, 2–5 e 3–4 na planificação;
- velha: 2 tabuleiros, 5 estrelas e 5 corações;
- regras dos 5 jogos na pág. 2, já com a frase nova da trilha.

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 3–5 (bingo) | cosmético | As figuras estão mal distribuídas nas cartelas. O **balão** está nas 6 (quando sai, todo mundo marca), banana e maçã estão em 5, e árvore e passarinho em só 1. As linhas ficam muito parecidas entre os jogadores, e algumas fichas quase nunca contam. | Distribuir as 16 figuras de forma parelha: 54 casas ÷ 16 figuras dá 3 ou 4 cartelas por figura. Manter o assert de "cobre as 16" e somar outro com "cada figura em no máximo 4 cartelas". |

---

## Pendências para fechar a revisão

Todas cosméticas. Nenhuma impede o uso:

1. B3 · carta 35 parecida com a 28 (comida caindo do céu).
2. B4 · págs. 4, 5, 6 e 12: respostas e contas repetidas na mesma folha do N1.
3. B4 · pág. 47: o copo nos 5 problemas do mercadinho.
4. B5 · pág. 54: SA serve duas palavras e aparece uma vez só na fileira de sílabas.
5. B5 · pág. 61: a sílaba que sobra (MA) forma MALA.
6. B5 · pág. 13: 5 das 6 vogais que faltam são A.
7. B6 · bingo: balão nas 6 cartelas; figuras mal distribuídas.

Os itens 1, 4 e 5 vêm das correções da rodada 2. Os outros já estavam nos PDFs e não tinham sido apontados.
