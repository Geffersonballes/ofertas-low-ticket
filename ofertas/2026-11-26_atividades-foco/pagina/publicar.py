"""Copia a página para publicado/<slug>/ preenchendo os dados de dados.json.
Uso: python3 publicar.py   (depois: git add publicado/<slug> && git push origin main → no ar em até 60 s)
Dados ainda vazios em dados.json ficam visíveis como {{CHAVE}}, exceto o checkout,
que aponta para o bloco de preço (#preco) enquanto não existir — nunca para um link quebrado."""
import json
import pathlib
import shutil

AQUI = pathlib.Path(__file__).parent
RAIZ = AQUI.parents[2]
dados = json.loads((AQUI / "dados.json").read_text(encoding="utf-8"))
DEST = RAIZ / "publicado" / dados["slug"]

PAGINAS = ["index.html", "privacidade.html", "termos.html"]
IMAGENS = ["heroi.webp", "mockup-capa.webp", "mockup-pacote.webp", "mockup-pacote.png", "folheando.mp4", "folheando-poster.jpg",
           "amostra-nivel1.jpg", "amostra-nivel2.jpg"] + [f"dentro-{i}.jpg" for i in range(1, 7)]
FONTES = ["Baloo2.woff2", "Nunito.woff2", "LICENCA.md"]

(DEST / "img").mkdir(parents=True, exist_ok=True)
(DEST / "fontes").mkdir(exist_ok=True)
valores = dict(dados["campos"])
if not valores.get("LINK_CHECKOUT"):
    valores["LINK_CHECKOUT"] = "#preco"
pendentes = set()
for nome in PAGINAS:
    html = (AQUI / nome).read_text(encoding="utf-8")
    for chave, valor in valores.items():
        if valor:
            html = html.replace("{{" + chave + "}}", valor)
        elif "{{" + chave + "}}" in html:
            pendentes.add(chave)
    (DEST / nome).write_text(html, encoding="utf-8")
for f in IMAGENS:
    shutil.copy2(AQUI / "img" / f, DEST / "img" / f)
for f in FONTES:
    shutil.copy2(AQUI / "fontes" / f, DEST / "fontes" / f)
print(f"publicado/{dados['slug']}/ atualizado · pendentes: {sorted(pendentes) or 'nenhum'}"
      + ("" if dados["campos"].get("LINK_CHECKOUT") else " · checkout ainda não existe (botões → #preco)"))
