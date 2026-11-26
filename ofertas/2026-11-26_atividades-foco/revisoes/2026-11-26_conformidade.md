# Portão 2 — Conformidade · Dez Minutinhos

- Data: 2026-11-26 · Revisor: revisor-de-conformidade
- Escopo: página publicada (prévia) + `pagina/index.html`, `privacidade.html`, `termos.html`; produto
  `produto/final/dez-minutinhos.pdf` (amostragem em `produto/gerador/saida/completo-*.png`) e
  `produto/sumario.md`; 7 bumps (`bumps/bumps.md`, capas e páginas `saida/bump-*-NNN.png`);
  `criativos/roteiros.md`; `hotmart/kit-cadastro.md`. Referência: `dossie.md` (NeuroKids).
- Critérios: políticas de anúncio da Meta, CDC (arts. 6º, 30, 31, 37, 49), Decreto 7.962/2013,
  LGPD (art. 9º), originalidade, prova social, regras do `CLAUDE.md`.

## Veredito geral: APROVADO COM AJUSTES

Nada exige voltar etapa. Os ajustes abaixo marcados **obrigatórios** têm de ser feitos antes do
Portão 4 (publicar anúncio). Os **recomendados** não bloqueiam.

| Peça | Veredito |
|---|---|
| Página (index + legais) | APROVADO COM AJUSTES |
| Produto principal | APROVADO |
| Order bumps (PDFs) | APROVADO COM AJUSTES |
| Criativos | APROVADO COM AJUSTES |
| Textos da Hotmart | APROVADO COM AJUSTES |

---

## 1. Página de vendas — APROVADO COM AJUSTES

### O que está conforme
- Sem depoimento, estrela, número de clientes, selo falso, contador ou "só hoje". Sem "de/por".
- Sem saúde, cérebro, TDAH, foco/calma como resultado, prazo de resultado. "Não é para você se…
  espera tratamento" e os termos ("não é tratamento, avaliação nem acompanhamento") delimitam bem.
- Título e ganchos falam da situação (tablet, fim de tarde, férias), não de atributo da criança ou
  do adulto.
- Imagens: só mockups e páginas reais do caderno; nenhuma criança, rosto ou pessoa.
- Preço claro (R$ 37,00, "uma vez só", sem mensalidade); âncora por custo é conta real
  (37/30 = 1,23; 37/120 = 0,31).
- Garantia de 7 dias visível no topo, nos selos, em bloco próprio, no FAQ e no fecho, com o canal
  (Hotmart ou e-mail).
- Versão publicada: rodapé e páginas legais com nome, CPF e e-mail de suporte preenchidos; sem
  `{{...}}` sobrando.
- Tudo o que a página promete existe no produto (ver seção 2).
- Originalidade: nome, marca, textos e imagens próprios; nenhuma frase traduzida da NeuroKids. Da
  referência ficaram só estrutura e ideia (10 min/dia, sem tela, categorias, tabela comparativa),
  o que é modelagem permitida.

### Ajustes obrigatórios
1. **Link do checkout** — `pagina/index.html`, todos os `href="{{LINK_CHECKOUT}}"` (na prévia,
   todos apontam para `#preco`, inclusive o botão do próprio bloco de preço). Correção: trocar
   pelo link de pagamento da oferta Hotmart e republicar. Sem isso o anúncio leva a uma página
   que não vende (sem ele, nada vai para o Portão 4).
2. **Parcelamento sem número de parcelas** — `index.html`, `.cond` "à vista ou<br>parcelado no
   cartão" (topo e bloco de preço) e FAQ "Quais as formas de pagamento?" ("ou parcelado no
   cartão"). CDC art. 31 e art. 52. Correção: quando o dono decidir, escrever o número máximo de
   parcelas e se tem juros. Ex.: "à vista ou em até 5x no cartão (com juros da Hotmart; o valor de
   cada parcela aparece no checkout)". Se for sem juros: "ou em até 5x sem juros".
3. **"Acesso na hora"** — `index.html`: `.faixa` "Acesso na hora, pelo e-mail"; selo "Acesso na
   hora / o link chega no seu e-mail"; nota do fecho "Acesso na hora, pelo e-mail". Com boleto
   ligado no checkout o acesso não é na hora (só após compensação). Correção: "Acesso logo após o
   pagamento aprovado" (selo: "Acesso rápido / o link chega no seu e-mail assim que o pagamento é
   aprovado"). Alternativa: o dono desliga o boleto e o texto pode ficar.
4. **Endereço do fornecedor** — rodapé de `index.html`, `privacidade.html` e `termos.html`
   ("Responsável: … · CPF … · Contato: …"). O Decreto 7.962/2013, art. 2º, II, pede **endereço
   físico e eletrônico**; hoje só há o e-mail. Correção (decisão do dono, nunca endereço falso):
   incluir um endereço real para correspondência (pode ser comercial/fiscal). Sugestão para não
   expor casa e CPF: abrir MEI e usar CNPJ + endereço comercial.
5. **Política de privacidade incompleta (LGPD art. 9º)** — `privacidade.html`. Faltam o prazo de
   guarda e as bases legais. Correção: incluir uma seção, p. ex.:
   "**Por quanto tempo guardamos:** os dados da compra ficam guardados enquanto forem necessários
   para suporte e garantia e pelo prazo exigido pela lei fiscal (até 5 anos). Depois são apagados.
   **Base legal:** execução do contrato de compra (dados da compra) e consentimento/legítimo
   interesse para os cookies de medição de anúncios." E acrescentar aos direitos: "revogar o
   consentimento e reclamar à ANPD".

### Recomendados
- `index.html`, `.obs`: "Os 10 minutos são só o tamanho médio" — não há medição; trocar por "Os 10
  minutos são uma referência", como no guia do adulto (p. 148).
- Refazer `img/heroi.webp`, `img/mockup-capa.webp` e `img/mockup-pacote.*` a partir do PDF final:
  a capa nos mockups ainda é a versão sem "por Gefferson Balles", e as etiquetas das folhas no
  herói parecem de uma versão anterior (o código secreto, que no produto é só do Nível 2, aparece
  com etiqueta de outro nível/categoria). Não é enganoso, mas o mockup deve bater com o arquivo.
- Pôr aviso simples de cookies quando o pixel for instalado (`<!-- PIXEL META -->`).
- Manter `pagina/index.html` e as legais com os `{{...}}` só se o build substituir tudo; conferir
  a prévia de novo depois de cada republicação.

---

## 2. Produto principal — APROVADO

Conferido em `sumario.md` e nas páginas 1, 2, 3, 5, 11, 66, 78, 80, 128, 141, 142, 143, 146–149.

| Promessa da página | No produto | OK |
|---|---|---|
| 120 atividades | 60 + 60 (sumário; plano N1 p. 5 e N2 p. 67 com 30 dias × 2 folhas) | ✅ |
| 2 níveis de 60 | Nível 1 p. 4–65 (4–6, sem leitura); Nível 2 p. 66–127 (7–10, leitura inicial) | ✅ |
| 6 categorias | Atenção, Memória, Padrões, Lógica, Traçado, Cores e códigos (12/8/10/12/10/8 por nível) | ✅ |
| Plano de 30 dias por nível | p. 5 e p. 67, com páginas e caixa "Feito" | ✅ |
| Gabarito completo | p. 128–141, 9 por página, as 120 cobertas; atividades livres (siga o caminho, copiar) marcadas como "atividade livre" | ✅ |
| 1 atividade por folha | cada página de atividade tem uma atividade, com rodapé "Dia N · Feito!" | ✅ |
| Bônus 1: quadro + 6 certificados | p. 142 (30 dias) + p. 143–145 (2 por página) | ✅ |
| Bônus 2: 30 ideias sem imprimir | p. 146–147, 30 itens; os que envolvem água, cozinha, massinha trazem "adulto por perto / sem faca e sem fogo / não colocar na boca" | ✅ |
| Bônus 3: guia do adulto 2 págs., inclui quando passar do N1 ao N2 | p. 148–149 | ✅ |
| A4, P&B, uso familiar | capa, "Como usar" p. 2 | ✅ |
| Autor na capa (Hotmart) | "por Gefferson Balles" na p. 1 | ✅ |

Sem palavras vetadas, sem rosto de criança, sem marca de terceiros. Nada da NeuroKids reaproveitado.

Observação sem ajuste: a mensagem do código secreto p. 78 ("BRINCAR FAZ BEM") é neutra, não é alegação.

---

## 3. Order bumps (PDFs e `bumps/bumps.md`) — APROVADO COM AJUSTES

Conferidos capa/"como usar" e amostras de: Para levar na bolsa (p. 1–2), Recortar e colar (p. 2),
Cartas de conversa (p. 1–4, 9), Matemática brincando (p. 2–3), Letras e palavras (p. 2), Jogos de
mesa (p. 1), Volume 2 (p. 1). Quantidades da tabela de `bumps.md` batem com capas e "como usar"
(30 · 40 · 48 · 60 · 60 · 5 jogos · 120). Títulos e descrições de checkout em `bumps.md` são fiéis
ao conteúdo. Fichas do mercadinho são próprias e trazem "Não são dinheiro de verdade". Recortar e
colar traz "tesoura sem ponta" e "adulto por perto".

### Ajuste obrigatório
1. **"Bônus extra do Dez Minutinhos" em produto pago** — capa de todos os 7 bumps
   (`produto/bumps/*/*.pdf`, p. 1) e `bumps.md` linha 17. Bônus dá a entender que é grátis; o
   item é vendido à parte (R$ 9,90 a R$ 27,00) e a imagem do bump no checkout será feita a partir
   dessa capa (`kit-cadastro.md`, seção 3). Correção: trocar por **"Complemento do Dez
   Minutinhos"** (Volume 2: "Continuação do Dez Minutinhos"), gerar os PDFs de novo e só então
   gerar as imagens do checkout.

### Recomendado
- Unificar a fonte dos textos de checkout: hoje `bumps.md` e `hotmart/kit-cadastro.md` têm
  títulos/descrições diferentes para os 7 bumps. Usar os de `bumps.md` (mais fiéis) — ver seção 5.

---

## 4. Criativos (`criativos/roteiros.md`) — APROVADO COM AJUSTES

### O que está conforme
- Ganchos sobre atividade/tela/preparo/ocasião; nenhum atributo pessoal ("seu filho se frustra?"
  da referência foi removido corretamente).
- Sem promessa de efeito, sem prazo, sem prova social, sem urgência, sem "de/por". Custo por dia
  sempre com "no plano de 30 dias".
- Só imagens do produto real; proibição explícita de criança, pessoa, IA realista e aparelho
  fotorrealista. Declaração de IA: não marcar está de acordo com o `CLAUDE.md` (voz sintética sobre
  telas do produto, sem pessoa nem evento realista).
- Todos os 5 anúncios têm texto principal, título, descrição e CTA "Saiba mais"; URL de destino
  definida.
- Tudo citado existe no caderno nas páginas indicadas; nenhuma atividade atribuída a nível errado.
- Originalidade: estruturas modeladas, nenhum texto traduzido (p. ex. "Parents are replacing
  screen time…" virou convite direto "Troque 10 minutos de tela…", sem a prova social difusa).

### Ajuste obrigatório
1. **Criativo 1, Descrição:** "O PDF chega no seu e-mail na hora". Mesmo motivo do ajuste 3 da
   página (boleto). Correção: "O PDF chega no seu e-mail após o pagamento". (Se o dono desligar o
   boleto, pode ficar.)

### Recomendados
- Criativo 4, Título "Pediu o tablet? Entregue um labirinto." — ok; se o dono trocar o título da
  página, manter os dois iguais (pendência já anotada no roteiro).
- Criativo 5: rodar só na temporada de férias, como o próprio roteiro diz; fora dela, trocar o
  topo por outra ocasião (nunca por prazo).
- Conjunto de anúncios: público 18+ (o anúncio é para adultos; produto infantil não pode
  segmentar menores).

---

## 5. Textos da Hotmart (`hotmart/kit-cadastro.md`) — APROVADO COM AJUSTES

Conformes: nome, descrição curta, preço R$ 37,00, garantia 7 dias, e-mail de suporte, DRM
desligado, "Avaliações", "Contagem regressiva" e "outras pessoas compraram" desligados. Quantidades
dos 7 bumps (30, 40, 48, 60, 60, 5 jogos, 120) batem com os PDFs.

### Ajustes obrigatórios (o kit é o que será colado no painel)
1. **Descrição longa do produto principal** — "um calendário com 30 ideias de brincadeiras". O
   bônus 2 é uma lista numerada (p. 146–147), não um calendário. Correção: "uma lista com 30 ideias
   de brincadeiras que não precisam de impressão".
2. **Bump 3 (Cartas de conversa)** — título "Hora do jantar com assunto: 48 cartas de conversa
   para recortar"; descrição no checkout "Perguntas simples sobre o dia a dia e o que a criança
   sente"; descrição do produto "gostos e sentimentos… Não é lição nem terapia". O PDF não tem
   cartas sobre sentimentos (categorias: Meu dia, Imaginação, E se…?, Preferidos) e "terapia"
   aproxima o produto de tema de saúde. Correção: usar o texto de `bumps.md` — título "Cartas de
   conversa: 48 perguntas para a família"; checkout "Para recortar e usar no jantar, no carro ou
   antes de dormir. Perguntas leves sobre o dia, imaginação e preferidos, sem lição."; descrição do
   produto: "Complemento do caderno Dez Minutinhos. São 48 cartas com perguntas leves em 4 tipos
   (Meu dia, Imaginação, E se…? e Preferidos), para imprimir, recortar e usar na mesa do jantar, no
   carro ou antes de dormir. Todo mundo responde, adultos também. PDF em A4 para imprimir."
3. **Bump 6 (Jogos de mesa)** — título "bingo, dominó, memória e trilha" e descrição "entre eles
   bingo, dominó, jogo da memória e trilha"; arquivo "pendente (conferir qual é o 5º jogo)". O PDF
   tem 5 jogos. Correção: título "Jogos de mesa para imprimir: bingo, dominó, memória, trilha e
   jogo da velha"; descrição do produto: "…São 5 jogos de mesa para imprimir e montar em casa:
   bingo, dominó, jogo da memória, trilha e jogo da velha, com as regras numa página só…".
4. **Bump 4 (Matemática brincando)** — "dinheirinho de papel" / "dinheirinho de brincar desenhado
   por nós". O PDF traz "Fichas de brincar. Não são dinheiro de verdade." Correção: "fichas de
   brincar de papel (não são dinheiro de verdade)" no checkout e na descrição.
5. **Status desatualizado no kit** — seção 1 ("a capa atual… não tem 'Gefferson Balles'"), seção
   3 ("os bumps 1 a 6 ainda não têm PDF"; cada bump com "Arquivo: ⬜ pendente") e checklist.
   Correção: atualizar para o estado real (capas com autor; 7 PDFs prontos), para quem cadastrar
   não subir arquivo errado ou travar à toa.

### Recomendados
- Bump 1: trocar "Dobra e cabe na bolsa" pelo texto de `bumps.md` ("Imprime duas por folha, corta
  no meio e cabe na bolsa"), que descreve o passo de cortar.
- Bump 5: "Nível 1 com letras e sons" → "Nível 1 com vogais e primeira letra" (é o que o PDF
  traz); título igual ao de `bumps.md` ("alfabeto, sílabas e rimas") ou manter "caça-palavras" —
  ambos existem; só não deixar dois títulos diferentes.
- Bump 7: título do kit ok; preferir o de `bumps.md` para ter uma fonte só.
- Forma de pagamento escolhida pelo dono tem de ser a mesma escrita na página (ajuste 2 da página).

---

## Resumo dos obrigatórios (para quem vai corrigir)

| # | Arquivo | Correção | Dono da correção |
|---|---|---|---|
| 1 | `pagina/index.html` | Link real do checkout em todos os botões | construtor-de-pagina (após cadastro Hotmart) |
| 2 | `pagina/index.html` | Nº de parcelas e com/sem juros (topo, bloco de preço, FAQ) | dono decide → copywriter/construtor |
| 3 | `pagina/index.html` | "Acesso na hora" → "logo após o pagamento aprovado" (ou desligar boleto) | construtor-de-pagina |
| 4 | `index.html`, `privacidade.html`, `termos.html` | Endereço físico real do fornecedor (Decreto 7.962, art. 2º, II) | dono decide → construtor |
| 5 | `pagina/privacidade.html` | Prazo de guarda, bases legais, revogação/ANPD | construtor-de-pagina |
| 6 | `produto/bumps/*/*.pdf` (capas) + `bumps/bumps.md` | "Bônus extra" → "Complemento/Continuação do Dez Minutinhos" | criador-de-order-bumps |
| 7 | `criativos/roteiros.md` (Criativo 1) | Descrição sem "na hora" | roteirista-de-criativos |
| 8 | `hotmart/kit-cadastro.md` | Bônus 2 "lista", não "calendário" | quem mantém o kit |
| 9 | `hotmart/kit-cadastro.md` | Bump 3 sem "sentimentos/terapia"; textos de `bumps.md` | idem |
| 10 | `hotmart/kit-cadastro.md` | Bump 6 com os 5 jogos | idem |
| 11 | `hotmart/kit-cadastro.md` | Bump 4 "fichas de brincar", não "dinheirinho" | idem |
| 12 | `hotmart/kit-cadastro.md` | Atualizar status (autor na capa, 7 PDFs prontos) | idem |

Depois das correções, basta o revisor conferir os itens 1–12 (não precisa refazer a revisão inteira).
