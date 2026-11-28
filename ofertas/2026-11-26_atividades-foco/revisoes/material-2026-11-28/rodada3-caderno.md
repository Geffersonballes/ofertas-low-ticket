# Rodada 3 (final): revisão do caderno "Dez Minutinhos", 149 páginas

Data: 2026-11-28 · Arquivo: `produto/final/dez-minutinhos.pdf` (149 págs., A4, gerado em 2026-11-28 02:36 UTC,
md5 `32525034c4c0fed6fcbc440d48ea8cfe`). Base: `rodada2-caderno-p1-66.md`, `rodada2-caderno-p66-149.md` e
`correcoes.md` ("## Rodada 2"). Nenhum arquivo do produto foi editado.

## Veredito: NÃO LIMPA

**Pendências: 2.** Nada bloqueia.

- **1 atrapalha.** Não está no caderno, está no Volume 2 (pergunta 3). Na p. 124 do V2, 3 das 5 filas são
  iguais às da p. 125 do caderno. O mesmo acontece nas págs. 93 e 112 do V2, que repetem as págs. 95 e 113 do
  caderno. Isso enfraquece a promessa de "120 atividades novas".
- **1 cosmético no caderno.** No "O que vem depois?" do Nível 1, há 2 filas que são a mesma fila deslocada
  uma casa (págs. 14 × 20 e 27 × 38).

Os 6 itens da rodada 2 estão corrigidos. Os 2 itens aceitos pelo dono ("Cores e códigos" nos caça-palavras e a
estrela da p. 24) não contam como pendência.

**Contagem:** bloqueia 0 · atrapalha 1 (no V2) · cosmético 1 (no caderno)

**Páginas olhadas em imagem: 149 de 149.**

- **Todas as páginas:** a 65 dpi, em pares lado a lado.
- **Gabarito (págs. 128 a 141):** de novo a 110 dpi, página por página.
- **Ampliações (100 a 150 dpi):**
  - os sóis do "Qual é diferente?" (págs. 6, 12 e 23);
  - as flores da p. 19;
  - a parte de cima da p. 59;
  - a fila 4 da p. 77;
  - os dois quadros da p. 97.
- **Volume 2:** olhei em imagem as págs. 93, 112 e 124 e comparei por pixel as 14 folhas de "O que vem
  depois?" do V2 com as 14 do caderno.
- **Texto:** conferido com `pdftotext -layout`.

## Itens da rodada 2

| Item | Corrigido? | Evidência |
|---|---|---|
| Buraco no caule da flor (p. 61) | Sim | O 3 está nas colunas 5 e 6 em todas as linhas de 7 a 12. Na linha 9 vai da coluna 3 à 9 e na linha 10 da coluna 2 à 6, e as duas folhas encostam no caule. O gabarito da p. 134 mostra o caule verde inteiro |
| Filas repetidas no "O que vem depois?" do Nível 1 | Sim, para as 4 filas apontadas | As 4 duplas da rodada 2 sumiram. Fila 3 da p. 32: sol/nuvem. Fila 3 da p. 45: peixe, peixe, flor. Fila 2 da p. 51: coração, estrela, estrela. Fila 1 da p. 62: maçã/balão. Nas 50 filas do N1 não ficou nenhuma igual a outra. Ficaram 2 filas deslocadas: ver Achados |
| Convés do barquinho (p. 39) | Sim | O trecho de 14 a 6 já vem traçado na folha. A vela (6→7→…→14) e o casco (1→…→6, 14→15→1) ficam separados. No gabarito da p. 131 o convés está em preto e o contorno em laranja |
| Casa de cabeça para baixo (p. 125) | Sim | A fila 4 agora é coração, coração, coração virado (×2). A resposta única é o coração em pé, e o gabarito da p. 141 circula o coração em pé |
| Ideias no infinitivo (p. 146–147) | Sim | 14: "Lave frutas, conte colheres, arrume a mesa." 23: "Escreva ou desenhe uma cartinha…" As outras 28 ideias também estão no imperativo. "Medir com palmos" é só o título da 21 |
| Capa "Gabarito completo" (p. 1) | Sim | O rodapé da capa diz "Gabarito completo". A capa não tem mais "no final" |

## Achados

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| V2 p. 124 × caderno p. 125, V2 p. 93 × caderno p. 95, V2 p. 112 × caderno p. 113 (todas Nível 2, "O que vem depois?") | atrapalha | **Resposta à pergunta 3: é problema, e é maior que a fila do coração.** Comparei por pixel (diferença 0 a 134 px por fila, ou seja, iguais) e olhei em imagem. Em cada folha, 3 das 5 filas do V2 são iguais às do caderno, com as mesmas figuras, as mesmas opções e o mesmo "Dia N":<br>• **V2 p. 124 (Dia 29):** fila 2 (banana girando) = fila 2 da p. 125; fila 3 (coração, coração, coração virado) = fila 4; fila 4 (pássaro, pássaro, nuvem) = fila 5.<br>• **V2 p. 93 (Dia 14):** banana girando de 3 em 3 = fila 1 da p. 95; triângulo em pé/virado = fila 3; peixe, peixe, peixe virado = fila 5.<br>• **V2 p. 112 (Dia 23):** lua aberta/fechada + estrela = fila 2 da p. 113; coração girando = fila 3; barcos = fila 4. A fila 5 da p. 112 (triângulo, triângulo deitado, círculo) é a fila 1 da p. 125 do caderno.<br>As folhas de "O que vem depois?" do N1 do V2 não repetem o caderno. O V2 promete "120 atividades novas", e quem compra os dois faz 3 filas iguais no mesmo dia. A observação do `correcoes.md` ("as outras filas da folha são outras") não confere: as outras filas também se repetem | No V2, aplicar às filas de figuras do N2 a mesma checagem que já existe para "Que número falta?" (`CHECAR_JANELAS`): nenhuma fila do V2 igual ou deslocada em relação a uma fila do V1. Trocar as filas repetidas por filas novas de `CICLOS_EXTRAS` (o caderno pode ficar como está). Depois, reconferir por pixel as 14 folhas do V2 contra as 14 do caderno |
| 14 × 20 e 27 × 38 (Nível 1) | cosmético | Não há duas filas iguais, mas há 2 filas que são a mesma série deslocada uma casa (o mesmo critério do achado A2 do V2 na rodada 2):<br>• fila 3 da p. 14 (flor, balão, balão…, resposta flor) e fila 3 da p. 20 (balão, balão, flor…, resposta balão);<br>• fila 1 da p. 27 (maçã, coração…, resposta maçã) e fila 2 da p. 38 (coração, maçã…, resposta maçã)<br>A resposta muda e a criança dificilmente percebe | Opcional: em `sem_repetir_filas` do N1, comparar as filas como ciclos (qualquer rotação da sequência conta como repetida) e trocar a 2ª ocorrência por uma fila de `CICLOS_EXTRAS_N1` |

## O que conferi de novo e está certo

### Estrutura

- **Capa, "Como usar" e sumário:**
  - O "Como usar" aponta o plano do N1 na p. 5, o do N2 na p. 67 e o gabarito a partir da p. 128.
  - O sumário aponta as págs. 2, 4, 66, 128, 142, 146 e 148.
  - Tudo bate com as páginas.
- **Planos (págs. 5 e 67), por script:**
  - Há 60 + 60 entradas, que cobrem exatamente as págs. 6 a 65 e 68 a 127.
  - O título de cada entrada bate com o da folha.
  - O "Dia N" do rodapé de cada folha bate com o plano (0 erros nos 60 dias).
- **Gabarito:**
  - Tem 120 miniaturas, uma para cada página de 6 a 65 e de 68 a 127, sem falta e sem repetição (script).
  - O título e o nível de cada miniatura batem com os da folha.

### As 120 respostas

- **Sudokus de figuras do N1 (págs. 18, 34, 49 e 64):** resolvi os 4 à mão. Cada um tem uma solução só, e
  ela é igual à do gabarito.
- **Sudokus 6x6 (págs. 69, 84, 99, 111 e 127), por script:**
  - Os 5 têm solução única, com 20, 18, 17, 16 e 15 pistas.
  - O gabarito bate casa a casa.
- **"O que vem depois?":**
  - Conferi uma a uma as 50 filas do N1 e as 20 do N2.
  - Cada fila tem uma resposta só, ela está entre as opções e o gabarito circula a certa.
  - Inclui as filas novas das págs. 32, 45, 51, 62 e 125.
- **"Que número falta?":** as 36 filas estão certas no gabarito.
  - p. 70: 6, 22, 22, 15, 52 e 12.
  - p. 83: 13, 44, 21, 23, 18 e 17.
  - p. 88: 20, 48, 37, 37, 4 e 24.
  - p. 101: 8, 56, 44, 14, 19 e 17.
  - p. 106: 31, 38, 16, 16, 15 e 46.
  - p. 119: 82, 25, 33, 29, 22 e 46.
- **Caça-palavras (págs. 73, 93, 108 e 122), por script:**
  - Testei as 8 direções. As 32 palavras aparecem uma vez cada, só para a direita, para baixo ou na diagonal,
    como a instrução diz.
  - O realce do gabarito bate.
- **Códigos secretos:** BRINCAR FAZ BEM (p. 78), BOM TRABALHO (p. 103) e SUPER DESAFIO (p. 116).
- **Grades lógicas:** cada uma tem resposta única, e o gabarito está certo.
  - p. 80: Ana come banana, Beto come maçã e Caio come uva.
  - p. 96: Lia brinca com o barquinho, Téo com o carrinho e Rui com o balão.
  - p. 115: Duda desenhou a estrela, Enzo a lua e Bia o sol.
- **Contagens:** batem com o gabarito.
  - "Conte e circule" do N1 (20 quadros), por exemplo: p. 29 com 2, 4, 3 e 5; p. 36 com 3, 7, 5 e 8; p. 42
    com 7, 8, 5 e 3; p. 48 com 4, 5, 7 e 9.
  - "Quantos tem?": p. 81 com 9, 9 e 8; p. 98 com 8, 7, 8 e 3; p. 114 com 5, 4, 7 e 8.
- **Diferenças:**
  - "Ache as 5 diferenças" (págs. 53, 59 e 65): cada uma tem 5 diferenças, e o gabarito circula as 5. Na
    p. 59, a 5ª é o raio de cima do sol (conferi ampliado e por diferença de pixels).
  - "Jogo dos 7 erros" (págs. 68, 85, 97, 110 e 126): cada um tem 7 diferenças, e o gabarito circula as 7.
- **Figura diferente:**
  - "Qual é diferente?" do N1 (8 folhas) e "Encontre a diferente" do N2 (4 folhas): há uma diferente por fila
    ou quadro, e o gabarito marca a certa.
  - Os sóis diferentes estão sem o raio de cima, o que se vê bem ampliado.
- **Memória:**
  - "Olhe e lembre": todas as figuras de cima estão entre as opções. No N2, o gabarito dá 5, 6, 6, 7 e 8, e
    confere.
  - "Onde estava?": as posições do gabarito estão certas.
- **Pinte pelo código:**
  - Os 9 aparecem pintados no gabarito.
  - No peixe da p. 86, todas as contas dão 1, 2, 4 ou 6, que são as cores da legenda.
- **Ligue os pontos:**
  - Os 10 dizem "volte ao 1" e fecham no gabarito.
  - Barquinho p. 39: o convés já vem desenhado.
- **Labirintos:** os 12 têm entrada e saída, e o caminho do gabarito passa só pelos corredores.

### Impressão, português e idade

- **Impressão:** não vi texto cortado, nada fora da margem nem sobreposição. Os cinzas das diferenças, o fundo
  das pistas dos sudokus e o "✂ recorte na linha" ficam visíveis.
- **Português:** não achei erro de ortografia nem de concordância nas instruções, no bônus 1 (quadro e 6
  certificados), no bônus 2 (30 ideias, numeradas de 1 a 30) e no bônus 3 (guia, 2 páginas).
- **Idade:** no N1, nenhuma atividade pede que a criança leia; as instruções são para o adulto ler em voz
  alta. O ligue até 20 tem a ajuda do adulto depois do 10.
