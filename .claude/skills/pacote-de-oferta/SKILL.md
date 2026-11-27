---
name: pacote-de-oferta
description: Rotina do MINERADOR — minera ofertas low ticket em inglês, escolhe a melhor, faz a conferência manual na Biblioteca de Anúncios, monta dossiê e briefing e entrega um "pacote de oferta" num pull request para o operador. Use quando o minerador disser "minerar", "montar pacote", "próxima oferta" ou mandar links de ofertas para avaliar.
---
Leia antes: `docs/07_divisao-do-trabalho.md` (o que é um pacote pronto), `docs/03_mineracao.md`
(critérios), `CLAUDE.md` (regras), `mineracao/descartadas.md` (não repetir o que já foi descartado),
`docs/08_inteligencia-de-anuncios.md` e **`aprendizados/o-que-vende.md`** (priorize nichos, ângulos
e formatos que já venderam para nós; evite o que já falhou).

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
   Em seguida chame o `pesquisador-de-anuncios` para o nicho e a oferta escolhida: ele preenche a
   seção **"Inteligência de anúncios"** do `dossie.md` (padrões fortes a usar, a evitar, o que
   conferir à mão) e acrescenta os padrões em `aprendizados/padroes-externos.md`.
   Revise você mesmo: nada de saúde/TDAH/dinheiro garantido, nada traduzido literal, entregáveis que
   dá para produzir com qualidade por código/IA.
7. **Relatório do pacote:** preencha `ofertas/<pasta>/relatorio-pacote.md` (modelo já copiado de
   `_modelo/`) com TODOS os campos: números conferidos na Biblioteca, tabela dos anúncios que duram
   (anunciante, ativos, dias no ar, variações, formato, duração, gancho de 3 s, produto por dentro,
   CTA, preço, link), 5 padrões a usar e 3 a evitar com evidência e grau, táticas como opinião,
   o que pesou de `aprendizados/o-que-vende.md`, encaixe no Brasil e o CPA máximo desta oferta.
8. **status.md:** etapas 1 e 2 ✅ com data; P1 = "aguardando operador".
9. **Conferência automática (obrigatória):** rode `python3 ferramentas/conferir_pacote.py ofertas/<pasta>`.
   Só siga se sair "PACOTE OK". Se faltar algo, complete e rode de novo.
10. **Entregar:** commit + push do ramo e abra um pull request `Pacote de oferta: <nome> (<data>)`
   com o **relatório do pacote inteiro** na descrição (o modelo de PR já pede isso), incluindo: produto e promessa BR · preço · nº de anúncios e data conferidos ·
   nota · por que pode dar certo no Brasil · principal risco · **3 padrões de anúncio mais fortes
   (com evidência)** · o que de `aprendizados/o-que-vende.md` pesou na escolha · links (Biblioteca, página de referência,
   concorrentes BR). Não faça merge.
11. Se o operador devolver, registre em `mineracao/descartadas.md` (data, oferta, motivo) e volte ao 2.
