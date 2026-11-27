// Gera foto de perfil (720x720) e capa (1640x624) da Página do Facebook "Dez Minutinhos".
const {chromium}=require('playwright');const path=require('path');
const F='file://'+path.resolve(__dirname,'../pagina/fontes/');
const css=`@font-face{font-family:B;src:url(${F}/Baloo2.woff2)}@font-face{font-family:N;src:url(${F}/Nunito.woff2)}
*{margin:0;box-sizing:border-box}body{font-family:N}`;
const MOCK='file://'+path.resolve(__dirname,'../pagina/img/mockup-pacote.png');
const perfil=`<style>${css}body{width:720px;height:720px;background:#ff7a45;display:grid;place-items:center}
.c{width:520px;height:520px;border-radius:50%;background:#fff7f1;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 16px 0 #cf4a12}
.n{font-family:B;font-weight:800;font-size:200px;line-height:.8;color:#ff7a45}.t{font-family:B;font-weight:800;font-size:64px;color:#1d1d1f;line-height:1;margin-top:18px}
.r{width:150px;height:14px;border-radius:7px;background:#ffc93c;margin-top:18px}</style>
<div class=c><div class=n>10</div><div class=t>minutinhos</div><div class=r></div></div>`;
const capa=`<style>${css}body{width:1640px;height:624px;background:#fff7f1;position:relative;overflow:hidden}
.b{position:absolute;border-radius:50%}.t{position:absolute;left:210px;top:160px;width:660px}
h1{font-family:B;font-weight:800;font-size:78px;line-height:.98;color:#1d1d1f}h1 span{color:#ff7a45}
p{font-size:32px;color:#5a5a62;margin-top:22px;font-weight:700}
img{position:absolute;right:190px;top:70px;height:480px}</style>
<div class=b style="width:520px;height:520px;background:#ffe6d6;right:170px;top:62px"></div>
<div class=b style="width:120px;height:120px;background:#ffc93c;left:90px;top:430px"></div>
<div class=b style="width:70px;height:70px;background:#8fd3a8;left:930px;top:60px"></div>
<div class=t><h1>Atividades de <span>10 minutinhos</span> para imprimir</h1><p>Para crianças de 4 a 10 anos · sem tela</p></div>
<img src="${MOCK}">`;
(async()=>{const b=await chromium.launch();
for(const [n,h,w,ht] of [['perfil',perfil,720,720],['capa',capa,1640,624]]){
const fs=require('fs');const arq=path.join(__dirname,`_${n}.html`);fs.writeFileSync(arq,'<meta charset=utf-8>'+h);const p=await b.newPage({viewport:{width:w,height:ht}});await p.goto('file://'+arq,{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
await p.screenshot({path:path.join(__dirname,`facebook-${n}.png`)});await p.close();fs.unlinkSync(arq);}
await b.close();})();
