# Ofertas Low Ticket

Operação de infoprodutos de entrada barata (R$ 19,90 a R$ 67), vendidos com tráfego direto
(Meta Ads) e produzidos por uma esteira de agentes de IA. Sem expert, sem audiência própria,
sem aparecer em vídeo.

## Os quatro pilares

| Pilar | O que é | Documento |
|---|---|---|
| 1. Produto low ticket | Guias, e-books, planilhas e pacotes de materiais práticos, comprados por impulso | [docs/01_modelo-de-negocio.md](docs/01_modelo-de-negocio.md) |
| 2. Modelagem de ofertas validadas na gringa | Ofertas em inglês com vários anúncios ativos há mais de 2 semanas, adaptadas para o português | [docs/03_mineracao.md](docs/03_mineracao.md) |
| 3. Lucro no volume e nos order bumps | 1 a 3 ofertas testadas por dia com orçamento baixo; bumps levam o ticket de R$ 47 para R$ 90+ | [docs/04_order-bumps.md](docs/04_order-bumps.md), [docs/05_metricas-e-decisao.md](docs/05_metricas-e-decisao.md) |
| 4. Esteira automatizada com IA | Página, produto, bônus, vídeos de anúncio, pixel e campanha em rascunho feitos por agentes | [docs/02_esteira.md](docs/02_esteira.md) |

## Divisão do trabalho

Minerador (etapas 1–2, entrega pacote por pull request) e operador (etapas 3–7). Ver
[docs/07_divisao-do-trabalho.md](docs/07_divisao-do-trabalho.md).

## Como usar

1. **Minerar:** peça ao Claude "minere ofertas" → o agente `minerador-de-ofertas` preenche
   `mineracao/AAAA-MM-DD.md` com candidatas pontuadas.
2. **Escolher:** você marca quais candidatas viram oferta (ou deixa o `analista-de-oferta` sugerir).
3. **Produzir:** peça "produza a oferta X" → o `supervisor-de-ofertas` copia `ofertas/_modelo/`
   para `ofertas/AAAA-MM-DD_<slug>/` e roda a esteira, registrando tudo no `status.md`.
4. **Aprovar e subir:** você aprova a página, o produto e os criativos. A campanha só é criada
   **em rascunho**; quem publica e liga o orçamento é você.
5. **Medir:** o `analista-de-metricas` lê os números e aplica as regras de corte/escala.

## Estrutura

```
.claude/agents/     agentes da esteira (um por etapa)
docs/               prompt mestre (00), modelo, esteira, critérios, métricas e stack
mineracao/          radares de mineração (um arquivo por dia)
.claude/skills/     uma skill por etapa (os templates da aula)
ofertas/_modelo/    modelo de pasta de uma oferta — copie para cada nova oferta
ofertas/<data_slug> uma pasta por oferta em produção ou no ar
resultados/         painel por oferta e por anúncio (funil)
aprendizados/       o que vende (dados nossos + padrões da concorrência)
pesquisas/          relatórios do pesquisador-de-anuncios
```
