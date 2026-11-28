# Rodada 4 (final, regra R12): páginas que mudaram na correção da rodada 3

Data: 2026-11-28 · Revisor de qualidade · Nenhum arquivo do produto, dos criativos ou da página foi editado
(só este relatório foi gravado).

## Veredito: **LIMPA**

- **Bloqueia 0 · atrapalha 0 · cosmético novo 0.**
- **Pendências da rodada 3: 10 de 10 resolvidas** (A6, A7, o cosmético do caderno, os 7 itens dos bumps e B1).
- Os 2 itens que o dono aceitou por escrito ("Cores e códigos" e a estrela da p. 24) continuam como estão e não
  contam.
- **Para a versão 1.1:** nada novo. Ficam só 2 observações, que não são achados (ver o fim).

**O que foi olhado**
- **Páginas:** as 65 páginas que mudaram, renderizadas a 70 dpi (`pdftoppm -r 70`) e olhadas uma a uma. Também:
  - as 4 folhas de "O que vem depois?" do N2 do V2, a 90 dpi;
  - as 4 células de gabarito do N2 do V2 (págs. 134, 136, 138, 140), a 110 dpi;
  - as folhas do N1 do V2, lado a lado com a versão anterior.
- **Vídeos:** 13 quadros de cada anúncio, incluindo os últimos 3 s. Também todos os quadros a 10 por segundo,
  medidos por script.
- **Pasta das imagens:** `/tmp/claude-0/-home-user/2250d25c-d581-568f-b4e4-6cb893f20944/scratchpad/r4/`.

## 1. Prova por pixel (confirmada)

**Versão de base:** o pai do commit `3ae1194` ("correções da rodada 3"), via `git show 3ae1194^:<pdf>`. Os md5 da
base são os mesmos que a rodada 3 revisou: caderno `32525034…` e V2 `a5a67ec6…`. O PDF atual é igual ao de `HEAD`
(md5).

**Como comparei:** as duas versões renderizadas a 72 dpi, com diferença exata de pixels em todas as páginas.

| PDF | Págs. (base × atual) | Mudaram (achado por script) | Igual à lista do `correcoes.md`? |
|---|---|---|---|
| `produto/final/dez-minutinhos.pdf` | 149 × 149 | 20, 38, 129, 131 | sim |
| Bump 3 `cartas-de-conversa.pdf` | 10 × 10 | 8 | sim |
| Bump 4 `matematica-brincando.pdf` | 73 × 73 | 4, 5, 6, 11, 12, 13, 19, 20, 25, 26, 27, 31, 32, 33, 39, 47, 55, 61, 64, 65, 66, 67, 68, 69, 71, 72, 73 | sim |
| Bump 5 `letras-e-palavras.pdf` | 69 × 69 | 13, 29, 40, 47, 54, 61, 64, 65, 67, 68, 69 | sim |
| Bump 6 `jogos-de-mesa.pdf` | 12 × 12 | 3, 4, 5 | sim |
| Volume 2 `volume-2.pdf` | 140 × 140 | 7, 13, 19, 44, 56, 61, 76, 93, 112, 124, 127, 128, 131, 132, 133, 134, 136, 138, 140 | sim |

**O que não mudou:**
- Bumps 1 e 2: nada mudou na pasta desde a base (`git diff` vazio).
- **Zips:** os 8 têm 1 PDF cada, e o md5 de cada um é igual ao do PDF da pasta (caderno `7794e57d`, bump 3
  `27e77e58`, bump 4 `c2724cc4`, bump 5 `221564e5`, bump 6 `2f841784`, V2 `346a24c4`; bumps 1 e 2 iguais à base).

## 2. Pendências da rodada 3

| # | Pendência (relatório) | Resolvida? | Evidência |
|---|---|---|---|
| A6 | V2 N2: 15 das 20 filas de "O que vem depois?" iguais às do caderno (págs. 76, 93, 112, 124) · `rodada3-volume2-e-midia.md` | **sim** | **Conferência fila por fila.** Comparei as 20 filas do V2 N2 com as 20 do caderno N2 (págs. 77, 95, 113, 125, olhadas lado a lado). Nenhuma é igual, girada ou deslocada. Exemplos: o barco do caderno (p. 113 f4) é em pé, virado, virado; o do V2 é em pé, em pé, virado (p. 112 f2) ou em pé, virado, flor (p. 124 f4). O peixe do caderno é peixe, peixe, peixe virado (p. 95 f5); no V2 é peixe, virado, virado, nuvem (p. 93 f1) ou peixe, peixe, virado, virado (p. 124 f2).<br>**Folha por folha:** em cada folha, só uma fila gira cada figura.<br>**Respostas:** resolvi as 20 filas. Cada uma tem uma resposta só, e ela está entre as opções. Os gabaritos das págs. 134, 136, 138 e 140 circulam a certa nas 20 |
| A7 | V2 N1 repetia filas do caderno (p. 19 f1, p. 56 f5 + 8 achadas pelo script) | **sim** | Págs. 7, 13, 19, 44, 56 e 61 olhadas lado a lado com a versão anterior. As trocas usam o mesmo molde (AAB, AB, ABB…), então a dificuldade da folha não mudou.<br>Respostas: p. 7 peixe, coração, casa, estrela, quadrado; p. 13 coração, casa, triângulo, estrela, casa; p. 19 árvore, peixe, balão, triângulo, losango; p. 44 círculo, quadrado, losango, estrela, lua; p. 56 peixe, quadrado, balão, losango, círculo; p. 61 casa, nuvem, flor, casa, círculo.<br>As 6 batem com os gabaritos das págs. 127, 128, 131, 132 e 133 |
| Cad. | Caderno N1: mesma série deslocada (p. 14 × 20, p. 27 × 38) | **sim** | **p. 20 f3:** casa, casa, maçã (resposta casa). **p. 38 f2:** nuvem, coração (resposta nuvem). As duas folhas têm 5 filas com resposta única. Os gabaritos das págs. 129 e 131 circulam a certa nas 10 filas |
| Script | Nenhuma fila dos dois volumes repete outra (igual, girada ou deslocada) | **sim** | **Conferência independente das 140 filas.** Rodei o gerador numa cópia, na pasta de rascunho: o `completo.html` e o `bump-volume-2.html` gerados têm o mesmo md5 dos HTML do produto (`7e620d2f`, `04babf4a`). Depois agrupei as filas com uma função de comparação minha, que considera o ciclo reduzido, a menor rotação e o peixe/lua de ponta-cabeça como espelhados.<br>**Resultado:** 140 filas, 140 diferentes, 0 repetidas, em caderno × caderno, V2 × V2 e caderno × V2. Também com a fila lida de trás para frente: 0 repetidas |
| B3 | Carta 35 repetia a ideia da 28 | **sim** | p. 8: "E se a sua sombra saísse para passear sozinha? Aonde ela iria?". Não tem comida nem nuvem, e "aonde" está certo (verbo de movimento). Nenhuma outra carta fala de sombra |
| B4a | Págs. 4, 5, 6, 12: conta ou resposta repetida na folha do N1 | **sim** | **Conferência por script e na imagem**, nas págs. 5, 6, 12, 13, 19, 20, 26, 27, 32 e 33: nenhuma resposta e nenhuma conta repete na folha. Ex.: p. 5 dá 4, 3, 5, 2; p. 12 dá 5, 2, 3, 4.<br>**"Conte e escreva":**<br>• p. 4: 1, 3, 5, 5, 4, 2 (de 1 a 5, um só repete);<br>• p. 11: 3, 2, 6, 4, 1, 5;<br>• p. 25: 6, 8, 9, 3, 7, 5;<br>• p. 31: 6, 7, 8, 5, 4, 9.<br>Contei as figuras na imagem, e os gabaritos das págs. 64 a 68 batem em tudo |
| B4b | p. 47: o copo nos 5 problemas | **sim** | **p. 47:** copo 2, carrinho 2, sorvete 2, pipa 2, maçã 1. Respostas 11, 8, 12, 5, 15.<br>**As outras 3 folhas:**<br>• p. 39 (no máximo 2 por item): 10, 11, 16, 4, 16;<br>• p. 55: 12, 9, 6, 1, 24;<br>• p. 61: 11, 8, 16, 6, 19.<br>Fiz as contas pela tabela de preços, e os gabaritos das págs. 69, 71, 72 e 73 batem |
| B5a | p. 54: SA para CASA e MESA, só 7 sílabas | **sim** | A fileira é FU LU MA SA SA TE XE ZI (8 sílabas, com SA duas vezes). As respostas são CASA, LUA, PEIXE, MESA, MAÇÃ e TESOURA. O gabarito da p. 68 confere |
| B5b | p. 61: a sobra MA formava MALA (e p. 40 BECO, p. 47 COLO) | **sim** | As sobras são p. 40 JE/ZU, p. 47 JE/FE, p. 54 FU/ZI e p. 61 JU/XI. Testei cada sobra com as 6 metades de cada folha, e nenhuma forma palavra. As respostas e os gabaritos das págs. 67, 68 e 69 conferem (p. 61: ÁRVORE, GATO, VELA, FACA, OVO, ILHA) |
| B5c | p. 13: 5 de 6 vogais A | **sim** | **p. 13:** A, E, A, A, A, U (FACA, PENTE, CASA, BOLA, BALÃO, BULE): 3 vogais diferentes, o critério pedido.<br>**p. 29:** O, I, O, I, E, E (BARCO, SINO, LIVRO, MILHO, ÁRVORE, VELA).<br>Os ícones novos dão para reconhecer (pente, bule, sino, milho), e os gabaritos das págs. 64 e 65 conferem |
| B6 | Bingo mal distribuído (balão nas 6 cartelas) | **sim** | **Conferência por script, no texto das cartelas:** 6 cartelas diferentes, 9 figuras diferentes em cada. Das 16 figuras, 6 estão em 4 cartelas e 10 em 3, e as 16 aparecem.<br>**Cartelas parecidas:** duas cartelas dividem de 2 a 6 figuras, perto do que se espera ao acaso (≈ 5). As fichas da p. 6 são as mesmas 16 figuras |
| B1 | O zoom dos anúncios 1 e 2 cortava a borda da página | **sim** | **Medido por script em todos os quadros (10 por segundo):** em nenhum quadro a página branca encosta na borda do quadro. A menor margem é de 32 px dos dois lados (anúncio 1 aos 14,5 s; anúncio 2 aos 10,5 s).<br>**Olhado nos quadros:** "Plano de 30 dias" aparece inteiro, com o "P" e a coluna "Feito". O gabarito da p. 128 cabe inteiro na largura, e o selo "Gabarito completo" fica acima do cabeçalho "Dez Minutinhos", sem cobrir.<br>**Resto do vídeo:** os 3 últimos segundos dos dois anúncios mostram o cartão final inteiro (R$ 37,00, "Toque em Saiba mais"). Os dois têm 1080×1920 a 30 fps, com 22,10 s e 21,63 s |

## 3. Achados

| Página | Gravidade | Problema |
|---|---|---|
| — | — | Nenhum achado. Nas 65 páginas que mudaram, as atividades dão para fazer e as respostas do gabarito batem. A impressão está boa: nada cortado, contraste bom em P&B. O português está certo |

**Contagem:** bloqueia 0 · atrapalha 0 · cosmético 0.

## 4. Para a versão 1.1

Nenhum cosmético novo. Por isso não foi criado o `revisoes/melhorias-v1.1.md`.

Ficam 2 observações. Não são achados e não seguram o lançamento:
1. **Bump 5, p. 13:** a regra nova (pelo menos 3 vogais diferentes) está cumprida, mas a folha ainda tem 4 das 6
   respostas em A. Se um dia mexer no gerador, dá para pedir no máximo 3 respostas iguais por folha.
2. **V2, p. 13 (N1):** as filas 2 (casa, casa, triângulo) e 5 (casa, casa, flor) têm o mesmo molde e a mesma figura
   que se repete. As duas são do sorteio original e não mudaram nesta rodada. São filas diferentes e cada uma tem
   uma resposta só.
