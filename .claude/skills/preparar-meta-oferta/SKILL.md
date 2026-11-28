---
name: preparar-meta-oferta
description: Prepara de uma vez tudo o que o dono precisa fazer na Meta para uma oferta nova (Página, pixel, ligação com a conta de anúncios e Windsor), com os prompts da extensão do Chrome prontos e numa ordem que não trava. Use antes de cadastrar a oferta (etapa 5), depois do Portão M.
---
Conta de anúncios, portfólio e Windsor já existem (ver `docs/06_stack-e-conexoes.md` e `aprendizados/processo.md`).
Por oferta só se repetem 4 coisas. Gere **uma mensagem só** para o dono com os 4 blocos abaixo, já com o nome
da oferta, as imagens e os links preenchidos, e espere a volta com os dois IDs.

0. Antes: gere foto de perfil (720×720) e capa (1640×624) da Página com a identidade da página de vendas e publique em
   `publicado/<slug>/facebook/` (modelo: `ofertas/2026-11-26_atividades-foco/facebook/gerar.cjs`).

**Bloco 1 — Página (extensão, dentro do portfólio Balles Tech Energia Solar)**
> Em business.facebook.com/settings → Contas → Páginas → Adicionar → Criar uma Página: nome "<Nome>", categoria
> "<categoria>", bio "<1 frase>". Foto de perfil e capa: baixe <URL perfil> e <URL capa> e use. Em Informações, e-mail
> acessos@ballestech.com.br e site <URL da página de vendas>. Sem Instagram, sem endereço e sem telefone.
> No fim, me diga o ID da Página que aparece embaixo do nome nas Configurações (não o número do endereço profile.php).

**Bloco 2 — Pixel (extensão)**
> No Gerenciador de Eventos, crie um conjunto de dados Web "Pixel Oferta <Nome>" no portfólio Balles Tech Energia Solar.
> Escolha instalar manualmente e pare. Em Ativos conectados, adicione a conta de anúncios "Ofertas Low Ticket".
> Me diga o ID do pixel. Não gere token.

**Bloco 3 — Windsor (o dono, 1 minuto)**: abrir o link de conexão do Windsor (pegue com
`get_connector_connect_info`, conector `facebook`) → "Editar configurações" → marcar a Página nova → na tela final
do Windsor, manter marcada "Ofertas Low Ticket" → Save.

**Bloco 4 — Token da API de Conversões (o dono, nunca no chat)**: Gerenciador de Eventos → pixel → Configurações →
API de Conversões → Gerar token → colar na Hotmart, no pixel do produto principal e de cada bump.

Com os IDs de volta: instale o pixel na página (`<!-- PIXEL META -->`), registre em `campanha.md`, confira com
`get_connectors` se o Windsor vê a conta e teste os eventos simulando navegador comum (ver `aprendizados/processo.md`).
