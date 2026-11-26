"""Gera o caderno COMPLETO do Dez Minutinhos (120 atividades, 2 níveis, plano de 30 dias por nível,
gabarito e 3 bônus) em saida/completo.html. Depois: node render.cjs 1 completo
Uso: python3 gerar_completo.py"""
import json
import pathlib
import random

import atividades2 as B
import gerar_amostra as GA
from icones import icone

AQUI = pathlib.Path(__file__).parent
SAIDA = AQUI / "saida"
SEMENTE = 30112026

CSS_EXTRA = """
.plano { width: 100%; border-collapse: collapse; font-size: 9.6pt; margin-top: 3mm; }
.plano th, .plano td { border: .25mm solid #bbb; padding: 1.15mm 2mm; text-align: left; }
.plano th { background: #f4f4f4; font-family: 'Baloo 2'; font-weight: 800; }
.plano td.dia { font-family: 'Baloo 2'; font-weight: 800; text-align: center; width: 13mm; }
.plano td.ok { width: 12mm; text-align: center; }
.plano .pg { color: var(--cinza); font-size: 8.5pt; }
.plano tr:nth-child(7n) td { border-bottom: .5mm solid #888; }
.gab9 { display: grid; grid-template-columns: repeat(3, 1fr); grid-auto-rows: 78mm; gap: 3mm; margin-top: 4mm; flex: 1; }
.gab9 .card { border: .3mm solid #ccc; border-radius: 2mm; padding: 1.6mm 2mm; overflow: hidden; display: flex; flex-direction: column; }
.gab9 .card h3 { font-family: 'Baloo 2'; font-weight: 800; font-size: 8.6pt; line-height: 1.1; }
.gab9 .card p { font-size: 8.5pt; color: var(--cinza); margin-top: 2mm; }
.gab9 .card svg { width: 100%; flex: 1; min-height: 0; margin-top: 1mm; }
.sumario { list-style: none; font-size: 13pt; margin-top: 6mm; }
.sumario li { display: flex; gap: 2mm; padding: 2.4mm 0; border-bottom: .3mm dotted #bbb; }
.sumario li span:first-child { flex: 1; font-weight: 700; }
.sumario li small { display: block; font-weight: 600; color: var(--cinza); font-size: 10pt; }
.abertura { background: var(--fundo); }
.abertura .grande { font-family: 'Baloo 2'; font-weight: 800; font-size: 54pt; line-height: 1; margin-top: 40mm; }
.abertura .grande span { color: var(--laranja); }
.conquistas { display: grid; grid-template-columns: repeat(5, 1fr); gap: 3mm; margin-top: 5mm; }
.conquistas div { border: .4mm solid var(--tinta); border-radius: 3mm; height: 30mm; position: relative; }
.conquistas b { position: absolute; left: 2mm; top: 1mm; font-family: 'Baloo 2'; font-size: 13pt; }
.conquistas svg { position: absolute; right: 2mm; bottom: 2mm; width: 15mm; height: 15mm; }
.linha-nome { margin-top: 5mm; font-size: 13pt; font-weight: 700; }
.cert { flex: 1; border: 1.2mm solid var(--tinta); border-radius: 5mm; margin: 2mm 0; position: relative; padding: 8mm 12mm;
  display: flex; flex-direction: column; align-items: center; text-align: center; outline: .5mm dashed var(--laranja); outline-offset: -4mm; }
.cert .t1 { font-family: 'Baloo 2'; font-weight: 800; font-size: 13pt; color: var(--laranja); letter-spacing: 1pt; margin-top: 2mm; }
.cert .t2 { font-family: 'Baloo 2'; font-weight: 800; font-size: 27pt; line-height: 1.05; margin-top: 2mm; }
.cert .nome { margin-top: 7mm; font-size: 12pt; font-weight: 700; width: 75%; border-bottom: .4mm solid var(--tinta); padding-bottom: 7mm; }
.cert .rodcert { margin-top: auto; display: flex; justify-content: space-between; width: 100%; font-size: 10.5pt; font-weight: 700; }
.cert svg { position: absolute; width: 22mm; height: 22mm; }
.corte { text-align: center; font-size: 8pt; color: var(--cinza); border-top: .3mm dashed #999; padding-top: 1mm; }
.ideias { counter-reset: i var(--ini); list-style: none; margin-top: 4mm; font-size: 11.2pt; line-height: 1.4; }
.ideias li { counter-increment: i; position: relative; padding-left: 10mm; margin: 2.3mm 0; }
.ideias li::before { content: counter(i); position: absolute; left: 0; top: 0; width: 7mm; height: 7mm; border-radius: 50%; background: var(--laranja);
  color: #fff; font-family: 'Baloo 2'; font-weight: 800; font-size: 10pt; text-align: center; line-height: 7.4mm; }
.ideias b { font-family: 'Baloo 2'; font-weight: 800; }
.texto p { margin: 2mm 0; }
"""


# ------------------------------------------------------------------ atividades
def nivel1(rng):
    cat = {k: [] for k in ["Atenção", "Memória", "Padrões", "Lógica", "Traçado", "Cores e códigos"]}
    var = B.VARIANTES[:]
    for p in range(4):
        rng.shuffle(var)
        cat["Atenção"].append(("dif", lambda v=var[:6]: B.diferente(rng, v)))
    tipos_cont = [["maca", "estrela", "peixe", "balao"], ["flor", "carro", "coracao", "sol"], ["passaro", "uva", "casa", "lua"],
                  ["barco", "nuvem", "arvore", "banana"], ["estrela", "maca", "balao", "flor"]]
    faixas = [(1, 5), (2, 6), (3, 8), (3, 9), (4, 10)]
    for t, (a, b) in zip(tipos_cont, faixas):
        cat["Atenção"].append(("cont", lambda t=t, a=a, b=b: B.contar(rng, t, a, b)))
    for cena in ["quintal", "parque", "praia"]:
        cat["Atenção"].append(("erros", lambda c=cena: B.diferencas(rng, 1, c, 5)))
    for nv, no in [(3, 6), (3, 6), (3, 6), (4, 6), (4, 8), (4, 8), (5, 8), (5, 8)]:
        cat["Memória"].append(("mem", lambda nv=nv, no=no: B.memoria_figuras(rng, 1, nv, no)))
    moldes = [["A", "B"], ["A", "A", "B"], ["A", "B", "B"], ["A", "B", "C"], ["A", "A", "B", "B"]]
    for p in range(10):
        dif = moldes[:3] if p < 4 else moldes
        ciclos = []
        for _ in range(5):
            m = rng.choice(dif)
            figs = rng.sample(B.FIG_PADRAO, len(set(m)))
            mapa = dict(zip(sorted(set(m)), figs))
            ciclos.append([mapa[x] for x in m])
        cat["Padrões"].append(("pad", lambda c=ciclos: B.padroes(rng, 1, c)))
    pares_lab = [("passaro", "arvore"), ("peixe", "flor"), ("carro", "casa"), ("balao", "nuvem"), ("barco", "estrela"),
                 ("passaro", "casa"), ("carro", "arvore"), ("peixe", "estrela")]
    tam_lab = [(5, 6), (5, 7), (6, 7), (6, 8), (7, 8), (7, 9), (8, 10), (8, 11)]
    for (c, l), (a, b) in zip(tam_lab, pares_lab):
        cat["Lógica"].append(("lab", lambda c=c, l=l, a=a, b=b: B.labirinto(1, rng, c, l, a, b)))
    for d in [11, 10, 9, 8]:
        cat["Lógica"].append(("sud", lambda d=d: B.sudoku_figuras(rng, d)))
    cat["Lógica"] = [cat["Lógica"][i] for i in [0, 1, 8, 2, 3, 9, 4, 5, 10, 6, 7, 11]]
    for des, alvo in [("casinha", 10), ("coração", 13), ("barquinho", 15), ("peixe", 17), ("estrela", 20)]:
        cat["Traçado"].append(("pts", lambda d=des, a=alvo: B.ligue_pontos(rng, 1, d, a)))
    tipos_tr = [["reta", "onda", "zigue", "ponte", "montanha"], ["reta", "curva", "degraus", "onda", "zigue"],
                ["onda2", "montanha", "ponte", "degraus", "curva"], ["zigue", "onda2", "laco", "degraus", "montanha"],
                ["laco", "onda2", "degraus", "ponte", "zigue"]]
    figs = ["passaro", "arvore", "peixe", "barco", "sol", "nuvem", "estrela", "lua", "maca", "casa", "carro", "flor", "balao", "coracao"]
    for t in tipos_tr:
        pares = []
        for _ in range(5):
            a, b = rng.sample(figs, 2)
            pares.append((a, b))
        cat["Traçado"].append(("tr", lambda t=t, p=pares: B.tracado(rng, t, p)))
    cat["Traçado"] = [cat["Traçado"][i] for i in [5, 0, 6, 1, 7, 2, 8, 3, 9, 4]]
    for arte in ["coracao", "sol", "estrela", "sorvete", "casa", "arvore", "barco", "flor"]:
        cat["Cores e códigos"].append(("pinte", lambda a=arte: B.pinte_codigo(rng, 1, a)))
    return cat


def nivel2(rng):
    cat = {k: [] for k in ["Atenção", "Memória", "Padrões", "Lógica", "Traçado", "Cores e códigos"]}
    var = B.VARIANTES[:]
    gradesubs = [[("peixe", dict(variante="semboca")), ("estrela", dict(variante="6pontas")), ("maca", dict(variante="semfolha"))],
                 [("sol", dict(variante="poucosraios")), ("passaro", dict(espelhar=True)), ("flor", dict(variante="4petalas"))],
                 [("casa", dict(variante="semjanela")), ("lua", dict(espelhar=True)), ("carro", dict(espelhar=True))],
                 [("casa", dict(variante="semporta")), ("banana", dict(espelhar=True)), ("barco", dict(espelhar=True))]]
    qt = [["estrela", "coracao", "lua"], ["maca", "uva", "banana", "flor"], ["peixe", "barco", "sol", "nuvem"]]
    at = [("erros", lambda: B.diferencas(rng, 2, "quintal", 7)), ("gr", lambda: B.diferente_grade(rng, gradesubs[0])),
          ("qt", lambda: B.quantos_tem(rng, qt[0])), ("erros", lambda: B.diferencas(rng, 2, "parque", 7)),
          ("gr", lambda: B.diferente_grade(rng, gradesubs[1])), ("erros", lambda: B.diferencas(rng, 2, "praia", 7)),
          ("qt", lambda: B.quantos_tem(rng, qt[1])), ("gr", lambda: B.diferente_grade(rng, gradesubs[2])),
          ("erros", lambda: B.diferencas(rng, 2, "noite", 7)), ("qt", lambda: B.quantos_tem(rng, qt[2])),
          ("gr", lambda: B.diferente_grade(rng, gradesubs[3])), ("erros", lambda: B.diferencas(rng, 2, "festa", 7))]
    cat["Atenção"] = at
    cat["Memória"] = [("mem", lambda: B.memoria_figuras(rng, 2, 5, 10)), ("lug", lambda: B.memoria_lugares(rng, 3)),
                      ("mem", lambda: B.memoria_figuras(rng, 2, 6, 10)), ("mem", lambda: B.memoria_figuras(rng, 2, 6, 10)),
                      ("lug", lambda: B.memoria_lugares(rng, 4)), ("mem", lambda: B.memoria_figuras(rng, 2, 7, 10)),
                      ("lug", lambda: B.memoria_lugares(rng, 5)), ("mem", lambda: B.memoria_figuras(rng, 2, 8, 10))]

    def ciclos_rot():
        tipos = [
            lambda: [("triangulo", g, False) for g in (0, 90, 180, 270)],
            lambda: [("lua", 0, False), ("lua", 0, True)],
            lambda: [("peixe", 0, False), ("peixe", 0, True), ("estrela", 0, False)],
            lambda: [("coracao", 0, False), ("coracao", 180, False), ("coracao", 180, False)],
            lambda: [("passaro", 0, False), ("passaro", 0, True), ("passaro", 0, True), ("sol", 0, False)],
            lambda: [(f, 0, False) for f in rng.sample(B.FIG_PADRAO, 4)],
            lambda: [("banana", 0, False), ("banana", 90, False), ("banana", 180, False)],
        ]
        return [rng.choice(tipos)() for _ in range(5)]
    pad = []
    for k, f in enumerate([1, None, 1, 2, None, 2, 3, None, 3, None]):
        if f is None:
            c = ciclos_rot()
            pad.append(("padr", lambda c=c: B.padroes(rng, 2, c)))
        else:
            pad.append(("seq", lambda f=f: B.sequencias(rng, f)))
    cat["Padrões"] = pad
    labs = [(11, 13, "barco", "casa"), (12, 15, "carro", "arvore"), (14, 17, "balao", "nuvem"), (15, 19, "peixe", "estrela")]
    temas = B.TEMAS_LOGICA
    cat["Lógica"] = [("sud", lambda: B.sudoku6(rng, 20)), ("lab", lambda: B.labirinto(2, rng, *labs[0])),
                     ("gl", lambda: B.grade_logica(rng, temas[0])), ("sud", lambda: B.sudoku6(rng, 18)),
                     ("lab", lambda: B.labirinto(2, rng, *labs[1])), ("gl", lambda: B.grade_logica(rng, temas[1])),
                     ("sud", lambda: B.sudoku6(rng, 17)), ("lab", lambda: B.labirinto(2, rng, *labs[2])),
                     ("sud", lambda: B.sudoku6(rng, 16)), ("gl", lambda: B.grade_logica(rng, temas[2])),
                     ("lab", lambda: B.labirinto(2, rng, *labs[3])), ("sud", lambda: B.sudoku6(rng, 15))]
    tr = []
    for (des, alvo), seg in zip([("casinha", 24), ("foguete", 28), ("coração", 32), ("peixe", 34), ("estrela", 40)], [8, 10, 12, 14, 16]):
        tr.append(("cop", lambda s=seg: B.copie_desenho(rng, s)))
        tr.append(("pts", lambda d=des, a=alvo: B.ligue_pontos(rng, 2, d, a)))
    cat["Traçado"] = tr
    cat["Cores e códigos"] = [("caca", lambda: B.caca_palavras(rng, "frutas")), ("cod", lambda: B.codigo_secreto(rng, "BRINCAR FAZ BEM")),
                              ("pinte", lambda: B.pinte_codigo(rng, 2, "peixe", contas=True)), ("caca", lambda: B.caca_palavras(rng, "brinquedos")),
                              ("cod", lambda: B.codigo_secreto(rng, "BOM TRABALHO")), ("caca", lambda: B.caca_palavras(rng, "cozinha")),
                              ("cod", lambda: B.codigo_secreto(rng, "SUPER DESAFIO")), ("caca", lambda: B.caca_palavras(rng, "cores"))]
    return cat


def agenda(cat, rng):
    """Distribui 60 atividades em 30 dias, 2 por dia, de categorias diferentes, mantendo a ordem de dificuldade."""
    itens = []
    for nome, lista in cat.items():
        n = len(lista)
        for k, (tipo, f) in enumerate(lista):
            itens.append(((k + .5) / n + rng.uniform(-.004, .004), nome, f))
    itens.sort(key=lambda x: x[0])
    fila = [(c, f) for _, c, f in itens]
    dias = []
    while fila:
        a = fila.pop(0)
        j = next((i for i, b in enumerate(fila) if b[0] != a[0]), None)
        assert j is not None, "não deu para separar categorias"
        b = fila.pop(j)
        dias.append((a, b))
    assert len(dias) == 30
    return dias


# ------------------------------------------------------------------ páginas
def rodape(num, dia=None):
    dir_ = f'<span class="feito">Dia {dia} <span>Feito!<span class="caixa"></span></span></span>' if dia else "<span></span>"
    return f'<div class="rodape"><span>Dez Minutinhos · página {num}</span>{dir_}</div>'


def topo(*selos):
    return f'<div class="topo"><div class="marca">Dez <b>Minutinhos</b></div><div class="selos">{"".join(selos)}</div></div>'


def pag_atividade(at, num, dia):
    return f"""<section class="pagina">{topo(f'<span class="selo">{at["categoria"]}</span>', GA.selo(at["nivel"]))}
  <h1>{at['titulo']}</h1><p class="instrucao">{at['instrucao']}</p>
  <div class="area">{GA.svg(at['svg'])}</div>{rodape(num, dia)}</section>"""


def capa():
    html = GA.capa().replace("CADERNO-AMOSTRA · 13 ATIVIDADES · 2 NÍVEIS", "120 ATIVIDADES · 2 NÍVEIS · PLANO DE 30 DIAS")
    assert "120 ATIVIDADES" in html
    return html


def como_usar(pags):
    return f"""<section class="pagina">{topo('<span class="selo">Para o adulto</span>')}
  <h1>Como usar</h1><div class="texto">
  <ol class="passos">
    <li><b>Escolha o nível pela idade.</b> Nível 1 (4 a 6 anos) não pede leitura: você lê a instrução em voz alta. Nível 2 (7 a 10 anos) tem leitura inicial.</li>
    <li><b>Siga o plano do seu nível.</b> São 30 dias, com 2 folhas por dia de tipos diferentes. O plano do Nível 1 está na página {pags['plano1']} e o do Nível 2 na página {pags['plano2']}.</li>
    <li><b>Imprima só o que vai usar.</b> Uma semana são 14 folhas. Funciona em preto e branco, em papel A4 comum.</li>
    <li><b>Dez minutinhos bastam.</b> Se não terminar, tudo bem: guarde e continue depois. Pular um dia também não tem problema.</li>
    <li><b>Confira no gabarito</b> (a partir da página {pags['gabarito']}) e marque o dia no quadro de conquistas.</li>
  </ol>
  <h2>Os dois níveis</h2>
  <table class="niveis">
    <tr><th>Nível</th><th>Idade</th><th>Como é</th></tr>
    <tr><td><b>1</b></td><td>4 a 6 anos</td><td>Sem leitura. Figuras grandes, traço grosso, poucas etapas. 60 atividades.</td></tr>
    <tr><td><b>2</b></td><td>7 a 10 anos</td><td>Leitura inicial, números e regras com mais passos. 60 atividades.</td></tr>
  </table>
  <h2>Do que você vai precisar</h2>
  <p>Lápis, borracha e lápis de cor. Nas atividades de memória, a folha é dobrada numa linha: não precisa de tesoura.</p>
  <p class="aviso">Uso permitido: imprima quantas vezes quiser para as crianças da sua família. Não é permitido revender nem repassar o arquivo.</p>
  </div>{rodape(2)}</section>"""


def sumario(pags):
    itens = [("Como usar", "", 2), ("Nível 1 · 4 a 6 anos", "plano de 30 dias + 60 atividades", pags["plano1"]),
             ("Nível 2 · 7 a 10 anos", "plano de 30 dias + 60 atividades", pags["plano2"]),
             ("Gabarito", "respostas das atividades dos dois níveis", pags["gabarito"]),
             ("Bônus 1 · Quadro de conquistas e 6 certificados", "", pags["conquistas"]),
             ("Bônus 2 · 30 ideias longe da tela sem imprimir nada", "", pags["ideias"]),
             ("Bônus 3 · Guia do adulto", "", pags["guia"])]
    li = "".join(f'<li><span>{t}{f"<small>{s}</small>" if s else ""}</span><span>pág. {p}</span></li>' for t, s, p in itens)
    return f"""<section class="pagina">{topo()}<h1>O que tem aqui</h1><ul class="sumario">{li}</ul>{rodape(3)}</section>"""


def abertura(nivel, num):
    sub = "4 a 6 anos · sem leitura" if nivel == 1 else "7 a 10 anos · leitura inicial"
    figs = "".join(icone(n, 10 + i * 45, 10, 34) for i, n in enumerate(["estrela", "peixe", "balao", "flor"]))
    return f"""<section class="pagina abertura">{topo(GA.selo(nivel))}
  <div class="grande">Nível <span>{nivel}</span></div><p class="sub" style="font-size:17pt;font-weight:800;margin-top:4mm">{sub}</p>
  <p style="font-size:12pt;margin-top:6mm;max-width:150mm">60 atividades em 30 dias, 2 por dia. O plano está na próxima página.</p>
  <div style="margin-top:auto">{GA.svg(figs, 182, 60)}</div>{rodape(num)}</section>"""


def plano(nivel, dias, num, pag_de):
    linhas = ""
    for d, (a, b) in enumerate(dias, 1):
        linhas += (f'<tr><td class="dia">{d}</td><td>{a["titulo"]} <span class="pg">· {a["categoria"]} · pág. {pag_de[id(a)]}</span></td>'
                   f'<td>{b["titulo"]} <span class="pg">· {b["categoria"]} · pág. {pag_de[id(b)]}</span></td><td class="ok"><span class="caixa"></span></td></tr>')
    return f"""<section class="pagina">{topo(GA.selo(nivel))}<h1>Plano de 30 dias</h1>
  <p class="instrucao" style="min-height:0">2 folhas por dia. Imprima a semana de uma vez (14 folhas) e marque cada dia feito.</p>
  <table class="plano"><tr><th>Dia</th><th>Folha 1</th><th>Folha 2</th><th>Feito</th></tr>{linhas}</table>{rodape(num)}</section>"""


def gabarito(lista, num_ini):
    cards = []
    for num, at in lista:
        corpo = GA.svg(at["gabarito_svg"]) if at.get("gabarito_svg") else f"<p>{at['gabarito_txt']}</p>"
        cards.append(f'<div class="card"><h3>Pág. {num} · N{at["nivel"]} · {at["titulo"]}</h3>{corpo}</div>')
    pags = []
    for i in range(0, len(cards), 9):
        pags.append(f"""<section class="pagina">{topo('<span class="selo">Gabarito</span>')}
  <div class="gab9">{''.join(cards[i:i + 9])}</div>{rodape(num_ini + len(pags))}</section>""")
    return pags


def quadro_conquistas(num):
    est = '<svg viewBox="0 0 100 100"><polygon points="50,6 61,38 95,38 67,58 78,92 50,71 22,92 33,58 5,38 39,38" fill="none" stroke="#bbb" stroke-width="4" stroke-linejoin="round"/></svg>'
    caixas = "".join(f"<div><b>{d}</b>{est}</div>" for d in range(1, 31))
    return f"""<section class="pagina">{topo('<span class="selo">Bônus 1</span>')}<h1>Meu quadro de conquistas</h1>
  <p class="instrucao" style="min-height:0">A cada dia feito, pinte a estrela, cole um adesivo ou faça um carimbo.</p>
  <p class="linha-nome">Nome: ______________________________ &nbsp; Nível: ____</p>
  <div class="conquistas">{caixas}</div>{rodape(num)}</section>"""


CERTS = [("SEMANA 1 COMPLETA", "por fazer os dias 1 a 7 do plano"), ("SEMANA 2 COMPLETA", "por fazer os dias 8 a 14 do plano"),
         ("SEMANA 3 COMPLETA", "por fazer os dias 15 a 21 do plano"), ("SEMANA 4 COMPLETA", "por fazer os dias 22 a 30 do plano"),
         ("NÍVEL 1 CONCLUÍDO", "por terminar as 60 atividades do Nível 1"), ("NÍVEL 2 CONCLUÍDO", "por terminar as 60 atividades do Nível 2")]


def certificados(num_ini):
    pags = []
    for i in range(0, 6, 2):
        blocos = []
        for k, (t, sub) in enumerate(CERTS[i:i + 2]):
            ic1 = GA.svg(icone("estrela", 5, 5, 90), 100, 100).replace("<svg ", '<svg style="left:6mm;top:6mm" ')
            ic2 = GA.svg(icone("balao", 5, 5, 90), 100, 100).replace("<svg ", '<svg style="right:6mm;top:6mm" ')
            blocos.append(f"""<div class="cert">{ic1}{ic2}<div class="t1">CERTIFICADO DEZ MINUTINHOS</div><div class="t2">{t}</div>
              <div class="nome">Este certificado é de:</div><p style="margin-top:3mm;font-size:12pt;font-weight:700">{sub}</p>
              <div class="rodcert"><span>Data: ____/____/______</span><span>Assinatura: ____________________</span></div></div>""")
        pags.append(f"""<section class="pagina">{topo(f'<span class="selo">Bônus 1 · Certificados {i + 1} e {i + 2}</span>')}
  {blocos[0]}<div class="corte">✂ recorte na linha</div>{blocos[1]}{rodape(num_ini + len(pags))}</section>""")
    return pags


IDEIAS = [
    ("Caça às cores", "Diga uma cor e a criança traz 5 objetos dessa cor que encontrar pela casa."),
    ("Estátua", "Ponha uma música. Quando parar, todo mundo congela na posição em que estiver."),
    ("Eu vejo", "“Eu vejo uma coisa que é redonda e azul…” Quem adivinhar primeiro escolhe a próxima."),
    ("O que sumiu?", "Arrume 6 objetos na mesa, peça para a criança olhar, cubra com um pano e tire um. Qual sumiu?"),
    ("Desenho falado", "Um descreve um desenho sem mostrar. O outro tenta desenhar só ouvindo. Depois comparem."),
    ("Barquinho de papel", "Dobre um barquinho com uma folha usada e teste na pia ou na bacia, com um adulto por perto."),
    ("Quantos passos?", "Quantos passos do quarto até a cozinha? E de passinhos de formiga? E pulando?"),
    ("Cabana", "Monte uma cabana com lençol, cadeiras e almofadas. Vale ler um livro lá dentro."),
    ("Fantoche de meia", "Uma meia velha vira personagem. Invente a voz e faça um teatrinho atrás do sofá."),
    ("Boliche de garrafas", "Garrafas plásticas vazias de pé e uma bola. Conte quantas caíram em cada jogada."),
    ("Adivinhe o som", "De olhos fechados, a criança tenta descobrir que objeto fez o barulho: chave, colher, papel…"),
    ("História maluca", "Cada pessoa fala uma frase e o próximo continua a história. Quanto mais estranha, melhor."),
    ("Mímica de bichos", "Imite um bicho sem fazer som. Os outros tentam adivinhar."),
    ("Ajudante de cozinha", "Lavar frutas, contar colheres, arrumar a mesa. Sem faca e sem fogo."),
    ("Meias em par", "Misture as meias limpas e peça para juntar os pares e separar por tamanho."),
    ("Sombras na parede", "Com uma lanterna no escuro, faça bichos de sombra com as mãos."),
    ("Feijão no algodão", "Plante um feijão num copo com algodão úmido e acompanhe o broto a cada dia."),
    ("Amarelinha", "Desenhe a amarelinha no chão com fita crepe ou giz e jogue com uma tampinha."),
    ("Siga o mestre", "Um faz um movimento e todos copiam. Depois troca o mestre."),
    ("Inventor de caixas", "Caixas de papelão e fita adesiva viram carro, robô, casa ou o que imaginar."),
    ("Medir com palmos", "Quantos palmos tem a mesa? E a cama? Quem tem o palmo maior da casa?"),
    ("Lista ilustrada", "Faça a lista de compras junto: a criança desenha o que está faltando em casa."),
    ("Cartinha", "Escrever ou desenhar uma cartinha para alguém da família ou para um amigo."),
    ("Dança das almofadas", "Almofadas no chão, música tocando. Quando parar, cada um procura uma almofada."),
    ("Janela de contar", "Olhando pela janela: quantos carros brancos passam? Quantos cachorros?"),
    ("Do menor ao maior", "Arrume brinquedos ou livros em fila, do menor para o maior. Depois ao contrário."),
    ("Corrida da colher", "Leve uma bolinha de papel numa colher de uma ponta à outra da sala sem deixar cair."),
    ("Nuvens", "Deitados no chão do quintal ou olhando pela janela: com o que cada nuvem se parece?"),
    ("Massinha sem fogo", "Misture farinha, um pouco de sal e água até virar massinha. É só não colocar na boca."),
    ("Rádio da família", "Gravem no celular um “programa de rádio”: notícia do dia, previsão do tempo e uma música cantada."),
]


def ideias(num_ini):
    assert len(IDEIAS) == 30
    pags = []
    for parte, ini in [(IDEIAS[:15], 0), (IDEIAS[15:], 15)]:
        li = "".join(f"<li><b>{t}.</b> {d}</li>" for t, d in parte)
        cab = "<h1>30 ideias longe da tela</h1><p class='instrucao' style='min-height:0'>Para os dias em que a impressora não colaborar. Nada aqui precisa ser impresso.</p>" if ini == 0 else "<h1>30 ideias longe da tela <span style='color:var(--cinza);font-size:16pt'>(continuação)</span></h1>"
        pags.append(f"""<section class="pagina">{topo('<span class="selo">Bônus 2</span>')}{cab}
  <ol class="ideias" style="--ini:{ini}">{li}</ol>{rodape(num_ini + len(pags))}</section>""")
    return pags


def guia(num_ini):
    p1 = f"""<section class="pagina">{topo('<span class="selo">Bônus 3</span>')}<h1>Guia do adulto</h1><div class="texto">
  <h2>Como apresentar</h2>
  <p>Escolha um momento tranquilo e um lugar com mesa e boa luz. Leia a instrução em voz alta, mesmo no Nível 2: ajuda a criança a começar.
  Deixe que ela tente sozinha antes de ajudar. Se pedir ajuda, dê uma pista pequena (“olha esta parte aqui”) em vez da resposta.</p>
  <h2>O plano de 30 dias</h2>
  <p>Cada dia tem 2 folhas de tipos diferentes. A ordem vai do mais fácil para o mais difícil, então vale seguir a sequência.
  Pulou um dia? Continue de onde parou. Não existe atraso.</p>
  <h2>Quando parar</h2>
  <p>Os 10 minutos são uma referência, não uma meta. Se a criança cansou, ficou irritada ou quer brincar de outra coisa, pare e guarde a folha.
  Terminar não é obrigatório. A ideia é que seja um momento bom.</p>
  <h2>Errar faz parte</h2>
  <p>Use o gabarito para você conferir, não para corrigir em vermelho. Se algo saiu diferente, pergunte como ela pensou. Muitas vezes o caminho
  dela também faz sentido, e uma conversa vale mais do que a resposta certa.</p>
  </div>{rodape(num_ini)}</section>"""
    p2 = f"""<section class="pagina">{topo('<span class="selo">Bônus 3</span>')}<h1>Guia do adulto <span style="color:var(--cinza);font-size:16pt">(continuação)</span></h1><div class="texto">
  <h2>Nível 1 ou Nível 2?</h2>
  <p>A idade é só um ponto de partida. Alguns sinais de que é hora de passar do Nível 1 para o Nível 2:</p>
  <ul style="padding-left:6mm"><li>as atividades do Nível 1 terminam rápido demais e sem nenhuma dúvida;</li>
  <li>a criança já lê palavras curtas sozinha;</li><li>ela pede “uma mais difícil”.</li></ul>
  <p>Na dúvida, imprima uma folha de cada nível no mesmo dia e veja qual rende mais conversa e menos frustração.
  Também dá para voltar ao Nível 1 quando quiser: não tem problema nenhum.</p>
  <h2>Dicas de impressão</h2>
  <p>Papel A4 comum, em preto e branco. Na impressora, escolha “tamanho real” ou “100%” para nada ficar cortado.
  Para economizar, imprima a semana de uma vez (14 folhas) e guarde numa pasta.</p>
  <h2>Atividades de memória</h2>
  <p>Mostre a parte de cima pelo tempo indicado, dobre a folha na linha tracejada para esconder e peça para a criança responder embaixo.</p>
  <h2>Repetir vale</h2>
  <p>O arquivo é seu: imprima de novo as atividades preferidas, para repetir o plano ou para outra criança da família.</p>
  </div>{rodape(num_ini + 1)}</section>"""
    return [p1, p2]


# ------------------------------------------------------------------ montagem
def main():
    rng = random.Random(SEMENTE)
    niveis = []
    for nv, fab in [(1, nivel1), (2, nivel2)]:
        cat = fab(rng)
        assert sum(len(v) for v in cat.values()) == 60, (nv, {k: len(v) for k, v in cat.items()})
        dias = agenda(cat, rng)
        dias_at = [(fa(), fb()) for (ca, fa), (cb, fb) in dias]
        for d, (a, b) in enumerate(dias_at, 1):
            assert a["categoria"] != b["categoria"], (nv, d)
            assert a["nivel"] == nv and b["nivel"] == nv, (nv, d, a["titulo"])
        niveis.append(dias_at)

    # numeração: 1 capa, 2 como usar, 3 sumário, depois cada nível = abertura + plano + 60
    num = 4
    pags = {}
    pag_de, ordem = {}, []
    for nv, dias_at in enumerate(niveis, 1):
        pags[f"abertura{nv}"] = num; pags[f"plano{nv}"] = num + 1; num += 2
        for d, (a, b) in enumerate(dias_at, 1):
            for at in (a, b):
                pag_de[id(at)] = num; ordem.append((num, at, d)); num += 1
    pags["gabarito"] = num
    n_gab = -(-len(ordem) // 9)
    num += n_gab
    pags["conquistas"] = num; num += 1
    pags["certificados"] = num; num += 3
    pags["ideias"] = num; num += 2
    pags["guia"] = num; num += 2

    html_pags = [capa(), como_usar(pags), sumario(pags)]
    k = 0
    for nv, dias_at in enumerate(niveis, 1):
        html_pags.append(abertura(nv, pags[f"abertura{nv}"]))
        html_pags.append(plano(nv, dias_at, pags[f"plano{nv}"], pag_de))
        for d, (a, b) in enumerate(dias_at, 1):
            for at in (a, b):
                n_, at_, d_ = ordem[k]; k += 1
                assert at_ is at
                html_pags.append(pag_atividade(at, n_, d))
    html_pags += gabarito([(n_, at) for n_, at, _ in ordem], pags["gabarito"])
    html_pags.append(quadro_conquistas(pags["conquistas"]))
    html_pags += certificados(pags["certificados"])
    html_pags += ideias(pags["ideias"])
    html_pags += guia(pags["guia"])
    assert len(html_pags) == num - 1, (len(html_pags), num - 1)

    fontes = (AQUI / "fontes" / "fontes.css").read_text()
    html = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Dez Minutinhos — caderno completo</title><style>{fontes}{GA.CSS}{CSS_EXTRA}</style></head>
<body>{''.join(html_pags)}</body></html>"""
    assert "amostra" not in html.lower(), "sobrou texto de amostra"
    SAIDA.mkdir(exist_ok=True)
    (SAIDA / "completo.html").write_text(html, encoding="utf-8")
    import shutil
    shutil.copytree(AQUI / "fontes", SAIDA / "fontes", dirs_exist_ok=True)
    # resumo para o sumario.md
    resumo = {"paginas": len(html_pags), "secoes": pags, "niveis": []}
    for nv, dias_at in enumerate(niveis, 1):
        resumo["niveis"].append([[(a["titulo"], a["categoria"], a["tipo"], pag_de[id(a)]), (b["titulo"], b["categoria"], b["tipo"], pag_de[id(b)])]
                                 for a, b in dias_at])
    (SAIDA / "completo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=1))
    print(f"{len(html_pags)} páginas → {SAIDA / 'completo.html'}")


if __name__ == "__main__":
    main()
