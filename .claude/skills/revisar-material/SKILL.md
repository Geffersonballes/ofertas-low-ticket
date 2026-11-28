---
name: revisar-material
description: Etapa 4b — revisa página por página o infoproduto (PDF principal, bônus e order bumps) antes de qualquer coisa ir para a Hotmart, criativos ou campanhas. Textos, desenhos, atividades, gabarito, impressão e promessa da página. Termina no Portão M (dono aprova o conteúdo). Use depois de produzir o entregável e sempre que um PDF mudar.
---
Regra fixa (decidida pelo dono em 2026-11-28): **nenhum arquivo sobe para a Hotmart e nenhum criativo
ou campanha é criado antes de `python3 ferramentas/conferir_material.py ofertas/<pasta>` dizer
"MATERIAL APROVADO".** Mudou um PDF depois da aprovação → esta skill roda de novo (pelo menos nos
arquivos que mudaram).

## 1. Revisão (4 revisores em paralelo, `general-purpose`, em segundo plano)
Divida o material em blocos de até ~150 páginas. Para um caderno com bumps, o padrão é:
1. PDF principal, 1ª metade (abertura, como usar, sumário, plano e atividades do 1º nível)
2. PDF principal, 2ª metade (2º nível, gabarito completo, bônus)
3. Bumps pequenos (todos menos o maior)
4. Bump maior + conferência das **promessas** da página (`pagina/index.html`, `pagina/copy.md`) e dos
   anúncios (`criativos/roteiros.md`, se já existirem) contra o PDF

Cada revisor **renderiza as páginas em imagem** (`pdftoppm -r 60..70 -png`) e **olha** com Read — não
basta `pdftotext`. Procura, com página exata:
- atividade que não dá para fazer (labirinto sem saída/atalho, 7 erros que não são 7, sequência
  ambígua, conta errada, sudoku sem solução única, peça de jogo faltando, linha de corte ausente);
- gabarito errado, faltando ou que não cobre todas as atividades;
- plano/sumário apontando para página errada;
- impressão: corte, margem, sobreposição, cinza que some em P&B;
- português (ortografia, concordância, instrução confusa), nível de idade incompatível;
- contagem real × prometida (atividades, bônus, cartas, jogos);
- conteúdo impróprio para o público.

Saída: `ofertas/<pasta>/revisoes/material-AAAA-MM-DD/<bloco>.md` com tabela
Página | Gravidade (**bloqueia** / **atrapalha** / cosmético) | Problema | Sugestão.

## 2. Correção
- Corrija no **gerador** (`produto/gerador/`), nunca editando o PDF à mão, e gere de novo.
- Revise de novo só as páginas corrigidas (máximo 2 rodadas; depois leve ao dono).
- Promessa que não confere: corrija o produto **ou** a página — os dois precisam dizer a mesma coisa.
- Registre em `revisoes/material-AAAA-MM-DD/correcoes.md` o que foi corrigido e onde.

## 3. Portão M (dono)
Mostre ao dono: resumo dos achados e correções, contagem por gravidade, o que ficou como cosmético e
5–8 páginas de amostra em imagem (incluindo as corrigidas). **Só com o "aprovado" do dono na conversa**,
gere `revisoes/material-AAAA-MM-DD/APROVACAO.md`:

```
aprovado_por: Gefferson
data: AAAA-MM-DD
pendencias_bloqueia_atrapalha: 0
<sha256>  produto/final/<arquivo>.pdf
<sha256>  produto/bumps/<n>_<slug>/<slug>.pdf
...
```
(`cd ofertas/<pasta> && sha256sum produto/final/*.pdf produto/bumps/*/*.pdf >> revisoes/.../APROVACAO.md`)

Confira com `ferramentas/conferir_material.py` e registre no `status.md`. Depois disso seguem:
Hotmart (`cadastro-e-pixel`), criativos (`top5-criativos`) e campanhas (`subir-campanhas`).

## 4. Aprender
Todo erro encontrado vira uma linha em `aprendizados/processo.md` (seção "Material"), com a causa e a
regra para o gerador não repetir. Na próxima oferta, leia essa seção **antes** de gerar o produto.
