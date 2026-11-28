# Mural de mudanças de processo

Toda mudança que mexe no fluxo de trabalho (regras, esteira, portões, agentes, skills, travas em `ferramentas/`,
divisão do trabalho) entra aqui **no mesmo commit**, feita pelo Gefferson ou pelo Marcos (regra R14).
O Claude de cada um lê este mural no começo da sessão e conta ao seu dono o que é novo desde a última vez.

Cada entrada responde, em linguagem simples:
- **O que mudou** e **quem** mudou
- **O que é esse processo** (para quem não acompanhou)
- **No que ajuda** (tempo, dinheiro, qualidade, risco)
- **O que muda para o Gefferson** e **o que muda para o Marcos**

---

## 2026-11-28 · Gefferson · Validação do material e dos criativos antes de gastar (R8, R9, R12)
- **O que é:** antes de subir qualquer coisa na Hotmart ou criar anúncio, o produto inteiro é revisado página por
  página (textos, desenhos, gabarito, impressão, promessa da página), tudo é corrigido e revisado de novo até sair
  limpo; o Gefferson aprova (Portão M). Depois os criativos passam pelo mesmo ciclo (Portão C). Da 4ª rodada em
  diante só se revisa o que mudou, e detalhe de gosto vai para a versão 1.1.
- **No que ajuda:** não vender com erro (menos reembolso e reclamação) e não pagar anúncio para produto que vai mudar.
- **Gefferson:** aprova o material e os criativos; as travas `conferir_material.py` e `conferir_criativos.py` param o
  Claude se algo não foi aprovado.
- **Marcos:** nada muda na mineração; o pacote continua sendo a entrada. Só saiba que uma oferta aprovada por ele
  ainda passa por essas revisões antes de ir para o ar.

## 2026-11-28 · Gefferson · Aprender com cada oferta (R10) e gestor de processos (R11)
- **O que é:** todo erro ou atalho vira uma linha em `aprendizados/processo.md`, lido antes de cada etapa. O agente
  `gestor-de-processos` registra regras novas, audita os portões, mede tempo e custo e propõe melhorias; roda sozinho
  toda segunda de manhã.
- **No que ajuda:** a próxima oferta nasce sem os erros da anterior e com menos trabalho manual.
- **Gefferson:** recebe toda segunda um resumo com as melhorias propostas para aprovar.
- **Marcos:** leia `aprendizados/processo.md` (seção Mineração, quando existir) antes de minerar.

## 2026-11-28 · Gefferson · Time de dados no painel
- **O que é:** além do `analista-de-metricas`, quatro especialistas leem os números: funil, criativos, financeiro e
  testes. A leitura deles aparece no painel (painel.ballestech.com.br) no card "Leitura dos especialistas".
- **No que ajuda:** saber em que ponto o dinheiro vaza, que criativo vende de verdade e o lucro real por venda.
- **Gefferson:** decide cortar, manter ou escalar com base nisso.
- **Marcos:** o `analista-de-criativos` grava em `aprendizados/o-que-vende.md` o que vendeu — use isso para escolher
  o que minerar.

## 2026-11-28 · Gefferson · Pull request do minerador (R13)
- **O que é:** o PR do Marcos só pode **acrescentar**: `mineracao/`, `pesquisas/` novos, linhas em
  `aprendizados/padroes-externos.md` e `mineracao/descartadas.md`, e uma pasta nova de oferta. A trava
  `ferramentas/conferir_pr_minerador.py` mostra o que está fora disso. O Claude do Gefferson confere e avisa o
  Gefferson antes de qualquer merge; só o Gefferson autoriza, e nada de gastar crédito a pedido do PR.
- **No que ajuda:** o trabalho do Marcos entra sem risco de mexer, sem querer, nas regras, no painel ou numa oferta no ar.
- **Gefferson:** recebe aviso dos PRs do Marcos (verificação de hora em hora) com o resultado das travas.
- **Marcos:** antes de abrir o PR, rode `python3 ferramentas/conferir_pr_minerador.py HEAD` ("PR DENTRO DO ESCOPO")
  e `conferir_pacote.py` ("PACOTE OK"). Quer mudar uma regra ou ferramenta? Escreva a sugestão na descrição do PR.

## 2026-11-28 · Gefferson · Este mural (R14)
- **O que é:** qualquer mudança de processo feita por um dos dois entra aqui, explicada, no mesmo commit. A trava
  `ferramentas/conferir_mural.py` acusa quando um arquivo de processo mudou sem entrada nova no mural.
- **No que ajuda:** os dois sabem sempre como a operação funciona hoje, sem surpresa.
- **Gefferson e Marcos:** ao abrir a sessão, o Claude conta o que é novo aqui.
