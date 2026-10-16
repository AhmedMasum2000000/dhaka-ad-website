(() => {
  'use strict';
  const root = document.documentElement;
  const portal = document.querySelector('.portal');
  const stage = document.querySelector('.portal-stage');
  const leftPanel = document.querySelector('.shutter-left');
  const rightPanel = document.querySelector('.shutter-right');
  const title = document.querySelector('.portal-title');
  const titleLeft = document.querySelector('.title-left');
  const titleRight = document.querySelector('.title-right');
  const photo = document.querySelector('.portal-photo');
  const tone = document.querySelector('.photo-tone');
  const intro = document.querySelector('.portal-intro');
  const scene = document.querySelector('.portal-scene');
  if (!portal || !stage || !scene) return;
  const sceneLink = scene.querySelector('a');
  const travellerA = document.querySelector('.traveller-amber');
  const travellerT = document.querySelector('.traveller-teal');
  const progressBar = document.querySelector('.hero-progress span');
  const orbit = document.querySelector('.orbit-image');
  const question = document.querySelector('.hero-question');
  const clamp = (n, min = 0, max = 1) => Math.min(max, Math.max(min, n));
  let scheduled = false;
  let observer;

  function paint() {
    scheduled = false;
    if (!root.classList.contains('motion-ready')) return;
    const rect = portal.getBoundingClientRect();
    const p = clamp(-rect.top / Math.max(1, portal.offsetHeight - stage.offsetHeight));
    const open = clamp(p / .76);
    const eased = open * open * (3 - 2 * open);
    leftPanel.style.transform = `translateX(${-103 * eased}%)`;
    rightPanel.style.transform = `translateX(${103 * eased}%)`;
    title.style.transform = `scale(${1 + eased * .16})`;
    title.style.letterSpacing = `${-.055 - eased * .025}em`;
    titleLeft.style.transform = `translateX(${-eased * 62}%)`;
    titleRight.style.transform = `translateX(${eased * 78}%)`;
    title.style.opacity = `${1 - clamp((p - .36) / .3)}`;
    photo.style.transform = `scale(${1.16 - eased * .16})`;
    tone.style.opacity = `${eased * .16}`;
    intro.style.opacity = `${1 - clamp(p / .28)}`;
    if (question) { question.style.opacity = `${1 - clamp(p / .38)}`; question.style.transform = `translateY(${-p * 24}px)`; }
    intro.style.transform = `translateY(${p * 30}px)`;
    const sceneProgress = clamp((p - .47) / .25);
    scene.style.opacity = `${sceneProgress}`;
    scene.style.transform = `translateY(${(1 - sceneProgress) * 30}px)`;
    const sceneActive = sceneProgress > .8;
    sceneLink.tabIndex = sceneActive ? 0 : -1;
    sceneLink.style.pointerEvents = sceneActive ? 'auto' : 'none';
    scene.setAttribute('aria-hidden', String(!sceneActive));
    travellerA.style.transform = `translate(${-eased * stage.clientWidth * .43}px,${-eased * stage.clientHeight * .29}px)`;
    travellerT.style.transform = `translate(${eased * stage.clientWidth * .43}px,${eased * stage.clientHeight * .29}px)`;
    progressBar.style.width = `${p * 100}%`;
    const art = document.querySelector('.statement-art');
    if (art && orbit) {
      const artRect = art.getBoundingClientRect();
      const artProgress = clamp((innerHeight - artRect.top) / (innerHeight + artRect.height));
      orbit.style.transform = `translateY(${-30 * artProgress}px) rotate(${-12 + artProgress * 18}deg)`;
    }
  }
  function schedulePaint() { if (!scheduled) { scheduled = true; requestAnimationFrame(paint); } }
  function setMotion() {
    root.classList.add('motion-ready', 'motion-opt-in');
    root.classList.remove('motion-paused');
    observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) { entry.target.classList.add('is-visible'); observer.unobserve(entry.target); }
      });
    }, { threshold: .08 });
    document.querySelectorAll('.reveal:not(.is-visible)').forEach(el => observer.observe(el));
    schedulePaint();
  }
  addEventListener('scroll', schedulePaint, { passive: true });
  addEventListener('resize', schedulePaint, { passive: true });
  setMotion();

  const timeLabel = document.querySelector('.local-time');
  function tick() { if (!timeLabel) return; timeLabel.textContent = new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Dhaka', hour: '2-digit', minute: '2-digit', hour12: false }).format(new Date()); }
  tick(); setInterval(tick, 60000);
  const year = document.querySelector('#year');
  if (year) year.textContent = new Date().getFullYear();

  const menuButton = document.querySelector('.menu-toggle');
  const menu = document.querySelector('#mobile-menu');
  function closeMenu() { menu.hidden = true; menuButton.setAttribute('aria-expanded', 'false'); menuButton.innerHTML = 'Menu <span aria-hidden="true">+</span>'; }
  menuButton.addEventListener('click', () => { const opening = menu.hidden; menu.hidden = !opening; menuButton.setAttribute('aria-expanded', String(opening)); menuButton.innerHTML = opening ? 'Close <span aria-hidden="true">−</span>' : 'Menu <span aria-hidden="true">+</span>'; });
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
  addEventListener('keydown', e => { if (e.key === 'Escape' && !menu.hidden) { closeMenu(); menuButton.focus(); } });
  const desktopQuery = matchMedia('(min-width:761px)');
  desktopQuery.addEventListener('change', e => { if (e.matches) closeMenu(); });

  const deck = document.querySelector('.deck');
  if (!deck) return;
  const cards = [...deck.querySelectorAll('.location-card')];
  const dots = [...document.querySelectorAll('.deck-dots button')];
  let current = 0;
  let busy = false;
  let drag = null;
  function restack() {
    cards.forEach((card, i) => {
      const depth = (i - current + cards.length) % cards.length;
      card.style.zIndex = String(cards.length - depth);
      card.style.opacity = depth > 2 ? '0' : '1';
      card.style.transform = depth === 0 ? 'translate(0,0) rotate(-2deg) scale(1)' : `translate(${depth * 9}px,${-depth * 8}px) rotate(${depth % 2 ? 5 : -6}deg) scale(${1 - depth * .035})`;
      card.style.pointerEvents = depth === 0 ? 'auto' : 'none';
      card.setAttribute('aria-hidden', String(depth !== 0));
    });
    dots.forEach((dot, i) => dot.setAttribute('aria-pressed', String(i === current)));
    document.querySelector('#deck-count').textContent = `${String(current + 1).padStart(2, '0')} / ${String(cards.length).padStart(2, '0')}`;
    document.querySelector('#deck-name').textContent = cards[current].dataset.name;
    document.querySelector('#deck-category').textContent = cards[current].dataset.category;
    document.querySelector('#deck-status').textContent = `Location ${current + 1} of ${cards.length}: ${cards[current].dataset.name}`;
  }
  function selectCard(next, direction = 1) {
    if (busy || next === current) { restack(); return; }
    busy = true;
    const outgoing = cards[current];
    outgoing.style.transition = 'transform .4s cubic-bezier(.2,.7,.3,1),opacity .35s';
    outgoing.style.transform = `translate(${direction * deck.clientWidth * 1.2}px,-40px) rotate(${direction * 22}deg)`;
    outgoing.style.opacity = '0';
    setTimeout(() => { current = (next + cards.length) % cards.length; outgoing.style.transition = ''; busy = false; restack(); }, 380);
  }
  function nextCard(direction) { selectCard((current + direction + cards.length) % cards.length, direction); }
  document.querySelector('#deck-prev').addEventListener('click', () => nextCard(-1));
  document.querySelector('#deck-next').addEventListener('click', () => nextCard(1));
  dots.forEach((dot, i) => dot.addEventListener('click', () => selectCard(i, i >= current ? 1 : -1)));
  deck.addEventListener('keydown', e => { if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') { e.preventDefault(); nextCard(e.key === 'ArrowLeft' ? -1 : 1); } });
  deck.addEventListener('pointerdown', e => {
    if (busy || e.button !== 0) return;
    drag = { id: e.pointerId, x: e.clientX, y: e.clientY, dx: 0, dy: 0 };
    deck.setPointerCapture(e.pointerId);
    cards[current].style.transition = 'none';
  });
  deck.addEventListener('pointermove', e => {
    if (!drag || drag.id !== e.pointerId) return;
    drag.dx = e.clientX - drag.x; drag.dy = e.clientY - drag.y;
    if (Math.abs(drag.dy) > Math.abs(drag.dx) && Math.abs(drag.dy) > 12) { endDrag(e, true); return; }
    cards[current].style.transform = `translate(${drag.dx}px,${drag.dy * .3}px) rotate(${drag.dx / deck.clientWidth * 22 - 2}deg) scale(1.015)`;
  });
  function endDrag(e, cancelled = false) {
    if (!drag || drag.id !== e.pointerId) return;
    const dx = drag.dx; drag = null;
    if (deck.hasPointerCapture(e.pointerId)) deck.releasePointerCapture(e.pointerId);
    cards[current].style.transition = '';
    if (!cancelled && Math.abs(dx) > deck.clientWidth * .12) selectCard((current + 1) % cards.length, dx > 0 ? 1 : -1);
    else restack();
  }
  deck.addEventListener('pointerup', e => endDrag(e));
  deck.addEventListener('pointercancel', e => endDrag(e, true));
  deck.addEventListener('lostpointercapture', e => endDrag(e, true));
  restack();

})();
