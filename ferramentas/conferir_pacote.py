"""Confere se um pacote de oferta está completo antes do pull request.
Uso: python3 ferramentas/conferir_pacote.py ofertas/AAAA-MM-DD_<slug>
Sai com código 1 e lista o que falta; código 0 = pacote pronto."""
import pathlib
import re
import sys

PROIBIDAS = ["tdah", "cérebro", "cerebro", "cura ", "garantido", "ganhe dinheiro", "emagre"]


def main(pasta):
    p = pathlib.Path(pasta)
    faltas = []
    for arq in ["status.md", "dossie.md", "briefing.md", "relatorio-pacote.md"]:
        if not (p / arq).exists():
            faltas.append(f"falta o arquivo {arq}")
    prints = list((p / "referencia").glob("*.png")) + list((p / "referencia").glob("*.jpg")) if (p / "referencia").exists() else []
    if len(prints) < 3:
        faltas.append(f"referencia/ tem {len(prints)} prints (mínimo 3)")
    if (p / "relatorio-pacote.md").exists():
        r = (p / "relatorio-pacote.md").read_text(encoding="utf-8")
        if "<nome da oferta>" in r:
            faltas.append("relatorio-pacote.md: título ainda com <nome da oferta>")
        nota = re.search(r"Nota da mineração:\*\*\s*(\d+)/30", r)
        if not nota:
            faltas.append("relatorio: nota da mineração não preenchida")
        elif int(nota.group(1)) < 22:
            faltas.append(f"relatorio: nota {nota.group(1)}/30 abaixo de 22")
        sec2 = r.split("## 2.")[1].split("## 3.")[0] if "## 2." in r else ""
        linhas = [l for l in sec2.splitlines() if l.startswith("| ") and not l.startswith("| Item") and "---" not in l]
        if any(l.split("|")[2].strip() == "" for l in linhas):
            faltas.append("relatorio seção 2: há número da Biblioteca sem valor")
        def linhas_tab(titulo):
            if titulo not in r:
                return []
            bloco = r.split(titulo)[1].split("\n### ")[0].split("\n## ")[0]
            return [l for l in bloco.splitlines() if l.startswith("|") and "---" not in l][1:]
        anunc = [l for l in linhas_tab("### 3.1") if l.replace("|", "").strip()]
        if len(anunc) < 3:
            faltas.append(f"relatorio 3.1: {len(anunc)} anunciantes/anúncios listados (mínimo 3)")
        usar = [l for l in linhas_tab("### 3.2") if len(l.split("|")) > 3 and l.split("|")[2].strip()]
        if len(usar) < 5:
            faltas.append(f"relatorio 3.2: {len(usar)} padrões a usar (precisa de 5)")
        if any(len(l.split("|")) > 4 and not l.split("|")[3].strip() for l in usar):
            faltas.append("relatorio 3.2: padrão sem evidência")
        evitar = [l for l in linhas_tab("### 3.3") if len(l.split("|")) > 3 and l.split("|")[2].strip()]
        if len(evitar) < 3:
            faltas.append(f"relatorio 3.3: {len(evitar)} padrões a evitar (precisa de 3)")
        if "R$ __" in r:
            faltas.append("relatorio seção 6: CPA máximo desta oferta não calculado")
        if "- [ ]" in r.split("## 7.")[-1]:
            faltas.append("relatorio seção 7: checklist com itens não marcados")
    if (p / "dossie.md").exists() and "Inteligência de anúncios" not in (p / "dossie.md").read_text(encoding="utf-8"):
        faltas.append("dossie.md sem a seção 'Inteligência de anúncios'")
    texto = " ".join(f.read_text(encoding="utf-8").lower() for f in p.glob("*.md") if f.name in ("briefing.md",))
    for w in PROIBIDAS:
        if w in texto:
            faltas.append(f"briefing.md contém termo proibido: '{w.strip()}' (revise a promessa)")
    if faltas:
        print("PACOTE INCOMPLETO:")
        for f in faltas:
            print(" -", f)
        return 1
    print("PACOTE OK: pode abrir o pull request.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]) if len(sys.argv) > 1 else print(__doc__) or 2)
