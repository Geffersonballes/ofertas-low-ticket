---
name: pagina-de-vendas
description: Etapa 3 — recria a página de vendas em pt-BR com a estrutura e a estética da vencedora, gera mockups e GIFs do entregável e publica na Hostinger. Use depois do dossiê aprovado.
---
Entrada: pasta da oferta, `[TEMA escuro/claro]`, `[DOMINIO ou subdomínio]`.

1. `copywriter-de-pagina` → `pagina/copy.md`, seguindo a ordem de seções do `dossie.md`,
   corrigindo as falhas listadas. Texto próprio, nunca tradução literal.
2. Mídias (em `pagina/img/`): mockup da capa, mockup do pacote completo, 2–4 GIFs/vídeos curtos
   do entregável sendo folheado/usado. Use o gerador conectado (ver `docs/06_stack-e-conexoes.md`).
   Para GIF do material real, prefira capturar as páginas verdadeiras do produto e animar com ffmpeg.
3. `construtor-de-pagina` → `pagina/index.html`. Bloco de avaliações só com avaliações reais
   (ver `CLAUDE.md`).
3b. Revisão (até 2 rodadas): `critico-de-conversao` e `editor-de-copy` em paralelo sobre as fotos da
   página (390 e 1280 px); depois o `diretor-de-arte-web` aplica copy + design e confere de novo. Relatórios
   em `pagina/revisoes/`. Pare quando o crítico der nota ≥ 8 ou após a 2ª rodada.
4. Publicação: copie a página aprovada (index.html + img/) para `publicado/<slug>/` e faça
   push no ramo `main`. Em até 60 s ela está em `https://ofertas.ballestech.com.br/<slug>/` (ver `infra/README.md`).
   **Antes de publicar, mostre a página ao dono** e confira a URL depois do push.
5. Registre a URL final no `status.md`.
