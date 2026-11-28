# Revisão dos order bumps 1 a 6 — rodada 2 — 2026-11-28

Base: `bumps-1-a-6.md` (rodada 1) e `correcoes.md` desta pasta. Arquivos: `produto/bumps/<n>_<slug>/<slug>.pdf`.
Nenhum arquivo do material foi editado.

## Resumo

- **Veredito: NÃO LIMPA (só cosméticos).** Nenhum achado novo bloqueia ou atrapalha o uso. Sobram 13 cosméticos
  novos. Pela regra do dono ("corrigir todos os itens, inclusive os cosméticos"), a revisão ainda não sai limpa.
- **Itens da rodada 1: os 28 foram corrigidos** (tabela abaixo). Nenhum ficou pendente. Dois deles geraram
  efeitos colaterais pequenos, listados como achados novos: bump 2, pág. 40, e bump 4, págs. 42–58.
- **Páginas olhadas em imagem: 231 de 231.** Bump 1: 20/20 · Bump 2: 47/47 · Bump 3: 10/10 · Bump 4: 73/73 ·
  Bump 5: 69/69 · Bump 6: 12/12. Renderizei todas a 55 dpi (`pdftoppm -r 55`) e olhei em folhas de 4 páginas
  sem reduzir. Ampliei os pontos críticos de 80 a 150 dpi: quebra-cabeças do bump 2 (págs. 3 e 13), ícone do
  pato (pág. 35) e ícone da faca no bump 5 (pág. 13). Todo o texto também foi conferido com `pdftotext -layout`.
- **Conferido por script:** 140 contas do gabarito do bump 4, sem erro. Os 5 caça-palavras (bump 1 frutas;
  bump 5 casa, roupas, doces e brincadeiras) têm cada palavra uma vez só. Os 6 `.zip` têm 1 PDF cada, igual
  byte a byte (md5) ao PDF da pasta.
- **Medido:** a figura-guia dos quebra-cabeças do bump 2 agora tem cinza ≈ 169/255 (cerca de 34% de tinta;
  antes ≈ 225). As ligações da trilha (bump 6) têm ≈ 119/255 (#777).
- **Português:** não achei erro de ortografia, acento nem concordância nos 6 bumps. Li o bump 5 palavra por
  palavra: instruções, 30 palavras do "Qual vogal falta?", sílabas, rimas, frases e gabaritos.

| Bump | Prometido (`bumps/bumps.md`) | Real | Págs. prometidas × reais | Bloqueia | Atrapalha | Cosmético |
|---|---|---|---|---|---|---|
| 1 Para levar na bolsa | 30 atividades A5, 2 por folha, gabarito em 4 folhas | 30 (15 N1 + 15 N2) em 15 folhas A4 deitadas + capa/como usar + 4 de gabarito | 20 × 20 | 0 | 0 | 0 |
| 2 Recortar e colar | 40, nos dois níveis | 40 (20 N1 págs. 3–22 + 20 N2 págs. 23–42) + 5 de gabarito | 47 × 47 | 0 | 0 | 3 |
| 3 Cartas de conversa | 48 perguntas, 4 categorias de 12 | 48 (12 Meu dia, 12 Imaginação, 12 E se…?, 12 Preferidos), 6 por folha | 10 × 10 | 0 | 0 | 2 |
| 4 Matemática brincando | 60, nos dois níveis + fichas | 60 (30 N1 págs. 4–33 + 30 N2 págs. 34–63) + fichas (pág. 3) + 10 de gabarito | 73 × 73 | 0 | 0 | 1 |
| 5 Letras e palavras | 60 (N1 vogais/1ª letra; N2 sílabas, palavras, rimas, frases) | 60 (30 N1 págs. 3–32 + 30 N2 págs. 33–62) + 7 de gabarito | 69 × 69 | 0 | 0 | 6 |
| 6 Jogos de mesa | 5 jogos, regras numa página | bingo 6 cartelas + 16 fichas; dominó 28 peças; memória 24 cartas (12 pares); trilha 30 casas + 4 peões + dado; velha 2 tabuleiros + 10 peças; regras na pág. 2 | 12 × 12 | 0 | 0 | 1 |
| **Total** | | | 231 × 231 | **0** | **0** | **13** |

---

## (a) Itens da rodada 1

| Item | Corrigido? | Evidência |
|---|---|---|
| B1 · pág. 1: "folha" usada em dois sentidos (cosm.) | Sim | "Cada folha A4 traz duas atividades". "Meias folhas 1 a 15: Nível 1". Rodapés das A5 com "meia folha N". Gabarito com "Meia folha N · N1 · …" |
| B1 · págs. 17–20: gabarito sem aviso de corte (cosm.) | Sim | "Como usar", item 5: "Gabarito nas últimas páginas, em folha A4 inteira: essas não precisam ser cortadas." |
| B2 · pág. 6: ilha em "Na água" (atrap.) | Sim | Peças da pág. 6: passarinho, pato, balão, peixe, sol e polvo. A ilha saiu. No gabarito (pág. 43), o polvo está em "Na água" |
| B2 · págs. 3, 8, 13, 17, 21: figura-guia muito clara (atrap.) | Sim | Guia com cinza ≈ 169/255 (medido na pág. 3 a 100 dpi; antes ≈ 225). Continua mais clara que as peças pretas. Aparece bem em P&B nas 5 páginas |
| B2 · pág. 21: mastro na linha de corte (cosm.) | Sim | O mastro está ≈ 10 mm à esquerda da linha do meio. A peça com o mastro mostra a vela inteira junto, e nenhuma peça ficou só com um filete |
| B2 · pág. 4: sombra da lua só contorno (cosm.) | Sim | A lua da sombra agora é uma silhueta preta preenchida, como as outras |
| B2 · págs. 27, 32: contas até 10 no N2 (cosm.) | Sim | Pág. 27: 2+17, 19+1, 7+5, 13+4, 1+15. Pág. 32: 13−7, 20−10, 18−10, 2−1, 10−7. Ver o achado novo da pág. 40 |
| B2 · BALÃO 3× e OVO 2× em "Monte as palavras" (cosm.) | Sim | 15 palavras diferentes nas 5 folhas: OVO, BANANA, CORAÇÃO / ANEL, COPO, BALÃO / BARCO, DADO, ILHA / SORVETE, PÁSSARO, LUA / ESTRELA, BOLA, ÁRVORE |
| B2 · pág. 30: flor em "Na natureza" (cosm.) | Sim | A flor saiu e entrou o passarinho. Peças: sol, dado, nuvem, tesoura, chave, passarinho, lápis, ilha |
| B2 · ovo liso (cosm.) | Sim | Ovo no porta-ovo nas págs. 20, 24, 25 e no gabarito |
| B3 · carta 11: "junto" (cosm.) | Sim | "…que a gente já fez juntos?" (pág. 4) |
| B3 · carta 47: frase truncada (cosm.) | Sim | "Doce ou salgado? Qual é o seu doce preferido? E o salgado?" (pág. 10) |
| B3 · cartas 35 e 45: "de hoje" / "para amanhã" (cosm.) | Sim | "E se você pudesse escolher um jantar? O que seria?" e "Se você pudesse escolher um passeio, qual seria?" Ver o achado novo da carta 35 |
| B4 · págs. 9, 16: "de 1 até 10" (atrap.) | Sim | Agora diz "de 1 até 20". As fileiras vão de 1 a 20, e o gabarito (págs. 64 e 66) também |
| B4 · págs. 23, 30: "de 1 até 20" (atrap.) | Sim | Agora diz "de 1 até 40". São 4 fileiras até 40, e o gabarito (págs. 67 e 68) também |
| B4 · págs. 9, 16: figuras soltas sem instrução (cosm.) | Sim | "Terminou? Pinte as figuras:" acima das 5 figuras |
| B4 · págs. 34, 35: primeiras contas do N2 até 10 (cosm.) | Sim | Títulos "Contas de somar (aquecimento)" e "Contas de diminuir (aquecimento)", e instrução "Aquecimento com contas até 10." Ver o achado novo das págs. 42–58 |
| B4 · págs. 39, 47, 55, 61: preço em laranja (cosm.) | Sim | "N fichas" em preto nas 4 tabelas de preços |
| B4 · págs. 64–70: gabarito com miniaturas pequenas (cosm.) | Sim | Gabarito com 2 por linha nas págs. 64–73. O bump tem 73 páginas, como diz `bumps/bumps.md`. O "Como usar" não cita a página do gabarito |
| B5 · pág. 44: duas rimas certas (atrap.) | Sim | BALÃO–AVIÃO, JANELA–PANELA, DADO–LADO, MEIA–AREIA, SAPO–PAPO. Cada par tem um final próprio, e só uma ligação dá certo |
| B5 · pág. 51: duas rimas certas (atrap.) | Sim | UVA–LUVA, GATO–PATO, COPO–TOPO, MEL–PAPEL, CASA–ASA. Conferi também as págs. 37 (DEDO–MEDO, MALA–SALA, LUA–RUA, CANECA–BONECA, CHAVE–NAVE) e 58 (FLOR–CALOR, NARIZ–GIZ, PIPOCA–MINHOCA, CAMA–LAMA, BOLA–COLA): nenhuma tem rima cruzada |
| B5 · pág. 41: só palavras de 2 sílabas (cosm.) | Sim | FLOR (1) e PÁSSARO (3) junto com 6 palavras de 2 sílabas. As págs. 34, 48 e 55 também misturam 1, 2 e 3 |
| B5 · "Qual vogal falta?" com palavras repetidas (cosm.) | Sim | São 30 palavras diferentes nas págs. 7, 13, 19, 25 e 29 (entraram FACA, MESA, LIVRO, MALA, MEIA e VELA). As 30 vogais do gabarito estão certas. Ver o achado novo dos ícones |
| B5 · ovo liso (cosm.) | Sim | Porta-ovo nas págs. 10, 16, 19, 21, 31, 34, 41, 42 e no gabarito |
| B6 · pág. 2: regra de quem começa no dominó (atrap.) | Sim | "Quem tiver uma peça com a mesma figura dos dois lados começa. Se ninguém tiver, ou se mais de um tiver, começa o mais novo." |
| B6 · pág. 12: peças da velha do tamanho da casa (cosm.) | Sim | Peças com ≈ 20 mm, menores que a casa do tabuleiro (≈ 26 mm), medido na imagem |
| B6 · págs. 2/10: número exato na trilha (cosm.) | Sim | "Não precisa tirar o número exato: quem passar da casa 30 também chega." |
| B6 · pág. 10: trilha clara em P&B (cosm.) | Sim | Ligações com ≈ 119/255 e borda grossa nas 7 casas especiais. O fundo pêssego ficou quase branco no P&B, mas a borda e o ícone identificam a casa |

Os 28 itens das tabelas da rodada 1 estão todos corrigidos.

---

## (b) Por bump

### 1. Para levar na bolsa — 30 de 30 (20 de 20 págs.)

Contagem real: 30 atividades nas meias folhas 1–15 (N1) e 16–30 (N2), duas por A4 deitado. Tipos: labirinto 6,
o que vem depois 3, conte e circule 2, qual é diferente 2, ligue os pontos 2, siga o caminho 1, sudoku de
figuras 2, sudoku 6x6 3, que número falta 3, encontre a diferente 2, quantos tem 2, código secreto 1,
caça-palavras 1. Conferidos sem problema:
- sudokus de figuras (meias folhas 6 e 13) e 6x6 (17, 23, 29);
- sequências: as alternadas (meia folha 30) têm o número que falta no fim;
- contagens (3, 10, 20 e 27);
- "BOA VIAGEM" no código secreto;
- caça-palavras de frutas (script);
- os dois "ligue os pontos" fecham o desenho no gabarito (casa e coração);
- linha de corte no meio e conteúdo longe dela.

Novos achados: nenhum.

### 2. Recortar e colar — 40 de 40 (47 de 47 págs.)

Contagem real: N1 = 20 (quebra-cabeça 4 peças ×5, sombra ×5, menor ao maior ×4, classificar ×4, complete a
fila ×2). N2 = 20 (quebra-cabeça 9 peças ×5, monte as palavras ×5, classificar ×3, ordem ×3, cole o resultado ×4).
Conferidos sem problema:
- as contas e a peça que sobra (págs. 27, 32, 37, 40);
- as ordens (26, 31, 36);
- as sílabas das 15 palavras;
- os grupos no gabarito;
- as peças dos quebra-cabeças: estão misturadas, e 9 peças em todos os de 9.

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 27, 32, 37, 40 | cosmético | Nas 4 folhas de "Cole o resultado", a peça que sobra é sempre o **21**. Na terceira folha, a criança já sabe qual peça descartar sem fazer a conta. | Sortear o distrator perto dos resultados de cada folha (ex.: resultado ± 1 ou ± 2), sem repetir. |
| 40 (e 32) | cosmético | Efeito da correção das págs. 27/32 (as contas da pág. 40 mudaram junto): a pág. 40 agora tem 3 − 1 e 2 − 1, e 2 − 1 também aparece na pág. 32. São contas de 4–6 anos num nível de 7–10. | Na pág. 40, usar contas entre 11 e 20 (como 16 − 3 e 12 − 7, que já estão lá) e não repetir 2 − 1. |
| 16, 35 (gabarito 44, 46) | cosmético | Em "Bichos ou coisas?", o pato é o mesmo ícone de patinho de banheira (corpo arredondado e sem pernas, pág. 35 ampliada). A criança pode pôr em "Coisas" (brinquedo), e o gabarito põe em "Bichos". | Nessas duas páginas, trocar o pato por um bicho sem duplo sentido (cachorro, tartaruga, borboleta), ou desenhar o pato com pernas. |

### 3. Cartas de conversa — 48 de 48 (10 de 10 págs.)

Contagem real: 48 cartas numeradas de 1/48 a 48/48, 12 por categoria, 6 por folha nas págs. 3–10, com linha
tracejada em todas. Nenhuma pergunta invasiva.

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 8 (carta 35) | cosmético | Efeito da correção: "E se você pudesse escolher um jantar? O que seria?" saiu do tom da categoria. A pág. 2 define "E se…?" como "situações malucas", e essa virou uma pergunta de preferido, quase igual à carta 46 ("Qual comida você comeria todo dia?"). | Trocar por uma situação maluca sem pedido para o dia, ex.: "E se o jantar caísse do céu como chuva? O que você queria que caísse?" |
| 2 | cosmético | "E se…? situações malucas para pensar junto." A carta 11 foi corrigida para "juntos", e aqui ficou "junto". | "…para pensar juntos." |

### 4. Matemática brincando — 60 de 60 (73 de 73 págs.)

Contagem real: N1 = 30 (conte e escreva 5, quantos ao todo 5, quantos sobram 5, onde tem mais 4, ligue ao
número 4, complete os números 4, mercadinho 3). N2 = 30 (somar 5, diminuir 5, maior/menor 4, pirâmide 4,
dezenas 3, mercadinho 4, grupos iguais 3, que número sou eu 2). A pág. 3 tem 30 fichas (12 de 1, 8 de 2, 6 de 5
e 4 de 10, contadas na imagem). Conferidos sem problema:
- as 140 contas do gabarito (script);
- as 8 pirâmides;
- as 20 comparações;
- os 20 problemas de mercadinho;
- os grupos iguais;
- os "que número sou eu";
- as contagens das figuras e das barras de dezena.

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 42, 43, 51, 57, 58 | cosmético | Efeito da correção das págs. 34/35: só elas viraram "aquecimento", mas as folhas normais seguintes têm contas mais fáceis que o aquecimento. A pág. 43 tem 9 − 8, 3 − 1, 2 − 1, 7 − 6, 4 − 2 e 3 − 2 (10 das 12 contas até 10). Também há 2 + 1 (42), 2 − 1 (51), 1 + 1 (57) e 2 − 1 e 7 − 6 (58). O título "aquecimento" faz o adulto esperar que o resto seja mais difícil. | Nas folhas sem "aquecimento", exigir pelo menos uma parcela ≥ 10 em cada conta (até 30, como promete). Usar um rng derivado só para essas contas, para não mexer nas outras páginas. |

### 5. Letras e palavras — 60 de 60 (69 de 69 págs.)

Contagem real: N1 = 30 (letra A/E/I/O/U 5, com que letra começa 6, ligue à primeira letra 4, ache a letra 4,
qual vogal falta 5, letras iguais 5, as cinco vogais 1). N2 = 30 (complete com a sílaba 5, quantas sílabas 4,
desembaralhe 4, caça-palavras 4, rimas 4, complete a frase 5, ordem alfabética 4). Conferidos sem problema:
- as 36 letras iniciais;
- os 20 "ligue";
- as contagens de "ache a letra", contadas na imagem (A 10, E 11, O 10, B 11);
- as 30 vogais;
- as 30 sílabas e os 2 distratores de cada folha;
- as 32 contagens de sílabas;
- os 24 desembaralhes, com as mesmas letras da palavra;
- as 4 ordens alfabéticas;
- as 20 frases;
- os 4 caça-palavras (script).

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 35, 42, 49, 56 | cosmético | "Desembaralhe" repete palavras: são 15 palavras diferentes em 24 casas. A pág. 49 repete 4 das 6 palavras já usadas (LUA, PIPA, ILHA, CHAVE), e a pág. 56 repete 5 (GATO, CASA, FLOR, TESOURA, SOL). É o mesmo caso que a rodada 1 apontou no "Qual vogal falta?". | Aplicar o mesmo "sem repetir" do `vogal_sem_repetir` (ex.: BARCO já existe; entram DADO, BOLA, PEIXE, MAÇÃ, CARRO, ÁRVORE, ESTRELA). |
| 33, 40, 47, 54, 61; 41, 48, 55 | cosmético | "Complete com a sílaba": SORVETE está em 4 das 5 folhas (33, 40, 47, 61), PATO em 3 (33, 40, 54), LÁPIS em 3 (33, 54, 61) e ANEL em 2. "Quantas sílabas?": PÁSSARO, UVA e FLOR estão em 3 das 4 folhas cada. | Sortear sem repetição no nível, como nas vogais. |
| 35, 42 | cosmético | Dois embaralhados formam outra palavra: TOGA (pág. 35, para GATO) e SACA (pág. 42, para CASA). A criança pode achar que já está certo. | Embaralhar de novo até não sair palavra conhecida nem a própria palavra. |
| 59 | cosmético | "4. O ______ nada no rio." O PATO também nada no rio e está na lista. Só se chega ao PEIXE por eliminação, depois da frase 2. | "4. O ______ vive na água e tem escamas." ou "…nada no aquário." |
| 13, 29 | cosmético | Ícones novos do "Qual vogal falta?": a FACA (pág. 13) é um traço fino com cabo cinza e, ampliada, parece um palito ou um lápis. A MALA (pág. 29) parece uma pasta ou maleta. O adulto lê a palavra, então dá para fazer, mas a figura não ajuda. | Desenhar a faca com lâmina larga e ponta arredondada e a mala com rodinhas e alça de puxar, ou trocar por palavras com ícone claro e ainda não usadas nas 30 (ex.: BOLO, FOCA). |
| 57 | cosmético | No caça-palavras "brincadeiras", PEGA, PIQUE e BOLINHA são pedaços dos nomes (pega-pega, pique-esconde, bolinha de gude). | Trocar por nomes de uma palavra só: BALANÇO, AMARELINHA, ESCONDE, GUDE, PULA (ou manter e escrever "PEGA-PEGA" na lista com o hífen fora da grade). |

### 6. Jogos de mesa — 5 de 5 (12 de 12 págs.)

Contagem real:
- bingo: 6 cartelas 3x3, todas diferentes e sem figura repetida dentro da cartela. As 16 fichas aparecem em
  pelo menos uma cartela (árvore e passarinho em uma só);
- dominó: 28 peças das 7 figuras, sem repetição nem falta;
- memória: 24 cartas, 12 pares;
- trilha: 30 casas, com estrela em 5, 13 e 22, nuvem em 9, 18 e 26, e lua em 15;
- 4 peões;
- dado com faces opostas 1–6, 2–5 e 3–4;
- velha: 2 tabuleiros, 5 estrelas e 5 corações;
- regras dos 5 jogos na pág. 2.

| Página | Gravidade | Problema | Sugestão |
|---|---|---|---|
| 2 / 10 (trilha) | cosmético | A estrela da casa 13 manda avançar 2 e leva à casa 15, que é a lua ("fique uma rodada sem jogar"). A regra não diz se a figura da casa nova também vale. É a única combinação assim no tabuleiro. | Acrescentar "A figura só vale na casa onde o dado parou", ou tirar a estrela da 13 (ex.: para a 12). |
