"""Gera o HTML das telas do tutorial (1920×1080). Uma página com todas as telas; o render.cjs
fotografa cada estado (capítulo × nº de passos visíveis)."""
import json
import pathlib

from capitulos import CAPITULOS

AQUI = pathlib.Path(__file__).parent
RAIZ = AQUI.parents[1]
FONTES = RAIZ / "ofertas/2026-11-26_atividades-foco/pagina/fontes"
IMG_PAGINA = pathlib.Path("/tmp/claude-0/-home-user/2250d25c-d581-568f-b4e4-6cb893f20944/scratchpad/design-r1/celular-dobra.png")
if not IMG_PAGINA.exists():
    IMG_PAGINA = RAIZ / "ofertas/2026-11-26_atividades-foco/pagina/img/mockup-capa.png"

CSS = f"""
@font-face{{font-family:'Baloo 2';font-weight:400 800;src:url('{(FONTES/'Baloo2.woff2').as_uri()}') format('woff2')}}
@font-face{{font-family:'Nunito';font-weight:200 1000;src:url('{(FONTES/'Nunito.woff2').as_uri()}') format('woff2')}}
:root{{--lar:#ff7a45;--lar-esc:#cf4a12;--creme:#fff7f1;--tinta:#1d1d1f;--cinza:#6b6b70;--azul:#2357c6;--azul-cl:#e6eefc;--borda:#eadfd6;--verde:#1f7a4a;--verde-cl:#e3f4ea;--verm:#c0392b;--verm-cl:#fbe6e3}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1920px;height:1080px;overflow:hidden;background:var(--creme);font-family:'Nunito',sans-serif;color:var(--tinta)}}
.tela{{position:absolute;inset:0;display:none;padding:70px 90px 90px;grid-template-columns:820px 1fr;gap:70px}}
.tela.on{{display:grid}}
.esq{{display:flex;flex-direction:column;gap:22px}}
.eyebrow{{font-weight:800;letter-spacing:3px;text-transform:uppercase;color:var(--lar-esc);font-size:24px}}
h1{{font-family:'Baloo 2';font-weight:800;font-size:66px;line-height:1.02}}
ol{{list-style:none;display:flex;flex-direction:column;gap:18px;margin-top:14px}}
ol li{{display:grid;grid-template-columns:56px 1fr;gap:18px;align-items:center;font-size:31px;font-weight:700;line-height:1.25;transition:none}}
ol li .n{{width:56px;height:56px;border-radius:50%;background:var(--tinta);color:#fff;font-family:'Baloo 2';font-weight:800;font-size:30px;display:grid;place-items:center;padding-top:3px}}
ol li.oculto{{opacity:0}}
ol li.atual .n{{background:var(--lar)}}
ol li.atual{{color:var(--tinta)}}
ol li.passado{{color:#55555a}}
.dir{{position:relative;display:flex;align-items:center;justify-content:center}}
.rodape{{position:absolute;left:90px;right:90px;bottom:34px;display:flex;justify-content:space-between;align-items:center;font-size:20px;color:var(--cinza);font-weight:700}}
.rodape b{{color:var(--tinta)}} .rodape b i{{color:var(--lar);font-style:normal}}
.dots{{display:flex;gap:10px}} .dots span{{width:14px;height:14px;border-radius:50%;background:#e2d6cc}} .dots span.on{{background:var(--lar)}}
.selo-ilu{{position:absolute;top:-6px;right:0;background:#fff;border:2px dashed var(--cinza);color:var(--cinza);font-weight:800;font-size:18px;border-radius:999px;padding:4px 14px;letter-spacing:1px;text-transform:uppercase}}
.card{{background:#fff;border:2px solid var(--borda);border-radius:26px;box-shadow:0 18px 40px rgba(80,40,10,.10)}}
.janela{{width:900px;background:#fff;border-radius:22px;border:2px solid var(--borda);box-shadow:0 18px 40px rgba(80,40,10,.12);overflow:hidden}}
.janela .barra{{height:46px;background:#f1ece7;display:flex;align-items:center;gap:10px;padding:0 18px;font-size:18px;color:var(--cinza);font-weight:700}}
.janela .barra i{{width:13px;height:13px;border-radius:50%;background:#d9cfc6;display:inline-block}}
.janela .corpo{{padding:26px 30px;display:flex;flex-direction:column;gap:16px}}
.chip{{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:8px 18px;font-weight:800;font-size:22px;border:2px solid var(--tinta);background:#fff}}
.chip.lar{{background:var(--lar);border-color:var(--lar);color:#fff}}
.chip.azul{{background:var(--azul-cl);border-color:var(--azul);color:var(--azul)}}
table{{border-collapse:collapse;width:100%;font-size:23px}}
th,td{{text-align:left;padding:11px 14px;border-bottom:2px solid #f0e8e1}}
th{{font-size:18px;text-transform:uppercase;letter-spacing:1px;color:var(--cinza)}}
td.num{{font-family:'Baloo 2';font-weight:800;font-size:28px;text-align:right}}
tr.top td{{background:#fff1e8}}
.big{{font-family:'Baloo 2';font-weight:800}}
"""


def tela_html(c, total):
    passos = "".join(f'<li data-i="{i}"><span class="n">{i + 1}</span><span>{p}</span></li>' for i, p in enumerate(c["passos"]))
    dots = "".join(f'<span class="{"on" if k + 1 <= c["id"] else ""}"></span>' for k in range(total))
    return f"""<section class="tela" id="c{c['id']}">
  <div class="esq"><div class="eyebrow">{c['eyebrow']}</div><h1>{c['titulo']}</h1><ol>{passos}</ol></div>
  <div class="dir">{ILUSTRACOES[c['ilustracao']]()}</div>
  <div class="rodape"><b>Tutorial de mineração · <i>Operação Low Ticket</i></b><div class="dots">{dots}</div></div>
</section>"""


def ilu_papeis():
    return """<div style="display:flex;flex-direction:column;gap:30px;width:860px">
  <div style="display:flex;gap:14px;flex-wrap:wrap"><span class="chip lar">R$ 19 a R$ 67</span><span class="chip">Anúncio na Meta</span><span class="chip">Sem expert</span><span class="chip">Modelo que já vende nos EUA</span></div>
  <div style="display:grid;grid-template-columns:1fr 70px 1fr;align-items:center">
    <div class="card" style="padding:30px;background:var(--azul-cl);border-color:var(--azul)"><div style="font-weight:800;color:var(--azul);font-size:22px;text-transform:uppercase;letter-spacing:2px">Minerador</div><div class="big" style="font-size:46px">Marcos</div><div style="font-size:26px;font-weight:700;margin-top:8px">Etapas 1 e 2: acha a oferta e monta o plano</div></div>
    <div class="big" style="font-size:60px;text-align:center;color:var(--lar)">→</div>
    <div class="card" style="padding:30px;background:#ffe6d6;border-color:var(--lar)"><div style="font-weight:800;color:var(--lar-esc);font-size:22px;text-transform:uppercase;letter-spacing:2px">Operador</div><div class="big" style="font-size:46px">Gefferson</div><div style="font-size:26px;font-weight:700;margin-top:8px">Etapas 3 a 7: produz, publica e vende</div></div>
  </div>
  <div class="card" style="padding:22px 28px;font-size:25px;font-weight:700">A entrega entre vocês é um <span style="color:var(--lar-esc)">pacote de oferta</span>, num pull request no GitHub.</div>
</div>"""


def ilu_preparo():
    return """<div style="display:flex;flex-direction:column;gap:30px;position:relative;padding-top:30px"><span class="selo-ilu">ilustração</span>
  <div class="janela"><div class="barra"><i></i><i></i><i></i>&nbsp; github.com · ofertas-low-ticket · Settings › Collaborators</div>
   <div class="corpo"><div style="display:flex;justify-content:space-between;align-items:center;font-size:26px;font-weight:700"><span>👤 usuário do Marcos</span><span class="chip azul">Write</span></div>
   <div style="font-size:20px;color:var(--cinza);font-weight:700">O convite chega por e-mail · aceite para liberar</div></div></div>
  <div class="janela"><div class="barra"><i></i><i></i><i></i>&nbsp; claude.ai/code</div>
   <div class="corpo"><div style="font-size:22px;color:var(--cinza);font-weight:700">Repositório</div>
   <div style="font-size:30px;font-weight:800">Geffersonballes/ofertas-low-ticket</div>
   <div style="font-size:20px;color:var(--cinza);font-weight:700">Agentes e skills (como <b>pacote-de-oferta</b>) já vêm no repositório</div></div></div>
</div>"""


def ilu_nota():
    linhas = [("Escala (anúncios ativos)", 5), ("Tempo no ar", 5), ("Dor", 4), ("Facilidade de produção", 4), ("Potencial de order bumps", 5), ("Encaixe no Brasil", 4)]
    tr = "".join(f"<tr><td>{a}</td><td class='num'>{b}</td></tr>" for a, b in linhas)
    return f"""<div class="card" style="width:860px;padding:30px 34px">
  <div style="font-size:22px;font-weight:800;color:var(--cinza);text-transform:uppercase;letter-spacing:2px">Nota de 0 a 30 · exemplo real: NeuroKids</div>
  <table style="margin-top:12px"><tr><th>Critério</th><th style="text-align:right">0–5</th></tr>{tr}
  <tr class="top"><td style="font-weight:800">Total</td><td class="num" style="color:var(--lar-esc)">27</td></tr></table>
  <div style="margin-top:16px;display:flex;gap:12px"><span class="chip lar">Boa: 22 ou mais</span><span class="chip">Fonte: mineracao/2026-11-26.md</span></div>
</div>"""


def ilu_biblioteca():
    return """<div style="position:relative;padding-top:30px"><span class="selo-ilu">ilustração</span>
 <div class="janela"><div class="barra"><i></i><i></i><i></i>&nbsp; facebook.com/ads/library</div>
  <div class="corpo">
   <div style="display:flex;gap:12px;flex-wrap:wrap"><span class="chip">Mundo todo ▾</span><span class="chip">Todos os anúncios ▾</span><span class="chip azul">Ativos</span></div>
   <div style="border:2px solid var(--borda);border-radius:14px;padding:12px 18px;font-size:24px;font-weight:700;color:var(--cinza)">🔍 printable</div>
   <div class="card" style="padding:20px 24px;border-radius:18px;box-shadow:none">
     <div style="display:flex;justify-content:space-between;font-size:22px;font-weight:800"><span>NeuroKids</span><span style="color:var(--verde)">● Ativo</span></div>
     <div style="font-size:21px;color:var(--cinza);font-weight:700;margin-top:4px">Em veiculação desde 20 de mai de 2026</div>
     <div style="margin-top:12px;height:150px;border-radius:12px;background:repeating-linear-gradient(45deg,#f3ece6,#f3ece6 14px,#ebe2da 14px,#ebe2da 28px)"></div>
   </div>
   <div style="font-size:20px;color:var(--cinza);font-weight:700">Anote: nº de anúncios ativos · data do mais antigo ainda ativo · 3 a 5 prints</div>
  </div></div></div>"""


def ilu_rotina():
    return """<div style="display:flex;flex-direction:column;gap:22px;width:900px;position:relative;padding-top:30px"><span class="selo-ilu">ilustração</span>
 <div style="align-self:flex-end;background:var(--tinta);color:#fff;border-radius:22px 22px 6px 22px;padding:16px 24px;font-size:26px;font-weight:700">monte o próximo pacote de oferta</div>
 <div class="card" style="padding:18px 24px;border-radius:22px 22px 22px 6px">
   <div style="font-size:20px;font-weight:800;color:var(--cinza)">Claude · 3 melhores candidatas</div>
   <table><tr><th>Oferta</th><th style="text-align:right">Nota</th></tr>
   <tr class="top"><td>NeuroKids</td><td class="num">27</td></tr><tr><td>Smart Women Society</td><td class="num">26</td></tr><tr><td>Big Life Journal</td><td class="num">25</td></tr></table></div>
 <div class="janela" style="width:900px"><div class="barra"><i></i><i></i><i></i>&nbsp; github.com · Pull requests</div>
   <div class="corpo" style="padding:18px 26px"><div style="font-size:26px;font-weight:800">🟢 Pacote de oferta: &lt;nome&gt; (&lt;data&gt;)</div>
   <div style="display:flex;gap:12px"><span class="chip" style="background:var(--verde-cl);border-color:var(--verde);color:var(--verde)">Merge = aceito</span><span class="chip" style="background:var(--verm-cl);border-color:var(--verm);color:var(--verm)">Comentário = devolvido</span></div></div></div>
</div>"""


def ilu_exemplo():
    return f"""<div style="display:grid;grid-template-columns:1fr 360px;gap:34px;align-items:center;width:900px">
 <div style="display:flex;flex-direction:column;gap:18px">
  <div class="card" style="padding:20px 24px"><div style="font-size:20px;font-weight:800;color:var(--cinza)">REFERÊNCIA (EUA)</div><div class="big" style="font-size:40px">NeuroKids</div><div style="font-size:22px;font-weight:700">548 ativos (AdManage) · US$ 29,99</div></div>
  <div class="big" style="font-size:50px;color:var(--lar);text-align:center">↓</div>
  <div class="card" style="padding:20px 24px;background:#ffe6d6;border-color:var(--lar)"><div style="font-size:20px;font-weight:800;color:var(--lar-esc)">NOSSA VERSÃO</div><div class="big" style="font-size:40px">Dez Minutinhos</div><div style="font-size:22px;font-weight:700">R$ 37 · 120 atividades · 7 order bumps</div></div>
 </div>
 <img src="{IMG_PAGINA.as_uri()}" style="width:360px;border-radius:26px;box-shadow:0 18px 40px rgba(80,40,10,.18);border:6px solid var(--tinta)">
</div>"""


def ilu_regras():
    itens = [("✓", "Modelar a estrutura", "verde"), ("✕", "Copiar texto, imagem ou nome", "verm"),
             ("✕", "Depoimento ou número inventado", "verm"), ("✕", "Promessa de saúde ou dinheiro", "verm"),
             ("✕", "Merge, publicar ou cadastrar (é do Gefferson)", "verm")]
    li = "".join(f"""<div class="card" style="padding:18px 24px;display:flex;gap:18px;align-items:center;background:var(--{c}-cl);border-color:var(--{c})">
      <span class="big" style="font-size:42px;color:var(--{c});width:40px;text-align:center">{s}</span><span style="font-size:27px;font-weight:800">{t}</span></div>""" for s, t, c in itens)
    return f'<div style="display:flex;flex-direction:column;gap:16px;width:860px">{li}</div>'


def ilu_checklist():
    itens = ["Pasta ofertas/AAAA-MM-DD_nome/ com status.md", "Nº de ativos e data conferidos + 3 a 5 prints",
             "dossie.md completo", "briefing.md completo", "Procura no Brasil (links)", "Nota ≥ 22, sem corte reprovado"]
    li = "".join(f'<div style="display:flex;gap:16px;align-items:center;font-size:27px;font-weight:700"><span style="width:34px;height:34px;border:4px solid var(--azul);border-radius:8px;display:inline-block"></span>{t}</div>' for t in itens)
    return f"""<div style="display:flex;flex-direction:column;gap:26px;width:860px">
 <div class="card" style="padding:28px 32px;display:flex;flex-direction:column;gap:16px">{li}</div>
 <div style="display:flex;gap:14px"><span class="chip lar">3 a 5 candidatas por dia</span><span class="chip">1 pacote a cada 1–2 dias</span></div></div>"""


ILUSTRACOES = dict(papeis=ilu_papeis, preparo=ilu_preparo, nota=ilu_nota, biblioteca=ilu_biblioteca,
                   rotina=ilu_rotina, exemplo=ilu_exemplo, regras=ilu_regras, checklist=ilu_checklist)

JS = """
function mostrar(id, k){
  document.querySelectorAll('.tela').forEach(t=>t.classList.toggle('on', t.id==='c'+id));
  document.querySelectorAll('#c'+id+' ol li').forEach(li=>{
    const i=+li.dataset.i; li.classList.toggle('oculto', i>k); li.classList.toggle('atual', i===k); li.classList.toggle('passado', i<k);
  });
}
"""


def main():
    total = len(CAPITULOS)
    html = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body>{''.join(tela_html(c, total) for c in CAPITULOS)}<script>{JS}</script></body></html>"""
    (AQUI / "telas.html").write_text(html, encoding="utf-8")
    (AQUI / "estados.json").write_text(json.dumps([{"id": c["id"], "n": len(c["passos"])} for c in CAPITULOS]))
    print("telas.html ok")


if __name__ == "__main__":
    main()
