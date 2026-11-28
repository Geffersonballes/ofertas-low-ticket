#!/usr/bin/env python3
"""R13 — Confere o que um pull request do minerador mexe, antes de o dono autorizar o merge.
Uso: python3 ferramentas/conferir_pr_minerador.py <ramo-ou-commit-do-PR> [base=origin/main]

O minerador só pode ADICIONAR: `mineracao/AAAA-MM-DD.md`, linhas em `mineracao/descartadas.md` e em
`aprendizados/padroes-externos.md` (sem apagar nada), `pesquisas/AAAA-MM-DD_*.md` novos e uma pasta NOVA
`ofertas/AAAA-MM-DD_<slug>/`. Qualquer outro arquivo (CLAUDE.md, agentes, skills, ferramentas, docs, painel,
infra, publicado/, aprendizados/, ofertas já existentes) é FORA DO ESCOPO e o dono decide item a item.
"""
import re, subprocess, sys

def git(*a): return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    head, base = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "origin/main")
    mb = git("merge-base", base, head).strip()
    linhas = [l.split("\t") for l in git("diff", "--name-status", mb, head).splitlines() if l]
    existentes = {p.split("/")[1] for p in git("ls-tree", "-r", "--name-only", base, "ofertas/").splitlines() if p.count("/") >= 2}
    ok, fora = [], []
    for st, *caminhos in linhas:
        p = caminhos[-1]
        novo_oferta = re.match(r"ofertas/(\d{4}-\d{2}-\d{2}_[a-z0-9-]+)/", p)
        so_acrescenta = False
        if st == "M":
            ad, rm = git("diff", "--numstat", mb, head, "--", p).split()[:2]
            so_acrescenta = rm == "0"
        permitido = (re.fullmatch(r"mineracao/\d{4}-\d{2}-\d{2}\.md", p) and st in ("A", "M")) \
            or (p in ("mineracao/descartadas.md", "aprendizados/padroes-externos.md") and st == "M" and so_acrescenta) \
            or (re.fullmatch(r"pesquisas/\d{4}-\d{2}-\d{2}_[\w-]+\.md", p) and st == "A") \
            or (novo_oferta and novo_oferta.group(1) not in existentes and st == "A")
        (ok if permitido else fora).append(f"{st}\t{p}")
    print(f"PR {head} contra {base}: {len(linhas)} arquivos")
    if fora:
        print("PR FORA DO ESCOPO — o dono precisa decidir estes itens antes do merge:")
        for f in fora: print("  -", f)
    else:
        print("PR DENTRO DO ESCOPO (só mineração e pasta de oferta nova)")
    for f in ok: print("  ok", f)
    sys.exit(1 if fora else 0)

if __name__ == "__main__":
    main()
