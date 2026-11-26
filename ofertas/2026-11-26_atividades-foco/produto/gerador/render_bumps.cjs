// Renderiza um bump: saida/bump-<slug>.html → PDF + uma imagem por página (para conferência).
// Uso: node render_bumps.cjs <slug> <pdf-de-saida> [escala]
const { chromium } = require('playwright');
const path = require('node:path');
(async () => {
  const [slug, pdf, esc] = process.argv.slice(2);
  const saida = path.join(__dirname, 'saida');
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: Number(esc || 1) });
  await page.goto('file://' + path.join(saida, `bump-${slug}.html`));
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: pdf, printBackground: true, preferCSSPageSize: true });
  await page.emulateMedia({ media: 'print' });
  const paginas = await page.$$('section.pagina');
  for (let i = 0; i < paginas.length; i++) {
    await paginas[i].screenshot({ path: path.join(saida, `bump-${slug}-${String(i + 1).padStart(3, '0')}.png`) });
  }
  console.log(`${slug}: ${paginas.length} páginas`);
  await browser.close();
})();
