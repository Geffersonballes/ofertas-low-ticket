---
name: revisar-criativos
description: Etapa 6b — revisa cada criativo de anúncio (vídeos e imagens) e o texto de cada anúncio antes de subir para a Meta. Só roda depois do Portão M (material aprovado). Termina no Portão C (dono aprova os criativos). Use depois de produzir os criativos e sempre que um vídeo, imagem ou texto de anúncio mudar.
---
Regra fixa (decidida pelo dono em 2026-11-28): a validação dos criativos acontece **depois** da
validação do documento principal. Nenhum criativo sobe para a Meta e nenhum anúncio é criado ou
atualizado antes de `python3 ferramentas/conferir_criativos.py ofertas/<pasta>` dizer
"CRIATIVOS APROVADOS" (que já exige "MATERIAL APROVADO").

## 0. Pré-requisito
`python3 ferramentas/conferir_material.py ofertas/<pasta>` → "MATERIAL APROVADO". Se não, pare.
Se o material mudou desde que os criativos foram feitos, **refaça os criativos** com as páginas novas
(`criativos/montador/`) antes de revisar.

## 1. Revisão (em paralelo, em segundo plano)
1. **Técnica, um vídeo por vez** (agente `controle-de-qualidade` ou `general-purpose`): extrair quadros
   (início, meio de cada frase, fecho) e **olhar**; conferir áudio (volume, cortes), legenda igual à fala e
   sincronizada, texto cortado, tela preta, duração 15–30 s, 9:16, área segura (título abaixo de 200 px
   do topo, legenda acima de 250 px da base). Imagens: tamanho, legibilidade no celular, pouco texto.
2. **Verdade do produto:** toda página, número e preço que aparece no criativo **existe no PDF aprovado**
   (comparar com `produto/final/` e bumps). Nada da amostra antiga, nada que o produto não entregue.
3. **Conformidade** (`revisor-de-conformidade`, tem veto): políticas da Meta (sem atributo pessoal,
   promessa de resultado, urgência falsa, antes/depois), CDC, sem prova inventada, cópia da referência.
4. **Texto do anúncio** (`criativos/roteiros.md`): Texto Principal, Título, Descrição, CTA "Saiba mais"
   e URL presentes; português; o que diz bate com a página e o produto.

Saída: `ofertas/<pasta>/revisoes/criativos-AAAA-MM-DD/<bloco>.md` com tabela
Criativo | Momento/trecho | Gravidade (bloqueia / atrapalha / cosmético) | Problema | Sugestão.

## 2. Correção
Corrija **tudo** (inclusive cosmético; só fica de fora o que o dono aceitar por escrito) no montador
(`criativos/montador/`) ou no texto, gere de novo, e **revise de novo todos os criativos que mudaram**.
Repita até a rodada sair limpa. Fechamento igual ao do material (`revisar-material`, seção 2): da 4ª rodada em
diante só o que mudou; cosmético novo vai para `revisoes/melhorias-v1.1.md` e não segura o lançamento. Registre em `correcoes.md`.

## 3. Portão C (dono)
Mostre ao dono cada criativo (vídeo/imagem + texto do anúncio) e o resumo das correções. **Só com o
"aprovado" do dono na conversa**, gere `revisoes/criativos-AAAA-MM-DD/APROVACAO.md`:

```
aprovado_por: Gefferson
data: AAAA-MM-DD
pendencias: 0
revisao_final_limpa: AAAA-MM-DD (rodada N, todos os criativos)
material_aprovado_em: revisoes/material-AAAA-MM-DD/APROVACAO.md
cosmeticos_aceitos: nenhum
<sha256>  criativos/videos/<arquivo>.mp4
<sha256>  criativos/estatico/<arquivo>.jpg
```
(`cd ofertas/<pasta> && sha256sum criativos/videos/*.mp4 criativos/estatico/*.jpg >> revisoes/.../APROVACAO.md`)

Depois: `subir-campanhas` (subir os criativos aprovados e criar/atualizar os anúncios, sempre pausados).

## 4. Aprender
Cada erro vira uma linha em `aprendizados/processo.md` (seção "Criativos"), com a causa e a regra para o
montador/roteirista não repetir.
