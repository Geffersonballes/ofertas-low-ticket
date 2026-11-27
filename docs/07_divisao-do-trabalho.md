# 07 — Divisão do trabalho

Duas pessoas, cada uma com a própria conta do Claude, no mesmo repositório do GitHub.

| | **Minerador** (irmão) | **Operador** (Gefferson) |
|---|---|---|
| Etapas | 1. Mineração · 2. Dossiê e briefing | 3 a 7: página, produto, bumps, Hotmart, pixel, anúncios, campanhas · leitura de métricas |
| Entrega | **Pacote de oferta** num pull request | Oferta no ar, campanhas em rascunho, decisão de escala |
| Skill principal | `pacote-de-oferta` | `pagina-de-vendas`, `entregavel-e-bonus`, `cadastro-e-pixel`, `top5-criativos`, `subir-campanhas` |
| Ramos no git | `mineracao/AAAA-MM-DD_<slug>` | `main` (e o ramo de trabalho da sessão) |
| Decide | quais candidatas viram pacote | **Portão 1:** aceitar ou devolver o pacote · Portões 3 e 4 |

## Como os dois ficam ligados

Ver `docs/08_inteligencia-de-anuncios.md`. Em resumo:
- **Marcos → Gefferson:** o pacote traz a seção "Inteligência de anúncios" (o que comprovadamente
  vende no nicho). O operador usa isso para escrever os roteiros e montar os anúncios.
- **Gefferson → Marcos:** o `analista-de-metricas` grava diariamente em `resultados/painel.md` e
  `aprendizados/o-que-vende.md` o que vendeu e o que não vendeu. O minerador lê antes de minerar.
- **Avisos rápidos:** grupo de WhatsApp "Ofertas Low Ticket · Balles" (pacote novo, anúncio vencedor,
  oferta cortada). Decisões e números ficam sempre no repositório.
- O minerador não acessa conta de anúncios nem Hotmart; vê os números pelo painel.

## Como o pacote chega

1. O minerador abre um **pull request** chamado `Pacote de oferta: <nome> (<data>)`.
2. O operador lê a descrição do PR (resumo de 1 tela) e decide:
   - **Aceito** → faz merge do PR. Isso é o Portão 1. A pasta `ofertas/AAAA-MM-DD_<slug>/` passa a
     existir no `main` e a esteira segue a partir da etapa 3.
   - **Devolvido** → comenta no PR o motivo (ex.: mercado BR saturado, risco de política). O minerador
     registra em `mineracao/descartadas.md` e segue para a próxima.
3. Meta de ritmo: **3 a 5 candidatas pontuadas por dia** e **1 pacote completo a cada 1–2 dias**.

## O que é um "pacote de oferta" pronto

Tudo resumido no **relatório do pacote** (`relatorio-pacote.md`, modelo em `ofertas/_modelo/`),
que vai inteiro na descrição do PR. A conferência `python3 ferramentas/conferir_pacote.py
ofertas/<pasta>` precisa dar "PACOTE OK" antes de abrir o PR.


Tudo dentro de `ofertas/AAAA-MM-DD_<slug>/` (copiado de `ofertas/_modelo/`):

- [ ] `status.md` com a origem (arquivo de mineração e nº da candidata) e etapas 1–2 ✅
- [ ] **Conferência manual na Biblioteca de Anúncios** (a Biblioteca bloqueia robôs): nº de anúncios
      ativos, data de início do anúncio mais antigo **ainda ativo**, e 3 a 5 prints em
      `ofertas/<pasta>/referencia/` (nomes `biblioteca-1.png`…). Sem isso o pacote não é aceito.
- [ ] `dossie.md` completo: promessa, mecanismo, público, página seção por seção, entregáveis, bumps
      vistos, **Top 5 anúncios mais antigos com link**, objeções, falhas a corrigir
- [ ] `briefing.md` completo: nome em pt-BR (3 opções), promessa sem saúde/dinheiro garantido, formato
      e entregáveis que a IA consegue produzir com qualidade, preço e âncora honesta, 2–4 bônus,
      5–8 bumps com preço e ticket médio estimado, 5 ângulos de anúncio, slug, riscos
- [ ] **Google Trends Brasil (12 meses)**: 3 termos em pt-BR, tendência, sazonalidade, link e print
      (`referencia/trends-1.png`). Interesse relativo, não volume.
- [ ] Encaixe Brasil verificado: buscas em português (Hotmart, Kiwify, Mercado Livre, Google) com links
- [ ] Seção "Inteligência de anúncios" no `dossie.md` (5 padrões a usar, 3 a evitar, com evidência)
- [ ] Nota ≥ 22/30 e nenhum critério de corte reprovado (`docs/03_mineracao.md`)

## O que o minerador NÃO faz

Não produz página, produto, criativos nem campanha; não cadastra nada na Hotmart nem na Meta; não
publica em `publicado/`; não faz merge no `main`. Não copia texto nem imagem da oferta gringa para
dentro do pacote além do necessário para análise (prints da Biblioteca ficam só em `referencia/`).
