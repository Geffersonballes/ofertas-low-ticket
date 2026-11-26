// Fotografa cada estado das telas: quadros/c{id}-{k}.png (k = último passo visível).
const { chromium } = require('playwright');
const path = require('node:path');
const fs = require('node:fs');
(async () => {
  const estados = JSON.parse(fs.readFileSync(path.join(__dirname, 'estados.json'), 'utf8'));
  const out = path.join(__dirname, 'quadros'); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(__dirname, 'telas.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  let n = 0;
  for (const e of estados) for (let k = 0; k < e.n; k++) {
    await p.evaluate(([id, k]) => mostrar(id, k), [e.id, k]);
    await p.screenshot({ path: path.join(out, `c${e.id}-${k}.png`) }); n++;
  }
  await b.close(); console.log(n + ' quadros');
})();
