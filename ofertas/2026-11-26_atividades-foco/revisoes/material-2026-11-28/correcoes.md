# Correções do material — 2026-11-28

Base: os 4 relatórios desta pasta (`caderno-p1-66.md`, `caderno-p66-149.md`, `bumps-1-a-6.md`,
`volume2-e-promessa.md`). Tudo foi corrigido no gerador (`produto/gerador/`) e nas mídias da página
(`pagina/midia/`), e os PDFs, zips, imagens e vídeos foram gerados de novo. Nenhum PDF foi editado à mão.
Nada foi publicado, enviado à Hotmart ou à Meta, e nada foi commitado.

**Regra do dono (atualizada em 2026-11-28):** corrigir todos os itens, inclusive os cosméticos. Os que
ficaram para o dono decidir estão na seção "Cosméticos para o dono decidir", com o motivo.

**Como conferi:** cada página que mudou foi renderizada a 60 dpi (`pdftoppm -r 60 -png`) e olhada em
imagem, em folhas de contato de 6 a 9 páginas. Os pontos críticos também foram vistos ampliados (90 dpi).
Para achar as páginas que mudaram, comparei cada página nova com a antiga por pixel. As conferências do
gerador rodaram em todas as gerações: contagens, sudokus com solução única, caça-palavras com cada palavra
uma vez, 7 e 5 diferenças, plano de 30 dias com categorias diferentes no dia e o novo assert das famílias
de rima. Também conferi que o rng de cada página do caderno é igual ao de antes (rastreio do estado do
rng página a página). Assim, as páginas que eu não quis mudar ficaram iguais.

## Correções

### Caderno principal (`produto/final/dez-minutinhos.pdf`, 149 págs.)

| Item | Arquivo / página | O que foi feito | Conferido em imagem |
|---|---|---|---|
| 1. Gabarito do "Pinte pelo código" sem cor (atrapalha) | `atividades2.py` `pinte_codigo` · gabarito das págs. 10, 16, 24, 30, 40, 47, 55, 61, 86 (págs. 128–136) | As casas coloridas agora são desenhadas por cima da grade (`base + gab`). Os 9 gabaritos mostram o desenho pintado | sim |
| 2. Ligue os pontos aberto (atrapalha) | `atividades2.py` `ligue_pontos` · págs. 15, 26, 39, 50, 63, 76, 89, 100, 112, 124 e o gabarito | Instrução "Ligue do 1 ao N, na ordem, e volte ao 1 para fechar o desenho". Gabarito em `polygon` (fecha) | sim |
| 2b. Barquinho sem metade do convés (atrapalha) | `DESENHOS_PONTOS["barquinho"]` · pág. 39 (gabarito na pág. 131) | Contorno fechado de um traço: casco, vela até a ponta do convés, mastro e convés. Agora tem 15 pontos | sim |
| 3. Sequências ambíguas (atrapalha) | `atividades2.py` `sequencias` · págs. 106 (fila 5) e 119 (fila 2) | Na regra alternada, o número que falta fica sempre na última casa: 1 5 8 12 ○ e 7 11 16 20 ○ | sim |
| 3b. Filas repetidas | `SEQ_USADAS` · págs. 101 e 106 | Nenhuma fila se repete no caderno. A fila repetida é trocada por outra, sorteada com um rng derivado | sim |
| 4. Carro espelhado quase igual (atrapalha) | `VARIANTES` + `icones.py` (variante `semroda`) · págs. 12, 19, 23 e 105 | O carro diferente agora está sem a roda de trás | sim |
| 4b. Balão espelhado no 7 erros (atrapalha) | `diferencas` · pág. 85 (e carro/balão em qualquer cena) | "Espelhar" em figura quase simétrica (balão, carro) vira "menor", ou "remover" se a figura for pequena | sim |
| 4c. Flor de 4 pétalas pequena (atrapalha) | `diferencas` · pág. 59 | Variante em objeto pequeno (< 16 mm, ou < 20 mm no Nível 1) vira "cinza" | sim |
| 10. Legenda de cor em P&B | `pinte_codigo` + "Como usar" (pág. 2) | Nome da cor em maiúsculas, maior e preto embaixo de cada amostra. Linha nova no "Como usar": "No Pinte pelo código, leia para a criança o nome da cor de cada número" | sim |
| 10. Grade do pinte clara (cosmético) | `pinte_codigo` | Grade #777 com 0,45 mm (antes #9a9a9a com 0,35 mm) | sim |
| 10. Pontilhado do "Siga o caminho" claro (cosmético) | `tracado` · págs. 9, 21, 33, 44, 56 | #6b6b6b com 1,6 de traço (antes #9a9a9a com 1,3) | sim |
| 10. "OLHE BEM" cinza e figuras giradas (cosmético) | `memoria_figuras` / `memoria_lugares` | Rótulo em preto. No Nível 1 as figuras de cima não giram mais (o sorteio continua, para não mudar o rng) | sim |
| 10. "no ?." (cosmético) | `padroes` · todas as "O que vem depois?" | "…circule embaixo a figura que entra no quadrinho do ponto de interrogação." | sim |
| Sumário apontava para os planos (cosmético) | `gerar_completo.py` `sumario` · pág. 3 | Nível 1 na pág. 4 e Nível 2 na pág. 66 (aberturas), com "abertura, plano de 30 dias + 60 atividades" | sim |
| Ligue até 20 no Nível 1 (cosmético) | `ligue_pontos` · pág. 63 (e pág. 50, com 16 pontos) | Instrução com "Se precisar, o adulto ajuda a achar os números depois do 10." | sim |
| Estrela quadrada no pinte (cosmético) | `_arte("estrela")` · pág. 24 | Estrela maior, com pontas mais finas. Melhorou, mas ainda tem o limite da grade 12x12 | sim |
| Maçã sem folha pequena (cosmético) | `diferencas` · pág. 126 | Pela mesma regra do 4c, virou "maçã cinza" | sim |
| Pinte do N2 com uma cor só (cosmético) | `_arte("peixe_cores")` + `sorteio_como` · pág. 86 | Peixe de 4 cores (vermelho, amarelo, azul e laranja), com contas de resultados diferentes. As contas são sorteadas como antes, para não mudar as outras páginas | sim |
| Filas repetidas no "O que vem depois?" N2 (cosmético) | `sem_repetir_filas` + `CICLOS_EXTRAS` · págs. 77, 95, 113, 125 | Nenhuma fila se repete no nível. A repetida é trocada por uma fila extra (girar ou espelhar) | sim |
| "Quadradão de 6 casinhas" (cosmético) | `sudoku6` · págs. 69, 84, 99, 111, 127 | Instrução: "…nem no bloco de 6 casinhas". Dica: "Cada linha, coluna e bloco de linha grossa (2 linhas x 3 colunas) tem 1 a 6." | sim |
| Regra pequena e laranja no gabarito (cosmético) | `sequencias` · págs. 134–141 | Regra com 6 pt (antes 4,2) e em preto | sim |
| Círculo cortado no gabarito (cosmético) | `diferencas` · pág. 141 | O centro dos círculos de marcação é limitado ao painel | sim |
| Números colados no ligue (cosmético) | `ligue_pontos` · pág. 89 (e todos os ligue) | Se o número ficar a menos de 4,5 mm de outro ponto ou número, vai para o lado com mais espaço | sim |
| "Recorte na linha" pequeno e claro, e certificado vazio (cosmético) | `.corte` + `certificados` · págs. 143–145 | Aviso de corte com 10 pt, em #444 e traço #555. No meio do certificado entram a frase "Cada dia de esforço conta. Parabéns!" e 5 figuras | sim |
| Quadro de conquistas com "Nível: ___" (cosmético) | `quadro_conquistas` · pág. 142 | Linha nova: "Imprima um quadro para cada nível: são 30 dias no Nível 1 e mais 30 no Nível 2." | sim |
| Modelo do "Copie o desenho" encostado na esquerda (cosmético) | `copie_desenho` · págs. 71, 82, 94, 107, 118 | O modelo fica centralizado na grade | sim |
| Gerador não reprodutível | `padroes` (`set` → `dict.fromkeys`) e `atv_recorte.padrao_cola` | O PDF não saía igual com outro PYTHONHASHSEED. Agora sai igual em qualquer execução | sim (md5 igual com 3 sementes de hash) |

### Volume 2 (`produto/bumps/7_volume-2/volume-2.pdf`, 140 págs.)

As correções do gerador comum (itens 1, 2, 3, 4 e 10) valem também para o Volume 2.

| Item | Arquivo / página | O que foi feito | Conferido em imagem |
|---|---|---|---|
| 1. Pinte sem cor no gabarito (atrapalha) | págs. 9, 15, 23, 29, 40, 45, 54, 60, 85 (gabarito nas págs. 127–135) | O gabarito mostra o desenho pintado. No N2, as cores mostram o resultado de cada conta | sim |
| 2. Ligue aberto (atrapalha) | págs. 14, 26, 38, 50, 62, 75, 87, 100, 111, 123 | "Volte ao 1" e gabarito fechado | sim |
| 2b. Guarda-chuva aberto (cosmético) | `bump_volume2.py` `NOVOS_PONTOS` + `TRACO_PRONTO` · págs. 38, 111 | A cobertura é um contorno fechado. O cabo já vem desenhado, e o número do ponto de encontro fica ao lado do cabo | sim |
| Borboleta sem corpo (cosmético) | `TRACO_PRONTO["borboleta"]` · pág. 123 | Corpo já desenhado no meio | sim |
| 3. Filas repetidas entre volumes e no próprio V2 (atrapalha) | `SEQ_USADAS` + `completo.json["sequencias"]` · págs. 69, 82, 88, 99, 106, 118 | O V2 lê as filas do volume 1 e não repete nenhuma, nem dentro do V2. A "dobra" ganhou outros inícios (ex.: 6 12 24 48 96) | sim |
| 4. Carro espelhado (atrapalha) | `gradesubs` · "Encontre a diferente" do N2 | Carro sem roda | sim |
| 5. Labirinto trivial (atrapalha) | `labirinto_bom` · pág. 27 (gabarito na pág. 129) | Labirinto com menos de 3 curvas no caminho é gerado de novo com um rng derivado. Só esse labirinto mudou | sim |
| "Seis tipos" (cosmético) | `como_usar` · pág. 2 | "nas mesmas seis categorias do caderno principal" | sim |
| Grades lógicas iguais ao V1 (cosmético) | `NOVOS_TEMAS_LOGICA` · págs. 96, 114 | "Quem come o quê?" com sorvete, ovo e uva. "Quem brinca com o quê?" com bola, pipa e dado | sim |
| Labirinto carro→árvore repetido (cosmético) | `pares_lab` / `labs` · págs. 22, 120 | Agora "carro → flor" (N1) e "passarinho → flor" (N2) | sim |
| Copie o desenho na esquerda (cosmético) | págs. 70, 81, 94, 105, 117 | Modelo centralizado | sim |

### Bumps 1 a 6

| Item | Arquivo / página | O que foi feito | Conferido em imagem |
|---|---|---|---|
| 6. "De 1 até 10/20" errado (atrapalha) | `atv_matematica.complete_numeros` · Bump 4, págs. 9, 16 (até 20) e 23, 30 (até 40) | A instrução é calculada do que a folha tem (`linhas * 10`) | sim |
| Figuras soltas sem instrução (cosmético) | idem · Bump 4, págs. 9, 16 | "Terminou? Pinte as figuras:" acima das figuras | sim |
| Primeiras contas do N2 até 10 (cosmético) | `atv_matematica.contas` · Bump 4, págs. 34, 35 | Título "(aquecimento)" e instrução "Aquecimento com contas até 10." Mudar o limite das contas mudaria o rng das páginas seguintes | sim |
| Preço do mercadinho em laranja (cosmético) | `mercadinho2` · Bump 4, págs. 39, 47, 55, 61 | Preço em preto, 5,4 pt | sim |
| Gabarito com miniatura pequena (cosmético) | `bumps_base.gabarito(por_pag=6)` · Bump 4 | Gabarito com 2 por linha. **O bump passou de 70 para 73 páginas** (só no gabarito, no fim). `bumps/bumps.md` foi atualizado | sim |
| 7. Rimas com duas respostas (atrapalha) | `atv_letras.RIMAS` + `FAMILIAS_RIMA` · Bump 5, págs. 37, 44, 51, 58 | Saíram FOGÃO/MAMÃO, PÃO/MÃO, SAPATO/RATO e VELA/TELA. Entraram SAPO/PAPO, DEDO/MEDO, NARIZ/GIZ e MEL/PAPEL. Cada par tem uma família de final própria, conferida por assert | sim |
| "Quantas sílabas?" só com 2 sílabas (cosmético) | `bump_letras.misturar_silabas` · Bump 5, pág. 41 | Toda folha tem palavras de 1, 2 e 3 sílabas (a pág. 41 tem FLOR e PÁSSARO) | sim |
| Palavras repetidas no "Qual vogal falta?" (cosmético) | `bump_letras.vogal_sem_repetir` + `VOGAL_EXTRAS` · Bump 5, págs. 7, 13, 19, 25, 29 | As 30 casas têm 30 palavras diferentes. Entraram 6 palavras com ícone novo: LIVRO, MESA, FACA, VELA, MEIA, MALA | sim |
| Ovo liso (cosmético) | `bumps_base.EXTRAS["ovo"]` · Bumps 2, 5 e Volume 2 | Ovo no porta-ovo | sim |
| 8. Dominó: quem começa (atrapalha) | `bump_jogos.REGRAS` · Bump 6, pág. 2 | "Quem tiver uma peça com a mesma figura dos dois lados começa. Se ninguém tiver, ou se mais de um tiver, começa o mais novo." | sim |
| Trilha: número exato (cosmético) | idem | "Não precisa tirar o número exato: quem passar da casa 30 também chega." | sim |
| Trilha clara em P&B (cosmético) | `trilha` · Bump 6, pág. 10 | Ligações em #777 e borda de 2 mm nas casas especiais | sim |
| Peças da velha do tamanho da casa (cosmético) | `velha` · Bump 6, pág. 12 | Peças de 20 mm (antes 30) com figura de 15 mm. A casa do tabuleiro tem 26 mm | sim |
| 9. Ilha em "Na água" (atrapalha) | `atv_recorte.GRUPOS` + ícone novo `polvo` · Bump 2, pág. 6 (gabarito na pág. 43) | A ilha saiu e entrou o polvo | sim |
| 9. Figura-guia clara (atrapalha) | `quebra_cabeca` · Bump 2, págs. 3, 8, 13, 17, 21 | Opacidade da guia de 0,13 para 0,38. Continua mais clara que as peças | sim |
| Mastro na linha de corte (cosmético) | ícone `barco_qc` · Bump 2, pág. 21 | Barco 9% para a esquerda, e o mastro saiu da linha do meio | sim |
| Sombra da lua só contorno (cosmético) | ícone `lua_grossa` · Bump 2, "Cada um na sua sombra" (pág. 4) | Lua mais gorda, e a silhueta preta aparece | sim |
| Contas até 10 no N2 (cosmético) | `bump_recorte` · Bump 2, págs. 27, 32 | Contas até 20 (as págs. 37 e 40 mudaram junto, porque vêm depois no sorteio) | sim |
| BALÃO e OVO repetidos (cosmético) | `bump_recorte.silabas_sem_repetir` · Bump 2, págs. 24, 29, 34, 39, 42 | 15 palavras diferentes nas 5 folhas | sim |
| Flor em "Na natureza" (cosmético) | `GRUPOS["casa_natureza"]` · Bump 2, pág. 30 | A flor saiu e entrou o passarinho | sim |
| "Folha" em dois sentidos (cosmético) | `bump_bolsa` · Bump 1, pág. 1, rodapés e gabarito | "Cada folha A4 traz duas atividades". As A5 viraram "meia folha N" no rodapé, no "Como usar" e no gabarito | sim |
| Gabarito sem aviso de corte (cosmético) | idem | "Gabarito nas últimas páginas, em folha A4 inteira: essas não precisam ser cortadas." | sim |
| Cartas 11, 47, 35 e 45 (cosmético) | `bump_cartas.py` · Bump 3, págs. 4, 8, 10 | "fez juntos". "Qual é o seu doce preferido? E o salgado?" "E se você pudesse escolher um jantar?" "Se você pudesse escolher um passeio, qual seria?" | sim |

### Página de vendas e anúncios

| Item | Arquivo | O que foi feito | Conferido em imagem |
|---|---|---|---|
| 11. Imagens do PDF de amostra | `pagina/midia/gerar_midia.py` (agora rasteriza `produto/final/dez-minutinhos.pdf` a 192 dpi) → `pagina/img/dentro-1..6.jpg`, `amostra-nivel1.jpg`, `amostra-nivel2.jpg`, `folheando.mp4`, `folheando.gif`, `folheando-poster.jpg` | Tamanhos, formatos e enquadramento iguais aos de antes (600×849, 900×1274, 720×550 com 13 s, GIF 540×413, pôster 720×551). Páginas reais equivalentes às da legenda: dentro-1 labirinto N1 (p. 7), dentro-2 qual é diferente (p. 6), dentro-3 ligue os pontos (p. 39), dentro-4 sudoku 6x6 (p. 69), dentro-5 caça-palavras (p. 73), dentro-6 7 erros (p. 68). Amostras: N1 "O que vem depois?" (p. 8) e N2 código secreto (p. 78). O folheando mostra as págs. 1, 7, 8, 39, 104, 69, 73, 68 e 70 | sim (quadros do MP4 extraídos e olhados) |
| 11b. Mockups e topo também vinham da amostra | `gerar_midia.py`, `gerar_heroi.py` → `mockup-capa.png/.webp`, `mockup-pacote.png/.webp`, `heroi.webp` | Mesmo processo e mesmo tamanho. A capa agora é a do caderno vendido (antes aparecia "CADERNO-AMOSTRA · 13 ATIVIDADES"), e as folhas são as págs. 7, 78, 68, 69 e 8 | sim |
| 11c. Labirinto animado da seção "Veja por dentro" | `pagina/midia/labirinto_svg.py` → SVG inline em `pagina/index.html` (seção `#lab`) | Era o labirinto da amostra. Agora é o da pág. 7 (o mesmo de dentro-1), com o caminho do gabarito. A espessura e o enquadramento vêm do próprio gerador | sim (captura da seção) |
| 12. Vídeos dos anúncios | `criativos/montador/montador.py` (aceita `polygon` no traço animado) → `criativos/videos/anuncio-1..4-amandinha.mp4` | Usavam o `folheando.mp4` da amostra e páginas que mudaram (8, 11, 15, 69, 128, 142, 143). Foram montados de novo com o mesmo áudio. Detalhes e QC na seção abaixo | ver abaixo |

### Vídeos dos anúncios: o que foi refeito e o QC

- **O que foi refeito:** a cache de páginas (`node paginas2x.cjs 5 6 7 8 78 128 142 143`), os quadros do
  `folheando.mp4` novo e os 4 vídeos (`python3 montador.py N amandinha`). O áudio é o mesmo
  (`criativos/audio/amandinha-N.mp3`).
- **Durações iguais às de antes:** 22,10 s, 21,63 s, 22,90 s e 22,50 s. Nos 4 vídeos, as fronteiras das
  frases caem em pausas reais (8/8, 8/8, 6/6 e 8/8).
- **`qc.py`:** os 4 deram 1080×1920, 30 fps, h264 + aac e pico de −1,5 dB. Olhei as folhas de contato em
  `criativos/montador/tmp/qc/anuncio-N-amandinha-contato.jpg`: nenhuma tela preta, nada cortado, e a
  legenda bate com a fala. No anúncio 4, o "Ligue os pontos" agora fecha a casinha.
- **Quadros de referência:** `criativos/videos/quadro-anuncio-1..4.jpg` foram tirados de novo, no mesmo
  instante dos antigos (2,0 s, 3,2 s, 1,4 s e 11,1 s). O instante foi achado comparando com o vídeo antigo.
- **Atenção:** pelo `campanha.md`, os vídeos ANTIGOS já estão na Meta (IDs anotados lá). Nada foi
  enviado. A troca na Meta fica com o dono, depois do Portão M e do Portão C.

## Cosméticos para o dono decidir

1. **Categoria dos caça-palavras ("Cores e códigos").** O relatório sugere "Atenção" ou uma categoria
   "Letras". A categoria é uma das 6 que a página de vendas promete e organiza o plano de 30 dias (cada
   dia junta 2 categorias diferentes). Trocá-la mexe na promessa da página, nos selos e no plano. Proposta:
   renomear a categoria para "Letras, cores e códigos" no caderno, no Volume 2 e na página. Fica para o
   dono decidir porque muda texto de venda.
2. **Estrela do "Pinte pelo código" (pág. 24).** Ficou melhor, mas numa grade 12x12 a estrela sempre
   fica um pouco quadrada. Se o dono quiser, troco a arte por outra (ex.: lua ou balão).
3. **"O que vem depois?" com 2 linhas de instrução.** A frase nova (sem "no ?.") ocupa 2 linhas no A4. A
   página promete "instrução em uma linha" no Nível 1. O relatório da promessa já marcava "parcial" (o
   "Pinte pelo código" e o "Olhe e lembre" também têm 2 linhas). Encurtar mais deixaria a frase menos
   clara. Proposta: ajustar o texto da página ("instrução curta para o adulto ler").
4. **"Gabarito no fim" (promessa parcial).** Os bônus vêm depois do gabarito (págs. 142–149). Mudar a
   ordem muda a numeração de páginas, os planos e o sumário. A recomendação é não mexer, ou trocar o texto
   da página para "gabarito completo antes dos bônus".

## Paginação

- **Caderno:** não mudou. São 149 páginas, com as mesmas páginas por atividade, os mesmos planos de 30
  dias (págs. 5 e 67, idênticas às de antes) e o gabarito nas págs. 128–141. O sumário só passou a
  apontar as aberturas (4 e 66).
- **Volume 2:** não mudou (140 páginas, planos nas págs. 4 e 66, gabarito nas págs. 127–140).
- **Bumps:** só o Bump 4 mudou, de 70 para 73 páginas, por causa do gabarito com 2 por linha no fim. As
  60 atividades continuam nas págs. 4–63, e o "Como usar" não cita a página do gabarito. Os outros bumps
  mantêm as páginas: 20, 47, 10, 69 e 12.
- **Contagens** iguais: 120 atividades (60/60) no caderno e no Volume 2. Bumps com 30, 40, 48, 60, 60 e
  5 jogos.

## Arquivos regenerados

- PDFs: `produto/final/dez-minutinhos.pdf` e `produto/bumps/{1_para-levar-na-bolsa,2_recortar-e-colar,3_cartas-de-conversa,4_matematica-brincando,5_letras-e-palavras,6_jogos-de-mesa,7_volume-2}/<slug>.pdf`.
- Zips de entrega (1 PDF dentro de cada, como antes): `produto/final/dez-minutinhos-entrega.zip` e os 7
  `produto/bumps/*/<slug>.zip`.
- Página (só local, nada publicado): `pagina/img/dentro-1..6.jpg`, `amostra-nivel1.jpg`,
  `amostra-nivel2.jpg`, `folheando.mp4`, `folheando.gif`, `folheando-poster.jpg`, `mockup-capa.png/.webp`,
  `mockup-pacote.png/.webp`, `heroi.webp` e o SVG do labirinto inline em `pagina/index.html`.
- Vídeos (só local, nada enviado à Meta): `criativos/videos/anuncio-1-amandinha.mp4` a
  `anuncio-4-amandinha.mp4` e `quadro-anuncio-1..4.jpg`.
- Documentos atualizados: `bumps/bumps.md` (Bump 4 com 73 págs.), `criativos/videos/LEIA.md` (remontagem),
  `aprendizados/processo.md` (seção Material) e `status.md` (registro).

## Antes / depois

- `amostras/01-gabarito-pinte-pelo-codigo-p128.png`: gabarito sem cor → desenho pintado.
- `amostras/02-ligue-os-pontos-barquinho-p39.png`: barco aberto → contorno fechado e "volte ao 1".
- `amostras/03-gabarito-ligue-barquinho-p131.png`: gabarito do barco aberto → fechado.
- `amostras/04-sequencia-ambigua-p106.png`: 1 5 ○ 12 15 → 1 5 8 12 ○.
- `amostras/05-carro-qual-e-diferente-p12.png`: carro espelhado → carro sem roda.
- `amostras/06-volume2-labirinto-trivial-p27.png`: caminho reto → labirinto que usa o miolo.
- `amostras/07-bump5-rimas-p44.png`: BALÃO/FOGÃO × MAMÃO/AVIÃO → um par só por final.
- `amostras/08-bump2-figura-guia-p3.png`: guia a 13% → 38%.
- `amostras/09-pagina-de-vendas-dentro-5.png`: "Caça-palavras: bichos" da amostra → pág. 73 do caderno.

## Próximo passo

`python3 ferramentas/conferir_material.py ofertas/2026-11-26_atividades-foco` dá "MATERIAL NÃO APROVADO"
porque ainda falta o `APROVACAO.md`. Pela regra 7 do CLAUDE.md, falta uma nova revisão do documento
inteiro sair limpa e o dono aprovar (Portão M), além de decidir os 4 cosméticos acima.

## Decisão do dono sobre os cosméticos (2026-11-28)
1. Etiqueta "Cores e códigos" nos caça-palavras — **mantida** (aceita pelo dono).
2. Estrela da p. 24 levemente quadrada — **mantida** (aceita pelo dono).
3. "Instrução em uma linha" — **página ajustada**: "instrução curta para o adulto ler" (index.html e copy.md, seção dos níveis e FAQ).
4. "Gabarito no fim" — **página ajustada**: "Gabarito completo" / "logo depois das atividades" (index.html e copy.md, 4 trechos).

## Rodada 2

Base: `rodada2-caderno-p1-66.md`, `rodada2-caderno-p66-149.md`, `rodada2-bumps-1-a-6.md` e
`rodada2-volume2-e-promessa.md`. Regra do dono: corrigir todos os cosméticos. Os 2 itens aceitos pelo dono
(etiqueta "Cores e códigos" dos caça-palavras e estrela da p. 24) **não foram mexidos**.

**Como conferi:** tudo corrigido no gerador (`produto/gerador/`, `criativos/montador/`, `pagina/midia/`), nenhum PDF
editado à mão. Cada PDF novo foi comparado página a página com o da rodada 2 por pixel (40 dpi) para achar as páginas
que mudaram, e **todas as páginas que mudaram foram olhadas em imagem** (50 a 80 dpi; recortes ampliados na melancia
e no ligue p. 111 do V2). Os asserts do gerador rodaram em todas as gerações (contagens, sudokus, caça-palavras,
5/7 diferenças, plano com categorias diferentes no dia, famílias de rima, `assert` novos de sílabas, desembaralhe e
contas). O caça-palavras novo do bump 5 foi conferido por script nas 8 direções (cada palavra 1 vez). As filas de
"Que número falta?" do V2 foram conferidas por script: nenhuma janela de 4 termos igual a outra do V1 ou do V2.
O gerador continua reprodutível: md5 igual de todos os HTML com PYTHONHASHSEED 1, 77 e aleatório.
As correções que mudam conteúdo sorteado gastam o rng principal como antes e sorteiam o novo num rng derivado, então
as outras páginas ficaram iguais (a lista de páginas alteradas abaixo vem da comparação por pixel).

### Caderno principal (`produto/final/dez-minutinhos.pdf`, 149 págs.)

| Item | Arquivo/página | O que foi feito | Conferido em imagem |
|---|---|---|---|
| Buraco no caule da flor | `atividades2._arte("flor")` · p. 61 (gabarito p. 134) | Linha 10 passou a `.33333......`: caule contínuo nas colunas 5–6 da linha 7 à 12, folha da esquerda encostada | sim (p. 61 e gabarito p. 134) |
| Filas repetidas no "O que vem depois?" do Nível 1 | `gerar_completo.nivel1` + `sem_repetir_filas(..., CICLOS_EXTRAS_N1)` · p. 32, 45, 51, 62 (gabarito p. 130, 132, 133, 134) | Nenhuma fila repete no Nível 1. A 2ª ocorrência virou uma fila extra só com figuras em pé (sol/nuvem, peixe-peixe-flor, coração-estrela-estrela, maçã/balão). P. 8, 14 e 57 ficaram iguais | sim (resposta única conferida nas 4 filas novas) |
| Convés do barquinho | `TRACO_PRONTO["barquinho"]` · p. 39 (gabarito p. 131) | O trecho do convés entre o pé do mastro (14) e a ponta da direita (6) já vem traçado: vela e casco ficam separados | sim |
| Casa de cabeça para baixo | `CICLOS_EXTRAS` · p. 125 fila 4 (gabarito p. 141) | A fila extra da casa virada saiu; entrou coração, coração, coração virado. Resposta única (coração em pé) | sim |
| Ideias no infinitivo | `gerar_completo.IDEIAS` · p. 146–147 | 14: "Lave frutas, conte colheres, arrume a mesa." 23: "Escreva ou desenhe uma cartinha…" | sim |
| B1 · capa "Gabarito no final" | `gerar_completo.capa` · p. 1 | Capa diz "Gabarito completo" (assert: não sobra "no final") | sim |

### Bumps 1 a 6

| Item | Arquivo/página | O que foi feito | Conferido em imagem |
|---|---|---|---|
| B2 · peça que sobra sempre 21 | `atv_recorte.contas_cola` · p. 27, 32, 37, 40 (gabarito p. 46–47) | A sobra é sorteada (rng derivado) entre resultado ± 1 ou ± 2, sem repetir entre folhas: 10, 11, 9, 15 | sim |
| B2 · contas fáceis na p. 40 (e 2 − 1 na p. 32) | idem | Soma com resultado > 10 e diminuir com o primeiro número ≥ 11; nenhuma conta repete no bump. P. 32: 2 − 1 e 10 − 7 viraram 15 − 1 e 20 − 11; p. 40: 12 − 3, 15 − 8, 16 − 2, 13 − 1, 13 − 12. P. 27 igual | sim |
| B2 · pato ambíguo | `GRUPOS["bichos_coisas"]` · p. 16, 35 (gabarito p. 44, 46) | Pato trocado pelo polvo (mesmo lugar na lista: o sorteio não muda) | sim |
| B3 · carta 35 | `bump_cartas.py` · p. 8 | "E se o jantar caísse do céu como chuva? O que você queria que caísse?" | sim |
| B3 · "pensar junto" | idem · p. 2 | "…para pensar juntos." | sim |
| B4 · contas mais fáceis que o aquecimento | `atv_matematica.contas` · p. 42, 43, 50, 51, 57, 58, 62, 63 (gabarito p. 70–73) | Fora do aquecimento: soma com uma parcela ≥ 10 e diminuir com o primeiro número ≥ 11, sem repetir conta no bump (rng derivado; as outras páginas não mudam) | sim |
| B5 · palavras repetidas no "Desembaralhe" | `bump_letras.forme_sem_repetir` · p. 35, 42, 49, 56 (gabarito p. 64, 67, 68, 69) | 24 palavras diferentes nas 4 folhas (entraram FACA, TREM, MESA, MEIA, MALA etc.) | sim |
| B5 · anagramas TOGA e SACA | `atv_letras.forme_palavra(evitar=EMBARALHADAS_PROIBIDAS)` · p. 35, 42 | Embaralha de novo se sair palavra conhecida. Li os 24 embaralhados: nenhum forma palavra (ex.: OTGA, ACSA) | sim |
| B5 · repetidas no "Complete com a sílaba" | `bump_letras.silaba_sem_repetir` · p. 33, 40, 47, 54, 61 | 30 palavras diferentes nas 5 folhas | sim |
| B5 · repetidas no "Quantas sílabas?" | `bump_letras.conte_sem_repetir` + ícones novos PÃO e TREM · p. 41, 48, 55 (p. 34 igual) | 32 palavras diferentes nas 4 folhas, cada folha com 1, 2 e 3 sílabas (1 sílaba: FLOR, TREM, SOL, PÃO) | sim |
| B5 · p. 59 com duas respostas | `atv_letras.FRASES` · p. 59 (gabarito p. 68) | "4. O ______ vive na água e tem escamas." | sim |
| B5 · ícones de FACA e MALA | `VOGAL_EXTRAS` · p. 13, 29 (e onde mais aparecem) | Faca com lâmina larga, ponta arredondada e cabo com rebites; mala com alça de puxar e rodinhas | sim |
| B5 · PEGA, PIQUE, BOLINHA | `TEMAS["brincadeiras"]` · p. 57 (gabarito p. 69) | Lista: XADREZ, QUEIMADA, PIPA, AMARELINHA, RODA, CORDA, CIRANDA, PETECA. Grade sai de rng derivado (as outras páginas não mudam); cada palavra 1 vez (script) | sim |
| B6 · estrela que leva à lua | `bump_jogos.REGRAS` · p. 2 | "A figura só vale na casa onde o dado parou: se a estrela ou a nuvem levar a outra figura, essa não vale." | sim |

### Volume 2 (`produto/bumps/7_volume-2/volume-2.pdf`, 140 págs.)

| Item | Arquivo/página | O que foi feito | Conferido em imagem |
|---|---|---|---|
| A1 · "29" escondido pelo cabo | `atividades2.ligue_pontos` (ponto de `ROTULO_AO_LADO` nunca vai para baixo) · p. 111 (gabarito p. 138) | O "29" fica em cima do ponto, fora do cabo | sim (ampliado) |
| A2 · séries deslocadas | `atividades2.CHECAR_JANELAS` / `SEQ_JANELAS` (só o V2 liga) · p. 69, 82, 88, 99 (gabarito p. 133, 135, 136, 137) | Nenhuma fila do V2 tem 4 termos seguidos iguais a outra do V1 ou do V2 (script). O caderno não muda | sim |
| A3 · fila da lua igual e duas filas de casinha | `bump_volume2.diferente_variado` · p. 6, 12, 18, 21 (gabarito p. 127, 128) | Uma figura por fila na folha (sem duas casinhas) e a mesma variante nunca na mesma posição de uma folha anterior (lua: 3ª, 5ª e 4ª) | sim |
| A4 · guarda-chuva em dias seguidos | `NOVAS_ARTES["melancia"]` · p. 40 (gabarito p. 130) | O "Pinte pelo código" do Dia 18 virou uma fatia de melancia (vermelho, verde e marrom) | sim (ampliado) |
| A5 · "gato até a casa" nos dois níveis | `nivel2.labs` · p. 104 (gabarito p. 137) | N2: "Leve o gato até a árvore" (par que não existe no V1 nem no V2 N1). Mesmo labirinto | sim |
| Efeito da troca da casa virada | `CICLOS_EXTRAS` · p. 124 fila 3 (gabarito p. 140) | No V2 a mesma fila extra (casa virada) também saiu e virou a do coração | sim |

### Promessa (B1) e mídia

| Item | Arquivo | O que foi feito | Conferido em imagem |
|---|---|---|---|
| Capa no topo, mockups e folheando | `pagina/midia/gerar_midia.py` + `fotografar.cjs`, `gerar_heroi.py` | Refeitos do PDF final: `heroi.webp`, `mockup-capa.png/.webp`, `mockup-pacote.png/.webp`, `folheando.mp4/.gif`, `folheando-poster.jpg`, `dentro-3.jpg` (p. 39). As outras `dentro-*`/`amostra-*`/`obrigado-*` saíram iguais byte a byte. SVG do labirinto (p. 7) igual ao inline do `index.html` (não mudou). Página aberta no navegador: nenhuma imagem faltando | sim (quadros do MP4 a 1 fps, mockups e topo da página) |
| Imagem do produto na Hotmart mostrava a capa antiga | `gerar_midia.py` (cena nova `hotmart-produto`) → `hotmart/imagem-produto.png` | Refeita do PDF final, 1200×1200, fundo laranja (capa com "por Gefferson Balles" e "Gabarito completo" + p. 7 + lápis). As `imagem-bump-*.png` mostram as capas dos bumps, que não mudaram ("Gabarito no final" é verdade nelas): ficaram iguais | sim |
| Anúncio 2 "Gabarito no fim" | `criativos/montador/montador.py` l. 73, `criativos/roteiros.md` l. 111 | "Gabarito completo" | sim (folha de contato do QC) |
| 4 vídeos dos anúncios | `montador.py N amandinha` | Cache refeita (`paginas2x.cjs 5 6 7 8 78 128 142 143` + quadros do `folheando.mp4` novo). Mesmo áudio e mesma duração: 22,10 / 21,63 / 22,90 / 22,50 s; fronteiras em pausas 8/8, 8/8, 6/6, 8/8. `qc.py`: 1080×1920, 30 fps, h264 + aac, pico −1,5 dB; folhas de contato olhadas | sim |
| Quadros de referência | `criativos/videos/quadro-anuncio-1..4.jpg` | Tirados de novo nos mesmos instantes (2,0 / 3,2 / 1,4 / 11,1 s): saíram iguais byte a byte aos de antes (esses instantes não mostram a capa) | sim |
| Extra: outros criativos com a capa | `criativos/estatico/gerar.cjs`, `facebook/gerar.cjs` | `anuncio-5-ferias-4x5.jpg` e `facebook-capa.png` refeitos (usam os mockups com a capa). `facebook-perfil.png` saiu igual | sim |

### Páginas que mudaram (para a rodada 3)

- **Caderno:** 1, 32, 39, 45, 51, 61, 62, 125, 130, 131, 132, 133, 134, 141, 146, 147.
- **Bump 1:** nenhuma (PDF mantido o mesmo arquivo).
- **Bump 2:** 16, 27, 32, 35, 37, 40, 44, 45, 46, 47.
- **Bump 3:** 2, 8.
- **Bump 4:** 42, 43, 50, 51, 57, 58, 62, 63, 70, 71, 72, 73.
- **Bump 5:** 13, 29, 33, 35, 40, 41, 42, 47, 48, 49, 54, 55, 56, 57, 59, 61, 64, 65, 66, 67, 68, 69.
- **Bump 6:** 2.
- **Volume 2:** 6, 12, 18, 21, 40, 69, 82, 88, 99, 104, 111, 124, 127, 128, 130, 133, 135, 136, 137, 138, 140.

### Paginação

Não mudou em nenhum PDF: caderno 149, bumps 20 / 47 / 10 / 73 / 69 / 12, Volume 2 140. Planos de 30 dias
(caderno p. 5 e 67; V2 p. 4 e 66), sumário e "Como usar" saíram iguais (não estão na lista de páginas alteradas).
Contagens iguais (120 + 120 atividades; bumps 30, 40, 48, 60, 60 e 5 jogos). `bumps/bumps.md` não precisou mudar.

### Arquivos regenerados

- PDFs: `produto/final/dez-minutinhos.pdf`; `produto/bumps/2_recortar-e-colar/recortar-e-colar.pdf`,
  `3_cartas-de-conversa/cartas-de-conversa.pdf`, `4_matematica-brincando/matematica-brincando.pdf`,
  `5_letras-e-palavras/letras-e-palavras.pdf`, `6_jogos-de-mesa/jogos-de-mesa.pdf`, `7_volume-2/volume-2.pdf`.
- Zips (1 PDF dentro, md5 igual ao da pasta): `produto/final/dez-minutinhos-entrega.zip` e os 6 zips desses bumps.
  Bump 1 (PDF e zip) não mudou.
- Página (local): `pagina/img/heroi.webp`, `mockup-capa.png/.webp`, `mockup-pacote.png/.webp`, `folheando.mp4`,
  `folheando.gif`, `folheando-poster.jpg`, `dentro-3.jpg`.
- Hotmart (local, nada enviado): `hotmart/imagem-produto.png`.
- Vídeos (local, nada enviado à Meta): `criativos/videos/anuncio-1..4-amandinha.mp4`.
- Outros criativos (local): `criativos/estatico/anuncio-5-ferias-4x5.jpg`, `facebook/facebook-capa.png`.
- Código: `produto/gerador/{atividades2,gerar_completo,atv_recorte,atv_matematica,atv_letras,bump_letras,bump_cartas,bump_jogos,bump_volume2}.py`,
  `pagina/midia/gerar_midia.py`, `criativos/montador/montador.py`, `criativos/roteiros.md`.

### Cosméticos não corrigidos

Nenhum. (Os 2 aceitos pelo dono por escrito continuam como estão: "Cores e códigos" e a estrela da p. 24.)

Observação para a rodada 3: a fila extra nova (coração, coração, coração virado) aparece na p. 125 do caderno e na
p. 124 do Volume 2, como antes acontecia com a casa virada. São volumes diferentes e as outras filas da folha são
outras; se a rodada 3 achar que isso conta como repetição entre volumes, a troca é de uma linha em `CICLOS_EXTRAS`.

Nada foi publicado (`publicado/` intocado), nada foi enviado à Hotmart nem à Meta, e nada foi commitado.
