// Fotografa as cenas de cenas/lista.json (ou da lista passada como argumento, ex.: lista-heroi.json) (PNG; transparentes quando a cena não tem fundo).
const { chromium } = require('playwright');
const path = require('node:path');
const fs = require('node:fs');
(async () => {
  const dir = path.join(__dirname, 'cenas');
  const lista = JSON.parse(fs.readFileSync(path.join(dir, process.argv[2] || 'lista.json'), 'utf8'));
  const browser = await chromium.launch();
  for (const c of lista) {
    const page = await browser.newPage({ viewport: { width: c.w, height: c.h }, deviceScaleFactor: 1 });
    await page.goto('file://' + path.join(dir, c.nome + '.html'));
    await page.waitForLoadState('networkidle');
    await page.screenshot({ path: path.join(dir, c.nome + '.png'), omitBackground: c.transparente });
    await page.close();
  }
  await browser.close();
  console.log(lista.length + ' cenas fotografadas');
})();
