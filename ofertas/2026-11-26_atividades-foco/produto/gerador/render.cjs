// Gera o PDF e uma imagem por página a partir de saida/amostra.html.
// Uso: node render.cjs [escala] [vitrine|completo]
//   (sem modo: amostra + PDF; 'vitrine': vitrine-XX.png sem PDF; 'completo': completo-XXX.png + dez-minutinhos.pdf)
const { chromium } = require('playwright');
const path = require('node:path');

(async () => {
  const saida = path.join(__dirname, 'saida');
  const escala = Number(process.argv[2] || 1);
  const modo = process.argv[3] || 'amostra';
  const vitrine = modo === 'vitrine';
  const nome = modo;
  const prefixo = modo === 'amostra' ? 'pagina' : modo;
  const pdf = modo === 'completo' ? 'dez-minutinhos.pdf' : 'dez-minutinhos-amostra.pdf';
  const dig = modo === 'completo' ? 3 : 2;
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: escala });
  await page.goto('file://' + path.join(saida, nome + '.html'));
  await page.evaluate(() => document.fonts.ready);
  if (!vitrine) await page.pdf({ path: path.join(saida, pdf), format: 'A4', printBackground: true, preferCSSPageSize: true });
  await page.emulateMedia({ media: 'print' });
  const paginas = await page.$$('section.pagina');
  for (let i = 0; i < paginas.length; i++) {
    await paginas[i].screenshot({ path: path.join(saida, `${prefixo}-${String(i + 1).padStart(dig, '0')}.png`) });
  }
  console.log(`${paginas.length} páginas renderizadas`);
  await browser.close();
})();
