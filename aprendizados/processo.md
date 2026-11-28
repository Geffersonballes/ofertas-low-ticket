# Aprendizados de processo — o que já deu errado e como não repetir

Leia antes de cada etapa (regra 8 do `CLAUDE.md`). Cada linha: data · oferta · o que aconteceu → regra.
O que **vende** fica em `o-que-vende.md`; aqui fica **como trabalhar** com menos retrabalho.

## Ordem da esteira
- 2026-11-28 · Dez Minutinhos · Hotmart, criativos e campanhas foram feitos antes da revisão página por
  página do material → **Portão M**: revisar e aprovar o conteúdo primeiro (`revisar-material`,
  `ferramentas/conferir_material.py`). Só então Hotmart → criativos → campanhas.

## Material (infoproduto)
- 2026-11-28 · Dez Minutinhos · gabarito do "Pinte pelo código" sem cor: as casas coloridas eram desenhadas antes da grade branca e ficavam cobertas → no SVG, o que é resposta vai sempre POR CIMA da base (`base + gab`), e a conferência olha a miniatura do gabarito, não só o texto.
- 2026-11-28 · Dez Minutinhos · "Ligue os pontos" com desenho aberto (último número não voltava ao 1; barco sem metade do convés) → todo desenho de pontos é um contorno fechado de um traço só (canto final = canto inicial; T-junção vira traço pronto já impresso), instrução "volte ao 1" e gabarito em `polygon`.
- 2026-11-28 · Dez Minutinhos · sequência numérica com regra alternada (+4, +3) e o buraco no meio admitia duas respostas → regra alternada só com o buraco na última casa; filas nunca se repetem no volume nem entre volumes (registro global `SEQ_USADAS`, e o Volume 2 lê as do volume 1 no `completo.json`).
- 2026-11-28 · Dez Minutinhos · diferença "espelhada" em figura quase simétrica (carro, balão) e variante pequena (flor de 4 pétalas com 14 mm) eram invisíveis para 4–10 anos → não espelhar figura quase simétrica (usar variante visível: carro sem roda, ou "menor"); variante em objeto < 16 mm (N1 < 20 mm) vira "cinza".
- 2026-11-28 · Dez Minutinhos · labirinto gerado com caminho quase reto (desce a coluna e segue a última linha) → rejeitar labirinto com menos de 3 curvas no caminho da solução (`labirinto_bom`).
- 2026-11-28 · Dez Minutinhos · instrução com número fixo que não batia com a folha ("de 1 até 10" numa folha até 20) → texto da instrução sempre calculado do que foi desenhado (ex.: `linhas * por`), nunca do parâmetro.
- 2026-11-28 · Dez Minutinhos · rimas com duas respostas (BALÃO/FOGÃO com MAMÃO/AVIÃO) → cada par de rima tem uma família de final própria (`FAMILIAS_RIMA` com assert); vale para qualquer "ligue" com pares: um item só pode casar com um.
- 2026-11-28 · Dez Minutinhos · regra de jogo ambígua ("a peça com duas casas", sem desempate com 2 jogadores) → regra escrita com o caso de empate e o caso "ninguém tem"; não usar nome de figura como palavra comum.
- 2026-11-28 · Dez Minutinhos · item no grupo errado (ilha em "Na água"; flor em "Na natureza" quando pode estar no vaso) → nas atividades de classificar, só itens sem dúvida para uma criança; revisar a lista de grupos à mão.
- 2026-11-28 · Dez Minutinhos · cinzas claros que somem em P&B econômico (figura-guia a 13%, pontilhado #9a9a9a, ligações da trilha #bbb, legenda de cor só por cor, preço em laranja) → nada essencial abaixo de ~35% de tinta; cor nunca é a única pista (nome escrito, borda grossa, rótulo).
- 2026-11-28 · Dez Minutinhos · conteúdo repetido entre folhas (palavras, filas de padrão, itens de grade lógica) → cada gerador guarda o que já usou no volume e troca o repetido.
- 2026-11-28 · Dez Minutinhos · o gerador não era reprodutível (`set()` de tuplas/strings muda com o PYTHONHASHSEED) e qualquer troca mexia no rng e mudava páginas já revisadas → nunca iterar `set` para sortear (usar `dict.fromkeys`/`sorted`); correção que muda o conteúdo sorteado gasta o rng principal como antes e sorteia o novo com um `random.Random(derivado)`, para as outras páginas ficarem iguais (conferir com rastreio do estado do rng por página).
- 2026-11-28 · Dez Minutinhos · imagens e vídeo da página de vendas vieram do PDF de amostra (páginas que não existem no caderno) → mídia da página sai do PDF FINAL rasterizado (`pagina/midia/gerar_midia.py` agora faz isso) e é refeita sempre que o PDF mudar.
- 2026-11-28 · Dez Minutinhos (rodada 2) · regra de "não repetir" aplicada num nível e esquecida no outro (filas do "O que vem depois?" só no N2; palavras sem repetir só no "Qual vogal falta?") → toda regra de "não repetir" vale para todas as atividades que sorteiam palavras/filas, em todos os níveis e volumes; ao corrigir uma, procurar as irmãs no gerador.
- 2026-11-28 · Dez Minutinhos (rodada 2) · correção de dificuldade só em parte ("aquecimento" no começo, mas as folhas seguintes ainda tinham 2 − 1; a peça que sobra era sempre 21) → regra de dificuldade vale para todas as folhas do tipo; distrator sempre perto da resposta e sorteado, nunca um valor fixo.
- 2026-11-28 · Dez Minutinhos (rodada 2) · "não repete" medido só na linha inteira (2 4 6 8 10 × 4 6 8 10 12) → comparar o que a criança vê (janelas de termos seguidos), não só a tupla inteira.
- 2026-11-28 · Dez Minutinhos (rodada 2) · embaralhado que vira outra palavra (TOGA, SACA) e figura girada que vira outra coisa (casa de cabeça para baixo) → todo embaralhado passa por lista de palavras proibidas e é lido por uma pessoa; só girar figura que continua reconhecível virada.
- 2026-11-28 · Dez Minutinhos (rodada 2) · capa e anúncio com texto de promessa antigo ("Gabarito no fim") depois de a página mudar → quando o dono muda um texto de promessa, procurar a frase no repositório todo (gerador, capa, montador, roteiros, imagens da Hotmart) e refazer toda a mídia que mostra aquilo.
- 2026-11-28 · Dez Minutinhos (rodada 2) · imagem do produto da Hotmart não tinha gerador e ficou com a capa antiga → toda imagem derivada do PDF sai de um script (`pagina/midia/gerar_midia.py` agora gera também `hotmart/imagem-produto.png`); para saber o que refazer, comparar PDF novo × antigo por pixel e refazer o que usa as páginas alteradas.
- 2026-11-28 · Dez Minutinhos (rodada 2) · número do "ligue os pontos" movido para "o lado com mais espaço" caiu em cima do traço pronto (cabo do guarda-chuva) → a posição do rótulo considera também os traços já impressos, não só pontos e rótulos.
- 2026-11-28 · Dez Minutinhos (rodada 3) · a trava de "não repetir" entre volumes existia só para os números (`CHECAR_JANELAS`); as filas de figuras do Volume 2 saíam das mesmas listas do caderno e 15 de 20 repetiam → toda atividade sorteada de um volume novo carrega o que o volume anterior já usou (via `completo.json`) e tem assert "nada em comum"; ao criar a trava num tipo, criar nos tipos irmãos no mesmo dia.
- 2026-11-28 · Dez Minutinhos (rodada 3) · "fila igual" comparada como tupla deixou passar a mesma série deslocada (A B × B A) e a figura que, girada 180°, fica igual à espelhada (peixe, lua) → comparar o que a criança vê: ciclo pela menor rotação, figura simétrica espelhada = em pé, e também o "núcleo" (a parte que gira, sem a figura de apoio).
- 2026-11-28 · Dez Minutinhos (rodada 3) · troca sorteando a folha inteira de novo deixou folhas do fim do nível mais fáceis (10 − 1 virou 3 − 1) → ao corrigir repetição, trocar só o item repetido, com o mesmo molde/faixa do original, e olhar a dificuldade antes × depois.
- 2026-11-28 · Dez Minutinhos (rodada 3) · sílaba que sobra formando palavra (MA + LA = MALA; também BECO, COLO, CANO, BELA) e a fileira com uma sílaba só para duas respostas → toda sobra/distrator passa por teste "sobra + metade não é palavra" contra as palavras do bump + uma lista de palavras comuns, conferido imprimindo todas as combinações; fileira traz cada resposta quantas vezes ela é usada.
- 2026-11-28 · Dez Minutinhos (rodada 3) · respostas concentradas na mesma folha (5 de 6 vogais A; 4 de 6 contas dando 5; o mesmo item nos 5 problemas; balão nas 6 cartelas) → toda folha sorteada tem regra de variedade com assert (respostas diferentes, ≥ 3 vogais, item ≤ 2 vezes, figura em 3–4 cartelas), aplicada a todas as folhas do tipo.

## Criativos
- 2026-11-28 · Dez Minutinhos · o vídeo "caderno folheando" (página e fim dos anúncios) foi gravado do
  caderno-amostra e mostra páginas que não existem no produto vendido → criativos só depois do material
  aprovado e feitos a partir do PDF final (Portão C confere).
- 2026-11-28 · Dez Minutinhos (rodada 3) · zoom de câmera com escala fixa (1,9×) cortava a borda da página ("lano de 30 dias") → zoom de página com limite calculado para caber no quadro (`caber` no montador); conferir os quadros do fim de cada zoom, não só o meio da frase (a folha de contato do `qc.py` pega o meio).
- 2026-11-28 · Dez Minutinhos (criativos, rodada 1) · legenda cortada pela proporção de caracteres chegava ~0,3 s atrasada e partia "de 4 a / 6 anos" → cortar pelo tempo real das palavras (`montador/palavras.py`, faster-whisper com tempo por palavra; o montador casa texto × transcrição) e marcar os blocos à mão com "|" (até 7 palavras, nunca partindo número + unidade); espaço que não quebra em "4 a 10 anos", "30 dias", "R$ 37,00" e `text-wrap: balance` no título e na legenda.
- 2026-11-28 · Dez Minutinhos (criativos, rodada 1) · zoom de página passava por baixo da legenda (plano, quadro de conquistas, memória) → todo zoom que cresce para baixo roda dentro de uma `janela` que termina acima da legenda; zoom no topo de um cartão usa foco no topo (0 %), para o cabeçalho não subir para baixo do título.
- 2026-11-28 · Dez Minutinhos (criativos, rodada 1) · fecho com botão escuro e legenda escura empilhados, e roteiro pedindo garantia que o vídeo não tinha → o cartão final segue o roteiro ao pé da letra (preço + "Garantia de 7 dias" + botão) e a legenda do fecho fica clara e longe do botão; conferir o roteiro contra o `LEIA.md` antes de montar.
- 2026-11-28 · Dez Minutinhos (criativos, rodada 1) · na imagem estática, uma miniatura de tabela (plano de 30 dias) nunca fica legível no celular, e um leque fechado esconde as páginas → tabela vira texto grande; o leque mostra cada página com o título visível; páginas rasterizadas do PDF aprovado (`pdftoppm`) e as mesmas que o roteiro cita; produzir todos os formatos que o roteiro lista (o 1:1 tinha ficado para trás).
- 2026-11-28 · Dez Minutinhos (criativos, rodada 1) · texto de anúncio prometendo mais que o produto ("4 atividades em 10 minutos"; descrição só com "R$ 1,23 por dia") → cada campo do anúncio (título e descrição aparecem sozinhos em vários posicionamentos) tem de valer sozinho: preço com "uma vez só" e tempo igual ao da página ("2 folhas, uns 10 minutinhos").
- 2026-11-28 · Dez Minutinhos (criativos, rodada 1) · anúncios criados antes do Portão C com vídeos antigos e IDs de vídeo diferentes entre as tabelas de `campanha.md` → nunca criar anúncio antes de "CRIATIVOS APROVADOS"; ao subir mídia, anotar o ID na mesma linha do anúncio que a usa.
- 2026-11-28 · Dez Minutinhos (criativos, rodada 2) · a `janela` da rodada 1 só cobria os zooms, e as **entradas** animadas (página subindo de baixo no A2 e no A3) continuavam passando por baixo da legenda; no A2 o 1º quadro (miniatura do vídeo) saía quase vazio → toda cena que entra ou cresce para baixo roda dentro da `janela`, inclusive entradas; olhar o quadro 0,0 s em tamanho grande, porque ele é a miniatura.
- 2026-11-28 · Dez Minutinhos (criativos, rodada 2) · título longo com separador ("Sem saber ensinar · sem montar rotina") quebrava com o "·" pendurado e encostava nas bordas → título de 2 linhas é escrito com quebra explícita ("\n", o título aceita `pre-line`) e sem "·"; margem lateral do título ≥ 150 px como os outros.
- 2026-11-28 · Dez Minutinhos (criativos, rodada 2) · a voz sintética às vezes diz palavra que não está no texto enviado ("com **o** quadro"); o whisper ouve pela gramática, então leitura só de modelo não basta → recortar o trecho, comparar a duração da sílaba com a mesma palavra em outro ponto do áudio (espectrograma + energia) e registrar a decisão; na dúvida, a legenda segue o que se ouve (como o "imprime e entrega").
- 2026-11-28 · Dez Minutinhos (criativos, rodada 2) · roteiro com margem diferente da skill (250/340 px × 200/250 px) e com tabelas de cena de antes da montagem → uma regra de margem só (a da skill `revisar-criativos`), medida nos quadros; depois de montar, atualizar no roteiro as cenas, títulos, durações e pendências pelo vídeo real (o `LEIA.md` não basta).

## Hotmart
- 2026-11-27 · O e-mail de compra e o checkout mostram o nome do titular da conta (CPF) → os dados legais
  da página precisam ser os mesmos da conta Hotmart.
- 2026-11-27 · Order bumps colocados só como bloco na página de pagamento "Em Branco" aparecem apenas
  com `?checkoutMode=10` **e** depois de "Alterar país"; a ferramenta `/cross-sell/order-bump` ficou vazia
  → configurar os bumps pela ferramenta Order Bump e testar o checkout em aba anônima no celular antes de
  seguir. (Chamado aberto no suporte; registrar aqui a solução quando vier.)
- 2026-11-27 · Recuperação de pagamento "Pix + cartão" não funciona com order bump → deixar desligada.
- 2026-11-27 · A extensão do Chrome trunca prompts longos → mandar prompts em partes curtas, uma tarefa
  por vez, e pedir "não mude nada, só me traga" quando for só leitura.
- 2026-11-27 · Pixel: cadastrar no principal **e em cada bump**; o token da API de Conversões é colado
  pelo dono. Eventos da Hotmart: "Vendas realizadas" (= Purchase) e "Visita à página de pagamento".
- 2026-11-28 · A API da Hotmart não troca arquivo de produto → troca de PDF é pela extensão do Chrome.

## Meta (Página, pixel, conta de anúncios, Windsor)
- 2026-11-28 · Usar sempre a conta **Ofertas Low Ticket · 1534301375187089** (portfólio Balles Tech).
  Conta pessoal sem pagamento não entra no portfólio; conta sem forma de pagamento não cria nem anúncio pausado.
- 2026-11-28 · O número de `facebook.com/profile.php?id=` **não** é o ID da Página para anúncios
  ("Página ausente"). Usar o ID de business.facebook.com/settings → Páginas.
- 2026-11-28 · Criar a Página da oferta **já dentro do portfólio**; criar o pixel e ligar a conta de
  anúncios em "Ativos conectados" antes de criar o conjunto (senão "conta sem acesso ao pixel").
- 2026-11-28 · Conta, Página ou pixel novos só aparecem no Windsor depois de refazer o link de conexão,
  clicar em "Editar configurações" e **marcar** o item na tela final do Windsor.
- 2026-11-27 · O pixel não dispara em navegador automatizado (headless): para testar, simular navegador
  comum (sem `navigator.webdriver`) ou usar Eventos de teste no navegador do dono.
- 2026-11-27 · Pixel de uma empresa (ex.: energia solar) nunca é reaproveitado numa oferta: um pixel por oferta.
- 2026-11-28 · "Anunciante e pagador" (exigência Brasil) não sai pela API sem identidade verificada →
  o dono preenche no conjunto na revisão do Portão 4.

## Infra
- 2026-11-27 · Vídeos e arquivos que a Meta precisa baixar: publicar em `publicado/<slug>/anuncios/`
  (servido pela VPS) e passar a URL para `create_ad_video`.
