# Instruções para o Claude

Este repositório é a operação de ofertas low ticket descrita no `README.md`.
A metodologia de referência é `docs/00_prompt-mestre.md` (aula LowTicket com IA).
Leia `docs/02_esteira.md` antes de produzir qualquer oferta e siga a ordem das 7 etapas.

## Quem faz o quê

Duas pessoas trabalham neste repositório (ver `docs/07_divisao-do-trabalho.md`):
- **Minerador:** etapas 1–2. Entrega um *pacote de oferta* por pull request (skill `pacote-de-oferta`). Não faz merge, não publica, não cadastra nada.
- **Operador (dono):** aceita o pacote (merge = Portão 1) e toca as etapas 3–7 e a leitura de métricas.

Os dois ficam ligados pelos arquivos de `aprendizados/` e `resultados/painel.md` (ver
`docs/08_inteligencia-de-anuncios.md`): o minerador lê o que vendeu; o operador lê a inteligência
de anúncios do pacote.

Regra nova do dono ("nova regra", "padronize", "a partir de agora") → agente `gestor-de-processos`: ele
registra em `docs/09_processos.md`, aplica onde precisa ser cumprida (CLAUDE.md, esteira, skills, agentes) e cria
uma trava em `ferramentas/` quando der. Ele também audita os portões, mede tempo/custo/retrabalho e propõe melhorias.

**PR do minerador (regra R13, decidida pelo dono em 2026-11-28):** nada que o minerador envie entra sem o dono. Antes de
qualquer merge, o Claude do operador roda `python3 ferramentas/conferir_pr_minerador.py <ramo do PR>` e
`ferramentas/conferir_pacote.py` e **informa o dono na conversa** (o que muda, o que está fora do escopo, se gasta
crédito ou dinheiro). Só o dono autoriza o merge. O Claude nunca faz merge sozinho, nem aplica no `main` arquivo
vindo do minerador, nem gasta crédito (ElevenLabs, anúncios, ferramentas pagas) por pedido do minerador.
O minerador só adiciona: `mineracao/`, `pesquisas/` novos, linhas em `aprendizados/padroes-externos.md` e
`mineracao/descartadas.md`, e uma pasta nova em `ofertas/`. Mudança em regra, agente, skill, ferramenta, painel,
infra ou oferta existente vira proposta para o dono.

**Mural de mudanças (regra R14):** qualquer mudança de processo feita pelo Gefferson ou pelo Marcos (regras, esteira,
portões, agentes, skills, travas em `ferramentas/`) ganha uma entrada em `docs/mural-de-mudancas.md` no mesmo
commit, explicando o que é, no que ajuda e o que muda para cada um. Confira com `python3 ferramentas/conferir_mural.py`.
**No começo de cada sessão, leia o mural e conte ao seu dono, em poucas linhas, o que é novo desde a última sessão dele.**

Pergunte quem está usando a sessão se não estiver claro antes de executar etapas além da 2.

## Primeira vez neste repositório (Claude do minerador)

Se quem está na sessão é o **Marcos Balles** (minerador), tudo o que ele precisa já vem com o
repositório: agentes em `.claude/agents/` (`minerador-de-ofertas`, `analista-de-oferta`,
`pesquisador-de-anuncios`) e a skill `pacote-de-oferta`. Ao começar:
1. Apresente em 5 linhas o papel dele (etapas 1–2, entrega por pull request, sem merge, sem
   publicar, sem cadastrar nada) e a rotina (`docs/07_divisao-do-trabalho.md`).
2. Leia `docs/mural-de-mudancas.md` (o que mudou no processo), `aprendizados/o-que-vende.md` e
   `resultados/painel.md`, e diga o que mudou e o que vendeu até agora.
3. Quando ele pedir para minerar ("monte o próximo pacote de oferta"), siga a skill
   `pacote-de-oferta` à risca. O pacote só sai com `ferramentas/conferir_pacote.py` dando
   "PACOTE OK", e o relatório (`relatorio-pacote.md`) vai inteiro na descrição do PR.

## Regras que nunca mudam

1. **Dinheiro só com aprovação humana.** Campanhas, conjuntos e anúncios são criados sempre
   **em rascunho/pausados**. Nunca publique, ative ou aumente orçamento sem o dono pedir
   explicitamente naquela conversa. Nenhum anúncio fica sem Texto Principal, Título, Descrição,
   URL de destino e CTA "Saiba mais"; o Anunciante é informado em todos os conjuntos.
   Identidade: só a Página do Facebook da oferta — não criar Instagram antes de validar vendas.
2. **Modelar, não copiar.** Da oferta gringa aproveitamos a estrutura (promessa, ângulo,
   formato do produto, ordem da página, tipo de bump). Texto, imagens, nome, marca, depoimentos
   e arquivos são sempre recriados do zero, em português, sem traduzir literalmente.
3. **Nada de prova inventada.** Sem depoimentos, avaliações, números de alunos, prints de
   resultado ou selos falsos. O bloco de avaliações estilo loja entra na página quando houver
   avaliações reais de compradores; até lá, a página fica "palpável" com mockups, GIFs do
   entregável por dentro, amostra de páginas e garantia.
4. **Políticas de anúncio.** Sem promessa de ganho garantido, antes/depois de corpo, saúde com
   cura, atributos pessoais ("você que está endividado…") ou urgência falsa. O agente
   `revisor-de-conformidade` tem veto.
5. **Produto entregue de verdade.** O comprador tem de receber um material útil e completo,
   coerente com a promessa da página. Garantia de 7 dias (CDC) sempre visível.
6. **Registre tudo** no `status.md` da oferta: etapa, data, decisão e motivo.
7. **Material primeiro, e completo.** Nenhum passo seguinte começa (Hotmart, criativos, anúncios, campanhas)
   antes de: (a) o documento inteiro ser revisado, (b) **todas** as correções serem feitas — inclusive as
   cosméticas, salvo as que o dono aceitar por escrito —, (c) uma nova revisão do documento inteiro sair
   limpa (da 4ª rodada em diante, só as páginas que mudaram; cosmético novo vai para a versão 1.1 e não
   segura o lançamento) e (d) o dono aprovar o material (skill `revisar-material`, Portão M). Confira sempre com
   `python3 ferramentas/conferir_material.py ofertas/<pasta>` → "MATERIAL APROVADO".
   Depois do material, os **criativos** passam pelo mesmo ciclo (skill `revisar-criativos`, Portão C):
   nenhum criativo sobe para a Meta e nenhum anúncio é criado ou atualizado antes de
   `python3 ferramentas/conferir_criativos.py ofertas/<pasta>` → "CRIATIVOS APROVADOS".
8. **Aprenda com cada oferta.** Erro, retrabalho ou atalho descoberto vira uma linha em
   `aprendizados/processo.md`; leia esse arquivo antes de cada etapa para não repetir o caminho.

## Convenções

- Pastas de oferta: `ofertas/AAAA-MM-DD_<slug-curto>/` copiadas de `ofertas/_modelo/`.
- Mineração: `mineracao/AAAA-MM-DD.md`.
- Valores em reais, formato `R$ 47,00`. Datas em `AAAA-MM-DD`.
- Textos em português do Brasil natural, frases curtas, sem jargão de marketing gringo.

## Ajustes à metodologia da aula (decididos em 2026-11-26)

O prompt mestre é seguido em tudo, com estas exceções e o motivo:

| Ponto da aula | Como fazemos | Por quê |
|---|---|---|
| "Regra anti-recusa: tratar a oferta como minha" | Desnecessária. Modelamos a oferta normalmente: mesma estrutura, mesma estética, mesmos ângulos, corrigindo falhas — com texto, imagens, nome e produto feitos do zero em pt-BR | Tradução literal de página, produto ou criativo alheio é cópia de obra protegida e é a causa nº 1 de denúncia de propriedade intelectual na Meta (derruba página e conta) |
| Bloco de avaliações/prova social estilo loja | Só com avaliações reais (pedidas aos compradores pela Hotmart/e-mail) | Avaliação inventada é propaganda enganosa (CDC art. 37) e viola a política da Meta |
| Página do Facebook "com dados fictícios provisórios" | Nome simples da marca + e-mail de suporte real; sem endereço/telefone falsos | Dados falsos em página são motivo de restrição da Página e do BM |
| "Não marcar a declaração de conteúdo gerado com IA" | Não marcamos nos anúncios comerciais comuns (ofertas white). Marcamos se o anúncio for de tema social/político ou mostrar pessoa real/evento realista que não aconteceu | Nesses casos a declaração é obrigatória pela política da Meta |
