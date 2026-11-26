"""Reproduz as atividades do caderno completo (mesma semente e mesma ordem de gerar_completo.main)
e devolve {número da página: atividade}, com 'svg' e 'gabarito_svg' (área 182x228).
Não grava nada no gerador."""
import json
import pathlib
import random
import sys

sys.dont_write_bytecode = True
GER = pathlib.Path(__file__).resolve().parents[2] / "produto" / "gerador"
sys.path.insert(0, str(GER))
import gerar_completo as GC  # noqa: E402


def por_pagina():
    rng = random.Random(GC.SEMENTE)
    niveis = []
    for nv, fab in [(1, GC.nivel1), (2, GC.nivel2)]:
        cat = fab(rng)
        dias = GC.agenda(cat, rng)
        niveis.append([(fa(), fb()) for (ca, fa), (cb, fb) in dias])
    num, mapa = 4, {}
    for dias_at in niveis:
        num += 2
        for a, b in dias_at:
            for at in (a, b):
                mapa[num] = at
                num += 1
    return mapa


if __name__ == "__main__":
    m = por_pagina()
    resumo = json.loads((GER / "saida" / "completo.json").read_text())
    ok = 0
    for nv, dias in enumerate(resumo["niveis"], 1):
        for par in dias:
            for titulo, cat, tipo, pag in par:
                assert m[pag]["titulo"] == titulo, (pag, m[pag]["titulo"], titulo)
                ok += 1
    print(ok, "atividades conferidas com completo.json")
    for p in (7, 8, 11, 13, 15, 18, 68, 69, 75, 78):
        print(p, m[p]["titulo"], "| gabarito:", "svg" if m[p].get("gabarito_svg") else m[p].get("gabarito_txt", "")[:30])
