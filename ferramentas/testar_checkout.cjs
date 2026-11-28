// P2 — Teste do checkout da Hotmart antes do Portão 4.
// Uso: node ferramentas/testar_checkout.cjs <url-checkout> --preco "37,00" --bumps "Bolsa,Recortar,Cartas"
// Abre como navegador comum, escolhe Brasil, confere preço, cada bump (pelo nome) e os meios de pagamento.
// Também diz se os bumps aparecem SEM trocar o país (falha conhecida da Hotmart, ver aprendizados/processo.md).
const { chromium } = require('playwright');
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const url = process.argv[2];
if (!url || url.startsWith('--')) { console.log('uso: node ferramentas/testar_checkout.cjs <url> --preco "37,00" --bumps "A,B"'); process.exit(2); }
const preco = arg('--preco', null);
const bumps = (arg('--bumps', '') || '').split(',').map(s => s.trim()).filter(Boolean);
const norm = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
(async () => {
  const b = await chromium.launch({ args: ['--disable-blink-features=AutomationControlled'] });
  const c = await b.newContext({ locale: 'pt-BR', viewport: { width: 420, height: 900 },
    userAgent: 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Mobile Safari/537.36' });
  const p = await c.newPage();
  await p.goto(url, { waitUntil: 'networkidle', timeout: 60000 }); await p.waitForTimeout(3000);
  const antes = norm(await p.innerText('body'));
  try { await p.getByText(/Change country|Alterar país/).first().click(); await p.waitForTimeout(800);
        await p.getByText(/^Brasil$|^Brazil$/).first().click(); await p.waitForTimeout(5000); } catch (e) {}
  const t = norm(await p.innerText('body'));
  await p.screenshot({ path: 'checkout-teste.png', fullPage: true }); await b.close();
  const falhas = [], avisos = [];
  if (preco && !t.includes(norm(preco))) falhas.push(`preço R$ ${preco} não aparece`);
  for (const m of ['pix', 'boleto', 'cartao']) if (!t.includes(m)) falhas.push(`meio de pagamento "${m}" não aparece`);
  if (!t.includes('comprar agora')) falhas.push('botão "Comprar agora" não aparece');
  const foraDoBrasil = !antes.includes('r$');
  if (foraDoBrasil) avisos.push('esta sessão abriu o checkout fora do Brasil (sem R$): não dá para conferir daqui se os bumps aparecem sem trocar o país. Confira no celular, em aba anônima, a partir da página de vendas.');
  for (const bp of bumps) {
    if (!t.includes(norm(bp))) falhas.push(`bump "${bp}" não aparece (nem depois de escolher Brasil)`);
    else if (!foraDoBrasil && !antes.includes(norm(bp))) avisos.push(`bump "${bp}" só aparece depois de "Alterar país → Brasil" (comprador que não troca o país não vê)`);
  }
  console.log(falhas.length ? 'CHECKOUT COM FALHA' : 'CHECKOUT OK');
  falhas.forEach(f => console.log(' - FALHA:', f)); avisos.forEach(a => console.log(' - AVISO:', a));
  console.log('print: checkout-teste.png');
  process.exit(falhas.length ? 1 : 0);
})();
