// Site behaviour: motion, mobile nav, header scroll state, reveals, forms. No dependencies.
(() => {
  const doc = document.documentElement;
  doc.classList.add('js');
  const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  const reduceMotion = motionQuery.matches;

  // ------------------------------------------------------------ motion
  // All animation runs in JavaScript (the user's standard, 2026-10-09); CSS only describes the states, and
  // qa.py errors on CSS transition, animation and @keyframes. morph(parts, change) reads how each part looks
  // now (mid-animation included), runs `change` (a class or attribute toggle), reads the new CSS state and
  // animates between the two with the Web Animations API. The CSS state is always the end point, so with
  // reduced motion (or no WAAPI) the change just happens. Parts: { el, props, pseudo? }. Animate transform
  // and opacity only; visibility may ride along so a closing panel stays visible until the end.
  const EASE = getComputedStyle(doc).getPropertyValue('--ease').trim() || 'cubic-bezier(.2, .7, .2, 1)';
  const running = new WeakMap();  // el -> { [pseudo]: Animation }
  const camel = p => p.replace(/-(\w)/g, (_, c) => c.toUpperCase());
  const morph = (parts, change, { duration = 250 } = {}) => {
    parts = parts.filter(p => p.el);
    if (motionQuery.matches || !doc.animate || !parts.length) { change(); return; }
    const read = ({ el, props, pseudo }) => {
      const cs = getComputedStyle(el, pseudo || null);
      return Object.fromEntries(props.map(p => [camel(p), cs.getPropertyValue(p)]));
    };
    const from = parts.map(read);
    parts.forEach(({ el, pseudo = '' }) => running.get(el)?.[pseudo]?.cancel());
    change();
    parts.forEach((part, i) => {
      const to = read(part), pseudo = part.pseudo || '';
      if (Object.keys(to).every(k => to[k] === from[i][k])) return;
      const anims = running.get(part.el) || {};
      anims[pseudo] = part.el.animate([from[i], to], { duration, easing: EASE, ...(pseudo && { pseudoElement: pseudo }) });
      running.set(part.el, anims);
    });
  };

  // ------------------------------------------------------------ mobile nav
  const toggle = document.querySelector('[data-nav-toggle]');
  if (toggle) {
    const nav = document.querySelector('.site-nav');
    const setOpen = open => morph([{ el: nav, props: ['opacity', 'transform', 'visibility'] }], () => {
      toggle.setAttribute('aria-expanded', String(open));
      doc.classList.toggle('nav-open', open);
    }, { duration: 200 });
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && doc.classList.contains('nav-open')) { setOpen(false); toggle.focus(); }
    });
  }

  // ------------------------------------------------------------ header state
  // Fixed-height bar; .is-scrolled is styled with transform/opacity only: the backdrop (::before) fades in
  // and the logo scales, animated by morph().
  const header = document.querySelector('[data-header]');
  if (header) {
    let queued = false;
    const parts = [{ el: header, props: ['opacity'], pseudo: '::before' },
      { el: header.querySelector('.brand'), props: ['transform'] }];
    const update = () => {
      queued = false;
      const on = window.scrollY > 40;
      if (on !== header.classList.contains('is-scrolled')) morph(parts, () => header.classList.toggle('is-scrolled', on));
    };
    window.addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(update); } }, { passive: true });
    update();
  }

  // ------------------------------------------------------------ reveals
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length && !reduceMotion && 'IntersectionObserver' in window) {
    // Reveals replay each time they come back into view (REPLAY, the user's standard 2026-10-09): .is-in comes
    // off only once the element is fully off-screen, so the reset is never seen. false = reveal once.
    const REPLAY = true;
    const io = new IntersectionObserver(entries => entries.forEach(({ isIntersecting, target: el }) => {
      if (!isIntersecting || el.classList.contains('is-in')) return;
      morph([{ el, props: ['opacity', 'transform'] }], () => el.classList.add('is-in'), { duration: 600 });
      if (!REPLAY) io.unobserve(el);
    }), { rootMargin: '0px 0px -10% 0px' });
    const away = new IntersectionObserver(entries => entries.forEach(({ isIntersecting, target: el }) => {
      if (isIntersecting) return;
      running.get(el)?.['']?.cancel();
      el.classList.remove('is-in');
    }));
    reveals.forEach(el => { io.observe(el); if (REPLAY) away.observe(el); });
  } else {
    reveals.forEach(el => el.classList.add('is-in'));
  }

  // ------------------------------------------------------------ parallax
  // Default speed: 50% of scroll (the user's standard, Macz 2026-10-07). Mark a full-bleed photo
  // <div class="media"><img data-parallax ...></div>; it moves by half its frame's offset from the
  // viewport top (transform: translateY only). CSS sizes it so the frame never shows a gap.
  // If SPEED changes, change the 50% / 50lvh in the CSS height formula to match.
  const SPEED = 0.5;
  const layers = [...document.querySelectorAll('[data-parallax]')];
  if (layers.length && !reduceMotion) {
    let ticking = false;
    const move = () => {
      const vh = window.innerHeight;
      layers.forEach(img => {
        const frame = img.parentElement.getBoundingClientRect();
        if (frame.bottom < -100 || frame.top > vh + 100) return;
        img.style.transform = `translate3d(0, ${(-frame.top * (1 - SPEED)).toFixed(1)}px, 0)`;
      });
      ticking = false;
    };
    const queue = () => { if (!ticking) { ticking = true; requestAnimationFrame(move); } };
    window.addEventListener('scroll', queue, { passive: true });
    window.addEventListener('resize', queue);
    move();
  }

  // ------------------------------------------------------------ forms
  const clean = v => (v == null ? '' : String(v).trim());
  const isBlank = v => !v || v === 'null' || v === 'undefined';
  const params = new URLSearchParams(location.search);

  document.querySelectorAll('[data-form]').forEach(form => {
    // URL prefill, guarded so a missing param never produces "the null"
    form.querySelectorAll('[data-prefill]').forEach(field => {
      const value = clean(params.get(field.dataset.prefill));
      if (isBlank(value)) return;
      if (field.tagName === 'SELECT') {
        if ([...field.options].some(o => o.value === value)) field.value = value;
      } else {
        const tpl = field.dataset.prefillTemplate;
        field.value = tpl ? tpl.replace('{value}', value) : value;
      }
    });

    // The reply route becomes required when the visitor picks it: phone for a call or a text
    // (data-requires-phone="Phone call,Text"), email for email (data-requires-email="Email"), so no lead
    // arrives without a way to answer it (L-072).
    const pref = form.querySelector('[data-requires-phone], [data-requires-email]');
    const need = (input, list) => {
      if (!pref || !input || !list) return;
      const needs = list.split(',').map(s => s.trim()).includes(pref.value);
      input.required = needs;
      input.closest('.field')?.classList.toggle('is-required', needs);
    };
    const syncPhone = () => {
      need(form.querySelector('input[type="tel"]'), pref?.dataset.requiresPhone);
      need(form.querySelector('input[type="email"]'), pref?.dataset.requiresEmail);
    };
    pref?.addEventListener('change', syncPhone);
    syncPhone();

    const status = form.querySelector('[data-form-status]');
    const say = (msg, kind) => { if (status) { status.textContent = msg; status.dataset.kind = kind; } };
    const emptyFields = () => [...form.elements].filter(el =>
      el.name && !el.disabled && el.type !== 'submit' && el.type !== 'button' && clean(el.value) === '');

    form.addEventListener('submit', async e => {
      syncPhone();
      if (!form.checkValidity()) { e.preventDefault(); form.reportValidity(); return; }

      // data-native: let the browser post the form, but don't send fields left empty
      if ('native' in form.dataset) {
        emptyFields().forEach(el => { el.disabled = true; el.dataset.wasEmpty = ''; });
        return;
      }

      e.preventDefault();
      const endpoint = form.dataset.endpoint;
      if (!endpoint) {
        say('This form isn’t connected yet (preview build). Please call or email us instead.', 'error');
        return;
      }
      const thanks = form.dataset.success || 'Thanks, we got your message and will get back to you soon.';
      // Spam trap filled (only bots see it): look successful, send nothing
      if (clean(form.querySelector('[data-trap]')?.value)) { form.reset(); say(thanks, 'ok'); return; }
      const data = new FormData(form);
      emptyFields().forEach(el => data.delete(el.name));
      const button = form.querySelector('[type="submit"]');
      if (button) button.disabled = true;
      say('Sending…', 'pending');
      try {
        // Netlify Forms takes a url-encoded POST (with form-name); Web3Forms, Formspree and the like take FormData
        const netlify = form.dataset.backend === 'netlify';
        const res = await fetch(endpoint, netlify
          ? { method: 'POST', body: new URLSearchParams(data), headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
          : { method: 'POST', body: data, headers: { Accept: 'application/json' } });
        if (!res.ok) throw new Error(String(res.status));
        if (!netlify && (res.headers.get('content-type') || '').includes('json')) {
          const body = await res.json().catch(() => ({}));
          if (body.success === false) throw new Error(body.message || 'rejected');  // Web3Forms answers 200 + success:false on some errors
        }
        form.reset();
        syncPhone();
        say(thanks, 'ok');
      } catch {
        say('Something went wrong sending the form. Please call us instead.', 'error');
      } finally {
        if (button) button.disabled = false;
      }
    });
  });

  // Back/forward cache: re-enable fields disabled for a native submit
  window.addEventListener('pageshow', () => {
    document.querySelectorAll('[data-form] [data-was-empty]').forEach(el => {
      el.disabled = false;
      delete el.dataset.wasEmpty;
    });
  });
})();
