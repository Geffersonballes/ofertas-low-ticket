# 06 — Stack, conexões e o que está pronto

Situação levantada em 2026-11-26 nesta conta. Atualize a coluna "Situação" quando algo mudar.

| Função | Ferramenta da aula | Como entra no Claude | Situação | Alternativa já disponível |
|---|---|---|---|---|
| Mineração 24/7 | ChatGPT Dot / Grok Bot / ChatGPT Work | Agente externo manda links | ⬜ a definir | Agente `minerador-de-ofertas` sob demanda (busca na web) |
| Cérebro | Claude (Max / Claude Code) | — | ✅ Claude Code | — |
| Navegador | Extensão do Claude para Chrome | Abas logadas (Hostinger, Weven, Facebook) | ⬜ a confirmar | Sessão do Claude no computador do dono (Remote Control) |
| Hospedagem | Hostinger | MCP Hostinger (deploy direto, sem navegador) | ✅ conectado · 0 sites na conta | — |
| Checkout | Weven | Aba no Chrome | ⬜ a confirmar | Kiwify/Hotmart/Cakto (mesma lógica) |
| Imagens, mockups, GIFs | Higgsfield | Plugin | ⬜ não conectado | ElevenLabs (imagem/vídeo), Picsart, Canva — conectados |
| Narração | ElevenLabs | Plugin/MCP | ✅ conectado | — |
| Trilha | Epidemic Sound | Plugin | ⬜ não conectado | Trilhas livres de direitos baixadas manualmente |
| Campanhas | Meta Ads MCP (não oficial) | MCP configurado à mão | ⬜ não conectado | Windsor.ai (conector `facebook` tem ações de criar campanha/conjunto/anúncio) — falta conectar a conta de anúncios |
| Métricas | Gerenciador de Anúncios | — | ⬜ | Windsor.ai (`facebook`) |

## O que cada etapa precisa

1. **Mineração:** nada obrigatório. Opcional: minerador externo 24/7 que salve links em uma
   planilha/pasta que o Claude lê.
2. **Dossiê:** acesso à página de referência (web). Vídeos dos anúncios: baixar e transcrever
   (ElevenLabs transcreve áudio).
3. **Página:** MCP Hostinger + plano de hospedagem com domínio. Mockups/GIFs: gerador de imagem
   e vídeo.
4. **Entregável:** nada externo (Python gera PDF, planilhas e .zip). Imagens: gerador de imagem.
5. **Cadastro e pixel:** Weven e Facebook só têm interface web → extensão do Chrome no
   computador do dono, ou o dono faz com o passo a passo gerado pelo Claude.
6. **Criativos:** gerador de cenas + ElevenLabs + montagem com ffmpeg.
7. **Campanhas:** Meta Ads MCP **ou** Windsor.ai com a conta de anúncios conectada.
