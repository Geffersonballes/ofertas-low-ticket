#!/usr/bin/env bash
# Instalação única na VPS (rodar como root no Terminal da VPS no hPanel da Hostinger).
# Parte 1 gera a chave de leitura do GitHub; parte 2 (depois de cadastrar a chave) sobe tudo.
set -euo pipefail
REPO="git@github.com:Geffersonballes/ofertas-low-ticket.git"
RAMO="${RAMO:-main}"
CHAVE=/root/.ssh/deploy_ofertas

if [ ! -f "$CHAVE" ]; then
  mkdir -p /root/.ssh && ssh-keygen -t ed25519 -N "" -f "$CHAVE" -C "vps-ofertas-leitura" >/dev/null
  echo "== PARTE 1 =="
  echo "Cadastre a chave abaixo em GitHub → ofertas-low-ticket → Settings → Deploy keys → Add deploy key"
  echo "(título: VPS, NÃO marque 'Allow write access'). Depois rode este script de novo."
  echo; cat "$CHAVE.pub"; exit 0
fi

echo "== PARTE 2 =="
if [ ! -d /opt/ofertas-low-ticket/.git ]; then
  GIT_SSH_COMMAND="ssh -i $CHAVE -o StrictHostKeyChecking=accept-new" \
    git clone -q --branch "$RAMO" "$REPO" /opt/ofertas-low-ticket
fi
cd /opt/ofertas-low-ticket/infra
ACHADINHOS=$(sed -n 's/^DOMINIO=//p' /opt/tutoriais/robo-promocoes/landing/.env 2>/dev/null || true)
cat > .env <<ENV
DOMINIO_OFERTAS=ofertas.ballestech.com.br
DOMINIO_ACHADINHOS=${ACHADINHOS:-achadinhosdalay.ballestech.com.br}
RAMO=$RAMO
ENV
# libera as portas 80/443: o projeto "landing" para (não é apagado; o site dele passa a ser servido aqui)
docker compose -f /opt/tutoriais/robo-promocoes/landing/docker-compose.yml stop || true
docker compose up -d
sleep 5 && docker compose ps
echo "Pronto. Teste: https://${ACHADINHOS:-achadinhosdalay.ballestech.com.br} e https://ofertas.ballestech.com.br/"
