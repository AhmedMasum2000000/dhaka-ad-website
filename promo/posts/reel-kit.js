// Shared kit for Dhaka AD reels: photo scenes with slow zoom, slam-in type, countdown and call-to-action.
// A reel page sets window.T, includes this file, builds scenes with scene()/cta(), then calls start([photo names]).
// promo/render.js drives it through seek(t), DURATION and ready.
const W = 1080, H = 1920;
const stage = document.getElementById('stage');
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const ease = p => 1 - Math.pow(1 - clamp(p), 3);
const back = p => { p = clamp(p); const c = 1.9; return 1 + (c + 1) * Math.pow(p - 1, 3) + c * Math.pow(p - 1, 2); };
const lerp = (a, b, p) => a + (b - a) * p;
const scenes = [];
const IMG = n => `../../img/${n}.jpg`;
function el(tag, cls, html, parent) { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; (parent || stage).appendChild(e); return e; }
function fit(line, max) { line.style.fontSize = max + 'px'; const room = W - 180; if (line.offsetWidth > room) line.style.fontSize = Math.floor(max * room / line.offsetWidth) + 'px'; }
function rise(node, t, at, d = .3, dy = 40) { const p = ease((t - at) / d); node.style.opacity = p; node.style.transform = `translateY(${(1 - p) * dy}px)`; return p; }

// o: photo, zoom [from,to], pan [x0,x1] px, blur [from,to] px, dark 0-1, color, flash, lines [[html, at, size, cls]], sub [html, at], top, upd(t, root)
function scene(s, e, o = {}) {
  const root = el('div', 'scene');
  root.style.background = o.color || 'var(--bg)';
  let ph = null;
  if (o.photo) { ph = el('div', 'ph', null, root); ph.style.backgroundImage = `url('${IMG(o.photo)}')`; el('div', 'shade', null, root).style.background = `linear-gradient(180deg,rgba(10,12,14,.8) 0%,rgba(10,12,14,0) 28%,rgba(10,12,14,0) 55%,rgba(10,12,14,.92) 100%), rgba(10,12,14,${o.dark == null ? .45 : o.dark})`; }
  const block = el('div', 'block', null, root);
  if (o.top) { block.style.top = o.top; block.style.transform = 'none'; }
  const lines = (o.lines || []).map(([txt, at, size, cls]) => { const l = el('span', 'line ' + (cls || ''), txt, block); l._at = at; l._size = size; return l; });
  const sub = o.sub ? el('div', 'sub', o.sub[0], block) : null;
  stage.insertBefore(root, document.getElementById('flash'));
  const sc = { s, e, root, block, flash: o.flash, init() { lines.forEach(l => fit(l, l._size)); },
    upd(t) {
      const p = clamp((t - s) / (e - s));
      if (ph) {
        const z = o.zoom ? lerp(o.zoom[0], o.zoom[1], p) : lerp(1, 1.08, p), x = o.pan ? lerp(o.pan[0], o.pan[1], p) : 0;
        const b = o.blur ? lerp(o.blur[0], o.blur[1], ease(p * 1.6)) : 0;
        ph.style.transform = `translateX(${x}px) scale(${z})`; ph.style.filter = b > .2 ? `blur(${b}px)` : 'none';
      }
      lines.forEach(l => { const q = (t - l._at) / 0.16; l.style.opacity = clamp(q * 1.6); const k = q < 1 ? 1.35 - 0.35 * back(q) : 1; const sh = q > 1 && q < 1.8 ? Math.sin(q * 40) * 6 * (1.8 - q) : 0; l.style.transform = `translateX(${sh}px) scale(${k})`; });
      if (sub) rise(sub, t, o.sub[1], .25, 24);
      if (o.upd) o.upd(t, root);
    } };
  scenes.push(sc); return sc;
}

// A ring that counts down `secs` seconds from `at`, placed at top `y`.
function countdown(root, at, secs, y) {
  const r = el('div', 'timer', `<svg viewBox="0 0 220 220"><circle cx="110" cy="110" r="96" fill="rgba(10,12,14,.65)" stroke="rgba(237,231,220,.18)" stroke-width="12"/><circle class="rg" cx="110" cy="110" r="96" fill="none" stroke="#ff3131" stroke-width="12" stroke-linecap="round" transform="rotate(-90 110 110)" stroke-dasharray="603" stroke-dashoffset="0"/></svg><b></b>`, root);
  r.style.top = y + 'px';
  const num = r.querySelector('b'), ring = r.querySelector('.rg');
  return t => { const lt = t - at, left = clamp(secs - lt, 0, secs); r.style.opacity = clamp(lt / .15); num.textContent = Math.max(1, Math.ceil(left)); ring.setAttribute('stroke-dashoffset', 603 * (1 - left / secs)); r.style.transform = `scale(${1 + 0.08 * Math.max(0, 1 - ((Math.max(0, lt) % 1) / .18))})`; };
}

// Closing card: o.head (html), o.at, o.photo, o.foot
function cta(s, e, o) {
  const sc = scene(s, e, { photo: o.photo, dark: .8, zoom: [1.1, 1.18], flash: 'var(--red)' });
  const box = el('div', 'cta', null, sc.root);
  const a = el('div', 'line', o.head, box); a.style.cssText += ';font-size:100px;white-space:normal;width:auto;line-height:1.02';
  const c = el('div', 'pill', 'Call 01840 860 284 <span>↗</span>', box); c.style.marginTop = '56px';
  const d = el('div', 'url', o.url || 'dhakaad.com', box);
  const f = o.foot ? el('div', 'small', o.foot, box) : null; if (f) f.style.marginTop = '40px';
  const items = [[a, s + .1], [c, s + .6], [d, s + .9], [f, s + 1.4]].filter(x => x[0]);
  const u = sc.upd;
  sc.upd = t => { u(t); items.forEach(([n, at]) => rise(n, t, at)); const pulse = t > s + 1.1 ? 1 + 0.035 * Math.sin((t - s - 1.1) * 7) : 1; c.style.transform += ` scale(${pulse})`; };
  return sc;
}

const bar = document.getElementById('bar'), flash = document.getElementById('flash');
function seek(t) {
  let active = null;
  scenes.forEach(sc => { const on = t >= sc.s && t < sc.e; sc.root.style.display = on ? 'block' : 'none'; if (on) { sc.upd(t); active = sc; } });
  bar.style.width = (W * t / window.T) + 'px';
  const f = active && active.flash ? clamp(1 - (t - active.s) / .12) : 0;
  flash.style.background = active && active.flash || 'transparent'; flash.style.opacity = f * .55;
}
function start(photos) {
  window.seek = seek; window.DURATION = window.T;
  window.ready = (async () => {
    await document.fonts.ready;
    await Promise.all(photos.map(n => new Promise(r => { const i = new Image(); i.onload = i.onerror = r; i.src = IMG(n); })));
    scenes.forEach(sc => { sc.root.style.display = 'block'; sc.init(); sc.root.style.display = 'none'; });
    seek(0); return true;
  })();
}
