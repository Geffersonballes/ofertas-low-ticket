# Revisão — Volume 2 (bump) e promessa da página × produto

Data: 2026-11-28 · Revisor de qualidade · Nenhum arquivo do produto ou da página foi editado.

## Resumo

- **Volume 2 (`produto/bumps/7_volume-2/volume-2.pdf`, 140 págs. A4):** entrega o que promete.
  São **120 atividades** (60 no Nível 1, págs. 5–64; 60 no Nível 2, págs. 67–126), nas mesmas 6
  categorias e 2 níveis do caderno, com plano de 30 dias por nível (págs. 4 e 66) e gabarito
  (págs. 127–140). **Nenhuma atividade inteira repete o caderno principal.** Conferi assim: texto de
  todas as páginas, comparação de imagem de cada página do V2 com todas as páginas de atividade do
  V1, sudokus 6x6 casa a casa, caça-palavras, mensagens dos códigos, artes de pintar e desenhos de
  ligar pontos. Todos os temas e desenhos são novos. O que repete são **linhas soltas de "Que número
  falta?"** (4 linhas iguais ao V1, e 2 séries que aparecem 3 vezes no próprio V2).
- **Plano → página:** os 120 links dos dois planos batem com o título e com o "Dia N" do rodapé
  (conferido por script nos dois PDFs). Rodapés batem com o número real da página.
- **Gabarito:** os 120 itens estão lá. Os 5 sudokus 6x6 são válidos e batem com as casas dadas;
  os 4 sudokus de figuras, os 3 problemas de lógica, os 3 códigos (MUITO BEM, QUE LEGAL, CONTINUE
  ASSIM), as 4 contagens "Quantos tem?", as 36 sequências, os 8 + 3 caça-palavras (cada palavra
  aparece uma vez, em linha reta) e os erros/diferenças que contei estão certos. **Não achei
  resposta errada.** Ponto fraco, aqui e no caderno principal: o gabarito de "Pinte pelo código"
  só repete a grade com números, sem mostrar o desenho pintado.
- **Página de vendas × caderno principal:** quase tudo confere: 120 atividades, 60/60, 2 níveis,
  2 planos de 30 dias, gabarito, A4, preto e branco, 14 folhas por semana, os tipos citados e os 3
  bônus com o conteúdo descrito. **Não confere:** as imagens da seção "Veja por dentro"
  (`dentro-1` a `dentro-6`), `amostra-nivel1/2.jpg` e o `folheando.gif`. Elas vêm do PDF de amostra
  (18 págs.), não do caderno vendido, e a página diz "Páginas de verdade do caderno". Confere em
  parte: "gabarito completo / todas as respostas" e "instrução em uma linha".
- **Olhei em imagem 57 páginas do Volume 2:** 1–10, 14, 17, 22, 27, 50, 52, 64–68, 70, 72, 73, 77,
  79, 80, 85–87, 92, 98, 100, 102, 104, 107, 111, 113, 115, 120, 122, 123, 126 e o gabarito inteiro
  (127–140), mais ampliações de 9 trechos. No caderno principal olhei 9 páginas (1, 5, 6, 7, 67,
  118, 129, 142, 143), as 6 imagens `dentro-*`, as 2 `amostra-nivel*`, os mockups e quadros do GIF.
  O resto foi conferido com `pdftotext`/`-bbox` e scripts.

Contagem da parte A: **bloqueia 0 · atrapalha 4 · cosmético 6.**

## Parte A — Volume 2

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 9, 15, 23, 29, 40, 45, 54, 60, 85 (gabarito nas págs. 127–135) | atrapalha | O gabarito de "Pinte pelo código" é só a grade com os números, igual à folha. Não mostra o desenho pintado e não ajuda a conferir. No N2 (p. 85) mostra as contas sem o resultado. O caderno principal tem o mesmo problema (ex.: gabarito da p. 16, na p. 129). | Pintar as casas com a cor do resultado no gabarito (ou escrever o número do resultado no N2). Corrigir no gerador, para valer nos dois PDFs. |
| 14, 26, 50, 62, 75, 87, 100, 123 (gabarito 128–139) | atrapalha | Em "Ligue os pontos" o último número não volta ao 1, e o desenho fica aberto. Ex.: castelo p. 50 (falta o trecho 23→1 no chão), pipa p. 14 (10→1), pinheiro p. 62 (23→1), borboleta p. 123 (40→1). O gabarito também fica aberto. O caderno principal tem o mesmo (casinha, gabarito p. 129). | Repetir o "1" no fim ou trocar a instrução por "Ligue do 1 ao N e volte ao 1". |
| 69, 82, 99, 106, 118 | atrapalha | "Que número falta?": 4 linhas são idênticas ao Volume 1, com a mesma lacuna: 26-21-16-11 (V1 p. 70), 5-10-_-40-80 (V1 p. 88), 1-10-19-28 (V1 p. 88), 1-2-_-8-16 (V1 p. 88/101). No próprio V2, a série 5-10-20-40-80 aparece 3 vezes (p. 82, 99, 106), 1-2-4-8-16 aparece 3 vezes (p. 99, 106, 118) e 19-24-29-34 aparece 2 vezes (p. 69, 88). Não é uma atividade repetida, mas enfraquece o "nenhuma repetida". | Sortear as séries de "dobra" com outro início (3, 4, 6…) e impedir linha repetida entre os volumes. |
| 27 (gabarito 129) | atrapalha | Labirinto barco→ilha (6x8) sem desafio: o caminho é a coluna da esquerda direto para baixo e a última linha até a saída. O miolo do labirinto não é usado. | Gerar de novo com outra semente ou exigir caminho com um número mínimo de curvas. |
| 38, 111 | cosmético | Guarda-chuva com contorno aberto: falta a metade esquerda da borda de baixo da cobertura, e o ponto 1 fica solto. | Fechar a borda da cobertura no desenho `guarda-chuva`. |
| 123 | cosmético | A "borboleta" de 40 pontos é só o contorno das asas, sem corpo. Fica parecendo um trevo. | Aceitar ou pôr o corpo como traço pronto. |
| 2 | cosmético | "nos mesmos seis tipos do caderno principal": são 6 categorias com ~20 tipos de atividade. | "nas mesmas seis categorias". |
| 80, 96, 114 | cosmético | As grades lógicas mudam crianças e respostas, mas repetem o formato e os itens do V1 ("Quem come o quê?" maçã/banana/uva; "Quem brinca com o quê?" balão/carrinho/barquinho). Os problemas são outros. | Opcional: itens novos (ex.: brinquedos, bichos). |
| 22, 120 | cosmético | Labirinto "Leve o carro até a árvore" repete a dupla início/fim do V1 (V1 p. 52 e N2). O labirinto é outro. | Opcional: trocar a dupla. |
| 70, 81, 94, 105, 117 | cosmético | Em "Copie o desenho" o modelo fica sempre encostado nas 2–3 colunas da esquerda da grade (o mesmo no V1). | Centralizar o modelo na grade. |

Conferido sem problema: capa e "Como usar" (páginas citadas 4, 66 e 127 corretas), 2 aberturas,
rodapés "Dia N · Feito!", fontes embutidas, A4, margens, preto e branco (as diferenças dos jogos de
erros aparecem em cinza, e o cinza sai na impressão), `volume-2.zip` igual ao PDF (md5 conferido),
português das instruções e títulos.

## Parte B — Promessas da página e dos anúncios × caderno principal (`produto/final/dez-minutinhos.pdf`, 149 págs.)

| Promessa | Onde aparece | Confere? | Evidência (página do PDF) |
|---|---|---|---|
| 120 atividades | Título/subtítulo, botões, seção 6, oferta, barra fixa, todos os roteiros | sim | 120 páginas com "Dia N · Feito!": 6–65 e 68–127 |
| 60 atividades no Nível 1 + 60 no Nível 2 | Seção 6, oferta | sim | N1 6–65; N2 68–127; aberturas p. 4 e 66 |
| 2 níveis: 4 a 6 anos (sem leitura) e 7 a 10 anos (leitura inicial) | Topo, seção 3, FAQ, roteiros 3 e 5 | sim | p. 2, 4, 66; selos em toda página |
| Nível 1: "instrução em uma linha para o adulto ler" | Seção 5, FAQ "Serve para qual idade?" | parcial | A maioria tem 1 linha. "Pinte pelo código" (ex.: p. 10) e "Olhe e lembre" (ex.: p. 11) têm 2 linhas. O "você lê em voz alta" está na p. 2 |
| Plano de 30 dias, 2 folhas por dia, "cada dia já diz quais folhas imprimir" | Topo, seções 3, 6 e 9, roteiros 1, 2, 4 e 5 | sim | Planos N1 p. 5 e N2 p. 67. Os 120 links batem com título e "Dia N" (script) |
| Cada dia junta dois tipos diferentes, "sem repetir" | Seção 3, roteiro 4 | sim | Nos dois planos as 2 folhas do dia são de categorias diferentes. Nenhuma página aparece duas vezes |
| Imprimir a semana: 14 folhas | Seção 3, FAQ | sim | 1 atividade por folha. p. 2, p. 149 |
| Gabarito "no fim" | Topo, seção 3, FAQ | parcial | Gabarito nas p. 128–141, mas os bônus vêm depois (p. 142–149) |
| Gabarito completo, "todas as respostas" | Seção 4, 6 e 9, roteiros | parcial | Os 120 itens estão nas p. 128–141. "Pinte pelo código" mostra só a grade, sem o desenho pintado (ex.: p. 129). "Siga o caminho" diz "atividade livre" |
| Imprime em preto e branco / "não gasta tinta à toa" | Topo, seção 6, oferta, FAQ, roteiros | sim | Atividades a traço preto. Nas legendas de cor o nome da cor vem escrito ao lado do quadradinho (ex.: p. 10). Capa e aberturas usam fundo creme bem claro (p. 1, 4) |
| PDF tamanho A4 | Topo, seção 6, oferta, roteiros 1 e 5 | sim | `pdfinfo`: 594,96 × 841,92 pt (A4) em todas as páginas |
| 6 tipos (categorias): Atenção, Memória, Padrões, Lógica, Traçado, Cores e códigos | Seção 6 | sim | Selo da categoria em cada página. `produto/sumario.md` confere com o PDF |
| Labirinto | Título, topo, seções 3 e 6, todos os roteiros | sim | N1: 8 (ex.: p. 7, 13); N2: 4 (ex.: p. 75) |
| Memória: "olhe, dobre a folha na linha e responda" | Seção 6, roteiros 1 e 4 | sim | 16 páginas (ex.: p. 11, 72, 79) com linha "dobre aqui" |
| Sudoku (de figuras no N1, 6x6 no N2) | Topo, seções 5 e 6, roteiros | sim | Figuras: p. 18, 34, 49, 64. 6x6: p. 69, 84, 99, 111, 127 (gabaritos válidos, script) |
| Código secreto (com palavras, N2) | Topo, seção 5, roteiros 1, 3 e 5 | sim | p. 78 e mais 2 páginas do N2 |
| Caça-palavras (N2) | Seções 5 e 6, roteiro 3 | sim | p. 73 (frutas), 93 (brinquedos), 108 (cozinha), 122 (cores) |
| Jogo dos 7 erros (N2) e ache as 5 diferenças (N1) | Topo, seções 5 e 6, roteiros 3 e 5 | sim | 7 erros: p. 68, 85, 97, 110, 126. 5 diferenças: p. 53, 59, 65 |
| Ligue os pontos | Topo, seções 5 e 6, roteiro 4 | sim | 10 páginas (ex.: p. 15, 76). Desenho não fecha, ver parte A |
| Padrões / sequências para completar | Seção 6, roteiros 3 e 4 | sim | "O que vem depois?" (ex.: p. 8) e "Que número falta?" (ex.: p. 70) |
| Qual é diferente, conte e circule | Seção 5 e 6, roteiro 2 | sim | Ex.: p. 6 e p. 29 |
| Grades lógicas (N2) | Seção 6 | sim | p. 80, 96, 115 |
| Caminhos para seguir com o lápis | Seção 6 | sim | "Siga o caminho", ex.: p. 9 |
| Pinte pelo código | Seção 6 | sim | N1: 8 páginas (ex.: p. 10). N2: 1 com contas (p. 86) |
| Bônus 1: quadro de conquistas (cada dia do plano) + 6 certificados | Seções 3, 7 e 9, roteiro 4 | sim | Quadro com 30 dias p. 142. Certificados p. 143–145 (semanas 1–4, Nível 1, Nível 2) |
| Bônus 2: 30 ideias longe da tela sem imprimir nada | Seção 7 e 9, FAQ, roteiro 5 | sim | p. 146–147: 30 ideias, "Nada aqui precisa ser impresso" |
| Bônus 3: guia do adulto de 2 páginas (apresentar, quando parar, passar do Nível 1 para o 2) | Seção 7 e 9 | sim | p. 148–149, com os três temas |
| Pode imprimir quantas vezes quiser (uso familiar) | Seção 4, oferta, FAQ | sim | p. 2 |
| "Páginas de verdade do caderno, do jeito que saem na impressora" (6 imagens `dentro-1` a `-6`) | Seção 5 ("Veja por dentro") e tira Seg–Dom da seção 2 | **não** | As 6 imagens vêm de `produto/amostra/dez-minutinhos-amostra.pdf`, não do caderno. Ex.: "Caça-palavras: bichos" (GATO, CAVALO…) não existe no caderno (temas reais: p. 73, 93, 108, 122). "Ligue do 1 ao 18" com sol e ondas não existe. O labirinto e o "Qual é diferente?" são diferentes das p. 7 e 6. O labirinto da imagem ainda tem o selo "Atenção" |
| Amostras de página inteira do Nível 1 e do Nível 2 | Topo (galeria) e seção 5 (`amostra-nivel1.jpg`, `amostra-nivel2.jpg`) | **não** | Também vêm do PDF de amostra. O "Código secreto" da imagem (tabela A, B, C, E, F, I, M, N, O, R, T, Z) não é nenhum dos 3 do caderno (p. 78, 103, 116) |
| GIF/vídeo "O caderno sendo folheado" | Topo e seção 3, base visual dos roteiros (`folheando.gif/.mp4`) | **não** | Os quadros mostram páginas da amostra: "Labirinto desafio" e "Caça-palavras bichos", que não existem no caderno |
| Páginas citadas nos roteiros (p. 5, 6, 7, 8, 11, 13, 15, 18, 68, 69, 73, 75, 78, 128, 142, 143, 146) | `criativos/roteiros.md` | sim | Cada número aponta para o tipo dito no roteiro (conferido com `sumario.md` e com o texto do PDF) |
| Número total de páginas | — | não citado | A página e os anúncios não citam número de páginas (o PDF tem 149) |

### Observação para o operador

A correção da parte B fica na página, não no produto: refazer `dentro-1` a `-6`, `amostra-nivel1/2`
e o `folheando.gif/.mp4` a partir de `final/dez-minutinhos.pdf`, ou trocar o texto da seção 5.
Os roteiros já apontam para páginas do PDF final, mas usam o `folheando.mp4` atual, que mostra a
amostra.
