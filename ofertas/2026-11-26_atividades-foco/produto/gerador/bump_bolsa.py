"""Bump 1 — Para levar na bolsa: 30 atividades rápidas em meia folha (A5), duas por folha A4 deitada,
com linha de corte no meio. 15 do Nível 1 e 15 do Nível 2, gabarito no fim."""
import random

import atividades2 as B
import gerar_amostra as GA
from bumps_base import Bump

SEMENTE = 909
BUMP = Bump("Para levar na bolsa", "para-levar-na-bolsa", "30 ATIVIDADES EM MEIA FOLHA · 2 NÍVEIS")

CSS = """
@page { size: A4 landscape; margin: 0; }
.pagina.paisagem { width: 297mm; height: 210mm; padding: 0; flex-direction: row; }
.meia { width: 148.5mm; height: 210mm; padding: 8mm 9mm 6mm; display: flex; flex-direction: column; position: relative; }
.meia + .meia { border-left: .35mm dashed #999; }
.meia .topo { padding-bottom: 1.6mm; border-bottom-width: .4mm; }
.meia .marca { font-size: 9pt; }
.meia .selo { font-size: 7pt; padding: .3mm 2mm; }
.meia h1 { font-size: 17pt; margin-top: 2.5mm; }
.meia .instrucao { font-size: 8.6pt; min-height: 8mm; margin-top: .8mm; }
.meia .area { margin-top: 1mm; }
.meia .area svg { width: 124mm; height: 155mm; }
.meia .rodape { font-size: 7pt; padding-top: 1.2mm; margin-top: auto; }
.tesoura { position: absolute; left: 148.5mm; top: 3mm; transform: translateX(-50%); font-size: 11pt; color: #888; background: #fff; }
.capa-meia { background: var(--fundo); }
.capa-meia .titulo { font-family: 'Baloo 2'; font-weight: 800; font-size: 34pt; line-height: .95; margin-top: 4mm; }
.capa-meia .titulo span { color: var(--laranja); }
.capa-meia .sub { font-size: 11pt; font-weight: 700; margin-top: 4mm; }
.capa-meia .tag { display: inline-block; margin-top: 5mm; font-weight: 800; font-size: 8.5pt; background: var(--tinta); color: #fff; padding: 1mm 3mm; border-radius: 1.5mm; }
.meia .passos li { margin: 2mm 0; font-size: 10pt; }
.gab8 { display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(2, 1fr); gap: 3mm; flex: 1; margin-top: 3mm; }
.gab8 .card { border: .3mm solid #ccc; border-radius: 2mm; padding: 1.6mm 2mm; overflow: hidden; display: flex; flex-direction: column; }
.gab8 .card h3 { font-family: 'Baloo 2'; font-weight: 800; font-size: 8.4pt; line-height: 1.1; }
.gab8 .card svg { width: 100%; flex: 1; min-height: 0; margin-top: 1mm; }
.gab8 .card p { font-size: 8pt; color: var(--cinza); margin-top: 2mm; }
.pagina.paisagem.paisagem-pad { padding: 9mm 12mm 7mm; flex-direction: column; }
"""


def atividades(rng):
    n1 = [
        B.labirinto(1, rng, 5, 6, "passaro", "arvore"),
        B.padroes(rng, 1, [["circulo", "quadrado"], ["sol", "sol", "lua"], ["peixe", "barco"], ["maca", "flor", "flor"], ["estrela", "coracao"]]),
        B.contar(rng, ["maca", "estrela", "peixe", "balao"], 1, 5),
        B.diferente(rng, B.VARIANTES[:6]),
        B.ligue_pontos(rng, 1, "casinha", 10),
        B.sudoku_figuras(rng, 11),
        B.labirinto(1, rng, 6, 7, "carro", "casa"),
        B.padroes(rng, 1, [["coracao", "estrela", "estrela"], ["nuvem", "sol"], ["arvore", "arvore", "casa"], ["balao", "lua"], ["uva", "banana", "maca"]]),
        B.tracado(rng, ["reta", "onda", "zigue", "ponte", "degraus"],
                  [("passaro", "arvore"), ("peixe", "barco"), ("sol", "nuvem"), ("carro", "casa"), ("balao", "estrela")]),
        B.contar(rng, ["flor", "carro", "coracao", "sol"], 2, 7),
        B.diferente(rng, (B.VARIANTES[2:] + B.VARIANTES[:2])[:6]),
        B.ligue_pontos(rng, 1, "coração", 13),
        B.sudoku_figuras(rng, 10),
        B.labirinto(1, rng, 6, 8, "peixe", "flor"),
        B.padroes(rng, 1, [["sol", "lua", "estrela"], ["flor", "flor", "maca"], ["casa", "arvore"], ["quadrado", "circulo", "circulo"], ["peixe", "peixe", "barco", "barco"]]),
    ]
    n2 = [
        B.labirinto(2, rng, 10, 12, "barco", "casa"),
        B.sudoku6(rng, 20),
        B.sequencias(rng, 1),
        B.diferente_grade(rng, [("peixe", dict(espelhar=True)), ("estrela", dict(variante="6pontas")), ("maca", dict(variante="semfolha"))]),
        B.quantos_tem(rng, ["estrela", "coracao", "lua"]),
        B.codigo_secreto(rng, "BOA VIAGEM"),
        B.labirinto(2, rng, 11, 13, "carro", "arvore"),
        B.sudoku6(rng, 18),
        B.sequencias(rng, 2),
        B.caca_palavras(rng, "frutas"),
        B.diferente_grade(rng, [("sol", dict(variante="poucosraios")), ("passaro", dict(espelhar=True)), ("flor", dict(variante="4petalas"))]),
        B.quantos_tem(rng, ["maca", "uva", "banana", "flor"]),
        B.labirinto(2, rng, 12, 14, "balao", "nuvem"),
        B.sudoku6(rng, 17),
        B.sequencias(rng, 3),
    ]
    for a in n1:
        assert a["nivel"] == 1, a["titulo"]
    for a in n2:
        assert a["nivel"] == 2, a["titulo"]
    # intercala os níveis para o adulto achar fácil: folhas 1–15 Nível 1, 16–30 Nível 2
    return n1 + n2


def meia_atividade(at, folha):
    return f"""<div class="meia">{BUMP.topo(f'<span class="selo">{at["categoria"]}</span>', GA.selo(at["nivel"]))}
  <h1>{at['titulo']}</h1><p class="instrucao">{at['instrucao']}</p>
  <div class="area">{GA.svg(at['svg'])}</div>
  <div class="rodape"><span>Dez Minutinhos · Para levar na bolsa · folha {folha}</span><span class="feito">Feito!<span class="caixa"></span></span></div></div>"""


def capa_e_uso():
    figs = "".join(f'<circle cx="{18 + i * 30}" cy="20" r="13" fill="#ffe1cf"/>' for i in range(4))
    from icones import icone
    figs += "".join(icone(n, 8 + i * 30, 10, 20) for i, n in enumerate(["carro", "barco", "balao", "estrela"]))
    capa = f"""<div class="meia capa-meia"><div class="marca">Dez <b>Minutinhos</b></div>
  <div class="bump" style="font-family:'Baloo 2';font-weight:800;font-size:9pt;color:var(--laranja);margin-top:2mm">BÔNUS EXTRA DO DEZ MINUTINHOS</div>
  <div class="titulo">Para levar<br><span>na bolsa</span></div>
  <p class="autor" style="font-size:9pt">por Gefferson Balles</p>
  <p class="sub">30 atividades rápidas em meia folha, para restaurante, viagem e sala de espera.</p>
  <div><span class="tag">30 ATIVIDADES · 2 NÍVEIS · GABARITO</span></div>
  <div style="margin-top:auto">{GA.svg(figs, 124, 40)}</div>
  <div class="rodape"><span>Nível 1 · 4 a 6 anos | Nível 2 · 7 a 10 anos</span><span></span></div></div>"""
    uso = f"""<div class="meia">{BUMP.topo('<span class="selo">Para o adulto</span>')}<h1>Como usar</h1>
  <div class="texto"><ol class="passos">
    <li><b>Imprima em A4 deitado</b> (paisagem), papel comum, preto e branco. Cada folha traz duas atividades.</li>
    <li><b>Corte na linha tracejada do meio.</b> Cada metade é uma meia folha (A5): dobre e guarde na bolsa.</li>
    <li><b>Folhas 1 a 15:</b> Nível 1 (4 a 6 anos, sem leitura). <b>Folhas 16 a 30:</b> Nível 2 (7 a 10 anos).</li>
    <li><b>Leve um lápis</b> e, se der, uma prancheta ou um livro para apoiar.</li>
    <li><b>Gabarito</b> nas últimas páginas.</li>
  </ol>
  <p class="aviso" style="font-size:9pt">Uso permitido: imprima quantas vezes quiser para as crianças da sua família. Não é permitido revender nem repassar o arquivo.</p></div>
  <div class="rodape"><span>Dez Minutinhos · Para levar na bolsa</span><span></span></div></div>"""
    return f'<section class="pagina paisagem">{capa}{uso}<span class="tesoura">✂</span></section>'


def gabarito(lista, pag_ini):
    cards = []
    for folha, at in lista:
        corpo = GA.svg(at["gabarito_svg"]) if at.get("gabarito_svg") else f"<p>{at['gabarito_txt']}</p>"
        cards.append(f'<div class="card"><h3>Folha {folha} · N{at["nivel"]} · {at["titulo"]}</h3>{corpo}</div>')
    pags = []
    for i in range(0, len(cards), 8):
        pags.append(f"""<section class="pagina paisagem paisagem-pad">{BUMP.topo('<span class="selo">Gabarito</span>')}
  <div class="gab8">{''.join(cards[i:i + 8])}</div>
  <div class="rodape"><span>Dez Minutinhos · Para levar na bolsa · gabarito {len(pags) + 1}</span><span></span></div></section>""")
    return pags


def gerar():
    rng = random.Random(SEMENTE)
    ats = atividades(rng)
    assert len(ats) == 30
    pags = [capa_e_uso()]
    for i in range(0, 30, 2):
        pags.append(f'<section class="pagina paisagem">{meia_atividade(ats[i], i + 1)}{meia_atividade(ats[i + 1], i + 2)}'
                    f'<span class="tesoura">✂</span></section>')
    pags += gabarito([(i + 1, a) for i, a in enumerate(ats)], len(pags) + 1)
    total = BUMP.montar(pags, CSS)
    return dict(paginas_a4=total, atividades=len(ats))


if __name__ == "__main__":
    print(gerar())
