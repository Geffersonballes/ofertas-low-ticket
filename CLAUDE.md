# Instruções para o Claude

Este repositório é a operação de ofertas low ticket descrita no `README.md`.
A metodologia de referência é `docs/00_prompt-mestre.md` (aula LowTicket com IA).
Leia `docs/02_esteira.md` antes de produzir qualquer oferta e siga a ordem das 7 etapas.

## Quem faz o quê

Duas pessoas trabalham neste repositório (ver `docs/07_divisao-do-trabalho.md`):
- **Minerador:** etapas 1–2. Entrega um *pacote de oferta* por pull request (skill `pacote-de-oferta`). Não faz merge, não publica, não cadastra nada.
- **Operador (dono):** aceita o pacote (merge = Portão 1) e toca as etapas 3–7 e a leitura de métricas.

Pergunte quem está usando a sessão se não estiver claro antes de executar etapas além da 2.

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
