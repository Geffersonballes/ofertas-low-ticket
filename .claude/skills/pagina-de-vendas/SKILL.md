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
4. Publicação: na VPS Hostinger (KVM 2), em `/var/www/<subdominio>/` servido pelo nginx, com
   registro DNS A do subdomínio apontando para o IP da VPS (MCP Hostinger) e HTTPS (certbot).
   **Antes de publicar, mostre a página ao dono e confirme o domínio** — publicar sobrescreve o site.
5. Registre a URL final no `status.md`.
