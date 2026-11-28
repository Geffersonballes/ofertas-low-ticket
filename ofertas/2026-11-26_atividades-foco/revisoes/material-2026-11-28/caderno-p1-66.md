# Revisão do caderno "Dez Minutinhos": páginas 1 a 66 (Nível 1) e gabarito correspondente

Data: 2026-11-28 · Arquivo: `produto/final/dez-minutinhos.pdf` (149 págs., A4)

**Resumo**
1. As 60 atividades do Nível 1 podem ser feitas. Labirintos, sudokus, sequências, contagens, memória, "qual é diferente" e "ache as 5 diferenças" conferem com o gabarito, e o plano de 30 dias aponta certo nas 60 entradas.
2. Dois defeitos se repetem em várias páginas. Os 5 "Ligue os pontos" não fecham o desenho: falta o traço do último número de volta ao 1, e no barco falta metade do convés. O gabarito dos 8 "Pinte pelo código" sai sem cor nenhuma, igual à folha em branco.
3. O resto é ajuste fino: carro espelhado sutil demais para 4 a 6 anos, legenda de cores que vira cinza em P&B, cinzas claros e detalhes de texto.

**Páginas olhadas em imagem: 73.** São as 66 páginas (1 a 66) mais as 7 do gabarito do Nível 1 (128 a 134). Também ampliei trechos das págs. 6, 12, 19, 23, 53, 59 e 65 e comparei por pixel os dois quadros das 3 "Ache as 5 diferenças". Usei o texto (`pdftotext`) para conferir o plano e o português. Nenhum arquivo do produto foi alterado.

**Contagem:** bloqueia 0 · atrapalha 6 · cosmético 7

## Problemas encontrados

| Página | Gravidade | Problema | Sugestão de correção |
|---|---|---|---|
| 15, 26, 50, 63 (gabarito 129, 130, 132, 134) | atrapalha | "Ligue do 1 ao N" em desenho fechado (casinha 1–12, coração 1–13, peixe 1–16, estrela 1–20). O desenho só fecha voltando do último número ao 1, mas a instrução manda parar no último. A casa fica sem chão, o peixe sem barriga e o coração e a estrela abertos. O gabarito também não fecha. | Em `ligue_pontos` (`gerador/atividades2.py`), repetir o ponto 1 no fim e escrever "Ligue do 1 ao N e volte ao 1". No gabarito, usar `polygon` ou fechar a `polyline`. |
| 39 (gabarito 131) | atrapalha | Barquinho 1–16: o casco não fecha. O convés vai do 6 ao 8 (no mastro) e falta o trecho do 8 de volta ao 1. O gabarito mostra o barco aberto à esquerda. | Em `DESENHOS_PONTOS["barquinho"]`, incluir o canto (30,150) depois de (100,135), ou ligar 16→1. Gerar de novo e conferir o gabarito. |
| Gabarito de 10, 16, 24, 30, 40, 47, 55, 61 (págs. 128 a 134) | atrapalha | Gabarito do "Pinte pelo código" sem cor. Os quadrados coloridos são desenhados por baixo e a grade branca (`fill="#fff"`) os cobre. Conferido ampliando o cartão da pág. 10: só a amostra da legenda é vermelha. | Em `pinte_codigo`, desenhar os retângulos coloridos depois da grade (`base + gab`) ou deixar a grade sem preenchimento no gabarito. |
| 12, 19, 23 | atrapalha | "Qual é diferente?": na fila do carro, a diferença é o carro espelhado. O desenho é quase simétrico (só a inclinação do capô muda), então para 4 a 6 anos é quase impossível de achar. O gabarito está certo: carro 2 nas págs. 12 e 19, carro 1 na pág. 23. | Trocar a variante do carro por algo bem visível (sem uma roda, ou com janela) ou tirar o carro da lista `VARIANTES` do Nível 1. |
| 10, 16, 24, 30, 40, 47, 55, 61 | atrapalha | Impresso em P&B, as amostras de cor da legenda (vermelho, amarelo, verde, azul, marrom, laranja) viram tons de cinza parecidos. A criança que não lê não sabe que cor é o número; o adulto tem de ler o nome. O "Como usar" diz que tudo funciona em preto e branco. | Pôr na legenda um desenho reconhecível de cada cor (morango = vermelho, folha = verde etc.) ou avisar no "Como usar" que nessa atividade o adulto lê o nome da cor. |
| 59 | atrapalha | Uma das 5 diferenças é a florzinha da direita com 4 pétalas em vez de 5. A flor tem uns 14 mm e a mudança é sutil para 4 a 6 anos (outra das diferenças é o sol com menos raios, que se vê bem). | Usar na flor "remover" ou "cinza", ou só aplicar a variante de pétalas em objetos grandes. |
| 63 | cosmético | Ligue os pontos até 20 está no limite para 4 anos (a numeração vai a 20). | Manter como último desafio, mas pôr "peça ajuda ao adulto nos números depois do 10" ou baixar para 15 pontos. |
| 9, 21, 33, 44, 56 | cosmético | O pontilhado do "Siga o caminho" é cinza médio (#9a9a9a) e fino, e pode ficar fraco em impressora jato de tinta econômica. | Escurecer para #6b6b6b e engrossar um pouco o traço. |
| 10, 16, 24, 30, 40, 47, 55, 61 | cosmético | Grade do "Pinte pelo código" em cinza claro (#9a9a9a, 0,35 mm). Pode sumir em P&B econômico. | Grade em #777 e 0,45 mm. |
| 11, 17, 25, 31, 41, 46, 54, 60 | cosmético | "OLHE BEM" em cinza claro (#888). Algumas figuras de cima aparecem levemente giradas (ex.: o quadrado da pág. 11) e as de baixo não, o que pode confundir quem é muito literal. | Rótulo em preto. Tirar a rotação (`girar`) das figuras de memória do Nível 1. |
| 6 a 65 (todas as "O que vem depois?") | cosmético | Instrução termina com "no ?." (ponto depois de interrogação), estranho para ler em voz alta. | "…e circule embaixo a figura que entra no quadrinho com o ponto de interrogação." |
| 3 | cosmético | O sumário diz "Nível 1 · pág. 5" e "Nível 2 · pág. 67", mas as aberturas dos níveis estão nas págs. 4 e 66 (5 e 67 são os planos). Não atrapalha. | Apontar para 4 e 66 ou escrever "plano na pág. 5". |
| 24 | cosmético | A estrela do "Pinte pelo código" (2 = amarelo) fica bem quadrada e pouco reconhecível em 12×12. | Ajustar a máscara da estrela ou trocar por outro desenho. |

## Por categoria

1. **Erros que impedem a atividade:** nada bloqueia.
   - Labirintos (7, 13, 22, 28, 37, 43, 52, 58): o gerador é de caminho único (DFS), com entrada no alto à esquerda e saída embaixo à direita, e o caminho do gabarito confere. Não vi atalho nem labirinto sem saída.
   - Sudokus (18, 34, 49, 64): resolvi os quatro à mão. Cada um tem solução única, igual à do gabarito.
   - "O que vem depois?" (10 páginas, 50 filas): todas sem ambiguidade, com a resposta certa entre as opções.
   - "Conte e circule" (29, 35, 36, 42, 48): contei os 20 quadros e batem com o gabarito.
   - "Ache as 5 diferenças" (53, 59, 65): comparei os quadros por pixel. Há exatamente 5 em cada um e o gabarito marca as 5.
   - O que atrapalha está na tabela: ligue-os-pontos aberto e carro espelhado sutil.
2. **Gabarito:** todas as 60 atividades do Nível 1 têm cartão no gabarito, e as respostas conferem. Há dois defeitos: os 8 gabaritos de "Pinte pelo código" saem sem cor e os 5 de "Ligue os pontos" mostram o desenho aberto. "Siga o caminho" tem só o texto "atividade livre", o que está certo.
3. **Plano de 30 dias (pág. 5):** conferi as 60 entradas pelo texto. Cada página citada existe, é do Nível 1, tem o tipo de atividade indicado e traz no rodapé o mesmo "Dia N" do plano. Não achei erro.
4. **Impressão:** não vi texto cortado, nada fora da margem nem sobreposição. Os pontos de atenção são os cinzas claros e a legenda de cores em P&B (na tabela).
5. **Português:** não achei erro de ortografia nem de concordância. Só a construção "no ?." (na tabela).
6. **Nível:** nenhuma atividade exige ler palavras. As instruções são para o adulto ler e as legendas de cor têm o nome escrito, que o adulto lê. Nos limites de dificuldade estão o carro espelhado, a flor de 4 pétalas da pág. 59 e o ligue-os-pontos até 20.
