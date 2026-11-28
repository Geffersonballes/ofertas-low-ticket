#!/usr/bin/env python3
"""R14 — Toda mudança em arquivo de processo precisa de uma entrada nova em docs/mural-de-mudancas.md.
Uso: python3 ferramentas/conferir_mural.py [base=origin/main] [head=HEAD]
"""
import subprocess, sys

PROCESSO = ("CLAUDE.md", "docs/02_esteira.md", "docs/07_divisao-do-trabalho.md", "docs/08_inteligencia-de-anuncios.md",
            "docs/09_processos.md", ".claude/agents/", ".claude/skills/", "ferramentas/")
MURAL = "docs/mural-de-mudancas.md"

def git(*a): return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout

base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
head = sys.argv[2] if len(sys.argv) > 2 else "HEAD"
mb = git("merge-base", base, head).strip()
mudou = [p for p in git("diff", "--name-only", mb, head).splitlines() if p.startswith(PROCESSO)]
if not mudou:
    print("MURAL OK (nenhum arquivo de processo mudou)"); sys.exit(0)
add = [l for l in git("diff", "-U0", mb, head, "--", MURAL).splitlines() if l.startswith("+## ")]
if add:
    print(f"MURAL OK ({len(mudou)} arquivo(s) de processo; entrada nova: {add[-1][4:]})"); sys.exit(0)
print("MURAL DESATUALIZADO — estes arquivos de processo mudaram sem entrada nova no mural:")
for p in mudou: print("  -", p)
sys.exit(1)
