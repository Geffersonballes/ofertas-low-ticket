# 01 — Modelo de negócio

## O que vendemos

Produtos digitais de entrada, prontos para baixar, que resolvem **um problema específico e
imediato**. Compra por impulso: a pessoa vê o anúncio, entende em 3 segundos, paga e baixa.

Formatos que funcionam:

- Guia prático / e-book curto (20–60 páginas, muito visual, passo a passo)
- Planilha pronta (orçamento, dieta, treino, controle financeiro, cronograma)
- Pacote de materiais (templates, checklists, atividades imprimíveis, roteiros, prompts)
- Mini-curso em PDF + áudios curtos (sem rosto)

Faixa de preço: **R$ 19,90 a R$ 67**. Preço de referência para começar: **R$ 47**.

## Sem expert

Não existe "rosto" da marca. A autoridade vem de:
clareza da promessa, qualidade visível do material (mockups e páginas de amostra),
garantia de 7 dias e preço baixo que reduz o risco percebido.

## Como o dinheiro entra

```
Anúncio (Meta) → Página de vendas → Checkout (produto R$ 47 + order bumps) → Entrega automática
                                                       ↓
                                              (opcional) Upsell 1 clique
```

- Margem vem do **ticket médio** (produto + bumps), não do produto principal sozinho.
- Meta: ticket médio **≥ R$ 90** com 3–5 bumps bem casados.
- O CPA (custo por compra) tem de ficar abaixo do ticket médio líquido de taxas.

## Ritmo

- Testar **1 a 3 ofertas novas por dia**, cada uma com orçamento baixo (ex.: **R$ 70/dia**).
- A maioria vai morrer. O jogo é achar rápido as poucas que dão lucro e escalar essas.
- Por isso a produção precisa ser barata e rápida: é onde a esteira de IA entra.

## Ferramentas (a definir/confirmar)

| Função | Opções | Decisão |
|---|---|---|
| Checkout e entrega | Hotmart | Hotmart |
| Página de vendas | HTML estático na VPS Hostinger | VPS KVM 2 |
| Anúncios | Meta Ads (Facebook/Instagram) | Meta Ads |
| Vídeos de anúncio | Narração ElevenLabs + cenas geradas + ffmpeg | ElevenLabs |
| Campanhas e métricas | Windsor.ai (conector `facebook`) + painel da Hotmart | Windsor.ai |
