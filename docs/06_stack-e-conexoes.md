# 06 — Stack, conexões e o que está pronto

Situação levantada em 2026-11-26 nesta conta (diagnóstico respondido pelo dono no mesmo dia). Atualize a coluna "Situação" quando algo mudar.

| Função | Ferramenta da aula | Como entra no Claude | Situação | Alternativa já disponível |
|---|---|---|---|---|
| Mineração 24/7 | ChatGPT Dot / Grok Bot / ChatGPT Work | Agente externo manda links | ⬜ a definir | Agente `minerador-de-ofertas` sob demanda (busca na web) |
| Cérebro | Claude (Max / Claude Code) | — | ✅ Claude Code | — |
| Navegador | Extensão do Claude para Chrome | Abas logadas (Hotmart, Facebook, Gerenciador de Eventos) | ✅ decidido: computador do dono ligado ao Claude (Remote Control) | Passo a passo manual |
| Hospedagem | Hostinger | MCP Hostinger | ✅ conectado · plano **VPS KVM 2** (Ubuntu 24.04) + domínios ballestech.com.br, ballestech.shop, balleseballes.com.br/.online, engajadamente.cloud | Caddy único na VPS (`infra/`), uma pasta por oferta: `ofertas.ballestech.com.br/<slug>/` |
| Checkout | Weven (aula) | Aba no Chrome | ✅ decidido: **Hotmart** | — |
| Imagens, mockups, GIFs | Higgsfield | Plugin | ⬜ não conectado | ElevenLabs (imagem/vídeo), Picsart, Canva — conectados |
| Narração | ElevenLabs | Plugin/MCP | ✅ conectado | — |
| Trilha | Epidemic Sound | Plugin | ⬜ não conectado | Trilhas livres de direitos baixadas manualmente |
| Campanhas | Meta Ads MCP (não oficial) | MCP configurado à mão | ✅ decidido: **Windsor.ai** (conector `facebook`) | ⬜ falta conectar a conta de anúncios no Windsor |
| Métricas | Gerenciador de Anúncios | — | ⬜ | Windsor.ai (`facebook`) |

## O que cada etapa precisa

1. **Mineração:** nada obrigatório. Opcional: minerador externo 24/7 que salve links em uma
   planilha/pasta que o Claude lê.
2. **Dossiê:** acesso à página de referência (web). Vídeos dos anúncios: baixar e transcrever
   (ElevenLabs transcreve áudio).
3. **Página:** VPS da Hostinger com Caddy + sincronizador do git (`infra/README.md`);
   DNS `ofertas.ballestech.com.br` → IP da VPS (já criado). Mockups/GIFs: gerador de imagem
   e vídeo.
4. **Entregável:** nada externo (Python gera PDF, planilhas e .zip). Imagens: gerador de imagem.
5. **Cadastro e pixel:** Hotmart e Facebook só têm interface web → computador do dono ligado
   ao Claude (Remote Control) com as abas já logadas.
6. **Criativos:** gerador de cenas + ElevenLabs + montagem com ffmpeg.
7. **Campanhas:** Windsor.ai com a conta de anúncios conectada (conector `facebook`).

## Meta Ads — o que já está pronto (configurado em 2026-11-28, vale para todas as ofertas)

| Item | Valor | Repete por oferta? |
|---|---|---|
| Portfólio empresarial | Balles Tech Energia Solar (873867164377276) | não |
| Conta de anúncios | **Ofertas Low Ticket · 1534301375187089** (pagamento, telefone verificado) | não |
| Windsor.ai | conector `facebook` com a conta acima liberada | não |
| Página do Facebook | uma por oferta (ex.: Dez Minutinhos · **1532919519896130**) | **sim** |
| Pixel | um por oferta (ex.: Pixel Oferta Dez Minutinhos · 2360537971467958) | **sim** |

Checklist de uma oferta nova (o resto o Claude faz pela API):
1. Criar a Página da oferta **dentro do portfólio** (business.facebook.com/settings → Contas → Páginas → Adicionar → Criar).
2. Criar o pixel no Gerenciador de Eventos e, em Ativos conectados, ligar a conta **Ofertas Low Ticket**.
3. Liberar a Página nova no Windsor: refazer o link de conexão do Windsor → "Editar configurações" → marcar a Página.
4. Passar ao Claude o **ID da Página do portfólio** (Configurações → Páginas → ID embaixo do nome). Atenção: o número de
   `profile.php?id=` é o ID do perfil e a API de anúncios recusa ("Página ausente").

Lições: conta de anúncios pessoal sem pagamento não entra no portfólio; a conta precisa ter forma de pagamento até
para criar anúncio pausado; a conta precisa estar ligada ao pixel do conjunto.
