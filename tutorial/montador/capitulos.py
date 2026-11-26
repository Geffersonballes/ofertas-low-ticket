"""Roteiro do tutorial de mineração (fonte única: narração + telas).
Cada capítulo: título, narração (texto enviado ao ElevenLabs), passos que aparecem na tela
conforme a fala, e a ilustração da direita."""

CAPITULOS = [
    dict(
        id=1, eyebrow="Capítulo 1", titulo="A operação em 30 segundos",
        narracao=("Oi, Marcos. Este vídeo mostra como você vai minerar ofertas para a nossa operação. "
                  "A ideia é simples: vender infoprodutos baratos, de dezenove a sessenta e sete reais, "
                  "com anúncio no Facebook e no Instagram, sem especialista e sem seguidores. "
                  "A gente não inventa produto. A gente acha o que já vende nos Estados Unidos e cria uma versão brasileira, nossa. "
                  "O seu papel é achar a oferta e montar o plano. O Gefferson produz, publica e vende."),
        passos=["Infoprodutos de R$ 19 a R$ 67", "Anúncio na Meta, sem expert e sem seguidores",
                "Modelamos o que já vende nos EUA", "Você acha e planeja · Gefferson produz e vende"],
        ilustracao="papeis",
    ),
    dict(
        id=2, eyebrow="Capítulo 2", titulo="Preparação (uma vez só)",
        narracao=("Antes de começar, três coisas, uma vez só. "
                  "Primeiro: o Gefferson te adiciona como colaborador no GitHub, no repositório ofertas low ticket. "
                  "Segundo: na sua conta do Claude, em claude ponto ai barra code, você liga o seu GitHub e abre uma sessão nesse repositório. "
                  "Os agentes e as instruções já vêm junto. "
                  "Terceiro, opcional: instale a extensão do Claude para o Chrome. Ela ajuda a conferir a Biblioteca de Anúncios."),
        passos=["Gefferson te adiciona no GitHub (Collaborators)",
                "claude.ai/code → ligar GitHub → abrir Geffersonballes/ofertas-low-ticket",
                "Opcional: extensão do Claude para Chrome"],
        ilustracao="preparo",
    ),
    dict(
        id=3, eyebrow="Capítulo 3", titulo="O que é uma oferta boa",
        narracao=("O que é uma oferta boa? Ela passa em todos os cortes. "
                  "Pelo menos vinte anúncios ativos; as melhores têm de cinquenta a mais de cem. "
                  "Algum anúncio rodando há catorze dias ou mais, porque ninguém paga anúncio duas semanas sem vender. "
                  "Produto digital, para baixar, de até uns quarenta e sete dólares. "
                  "E oferta limpa: nada de saúde, cura, emagrecimento, dinheiro garantido, conteúdo adulto ou armas. "
                  "Depois, o Claude dá uma nota de zero a trinta. Nota boa é vinte e dois para cima."),
        passos=["≥ 20 anúncios ativos (as melhores: 48 a 112+)", "Algum anúncio ativo há 14+ dias",
                "Digital, por download, até ~US$ 47", "White: sem saúde, cura, dinheiro garantido, adulto, armas",
                "Nota 0–30 · boa ≥ 22"],
        ilustracao="nota",
    ),
    dict(
        id=4, eyebrow="Capítulo 4", titulo="Onde procurar",
        narracao=("Onde procurar? Na Biblioteca de Anúncios da Meta. "
                  "Marque Mundo todo, Todos os anúncios e só os ativos. "
                  "Busque em inglês: ebook, guide, planner, printable, template, spreadsheet, bundle. "
                  "Os nichos que mais rendem são finanças, casa, maternidade, pets, receitas, estudos e pequenos negócios. "
                  "Dica: se o link abrir vazio, busque o nome exato da página que anuncia. Aí aparecem as datas reais."),
        passos=["facebook.com/ads/library", "Mundo todo · Todos os anúncios · Ativos",
                "Buscas em inglês: ebook, guide, planner, printable, template…",
                "Link vazio? Busque o nome exato da página anunciante"],
        ilustracao="biblioteca",
    ),
    dict(
        id=5, eyebrow="Capítulo 5", titulo="A rotina com o Claude",
        narracao=("Agora, a rotina. Um: abra uma sessão no repositório e diga: monte o próximo pacote de oferta. "
                  "Dois: o Claude minera e mostra as três melhores. Você escolhe uma. "
                  "Três: confira na mão, na Biblioteca. Anote quantos anúncios estão ativos e a data do mais antigo, e salve alguns prints. "
                  "Isso é obrigatório, porque a Biblioteca bloqueia robôs. "
                  "Quatro: o Claude faz o dossiê e o briefing, e você revisa. "
                  "Cinco: o Claude abre um pul ríquest chamado Pacote de oferta. O Gefferson aceita, ou devolve com o motivo."),
        passos=["Diga: “monte o próximo pacote de oferta”", "O Claude mostra as 3 melhores · você escolhe",
                "Conferência manual na Biblioteca + 3 a 5 prints", "Dossiê e briefing · você revisa",
                "Pull request “Pacote de oferta: …” → Gefferson aceita ou devolve"],
        ilustracao="rotina",
    ),
    dict(
        id=6, eyebrow="Capítulo 6", titulo="Exemplo real: NeuroKids → Dez Minutinhos",
        narracao=("Um exemplo real. Na primeira mineração, a melhor candidata foi a NeuroKids: atividades para imprimir, "
                  "com quinhentos e quarenta e oito anúncios ativos e nota vinte e sete. "
                  "Aproveitamos o formato, os ângulos de anúncio e a ideia dos order bumps. "
                  "Não copiamos texto, imagens nem o nome. E cortamos o que não pode: falar de TDAH e prometer resultado em poucos dias. "
                  "Assim nasceu o Dez Minutinhos, com produto, página e anúncios nossos."),
        passos=["NeuroKids: 548 anúncios ativos · nota 27/30", "Modelamos: formato, ângulos, order bumps",
                "Não copiamos: texto, imagens, nome", "Cortamos: TDAH, “resultado em 3 a 7 dias”"],
        ilustracao="exemplo",
    ),
    dict(
        id=7, eyebrow="Capítulo 7", titulo="Regras de ouro",
        narracao=("Quatro regras de ouro. Modelar, nunca copiar. "
                  "Nada de prova inventada: sem depoimento, sem número de alunos. "
                  "Nada de promessa de saúde ou de dinheiro. "
                  "E você não faz merge, não publica e não cadastra nada. Isso é com o Gefferson."),
        passos=["Modelar, nunca copiar", "Nada de prova inventada", "Nada de promessa de saúde ou dinheiro",
                "Sem merge, sem publicar, sem cadastrar"],
        ilustracao="regras",
    ),
    dict(
        id=8, eyebrow="Capítulo 8", titulo="Pacote pronto e ritmo",
        narracao=("Para fechar: o pacote pronto tem a pasta da oferta, os números conferidos com prints, "
                  "o dossiê, o briefing, a prova de que tem procura no Brasil, e nota de vinte e dois para cima. "
                  "A meta é avaliar de três a cinco candidatas por dia e entregar um pacote a cada um ou dois dias. Bora minerar!"),
        passos=["Números conferidos + prints", "dossie.md e briefing.md completos",
                "Procura no Brasil comprovada · nota ≥ 22", "Meta: 3–5 candidatas/dia · 1 pacote a cada 1–2 dias"],
        ilustracao="checklist",
    ),
]

if __name__ == "__main__":
    tot = 0
    for c in CAPITULOS:
        n = len(c["narracao"]); tot += n
        print(c["id"], n, "car.", len(c["narracao"].split()), "palavras")
    print("total", tot, "car. ≈", round(tot / 15), "s")
