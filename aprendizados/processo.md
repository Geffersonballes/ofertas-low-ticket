# Aprendizados de processo — o que já deu errado e como não repetir

Leia antes de cada etapa (regra 8 do `CLAUDE.md`). Cada linha: data · oferta · o que aconteceu → regra.
O que **vende** fica em `o-que-vende.md`; aqui fica **como trabalhar** com menos retrabalho.

## Ordem da esteira
- 2026-11-28 · Dez Minutinhos · Hotmart, criativos e campanhas foram feitos antes da revisão página por
  página do material → **Portão M**: revisar e aprovar o conteúdo primeiro (`revisar-material`,
  `ferramentas/conferir_material.py`). Só então Hotmart → criativos → campanhas.

## Material (infoproduto)
- (preencher com os achados da revisão de 2026-11-28: tipo de erro → regra para o gerador)

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
