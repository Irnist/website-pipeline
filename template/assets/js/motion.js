// GSAP scroll motion. Loaded only when site_config.GSAP lists plugins (BRIEF.md "GSAP motion: yes");
// otherwise the build leaves this file out. Runs after main.js and the self-hosted GSAP files.
//
// Rules (CLAUDE.md + browser_qa.mjs motion pass):
// - Animate transform and opacity only: x, y, xPercent, yPercent, scale, rotation, opacity/autoAlpha.
// - Never tween an element that main.js already moves (.reveal, data-parallax, the header and mobile nav):
//   two systems on one transform fight. Animate a child or a wrapper instead.
// - No CSS transitions or keyframes anywhere (the user's standard; qa.py errors): UI motion is main.js
//   morph() (Web Animations API), signature moments are GSAP here.
// - Everything sits inside the reduced-motion gate below; reduced motion gets the plain, fully visible page.
// - Never hide the hero headline or hero image at load (LCP). Signature moments live below the fold.
// - 1–3 signature moments per site, built from this business's story, not effects on every section.
//
// Ready recipes, all optional (add the attribute in a page to use one): data-gsap="split" (headline),
// "trace" (line + nodes down a list), "sticker" (badge slaps on), "h-scroll" (pinned sideways gallery).
(() => {
  if (!window.gsap) return;
  const plugins = ['ScrollTrigger', 'SplitText', 'Flip', 'DrawSVGPlugin', 'MotionPathPlugin',
    'MorphSVGPlugin', 'Observer', 'ScrollToPlugin', 'CustomEase'].map(n => window[n]).filter(Boolean);
  gsap.registerPlugin(...plugins);
  const mm = gsap.matchMedia();
  // Measure triggers in page order, whatever order this file creates them in: ScrollTrigger refreshes in
  // creation order, so a trigger made before a pin above it misses the pin's scroll length and fires early
  // (L-050; browser_qa errors on starts that disagree with the layout). sort() orders by page position.
  if (window.ScrollTrigger) ScrollTrigger.addEventListener('refreshInit', () => ScrollTrigger.sort());

  // Circuit trace helper (used by the data-gsap="trace" recipe below; reuse it for a project's own traces).
  // The list's ::before is the rail: it draws downward with scroll (--rail 0→1, a scaleY in styles.css). Each
  // item's node pseudo (`pseudo`) pops in the moment the rail reaches its centre. Lighting follows the rail
  // tween's own progress and the node positions are measured from the CSS, then re-measured on every
  // ScrollTrigger refresh, so a node never lights ahead of the rail at any width.
  // Returns a cleanup for the matchMedia callback.
  const trace = (list, items, { pseudo = '::before', scrollTrigger }) => {
    let marks = [], span = 1;
    const measure = () => {
      const inset = parseFloat(getComputedStyle(list, '::before').top) || 0;
      span = Math.max(1, list.offsetHeight - 2 * inset);
      marks = items.map(el => {
        const node = getComputedStyle(el, pseudo);
        return (el.offsetTop + parseFloat(node.top) + parseFloat(node.height) / 2 - inset) / span;
      });
    };
    // An item that is itself moving (a scrubbed rise, y) carries its node with it: light at its current spot.
    // The node pops with GSAP (--node 0→1, read by the pseudo's scale in styles.css); .is-lit records the state.
    // overwrite 'auto', not true: true would also kill other tweens on the item (a scrubbed rise).
    const light = p => items.forEach((el, i) => {
      const on = p >= Math.min(0.98, marks[i] + (+gsap.getProperty(el, 'y') || 0) / span);
      if (on === el.classList.contains('is-lit')) return;
      el.classList.toggle('is-lit', on);
      gsap.to(el, { '--node': on ? 1 : 0, duration: on ? 0.35 : 0.2, ease: on ? 'back.out(3)' : 'power2.in', overwrite: 'auto' });
    });
    measure();
    list.classList.add('is-tracing');
    gsap.set(items, { '--node': 0 });
    // A function, not an arrow on `rail`: the first render runs onUpdate before `rail` is assigned
    const rail = gsap.fromTo(list, { '--rail': 0 }, { '--rail': 1, ease: 'none', scrollTrigger,
      onUpdate() { light(this.progress()); } });
    const onRefresh = () => { measure(); light(rail.progress()); };
    ScrollTrigger.addEventListener('refresh', onRefresh);
    return () => {
      ScrollTrigger.removeEventListener('refresh', onRefresh);
      list.classList.remove('is-tracing');
      items.forEach(el => { el.classList.remove('is-lit'); gsap.killTweensOf(el, '--node'); el.style.removeProperty('--node'); });
    };
  };

  // Entrance moments replay every time they come back into view, scrolling down or up (the user's standard,
  // 2026-10-09). A moment plays once its trigger is `at` of the way onto the screen from either edge (0.85: its
  // top passes 85% down the screen, or, scrolling up, its bottom drops past 15%). It resets only when the trigger
  // is fully off-screen, so the reset is never seen. Use on a paused tween or timeline: `paused: true,
  // scrollTrigger: inView(el, 0.85)`. The trigger belongs to the animation, so killing it (SplitText re-split)
  // removes both. Exception: things people scroll back and forth to compare (a product grid) play once.
  // Inside a pinned section (mark it data-pin, or the h-scroll recipe; give its pin refreshPriority: 1 so it's
  // measured first), the end moves on by the pin's length: 'bottom top' alone "left" partway through the pin and
  // reset text still on screen (a pinned heading vanished, L-078). pinnedContainer doesn't cover this:
  // ScrollTrigger only offsets triggers that start after the pin does. A reset also waits until the text really
  // is off-screen.
  const inView = (trigger, at = 0.85) => {
    const check = self => {
      const anim = self.animation, r = self.trigger.getBoundingClientRect();
      if (anim && anim.paused() && r.top < innerHeight * at && r.bottom > innerHeight * (1 - at)) anim.restart(true);
    };
    const reset = self => {
      const r = self.trigger.getBoundingClientRect();
      if (self.animation && (r.bottom <= 1 || r.top >= innerHeight - 1)) self.animation.pause(0);
    };
    const box = trigger.closest?.('[data-pin], [data-gsap="h-scroll"]');
    const pinLength = () => {
      const pin = ScrollTrigger.getAll().find(t => t.pin === box);
      return pin ? pin.end - pin.start : 0;
    };
    return { trigger, start: 'top bottom', end: box ? () => `bottom top-=${pinLength()}` : 'bottom top',
      toggleActions: 'none none none none',
      onUpdate: check, onToggle: check, onRefresh: check, onLeave: reset, onLeaveBack: reset };
  };

  mm.add('(prefers-reduced-motion: no-preference)', () => {
    const cleanups = [];

    // ---------------------------------------------------------- split headline
    // <h2 data-gsap="split">…</h2>: words rise out of a line mask as the heading scrolls in.
    // SplitText keeps an aria-label with the full text; autoSplit re-splits when fonts load or the width changes.
    // A re-split rebuilds only that heading's trigger, but its new line count moves everything below it: refresh
    // every trigger once the re-splits settle (L-076: the music shop sample's section triggers drifted 90–170px).
    if (window.SplitText && window.ScrollTrigger) {
      const split = new WeakSet();
      let settle = null;
      const refreshSoon = () => { if (settle) settle.kill(); settle = gsap.delayedCall(0.15, () => ScrollTrigger.refresh()); };
      gsap.utils.toArray('[data-gsap="split"]').forEach(el => {
        SplitText.create(el, {
          type: 'lines,words', mask: 'lines', autoSplit: true,
          onSplit: self => {
            if (split.has(el)) refreshSoon(); else split.add(el);
            return gsap.from(self.words, {
              yPercent: 110, duration: 0.8, ease: 'power3.out', stagger: 0.035,
              paused: true, scrollTrigger: inView(el, 0.85),
            });
          },
        });
      });
      if (document.fonts) document.fonts.ready.then(() => ScrollTrigger.refresh());
    }

    // ---------------------------------------------------------- circuit trace (optional effect)
    // <ol data-gsap="trace">…<li>…</li>…</ol>: a line draws down the list as it scrolls and a node lights at each
    // item: a timeline of years, a process, a build log. Rail and nodes are styled in styles.css (a static trace
    // without motion); nodes use each item's ::before. Only the line and nodes move, never the text (L-047).
    if (window.ScrollTrigger) {
      gsap.utils.toArray('[data-gsap="trace"]').forEach(list => cleanups.push(trace(list, [...list.children], {
        scrollTrigger: { trigger: list, start: 'top 80%', end: 'bottom 55%', scrub: 0.4 },
      })));
    }

    // ---------------------------------------------------------- sticker (optional effect)
    // <span class="badge" data-gsap="sticker">−20%</span>: the badge slaps on like a price sticker as it scrolls
    // in (big and tilted → rest). Scale and rotation only, no fade, so its text is never half-transparent. It
    // waits at 1.9× until it plays: keep it inside a card with overflow: clip, or away from the screen edge,
    // or it widens the page on phones (the motion pass errors on overflow). Never on a .reveal element.
    if (window.ScrollTrigger) {
      gsap.utils.toArray('[data-gsap="sticker"]').forEach(el => gsap.from(el, {
        scale: 1.9, rotation: -16, duration: 0.55, delay: 0.15, ease: 'back.out(2.2)', transformOrigin: '30% 50%',
        paused: true, scrollTrigger: inView(el, 0.85),
      }));
    }

    // ---------------------------------------------------------- project moments
    // Write this site's signature moments here (pinned process story, Flip filter, drawn SVG line, ...).

    return () => cleanups.forEach(fn => fn());
  });

  // ------------------------------------------------------------ scene shapes for QA (L-079)
  // A fixed or background scene (a canvas stage, a big SVG behind the page) whose shapes stand near page text
  // reports where they are, so browser_qa can sweep the page at 1280×720, 1440×900, 1731×860, 1920×1080 and
  // 390×844 and error on a shape over text (a snare met the metronome only in the user's 1731×860 window).
  // Define it where the scene knows its shapes (field.js on the music shop sample); it only reads, never changes the drawing:
  //   window.__motionShapes = () => [{
  //     name: 'snare',            // what the report calls it
  //     x, y, w, h,               // viewport rect (CSS px) of what is drawn now
  //     points: [[x, y], …],      // optional: the drawn points (particles); checked instead of the rect
  //     settled: true,            // optional: false while it still eases toward where the scroll puts it (QA waits)
  //     formed: true,             // fully assembled and settled (not mid-morph, not fading); only these are judged
  //     dim: 0.75,                // optional: how bright it is drawn, for the report
  //   }];
  //   window.__motionShapes.stops = () => [0, 2140, …];  // optional: the scrollY values where each shape stands
  //                                                       // in the place it was set to clear the text
  // Only pages that define it get the sweep: at the stops if given, else every half screen. Give stops when text
  // is meant to scroll on over a held background shape (dimmed) after it has formed in its clear place. Text on
  // an opaque surface (a card, a photo) above a scene behind the page is skipped: the scene can't show through.

  // ------------------------------------------------------------ horizontal gallery
  // <section data-gsap="h-scroll" aria-label="…">
  //   <div class="h-track" data-gsap-track tabindex="0" role="region" aria-label="… (scrolls sideways)">…items…</div>
  // </section>
  // Desktop: the section pins and vertical scrolling slides the track. Phones and reduced motion: the track
  // stays a native swipe row with scroll-snap (styles.css), so nothing is hidden without GSAP. tabindex lets
  // keyboard users scroll that row (axe scrollable-region-focusable).
  if (window.ScrollTrigger) {
    mm.add('(min-width: 900px) and (prefers-reduced-motion: no-preference)', () => {
      gsap.utils.toArray('[data-gsap="h-scroll"]').forEach(section => {
        const track = section.querySelector('[data-gsap-track]');
        if (!track) return;
        section.classList.add('is-h-pinned');
        const distance = () => Math.max(0, track.scrollWidth - section.clientWidth);
        gsap.to(track, {
          x: () => -distance(), ease: 'none',
          scrollTrigger: {
            trigger: section, start: 'top top', end: () => `+=${distance()}`,
            pin: true, scrub: true, invalidateOnRefresh: true, refreshPriority: 1,  // before inView() text inside it
          },
        });
      });
      return () => document.querySelectorAll('.is-h-pinned').forEach(s => s.classList.remove('is-h-pinned'));
    });
    // Late images and fonts change heights after the triggers were measured
    window.addEventListener('load', () => ScrollTrigger.refresh());
  }
})();
