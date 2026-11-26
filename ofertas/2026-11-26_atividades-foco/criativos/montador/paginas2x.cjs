// Fotografa páginas do caderno completo em 2x (para ficarem nítidas no vídeo 1080x1920).
// Uso: node paginas2x.cjs 5 6 7 ...   → cache/pag-005.png ...
const { chromium } = require('playwright');
const path = require('node:path');
(async () => {
  const nums = process.argv.slice(2).map(Number);
  const html = path.resolve(__dirname, '../../produto/gerador/saida/completo.html');
  const b = await chromium.launch();
  const p = await b.newPage({ deviceScaleFactor: 2 });
  await p.goto('file://' + html);
  await p.evaluate(() => document.fonts.ready);
  await p.emulateMedia({ media: 'print' });
  const secs = await p.$$('section.pagina');
  for (const n of nums) {
    await secs[n - 1].screenshot({ path: path.join(__dirname, 'cache', `pag-${String(n).padStart(3, '0')}.png`) });
  }
  await b.close();
  console.log(nums.length + ' páginas em 2x');
})();
