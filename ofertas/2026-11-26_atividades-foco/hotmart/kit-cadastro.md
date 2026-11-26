# Kit de cadastro na Hotmart — Dez Minutinhos

Preparado em 2026-11-26 para o cadastro de 2026-11-27, com o Claude operando o navegador do dono.
Base: `briefing.md`, `pagina/copy.md`, `pagina/dados.json`, `produto/sumario.md`, `status.md`,
`docs/04_order-bumps.md`. Pesquisa feita na Central de Ajuda oficial (help.hotmart.com) em
2026-11-26. Cada regra da plataforma traz a fonte; o que não achei na documentação oficial está
marcado **não confirmado**.

Regras da casa que valem aqui (CLAUDE.md):
- Nada é publicado em anúncio nesta etapa. Cadastrar produto e checkout não gasta dinheiro.
- Sem prova inventada, sem promessa de saúde/escola/resultado, sem urgência ou "de/por".
- **Token da API de Conversões é segredo:** só o dono cola, direto na Hotmart. Nunca no chat, nunca
  neste repositório.

---

## 0. Resumo do que a Hotmart confirma hoje

| Ponto | O que vale | Fonte |
|---|---|---|
| Onde cria | Produtos > Meus produtos > **+ Criar produto** > escolher formato | [215828518](https://help.hotmart.com/pt-br/article/215828518/) |
| Formato | Escolhido no início; **não pode ser trocado depois que o produto é ativado** | [215828518](https://help.hotmart.com/pt-br/article/215828518/), [360016600591](https://help.hotmart.com/pt-br/article/360016600591/) |
| Campos da aba Informações | Nome; Descrição (**mínimo 200 caracteres**); Imagem (**JPG, PNG ou GIF, até 5 MB**); idioma, categoria e mercado de atuação | [215828518](https://help.hotmart.com/pt-br/article/215828518/) |
| Limite máximo de caracteres do nome e da descrição | **não confirmado** (a documentação só dá o mínimo da descrição) | — |
| Dimensão em pixels da imagem do produto | **não confirmado** (só formato e peso). Fizemos quadrada 1200 × 1200 | — |
| Garantia | 7, 15, 21 ou 30 dias | [215828518](https://help.hotmart.com/pt-br/article/215828518/) |
| Forma de pagamento | À vista / parcelado com taxas para o cliente / parcelado sem taxas (produtor absorve); **não dá para trocar depois de criar a oferta** | [215828518](https://help.hotmart.com/pt-br/article/215828518/), [4404509205005](https://help.hotmart.com/pt-br/article/4404509205005/) |
| Parcela mínima no Brasil | **R$ 7,00 por parcela**; até 12x no cartão conforme valor e configuração | [4404509205005](https://help.hotmart.com/pt-br/article/4404509205005/), [216440337](https://help.hotmart.com/pt-br/article/216440337/) |
| eBook (conteúdo) | até **20 arquivos de até 250 MB**; formatos **PDF, ePub, XLS, XLSX, XLSM, XLSB, CSV** (não aceita ZIP); capa com **nome do autor** e título condizente com o nome do produto | [215828518](https://help.hotmart.com/pt-br/article/215828518/) |
| Arquivos para baixar | até 20 arquivos de até 250 MB, **ZIP ou RAR**, e um deles tem de ser um **PDF "Manual de Instruções"** com capa, autor e título | [215828518](https://help.hotmart.com/pt-br/article/215828518/) |
| Como o comprador recebe um eBook | Acesso liberado quando o pagamento é confirmado; baixa pelo e-mail "Compra aprovada…" (botão **Acessar meu produto**) ou em consumer.hotmart.com > Minhas compras > **Baixar conteúdo** | [215827338](https://help.hotmart.com/pt-br/article/215827338/) |
| Página de vendas externa | Produto > Página do produto > **Sua página externa** > Configurar página > URL. A página tem de ter botão para o link de pagamento | [360017889651](https://help.hotmart.com/pt-br/article/360017889651/) |
| Marketplace | Ligado por padrão; dá para desligar | [215828518](https://help.hotmart.com/pt-br/article/215828518/) |
| Aprovação | Depois de **Finalizar cadastro**, verificação de **cerca de 15 minutos, podendo chegar a 1 dia útil** | [215828518](https://help.hotmart.com/pt-br/article/215828518/) |
| Motivos de reprovação comuns | conteúdo incompleto, conteúdo achado de graça na internet, conteúdo genérico/IA superficial, falta do nome do autor, promessa de resultado de saúde/dinheiro | [31594947721485](https://help.hotmart.com/pt-br/article/31594947721485/) |
| Produto feito com IA | Aceito, se entregar valor real, respeitar PI e não simular depoimentos | [215828518](https://help.hotmart.com/pt-br/article/215828518/) |
| Order bump | Ferramentas > Aparência da Página de Pagamento > produto > Editar > **Order Bump** > Selecionar Produto (escolhe a **oferta** de outro produto) > Inserir > Salvar > Publicar | [360019967392](https://help.hotmart.com/pt-br/article/360019967392/) |
| Bump = produto próprio | Sim: o bump é a oferta de um produto cadastrado ("escolha a oferta do produto complementar"). Logo, **cada um dos 7 bumps precisa ser um produto Hotmart** com conteúdo e oferta | [360019967392](https://help.hotmart.com/pt-br/article/360019967392/) |
| Bump precisa estar aprovado antes de ser escolhido | **não confirmado** (provável, já que só produto aprovado vende) | — |
| Quantos bumps por checkout | **até 9** segundo a página comercial da Hotmart; a Central de Ajuda não diz o número. Usaremos 7 | [hotmart.com/pt-br/order-bump](https://hotmart.com/pt-br/order-bump) |
| Campos do bump (título, descrição, imagem) e limites | O blog oficial cita imagem, título e descrição editáveis; **limite de caracteres não confirmado** | [blog: order-bump-da-hotmart](https://hotmart.com/pt-br/blog/order-bump-da-hotmart) |
| Parcelas do bump | Não precisam ser iguais às do principal; formato Serviço Online não pode ser bump | [360019967392](https://help.hotmart.com/pt-br/article/360019967392/) |
| Pagamentos aceitos com bump | cartão, cartão virtual Caixa, saldo Hotmart, boleto, Pix, PayPal, dois cartões (sem parcelamento nesse caso) | [360019967392](https://help.hotmart.com/pt-br/article/360019967392/) |
| Pixel da Meta | **por produto**: Ferramentas > Ver todas > Pixel de Rastreamento > produto > **Facebook + Instagram** > ID > eventos > envio **Web, API de Conversões ou ambos** > Salvar | [115004826368](https://help.hotmart.com/pt-br/article/115004826368/), [360015341051](https://help.hotmart.com/pt-br/article/360015341051/) |
| Token | A opção API de Conversões pede **token gerado no Gerenciador de Eventos da Meta** | [9025315539981](https://help.hotmart.com/pt-br/article/9025315539981/), [6565866201741](https://help.hotmart.com/pt-br/article/6565866201741/) |
| Domínio no pixel | Não é mais necessário configurar domínio | [9025315539981](https://help.hotmart.com/pt-br/article/9025315539981/) |
| Pixel nos bumps | Venda do bump só vai para a Meta se **o produto do bump também tiver o pixel** | [6565866201741](https://help.hotmart.com/pt-br/article/6565866201741/) |
| Nome na fatura | até **22 caracteres** | [360041594231](https://help.hotmart.com/pt-br/article/360041594231/) |
| CPF/CNPJ do comprador | Obrigatório para comprador brasileiro (reforma tributária) | [360038937471](https://help.hotmart.com/pt-br/article/360038937471/) |
| Taxa Hotmart (BRL) | Venda > R$ 10: **9,9% + R$ 2,49**. Venda ≤ R$ 10 (microtransação): **20%** | [208298448](https://help.hotmart.com/pt-br/article/208298448/) |

---

## 1. Decisão de entrega: eBook com o PDF (recomendado)

O `.zip` de entrega (`produto/final/dez-minutinhos-entrega.zip`, 4,7 MB) tem **um arquivo só**:
`Dez Minutinhos - caderno completo.pdf` (5,3 MB, 149 páginas). Por isso:

- **Formato recomendado: eBook**, subindo direto o PDF `produto/final/dez-minutinhos.pdf`
  (a Hotmart aceita PDF até 250 MB no eBook; o ZIP não está na lista do eBook). Zipar um PDF não
  diminui quase nada e obriga o comprador a descompactar no celular.
- O comprador baixa pelo e-mail de compra aprovada ou em Minhas compras. Isso bate com a copy
  ("chega no seu e-mail o link para baixar o arquivo, pela Hotmart").
- **Área de membros (Hotmart Club)** fica para o formato Curso online; para um PDF único não traz
  vantagem e exige módulo/aula. Não usar agora.
- "Arquivos para baixar" (ZIP) exigiria ainda um PDF de "Manual de Instruções" separado. Não vale a
  pena.
- ⚠️ **DRM Social: NÃO ativar.** A proteção de PDF da Hotmart inclui bloqueio de impressão e senha
  ([215827938](https://help.hotmart.com/pt-br/article/215827938/)), e o produto existe para ser impresso.

**✅ Resolvido (2026-11-26):** a capa do PDF principal e as capas dos 7 bumps já trazem "por Gefferson Balles" (regra do eBook, [215828518](https://help.hotmart.com/pt-br/article/215828518/)).

---

## 2. Passo a passo no painel — produto principal

Endereço: https://app.hotmart.com (login do dono; o Claude não digita senha).

### Passo 1 — Criar o produto
1. Menu lateral **Produtos > Meus produtos**.
2. Canto superior direito: **+ Criar produto**.
3. Formato: **eBook**.

### Passo 2 — Aba Informações

| Campo | Texto para colar |
|---|---|
| **Nome do produto** | `Dez Minutinhos – Caderno de Atividades para Imprimir (4 a 10 anos)` |
| Nome curto (se o campo recusar o longo) | `Dez Minutinhos` |
| **Descrição** | o texto longo abaixo (1.131 caracteres; mínimo exigido: 200) |
| Descrição curta (usar se houver limite menor ou em outro campo de resumo) | o texto curto abaixo (261 caracteres) |
| **Imagem do produto** | `hotmart/imagem-produto.png` (1200 × 1200, PNG, 0,3 MB) |
| **Idioma** | Português |
| **Categoria** | sugestão: **Educacional**; alternativa: **Hobbies**. Os nomes exatos da lista **não foram confirmados** — escolher o que existir no menu. Evitar "Saúde e Esportes" e "Desenvolvimento Pessoal" |
| **Mercado de atuação** | Brasil (opção exata **não confirmada**) |

**Descrição longa (colar no campo Descrição):**

```
Dez Minutinhos é um caderno de atividades em PDF para imprimir em casa, feito para crianças de 4 a 10 anos. São 120 atividades de papel e lápis: labirintos, ligue os pontos, jogo dos 7 erros, sudoku, caça-palavras, código secreto, sequências e jogos de memória.

As atividades vêm em dois níveis. Nível 1 (4 a 6 anos): sem leitura, com a instrução em uma linha para o adulto ler. Nível 2 (7 a 10 anos): leitura inicial e desafios maiores.

Cada nível tem um plano de 30 dias com duas folhas por dia, de tipos diferentes, que levam uns 10 minutos. No fim do arquivo há gabarito completo para o adulto conferir.

O arquivo é um PDF em tamanho A4, com 149 páginas e traço pensado para impressora preto e branco. No mesmo arquivo vêm 3 bônus: quadro de conquistas com 6 certificados, uma lista com 30 ideias de brincadeiras que não precisam de impressão e um guia de 2 páginas para o adulto.

Pode imprimir quantas vezes quiser para as crianças da sua família. Não é permitido revender nem repassar o arquivo. Produto digital: nada é enviado pelo correio. O acesso é liberado depois da confirmação do pagamento. Garantia de 7 dias.
```

**Descrição curta:**

```
Caderno em PDF para imprimir com 120 atividades de papel e lápis (labirintos, memória, padrões, lógica e mais) para crianças de 4 a 10 anos, em 2 níveis. Plano de 30 dias com 2 folhas por dia, gabarito completo e 3 bônus. Formato A4, funciona em preto e branco.
```

**Palavras-chave** (campo de palavras-chave/tags **não confirmado** no cadastro; usar se aparecer
no produto, na Página de Produto ou no Hotmart Pages):
`atividades para imprimir`, `caderno de atividades`, `atividades infantis`, `atividades 4 a 10 anos`,
`labirinto para imprimir`, `passatempo infantil`, `atividades sem tela`, `férias`, `PDF para imprimir`,
`sudoku infantil`, `caça-palavras infantil`.

Clique em **Próximo**.

### Passo 3 — Aba Precificação

| Campo | Valor |
|---|---|
| Moeda | Real (BRL) |
| Valor | **R$ 37,00** |
| Garantia | **7 dias** |
| Forma de pagamento | ⚠️ **decisão do dono** (não dá para trocar depois de criar a oferta). Sugestão: **Parcelado com taxas para o cliente, até 5x** (R$ 37 ÷ 5 = R$ 7,40, acima da parcela mínima de R$ 7). A copy já diz "à vista ou parcelado no cartão" |
| Projeto Hotmart One | decisão do dono (doa parte das vendas; sugestão: não, por ora) |
| Conversão de moeda | Não (venda só no Brasil) |

Sem assinatura (dono confirmou venda única em 2026-11-26). Clique em **Salvar e continuar**.

Conta de referência: taxa Hotmart em R$ 37,00 = 9,9% (R$ 3,66) + R$ 2,49 = **R$ 6,15**; sobra
≈ R$ 30,85 antes de impostos e de taxa de parcelamento ([208298448](https://help.hotmart.com/pt-br/article/208298448/)).

### Passo 4 — Painel do produto > aba Conteúdo
1. Subir `produto/final/dez-minutinhos.pdf` (capa já com o nome do autor).
2. Nome do autor: `Gefferson Balles`.
3. **Não** ativar Proteção para ebooks (DRM Social).

### Passo 5 — Precificação e ofertas (conferir a oferta criada)
Produtos > produto > **Precificação e ofertas** ([215827788](https://help.hotmart.com/pt-br/article/215827788/)).

| Campo da oferta | Texto |
|---|---|
| Nome deste preço (interno) | `Principal R$ 37 – página ballestech` |
| Descrição na página de pagamento | `120 atividades para imprimir · 2 níveis (4 a 10 anos) · plano de 30 dias · gabarito · 3 bônus` |

Copiar o **link de pagamento** dessa oferta: é o `LINK_CHECKOUT` que entra em `pagina/dados.json`
e nos botões da página (quem republica é o `construtor-de-pagina`; não mexi em `pagina/`).

### Passo 6 — Página do produto
1. **Sua página externa > Configurar página**: `https://ofertas.ballestech.com.br/dez-minutinhos/`
   ([360017889651](https://help.hotmart.com/pt-br/article/360017889651/)).
2. **Marketplace:** sugestão **desligar** por enquanto (tráfego é nosso; a vitrine da Hotmart
   pediria texto e vitrine próprios). Decisão do dono.

### Passo 7 — Configurações de pagamento (checkout)
Ferramentas > Ver todas > **Configurações de pagamento** > produto
([360038937471](https://help.hotmart.com/pt-br/article/360038937471/)).

| Campo | Valor |
|---|---|
| E-mail de suporte | `acessos@ballestech.com.br` |
| Dados solicitados | Nome, e-mail, CPF/CNPJ (obrigatório), celular. Endereço: recomendado pela Hotmart para nota fiscal — decisão do dono (pode baixar a conversão) |
| Formas de pagamento | Cartão, Pix, boleto (deixar as padrão) |
| Nome que aparece na fatura (máx. 22) | `DEZ MINUTINHOS` (14 caracteres) |
| Notificações de "outras pessoas compraram" | **Desligado** (seria prova social; regra 3) |
| Página de Obrigado | da própria Hotmart (padrão) |
| Idioma | Português |

### Passo 8 — Aparência da Página de Pagamento
Ferramentas > Ver todas > **Aparência da Página de Pagamento** > produto > template
([115003134331](https://help.hotmart.com/pt-br/article/115003134331/)).
- Cor de destaque: laranja `#ff7a45`; fundo creme `#fff7f1`.
- Componente **Selo de garantia**: sim (7 dias).
- Componentes **Avaliações** e **Contagem regressiva**: **NÃO** usar (regras 3 e 4: sem avaliação
  sem compradores reais, sem urgência falsa).
- Exit pop-up: não (evita cara de pressão; pode ser testado depois sem desconto falso).
- Configurar também a versão desktop (ícone de monitor; dá para copiar o modelo do celular).
- É nesta tela que entram os order bumps (seção 4). Atenção: duplicar a página **não** duplica os bumps.

### Passo 9 — Dados pessoais e Finalizar cadastro
1. Conferir aba **Dados pessoais** completa (pessoa física, Gefferson Balles).
2. **Painel > Finalizar cadastro** (aceita o Termo de Tratamento de Dados Pessoais).
3. Esperar a verificação (≈ 15 min, até 1 dia útil). Se vier "Ajustes pendentes", ler no painel
   ([31594947721485](https://help.hotmart.com/pt-br/article/31594947721485/)).

---

## 3. Os 7 produtos de order bump

Cada bump é **um produto eBook próprio**, cadastrado com os mesmos passos 1 a 5 e 9 (sem página
externa e com Marketplace desligado). Ordem do checkout: do mais barato/óbvio ao mais caro.

**Situação dos arquivos (2026-11-26, atualizado):** os 7 bumps têm PDF final em `produto/bumps/` e imagem 1200×1200 em `hotmart/imagem-bump-N.png`; quantidades conferidas com os PDFs (bolsa 30 atividades/20 págs, recortar 40/47, cartas 48/10, matemática 60/70, letras 60/69, jogos 5 jogos/12, volume 2 120/140). Capas com "Complemento do Dez Minutinhos" ("Continuação" no Volume 2) e "por Gefferson Balles".

⚠️ Antes de colar, **conferir as quantidades** (30, 40, 48, 60, 5 jogos, 120) com o PDF final de
cada bump. Se o número mudar no PDF, mudar aqui também. Todo PDF precisa de capa com "Gefferson
Balles".

Parcelamento dos bumps (parcela mínima R$ 7): bumps 1 e 2 só à vista; 3 a 6 até 2x; 7 até 3x.
Sugestão: deixar **todos à vista** para simplificar (decisão do dono).

Bump 1 (R$ 9,90) é microtransação (≤ R$ 10): taxa de 20% = R$ 1,98
([208298448](https://help.hotmart.com/pt-br/article/208298448/)).

### Bump 1 — R$ 9,90
- **Nome do produto:** `Dez Minutinhos – Para Levar na Bolsa`
- **Título no checkout:** `Para levar na bolsa: 30 atividades em meia folha`
- **Descrição no checkout:** `Tamanho A5, para restaurante, viagem e sala de espera. Dobra e cabe na bolsa.`
- **Descrição do produto (≥ 200):**
  ```
  Complemento do caderno Dez Minutinhos. São 30 atividades de papel e lápis em meia folha (tamanho A5), para levar dobradas na bolsa e usar no restaurante, na viagem ou na sala de espera. Nos dois níveis: 4 a 6 anos e 7 a 10 anos. PDF para imprimir, com gabarito.
  ```
- Arquivo: ✅ `produto/bumps/1_para-levar-na-bolsa/para-levar-na-bolsa.pdf` · Imagem: ✅ `hotmart/imagem-bump-1.png`

### Bump 2 — R$ 12,90
- **Nome do produto:** `Dez Minutinhos – Recortar e Colar`
- **Título no checkout:** `Tesoura e cola: 40 atividades de recortar e colar`
- **Descrição no checkout:** `Para fazer com tesoura sem ponta e cola branca. Tem atividades para os dois níveis.`
- **Descrição do produto:**
  ```
  Complemento do caderno Dez Minutinhos. São 40 atividades de recortar e colar para imprimir, pensadas para tesoura sem ponta e cola branca, com a supervisão de um adulto. Divididas em dois níveis: 4 a 6 anos e 7 a 10 anos. PDF em A4, funciona em preto e branco.
  ```
- Arquivo: ✅ `produto/bumps/2_recortar-e-colar/recortar-e-colar.pdf` · Imagem: ✅ `hotmart/imagem-bump-2.png`

### Bump 3 — R$ 14,90
- **Nome do produto:** `Dez Minutinhos – Cartas de Conversa`
- **Título no checkout:** `Cartas de conversa: 48 perguntas para a família`
- **Descrição no checkout:** `Para recortar e usar no jantar, no carro ou antes de dormir. Perguntas leves sobre o dia, imaginação e preferidos, sem lição.`
- **Descrição do produto:**
  ```
  Complemento do caderno Dez Minutinhos. São 48 cartas em 4 temas (meu dia, imaginação, "e se…?" e preferidos), para imprimir, recortar e usar na mesa do jantar, no carro ou antes de dormir. Não é lição: é um jeito leve de puxar conversa. PDF em A4 para imprimir.
  ```
- Arquivo: ✅ `produto/bumps/3_cartas-de-conversa/cartas-de-conversa.pdf` · Imagem: ✅ `hotmart/imagem-bump-3.png`

### Bump 4 — R$ 17,90
- **Nome do produto:** `Dez Minutinhos – Matemática Brincando`
- **Título no checkout:** `Matemática brincando: 60 atividades de contas e mercadinho`
- **Descrição no checkout:** `Contar, somar, subtrair e brincar de mercadinho com fichas de brincar. Nos dois níveis.`
- **Descrição do produto:**
  ```
  Complemento do caderno Dez Minutinhos. São 60 atividades para imprimir com números: contar, somar, subtrair e brincar de mercadinho com fichas de brincar (não são dinheiro de verdade nem imitam cédulas). Divididas em dois níveis, 4 a 6 anos e 7 a 10 anos, com gabarito. PDF em A4.
  ```
- Arquivo: ✅ `produto/bumps/4_matematica-brincando/matematica-brincando.pdf` · Imagem: ✅ `hotmart/imagem-bump-4.png`

### Bump 5 — R$ 17,90
- **Nome do produto:** `Dez Minutinhos – Letras e Palavras`
- **Título no checkout:** `Letras e palavras: 60 atividades de alfabeto, sílabas e caça-palavras`
- **Descrição no checkout:** `Nível 1 com letras e sons. Nível 2 com palavras e frases curtas.`
- **Descrição do produto:**
  ```
  Complemento do caderno Dez Minutinhos. São 60 atividades para imprimir com letras e palavras: alfabeto, sílabas, caça-palavras e frases curtas. Nível 1 (4 a 6 anos) com letras e sons; Nível 2 (7 a 10 anos) com palavras e frases. Com gabarito. PDF em A4, funciona em preto e branco.
  ```
- Arquivo: ✅ `produto/bumps/5_letras-e-palavras/letras-e-palavras.pdf` · Imagem: ✅ `hotmart/imagem-bump-5.png`

### Bump 6 — R$ 19,90
- **Nome do produto:** `Dez Minutinhos – Jogos de Mesa para Imprimir`
- **Título no checkout:** `5 jogos para imprimir: bingo, dominó, memória, trilha e jogo da velha`
- **Descrição no checkout:** `Cinco jogos para a família jogar junto. Regras de cada um em 1 página.`
- **Descrição do produto:**
  ```
  Complemento do caderno Dez Minutinhos. São 5 jogos de mesa para imprimir e montar em casa, bingo, dominó, jogo da memória, trilha e jogo da velha, com as regras de cada um em uma página. Para jogar em família com crianças de 4 a 10 anos. PDF em A4 para imprimir.
  ```
- Arquivo: ✅ `produto/bumps/6_jogos-de-mesa/jogos-de-mesa.pdf` · Imagem: ✅ `hotmart/imagem-bump-6.png`

### Bump 7 — R$ 27,00
- **Nome do produto:** `Dez Minutinhos – Volume 2`
- **Título no checkout:** `Volume 2: mais 120 atividades novas e mais 30 dias de plano`
- **Descrição no checkout:** `Mesmas categorias e os mesmos dois níveis, nenhuma atividade repetida do Volume 1. Com gabarito.`
- **Descrição do produto:**
  ```
  Continuação do caderno Dez Minutinhos. São mais 120 atividades novas para imprimir, nas mesmas categorias (atenção, memória, padrões, lógica, traçado, cores e códigos) e nos mesmos dois níveis, 4 a 6 e 7 a 10 anos, sem repetir nenhuma do Volume 1. Com plano de 30 dias por nível e gabarito. PDF em A4.
  ```
- Arquivo: ✅ `produto/bumps/7_volume-2/volume-2.pdf` · Imagem: ✅ `hotmart/imagem-bump-7.png`

### Montar os bumps no checkout (depois de os 7 produtos estarem aprovados)
Ferramentas > **Aparência da Página de Pagamento** > produto Dez Minutinhos > Editar > **Order Bump**
> Selecionar Produto (oferta do bump) > Inserir (área pontilhada) > repetir para os 7, na ordem
1 → 7 > **Salvar alterações** > **Publicar** ([360019967392](https://help.hotmart.com/pt-br/article/360019967392/)).
Se aparecerem campos de título/descrição/imagem do bump, colar os textos acima (limites **não
confirmados**: se cortar, encurtar a descrição para a 1ª frase).

### Pós-compra "Coleção Ano Inteiro" (R$ 47,00)
Fora do cadastro de amanhã: o produto não existe ainda e a ferramenta de funil/pós-compra
**não foi pesquisada** (não confirmado).

---

## 4. Pixel da Meta e API de Conversões

Pré-requisito (outro passo da Etapa 5): Pixel criado no Gerenciador de Eventos ligado à conta de
anúncios. Nome sugerido: `Pixel Oferta Dez Minutinhos`.

**Dados que entram depois:**
- ID do pixel: `________________` (número; pode ficar anotado em `campanha.md`, não é segredo)
- Token da API de Conversões: **o dono gera no Gerenciador de Eventos e cola direto no campo da
  Hotmart.** Não escrever aqui, não colar no chat, não salvar em arquivo.

**Passos na Hotmart** ([115004826368](https://help.hotmart.com/pt-br/article/115004826368/),
[6565866201741](https://help.hotmart.com/pt-br/article/6565866201741/)):
1. Ferramentas > Ver todas > **Pixel de Rastreamento**.
2. Produto: **Dez Minutinhos** > **Facebook + Instagram** (o mesmo pixel serve aos dois).
3. Colar o **ID do pixel** > Continuar.
4. Eventos:
   - ✅ **Visitas na Página de pagamento** → InitiateCheckout
   - ✅ **Vendas realizadas** → Purchase
   - ⬜ Visitas na Página de produto Hotmart (não usamos a página da Hotmart)
5. Configurações avançadas de vendas:
   - Método de pagamento: **Todos os métodos de pagamento**
   - Diferenciar imediato e não imediato: **Sim** (Purchase só para cartão; Pix/boleto gerado vira
     "Payment Generated"; evita contar boleto não pago como venda)
   - Valor enviado: **Valor da transação**
6. Envio: **Web e API de Conversões** (um cobre falha do outro). Na API, **o dono cola o token**.
7. **Salvar**.
8. Repetir 1–7 em **cada um dos 7 produtos de bump** (senão a venda do bump não chega à Meta).
9. Não há mais campo de domínio a configurar ([9025315539981](https://help.hotmart.com/pt-br/article/9025315539981/)).

O PageView da página de vendas é do código do pixel no `pagina/index.html` (troca de
`<!-- PIXEL META -->`, skill `cadastro-e-pixel`, passo 4) — não é feito na Hotmart.
Teste: Meta Pixel Helper no checkout (eventos Web); eventos só via API não aparecem no navegador,
conferir no Gerenciador de Eventos. Registrar PageView / InitiateCheckout / Purchase em `campanha.md`.

---

## 5. Checklist de amanhã

- [ ] PDF principal com "Gefferson Balles" na capa (criador-de-produto) — **bloqueia o passo 4**
- [ ] Dono decide: forma de pagamento/parcelas, Hotmart One, Marketplace, pedir endereço no checkout
- [ ] Produto principal: passos 1 a 9 → aguardar aprovação
- [ ] Link de pagamento → `pagina/dados.json` (`LINK_CHECKOUT`) → republicar página (construtor-de-pagina)
- [ ] PDFs dos bumps 1–6 prontos e conferidos; Volume 2 conferido; capas com autor
- [ ] Imagens dos 7 bumps (a partir das capas reais)
- [ ] 7 produtos de bump cadastrados e aprovados
- [ ] 7 bumps inseridos no checkout, na ordem, e publicados
- [ ] Pixel no principal + nos 7 bumps (ID pelo Claude; token pelo dono)
- [ ] Compra de teste? A Hotmart não foi pesquisada sobre compra-teste — **não confirmado**; se
      fizer compra real, pedir reembolso em seguida
- [ ] Registrar tudo no `status.md` (etapa 9) e em `campanha.md`

## Não confirmado (resumo)
- Limite máximo de caracteres do nome e da descrição do produto.
- Dimensão em pixels da imagem do produto (só formato e 5 MB são oficiais).
- Nomes exatos das categorias e do "mercado de atuação"; existência de campo de palavras-chave.
- Número máximo de bumps na Central de Ajuda (só a página comercial diz "até nove").
- Limite de caracteres dos campos do bump e se o produto do bump precisa estar aprovado antes de ser
  escolhido.
- Ferramenta de pós-compra (funil) e compra de teste.
- Caminho exato na Meta para gerar o token (a Hotmart só diz "Gerenciador de Eventos").
- Há divergência de menu entre artigos: Aparência da Página de Pagamento aparece em "menu lateral >
  Ferramentas" ([360019967392](https://help.hotmart.com/pt-br/article/360019967392/)) e em "menu de
  9 pontos > Ferramentas > Ver todas" ([115003134331](https://help.hotmart.com/pt-br/article/115003134331/)).
  Usar a busca do menu Ferramentas.

---

## Decisões do dono (2026-11-26)
- **Parcelamento do principal:** até **5x, com juros pagos pelo cliente** (a página já diz isso). Bumps: à vista (parcela mínima R$ 7).
- **Marketplace da Hotmart:** **ligado** (deixar o produto visível no Marketplace).
- **Endereço do comprador no checkout:** não pedir (produto digital).
- **Vendedor identificado na página:** Balles Tech Energia Ltda · CNPJ 57.165.092/0001-87 · Rua do Cara, 1379SW, Qd 26, Lt 05, Sala 01, Cidezal I, Sapezal/MT, CEP 78365-038. Autor do conteúdo na capa: Gefferson Balles.
  ⚠️ Conferir se a conta de produtor da Hotmart está no CNPJ (o recebedor deve ser o mesmo que aparece na página).
