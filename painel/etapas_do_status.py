#!/usr/bin/env python3
"""Copia a tabela de etapas do status.md de cada oferta para painel/site/dados.json.

O painel (painel.ballestech.com.br) só enxerga painel/site/, então o checklist da
coluna "Etapas da oferta" vem de dados.json -> ofertas[i].etapas e .agora.
Cada oferta do dados.json precisa do campo "pasta" (ex.: "2026-11-26_atividades-foco").

Uso:  python3 painel/etapas_do_status.py
Não apaga nada do dados.json: só troca "etapas", "agora" e "etapas_em".
"""
import json, re, sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "painel" / "site" / "dados.json"
SITUACAO = {"✅": "feito", "🟡": "andamento", "⬜": "pendente", "❌": "bloqueado", "⛔": "bloqueado"}


def limpa(t, n=None):
    t = re.sub(r"\*\*|`", "", t).strip()
    if n and len(t) > n:
        t = t[: n - 1].rsplit(" ", 1)[0] + "…"
    return t


def ler_status(md):
    etapas, agora, em_decisoes = [], None, False
    for linha in md.read_text(encoding="utf-8").splitlines():
        if linha.startswith("## "):
            em_decisoes = "Decis" in linha
            continue
        if em_decisoes and linha.startswith("- "):
            agora = linha[2:]  # a última decisão registrada é o "agora"
            continue
        cel = [c.strip() for c in linha.strip().strip("|").split("|")]
        if len(cel) < 6 or cel[0] in ("#", "") or set(cel[0]) <= set("-: "):
            continue
        sit = next((v for k, v in SITUACAO.items() if k in cel[3]), "pendente")
        etapas.append({
            "id": cel[0],
            "nome": limpa(cel[1]),
            "responsavel": limpa(cel[2]),
            "situacao": sit,
            "data": cel[4] or None,
            "obs": limpa("|".join(cel[5:]), 220) or None,
            "portao": cel[0].upper().startswith("P"),
        })
    if agora:
        m = re.match(r"(\d{4}-\d{2}-\d{2})\s*(\([^)]*\))?\s*:?\s*(.*)", agora)
        agora = {"data": m.group(1), "texto": limpa((m.group(2) or "") + " " + m.group(3), 200)} if m else {"data": None, "texto": limpa(agora, 200)}
    return etapas, agora


def main():
    dados = json.loads(DADOS.read_text(encoding="utf-8"))
    for o in dados.get("ofertas", []):
        pasta = o.get("pasta")
        md = RAIZ / "ofertas" / pasta / "status.md" if pasta else None
        if not md or not md.exists():
            print(f"- {o.get('nome')}: sem status.md (campo 'pasta' = {pasta!r})", file=sys.stderr)
            continue
        o["etapas"], o["agora"] = ler_status(md)
        o["etapas_em"] = date.today().isoformat()
        feitas = sum(e["situacao"] == "feito" for e in o["etapas"])
        print(f"- {o['nome']}: {feitas} de {len(o['etapas'])} etapas feitas")
    DADOS.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
