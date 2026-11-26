---
name: pacote-de-oferta
description: Rotina do MINERADOR — minera ofertas low ticket em inglês, escolhe a melhor, faz a conferência manual na Biblioteca de Anúncios, monta dossiê e briefing e entrega um "pacote de oferta" num pull request para o operador. Use quando o minerador disser "minerar", "montar pacote", "próxima oferta" ou mandar links de ofertas para avaliar.
---
Leia antes: `docs/07_divisao-do-trabalho.md` (o que é um pacote pronto), `docs/03_mineracao.md`
(critérios), `CLAUDE.md` (regras) e `mineracao/descartadas.md` (não repetir o que já foi descartado).

1. **Ramo:** crie `mineracao/AAAA-MM-DD_<slug-provisorio>` a partir do `main` atualizado.
2. **Minerar:** se o minerador trouxe links, avalie esses; senão chame o agente `minerador-de-ofertas`
   (meta: 5 a 10 candidatas, nichos variados, nada já descartado). Grave `mineracao/AAAA-MM-DD.md`.
3. **Escolher com o minerador:** mostre as 3 melhores (nome, produto, nota, por quê, risco) e
   pergunte qual vira pacote.
4. **Conferência manual (obrigatória):** a Biblioteca bloqueia acesso automático. Peça ao minerador
   para abrir o link da Biblioteca da candidata ("Mundo todo" + "Todos os anúncios" + ativos),
   anotar o nº de anúncios ativos e a data de início do mais antigo ainda ativo, e salvar 3–5 prints.
   Se ele usa a extensão do Claude para Chrome, você pode operar a aba e tirar os prints.
   Reprovou no corte (< 20 ativos ou nada ativo há 14+ dias)? Volte ao passo 3.
5. **Pasta:** `cp -r ofertas/_modelo ofertas/AAAA-MM-DD_<slug>`; prints em `referencia/`.
6. **Dossiê e briefing:** chame o agente `analista-de-oferta` com os links e os números conferidos.
   Revise você mesmo: nada de saúde/TDAH/dinheiro garantido, nada traduzido literal, entregáveis que
   dá para produzir com qualidade por código/IA.
7. **status.md:** etapas 1 e 2 ✅ com data; P1 = "aguardando operador".
8. **Entregar:** commit + push do ramo e abra um pull request `Pacote de oferta: <nome> (<data>)`
   com este resumo na descrição: produto e promessa BR · preço · nº de anúncios e data conferidos ·
   nota · por que pode dar certo no Brasil · principal risco · links (Biblioteca, página de referência,
   concorrentes BR). Não faça merge.
9. Se o operador devolver, registre em `mineracao/descartadas.md` (data, oferta, motivo) e volte ao 2.
