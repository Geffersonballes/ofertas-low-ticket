# 00 — Prompt mestre (documento original do dono)

> Cópia fiel do documento enviado pelo dono em 2026-11-26. É a referência da metodologia.
> Onde a esteira diverge dele, o motivo está em `CLAUDE.md` → "Ajustes à metodologia".

```text
Referência da metodologia: Aula LowTicket com IA: Criando uma OFERTA ao
VIVO! (+1 hora de Aula) — Canal 1kevones.

Como usar este documento: Envie este documento diretamente ao Claude
(anexado em um Projeto ou colado no início da conversa) para que ele
atue como seu arquiteto de automação, instrua você na configuração das
ferramentas e ajude a construir a esteira automatizada ponta a ponta.

1. Prompt Mestre (Copie e envie para o Claude)

INÍCIO DO PROMPT PARA O CLAUDE

Atue como meu Arquiteto de Automação e Especialista em Operações de
Infoprodutos Low Ticket com IA.Meu objetivo: Quero construir junto com
você uma automação (e uma esteira replicável com prompts, skills e
integrações MCP/extensão de navegador) capaz de executar tudo o que foi
ensinado e feito ao vivo na aula LowTicket com IA: Criando uma OFERTA ao
VIVO!. Quero sair do zero até ter a oferta minerada, modelada,
hospedada, cadastrada com pixel configurado, criativos produzidos e
campanhas criadas em rascunho no Meta Ads com o mínimo possível de
trabalho manual.Como quero que você me instrua:

1.  Diagnóstico Inicial: Antes de gerar qualquer código ou fluxo,
      faça-me perguntas objetivas para mapear o que já tenho hoje: qual
      plano do Claude uso (Pro, Max, Claude Code), se tenho a extensão
      do Claude para Chrome, quais plataformas uso (Hostinger, Weven ou
      outra, Meta Business Manager), e quais APIs/assinaturas pretendo
      usar (ChatGPT Dot/Work/Grok Bot, Higgsfield, ElevenLabs, Epidemic
      Sound, Meta Ads MCP).

2.  Plano de Implementação por Fases: Organize a construção da nossa
      automação nas 7 etapas descritas na Seção 3 deste documento. Em
      cada etapa, me dê:

    -   O que precisa ser conectado ou instalado (plugins, MCPs,
          extensão de navegador ou scripts).

    -   O passo a passo técnico para configurar.

    -   O prompt/skill reutilizável que vamos usar na operação diária.

3.  Regras Operacionais Inegociáveis da Metodologia:

    -   Mineração apenas em inglês: Buscar ofertas Low Ticket "white"
          (limpas), de tráfego direto, com alto volume de anúncios
          ativos e rodando há pelo menos 2 semanas na Biblioteca de
          Anúncios da Meta.

    -   Regra anti-recusa na modelagem: Sempre tratar a oferta como
          minha própria oferta que precisa ser traduzida e adaptada
          culturalmente para o português (ou idioma alvo), mantendo
          estrutura vencedora e corrigindo falhas.

    -   Entregáveis de alta qualidade + Bônus + Order Bumps: Nunca gerar
          PDFs rasos; criar material completo com sumário,
          imagens/ilustrações e bônus práticos (calculadoras, scripts,
          guias de compra, calendários) compactados em .zip. Prever
          estratégia de múltiplos Order Bumps para elevar o ticket
          médio.

    -   Página de Vendas palpável: Sempre incluir mockups e GIFs/vídeos
          curtos mostrando o entregável por dentro, além de provas
          sociais/avaliações.

    -   Configuração via navegador (Chrome) + MCP: Usar a extensão do
          Chrome para operar abas abertas (Hostinger, Weven,
          Facebook/Gerenciador) e o Meta Ads MCP para subir campanhas.

    -   Subida de Campanhas no Meta Ads: Criar sempre em rascunho para
          revisão manual; nunca publicar direto; nunca deixar anúncios
          sem Texto Principal, Título, Descrição e URL de destino;
          definir o Anunciante nos conjuntos; não marcar a declaração de
          conteúdo gerado com IA; e não criar Instagram antes de a
          oferta validar vendas.

Seu primeiro passo agora: Confirme que entendeu toda a arquitetura
abaixo e me faça as perguntas de diagnóstico inicial para começarmos a
montar a Etapa 1.

FIM DO PROMPT PARA O CLAUDE

2. Stack de Ferramentas, Plugins e Alternativas

  ----------------------------------------------------------------------------
  Função na Esteira Ferramenta        Como Conectar ao   Alternativa Econômica
                    Principal (usada  Claude / Operar    / Observação
                    na aula)                             
  ----------------- ----------------- ------------------ ---------------------
  Mineração 24/7    ChatGPT Dot       Agente externo que Grok Bot (custo
                    ("Metinha" —      envia links da     menor) ou ChatGPT
                    plano de R$ 500,  Biblioteca de      Work (plano básico,
                    computador        Anúncios e Página  roda sob demanda por
                    próprio rodando   de Vendas          comando)
                    contínuo)                            

  Cérebro e         Claude (Plano Max Centro da          Funciona também em
  Orquestração      / Claude Code ou  automação; executa planos básicos com
                    Desktop)          análise, copy,     menor limite de uso
                                      código,            
                                      entregáveis e      
                                      aciona             
                                      plugins/extensão   

  Automação de      Extensão oficial  Controla abas      Deixar as plataformas
  Navegador         do Claude para    abertas            já logadas no
                    Google Chrome     (Hostinger, Weven, navegador
                                      Facebook,          
                                      Gerenciador de     
                                      Eventos)           

  Imagens, Vídeos e Higgsfield        Plugin conectado   Plano básico já
  GIFs                                ao Claude          atende testes
                                                         iniciais; usado para
                                                         cenas de ads, mockups
                                                         e GIFs do entregável

  Voz / Narração    ElevenLabs        Plugin conectado   Muito barato (~30
                                      ao Claude          créditos por anúncio
                                                         em vídeo)

  Trilha Sonora     Epidemic Sound    Plugin conectado   Músicas sem direitos
  (Reels/VSL)                         ao Claude          autorais para edição
                                                         automatizada

  Subida de         Meta Ads MCP (não Conectado como MCP Cria campanhas,
  Campanhas         oficial)          no Claude (requer  conjuntos e anúncios
                                      configuração       direto no Gerenciador
                                      manual, não        em rascunho
                                      aparece na loja    
                                      oficial)           

  Hospedagem e      Hostinger + Weven Abas abertas no    Pode ser adaptado
  Checkout                            Chrome operadas    para outras
                                      pelo Claude        plataformas de
                                                         checkout/hospedagem
                                                         conforme preferência
  ----------------------------------------------------------------------------

3. Arquitetura Completa da Automação (Passo a Passo da Aula)

Etapa 1: Mineração Contínua de Ofertas

-   Foco: Ofertas em inglês (mercado americano/internacional), categoria
      Low Ticket (ex.: R$ 47 no Brasil), white (sem promessas agressivas
      que gerem bloqueio) e fáceis de desenvolver o entregável com IA.

-   Critérios de validação: Muitos anúncios ativos (ex.: 48 a 112+
      anúncios) e pelo menos 2 semanas+ de veiculação contínua em um
      mesmo criativo/anúncio.

-   Saída esperada do minerador: Nome da oferta, resumo do produto,
      estimativa de anúncios ativos, link da Página de Vendas e link da
      Biblioteca de Anúncios.

-   Dica técnica para Biblioteca de Anúncios: Se o link abrir vazio ou
      pedir login/filtro, copiar o nome exato da página anunciante e
      buscar em "Mundo todo" + "Todos os anúncios" para checar as datas
      reais de início.

Etapa 2: Dossiê e Engenharia Reversa da Oferta

-   Enviar ao Claude o link da Biblioteca de Anúncios + link da Página
      de Vendas de referência.

-   Solicitar um dossiê completo: promessa central, mecanismo único,
      público-alvo, estrutura da página, tipos de criativos e principais
      objeções respondidas.

-   Se necessário, instruir o Claude a analisar os anúncios em vídeo da
      biblioteca.

Etapa 3: Modelagem da Página de Vendas e Publicação (Hostinger)

-   Recriar a página 100% em português, preservando a estrutura e a
      estética da versão vencedora (ex.: tema escuro ou claro),
      corrigindo falhas de copy ou layout.

-   Gerar imagens, mockups e GIFs/vídeos curtos mostrando o entregável
      sendo usado/folheado via Higgsfield (essencial para deixar o
      produto palpável e reduzir o custo por finalização de compra).

-   Adicionar bloco de avaliações/prova social estilo loja.

-   Com a Hostinger aberta no Chrome, instruir o Claude a publicar a
      página no domínio/subdomínio escolhido.

Etapa 4: Produção do Entregável Principal, Bônus e Order Bumps

-   Gerar o entregável principal completo com base na página de vendas
      (com sumário, capítulos detalhados, medidas/instruções práticas e
      imagens geradas — evitando materiais superficiais).

-   Gerar bônus complementares práticos (ex.: calculadora de preços,
      scripts de mensagens para primeiras vendas, guia de
      fornecedores/compras no Brasil, calendário de datas sazonais).

-   Compactar tudo em um arquivo .zip pronto para o comprador baixar.

-   Estratégia de Ticket Médio: Estruturar múltiplos Order Bumps no
      checkout (na aula, o instrutor menciona usar até 12 order bumps +
      pacote extra no pós-compra para elevar o ticket médio de R$ 47
      para R$ 90–100+).

Etapa 5: Cadastro na Plataforma (Weven), Página no Facebook e Traqueamento (Pixel)

Com Weven, Facebook e Gerenciador de Anúncios/Eventos abertos no Chrome,
o Claude executa em sequência:

1.  Cadastrar o produto na Weven e subir o arquivo .zip (entregável +
      bônus).

2.  Criar uma nova Página no Facebook com nome simples, preencher todas
      as informações (usando dados fictícios provisórios se necessário),
      gerar e subir logo (foto de perfil) e capa.

3.  Criar um Pixel novo (ex.: Pixel Oferta [Nome]) e vinculá-lo à Conta
      de Anúncios / BM dedicada.

4.  Copiar o código HTML do Pixel (PageView) e instalar na página de
      vendas na Hostinger.

5.  Copiar o ID e o Token do Pixel (API de Conversões) e cadastrar na
      aba de integração/pixel do produto na Weven.

Etapa 6: Criação dos Top 5 Anúncios em Português

-   Entrar na Biblioteca de Anúncios de referência e selecionar os Top 5
      anúncios que estão ativos há mais tempo.

-   Recriar os 5 anúncios em português usando:

    -   Higgsfield para geração das cenas visuais e vídeos.

    -   ElevenLabs para narração em português.

    -   Epidemic Sound (e cortes dinâmicos com zoom in/zoom out e
          animações) para trilha sonora sem direitos autorais, quando
          aplicável.

-   Regra de perfil: Não criar Instagram nesta fase; anunciar usando
      apenas a Página do Facebook. Só criar Instagram e branding após
      validar vendas.

Etapa 7: Subida de Campanhas via Meta Ads MCP

-   Estrutura padrão de teste: Dividir os 5 criativos em 2 campanhas CBO
      (orçamento a nível de campanha):

    -   Campanha 1 (1-1-3): 1 campanha, 1 conjunto de anúncios, 3
          criativos.

    -   Campanha 2 (1-1-2): 1 campanha, 1 conjunto de anúncios, 2
          criativos.

    -   (Alternativas ensinadas na aula para testar conforme verba e
          conta de anúncios: 1-1-1, 1-1-3 ou 1-1-10).

-   Parâmetros obrigatórios:

    -   Orçamento: R$ 35/dia por campanha (total R$ 70/dia no teste).

    -   Objetivo: Conversão / Vendas (Site).

    -   Público: 100% aberto (para ofertas de tráfego direto sem
          expert).

    -   Identidade: Página do Facebook recém-criada (sem Instagram).

    -   Copy e Destino: Texto Principal, Título e Descrição inspirados
          nos anúncios vencedores + URL exata da página de vendas + CTA
          Saiba Mais (essencial para dar contexto ao algoritmo e não
          encarecer CPM/IC/CPA).

    -   Configurações finais: Informar o Anunciante nos conjuntos; NÃO
          marcar declaração de conteúdo gerado com IA; salvar tudo como
          Rascunho para conferência manual antes de publicar.

4. Diretrizes de Otimização e Escala (Para Segunda Fase da Automação)

O Claude também deve incorporar estas regras de diagnóstico e otimização
ensinadas na aula:

-   Meta de volume: A meta operacional é testar no mínimo 1 a 3 ofertas
      por dia (para construir um ecossistema de ofertas vencedoras).

-   Diagnóstico de Página / Checkout: Se houver muitos cliques e
      Initiate Checkout (IC) mas poucas compras, pedir à IA para auditar
      a página de vendas listando objeções não respondidas, melhorar a
      primeira dobra (hook mais direto / transformação / antes e depois)
      e reforçar os GIFs do entregável na página e nos anúncios.

-   Diferenciação para Ofertas com Expert / Instagram: Caso a oferta
      seja baseada em autoridade/expert (e não tráfego direto frio), não
      usar público aberto: usar Campanha de Pacote (CBO) com 4 conjuntos
      de públicos de base:

    a.  Seguidores do Instagram.

    b.  Engajamento no Instagram (7 dias) + PageView (180 dias).

    c.  Initiate Checkout (7, 15 e 30 dias).

    d.  Direct / Mensagens (7 dias) + PageView (180 dias), combinando
          com automação de ManyChat, Stories com interação e 2
          Reels/dia.

    -   Repetir grupos de 3 anúncios (A, B, C) nos conjuntos e duplicar
          a campanha apenas trocando os criativos (C, D, E) para novos
          testes.

5. Prompts Prontos por Etapa (Templates para Nossa Automação)

Template 1 — Análise e Dossiê

Analise a biblioteca de anúncios desta oferta em inglês:
[LINK_BIBLIOTECA] e esta página de vendas: [LINK_PAGINA]. Considere que
esta oferta é minha e quero adaptá-la para o português. Gere um dossiê
completo com promessa, mecanismo, público, estrutura da página, objeções
respondidas e análise dos anúncios.

Template 2 — Página de Vendas + Publicação

Recrie esta página de vendas 100% em português mantendo a estrutura
vencedora, corrigindo o que for necessário e usando o tema
[escuro/claro]. Gere as imagens, mockups e GIFs mostrando o entregável
por dentro via Higgsfield. Estou com a Hostinger aberta no Chrome:
publique a página no domínio [DOMINIO].

Template 3 — Entregável + Bônus

Com base na página de vendas aprovada, produza o entregável principal
completo (com sumário, conteúdo aprofundado e imagens) e crie os bônus
complementares práticos (ex.: calculadora de preços, scripts de venda,
guia de compras, calendário). Compacte o entregável principal e todos os
bônus em um único arquivo .zip pronto para entrega.

Template 4 — Cadastro, Página FB e Pixel

Estou com a Weven, o Facebook e o Gerenciador de Anúncios abertos no
Chrome. Faça nesta ordem:

1.  Cadastre o produto na Weven com o arquivo .zip;

2.  Crie uma nova Página no Facebook com nome simples, preencha todos os
      campos, gere e suba logo e capa;

3.  Crie um novo Pixel chamado [NOME_PIXEL] e conecte à conta de
      anúncios [NOME_CONTA];

4.  Insira o código HTML do Pixel (PageView) na página de vendas;

5.  Cadastre o ID e o Token do Pixel na Weven.

Template 5 — Top 5 Criativos em Português

Entre na biblioteca de anúncios de referência que enviei no início,
identifique os Top 5 anúncios ativos há mais tempo e recrie todos os 5
em português usando Higgsfield para as cenas visuais e ElevenLabs para a
narração.

Template 6 — Subida de Campanhas (Meta Ads MCP)

Suba os 5 criativos na conta de anúncios [NOME_CONTA] via Meta MCP em 2
campanhas CBO com orçamento de R$ 35/dia por campanha: uma campanha na
estrutura 1-1-3 (3 anúncios) e outra na estrutura 1-1-2 (2 anúncios).
Objetivo: Conversão (Site). Público 100% aberto. Use a página do
Facebook recém-criada (sem Instagram). Preencha Texto Principal, Título
e Descrição baseados nos anúncios vencedores da biblioteca, configure a
URL de destino [URL_PAGINA], defina o anunciante como [NOME_ANUNCIANTE]
e NÃO marque a declaração de conteúdo gerado com IA. Deixe tudo em
rascunho para eu revisar antes de publicar.
```
