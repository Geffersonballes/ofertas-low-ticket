"""Monta o tutorial: para cada capítulo, mostra os passos na tela no momento em que a fala chega
neles (estimativa por posição no texto, ajustada para a pausa mais próxima detectada no áudio),
junta com a narração e concatena os capítulos. Saída: ../mineracao-marcos.mp4
Uso: python3 telas.py && node render.cjs && python3 montar.py"""
import pathlib
import re
import subprocess

from capitulos import CAPITULOS

AQUI = pathlib.Path(__file__).parent
TUT = AQUI.parent
NARR = TUT / "narracao"
QUAD = AQUI / "quadros"
TMP = AQUI / "tmp"
LEAD, TAIL = 0.5, 1.0  # silêncio antes da fala e tela parada depois

# trecho da narração em que cada passo (a partir do 2º) começa
ANCORAS = {
    1: ["com anúncio", "A gente não inventa", "O seu papel"],
    2: ["Segundo:", "Terceiro"],
    3: ["Algum anúncio", "Produto digital", "E oferta limpa", "Depois, o Claude"],
    4: ["Marque Mundo", "Busque em inglês", "Dica:"],
    5: ["Dois:", "Três:", "Quatro:", "Cinco:"],
    6: ["Aproveitamos", "Não copiamos", "E cortamos"],
    7: ["Nada de prova", "Nada de promessa", "E você não faz"],
    8: ["o dossiê", "a prova de que", "A meta"],
}


def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)]))


def pausas(p):
    """Fins de silêncio (início da próxima frase) em segundos."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(p), "-af", "silencedetect=noise=-35dB:d=0.18", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    ini = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]
    fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r)]
    return list(zip(ini, fim))


def tempos(c, d, ps):
    txt = c["narracao"]
    ts = [0.0]
    anc = ANCORAS[c["id"]]
    for a in anc:
        pos = txt.index(a)
        est = d * pos / len(txt)
        # pausa cujo meio está mais perto da estimativa; troca no começo da pausa (+0,1 s)
        cand = [(abs((s + e) / 2 - est), s) for s, e in ps if 0.5 < s < d - 0.5]
        t = min(cand)[1] + 0.1 if cand and min(cand)[0] < 2.5 else est
        ts.append(max(t, ts[-1] + 0.8))
    return ts


def main():
    TMP.mkdir(exist_ok=True)
    partes, capitulos_ini, t_acum = [], [], 0.0
    for c in CAPITULOS:
        n = len(c["passos"])
        assert len(ANCORAS[c["id"]]) == n - 1, c["id"]
        aud = NARR / f"cap{c['id']}.mp3"
        d = dur(aud)
        ts = [t + LEAD for t in tempos(c, d, pausas(aud))]
        total = LEAD + d + TAIL
        lista = TMP / f"c{c['id']}.txt"
        linhas = []
        for k in range(n):
            fim = ts[k + 1] if k + 1 < n else total
            ini = 0.0 if k == 0 else ts[k]
            linhas += [f"file '{(QUAD / f'c{c['id']}-{k}.png').as_posix()}'", f"duration {fim - ini:.3f}"]
        linhas.append(f"file '{(QUAD / f'c{c['id']}-{n - 1}.png').as_posix()}'")
        lista.write_text("\n".join(linhas) + "\n")
        out = TMP / f"c{c['id']}.mp4"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lista), "-i", str(aud),
                        "-filter_complex", f"[0:v]fps=30,format=yuv420p,fade=t=in:st=0:d=0.3[v];[1:a]adelay={int(LEAD*1000)}:all=1,apad=whole_dur={total:.3f},aresample=48000[a]",
                        "-map", "[v]", "-map", "[a]", "-t", f"{total:.3f}", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", str(out)], check=True)
        capitulos_ini.append((c["id"], c["titulo"], t_acum))
        t_acum += total
        partes.append(out)
        print(f"cap {c['id']}: {total:5.1f}s · trocas em", ", ".join(f"{t:.1f}" for t in ts[1:]))
    junta = TMP / "partes.txt"
    junta.write_text("".join(f"file '{p.as_posix()}'\n" for p in partes))
    bruto = TMP / "bruto.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(junta), "-c", "copy", str(bruto)], check=True)
    final = TUT / "mineracao-marcos.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(bruto), "-c:v", "copy",
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", str(final)], check=True)
    (TUT / "capitulos.txt").write_text("".join(f"{int(t // 60)}:{int(t % 60):02d} {i}. {tit}\n" for i, tit, t in capitulos_ini))
    print("ok", final, f"{dur(final):.1f}s")
    print((TUT / "capitulos.txt").read_text())


if __name__ == "__main__":
    main()
