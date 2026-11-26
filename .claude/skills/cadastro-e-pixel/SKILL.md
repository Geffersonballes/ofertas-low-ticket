---
name: cadastro-e-pixel
description: Etapa 5 — cadastra o produto e o .zip na Weven, cria a Página do Facebook, cria o Pixel, instala o PageView na página e cadastra ID + token da API de Conversões na Weven. Use depois do Portão 3.
---
Entrada: `[NOME_PIXEL]` (padrão "Pixel Oferta <Nome>"), `[NOME_CONTA]` de anúncios/BM.

Weven, Facebook e Gerenciador de Eventos só têm interface web. Se houver navegador do dono
conectado (extensão do Chrome/Remote Control), opere as abas; senão, gere o passo a passo
exato e peça ao dono os dados de volta (link do checkout, ID do pixel).

1. **Weven:** produto, preço, descrição, .zip de entrega, order bumps e pós-compra.
2. **Página do Facebook:** nome simples da marca, categoria, descrição, e-mail de suporte real.
   Gere logo (foto de perfil) e capa. Sem Instagram nesta fase.
3. **Pixel novo** `[NOME_PIXEL]` ligado à conta `[NOME_CONTA]`.
4. **PageView na página:** troque `<!-- PIXEL META -->` em `pagina/index.html` pelo código
   do pixel e republique (Hostinger). Troque `{{LINK_CHECKOUT}}` pelo link da Weven.
5. **API de Conversões:** ID do pixel + token cadastrados na integração da Weven. O token é
   segredo: o dono cola direto na Weven — nunca no chat, nem no repositório.
6. Teste os eventos (PageView, InitiateCheckout, Purchase) e registre em `campanha.md`.
