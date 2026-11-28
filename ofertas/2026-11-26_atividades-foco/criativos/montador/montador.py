"""Monta os vídeos dos anúncios do Dez Minutinhos (9:16, 1080x1920, 30 fps) a partir de mídias REAIS:
atividades reais do caderno (SVG do gerador, com o gabarito animado), páginas do PDF, mockups e o vídeo
"folheando". A narração (ElevenLabs, já gerada) dita o tempo: as pausas da fala ancoram cenas e legendas.

Uso:
  node paginas2x.cjs 5 6 7 8 78 128 142 143        # uma vez: páginas em 2x → cache/
  ffmpeg -i ../../pagina/img/folheando.mp4 -vf fps=30 -q:v 3 cache/folheando/%04d.jpg   # uma vez
  python3 montador.py                 # os 8 vídeos
  python3 montador.py 2 amandinha     # só um
Saída: ../videos/anuncio-<n>-<voz>.mp4
"""
import html as H
import json
import math
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True
AQUI = pathlib.Path(__file__).resolve().parent
OFERTA = AQUI.parents[1]
IMG = OFERTA / "pagina" / "img"
FONTES = OFERTA / "pagina" / "fontes"
CACHE = AQUI / "cache"
TMP = AQUI / "tmp"
AUDIO = OFERTA / "criativos" / "audio"
VIDEOS = OFERTA / "criativos" / "videos"
FPS = 30
FECHO = 1.0  # segundos de cartão final depois da fala

sys.path.insert(0, str(AQUI))
from atividades_reais import por_pagina  # noqa: E402

ATV = por_pagina()


# ------------------------------------------------------------------ roteiros (texto = narração exata)
def F(texto, legenda, cena=None):
    return {"texto": texto, "legenda": legenda, "cena": cena}


FINAL = {"tipo": "final"}
ROTEIROS = {
    1: [
        F("Isto é o que cabe em dez minutinhos de papel e lápis.", "Isto é o que cabe em 10 minutinhos de papel e lápis.",
          {"tipo": "atividade", "pag": 7, "titulo": "Isto cabe em 10 minutinhos"}),
        F("Um labirinto.", "Um labirinto.", {"tipo": "atividade", "pag": 75, "titulo": "Labirinto"}),
        F("Um jogo de memória.", "Um jogo de memória.", {"tipo": "atividade", "pag": 11, "titulo": "Memória"}),
        F("Um sudoku.", "Um sudoku.", {"tipo": "atividade", "pag": 18, "titulo": "Sudoku"}),
        F("Um código secreto.", "Um código secreto.", {"tipo": "atividade", "pag": 78, "titulo": "Código secreto"}),
        F("Cento e vinte atividades prontas para imprimir, de quatro a dez anos.",
          "120 atividades prontas para imprimir, de 4 a 10 anos.",
          {"tipo": "folheando", "titulo": "120 atividades · 4 a 10 anos"}),
        F("O plano de trinta dias já diz as duas folhas de cada dia.", "O plano de 30 dias já diz as 2 folhas de cada dia.",
          {"tipo": "partes", "titulo": "Plano de 30 dias · 2 folhas por dia", "partes": [
              {"tipo": "pagina", "pag": 5, "zoom": [1.0, 1.9], "foco": [50, 17]},
              {"tipo": "duas", "pags": [6, 7], "rotulos": ["Dia 1 · folha 1", "Dia 1 · folha 2"]}]}),
        F("Dez Minutinhos, trinta e sete reais.", "Dez Minutinhos, R$ 37,00.", FINAL),
        F("Toque em saiba mais.", "Toque em Saiba mais."),
    ],
    2: [
        F("Imprimiu, entregou, pronto.", "Imprimiu, entregou, pronto.",
          {"tipo": "carimbo", "pag": 6, "titulo": "Imprimiu. Entregou. Pronto."}),
        F("Zero preparo.", "Zero preparo."),
        F("O plano já diz as duas folhas de cada dia.", "O plano já diz as 2 folhas de cada dia.",
          {"tipo": "partes", "titulo": "O plano já separou as folhas", "partes": [
              {"tipo": "pagina", "pag": 5, "zoom": [1.0, 1.9], "foco": [50, 17]},
              {"tipo": "duas", "pags": [6, 7], "rotulos": ["Dia 1 · folha 1", "Dia 1 · folha 2"]}]}),
        F("Abre, imprime, entrega com um lápis.", "Abre, imprime, entrega com um lápis.",
          {"tipo": "imagem", "src": "mockup-pacote.png", "lapis": True, "titulo": "Abre · imprime · entrega"}),
        F("As respostas estão no gabarito.", "As respostas estão no gabarito.",
          {"tipo": "pagina", "pag": 128, "zoom": [1.0, 1.8], "foco": [22, 28], "titulo": "Gabarito no fim"}),
        F("Cento e vinte atividades por trinta e sete reais.", "120 atividades por R$ 37,00.",
          {"tipo": "numeros", "linhas": ["120 atividades", "R$ 37,00"], "titulo": "Uma vez só"}),
        F("Um real e vinte e três por dia, no plano de trinta dias.", "R$ 1,23 por dia, no plano de 30 dias.",
          {"tipo": "numeros", "linhas": ["R$ 1,23", "por dia no plano de 30 dias"], "titulo": "Faça a conta"}),
        F("E imprime de novo quando quiser.", "E imprime de novo quando quiser.",
          {"tipo": "folheando", "titulo": "Imprime de novo quando quiser"}),
        F("Toque em saiba mais.", "Toque em Saiba mais.", FINAL),
    ],
    3: [
        F("App educativo continua sendo tela.", "App educativo continua sendo tela.",
          {"tipo": "risco", "antes": "App", "riscado": "educativo", "depois": "= tela"}),
        F("Vídeo de desenho também.", "Vídeo de desenho também.",
          {"tipo": "texto", "escuro": True, "linhas": ["Vídeo de desenho", "também."]}),
        F("Quer o mesmo tipo de desafio, só que no papel?", "Quer o mesmo tipo de desafio, só que no papel?",
          {"tipo": "atividade", "pag": 75, "revelar": False, "entrada": "baixo", "titulo": "O mesmo desafio. No papel."}),
        F("Labirinto, sudoku, sequência, jogo dos sete erros.", "Labirinto, sudoku, sequência, jogo dos 7 erros.",
          {"tipo": "partes", "partes": [
              {"tipo": "atividade", "pag": 75, "titulo": "Labirinto"},
              {"tipo": "atividade", "pag": 69, "titulo": "Sudoku"},
              {"tipo": "atividade", "pag": 8, "titulo": "Sequência"},
              {"tipo": "atividade", "pag": 68, "titulo": "7 erros"}]}),
        F("Dois níveis: de quatro a seis anos, sem precisar ler, e de sete a dez.",
          "2 níveis: de 4 a 6 anos, sem precisar ler, e de 7 a 10.",
          {"tipo": "duas", "pags": [6, 78], "rotulos": ["Nível 1 · 4 a 6 anos · sem leitura", "Nível 2 · 7 a 10 anos"],
           "titulo": "Dois níveis"}),
        F("Dez Minutinhos: cento e vinte atividades para imprimir.", "Dez Minutinhos: 120 atividades para imprimir.", FINAL),
        F("Toque em saiba mais.", "Toque em Saiba mais."),
    ],
    4: [
        F("Troque dez minutos de tela por dez minutos disto.", "Troque 10 minutos de tela por 10 minutos disto.",
          {"tipo": "partes", "partes": [
              {"tipo": "texto", "escuro": True, "linhas": ["10 min", "de tela"]},
              {"tipo": "atividade", "pag": 8, "revelar": False, "titulo": "10 min disto"}]}),
        F("Padrões para completar.", "Padrões para completar.", {"tipo": "atividade", "pag": 8, "titulo": "Padrões"}),
        F("Memória: olha, dobra a folha e responde.", "Memória: olha, dobra a folha e responde.",
          {"tipo": "atividade", "pag": 11, "zoom": [1.55, 1.0], "foco": [50, 30], "titulo": "Memória"}),
        F("Lógica, com labirinto e sudoku.", "Lógica, com labirinto e sudoku.",
          {"tipo": "partes", "titulo": "Lógica", "partes": [
              {"tipo": "atividade", "pag": 13}, {"tipo": "atividade", "pag": 18}]}),
        F("Ligue os pontos.", "Ligue os pontos.", {"tipo": "atividade", "pag": 15, "titulo": "Traçado"}),
        F("Não precisa saber ensinar nem montar rotina.", "Não precisa saber ensinar nem montar rotina.",
          {"tipo": "folheando", "titulo": "Sem saber ensinar · sem montar rotina"}),
        F("O plano de trinta dias já vem pronto, com quadro de conquistas.",
          "O plano de 30 dias já vem pronto, com quadro de conquistas.",
          {"tipo": "partes", "titulo": "Plano pronto · quadro de conquistas", "partes": [
              {"tipo": "pagina", "pag": 5, "zoom": [1.0, 1.3], "foco": [50, 20]},
              {"tipo": "pagina", "pag": 142, "zoom": [1.0, 1.12], "foco": [50, 40]},
              {"tipo": "pagina", "pag": 143, "zoom": [1.0, 1.12], "foco": [50, 30]}]}),
        F("Dez Minutinhos.", "Dez Minutinhos.", FINAL),
        F("Toque em saiba mais.", "Toque em Saiba mais."),
    ],
}


# ------------------------------------------------------------------ áudio: pausas e alinhamento
def duracao(arq):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(arq)],
                         capture_output=True, text=True, check=True).stdout
    return float(out)


def silencios(arq, dur, db=-38):
    log = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(arq), "-af",
                          f"silencedetect=noise={db}dB:d=0.15", "-f", "null", "-"], capture_output=True, text=True).stderr
    ini = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
    fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
    if len(fim) < len(ini):
        fim.append(dur)
    return list(zip(ini, fim))


def alinhar(arq, frases):
    """Devolve (dur, [(início, fim)] por frase, âncoras). As fronteiras entre frases caem no meio das pausas da
    fala, escolhidas por programação dinâmica perto do ponto esperado pela proporção de caracteres. Testa três
    limites de silêncio (vozes clonadas têm ruído de fundo nas pausas) e fica com o que ancora mais fronteiras."""
    dur = duracao(arq)
    melhor = None
    for db in (-38, -34, -30, -28):
        r = _alinhar(dur, silencios(arq, dur, db), frases)
        chave = sum(r[2])  # do mais rigoroso ao mais solto: só troca se ancorar MAIS fronteiras
        if melhor is None or chave > melhor[0]:
            melhor = (chave, r)
    front_ok = melhor[1]
    return dur, front_ok[1], front_ok[2]


def _alinhar(dur, sil, frases):
    vs = sil[0][1] if sil and sil[0][0] < 0.05 else 0.0
    ve = sil[-1][0] if sil and sil[-1][1] >= dur - 0.05 else dur
    meios = [(a + b) / 2 for a, b in sil if a > vs + 0.05 and b < ve - 0.05]
    pesos = [len(f) + 8 for f in frases]
    tot = sum(pesos)
    ideal = [vs + (ve - vs) * sum(pesos[:k + 1]) / tot for k in range(len(frases) - 1)]
    B, M, PEN = len(ideal), len(meios), 1.6
    INF = float("inf")
    # dp[m+1] = (custo, escolhas) com o último meio usado = m (−1 = nenhum)
    dp = {-1: (0.0, [])}
    for b in range(B):
        novo = {}
        for m, (c, esc) in dp.items():
            cand = [(c + PEN, m, esc + [None])]
            for j in range(m + 1, M):
                cand.append((c + abs(meios[j] - ideal[b]), j, esc + [j]))
            for cc, mm, ee in cand:
                if cc < novo.get(mm, (INF,))[0]:
                    novo[mm] = (cc, ee)
        dp = novo
    _, esc = min(dp.values(), key=lambda x: x[0])
    front = []
    for b, j in enumerate(esc):
        t = meios[j] if j is not None else ideal[b]
        front.append(max(t, front[-1] + 0.3) if front else t)
    inicios = [vs] + front
    fins = front + [ve]
    custo = min(dp.values(), key=lambda x: x[0])[0]
    return dur, list(zip(inicios, fins)), [j is not None for j in esc], custo


def blocos_legenda(texto, t0, t1, maxp=6):
    pal = texto.split()
    n = max(1, math.ceil(len(pal) / maxp))
    tam = math.ceil(len(pal) / n)
    grupos = [" ".join(pal[i:i + tam]) for i in range(0, len(pal), tam)]
    pesos = [len(g) + 2 for g in grupos]
    tot, t, out = sum(pesos), t0, []
    for g, w in zip(grupos, pesos):
        d = (t1 - t0) * w / tot
        out.append({"t0": round(t, 3), "t1": round(t + d, 3), "txt": g})
        t += d
    return out


# ------------------------------------------------------------------ HTML das cenas
NIVEL = {1: "Nível 1 · 4 a 6 anos", 2: "Nível 2 · 7 a 10 anos"}


def svg_atividade(pag):
    at = ATV[pag]
    base = at["svg"]
    gab = at.get("gabarito_svg") or ""
    # polyline (aberto) ou polygon (ligue os pontos fechado: o traço volta ao 1 desde 2026-11-28)
    traços = re.findall(r'<(polyline|polygon) points="([^"]+)"([^>]*?)/>', gab)
    traços = [(t, p, r) for t, p, r in traços if "#ff7a45" in r]
    if traços:
        ov = "".join(f'<path class="traco" d="M{" L".join(p.split())}{" Z" if t == "polygon" else ""}" pathLength="1" stroke-dasharray="1" '
                     f'stroke-dashoffset="1"{r}/>' for t, p, r in traços)
        modo = "traco"
    else:
        ov, modo = gab, ("fade" if gab else "nada")
    return at, base, ov, modo


def card_atividade(pag):
    at, base, ov, modo = svg_atividade(pag)
    return (f'<div class="card ativ" data-modo="{modo}"><div class="ctopo"><span class="marca">Dez <b>Minutinhos</b></span>'
            f'<span class="selo n{at["nivel"]}">{NIVEL[at["nivel"]]}</span></div>'
            f'<div class="ctit">{H.escape(at["titulo"])}</div><div class="cins">{H.escape(at["instrucao"])}</div>'
            f'<div class="sv"><svg viewBox="0 0 182 228">{base}</svg><svg class="ov" viewBox="0 0 182 228">{ov}</svg></div></div>')


def pag_url(n):
    return (CACHE / f"pag-{n:03d}.png").as_uri()


LAPIS = ('<svg class="lapis" viewBox="0 0 360 30"><polygon points="0,15 34,3 34,27" fill="#f4d3a8"/>'
         '<polygon points="0,15 12,11 12,19" fill="#333"/><rect x="34" y="3" width="270" height="24" fill="#ff7a45"/>'
         '<rect x="34" y="3" width="270" height="8" fill="#ff9468"/><rect x="304" y="3" width="26" height="24" fill="#c9c9c9"/>'
         '<rect x="330" y="3" width="30" height="24" rx="5" fill="#f29bb0"/></svg>')


def html_cena(c):
    t = c["tipo"]
    if t == "atividade":
        return card_atividade(c["pag"])
    if t == "pagina":
        return f'<div class="card pag"><img src="{pag_url(c["pag"])}" alt=""></div>'
    if t == "duas":
        return "".join(f'<div class="mini m{i}"><img src="{pag_url(p)}" alt=""><span>{H.escape(r)}</span></div>'
                       for i, (p, r) in enumerate(zip(c["pags"], c["rotulos"])))
    if t == "carimbo":
        return f'<div class="card pag sobe"><img src="{pag_url(c["pag"])}" alt=""></div><div class="carimbo">PRONTO</div>'
    if t == "imagem":
        return f'<img class="foto" src="{(IMG / c["src"]).as_uri()}" alt="">' + (LAPIS if c.get("lapis") else "")
    if t == "numeros":
        return (f'<img class="fundo-mock" src="{(IMG / "mockup-capa.png").as_uri()}" alt="">'
                + "".join(f'<div class="num l{i}">{H.escape(l)}</div>' for i, l in enumerate(c["linhas"])))
    if t == "texto":
        return "".join(f'<div class="tx l{i}">{H.escape(l)}</div>' for i, l in enumerate(c["linhas"]))
    if t == "risco":
        return (f'<div class="rs"><span>{H.escape(c["antes"])} </span><span class="riscado">{H.escape(c["riscado"])}'
                f'<i class="linha"></i></span></div><div class="rs2">{H.escape(c["depois"])}</div>')
    if t == "folheando":
        return '<canvas class="folh" width="720" height="551"></canvas>'
    if t == "final":
        return (f'<img class="fmock" src="{(IMG / "mockup-capa.png").as_uri()}" alt=""><div class="fnome">Dez Minutinhos</div>'
                '<div class="fsub">120 atividades para imprimir · 4 a 10 anos</div><div class="fpreco">R$ 37,00</div>'
                '<div class="fbot">Toque em Saiba mais</div>')
    raise ValueError(t)


CSS = """
@font-face{font-family:'Baloo 2';font-weight:400 800;src:url('%(f)s/Baloo2.woff2') format('woff2')}
@font-face{font-family:'Nunito';font-weight:200 1000;src:url('%(f)s/Nunito.woff2') format('woff2')}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:540px;height:960px;overflow:hidden;background:#fff7f1;font-family:'Nunito',sans-serif;color:#1d1d1f}
.cena{position:absolute;inset:0;display:none}
.cena.cheia{z-index:1}.cena.palco{z-index:2}
.escuro{background:#1d1d1f}.laranja{background:#ff7a45}
#titulo{position:absolute;left:24px;right:24px;top:118px;z-index:5;text-align:center;display:none}
#titulo span{display:inline-block;background:#fff;border:2.5px solid #1d1d1f;border-radius:16px;padding:6px 16px 4px;
  font-family:'Baloo 2';font-weight:800;font-size:27px;line-height:1.1;box-shadow:4px 4px 0 #ff7a45}
#legenda{position:absolute;left:22px;right:22px;top:712px;height:100px;z-index:6;display:flex;align-items:flex-start;justify-content:center}
#legenda span{background:rgba(29,29,31,.9);color:#fff;font-family:'Baloo 2';font-weight:700;font-size:27px;line-height:1.18;
  padding:7px 14px 5px;border-radius:12px;text-align:center;max-width:496px}
/* palco: área entre o título e a legenda (y 190–700) */
.palco .card{position:absolute;left:50%;top:445px;width:372px;margin-left:-186px;transform-origin:50% 50%}
.card{background:#fff;border-radius:14px;box-shadow:0 2px 4px rgba(0,0,0,.08),0 18px 40px rgba(80,40,10,.22);overflow:hidden}
.card.ativ{padding:12px 14px 10px;margin-top:-250px}
.ctopo{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #1d1d1f;padding-bottom:5px}
.marca{font-family:'Baloo 2';font-weight:800;font-size:12px}.marca b{color:#ff7a45}
.selo{font-weight:800;font-size:9.5px;border:1.5px solid #1d1d1f;border-radius:20px;padding:1px 8px}
.selo.n1{background:#fff1e8}.selo.n2{background:#e8f0ff}
.ctit{font-family:'Baloo 2';font-weight:800;font-size:23px;line-height:1.05;margin-top:6px}
.cins{font-size:10.5px;font-weight:700;color:#444;margin-top:2px;min-height:26px}
.sv{position:relative;width:344px;height:388px;margin-top:4px}
.sv svg{position:absolute;inset:0;width:100%%;height:100%%}
.card.pag{width:352px;margin-left:-176px;margin-top:-249px}
.card.pag img{display:block;width:352px;height:auto}
.mini{position:absolute;top:212px;width:228px}
.mini.m0{left:30px}.mini.m1{left:282px}
.mini img{display:block;width:228px;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,.08),0 14px 30px rgba(80,40,10,.2);background:#fff}
.mini span{display:block;text-align:center;font-family:'Baloo 2';font-weight:800;font-size:16px;margin-top:8px;line-height:1.1}
.carimbo{position:absolute;left:50%%;top:430px;transform:translate(-50%%,-50%%) rotate(-12deg);font-family:'Baloo 2';font-weight:800;
  font-size:64px;color:#e8481a;border:6px solid #e8481a;border-radius:14px;padding:4px 22px 0;background:rgba(255,255,255,.85);opacity:0}
.foto{position:absolute;left:30px;width:480px;top:215px}
.lapis{position:absolute;width:300px;left:150px;top:600px;transform:rotate(-14deg)}
.fundo-mock{position:absolute;width:300px;left:120px;top:205px;opacity:.95}
.num{position:absolute;left:20px;right:20px;text-align:center;font-family:'Baloo 2';font-weight:800;color:#1d1d1f;opacity:0}
.num.l0{top:470px;font-size:58px;line-height:1}.num.l1{top:540px;font-size:44px;line-height:1.05;color:#d9481a}
.tx{position:absolute;left:20px;right:20px;text-align:center;font-family:'Baloo 2';font-weight:800;color:#fff;opacity:0}
.tx.l0{top:330px;font-size:54px;line-height:1;white-space:nowrap}.tx.l1{top:400px;font-size:54px;line-height:1;color:#ff7a45;white-space:nowrap}
.rs{position:absolute;left:0;right:0;top:330px;text-align:center;font-family:'Baloo 2';font-weight:800;font-size:66px;color:#fff;line-height:1}
.riscado{position:relative;display:inline-block}
.linha{position:absolute;left:-4px;top:52%%;height:9px;background:#ff7a45;border-radius:5px;width:0}
.rs2{position:absolute;left:0;right:0;top:420px;text-align:center;font-family:'Baloo 2';font-weight:800;font-size:76px;color:#ff7a45;opacity:0}
.folh{position:absolute;left:20px;top:265px;width:500px;height:383px;border-radius:16px;box-shadow:0 18px 40px rgba(80,40,10,.22)}
.fmock{position:absolute;width:330px;left:105px;top:150px}
.fnome{position:absolute;left:0;right:0;top:438px;text-align:center;font-family:'Baloo 2';font-weight:800;font-size:54px;line-height:1}
.fsub{position:absolute;left:0;right:0;top:496px;text-align:center;font-weight:800;font-size:17px}
.fpreco{position:absolute;left:50%%;top:528px;transform:translateX(-50%%);background:#fff;border:3px solid #1d1d1f;border-radius:14px;
  font-family:'Baloo 2';font-weight:800;font-size:40px;padding:4px 18px 0;box-shadow:4px 4px 0 #1d1d1f}
.fbot{position:absolute;left:50%%;top:616px;background:#1d1d1f;color:#fff;font-family:'Baloo 2';font-weight:800;font-size:24px;
  padding:9px 22px 6px;border-radius:14px;white-space:nowrap}
"""

JS = r"""
const CENAS = __CENAS__, LEG = __LEG__, NFOLH = __NFOLH__;
const ease = x => x <= 0 ? 0 : x >= 1 ? 1 : 1 - Math.pow(1 - x, 3);
const cl = x => Math.max(0, Math.min(1, x));
const lerp = (a, b, x) => a + (b - a) * x;
const folh = [];
const espera = [document.fonts.ready];
for (const img of document.images) espera.push(img.decode().catch(() => { throw new Error('img ' + img.src); }));
if (NFOLH) for (let i = 1; i <= NFOLH; i++) { const im = new Image(); im.src = '__FOLH__/' + String(i).padStart(4, '0') + '.jpg'; folh.push(im); espera.push(im.decode()); }
window.pronto = Promise.all(espera);
const tituloEl = document.querySelector('#titulo'), tituloSp = tituloEl.querySelector('span');
const legEl = document.querySelector('#legenda'), legSp = legEl.querySelector('span');
function entra(el, dt, dy = 36) { const e = ease(dt / 0.3); el.style.opacity = e; return e; }
const A = {
  atividade(el, c, p, dt) {
    const card = el.querySelector('.card'), e = ease(dt / 0.3);
    const z0 = c.zoom ? c.zoom[0] : 1, z1 = c.zoom ? c.zoom[1] : 1.06;
    const z = lerp(z0, z1, ease(p));
    const dy = c.entrada === 'baixo' ? (1 - ease(dt / 0.5)) * 520 : (1 - e) * 30;
    card.style.transformOrigin = c.foco ? `${c.foco[0]}% ${c.foco[1]}%` : '50% 50%';
    card.style.transform = `translateY(${dy}px) scale(${(0.95 + 0.05 * e) * z})`;
    card.style.opacity = 1;
    if (c.revelar === false) { const o = card.querySelector('.ov'); if (o) o.style.opacity = 0; return; }
    const q = ease(cl((p - 0.12) / 0.7)), modo = card.dataset.modo;
    if (modo === 'traco') card.querySelectorAll('.traco').forEach(t => t.setAttribute('stroke-dashoffset', 1 - q));
    else if (modo === 'fade') card.querySelector('.ov').style.opacity = q;
  },
  pagina(el, c, p, dt) {
    const card = el.querySelector('.card'), e = ease(dt / 0.3);
    const z = lerp(c.zoom[0], c.zoom[1], ease(cl(p * 1.15)));
    card.style.transformOrigin = `${c.foco[0]}% ${c.foco[1]}%`;
    card.style.transform = `translateY(${(1 - e) * 30}px) scale(${(0.95 + 0.05 * e) * z})`;
    card.style.opacity = 1;
  },
  duas(el, c, p, dt) {
    el.querySelectorAll('.mini').forEach((m, i) => { const e = ease((dt - i * 0.1) / 0.2);
      m.style.opacity = i ? cl((dt - 0.1) / 0.07) : 1; m.style.transform = `translateY(${(1 - e) * 60}px) rotate(${i ? 2 : -2}deg)`; });
  },
  carimbo(el, c, p, dt) {
    const card = el.querySelector('.card'), s = el.querySelector('.carimbo');
    const u = ease(cl(p / 0.42));
    card.style.transform = `translateY(${(1 - u) * 760}px)`;
    const k = cl((p - 0.52) / 0.1);
    s.style.opacity = k; s.style.transform = `translate(-50%,-50%) rotate(-12deg) scale(${2.2 - 1.2 * ease(k)})`;
  },
  imagem(el, c, p, dt) {
    const f = el.querySelector('.foto'), e = ease(dt / 0.3);
    f.style.opacity = 1; f.style.transform = `scale(${1 + 0.06 * p}) translateY(${(1 - e) * 30}px)`;
    const l = el.querySelector('.lapis');
    if (l) { const u = ease(cl((p - 0.15) / 0.4)); l.style.transform = `translateX(${(1 - u) * 420}px) rotate(-14deg)`; }
  },
  numeros(el, c, p, dt) {
    const m = el.querySelector('.fundo-mock'); m.style.opacity = 1;
    m.style.transform = `translateY(${Math.sin(dt * 2) * 5}px) scale(${1 + 0.04 * p})`;
    el.querySelectorAll('.num').forEach((n, i) => { const k = ease(cl((p - 0.05 - i * 0.3) / 0.15));
      n.style.opacity = k; n.style.transform = `scale(${0.6 + 0.4 * k})`; });
  },
  texto(el, c, p, dt) {
    el.querySelectorAll('.tx').forEach((n, i) => { const k = ease(cl((dt - i * 0.35) / 0.3));
      n.style.opacity = k; n.style.transform = `translateY(${(1 - k) * 40}px)`; });
  },
  risco(el, c, p, dt) {
    const rs = el.querySelector('.rs'); rs.style.opacity = ease(dt / 0.25);
    const ln = el.querySelector('.linha'), w = el.querySelector('.riscado').offsetWidth + 8;
    ln.style.width = (w * ease(cl((p - 0.22) / 0.25))) + 'px';
    const k = ease(cl((p - 0.5) / 0.15)); const r2 = el.querySelector('.rs2');
    r2.style.opacity = k; r2.style.transform = `scale(${0.6 + 0.4 * k})`;
  },
  folheando(el, c, p, dt) {
    const cv = el.querySelector('canvas'), ctx = cv.getContext('2d');
    const i = Math.min(NFOLH - 1, Math.floor(((c.off || 0) + dt) * 30) % NFOLH);
    ctx.drawImage(folh[i], 0, 0, 720, 551); cv.style.opacity = 1;
  },
  final(el, c, p, dt) {
    const parts = ['.fmock', '.fnome', '.fsub', '.fpreco', '.fbot'];
    parts.forEach((s, i) => { const n = el.querySelector(s), k = ease((dt - i * 0.12) / 0.35); n.style.opacity = k;
      const base = s === '.fpreco' ? 'translateX(-50%) ' : s === '.fbot' ? 'translateX(-50%) ' : '';
      const extra = s === '.fmock' ? ` translateY(${Math.sin(dt * 2.2) * 6}px) rotate(-3deg)` : s === '.fbot' ? ` scale(${1 + 0.04 * Math.sin(dt * 7)})` : '';
      n.style.transform = base + `translateY(${(1 - k) * 30}px)` + extra; });
  },
};
window.render = function (t) {
  let tit = null, titT0 = 0, final = false;
  for (const c of CENAS) {
    const el = document.getElementById(c.id), on = t >= c.t0 && t < c.t1;
    el.style.display = on ? 'block' : 'none';
    if (!on) continue;
    A[c.tipo](el, c, (t - c.t0) / (c.t1 - c.t0), t - c.t0);
    if (c.titulo) { tit = c.titulo; titT0 = c.tt0 ?? c.t0; }
    if (c.tipo === 'final') final = true;
  }
  if (tit && !final) { tituloEl.style.display = 'block'; tituloSp.textContent = tit;
    const k = ease((t - titT0) / 0.25); tituloSp.style.transform = `scale(${0.85 + 0.15 * k})`; tituloEl.style.opacity = 1; }
  else tituloEl.style.display = 'none';
  const b = LEG.find(x => t >= x.t0 && t < x.t1);
  if (b) { legEl.style.display = 'flex'; legSp.textContent = b.txt; } else legEl.style.display = 'none';
};
"""


def montar(n, voz):
    frases = ROTEIROS[n]
    mp3 = AUDIO / f"{voz}-{n}.mp3"
    dur, tempos, ancoras = alinhar(mp3, [f["texto"] for f in frases])
    total = dur + FECHO
    nq = math.ceil(total * FPS)
    total = nq / FPS
    # cenas: cada frase com cena abre uma nova; frases sem cena continuam a anterior
    cenas, legs = [], []
    for k, (f, (a, b)) in enumerate(zip(frases, tempos)):
        legs += blocos_legenda(f["legenda"], a + 0.02, b)
        if f["cena"]:
            cenas.append({"c": f["cena"], "t0": 0.0 if k == 0 else a})
    for i, c in enumerate(cenas):
        c["t1"] = cenas[i + 1]["t0"] if i + 1 < len(cenas) else total
    # a última legenda some no fim da fala
    planas, divs, folh_off = [], [], 0.0
    for i, c in enumerate(cenas):
        spec = c["c"]
        if spec["tipo"] == "partes":
            k = len(spec["partes"])
            for j, sub in enumerate(spec["partes"]):
                t0 = c["t0"] + (c["t1"] - c["t0"]) * j / k
                t1 = c["t0"] + (c["t1"] - c["t0"]) * (j + 1) / k
                s = dict(sub)
                s.setdefault("titulo", spec.get("titulo"))
                if spec.get("titulo") and not sub.get("titulo"):
                    s["tt0"] = c["t0"]
                planas.append({**s, "t0": t0, "t1": t1})
        else:
            planas.append({**spec, "t0": c["t0"], "t1": c["t1"]})
    for i, s in enumerate(planas):
        s["id"] = f"c{i}"
        if s["tipo"] == "folheando":
            s["off"] = folh_off
            folh_off += 4.0
        classe = "cheia" + (" escuro" if s.get("escuro") or s["tipo"] == "risco" else "") + (" laranja" if s["tipo"] == "final" else "")
        if s["tipo"] not in ("texto", "risco", "final"):
            classe = "palco"
        divs.append(f'<div class="cena {classe}" id="{s["id"]}">{html_cena(s)}</div>')
    nfolh = len(list((CACHE / "folheando").glob("*.jpg"))) if any(s["tipo"] == "folheando" for s in planas) else 0
    js = (JS.replace("__CENAS__", json.dumps(planas, ensure_ascii=False)).replace("__LEG__", json.dumps(legs, ensure_ascii=False))
          .replace("__NFOLH__", str(nfolh)).replace("__FOLH__", (CACHE / "folheando").as_uri()))
    pagina = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS.replace("%(f)s", FONTES.as_uri()).replace("%%", "%")}</style></head><body>'
              f'{"".join(divs)}<div id="titulo"><span></span></div><div id="legenda"><span></span></div><script>{js}</script></body></html>')
    nome = f"anuncio-{n}-{voz}"
    TMP.mkdir(exist_ok=True)
    arq_html = TMP / f"{nome}.html"
    arq_html.write_text(pagina, encoding="utf-8")
    quadros = TMP / nome
    subprocess.run(["node", str(AQUI / "gravar.cjs"), str(arq_html), str(quadros), str(nq), str(FPS)], check=True)
    VIDEOS.mkdir(exist_ok=True)
    saida = VIDEOS / f"{nome}.mp4"
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-framerate", str(FPS), "-i", str(quadros / "%05d.jpg"),
                    "-i", str(mp3), "-filter_complex", "[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,alimiter=limit=0.84:level=disabled,apad[a]",
                    "-map", "0:v", "-map", "[a]", "-frames:v", str(nq), "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                    "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart",
                    str(saida)], check=True)
    info = {"video": saida.name, "duracao": round(total, 2), "fala": round(dur, 2),
            "frases": [{"t0": round(a, 2), "t1": round(b, 2), "txt": f["legenda"]} for f, (a, b) in zip(frases, tempos)],
            "ancoras_em_pausa": f"{sum(ancoras)}/{len(ancoras)}"}
    (TMP / f"{nome}.json").write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{saida.name}: {total:.2f}s · fronteiras em pausas {sum(ancoras)}/{len(ancoras)}")
    return info


if __name__ == "__main__":
    args = sys.argv[1:]
    alvos = [(int(args[0]), args[1])] if len(args) == 2 else [(n, v) for n in (1, 2, 3, 4) for v in ("laynner", "amandinha")]
    for n, v in alvos:
        montar(n, v)
