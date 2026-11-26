# Infraestrutura — publicação das páginas

- **Servidor:** VPS Hostinger KVM 2 (Ubuntu 24.04, IP 189.24.15.6).
- **Servidor web:** um único Caddy (`infra/docker-compose.yml`) com HTTPS automático, servindo:
  - as ofertas: `publicado/<slug>/index.html` → `https://ballestech.shop/<slug>/`
  - o site que já existia na VPS (landing do robô de promoções), sem mudança para quem acessa.
- **Publicar:** o Claude copia a página aprovada para `publicado/<slug>/` e faz push no ramo
  `main`. O contêiner `sync` baixa o repositório a cada 60 s; não precisa reiniciar nada.
- **DNS:** `ballestech.shop` e `www` com registro A → 189.24.15.6.

Uma URL por oferta no mesmo domínio (`/slug/`) evita criar DNS e certificado a cada oferta.
Se uma oferta precisar de domínio próprio, acrescente um bloco no `Caddyfile`.

## Instalação (uma vez só)

No hPanel: VPS → Terminal (navegador), como root:

```bash
curl -fsSL -o instalar.sh "<link raw do infra/instalar-vps.sh>"   # ou cole o conteúdo
bash instalar.sh     # parte 1: mostra a chave para cadastrar no GitHub (Deploy keys, só leitura)
bash instalar.sh     # parte 2: clona, sobe o Caddy + sincronizador e testa
```

Para voltar ao estado anterior: `docker compose -f /opt/ofertas-low-ticket/infra/docker-compose.yml down`
e `docker compose -f /opt/tutoriais/robo-promocoes/landing/docker-compose.yml start`.
