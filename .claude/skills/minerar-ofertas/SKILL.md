---
name: minerar-ofertas
description: Etapa 1 — minera ofertas low ticket em inglês (white, tráfego direto, muitos anúncios ativos há 14+ dias) e grava o radar do dia. Use quando o dono disser "minere ofertas", "buscar ofertas" ou mandar links da Biblioteca de Anúncios para avaliar.
---
1. Leia `docs/03_mineracao.md`.
2. Se o dono mandou links (do minerador externo ou próprios), avalie esses. Senão, chame o
   agente `minerador-de-ofertas` para buscar (meta: 5 a 10 candidatas que passem no corte).
3. Grave `mineracao/AAAA-MM-DD.md` a partir de `mineracao/_modelo.md`. Por candidata:
   nome, resumo do produto, estimativa de anúncios ativos, link da página de vendas, link
   da Biblioteca de Anúncios e pontuação.
4. Devolva as 3 melhores e pergunte qual vira oferta (Portão 1).
