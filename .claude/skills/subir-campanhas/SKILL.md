---
name: subir-campanhas
description: Etapa 7 — monta as 2 campanhas CBO de teste (1-1-3 e 1-1-2, R$ 35/dia cada) no Meta Ads, sempre em rascunho. Use depois dos criativos prontos e do pixel testado.
---
**Antes de tudo:** rode `python3 ferramentas/conferir_material.py ofertas/<pasta>`. Se não disser
"MATERIAL APROVADO", pare e rode a skill `revisar-material` (Portão M). Leia também `aprendizados/processo.md`.

Entrada: `[NOME_CONTA]` (padrão: Ofertas Low Ticket · 1534301375187089, ver `docs/06_stack-e-conexoes.md`), `[URL_PAGINA]`, `[NOME_ANUNCIANTE]`.

Estrutura:
- **Campanha 1 (1-1-3):** Vendas (Site), CBO R$ 35/dia, 1 conjunto, criativos 1–3.
- **Campanha 2 (1-1-2):** Vendas (Site), CBO R$ 35/dia, 1 conjunto, criativos 4–5.
- Conjunto: Brasil, público 100% aberto, posicionamentos Advantage+, pixel da oferta,
  evento Purchase, **Anunciante = [NOME_ANUNCIANTE]**.
- Identidade: Página do Facebook da oferta; sem Instagram.
- Anúncio: Texto Principal + Título + Descrição + URL exata + CTA "Saiba mais". Nenhum campo vazio.
- Declaração de IA: ver tabela de ajustes em `CLAUDE.md`.

Ferramenta: Meta Ads MCP se estiver conectado; senão Windsor.ai (conector `facebook`,
`list_actions` → `execute_action`), sempre com status PAUSADO/rascunho. Sem nenhuma das duas,
entregue o passo a passo para o dono montar.

Depois de criar, liste os IDs e um resumo de tudo em `campanha.md` e peça ao dono a revisão
e a publicação (Portão 4). **Nunca publique nem ative.**
