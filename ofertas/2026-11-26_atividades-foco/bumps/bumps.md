# Order bumps e pós-compra — Dez Minutinhos

Regras em `docs/04_order-bumps.md`. Fonte dos nomes, preços e ordem: `briefing.md` (seção "Order bumps").
Produzidos em 2026-11-26. Arquivos em `produto/bumps/<n>_<slug>/` (PDF versionado; o `.zip` de entrega
para a Hotmart fica ao lado e é ignorado pelo git). Gerador: `produto/gerador/bump_*.py` + `render_bumps.cjs`.

| Ordem | Nome | Título no checkout | Descrição (até 2 frases) | Preço | Págs | Arquivo | Status |
|---|---|---|---|---|---|---|---|
| 1 | Para levar na bolsa | Para levar na bolsa: 30 atividades em meia folha | Tamanho A5 para restaurante, viagem e sala de espera. Imprime duas por folha, corta no meio e cabe na bolsa. | R$ 9,90 | 20 (A4 deitado, 2 atividades por folha) | `produto/bumps/1_para-levar-na-bolsa/para-levar-na-bolsa.pdf` | ✅ |
| 2 | Recortar e colar | Tesoura e cola: 40 atividades de recortar e colar | Quebra-cabeças, sombras, grupos, sílabas e contas para recortar e colar, nos dois níveis. Com tesoura sem ponta e cola branca. | R$ 12,90 | 47 | `produto/bumps/2_recortar-e-colar/recortar-e-colar.pdf` | ✅ |
| 3 | Cartas de conversa | Cartas de conversa: 48 perguntas para a família | Para recortar e usar no jantar, no carro ou antes de dormir. Perguntas leves sobre o dia, imaginação e preferidos, sem lição. | R$ 14,90 | 10 | `produto/bumps/3_cartas-de-conversa/cartas-de-conversa.pdf` | ✅ |
| 4 | Matemática brincando | Matemática brincando: 60 atividades de contas e mercadinho | Contar, somar, diminuir, comparar e brincar de lojinha com fichas de papel, nos dois níveis. | R$ 17,90 | 70 | `produto/bumps/4_matematica-brincando/matematica-brincando.pdf` | ✅ |
| 5 | Letras e palavras | Letras e palavras: 60 atividades de alfabeto, sílabas e rimas | Nível 1 com vogais e primeira letra; Nível 2 com sílabas, palavras, rimas e frases curtas. | R$ 17,90 | 69 | `produto/bumps/5_letras-e-palavras/letras-e-palavras.pdf` | ✅ |
| 6 | Jogos de mesa | Jogos de mesa para imprimir: bingo, dominó, memória, trilha e jogo da velha | Cinco jogos com figuras para a família jogar junto, com as regras numa página só. | R$ 19,90 | 12 | `produto/bumps/6_jogos-de-mesa/jogos-de-mesa.pdf` | ✅ |
| 7 | Volume 2 | Volume 2: mais 120 atividades novas | Mesmas categorias e níveis do caderno, nenhuma repetida, com outro plano de 30 dias. | R$ 27,00 | 140 | `produto/bumps/7_volume-2/volume-2.pdf` | ✅ |

Todas as capas têm "Complemento do Dez Minutinhos" ("Continuação" no Volume 2) e "por Gefferson Balles" (exigência da Hotmart para eBook).
Rodapé de cada página: "Dez Minutinhos · <nome do bump> · página N".

## O que tem em cada um

1. **Para levar na bolsa** — 30 atividades rápidas (15 Nível 1, 15 Nível 2): labirintos pequenos, padrões,
   conte e circule, qual é diferente, ligue os pontos, siga o caminho, sudoku de figuras e 6x6, que número falta,
   encontre a diferente, quantos tem, código secreto ("BOA VIAGEM") e caça-palavras. Gabarito em 4 folhas.
2. **Recortar e colar** — Nível 1 (20): quebra-cabeça de 4 peças (com figura-guia), cada um na sua sombra,
   do menor ao maior, classificar em 2 grupos, complete a fila. Nível 2 (20): quebra-cabeça de 9 peças (com
   modelo ao lado), monte as palavras com sílabas, classificar, coloque números em ordem, cole o resultado da conta.
3. **Cartas de conversa** — 48 cartas, 6 por folha, em 4 categorias de 12: Meu dia, Imaginação, E se…?, Preferidos.
4. **Matemática brincando** — Nível 1 (30): conte e escreva, quantos ao todo, quantos sobram, onde tem mais,
   ligue ao número, complete os números (até 40), mercadinho. Nível 2 (30): contas de somar e diminuir (até 30),
   maior/menor/igual (até 99), pirâmide de somas, dezenas e unidades, mercadinho com problemas, grupos iguais
   (introdução à multiplicação), que número sou eu. Folha de fichas de brincar para recortar.
5. **Letras e palavras** — Nível 1 (30): letras A/E/I/O/U para cobrir, as cinco vogais, com que letra começa,
   ligue à primeira letra, ache a letra, qual vogal falta, letras iguais. Nível 2 (30): complete com a sílaba,
   quantas sílabas, desembaralhe, caça-palavras (casa, roupas, doces, brincadeiras), palavras que rimam,
   complete a frase, ordem alfabética.
6. **Jogos de mesa** — bingo de figuras (6 cartelas + 16 fichas), dominó de figuras (28 peças), jogo da
   memória (12 pares), trilha das figuras (tabuleiro de 30 casas, 4 peões e dado de papel para montar),
   jogo da velha (2 tabuleiros + 10 peças). Regras numa página.
7. **Volume 2** — 120 atividades novas (60 por nível, mesma distribuição de categorias do volume 1:
   atenção 12, memória 8, padrões 10, lógica 12, traçado 10, cores e códigos 8), plano de 30 dias por nível,
   gabarito. Cenas dos jogos de diferenças, desenhos de ligar pontos, artes do "pinte pelo código", temas de
   caça-palavras, grades lógicas e mensagens do código secreto são todos diferentes do volume 1.

## O que foi conferido

- Tudo que tem resposta é calculado e testado no código (assert): labirintos com saída, sudokus e grades
  lógicas com solução única, caça-palavras com cada palavra aparecendo uma só vez, contas, comparações,
  pirâmides, dezenas, sílabas que formam a palavra, rimas com o mesmo final, ordem alfabética, cartelas de
  bingo cobrindo as 16 figuras, 28 peças distintas no dominó, 12 pares exatos na memória, faces opostas do
  dado somando 7. Os gabaritos são gerados a partir dessas mesmas respostas.
- Todas as páginas de todos os bumps foram renderizadas e olhadas em folhas de contato; corrigido o que
  estava ruim (peças de quebra-cabeça saindo da página, legenda do arco-íris com cor sem uso, cena com
  objetos sobrepostos, texto estourando caixa, palavra longa invadindo a coluna, espaços desalinhados em frases).
- Nenhuma palavra vetada (TDAH, cérebro, neuro, potencial, cognitivo) — checado automaticamente na montagem.
- Sem rosto de criança, sem marca de terceiros, sem cédula ou moeda do Real (só fichas de desenho próprio).

## Pós-compra (ainda não produzido)

- **Coleção Ano Inteiro — R$ 47,00:** 12 cadernos temáticos mensais com datas do calendário brasileiro,
  30 atividades cada (360 no total). Produzir só depois de validar vendas.

## Ticket médio projetado (hipótese do briefing, não medida)

- Principal R$ 37,00 + bumps (aceites 35/25/20/25/20/15/12%) ≈ R$ 23,95 + pós-compra 8% ≈ R$ 3,76
  → **≈ R$ 64,70**. Trocar pelas taxas reais assim que houver vendas.
