/* Conversion and discovery helpers shared by every page: area finder, billboard
   filter, FAQ search, FAQ call nudge and stat count-up. Everything degrades to
   plain, readable HTML without JavaScript. */
(() => {
  'use strict';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const store = {
    get(k) { try { return sessionStorage.getItem(k); } catch (_) { return null; } },
    set(k, v) { try { sessionStorage.setItem(k, v); } catch (_) { /* storage unavailable */ } }
  };

  // Area finder on the homepage.
  const finderData = document.querySelector('#finder-data');
  if (finderData) {
    const data = JSON.parse(finderData.textContent);
    const box = document.querySelector('.finder-result');
    const field = name => box.querySelector(`[data-f="${name}"]`);
    const chips = [...document.querySelectorAll('[data-area]')];
    const show = key => {
      const d = data[key];
      if (!d) return;
      chips.forEach(c => c.setAttribute('aria-pressed', String(c.dataset.area === key)));
      field('name').textContent = d.name;
      field('who').textContent = d.who;
      field('led').textContent = d.led || '—';
      field('boards').textContent = d.boards || '—';
      const links = field('links');
      links.replaceChildren(...d.links.map(([href, text]) => {
        const a = document.createElement('a');
        a.href = href;
        const t = document.createElement('span'); t.textContent = text;
        const arrow = document.createElement('span'); arrow.setAttribute('aria-hidden', 'true'); arrow.textContent = '↗';
        a.append(t, arrow);
        return a;
      }));
      if (!reduce) box.animate([{ opacity: .35, transform: 'translateY(12px)' }, { opacity: 1, transform: 'none' }], { duration: 380, easing: 'cubic-bezier(.2,.7,.3,1)' });
    };
    chips.forEach(c => c.addEventListener('click', () => show(c.dataset.area)));
  }

  // Billboard directory filter by zone.
  const zoneButtons = [...document.querySelectorAll('[data-zone]')];
  if (zoneButtons.length) {
    const items = [...document.querySelectorAll('[data-zone-item]')];
    zoneButtons.forEach(btn => btn.addEventListener('click', () => {
      const z = btn.dataset.zone;
      zoneButtons.forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
      items.forEach(it => { it.hidden = z !== 'all' && it.dataset.zoneItem !== z; });
    }));
  }

  // FAQ search across every group.
  const search = document.querySelector('[data-faq-search]');
  if (search) {
    const scope = search.closest('.home-faq');
    const items = [...scope.querySelectorAll('.faq-item')];
    const groups = [...scope.querySelectorAll('[data-faq-group]')];
    const count = scope.querySelector('[data-faq-count]');
    const empty = scope.querySelector('.faq-empty');
    const total = items.length;
    search.addEventListener('input', () => {
      const q = search.value.trim().toLowerCase();
      if (q) scope.querySelectorAll('[data-faq-filter]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.faqFilter === 'all')));
      let shown = 0;
      items.forEach(it => {
        const hit = !q || it.textContent.toLowerCase().includes(q);
        it.hidden = !hit;
        if (hit) shown++;
      });
      groups.forEach(g => { g.hidden = !g.querySelector('.faq-item:not([hidden])'); });
      count.textContent = q ? `${shown} of ${total} answers` : `${total} answers`;
      empty.hidden = shown > 0;
    });
    // Choosing a topic clears the search; content.js then shows that topic's group.
    scope.querySelectorAll('[data-faq-filter]').forEach(b => b.addEventListener('click', () => {
      if (!search.value) return;
      search.value = '';
      items.forEach(it => { it.hidden = false; });
      count.textContent = `${total} answers`;
      empty.hidden = true;
    }));
  }

  // FAQ: animated opening, one-time call nudge after a few answers.
  const nudge = document.querySelector('.call-nudge');
  let opened = 0;
  document.querySelectorAll('.faq-item').forEach(item => item.addEventListener('toggle', () => {
    if (!item.open) return;
    item.classList.add('just-opened');
    setTimeout(() => item.classList.remove('just-opened'), 1600);
    opened++;
    if (nudge && opened >= 3 && !store.get('nudge-seen')) {
      store.set('nudge-seen', '1');
      nudge.hidden = false;
      requestAnimationFrame(() => nudge.classList.add('in'));
    }
  }));
  if (nudge) nudge.querySelector('.nudge-close').addEventListener('click', () => { nudge.classList.remove('in'); nudge.hidden = true; });

  // Count-up for network numbers.
  const counters = [...document.querySelectorAll('[data-count]')];
  if (counters.length && !reduce && 'IntersectionObserver' in window) {
    const fmt = n => n.toLocaleString('en-US');
    const io = new IntersectionObserver(entries => entries.forEach(en => {
      if (!en.isIntersecting) return;
      io.unobserve(en.target);
      const el = en.target, end = Number(el.dataset.count), t0 = performance.now(), dur = 1300;
      const step = t => {
        const p = Math.min(1, (t - t0) / dur), v = Math.round(end * (1 - Math.pow(1 - p, 3)));
        el.textContent = fmt(v);
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }), { threshold: .4 });
    counters.forEach(c => io.observe(c));
  }

  // Reveal-on-scroll for content pages that use .reveal outside the homepage script.
  if (!document.querySelector('.portal')) {
    const rev = [...document.querySelectorAll('.reveal')];
    if (rev.length && 'IntersectionObserver' in window) {
      document.documentElement.classList.add('reveal-ready');
      const io = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); } }), { threshold: .08 });
      rev.forEach(r => io.observe(r));
    }
  }
})();
