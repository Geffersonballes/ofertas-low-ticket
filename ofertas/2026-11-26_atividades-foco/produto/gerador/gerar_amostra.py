"""Gera o caderno-amostra do Dez Minutinhos em HTML (A4). O PDF sai do render.mjs.
Uso: python3 gerar_amostra.py  → saida/amostra.html"""
import pathlib
import random

import atividades as A
from icones import icone

AQUI = pathlib.Path(__file__).parent
SAIDA = AQUI / "saida"
SEMENTE = 2611  # mesma semente = mesmo caderno

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
:root { --laranja:#ff7a45; --tinta:#1d1d1f; --cinza:#6b6b70; --fundo:#fff7f1; }
body { font-family: 'Nunito', sans-serif; color: var(--tinta); background: #e9e9e9; }
.pagina { width: 210mm; height: 297mm; background: #fff; position: relative; overflow: hidden;
  page-break-after: always; break-after: page; padding: 12mm 14mm 10mm; display: flex; flex-direction: column; }
@media screen { .pagina { margin: 8mm auto; box-shadow: 0 2px 10px rgba(0,0,0,.12); } }
.topo { display: flex; align-items: center; justify-content: space-between; border-bottom: .6mm solid var(--tinta); padding-bottom: 2.5mm; }
.marca { font-family: 'Baloo 2'; font-weight: 800; font-size: 11pt; letter-spacing: .2pt; }
.marca b { color: var(--laranja); }
.selos { display: flex; gap: 2mm; }
.selo { font-weight: 800; font-size: 8.5pt; border: .35mm solid var(--tinta); border-radius: 10mm; padding: .6mm 3mm; }
.selo.n1 { background: #fff1e8; } .selo.n2 { background: #e8f0ff; }
h1 { font-family: 'Baloo 2'; font-weight: 800; font-size: 25pt; line-height: 1.05; margin-top: 4mm; }
.instrucao { font-size: 11.5pt; font-weight: 700; color: #333; margin-top: 1.5mm; min-height: 11mm; }
.area { flex: 1; display: flex; align-items: flex-start; justify-content: center; margin-top: 3mm; }
.area svg { width: 182mm; height: 228mm; }
.rodape { display: flex; justify-content: space-between; align-items: center; font-size: 8.5pt; color: var(--cinza);
  border-top: .3mm solid #ccc; padding-top: 2mm; }
.rodape .feito { display: flex; gap: 5mm; align-items: center; font-weight: 700; color: var(--tinta); }
.caixa { display: inline-block; width: 4mm; height: 4mm; border: .35mm solid var(--tinta); border-radius: .8mm; vertical-align: -0.8mm; margin-left: 1mm; }
/* capa */
.capa { background: var(--fundo); padding: 0; }
.capa .faixa { background: var(--laranja); height: 16mm; }
.capa .miolo { padding: 18mm 18mm 0; flex: 1; display: flex; flex-direction: column; }
.capa .titulo { font-family: 'Baloo 2'; font-weight: 800; font-size: 62pt; line-height: .92; margin-top: 4mm; }
.capa .titulo span { color: var(--laranja); }
.capa .sub { font-size: 16pt; font-weight: 700; margin-top: 6mm; max-width: 150mm; line-height: 1.3; }
.capa .tag { display: inline-block; margin-top: 8mm; font-weight: 800; font-size: 11pt; background: var(--tinta); color: #fff; padding: 1.5mm 4mm; border-radius: 2mm; }
.capa .figuras { margin-top: auto; }
.capa .base { padding: 6mm 18mm 10mm; display: flex; justify-content: space-between; font-weight: 700; font-size: 10pt; }
/* como usar */
.texto { font-size: 12pt; line-height: 1.5; }
.texto h2 { font-family: 'Baloo 2'; font-weight: 800; font-size: 16pt; margin: 7mm 0 2mm; }
.passos { list-style: none; counter-reset: p; }
.passos li { counter-increment: p; position: relative; padding-left: 11mm; margin: 3mm 0; }
.passos li::before { content: counter(p); position: absolute; left: 0; top: -.5mm; width: 7.5mm; height: 7.5mm; border-radius: 50%;
  background: var(--laranja); color: #fff; font-family: 'Baloo 2'; font-weight: 800; text-align: center; line-height: 8mm; }
table.niveis { width: 100%; border-collapse: collapse; margin-top: 2mm; font-size: 11pt; }
table.niveis td, table.niveis th { border: .3mm solid #bbb; padding: 2mm 3mm; text-align: left; vertical-align: top; }
table.niveis th { background: #f4f4f4; }
.aviso { margin-top: 7mm; font-size: 10pt; color: var(--cinza); border-left: 1.2mm solid var(--laranja); padding-left: 4mm; }
/* gabarito */
.gab { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4mm; margin-top: 5mm; align-content: start; flex: 1; }
.gab .card { border: .3mm solid #ccc; border-radius: 2mm; padding: 2mm; }
.gab .card h3 { font-family: 'Baloo 2'; font-weight: 800; font-size: 10pt; line-height: 1.1; }
.gab .card p { font-size: 8.5pt; color: var(--cinza); }
.gab .card svg { width: 100%; height: auto; display: block; margin-top: 1mm; }
"""


def svg(conteudo, w=A.W, h=A.H):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{conteudo}</svg>'


def selo(nivel):
    return (f'<span class="selo n1">Nível 1 · 4 a 6 anos</span>' if nivel == 1
            else f'<span class="selo n2">Nível 2 · 7 a 10 anos</span>')


def pagina_atividade(at, num, dia):
    return f"""<section class="pagina">
  <div class="topo"><div class="marca">Dez <b>Minutinhos</b></div>
    <div class="selos"><span class="selo">{at['categoria']}</span>{selo(at['nivel'])}</div></div>
  <h1>{at['titulo']}</h1>
  <p class="instrucao">{at['instrucao']}</p>
  <div class="area">{svg(at['svg'])}</div>
  <div class="rodape"><span>Caderno-amostra · página {num}</span>
    <span class="feito">Dia {dia} <span>Feito!<span class="caixa"></span></span></span></div>
</section>"""


def capa():
    itens = [("estrela", -8), ("peixe", 0), ("balao", 6), ("sol", 0), ("flor", -6), ("casa", 0), ("maca", 4), ("barco", 0)]
    fig = ""
    for i, (n, g) in enumerate(itens):
        cx, cy = 24 + (i % 4) * 45, 22 + (i // 4) * 44 + (12 if i % 2 else 0)
        fig += f'<circle cx="{cx}" cy="{cy}" r="19" fill="#ffe1cf"/>' + icone(n, cx - 15, cy - 15, 30, girar=g)
    return f"""<section class="pagina capa"><div class="faixa"></div>
  <div class="miolo">
    <div class="marca" style="font-size:13pt">Caderno de atividades para imprimir</div>
    <div class="titulo">Dez<br><span>Minutinhos</span></div>
    <p class="sub">Labirintos, memória, padrões e lógica para fazer com lápis e papel, longe da tela.</p>
    <div><span class="tag">CADERNO-AMOSTRA · 13 ATIVIDADES · 2 NÍVEIS</span></div>
    <div class="figuras">{svg(fig, 182, 112)}</div>
  </div>
  <div class="base"><span>Nível 1 · 4 a 6 anos &nbsp;|&nbsp; Nível 2 · 7 a 10 anos</span><span>Gabarito no final</span></div>
</section>"""


def como_usar():
    return """<section class="pagina">
  <div class="topo"><div class="marca">Dez <b>Minutinhos</b></div><div class="selos"><span class="selo">Para o adulto</span></div></div>
  <h1>Como usar</h1>
  <div class="texto">
  <ol class="passos">
    <li><b>Imprima só a folha do dia.</b> Funciona em preto e branco, em papel comum A4.</li>
    <li><b>Escolha o nível pela idade,</b> não pela série. Se ficar fácil demais, passe para o Nível 2.</li>
    <li><b>Leia a instrução em voz alta</b> e deixe a criança tentar sozinha antes de ajudar.</li>
    <li><b>Dez minutinhos bastam.</b> Se não terminar, tudo bem: guarde e continue amanhã.</li>
    <li><b>Marque "Feito!"</b> no rodapé. O gabarito está nas últimas páginas.</li>
  </ol>
  <h2>Os dois níveis</h2>
  <table class="niveis">
    <tr><th>Nível</th><th>Idade</th><th>Como é</th></tr>
    <tr><td><b>1</b></td><td>4 a 6 anos</td><td>Sem leitura. Figuras grandes, traço grosso, poucas etapas.</td></tr>
    <tr><td><b>2</b></td><td>7 a 10 anos</td><td>Leitura inicial, números e regras com mais passos.</td></tr>
  </table>
  <h2>Do que você vai precisar</h2>
  <p>Lápis, borracha e lápis de cor. Tesoura e cola só nas atividades de recortar.</p>
  <p class="aviso">Este é um caderno-amostra com 13 atividades. O caderno completo traz 120 atividades
  (60 por nível) e um plano de 30 dias.</p>
  </div>
  <div class="rodape"><span>Caderno-amostra · página 2</span><span></span></div>
</section>"""


def paginas_gabarito(lista, num_ini):
    cards = []
    for num, at in lista:
        corpo = svg(at["gabarito_svg"]) if at.get("gabarito_svg") else f"<p>{at['gabarito_txt']}</p>"
        cards.append(f'<div class="card"><h3>Pág. {num} · {at["titulo"]}</h3>{corpo}</div>')
    pags = []
    for i in range(0, len(cards), 6):
        pags.append(f"""<section class="pagina">
  <div class="topo"><div class="marca">Dez <b>Minutinhos</b></div><div class="selos"><span class="selo">Gabarito</span></div></div>
  <h1>Gabarito</h1>
  <div class="gab">{''.join(cards[i:i + 6])}</div>
  <div class="rodape"><span>Caderno-amostra · página {num_ini + len(pags)}</span><span></span></div>
</section>""")
    return pags


def main():
    rng = random.Random(SEMENTE)
    lista = [
        A.labirinto(1, rng), A.padroes(rng), A.diferente(rng), A.contar(rng), A.ligue_pontos(rng), A.tracado(rng),
        A.labirinto(2, rng), A.sudoku(rng), A.caca_palavras(rng), A.codigo_secreto(rng), A.sete_erros(rng),
        A.grade_logica(rng), A.sequencias(rng),
    ]
    paginas = [capa(), como_usar()]
    numeradas = []
    for i, at in enumerate(lista):
        num = 3 + i
        numeradas.append((num, at))
        paginas.append(pagina_atividade(at, num, i + 1))
    paginas += paginas_gabarito(numeradas, 3 + len(lista))
    fontes = (AQUI / "fontes" / "fontes.css").read_text()
    html = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Dez Minutinhos — caderno-amostra</title><style>{fontes}{CSS}</style></head>
<body>{''.join(paginas)}</body></html>"""
    SAIDA.mkdir(exist_ok=True)
    (SAIDA / "amostra.html").write_text(html, encoding="utf-8")
    import shutil
    shutil.copytree(AQUI / "fontes", SAIDA / "fontes", dirs_exist_ok=True)
    print(f"{len(paginas)} páginas, {len(lista)} atividades → {SAIDA / 'amostra.html'}")


if __name__ == "__main__":
    main()
