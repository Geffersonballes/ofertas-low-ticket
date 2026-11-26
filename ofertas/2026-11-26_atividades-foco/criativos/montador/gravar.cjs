// Grava os quadros de um vídeo: abre o HTML do player, espera as mídias e chama render(t) quadro a quadro.
// Uso: node gravar.cjs <player.html> <pasta-quadros> <n-quadros> [fps]
const { chromium } = require('playwright');
const path = require('node:path');
const fs = require('node:fs');
(async () => {
  const [html, pasta, nStr, fpsStr] = process.argv.slice(2);
  const n = Number(nStr), fps = Number(fpsStr || 30);
  fs.mkdirSync(pasta, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 540, height: 960 }, deviceScaleFactor: 2 });
  const erros = [];
  p.on('pageerror', e => erros.push(e.message));
  p.on('requestfailed', r => erros.push('falhou: ' + r.url()));
  await p.goto('file://' + path.resolve(html));
  await p.evaluate(() => window.pronto);
  if (erros.length) { console.error(erros); process.exit(1); }
  for (let i = 0; i < n; i++) {
    await p.evaluate(t => window.render(t), i / fps);
    await p.screenshot({ path: path.join(pasta, String(i).padStart(5, '0') + '.jpg'), type: 'jpeg', quality: 90 });
  }
  await b.close();
  console.log(n + ' quadros');
})();
