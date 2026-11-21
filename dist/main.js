(() => {
  document.documentElement.classList.add('js');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Header: switch to the light pill once the dark hero has scrolled away
  const header = document.querySelector('.site-header');
  const hero = document.querySelector('.hero, .page-hero');
  const setHeader = () => {
    const limit = hero ? hero.offsetHeight - 90 : 0;
    header.classList.toggle('light', window.scrollY > limit);
  };
  setHeader();
  window.addEventListener('scroll', setHeader, { passive: true });

  // Dropdowns: click/keyboard support on top of hover
  document.querySelectorAll('.has-menu').forEach(li => {
    const btn = li.querySelector('button');
    btn.addEventListener('click', () => {
      const open = !li.classList.contains('open');
      document.querySelectorAll('.has-menu.open').forEach(o => { o.classList.remove('open'); o.querySelector('button').setAttribute('aria-expanded', 'false'); });
      li.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', String(open));
    });
  });
  document.addEventListener('click', e => {
    if (!e.target.closest('.has-menu')) document.querySelectorAll('.has-menu.open').forEach(o => { o.classList.remove('open'); o.querySelector('button').setAttribute('aria-expanded', 'false'); });
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.has-menu.open').forEach(o => o.classList.remove('open'));
      closeMenu();
    }
  });

  // Mobile menu
  const mm = document.querySelector('.mobile-menu');
  const toggle = document.querySelector('.menu-toggle');
  function closeMenu() { if (!mm) return; mm.classList.remove('open'); toggle && toggle.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; }
  toggle && toggle.addEventListener('click', () => { mm.classList.add('open'); toggle.setAttribute('aria-expanded', 'true'); document.body.style.overflow = 'hidden'; mm.querySelector('.close').focus(); });
  mm && mm.querySelector('.close').addEventListener('click', closeMenu);

  // Hero parallax (subtle)
  const heroImg = document.querySelector('.hero-bg img');
  if (heroImg && !reduce) {
    window.addEventListener('scroll', () => {
      const y = Math.min(window.scrollY, 900);
      heroImg.style.transform = `scale(1.06) translateY(${y * 0.18}px)`;
    }, { passive: true });
  }

  // Counters
  const counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    const run = el => {
      const end = +el.dataset.count, start = +(el.dataset.from || 0);
      if (reduce) { el.textContent = end; return; }
      const t0 = performance.now(), dur = 1600;
      const tick = t => {
        const p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(start + (end - start) * e);
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };
    const io = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { run(en.target); io.unobserve(en.target); } }), { threshold: .5 });
    counters.forEach(c => io.observe(c));
  }

  // Expertise tabs (auto-advance, pause on hover/focus)
  document.querySelectorAll('[data-tabset]').forEach(set => {
    const btns = [...set.querySelectorAll('.tab-btn')];
    const panels = [...set.querySelectorAll('.tab-panel')];
    const ms = 7000; let i = 0, timer;
    set.style.setProperty('--tab-ms', ms + 'ms');
    const show = n => {
      i = (n + btns.length) % btns.length;
      btns.forEach((b, k) => { b.setAttribute('aria-selected', String(k === i)); b.tabIndex = k === i ? 0 : -1; });
      panels.forEach((p, k) => p.classList.toggle('active', k === i));
      // restart bar animation
      const bar = btns[i].querySelector('.bar'); bar.style.animation = 'none'; bar.offsetWidth; bar.style.animation = '';
    };
    const start = () => { if (reduce) return; clearInterval(timer); timer = setInterval(() => show(i + 1), ms); };
    btns.forEach((b, k) => {
      b.addEventListener('click', () => { show(k); start(); });
      b.addEventListener('keydown', e => {
        if (e.key === 'ArrowDown' || e.key === 'ArrowRight') { e.preventDefault(); show(i + 1); btns[i].focus(); start(); }
        if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') { e.preventDefault(); show(i - 1); btns[i].focus(); start(); }
      });
    });
    set.addEventListener('mouseenter', () => { clearInterval(timer); set.classList.add('paused'); });
    set.addEventListener('mouseleave', () => { set.classList.remove('paused'); start(); });
    show(0); start();
  });

  // Project team tabs (with #hash support)
  const tteams = document.querySelector('[data-teams]');
  if (tteams) {
    const tabs = [...tteams.querySelectorAll('.team-tab')];
    const panels = [...tteams.querySelectorAll('.team-panel')];
    const select = (id, push) => {
      tabs.forEach(t => { const on = t.dataset.target === id; t.setAttribute('aria-selected', String(on)); t.tabIndex = on ? 0 : -1; });
      panels.forEach(p => p.hidden = p.id !== id);
      if (push) history.replaceState(null, '', '#' + id);
    };
    tabs.forEach((t, k) => {
      t.addEventListener('click', () => select(t.dataset.target, true));
      t.addEventListener('keydown', e => {
        const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (d) { e.preventDefault(); const n = tabs[(k + d + tabs.length) % tabs.length]; n.focus(); select(n.dataset.target, true); }
      });
    });
    const h = location.hash.slice(1);
    select(panels.some(p => p.id === h) ? h : panels[0].id, false);
  }

  // Testimonials
  const quotes = document.querySelector('[data-quotes]');
  if (quotes) {
    const items = [...quotes.querySelectorAll('.quote')];
    const dots = [...quotes.querySelectorAll('.quote-dots span')];
    let i = 0, timer;
    const show = n => { i = (n + items.length) % items.length; items.forEach((q, k) => q.classList.toggle('active', k === i)); dots.forEach((d, k) => d.classList.toggle('on', k === i)); };
    const start = () => { if (reduce) return; clearInterval(timer); timer = setInterval(() => show(i + 1), 8000); };
    quotes.querySelector('[data-prev]').addEventListener('click', () => { show(i - 1); start(); });
    quotes.querySelector('[data-next]').addEventListener('click', () => { show(i + 1); start(); });
    show(0); start();
  }

  // Case study slide viewer
  const viewer = document.querySelector('[data-viewer]');
  if (viewer) {
    const slides = JSON.parse(viewer.dataset.slides);
    const img = viewer.querySelector('.viewer-stage img');
    const cur = viewer.querySelector('[data-cur]');
    const open = viewer.querySelector('[data-open]');
    const thumbs = [...viewer.querySelectorAll('.thumbs button')];
    let i = 0;
    const show = n => {
      i = (n + slides.length) % slides.length;
      img.src = slides[i] + '?w=1800&auto=format';
      img.alt = `Slide ${i + 1} of ${slides.length}`;
      cur.textContent = i + 1;
      open.href = slides[i];
      thumbs.forEach((t, k) => t.setAttribute('aria-current', String(k === i)));
      // preload next
      const pre = new Image(); pre.src = slides[(i + 1) % slides.length] + '?w=1800&auto=format';
    };
    viewer.querySelector('[data-prev]').addEventListener('click', () => show(i - 1));
    viewer.querySelector('[data-next]').addEventListener('click', () => show(i + 1));
    thumbs.forEach((t, k) => t.addEventListener('click', () => show(k)));
    document.addEventListener('keydown', e => {
      if (e.target.closest('input, textarea')) return;
      if (e.key === 'ArrowRight') show(i + 1);
      if (e.key === 'ArrowLeft') show(i - 1);
    });
    // swipe
    let x0 = null;
    img.addEventListener('touchstart', e => x0 = e.touches[0].clientX, { passive: true });
    img.addEventListener('touchend', e => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1)); x0 = null; });
    show(0);
  }

  // Scroll reveal with stagger for cards in the same group
  const revealSel = '.h-section, .lede, .stat, .mission-card, .tab-panels, .tablist, .person, .advisor, .logo-tile, .service, .step, .steps, .case-card, .viewer, .photo, .faq details, .form-card, .social-link, .team-tab, .cta-band, .why, .letter p, .signature';
  const els = [...document.querySelectorAll(revealSel)].filter(el => !el.closest('.hero, .page-hero, .site-header, .mobile-menu'));
  els.forEach(el => {
    el.setAttribute('data-reveal', '');
    const sibs = [...el.parentElement.children].filter(c => c.matches(revealSel));
    const idx = sibs.indexOf(el);
    el.style.setProperty('--d', Math.min(idx, 8) * 70 + 'ms');
  });
  if (reduce || !('IntersectionObserver' in window)) {
    els.forEach(el => el.classList.add('in'));
  } else {
    const rio = new IntersectionObserver(es => es.forEach(en => {
      if (en.isIntersecting) { en.target.classList.add('in'); rio.unobserve(en.target); }
    }), { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(el => rio.observe(el));
    // re-observe cards inside project-team panels when a tab is switched in
    document.querySelectorAll('.team-tab').forEach(t => t.addEventListener('click', () => {
      document.querySelectorAll('.team-panel:not([hidden]) [data-reveal]:not(.in)').forEach(el => rio.observe(el));
    }));
  }

  // Cursor-following glow
  const glowSel = '.service, .step, .mission-card, .advisor, .case-card, .stat, .form-card, .team-tab, .person';
  document.querySelectorAll(glowSel).forEach(card => {
    card.classList.add('glow');
    card.addEventListener('pointermove', e => {
      const r = card.getBoundingClientRect();
      card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      card.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });

  // Contact form (not connected yet)
  const form = document.querySelector('[data-contact]');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      form.querySelector('.form-note').classList.add('show');
    });
  }
})();
