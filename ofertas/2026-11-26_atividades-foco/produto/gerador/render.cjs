// Gera o PDF e uma imagem por página a partir de saida/amostra.html.
// Uso: node render.cjs [escala] [vitrine]   (escala: 1 conferência, 2 mostrar; 'vitrine' gera vitrine-XX.png sem PDF)
const { chromium } = require('playwright');
const path = require('node:path');

(async () => {
  const saida = path.join(__dirname, 'saida');
  const escala = Number(process.argv[2] || 1);
  const vitrine = process.argv[3] === 'vitrine';
  const nome = vitrine ? 'vitrine' : 'amostra';
  const prefixo = vitrine ? 'vitrine' : 'pagina';
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: escala });
  await page.goto('file://' + path.join(saida, nome + '.html'));
  await page.evaluate(() => document.fonts.ready);
  if (!vitrine) await page.pdf({ path: path.join(saida, 'dez-minutinhos-amostra.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });
  await page.emulateMedia({ media: 'print' });
  const paginas = await page.$$('section.pagina');
  for (let i = 0; i < paginas.length; i++) {
    await paginas[i].screenshot({ path: path.join(saida, `${prefixo}-${String(i + 1).padStart(2, '0')}.png`) });
  }
  console.log(`${paginas.length} páginas renderizadas`);
  await browser.close();
})();
