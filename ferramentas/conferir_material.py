#!/usr/bin/env python3
"""Portão do Material: confere se o infoproduto da oferta foi revisado e aprovado pelo dono
e se os PDFs são exatamente os aprovados. Uso: python3 ferramentas/conferir_material.py ofertas/<pasta>

Sem "MATERIAL APROVADO" não se sobe arquivo na Hotmart, não se cria criativo nem campanha.
Qualquer PDF alterado depois da aprovação (hash diferente) exige nova revisão e nova aprovação.
"""
import hashlib, pathlib, re, sys

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def pdfs(pasta):
    return sorted([*pasta.glob("produto/final/*.pdf"), *pasta.glob("produto/bumps/*/*.pdf")])

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    pasta = pathlib.Path(sys.argv[1]).resolve()
    prob = []
    arqs = pdfs(pasta)
    if not arqs: prob.append("nenhum PDF em produto/final/ ou produto/bumps/*/")
    aprov = sorted(pasta.glob("revisoes/material-*/APROVACAO.md"))
    if not aprov:
        prob.append("falta revisoes/material-AAAA-MM-DD/APROVACAO.md (rode a skill revisar-material e peça a aprovação do dono)")
    else:
        a = aprov[-1]; t = a.read_text(encoding="utf-8")
        if not re.search(r"^aprovado_por:\s*\S+", t, re.M): prob.append(f"{a.name}: falta 'aprovado_por:'")
        if not re.search(r"^data:\s*\d{4}-\d{2}-\d{2}", t, re.M): prob.append(f"{a.name}: falta 'data: AAAA-MM-DD'")
        if not re.search(r"^pendencias_bloqueia_atrapalha:\s*0\s*$", t, re.M):
            prob.append(f"{a.name}: 'pendencias_bloqueia_atrapalha: 0' ausente (há erro que bloqueia/atrapalha em aberto?)")
        aprovados = {nome: h for h, nome in re.findall(r"^([0-9a-f]{64})\s+(\S+)$", t, re.M)}
        for p in arqs:
            rel = str(p.relative_to(pasta))
            if rel not in aprovados: prob.append(f"{rel}: não estava na aprovação (arquivo novo → revisar)")
            elif aprovados[rel] != sha(p): prob.append(f"{rel}: mudou depois da aprovação → revisar de novo")
    if prob:
        print("MATERIAL NÃO APROVADO"); [print(" -", x) for x in prob]; sys.exit(1)
    print(f"MATERIAL APROVADO ({len(arqs)} PDFs conferem com {aprov[-1].relative_to(pasta)})")

if __name__ == "__main__":
    main()
