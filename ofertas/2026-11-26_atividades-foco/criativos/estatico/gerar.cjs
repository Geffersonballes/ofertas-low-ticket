// Criativo 5 (férias), peça 4:5 1080x1350. Só mídia real do produto.
const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
const R=p=>'file://'+path.resolve(__dirname,p);
const html=`<meta charset=utf-8><style>
@font-face{font-family:B;src:url(${R('../../pagina/fontes/Baloo2.woff2')})}@font-face{font-family:N;src:url(${R('../../pagina/fontes/Nunito.woff2')})}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;background:#fff7f1;font-family:N;position:relative;overflow:hidden}
.top{padding:70px 70px 0;text-align:center}h1{font-family:B;font-weight:800;font-size:92px;line-height:1;color:#1d1d1f}
h2{font-size:42px;font-weight:800;color:#b93f0c;margin-top:18px}
.pg{position:absolute;width:300px;box-shadow:0 18px 40px rgba(0,0,0,.18);border-radius:6px;background:#fff}
.capa{position:absolute;left:30px;top:420px;width:620px}
.plano{position:absolute;left:90px;bottom:170px;display:flex;align-items:center;gap:22px}
.plano img{width:170px;box-shadow:0 10px 24px rgba(0,0,0,.15);border-radius:4px}.plano b{font-family:B;font-size:40px;color:#1d1d1f}
.rod{position:absolute;left:0;right:0;bottom:0;height:120px;background:#ff7a45;color:#fff;font-family:B;font-weight:800;font-size:46px;display:flex;align-items:center;justify-content:center}
</style>
<div class=top><h1>Férias. O que tem<br>para fazer hoje?</h1><h2>30 dias de atividades prontas para imprimir</h2></div>
<img class=pg src="${R('../montador/cache/pag-078.png')}" style="right:60px;top:430px;transform:rotate(9deg)">
<img class=pg src="${R('../montador/cache/pag-008.png')}" style="right:150px;top:440px;transform:rotate(3deg)">
<img class=pg src="${R('../montador/cache/pag-007.png')}" style="right:250px;top:455px;transform:rotate(-4deg)">
<img class=capa src="${R('../../pagina/img/mockup-capa.png')}">
<div class=plano><img src="${R('../montador/cache/pag-005.png')}"><b>Plano de 30 dias<br>2 folhas por dia</b></div>
<div class=rod>4 a 10 anos · 2 níveis · R$ 37,00</div>`;
(async()=>{const a=path.join(__dirname,'_p.html');fs.writeFileSync(a,html);const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto('file://'+a,{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);
await p.screenshot({path:path.join(__dirname,'anuncio-5-ferias-4x5.jpg'),type:'jpeg',quality:90});await b.close();fs.unlinkSync(a);})();
