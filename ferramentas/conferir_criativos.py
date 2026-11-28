#!/usr/bin/env python3
"""Portão C (Criativos): só depois do Portão M. Confere se os criativos da oferta (vídeos e imagens de
anúncio) foram revisados e aprovados pelo dono e se os arquivos são exatamente os aprovados.
Uso: python3 ferramentas/conferir_criativos.py ofertas/<pasta>

Sem "CRIATIVOS APROVADOS" não se sobe criativo para a Meta nem se cria/atualiza anúncio.
"""
import hashlib, pathlib, re, subprocess, sys

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def arquivos(pasta):
    c = pasta / "criativos"
    return sorted([*c.glob("videos/*.mp4"), *c.glob("estatico/*.jpg"), *c.glob("estatico/*.png")])

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    pasta = pathlib.Path(sys.argv[1]).resolve()
    prob = []
    m = subprocess.run([sys.executable, str(pathlib.Path(__file__).with_name("conferir_material.py")), str(pasta)],
                       capture_output=True, text=True)
    if m.returncode != 0:
        prob.append("o MATERIAL ainda não foi aprovado (Portão M vem antes do Portão C)")
    arqs = arquivos(pasta)
    if not arqs: prob.append("nenhum criativo em criativos/videos/*.mp4 ou criativos/estatico/")
    aprov = sorted(pasta.glob("revisoes/criativos-*/APROVACAO.md"))
    if not aprov:
        prob.append("falta revisoes/criativos-AAAA-MM-DD/APROVACAO.md (rode a skill revisar-criativos e peça a aprovação do dono)")
    else:
        a = aprov[-1]; t = a.read_text(encoding="utf-8")
        for campo, msg in [(r"^aprovado_por:\s*\S+", "aprovado_por:"), (r"^data:\s*\d{4}-\d{2}-\d{2}", "data: AAAA-MM-DD"),
                           (r"^pendencias:\s*0\s*$", "pendencias: 0"),
                           (r"^revisao_final_limpa:\s*\d{4}-\d{2}-\d{2}", "revisao_final_limpa: AAAA-MM-DD"),
                           (r"^material_aprovado_em:\s*\S+", "material_aprovado_em: <APROVACAO.md do material>")]:
            if not re.search(campo, t, re.M): prob.append(f"{a.name}: falta '{msg}'")
        aprovados = {nome: h for h, nome in re.findall(r"^([0-9a-f]{64})\s+(\S+)$", t, re.M)}
        for p in arqs:
            rel = str(p.relative_to(pasta))
            if rel not in aprovados: prob.append(f"{rel}: não estava na aprovação (criativo novo → revisar)")
            elif aprovados[rel] != sha(p): prob.append(f"{rel}: mudou depois da aprovação → revisar de novo")
    if prob:
        print("CRIATIVOS NÃO APROVADOS"); [print(" -", x) for x in prob]; sys.exit(1)
    print(f"CRIATIVOS APROVADOS ({len(arqs)} arquivos conferem com {aprov[-1].relative_to(pasta)})")

if __name__ == "__main__":
    main()
