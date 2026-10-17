// Screenshot every .slide in a slides.html to PNG (1080 wide). Usage: node promo/posts/render_slides.js <post-dir>
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1400 }, deviceScaleFactor: 1 });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + path.join(dir, 'slides.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const slides = await p.$$('.slide');
  for (let i = 0; i < slides.length; i++) await slides[i].screenshot({ path: path.join(dir, `slide-${String(i + 1).padStart(2, '0')}.png`) });
  console.log(JSON.stringify({ slides: slides.length, errs })); await b.close();
})();
