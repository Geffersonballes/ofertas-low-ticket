# 08 — Inteligência de anúncios: o que realmente vende

Pesquisa de "dicas" não prevê venda. O que prevê venda são **números**, de dois lugares:
1. **Antes de gastar:** sinais que a concorrência já pagou para descobrir (tempo de vida dos anúncios).
2. **Depois de gastar pouco:** os nossos números, lidos com regras fixas, anúncio por anúncio.

E tudo o que se aprende vira arquivo no repositório, para o minerador e o operador usarem.

## As três camadas

| Camada | Quem roda | Agente | Saída |
|---|---|---|---|
| 1. Sinais externos (antes de gastar) | **Marcos** (no pacote) e **Gefferson** (antes de criar anúncios) | `pesquisador-de-anuncios` | `pesquisas/AAAA-MM-DD_<tema>.md` + `aprendizados/padroes-externos.md` |
| 2. Funil por anúncio (depois de gastar) | **Gefferson** (diário) | `analista-de-metricas` | `resultados/painel.md` + recomendação de corte/escala |
| 3. Aprendizado acumulado | os dois (automático) | `analista-de-metricas` e `pesquisador-de-anuncios` | `aprendizados/o-que-vende.md` |

## Como os dois ficam ligados

```
          MARCOS (minerador)                         GEFFERSON (operador)
  lê aprendizados/o-que-vende.md  ◄──────────── analista grava o que vendeu (diário)
  roda pesquisador-de-anuncios                  lê a seção "Inteligência de anúncios"
  ──► pacote de oferta (PR) com a seção  ─────► do dossiê para escrever os roteiros
      "Inteligência de anúncios" no dossiê       publica, mede, corta e escala
```

- **Canal:** o repositório no GitHub (pull requests, arquivos de aprendizado) + o grupo de WhatsApp
  para avisos ("pacote novo", "anúncio X venceu").
- **Marcos não vê a conta de anúncios.** Ele vê o que o analista escreve em `aprendizados/` e
  `resultados/painel.md` — números e conclusões, sem acesso a dinheiro.
- **Gefferson decide** tudo o que gasta dinheiro. Os agentes só recomendam.

## Camada 1 — sinais externos (Biblioteca de Anúncios)

O sinal mais confiável e grátis: **anúncio que fica no ar por semanas dá lucro** (ninguém paga
prejuízo por 30 dias). O `pesquisador-de-anuncios` levanta, para um nicho ou uma oferta:
- ganchos, formatos e ângulos que se repetem nos anúncios **ativos há 30+ dias**;
- quantas **variações** o anunciante fez de cada um (muitas = está escalando);
- o que os anúncios que **morreram em menos de 7 dias** têm em comum;
- duração dos vídeos, tipo de abertura, se mostra o produto por dentro, CTA.

Cada padrão leva **evidência** (anunciante, nº de anúncios, dias no ar, link) e um grau:
**forte** (3+ anunciantes, 30+ dias), **médio** (1–2 anunciantes ou 14–30 dias), **fraco/opinião**
(só artigo, vídeo de YouTube ou "guru"). YouTube e Google entram só para **táticas de
configuração** e sempre como "opinião — a testar".

Limite honesto: a Biblioteca bloqueia acesso automático. O agente usa espelhos públicos
(AdManage, AdScan etc.) e pede **conferência manual** dos números-chave (prints), como na mineração.

## Camada 2 — funil por anúncio

| Etapa | Métrica | Mostra | Meta inicial |
|---|---|---|---|
| Parou de rolar | **Taxa de gancho** = visualizações de 3 s ÷ impressões | se os 3 primeiros segundos prendem | ≥ 25% |
| Assistiu | **Retenção** = ThruPlay ÷ visualizações de 3 s | se o vídeo segura | ≥ 15% |
| Clicou | **CTR no link** = cliques no link ÷ impressões | se a promessa interessa | ≥ 1% |
| Chegou | Visualizações da página ÷ cliques no link | se a página carrega | ≥ 75% |
| Quis comprar | **Início de checkout** ÷ visualizações da página | se a página convence | ≥ 8% |
| Comprou | **CPA** e **ROAS** | se dá lucro | CPA ≤ R$ 45 · ROAS ≥ 1,5 |

CPA máximo: ticket médio estimado R$ 65 − taxa Hotmart ≈ R$ 56 líquidos por venda; R$ 45 deixa
margem. **Trocar pela conta real** assim que houver 20+ vendas (registrar aqui a mudança).

### Regras de corte e escala (por anúncio)
1. Gastou **R$ 15** e taxa de gancho < 15% → **desligar** (abertura não funciona).
2. Gastou **R$ 30** e CTR no link < 0,8% → **desligar** (promessa não interessa).
3. Gastou **R$ 56** (1 venda líquida) sem nenhum início de checkout → **desligar**.
4. CTR bom mas início de checkout < 3% → problema da **página**, não do anúncio: rodar o ciclo
   de revisão da página (etapa 3b) antes de cortar anúncios.
5. 3 dias com ROAS ≥ 2 → **escalar** +20% a cada 48 h e criar **3 variações** do vencedor
   (mesmo gancho, cenas novas).
6. Regras da oferta inteira continuam em `docs/05_metricas-e-decisao.md`.

Os limites acima são hipóteses iniciais; o analista sugere ajustes quando os dados contrariarem.

## Camada 3 — aprendizado acumulado

`aprendizados/o-que-vende.md` é a memória do negócio. Cada linha: data · oferta · nicho · o que
foi testado (gancho, formato, voz, duração, ângulo, bump) · números · conclusão · grau de
confiança. Regras:
- só entra conclusão com número (nada de "acho que");
- o minerador **lê antes de minerar** (prioriza nichos e ângulos que venderam);
- o roteirista **lê antes de escrever** criativos (começa pelos ganchos vencedores).
