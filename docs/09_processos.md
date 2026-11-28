# 09 — Gestão de processos

Mantido pelo agente `gestor-de-processos`. Aqui ficam as regras vigentes (com onde estão aplicadas e a
trava que as confere), a auditoria, os indicadores do processo e as propostas de melhoria.

## Regras vigentes

| # | Regra | Desde | Origem | Onde está aplicada | Trava |
|---|---|---|---|---|---|
| R1 | Dinheiro só com aprovação humana; campanhas sempre pausadas; o dono ativa | 2026-11-26 | dono | CLAUDE.md 1, `subir-campanhas`, `gestor-de-trafego` | ações do Windsor que gastam pedem confirmação |
| R2 | Modelar, não copiar | 2026-11-26 | dono | CLAUDE.md 2, `revisor-de-conformidade` | veto do revisor |
| R3 | Nada de prova inventada | 2026-11-26 | dono | CLAUDE.md 3 | veto do revisor |
| R4 | Políticas de anúncio | 2026-11-26 | dono | CLAUDE.md 4 | veto do revisor |
| R5 | Produto entregue de verdade; garantia de 7 dias visível (obrigatória por lei e pela Hotmart) | 2026-11-26 | dono | CLAUDE.md 5, docs/08 (reembolso) | painel: alerta de reembolso > 10% |
| R6 | Registrar tudo no `status.md` | 2026-11-26 | dono | CLAUDE.md 6 | auditoria |
| R7 | Pacote do minerador só sai com "PACOTE OK" | 2026-11-27 | dono | CLAUDE.md, `pacote-de-oferta` | `ferramentas/conferir_pacote.py` |
| R8 | **Material primeiro e completo:** revisar o documento inteiro, corrigir tudo (inclusive cosmético), revisar inteiro de novo até sair limpo, dono aprova (Portão M); só então Hotmart, criativos e campanhas | 2026-11-28 | dono | CLAUDE.md 7, esteira, `revisar-material`, `cadastro-e-pixel`, `top5-criativos`, `subir-campanhas`, supervisor | `ferramentas/conferir_material.py` (hash de cada PDF) |
| R9 | **Criativos depois do material:** mesmo ciclo de revisão; dono aprova (Portão C); só então criativo sobe para a Meta e anúncio é criado/atualizado | 2026-11-28 | dono | CLAUDE.md 7, esteira, `revisar-criativos`, `subir-campanhas`, supervisor | `ferramentas/conferir_criativos.py` (exige R8 + hash de cada criativo) |
| R10 | Aprender com cada oferta: erro ou atalho vira linha em `aprendizados/processo.md`, lido antes de cada etapa | 2026-11-28 | dono | CLAUDE.md 8, supervisor, skills | auditoria |
| R12 | **Fechamento da revisão:** da 4ª rodada em diante, revisar só o que mudou (prova por pixel do resto); bloqueia/atrapalha é corrigido; cosmético novo vai para `melhorias-v1.1.md` e não segura o lançamento | 2026-11-28 | dono | CLAUDE.md 7, `revisar-material`, `revisar-criativos` | `cosmeticos_aceitos` no APROVACAO.md |
| R13 | **PR do minerador não interfere na operação:** o Claude informa o dono (escopo, o que muda, gasto) antes de qualquer merge; só o dono autoriza; minerador só adiciona mineração, pesquisas, aprendizados (sem apagar) e pasta de oferta nova; nada de gastar crédito a pedido dele | 2026-11-28 | dono | CLAUDE.md, `pacote-de-oferta` | `ferramentas/conferir_pr_minerador.py` + verificação de hora em hora dos PRs (agendada) |
| R11 | Toda regra nova é registrada aqui e aplicada onde precisa ser cumprida, com trava quando possível | 2026-11-28 | dono | `gestor-de-processos` | auditoria |

## Fluxo atual (resumo)
Garimpar (Marcos, P1) → Produzir (página + produto) → Revisar material (PM) → Criativos → Revisar
criativos (PC) → Conformidade e aprovação (P2, P3) → Hotmart + Meta → Campanhas pausadas → Dono ativa
(P4) → Vender e aprender. Imagens: `docs/img/workflow.png` e `docs/img/workflow-simples.png`.

## Auditoria

| Data | Oferta | Desvio | Correção |
|---|---|---|---|
| 2026-11-28 | Dez Minutinhos | Hotmart, criativos e campanhas feitos antes da revisão do material (regra ainda não existia) | Campanhas seguem pausadas; material em correção; depois PM, revisão dos criativos, PC e troca dos PDFs/criativos |
| 2026-11-28 | Dez Minutinhos | Página de vendas e vídeo "folheando" com páginas do caderno-amostra | Regenerar a partir do PDF final (em andamento) |

## Indicadores do processo

| Oferta | P1 → P4 | Rodadas de revisão (material / criativos) | Erros (bloqueia / atrapalha / cosmético) | Toques manuais do dono | Custo de produção |
|---|---|---|---|---|---|
| Dez Minutinhos | 2026-11-26 → (pendente) | 1 / 0 (em andamento) | 0 / 22 / ~45 | alto (Hotmart, Página, pixel, conta de anúncios, Windsor: ~15 rodadas de prompts e prints) | ElevenLabs ~6,8 mil créditos no tutorial + vozes dos anúncios; R$ 0 em anúncio |

Metas para a próxima oferta: P1 → P4 em até 2 dias; ≤ 2 rodadas de revisão do material; toques manuais
do dono ≤ 5 (Página, pixel, Windsor, troca de arquivo, ativar).

## Propostas

| # | Problema (com número) | Proposta | Ganho | Esforço | Status |
|---|---|---|---|---|---|
| P1 | Cada oferta exigiu ~15 idas e vindas do dono com a Meta (Página, pixel, conta, Windsor) | Checklist único de 4 passos por oferta (já em docs/06) + o Claude gera os prompts da extensão de uma vez | −1 a 2 h do dono por oferta | baixo | feita 2026-11-28 (skill `preparar-meta-oferta`) |
| P2 | Bumps não apareciam no checkout e só descobrimos tarde | Script de teste do checkout (Playwright, país Brasil) que confere preço, bumps e meios de pagamento antes do Portão 4 | evita vender sem bump (receita extra) | baixo | feita 2026-11-28 (`ferramentas/testar_checkout.cjs`, ligado em `subir-campanhas`) |
| P3 | Trocar PDF na Hotmart é manual | Skill `trocar-arquivo-hotmart`: gera PDF + link temporário + uma frase para a extensão | −15 min por troca | baixo | feita 2026-11-28 (skill `trocar-arquivo-hotmart`) |
| P4 | 22 erros "atrapalha" achados só na revisão final | Testes automáticos no gerador (labirinto tem caminho único, sudoku solução única, sequência resposta única, ligue-os-pontos fecha, gabarito pintado) rodando a cada geração | revisão do material em 1 rodada | médio | aprovada 2026-11-28 (asserts de rima/sequência já entraram no gerador; falta a suíte completa) |
| P5 | Página e anúncios usaram imagens da amostra | Mídia da página e dos criativos sempre gerada do PDF final por um único script, chamado depois do Portão M | zero divergência promessa × produto | baixo | aprovada 2026-11-28 (`pagina/midia/gerar_midia.py` já rasteriza o PDF final; falta ligar à esteira depois do Portão M) |
| P6 | Indicadores do processo são preenchidos à mão | Revisão semanal agendada do `gestor-de-processos` (lê status.md e git, atualiza esta página) | visão contínua sem esforço | baixo | feita 2026-11-28 (agendamento semanal, segundas 07:12 Cuiabá) |
