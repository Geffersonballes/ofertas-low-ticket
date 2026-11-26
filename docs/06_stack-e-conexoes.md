# 06 — Stack, conexões e o que está pronto

Situação levantada em 2026-11-26 nesta conta (diagnóstico respondido pelo dono no mesmo dia). Atualize a coluna "Situação" quando algo mudar.

| Função | Ferramenta da aula | Como entra no Claude | Situação | Alternativa já disponível |
|---|---|---|---|---|
| Mineração 24/7 | ChatGPT Dot / Grok Bot / ChatGPT Work | Agente externo manda links | ⬜ a definir | Agente `minerador-de-ofertas` sob demanda (busca na web) |
| Cérebro | Claude (Max / Claude Code) | — | ✅ Claude Code | — |
| Navegador | Extensão do Claude para Chrome | Abas logadas (Hotmart, Facebook, Gerenciador de Eventos) | ✅ decidido: computador do dono ligado ao Claude (Remote Control) | Passo a passo manual |
| Hospedagem | Hostinger | MCP Hostinger | ✅ conectado · plano **VPS KVM 2** (Ubuntu 24.04) + domínios ballestech.com.br, ballestech.shop, balleseballes.com.br/.online, engajadamente.cloud | Páginas estáticas servidas na VPS (nginx), um subdomínio por oferta |
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
3. **Página:** VPS da Hostinger (nginx servindo HTML estático por subdomínio) + DNS do domínio
   apontado para o IP da VPS (MCP Hostinger gerencia o DNS). Mockups/GIFs: gerador de imagem
   e vídeo.
4. **Entregável:** nada externo (Python gera PDF, planilhas e .zip). Imagens: gerador de imagem.
5. **Cadastro e pixel:** Hotmart e Facebook só têm interface web → computador do dono ligado
   ao Claude (Remote Control) com as abas já logadas.
6. **Criativos:** gerador de cenas + ElevenLabs + montagem com ffmpeg.
7. **Campanhas:** Windsor.ai com a conta de anúncios conectada (conector `facebook`).
