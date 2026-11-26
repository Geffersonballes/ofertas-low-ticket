# 02 — Esteira de produção de uma oferta

Responsável pela orquestração: agente `supervisor-de-ofertas`.
Cada oferta vive em `ofertas/AAAA-MM-DD_<slug>/` (cópia de `ofertas/_modelo/`), e cada etapa
é marcada no `status.md` da pasta.

| # | Etapa | Agente | Saída |
|---|---|---|---|
| 1 | Mineração | `minerador-de-ofertas` | `mineracao/AAAA-MM-DD.md` com candidatas pontuadas |
| 2 | Análise e escolha | `analista-de-oferta` | `briefing.md` (promessa, público, ângulo, preço) |
| — | **Portão 1 (humano)** | dono | aprova qual candidata vira oferta |
| 3 | Produto | `criador-de-produto` | `produto/` — sumário, conteúdo completo, mockup |
| 4 | Order bumps e upsell | `criador-de-order-bumps` | `bumps/bumps.md` + conteúdo de cada bump |
| 5 | Copy da página | `copywriter-de-pagina` | `pagina/copy.md` |
| 6 | Construção da página | `construtor-de-pagina` | `pagina/index.html` responsiva, pronta para publicar |
| 7 | Criativos | `roteirista-de-criativos` | `criativos/` — 3 a 5 roteiros + textos dos anúncios |
| 8 | Conformidade | `revisor-de-conformidade` | parecer no `status.md` (**Portão 2**, tem veto) |
| — | **Portão 3 (humano)** | dono | aprova página, produto e criativos |
| 9 | Checkout, pixel e campanha | `gestor-de-trafego` | `campanha.md` + campanha **em rascunho** |
| — | **Portão 4 (humano)** | dono | publica a campanha e liga o orçamento |
| 10 | Leitura de resultado | `analista-de-metricas` | decisão em `resultados/painel.md` |

Regras:

- Nenhum portão é pulado. Se um portão reprova, a oferta volta para a etapa indicada.
- Máximo de 2 voltas por etapa; depois disso, a oferta é descartada e o motivo registrado.
- As etapas 3, 4 e 5 podem rodar em paralelo depois do Portão 1.
- Arquivos pesados (vídeos, zips) ficam fora do git — registre o link no `status.md`.
