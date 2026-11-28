# Rodada 2: revisão do caderno "Dez Minutinhos", páginas 66 a 149

Arquivo: `produto/final/dez-minutinhos.pdf` (149 págs., A4, gerado em 2026-11-28 01:58). Revisado em 2026-11-28.
Base: `caderno-p66-149.md` (rodada 1) e `correcoes.md`. Nenhum arquivo do produto foi editado.

**Veredito: NÃO LIMPA.** O único motivo é 1 cosmético da rodada 1 que não foi corrigido de propósito: a
categoria "Cores e códigos" nos caça-palavras ficou para o dono decidir (`correcoes.md`, "Cosméticos para o
dono decidir", item 1). Tirando isso, a revisão está limpa. Não há nada que bloqueie ou atrapalhe. Os 2 achados
novos são cosméticos e opcionais. Se o dono decidir manter a categoria como está, o veredito passa a ser LIMPA.

**Resumo**
1. Dos 15 itens da rodada 1, 14 foram corrigidos e conferidos em imagem. O 15º (categoria dos caça-palavras)
   está pendente de decisão do dono.
2. O gabarito tem 120 miniaturas, uma para cada atividade das págs. 6 a 65 e 68 a 127, sem falta e sem
   repetição. O título de cada miniatura bate com o da folha, conferido por script.
3. Conferi todas as 60 respostas do Nível 2 contra a atividade:
   - **Sudokus:** os 5 foram resolvidos por script. Cada um tem solução única e o gabarito bate casa a casa.
   - **Que número falta?:** as 36 filas estão certas e nenhuma se repete.
   - **Códigos secretos:** BRINCAR FAZ BEM, BOM TRABALHO e SUPER DESAFIO.
   - **Grades lógicas:** as 3 têm resposta única.
   - **Caça-palavras:** as 32 palavras aparecem uma vez cada, nas direções que a instrução promete.
   - **Jogos dos 7 erros:** os 5 têm 7 diferenças, comparadas a olho e por diferença de pixels. O gabarito
     circula as 7.
   - **Contagens, memória, "Onde estava?", "Encontre a diferente" e "O que vem depois?":** todos conferem.
4. Os 9 "Pinte pelo código" agora mostram o desenho pintado no gabarito: coração, sol, estrela, sorvete,
   casa, árvore, barco, flor e o peixe de 4 cores do N2.
5. Os 10 "Ligue os pontos" fecham no gabarito: casa, coração, barquinho, peixe e estrela no N1; casa,
   foguete, coração, peixe e estrela no N2. A instrução diz "volte ao 1".
6. Os 2 cosméticos novos: a casa de cabeça para baixo na pág. 125 e duas frases no infinitivo no bônus 2.
   A ordem do plano e o rodapé "Dia N" de cada página batem.

**Páginas olhadas em imagem: 84 de 84 (66 a 149).**
- **Todas as páginas:** a 70 dpi, em pares lado a lado.
- **Gabarito (128 a 141):** de novo a 110 dpi, página por página.
- **Recortes ampliados (150 a 200 dpi):** págs. 74 (maçãs), 85 (balões e flores), 89 (números 17 a 22),
  91 (flores), 105 (carros), 113 e 125 (filas de barcos, casas e pássaros), 138 (regras do gabarito) e
  141 (círculos do 7 erros).
- **Texto:** conferido com `pdftotext -layout` e `-bbox`.

Contagem dos achados novos: **bloqueia 0 · atrapalha 0 · cosmético 2**
(e mais 1 cosmético da rodada 1 que continua pendente de decisão do dono)

## (a) Itens da rodada 1

| Item | Corrigido? | Evidência |
|---|---|---|
| Gabarito dos 9 "Pinte pelo código" sem cor (atrapalha) | Sim | Págs. 128 (p. 10, coração vermelho), 129 (p. 16, sol), 130 (p. 24, estrela, e p. 30, sorvete), 131 (p. 40, casa), 132 (p. 47, árvore), 133 (p. 55, barco), 134 (p. 61, flor) e 136 (p. 86, peixe). Todos aparecem pintados, com a legenda de cores. As cores do peixe da p. 86 batem com as contas (resultados 1, 2, 4 e 6) |
| Pág. 106, fila 5 ambígua (atrapalha) | Sim | Agora é 1 › 5 › 8 › 12 › ○, e o gabarito (p. 138) dá 15 com a regra "+4, +3". A fila 4 (6 › 8 › 11 › 13 › ○ = 16) também deixa o número que falta na última casa |
| Pág. 119, fila 2 ambígua (atrapalha) | Sim | Agora é 7 › 11 › 16 › 20 › ○, e o gabarito (p. 140) dá 25 com a regra "+4, +5" |
| Pág. 85, balão espelhado quase invisível (atrapalha) | Sim | O 2º balão agora está **menor**, bem visível (recorte a 200 dpi). Os 7 erros são: balão cinza, balão menor, árvore sumida, árvore cinza, carro cinza e as 2 flores cinza. O gabarito (p. 136) circula os 7 |
| Pág. 105, carro espelhado (atrapalha) | Sim | O carro diferente (2ª fila, 4º) está **sem a roda de trás** e com a base reta, fácil de ver (recorte a 200 dpi). O gabarito (p. 138) circula o carro certo |
| Pág. 126, maçã sem folha pequena (cosmético) | Sim | Agora é a **maçã cinza**. O gabarito (p. 141) circula as 7: 2 balões cinza, coração menor, estrela menor, árvore sumida, flor cinza e maçã cinza |
| Pág. 86, "Pinte pelo código" de uma cor só (cosmético) | Sim | O peixe tem 4 cores (1 vermelho, 2 amarelo, 4 azul, 6 laranja) e contas com resultados diferentes. Nenhuma conta dá um número fora da legenda |
| Págs. 77, 95, 113 e 125, filas repetidas no "O que vem depois?" (cosmético) | Sim | Comparei as 20 filas e nenhuma se repete. A fila "( ) ( ) ( )" só aparece na p. 77. "Peixe, peixe espelhado, estrela" também só na p. 77. Os triângulos girando estão na p. 77 e a fila de pássaros com nuvem na p. 125 é diferente da p. 77. Todas as respostas têm opção única |
| Págs. 69, 84, 99, 111 e 127, "quadradão de 6 casinhas" (cosmético) | Sim | A instrução diz "…nem no bloco de 6 casinhas". A dica diz "Cada linha, coluna e bloco de linha grossa (2 linhas x 3 colunas) tem 1 a 6." |
| Págs. 73, 93, 108 e 122, etiqueta "Cores e códigos" nos caça-palavras (cosmético) | **Não** | As 4 páginas continuam com "Cores e códigos" no topo. Foi de propósito: está em `correcoes.md`, "Cosméticos para o dono decidir", item 1 (a proposta é "Letras, cores e códigos"). Espera decisão do dono |
| Págs. 134 a 141, regra pequena e laranja no gabarito (cosmético) | Sim | A regra agora sai em preto, maior e legível (recorte da p. 138 a 200 dpi: "soma 5", "+2, +3", "+4, +3", "soma 6") |
| Pág. 141, círculo do balão cortado (cosmético) | Sim | O círculo do balão da direita fica inteiro dentro do painel. Ele encosta na borda, mas não é cortado (recorte a 200 dpi) |
| Pág. 89, números 18 e 20 colados (cosmético) | Sim | O 18 está embaixo do ponto dele e o 20 à esquerda do dele. Cada número fica claramente com o seu ponto (recorte a 200 dpi) |
| Págs. 143 a 145, "recorte na linha" claro e certificado vazio (cosmético) | Sim | O "✂ recorte na linha" está maior e mais escuro. No meio dos 6 certificados entram a frase "Cada dia de esforço conta. Parabéns!" e 5 figuras |
| Pág. 142, quadro de conquistas com "Nível: ___" (cosmético) | Sim | Linha nova: "Imprima um quadro para cada nível: são 30 dias no Nível 1 e mais 30 no Nível 2." |
| Extra: "Ligue os pontos" aberto, item 2 do `correcoes.md` (de outro relatório, conferido aqui) | Sim | As 5 instruções do N2 (págs. 76, 89, 100, 112 e 124) dizem "e volte ao 1 para fechar o desenho". Os 10 gabaritos (págs. 129 a 140) mostram o contorno fechado, incluindo o barquinho da p. 39 com 15 pontos |
| Extra: "Copie o desenho" encostado na esquerda (de outro relatório) | Sim | Nas págs. 71, 82, 94, 107 e 118, o modelo está no meio da grade de 7x7 |

## (b) Novos achados

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 125 (fila 4) | cosmético | A variante nova "girar" (de `CICLOS_EXTRAS`) pôs a **casa de cabeça para baixo** (casa, casa invertida, casa invertida…). Invertida, a casa parece uma seta ou uma caixa, e a criança pode não reconhecer que é a mesma figura. A resposta (casa em pé) está certa e é a única opção possível | Opcional: em `CICLOS_EXTRAS`, girar só figuras que continuam reconhecíveis de cabeça para baixo (seta, triângulo, banana, coração) e não a casa. Ou trocar a fila |
| 146 e 147 | cosmético | No bônus "30 ideias longe da tela", quase todas as ideias usam o imperativo ("Ponha", "Arrume", "Monte"). Duas usam o infinitivo: a 14 ("Lavar frutas, contar colheres, arrumar a mesa") e a 23 ("Escrever ou desenhar uma cartinha…") | Opcional: "Lave frutas, conte colheres, arrume a mesa." e "Escreva ou desenhe uma cartinha…" |

## O que foi conferido de novo e está certo

- **Abertura e plano (66–67):** as 60 entradas apontam a página certa e com o mesmo título da folha (script).
  O rodapé "Dia N" de cada página, de 68 a 127, bate com o plano. Os 2 tipos de cada dia são diferentes.
- **Sudokus 6x6:** cada um tem solução única, e o gabarito bate casa a casa com a solução calculada.
  - Pág. 69: 20 pistas.
  - Pág. 84: 18 pistas.
  - Pág. 99: 17 pistas.
  - Pág. 111: 16 pistas.
  - Pág. 127: 15 pistas.
- **Que número falta?:** as 36 filas estão certas no gabarito, nenhuma se repete entre as 6 folhas e nenhuma
  fica ambígua. Nas filas de regra alternada, o número que falta fica sempre na última casa.
  - Pág. 70: 6, 22, 22, 15, 52 e 12.
  - Pág. 83: 13, 44, 21, 23, 18 e 17.
  - Pág. 88: 20, 48, 37, 37, 4 e 24.
  - Pág. 101: 8, 56, 44, 14, 19 e 17.
  - Pág. 106: 31, 38, 16, 16, 15 e 46.
  - Pág. 119: 82, 25, 33, 29, 22 e 46.
- **Caça-palavras (73, 93, 108, 122):** as 32 palavras foram achadas por script, uma vez cada, para o lado,
  para baixo ou na diagonal. O realce do gabarito bate.
- **Código secreto (78, 103, 116):** BRINCAR FAZ BEM, BOM TRABALHO e SUPER DESAFIO. Todas as figuras estão
  na tabela.
- **Grades lógicas:** cada uma tem resposta única.
  - Pág. 80: Ana come banana, Beto come maçã e Caio come uva.
  - Pág. 96: Lia brinca com o barquinho, Téo com o carrinho e Rui com o balão.
  - Pág. 115: Duda desenhou a estrela, Enzo a lua e Bia o sol.
- **Quantos tem?:** contei de novo e bate com o gabarito.
  - Pág. 81: 9 estrelas, 9 corações e 8 luas.
  - Pág. 98: 8 maçãs, 7 uvas, 8 bananas e 3 flores.
  - Pág. 114: 5 peixes, 4 barcos, 7 sóis e 8 nuvens.
- **7 erros (68, 85, 97, 110, 126):** cada um tem 7 diferenças, todas visíveis. O gabarito circula as 7.
- **Olhe e lembre (72, 87, 92, 109, 123):** todas as figuras de cima estão nas opções. O gabarito dá 5, 6, 6,
  7 e 8, que confere.
- **Onde estava? (79, 102, 117):** as posições do gabarito estão certas.
- **Encontre a diferente (74, 91, 105, 120):** há uma diferente por quadro, visível a olho, e o gabarito está
  certo.
- **Labirintos (75, 90, 104, 121):** têm entrada e saída abertas, e o gabarito traça o caminho inteiro.
- **Gabarito do N1 (128–134):** olhei as 60 miniaturas. Nada cortado, os pintes estão pintados e os ligue
  fecham.
- **Bônus (142–149):**
  - Quadro de conquistas com 30 casas.
  - 6 certificados: semanas 1 a 4, Nível 1 e Nível 2.
  - "30 ideias longe da tela": 30, numeradas de 1 a 30.
  - "Guia do adulto": 2 páginas.
  - Fora as 2 frases da tabela, não vi erro de ortografia ou concordância.
- **Impressão:** não vi texto cortado nem fora da margem. Os cinzas das diferenças, o fundo das pistas do
  sudoku e o aviso de corte continuam visíveis em P&B.
