// Render reel.html frame by frame and encode an Instagram Reel (1080x1920, 30 fps, H.264).
// Usage: [REEL_HTML=page.html] [PREVIEW_DIR=dir] node promo/render.js [out.mp4] [--preview t1,t2,...]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
(async () => {
  const args = process.argv.slice(2);
  const out = args[0] && !args[0].startsWith('--') ? args[0] : path.join(__dirname, 'dhaka-ad-reel-silent.mp4');
  const prevIdx = args.indexOf('--preview');
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  const html = process.env.REEL_HTML ? path.resolve(process.env.REEL_HTML) : path.join(__dirname, 'reel.html');
  await p.goto('file://' + html);
  await p.evaluate(() => window.ready);
  if (prevIdx >= 0) {
    for (const t of args[prevIdx + 1].split(',')) { await p.evaluate(t => seek(+t), t); await p.screenshot({ path: path.join(process.env.PREVIEW_DIR || path.dirname(html), `preview-${t}.jpg`), type: 'jpeg', quality: 80 }); }
    console.log(JSON.stringify({ errs })); await b.close(); return;
  }
  const fps = 30, dur = await p.evaluate(() => window.DURATION), n = Math.round(dur * fps);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let i = 0; i < n; i++) {
    await p.evaluate(t => seek(t), i / fps);
    const buf = await p.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 150 === 0) console.error(`frame ${i}/${n}`);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r));
  console.log(JSON.stringify({ out, frames: n, errs })); await b.close();
})();
