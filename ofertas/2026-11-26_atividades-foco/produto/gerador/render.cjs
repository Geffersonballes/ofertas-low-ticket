// Gera o PDF e uma imagem por página a partir de saida/amostra.html.
// Uso: node render.cjs [escala]   (escala das imagens: 1 para conferência, 2 para mostrar)
const { chromium } = require('playwright');
const path = require('node:path');

(async () => {
  const saida = path.join(__dirname, 'saida');
  const escala = Number(process.argv[2] || 1);
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: escala });
  await page.goto('file://' + path.join(saida, 'amostra.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: path.join(saida, 'dez-minutinhos-amostra.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
  await page.emulateMedia({ media: 'print' });
  const paginas = await page.$$('section.pagina');
  for (let i = 0; i < paginas.length; i++) {
    await paginas[i].screenshot({ path: path.join(saida, `pagina-${String(i + 1).padStart(2, '0')}.png`) });
  }
  console.log(`${paginas.length} páginas renderizadas`);
  await browser.close();
})();
