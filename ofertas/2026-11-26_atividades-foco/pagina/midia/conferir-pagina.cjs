// Fotos da página inteira no celular e no computador. Uso: node conferir-pagina.cjs <pasta-de-saida> [escala]
const { chromium } = require('playwright');
const path = require('node:path');
(async () => {
  const out = process.argv[2]; const esc = Number(process.argv[3] || 1);
  const browser = await chromium.launch();
  for (const [nome, w, h] of [['celular', 390, 844], ['computador', 1280, 800]]) {
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: esc });
    const erros = [];
    page.on('pageerror', e => erros.push(e.message));
    page.on('requestfailed', r => erros.push('falhou: ' + r.url()));
    await page.goto(process.env.URL || ('file://' + path.join(__dirname, '..', 'index.html')));
    await page.evaluate(() => document.fonts.ready);
    for (let y = 0; y < 30000; y += 600) { await page.evaluate(v => window.scrollTo(0, v), y); await page.waitForTimeout(40); }
    await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(800);
    const larg = await page.evaluate(() => document.documentElement.scrollWidth);
    await page.screenshot({ path: path.join(out, `pagina-${nome}.png`), fullPage: true });
    const alt = await page.evaluate(() => document.documentElement.scrollHeight);
    console.log(nome, 'largura do conteúdo', larg, '(janela ' + w + ')', 'altura', alt, erros.length ? erros : 'sem erros');
    await page.close();
  }
  await browser.close();
})();
