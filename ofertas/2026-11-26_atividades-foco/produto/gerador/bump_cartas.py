"""Bump 3 — Cartas de conversa: 48 cartas (6 por folha A4, com linhas de corte) com perguntas leves
para a família, em 4 categorias de 12. Sem tema sensível, sem aparência/peso/medos, sem "lição"."""
import gerar_amostra as GA
from bumps_base import Bump
from icones import icone

BUMP = Bump("Cartas de conversa", "cartas-de-conversa", "48 CARTAS PARA RECORTAR")

CATEGORIAS = [
    ("MEU DIA", "sol", [
        "Qual foi a melhor parte do seu dia hoje?",
        "O que te fez rir hoje?",
        "Você aprendeu alguma coisa nova hoje? O quê?",
        "Com quem você brincou hoje? Do que vocês brincaram?",
        "Qual foi a coisa mais gostosa que você comeu hoje?",
        "Se o seu dia fosse uma cor, que cor seria?",
        "Você ajudou alguém hoje? Como foi?",
        "O que você quer fazer amanhã?",
        "Qual foi o momento mais tranquilo do seu dia?",
        "Qual é a lembrança mais divertida das últimas férias?",
        "Qual foi o passeio mais legal que a gente já fez junto?",
        "Conte uma coisa boa que aconteceu esta semana.",
    ]),
    ("IMAGINAÇÃO", "balao", [
        "Se você pudesse inventar um bicho, como ele seria?",
        "Como seria uma casa construída em cima de uma nuvem?",
        "Invente um nome para um planeta novo. Quem mora lá?",
        "Se os brinquedos conversassem à noite, sobre o que falariam?",
        "Invente um monstro bonzinho. Qual é o nome dele?",
        "Como seria uma escola no fundo do mar?",
        "Se você tivesse uma máquina de inventar, o que ela faria?",
        "Invente um sabor de sorvete que ainda não existe.",
        "Qual seria o seu superpoder? Para que você usaria?",
        "Como seria um dia em que tudo fosse feito de bolo?",
        "Se você fosse personagem de um livro, qual seria a sua aventura?",
        "Invente uma dança nova e ensine para a família.",
    ]),
    ("E SE…?", "estrela", [
        "E se os gatos pudessem falar? O que um gato diria?",
        "E se a gente pudesse voar por um dia? Para onde você iria?",
        "E se você ficasse do tamanho de uma formiga?",
        "E se chovesse pipoca?",
        "E se você pudesse conversar com uma árvore? O que perguntaria?",
        "E se o dia tivesse 30 horas? O que você faria com as horas a mais?",
        "E se a gente morasse num barco?",
        "E se todos os carros virassem bicicletas gigantes?",
        "E se você acordasse dentro do seu desenho animado preferido?",
        "E se toda segunda-feira fosse dia de festa?",
        "E se você escolhesse o jantar de hoje? O que seria?",
        "E se você ganhasse um robô ajudante? O que ele faria primeiro?",
    ]),
    ("PREFERIDOS", "coracao", [
        "Qual é a sua fruta preferida? E qual você ainda quer provar?",
        "Praia ou montanha? Por quê?",
        "Qual é o seu bicho preferido? O que ele tem de especial?",
        "Qual brincadeira você nunca cansa de brincar?",
        "Qual é a música que você mais gosta de cantar?",
        "Dia de sol ou dia de chuva? O que você faz em cada um?",
        "Qual é a sua cor preferida hoje? Ela já foi outra?",
        "Qual é a sua história preferida? Conte o começo.",
        "Se pudesse escolher um passeio para amanhã, qual seria?",
        "Qual comida você comeria todo dia?",
        "Doce ou salgado? Qual é o seu preferido de cada?",
        "Qual é o seu cantinho preferido da casa? Por quê?",
    ]),
]


def gerar():
    perguntas = [q for _, _, qs in CATEGORIAS for q in qs]
    assert len(perguntas) == 48 and len(set(perguntas)) == 48
    assert all(len(qs) == 12 for _, _, qs in CATEGORIAS)
    for q in perguntas:
        assert len(q) <= 75, q
        low = q.lower()
        for veto in ("medo", "triste", "peso", "gord", "feio", "bonit", " nota ", "prova ", "brig", "chor", "morr"):
            assert veto not in low, (veto, q)
    capa = BUMP.capa("48 perguntas leves para o jantar, o carro ou a hora de dormir. Sem lição, só conversa.",
                     ("Para crianças de 4 a 10 anos e a família toda", "Recorte na linha tracejada"),
                     ["sol", "balao", "estrela", "coracao", "lua", "flor", "nuvem", "casa"])
    uso = BUMP.pagina_texto("Como usar as cartas", """
  <ol>
    <li><b>Imprima e recorte</b> nas linhas tracejadas (6 cartas por folha). Papel mais grosso dura mais, mas o comum funciona.</li>
    <li><b>Guarde num potinho</b> ou envelope perto da mesa.</li>
    <li><b>Na hora do jantar, no carro ou antes de dormir,</b> alguém tira uma carta e lê. Todo mundo responde, adultos também.</li>
  </ol>
  <h2>Quatro tipos de carta</h2>
  <ul>
    <li><b>Meu dia:</b> sobre o que aconteceu hoje e lembranças boas.</li>
    <li><b>Imaginação:</b> para inventar coisas.</li>
    <li><b>E se…?</b> situações malucas para pensar junto.</li>
    <li><b>Preferidos:</b> do que cada um gosta.</li>
  </ul>
  <h2>Dicas</h2>
  <ul>
    <li>Não existe resposta certa. Vale responder com um desenho no ar ou com mímica.</li>
    <li>Quem não quiser responder pode passar a vez.</li>
    <li>Para os pequenos, o adulto lê a pergunta em voz alta.</li>
  </ul>
  <p class="aviso">Uso permitido: imprima quantas vezes quiser para a sua família. Não é permitido revender nem repassar o arquivo.</p>""", 2)
    pags = [capa, uso]
    n = 0
    for nome_cat, ic, qs in CATEGORIAS:
        for k in range(0, 12, 6):
            cartas = ""
            for q in qs[k:k + 6]:
                n += 1
                cartas += (f'<div class="carta"><div class="cat">{nome_cat}</div>{GA.svg(icone(ic, 5, 5, 90), 100, 100)}'
                           f'<div class="q">{q}</div>' + GA.svg(icone(ic, 5, 5, 90, cor="#bbbbbb"), 100, 100).replace("<svg ", '<svg class="fundo" ')
                           + f'<div class="num">{n}/48</div></div>')
            num = len(pags) + 1
            pags.append(f"""<section class="pagina">{BUMP.topo(f'<span class="selo">{dict(zip(["MEU DIA", "IMAGINAÇÃO", "E SE…?", "PREFERIDOS"], ["Meu dia", "Imaginação", "E se…?", "Preferidos"]))[nome_cat]}</span>')}
  <div class="cartas">{cartas}</div>
  <div class="corte" style="margin-top:2mm">✂ recorte nas linhas tracejadas</div>{BUMP.rodape(num)}</section>""")
    assert n == 48
    return dict(paginas=BUMP.montar(pags), cartas=n)


if __name__ == "__main__":
    print(gerar())
