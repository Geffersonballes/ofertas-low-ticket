# Revisão do caderno "Dez Minutinhos": páginas 66 a 149

Arquivo: `produto/final/dez-minutinhos.pdf` (149 págs., A4). Revisado em 2026-11-28.

**Resumo**
1. Nenhuma atividade do Nível 2 está impossível. Os 5 labirintos têm saída e caminho único (o gerador faz labirinto perfeito). Os 5 jogos têm 7 erros cada, conferidos por diferença de pixels. Os 5 sudokus 6x6 têm solução única (resolvidos por script). Os 3 códigos secretos e os 4 caça-palavras estão completos, e as 3 grades lógicas têm resposta única. O plano de 30 dias aponta todas as páginas certas.
2. O gabarito cobre as 120 atividades, sem repetir nenhuma, e cada "Pág. N" bate com o título da página. Todas as 60 respostas do Nível 2 conferem. Uma falha atinge os dois níveis: o gabarito dos 9 "Pinte pelo código" sai **sem as cores**, idêntico à folha em branco.
3. O que atrapalha: 2 sequências numéricas ambíguas (regra alternada com o número faltando no meio) e 2 diferenças quase invisíveis (um balão espelhado e um carro espelhado). O resto é cosmético. Os 3 bônus estão completos: 6 certificados, 30 ideias contadas e guia de 2 páginas.

**Páginas olhadas em imagem: 84 de 84** (66 a 149, todas a 70 dpi). As páginas 134 a 141 (gabarito do Nível 2) também foram vistas a 130 dpi. Houve recortes ampliados das págs. 77, 85, 89, 105, 110, 126 e 136. O texto foi conferido com `pdftotext -layout`.

Contagem: **bloqueia 0 · atrapalha 5 · cosmético 10**

| Página | Gravidade | Problema | Sugestão de correção |
|---|---|---|---|
| 128 a 134 e 136 (gabarito das págs. 10, 16, 24, 30, 40, 47, 55, 61 e 86) | atrapalha | Os 9 "Pinte pelo código" (8 do N1 e 1 do N2) aparecem no gabarito **sem nenhuma cor**, iguais à atividade. Visto na pág. 136 (p. 86) a 220 dpi e nas demais a 70 dpi. Causa em `gerador/atividades2.py`, `pinte_codigo()`: o gabarito monta `"".join(gab) + base`, e os quadradinhos brancos (`fill="#fff"`) de `base` cobrem os retângulos coloridos. | Desenhar as cores **depois** da base (`base + "".join(gab)`), ou tirar o `fill="#fff"` das casas com número na versão do gabarito. Gerar de novo e conferir as 9 miniaturas. |
| 106 (fila 5) | atrapalha | Sequência **1 › 5 › ○ › 12 › 15**, com a regra alternada "+4, +3" e o número faltando no meio. Tanto 8 (+4 +3 +4 +3) quanto 9 (+4 +4 +3 +3) parecem padrão para uma criança de 7 a 10 anos. O gabarito só aceita 8. | Na regra "alterna", deixar o número faltando só na última posição (`falta = 4`), ou trocar por uma regra de soma simples. |
| 119 (fila 2) | atrapalha | Mesmo problema: **7 › 11 › ○ › 20 › 25** com a regra "+4, +5". Cabem 16 (+4 +5 +4 +5) e também 15 (+4 +4 +5 +5). O gabarito diz 16. | Mesma correção da linha acima. |
| 85 | atrapalha | Jogo dos 7 erros: um dos 7 erros é o **2º balão espelhado**. O balão é simétrico, então só o rabinho do barbante muda. Na folha impressa (cerca de 1 cm) quase não dá para ver, e a criança fica procurando o 7º erro. Os outros 6 são bons (balão cinza, árvore sumida, árvore cinza, carro cinza, flor de 4 pétalas, flor cinza). | Em `diferencas()`, não usar "espelhar" em objeto quase simétrico (balão). Usar remover, cinza ou menor. |
| 105 (quadro 3) | atrapalha | "Encontre a diferente": o carro diferente (2ª fila, 4º) é só **espelhado**. Como o desenho do carro é quase simétrico, ele só foi achado por comparação de pixels. A olho, numa folha impressa, é muito difícil para 7 a 10 anos. O gabarito circula o carro certo. | Tirar o carro de `VARIANTES` com `espelhar` ou trocar por uma variante visível (sem roda, sem janela). |
| 126 | cosmético | Um dos 7 erros é a **maçã sem folha**. O erro existe, mas a folha tem uns 3 mm e está preenchida de cinza claro. É fácil de perder. | Aceitável. Se quiser, aumentar a maçã ou usar "cinza" ou "remover" nela. |
| 86 | cosmético | "Pinte pelo código" do N2 tem **todas as contas dando 6** e uma cor só (laranja). A conta nunca muda a cor, então o exercício vira só pintar a silhueta do peixe. É o único desse tipo no N2. | Usar uma arte com 2 a 4 cores (resultados diferentes), como no N1. |
| 77, 95, 113, 125 | cosmético | "O que vem depois?" repete filas inteiras entre as 4 folhas. A fila "( ) ( ) ( ) ?" aparece nas 4. "Peixe, peixe espelhado, estrela" está nas págs. 77, 95 e 125. Os pássaros aparecem iguais nas págs. 77 e 125, e os triângulos girando nas págs. 77 e 113. As respostas estão certas. | Não repetir a mesma sequência no nível (guardar as já usadas, como já é feito em `sequencias()`). |
| 69, 84, 99, 111, 127 | cosmético | A instrução e o rodapé falam em "quadradão de 6 casinhas", mas o bloco é um retângulo de 2 linhas x 3 colunas. Uma criança de 7 anos pode procurar um quadrado. | Escrever "cada bloco de 6 casinhas (2 linhas x 3 colunas, marcado com linha grossa)". |
| 73, 93, 108, 122 | cosmético | Os caça-palavras levam a etiqueta de categoria "Cores e códigos" no topo da página (e o sumário repete isso). Não combina com a atividade, só a da pág. 122 é de cores. | Usar "Atenção" ou criar a categoria "Letras". |
| 134 a 141 (gabarito do N2) | cosmético | A regra escrita no gabarito de "Que número falta?" ("soma 5", "tira 3", "+2, +3") sai em letra muito pequena e laranja. Fica legível a 130 dpi, mas no limite no A4 em P&B. | Aumentar a fonte da regra no gabarito (4,2 para cerca de 6) e usar cor escura. |
| 141 | cosmético | Gabarito da pág. 126: o círculo do balão da direita sai **cortado** pela borda do painel. | Limitar o raio e o centro dos círculos de marcação à área do painel. |
| 89 | cosmético | Ligue os pontos: os números 18 e 20 ficam colados aos pontos vizinhos (rótulo à esquerda e embaixo). Dá para fazer, mas pode confundir. | Afastar os rótulos de pontos muito próximos. |
| 143 a 145 | cosmético | O "✂ recorte na linha" sai em letra mínima e cinza claro, com risco de sumir na impressão P&B. Os certificados também têm um grande espaço vazio no meio. | Escurecer e aumentar o aviso de corte. Usar o espaço para um desenho ou uma frase. |
| 142 | cosmético | O quadro de conquistas tem 30 casas e o campo "Nível: ___", mas o caderno tem 2 níveis (60 dias). | Dizer no próprio quadro "imprima um para cada nível", ou fazer 2 quadros. |

## O que foi conferido e está certo (sem achado)

- **Abertura e plano (66–67):** os 60 itens do plano apontam a página certa, com o mesmo título da folha. Os 2 tipos de cada dia são sempre diferentes, como diz o guia.
- **7 erros (68, 85, 97, 110, 126):** cada um tem exatamente 7 diferenças, conferidas por diferença de pixels entre os dois painéis. O gabarito circula as 7 em todos.
- **Sudokus 6x6:** todos com solução única, e o gabarito bate casa a casa com a solução calculada.
  - Pág. 69: 20 pistas.
  - Pág. 84: 18 pistas.
  - Pág. 99: 17 pistas.
  - Pág. 111: 16 pistas.
  - Pág. 127: 15 pistas.
- **Que número falta? (70, 83, 88, 101, 106, 119):** as 36 filas foram conferidas contra o gabarito e estão todas certas. As duas ambíguas estão na tabela.
- **Caça-palavras (73, 93, 108, 122):** as 32 palavras estão na grade, cada uma uma vez só, conferidas por script. Todas seguem as direções que a instrução promete (para o lado, para baixo ou na diagonal ↘).
- **Código secreto:** todas as figuras estão na tabela e o gabarito bate.
  - Pág. 78: BRINCAR FAZ BEM.
  - Pág. 103: BOM TRABALHO.
  - Pág. 116: SUPER DESAFIO.
- **Grades lógicas (80, 96, 115):** cada uma tem solução única. O gabarito traz banana, maçã e uva (p. 80), barquinho, carrinho e balão (p. 96) e estrela, lua e sol (p. 115).
- **Quantos tem?:** contei na imagem e a contagem bate com o gabarito.
  - Pág. 81: 9 estrelas, 9 corações e 8 luas.
  - Pág. 98: 8 maçãs, 7 uvas, 8 bananas e 3 flores.
  - Pág. 114: 5 peixes, 4 barcos, 7 sóis e 8 nuvens.
- **Olhe e lembre (72, 87, 92, 109, 123):** todas as figuras de cima aparecem nas opções. O gabarito dá 5, 6, 6, 7 e 8, que confere.
- **Onde estava? (79, 102, 117):** as figuras e as posições do gabarito estão certas.
- **Encontre a diferente (74, 91, 105, 120):** há uma figura diferente por quadro, e o gabarito está certo. O carro da pág. 105 está na tabela.
- **O que vem depois?:** as 20 filas têm a resposta entre as opções e o gabarito está certo.
- **Labirintos (75, 90, 104, 121), ligue os pontos (76, 89, 100, 112, 124) e copie o desenho (71, 82, 94, 107, 118):** todos têm entrada e saída abertas e numeração completa (1 a 24, 28, 32, 34 e 40). O gabarito mostra o traço completo.
- **Gabarito (128–141):** 120 miniaturas, sem faltar nem repetir nenhuma página de 6 a 65 e de 68 a 127. O título de cada miniatura bate com o da atividade.
- **Bônus:**
  - Quadro de conquistas (p. 142): 30 casas.
  - 6 certificados (p. 143–145): semanas 1 a 4, Nível 1 e Nível 2.
  - "30 ideias longe da tela" (p. 146–147): contei 30, numeradas de 1 a 30.
  - "Guia do adulto" (p. 148–149): 2 páginas.
  - Não vi erro de ortografia ou concordância no texto dos bônus.
- **Impressão:** não vi texto cortado nem fora da margem nas atividades. O cinza das diferenças (#a8a8a8) e o fundo das pistas do sudoku (#eee) continuam visíveis em P&B.
