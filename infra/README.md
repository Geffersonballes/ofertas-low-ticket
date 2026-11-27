# Infraestrutura — publicação das páginas

- **Servidor:** VPS Hostinger KVM 2 (Ubuntu 24.04, IP 189.24.15.6).
- **Servidor web:** um único Caddy (`infra/docker-compose.yml`) com HTTPS automático, servindo:
  - as ofertas: `publicado/<slug>/index.html` → `https://ofertas.ballestech.com.br/<slug>/`
  - o site que já existia na VPS (landing do robô de promoções), sem mudança para quem acessa.
- **Publicar:** o Claude copia a página aprovada para `publicado/<slug>/` e faz push no ramo
  `main`. O contêiner `sync` baixa o repositório a cada 60 s; não precisa reiniciar nada.
- **DNS:** `ofertas.ballestech.com.br` com registro A → 189.24.15.6 (zona na Hostinger, criado em 2026-11-26).
  A raiz `ballestech.com.br` é o site da Balles Tech (HostGator) e o e-mail é da Hostinger: não mexer.

Uma URL por oferta no mesmo domínio (`/slug/`) evita criar DNS e certificado a cada oferta.
Se uma oferta precisar de domínio próprio, acrescente um bloco no `Caddyfile`.

## Como está instalado (feito pelo Claude via API da Hostinger, sem terminal)

Dois projetos Docker na VPS, criados com a operação `vps_docker_create` do MCP Hostinger:

| Projeto | O que faz | Compose |
|---|---|---|
| `ofertas-sync` | Gera a chave de leitura em `/opt/ofertas-chave/`, clona o repositório em `/opt/ofertas-low-ticket` e faz `fetch` + `reset` do ramo `main` a cada 60 s | `infra/compose-sync.yml` |
| `ofertas-web` | Caddy único nas portas 80/443: ofertas, landing dos achadinhos e o **painel** (`painel.ballestech.com.br`, com senha; o hash da senha fica só na VPS) | `infra/compose-web.yml` |

Para conferir a sincronização: os logs do `ofertas-sync` (`vps_docker_logs`) mostram
"sincronizado em <commit>" a cada atualização, ou "ERRO no fetch".

A chave pública está cadastrada em GitHub → Settings → Deploy keys ("VPS", só leitura).
O projeto antigo `landing` (em `/opt/tutoriais/robo-promocoes/landing`) fica **parado, não apagado**.

Mudou o `Caddyfile`? Depois do push e da sincronização, reinicie o projeto `ofertas-web`
(`vps_docker_restart`).

## Voltar ao estado anterior

1. `vps_docker_stop` em `ofertas-web`
2. `vps_docker_start` em `landing`

(`infra/instalar-vps.sh` + `infra/docker-compose.yml` ficam como alternativa manual por terminal.)
