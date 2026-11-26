# 02 — Esteira de produção de uma oferta (7 etapas da aula)

Referência: `docs/00_prompt-mestre.md`. Orquestração: agente `supervisor-de-ofertas`.
Cada oferta vive em `ofertas/AAAA-MM-DD_<slug>/` (cópia de `ofertas/_modelo/`), e cada etapa
é marcada no `status.md`. Ferramentas e conexões de cada etapa: `docs/06_stack-e-conexoes.md`.

| Etapa | O que acontece | Agente(s) | Skill de uso diário | Saída |
|---|---|---|---|---|
| 1. Mineração | Ofertas em inglês, white, low ticket, 48–112+ anúncios, 14+ dias | `minerador-de-ofertas` | `minerar-ofertas` | `mineracao/AAAA-MM-DD.md` |
| — | **Portão 1 (dono):** escolhe a candidata | | | |
| 2. Dossiê | Engenharia reversa: promessa, mecanismo, público, estrutura da página, criativos, objeções | `analista-de-oferta` | `dossie-oferta` | `dossie.md` + `briefing.md` |
| 3. Página | Página 100% em pt-BR, mesma estrutura e estética, mockups e GIFs do entregável, publicação na Hostinger | `copywriter-de-pagina`, `construtor-de-pagina` | `pagina-de-vendas` | `pagina/index.html` publicada |
| 4. Entregável | Produto completo + bônus práticos em .zip; até 12 order bumps + oferta pós-compra | `criador-de-produto`, `criador-de-order-bumps` | `entregavel-e-bonus` | `produto/`, `bumps/`, .zip |
| — | **Portão 2:** `revisor-de-conformidade` (veto) · **Portão 3 (dono):** aprova página e produto | | | |
| 5. Cadastro e pixel | Produto + .zip na Hotmart, Página do Facebook, Pixel novo, PageView na página, ID + token da API de Conversões na Hotmart | `gestor-de-trafego` | `cadastro-e-pixel` | `campanha.md` (parte 1) |
| 6. Criativos | Top 5 anúncios mais antigos da referência recriados em pt-BR (cenas, narração, trilha) | `roteirista-de-criativos` | `top5-criativos` | `criativos/` |
| 7. Campanhas | 2 campanhas CBO (1-1-3 e 1-1-2), R$ 35/dia cada, Vendas (Site), público aberto, **rascunho** | `gestor-de-trafego` | `subir-campanhas` | `campanha.md` (parte 2) |
| — | **Portão 4 (dono):** revisa os rascunhos, publica e liga o orçamento | | | |
| Fase 2. Otimização | Leitura diária, diagnóstico de página/checkout, corte e escala | `analista-de-metricas` | — | `resultados/painel.md` |

Regras:

- Nenhum portão é pulado. Reprovação volta para a etapa indicada; no máximo 2 voltas por
  etapa, depois a oferta é descartada com o motivo registrado.
- Depois do Portão 1, as etapas 3, 4 e 6 (roteiros) podem rodar em paralelo.
- Meta operacional: 1 a 3 ofertas novas por dia.
- Arquivos pesados (vídeos, .zip, GIFs) ficam fora do git: registre o link no `status.md`.
