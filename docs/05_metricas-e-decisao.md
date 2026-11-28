# 05 — Métricas e regras de decisão

Estrutura de teste padrão (aula): **2 campanhas CBO** — 1-1-3 e 1-1-2 — com **R$ 35/dia cada**
(R$ 70/dia por oferta), objetivo Vendas (Site), público 100% aberto. Variações: 1-1-1, 1-1-10. As regras abaixo são o ponto de
partida e devem ser ajustadas com os dados reais (registre a mudança e o motivo aqui).

## Números que importam

| Métrica | Fórmula | Alvo inicial |
|---|---|---|
| CPA | gasto ÷ compras | < ticket médio líquido |
| Ticket médio (TM) | faturamento ÷ compras | ≥ R$ 90 |
| ROAS | faturamento ÷ gasto | ≥ 1,5 para manter, ≥ 2 para escalar |
| CTR (link) | cliques ÷ impressões | ≥ 1% |
| Conversão da página | compras ÷ visitas na página | ≥ 2% |
| Aceite de bump | bumps vendidos ÷ compras | ≥ 30% por bump |
| CPM | custo por mil impressões | referência, não decisão |

"Líquido" = depois das taxas da plataforma de checkout (registre a taxa em `campanha.md`).

## Diagnóstico de página/checkout (aula)

Muitos cliques e Initiate Checkout, poucas compras → auditar a página: listar objeções não
respondidas, deixar a primeira dobra mais direta (gancho/transformação/antes e depois),
reforçar os GIFs do entregável na página e nos anúncios, conferir o checkout e os bumps.

## Ofertas com expert/Instagram (não é o padrão)

Sem público aberto: campanha CBO com 4 conjuntos — seguidores do IG; engajamento IG 7d +
PageView 180d; Initiate Checkout 7/15/30d; Direct 7d + PageView 180d. Grupos de 3 anúncios
(A, B, C) e duplicação trocando só os criativos (C, D, E).

## Regras de corte e escala

1. **Dia 1, gastou R$ 70 e 0 vendas e CTR < 0,8%:** problema de criativo → trocar criativos
   uma vez. Se repetir, matar.
2. **CTR bom (≥ 1%) mas 0 vendas após ~1,5× o ticket gasto:** problema de página/preço →
   revisar página uma vez. Se repetir, matar.
3. **ROAS entre 1 e 1,5 por 3 dias:** manter, testar novos bumps e novos criativos.
4. **ROAS ≥ 2 por 3 dias seguidos:** escalar +20–30% do orçamento a cada 48 h, ou duplicar o
   conjunto vencedor.
5. **ROAS < 1 por 3 dias depois de ajustes:** matar e registrar o aprendizado.

Toda decisão é **sugerida** pelo `analista-de-metricas` e **executada pelo dono**.


## Time de dados (2026-11-28)

| Especialista | Pergunta que responde |
|---|---|
| `analista-de-metricas` | coordena: coleta (Windsor + Hotmart), chama os outros, atualiza o painel |
| `analista-de-funil` | em que ponto do funil o dinheiro vaza e qual o conserto |
| `analista-de-criativos` | qual ângulo/gancho/formato para, assiste e vende |
| `analista-financeiro` | lucro real por venda, CPA máximo, quanto escalar |
| `analista-de-testes` | a diferença é real ou acaso? quanto dado falta? |

A leitura deles aparece no painel (`diagnosticos` em `painel/site/dados.json`).
