# Revisão de conversão — Dez Minutinhos — rodada 1

Data: 2026-11-26 · Revisor: critico-de-conversao · Base: `pagina/index.html` + fotos ao vivo (celular 390 px, 00–10; computador 1280 px, 00–07).
Ignorado de propósito: botões sem checkout e `{{placeholders}}` de e-mail/nome/CNPJ (pendências conhecidas).

## Nota: 6,5 / 10

A página é honesta, clara e leve (~1 MB no total, vídeo de 192 KB). O produto real aparece
(6 páginas por dentro + 2 amostras grandes), a garantia está bem explicada e o FAQ responde quase
tudo. O que segura a nota: **no celular ela é morna**. O topo é creme sobre creme, com um mockup
pálido e pequeno; o preço e o botão só aparecem depois de ~1,5 tela; o título descreve o produto mas
não toca a situação da mãe; e o meio da página é longo e repetido (mesma imagem 4 vezes, preço 4
vezes, tabela comparativa de ~1.300 px que não favorece a oferta em várias linhas). Para quem chega
frio de um anúncio, falta um "uau, quero isso" nos 3 primeiros segundos.

## Leitura como a mãe de 30–45 anos, no celular

1. **3 primeiros segundos** — vejo "Dez Minutinhos" e uma capa clarinha. Só entendo que é para
   imprimir quando leio o título (que começa abaixo da dobra). Preço: não vejo. Para quem: não vejo
   "4 a 10 anos" na primeira tela.
2. **Confiança** — parece real (páginas de verdade, Hotmart, garantia). Falta quem faz (rodapé com
   `{{placeholders}}` já é pendência conhecida).
3. **Objeções** — quase todas respondidas no FAQ. Faltam: "e se meu filho não quiser fazer?",
   "posso usar com meus alunos?", "tem Pix?" perto do preço.
4. **Atrito** — tabela longa, seção "Por que escolher" repete "O que você recebe", 3 blocos de preço
   iguais antes do fim.
5. **CTAs** — bem distribuídos (6 botões + barra fixa). O texto do botão é sempre o mesmo e não diz
   o que acontece.

## Os 10 problemas, em ordem de impacto

### 1. Primeira tela do celular não vende (celular-00)
- **Onde:** topo. Logo + mockup (~420 px de altura) + miniaturas ocupam a tela toda; o H1 começa
  perto de 620 px; preço e botão em ~1.200 px.
- **Por que atrapalha:** quem vem do anúncio decide em 3 s. Não vê para que idade é, quanto custa,
  nem uma folha de atividade de perto. O mockup é creme sobre fundo creme, sem contraste, e parece
  "papel em branco".
- **Correção:** no celular, colocar o H1 **acima** da imagem (ou uma linha curta sobre ela:
  "Para imprimir · 4 a 10 anos · R$ 37"); reduzir a imagem para ~300 px; fundo do hero em cor
  sólida (laranja claro saturado ou verde-menta) para a capa "saltar"; esconder as miniaturas no
  celular (deixar só o swipe com bolinhas). Meta: título + "4 a 10 anos" + R$ 37,00 visíveis sem
  rolar.

### 2. Título descritivo, sem a dor da situação
- **Onde:** H1 "120 atividades prontas para imprimir. Dez minutinhos por dia, longe da tela."
- **Por que atrapalha:** é correto, mas é lista de especificação. A cena que dá vontade ("5 da tarde,
  jantar no fogo, 'posso ver o tablet?'") só aparece na 2ª/3ª tela.
- **Correção (opções, todas sem atributo pessoal e sem promessa de efeito):**
  - "Para a hora do 'posso ver o tablet?': 10 minutos de papel e lápis, já prontos."
  - "Imprimiu, entregou. 120 atividades para os 10 minutos sem tela do dia."
  - "Fim de tarde sem tela: 2 folhas por dia, 30 dias de atividades prontas."
  Manter o subtítulo atual (2 níveis, plano, gabarito, P&B) logo abaixo e acrescentar "4 a 10 anos"
  no subtítulo ou num selo sobre a imagem.

### 3. "Já impresso, já pronto" é falso (celular-09, fecho)
- **Onde:** H2 do bloco final escuro.
- **Por que atrapalha:** o produto é PDF; "já impresso" contradiz o "nada é enviado pelo correio" e
  pode gerar reembolso/reclamação de quem esperava o caderno físico.
- **Correção:** "Dez minutinhos por dia. Imprimiu, está pronto." ou "Abre, imprime, entrega."

### 4. Tabela comparativa longa e que joga contra (celular-03)
- **Onde:** "Três jeitos de arrumar uma atividade para agora".
- **Por que atrapalha:** ~1.300 px de rolagem no celular. E em 3 das 6 linhas a concorrência
  "empata" ou "ganha" no texto: folhinhas "Fica longe da tela: Sim", app "Tempo para preparar:
  Nenhum", app "Gabarito: Não precisa". A mãe lê e pensa "então o app é mais fácil".
- **Correção:** virar uma grade compacta de 4 linhas × 3 colunas com ícones ✓ / ✗ / "às vezes",
  só nas linhas em que o Dez Minutinhos realmente se diferencia: **separado por idade**, **ordem
  para seguir (plano 30 dias)**, **gabarito**, **longe da tela**. Tirar "tempo para preparar" e
  "imprimir de novo" (já aparecem em outros blocos). Cabe em uma tela.

### 5. Repetição: mesma imagem 4×, preço 4×, benefícios 3×
- **Onde:** `mockup-capa` no hero, no cartão de oferta, no "Como funciona" (poster do vídeo) e no
  fecho; bloco de preço no hero, cartão de oferta, "Quanto custa" e fecho; "Por que escolher"
  repete "O que você recebe" e os bullets do hero.
- **Por que atrapalha:** a sensação é de página "enchendo linguiça"; a imagem repetida faz o
  produto parecer menor do que é.
- **Correção:** tirar a seção "Por que escolher o Dez Minutinhos" (tudo já foi dito); no cartão
  de oferta (logo após o hero) usar `mockup-pacote` (leque de folhas) em vez da capa de novo; no
  fecho usar uma foto/mockup diferente (ex.: semana impressa em pilha). Manter 3 blocos de preço:
  hero, "Quanto custa", fecho.

### 6. Amostras pequenas demais no celular (celular-04)
- **Onde:** "Veja 6 páginas por dentro" em grade 2 × 3.
- **Por que atrapalha:** cada página fica com ~170 px de largura; o "toque para ampliar" abre a
  imagem crua em outra aba (sai da página). É a melhor prova que temos e está miúda.
- **Correção:** carrossel de 1 página por vez com swipe (largura ~85% da tela, a próxima espiando
  na borda) e ampliação em sobreposição na mesma página, não em nova aba. Uma linha de legenda
  com o nível e o tempo ("Nível 1 · uns 5 minutos").

### 7. Bônus sem imagem nenhuma (celular-06)
- **Onde:** 3 cartões tracejados só com texto.
- **Por que atrapalha:** bônus sem imagem parece enchimento; com imagem vira "olha quanta coisa".
- **Correção:** quando os bônus estiverem **produzidos** (status: produto ainda em 13 atividades de
  amostra), pôr uma miniatura real de cada: o quadro de conquistas, um certificado, o calendário
  das 30 ideias. Até lá, manter só texto — **não** mostrar mockup de bônus que ainda não existe.

### 8. Preço sem Pix e sem parcela; CTA sempre igual
- **Onde:** todos os blocos de preço ("à vista ou parcelado no cartão") e botões.
- **Por que atrapalha:** Pix é o meio preferido de quem compra R$ 37 no celular; "parcelado" sem
  número deixa dúvida. Botão idêntico 6 vezes não diz o que acontece depois.
- **Correção:** "R$ 37,00 no Pix ou cartão · ou em até Nx" (N = número real configurado na
  Hotmart, pendente do dono). Microtexto sob o botão principal: "Você paga na Hotmart e recebe o
  PDF no e-mail em minutos." Variar o texto do último botão: "Quero imprimir hoje".

### 9. Objeções que faltam no FAQ
- **Onde:** Perguntas frequentes.
- **Por que atrapalha:** as dúvidas mais comuns de mãe sobre material de atividade não estão lá.
- **Correção:** acrescentar, com respostas curtas e sem promessa de efeito:
  - "E se meu filho não quiser fazer?" → é brincadeira de 10 min, dá para fazer só uma folha, o
    quadro de conquistas ajuda a criar o hábito; e há a garantia.
  - "Posso usar com meus alunos / na escolinha?" → depende da licença (decisão pendente do dono).
  - "O que é o gabarito?" já está implícito — ok.
  Reduzir o FAQ juntando "Por quanto tempo tenho acesso?" com "Como eu recebo?".

### 10. Barra fixa cobre texto e topo do hero tem selos fracos
- **Onde:** barra fixa inferior (celular-00 mostra o subtítulo cortado atrás dela); selos "Acesso
  na hora / PDF A4 / Garantia" em cinza claro, letra pequena (celular-01).
- **Por que atrapalha:** texto escondido atrás da barra irrita; selos de confiança que ninguém lê
  não fazem efeito.
- **Correção:** `padding-bottom` no `body` igual à altura da barra quando ela está visível; selos
  com ícone (relógio, impressora, escudo), fundo branco com borda e texto 15 px escuro.

## Ideias de impacto visual (o "algo 3D" que o dono pediu)

Tudo leve (imagem estática ou CSS; nada de WebGL/three.js, que pesa e trava celular fraco) e
sem prova falsa.

1. **Hero 3D de verdade, renderizado como imagem.** Caderno impresso grampeado em perspectiva
   (Blender ou mockup 3D), levemente inclinado, sombra forte, sobre fundo laranja vivo; ao lado,
   2–3 folhas soltas "voando" com labirinto e código secreto visíveis, e um lápis. WebP ≤ 80 KB.
   **Selo obrigatório na imagem:** "Você recebe em PDF para imprimir" — mockup 3D de caderno físico
   sem isso vira promessa de produto físico.
2. **Inclinação 3D leve ao rolar/tocar.** `transform: perspective(800px) rotateY(-12deg)` na capa
   que volta a 0° quando entra na tela; respeitar `prefers-reduced-motion`. Custo: zero KB.
3. **Labirinto se resolvendo sozinho.** Animação SVG do caminho do gabarito sendo traçado em
   laranja sobre a página real do labirinto (stroke-dashoffset). Mostra a atividade E o gabarito
   num gesto só; < 10 KB. Ótimo logo abaixo do título.
4. **Vídeo curto real de mãos (sem rosto).** 5–6 s em loop: folha saindo da impressora → mão de
   criança com lápis fazendo o labirinto → check no quadro de conquistas. Filmado com as folhas
   reais da amostra. MP4 ≤ 500 KB, `muted playsinline`. É a imagem mais "palpável" possível.
5. **"A semana na gaveta".** Mockup das 14 folhas da semana em pilha/leque com etiqueta
   "Seg · Ter · Qua…" — visualiza o plano de 30 dias melhor que o texto dos 5 passos.
6. **Número "120" grande** com volume (sombra em camadas, CSS `text-shadow`), cercado pelas
   6 categorias em ícones coloridos grandes (atenção, memória, padrões, lógica, traçado, cores).
7. **Seções com cor.** Alternar creme com 1–2 blocos de cor sólida (laranja no hero e no fecho,
   azul-claro nas amostras). Hoje é quase tudo creme e branco: sem contraste, nada "salta".
8. **"Toque para ver a resposta".** Numa das amostras (ex.: código secreto), um botão revela a
   resposta do gabarito por cima. Interação pequena, prova que o gabarito existe.

Não fazer: contador regressivo, "X pessoas vendo agora", estrelas/avaliações, foto realista de
criança (mesmo de IA), "antes/depois" de criança, selos de "aprovado por educadores".

## O que NÃO mudar

- Mostrar páginas reais do caderno (6 por dentro + 2 amostras inteiras) — é a melhor prova.
- Bloco de dor "Sabe aquela hora em que você só precisa de 10 minutos?" — texto excelente, situação
  e não atributo. (Só subir uma frase dele para o topo, ver problema 2.)
- "Como funciona" em 5 passos e a nota "Os 10 minutos são só uma ideia do tamanho" — honesta.
- "É para você se… / Não é para você se…" — filtra quem pediria reembolso.
- Âncora por custo (R$ 1,23/dia, R$ 0,31/atividade) sem "de/por".
- Garantia com selo e explicação de como pedir; FAQ do celular/impressora/irmãos.
- Peso da página (~1 MB) e vídeo em MP4 em vez do GIF de 1,8 MB — manter assim.
- Ausência de urgência, contagem de clientes e palavras de saúde.
