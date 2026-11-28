// Criativo 5 (férias): peça 4:5 (1080x1350) e peça 1:1 (1080x1080). Só mídia real do produto.
// As páginas vêm do PDF APROVADO (produto/final/dez-minutinhos.pdf), rasterizadas com pdftoppm:
// p. 7 (labirinto N1), p. 68 (jogo dos 7 erros N2), p. 78 (código secreto N2).
// O plano de 30 dias (p. 5) não entra como miniatura (ficava ilegível no celular): virou texto.
// Uso: node gerar.cjs   → anuncio-5-ferias-4x5.jpg e anuncio-5-ferias-1x1.jpg
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const { execFileSync } = require('child_process');

const R = p => 'file://' + path.resolve(__dirname, p);
const PDF = path.resolve(__dirname, '../../produto/final/dez-minutinhos.pdf');
const PAGS = path.resolve(__dirname, '../montador/cache/pdf');
fs.mkdirSync(PAGS, { recursive: true });
const pag = n => {
  const base = path.join(PAGS, `pag-${String(n).padStart(3, '0')}`);
  execFileSync('pdftoppm', ['-f', String(n), '-l', String(n), '-r', '150', '-png', '-singlefile', PDF, base]);
  return 'file://' + base + '.png';
};
const P7 = pag(7), P68 = pag(68), P78 = pag(78);

const base = (w, h) => `<meta charset=utf-8><style>
@font-face{font-family:B;src:url(${R('../../pagina/fontes/Baloo2.woff2')})}@font-face{font-family:N;src:url(${R('../../pagina/fontes/Nunito.woff2')})}
*{margin:0;box-sizing:border-box}body{width:${w}px;height:${h}px;background:#fff7f1;font-family:N;position:relative;overflow:hidden}
.top{padding:62px 60px 0;text-align:center}h1{font-family:B;font-weight:800;line-height:1;color:#1d1d1f}
h2{font-size:42px;font-weight:800;color:#b93f0c;margin-top:16px}
.pg{position:absolute;box-shadow:0 14px 34px rgba(0,0,0,.2);border-radius:6px;background:#fff;border:1px solid #e6dcd3}
.capa{position:absolute}
.rod{position:absolute;left:0;right:0;bottom:0;height:120px;background:#ff7a45;color:#fff;font-family:B;font-weight:800;font-size:46px;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.lista{position:absolute;font-family:B;font-weight:800;color:#1d1d1f;font-size:50px;line-height:1.15}
.lista div{display:flex;align-items:center;gap:18px;margin:10px 0}
.lista i{width:46px;height:46px;border-radius:10px;background:#ff7a45;flex:none;position:relative}
.lista i:after{content:'';position:absolute;left:15px;top:7px;width:12px;height:24px;border:solid #fff;border-width:0 6px 6px 0;transform:rotate(45deg)}
</style>`;

// 4:5 — leque aberto com as 3 páginas inteiras visíveis (título de cada atividade à mostra), capa embaixo à esquerda,
// plano em texto grande à direita.
const h45 = base(1080, 1350) + `
<div class=top><h1 style="font-size:92px">Férias. O que tem<br>para fazer hoje?</h1><h2>30 dias de atividades prontas para imprimir</h2></div>
<img class=pg src="${P7}"  style="left:52px;top:388px;width:330px;transform:rotate(-7deg)">
<img class=pg src="${P78}" style="left:698px;top:388px;width:330px;transform:rotate(7deg)">
<img class=pg src="${P68}" style="left:375px;top:362px;width:330px">
<img class=capa src="${R('../../pagina/img/mockup-capa.png')}" style="left:10px;top:805px;width:500px">
<div class=lista style="left:540px;top:930px"><div><i></i>Plano de 30 dias</div><div><i></i>2 folhas por dia</div></div>
<div class=rod>4 a 10 anos · 2 níveis · R$ 37,00</div>`;

// 1:1 — roteiro: topo com a pergunta, capa + 2 páginas (p. 7 e p. 78), rodapé com plano, idade e preço.
const h11 = base(1080, 1080) + `
<div class=top style="padding-top:56px"><h1 style="font-size:84px">Férias. O que tem<br>para fazer hoje?</h1></div>
<img class=pg src="${P7}"  style="left:515px;top:345px;width:300px;transform:rotate(-6deg)">
<img class=pg src="${P78}" style="left:700px;top:362px;width:300px;transform:rotate(6deg)">
<img class=capa src="${R('../../pagina/img/mockup-capa.png')}" style="left:15px;top:360px;width:590px">
<div class=rod style="font-size:44px">Plano de 30 dias · 4 a 10 anos · R$ 37,00</div>`;

(async () => {
  const b = await chromium.launch();
  for (const [html, w, h, nome] of [[h45, 1080, 1350, 'anuncio-5-ferias-4x5.jpg'], [h11, 1080, 1080, 'anuncio-5-ferias-1x1.jpg']]) {
    const a = path.join(__dirname, '_p.html');
    fs.writeFileSync(a, html);
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + a, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(__dirname, nome), type: 'jpeg', quality: 90 });
    await p.close();
    fs.unlinkSync(a);
    console.log(nome);
  }
  await b.close();
})();
