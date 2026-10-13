# Website design & build rules

Lessons from past client site builds (IronCity Rods & Customs, Weknz Patio Furniture and Trevor Travis Motors, 2026-10, and every site since; full log in `LESSONS.md`, one line per lesson in `LESSONS-INDEX.md`). Each rule exists because the mistake actually happened and had to be fixed after the user caught it or a critique flagged it. Apply them to every website project from the first draft, not as after-the-fact fixes.

These rules lived in `~/.claude/CLAUDE.md` until 2026-10-13. They moved here so they load only for website work: `/website` reads this file first, and the `CLAUDE.md` files in `Concept Websites/`, `Portfolio Site/` and this pipeline say to read it before any work there. (Plain instructions, not `@` imports: an import that points outside the session's folder asks the user for approval in every new site.) Older lessons that cite "CLAUDE.md › <section>" mean the same section here. Paths: `<workspace>` = `C:\Users\Administrator\Desktop\Claude Workspace`, `<pipeline>` = `<workspace>/Workflow and Pipeline/website-pipeline`.

## Pipeline & questions
- **New or continuing client sites run through the `/website` skill** (source: `<pipeline>`; launcher: `Desktop\New Website.cmd`). Its shared `tools/qa.py` and `tools/browser_qa.mjs` enforce most rules below; when a new lesson is learned, add the check there too.
- **Most sites are portfolio samples for now** (`Project type: sample` in BRIEF.md). A thin brief gets a plausible fictional business with 555-01xx numbers, and essentially no questions. Real client sites (`client`) are facts-only. Never invent reviews or claims about a *real* business, even in a sample.
- **A finished site reopened by the same name: ask "redesign it?" before anything** (user, 2026-10-10, L-057). No = do nothing, not even QA, a tool sync or a deploy. Yes = start it exactly like a new site (L-058): tag the old version in git, archive the old site and its BRIEF.md to `_temp`, reset BRIEF.md to the blank template, keep client-assets, open the brief form window (`brief-form/brief_form.py`) and wait for the user's "Start building". Never redesign on my own from the old brief. Unfinished projects still resume, and a phase arg (`qa`, `deploy`…) or a stated change runs as asked.
- **Record every mistake so it never repeats.** This applies on any website project, inside or outside `/website`, whenever the user corrects something, QA, a critique or a reviewer flags a first-draft error, or I notice a wrong assumption or misused tool. Log it straight away in the project's `PROJECT.md` › Mistakes. When it's user-caught or there won't be a handoff, also add it to `<pipeline>/LESSONS.md` and rerun `python dev/lessons_index.py`. Then enforce the fix as strongly as possible: an automated check in the shared tools, a rule here, or a pipeline step. Read `LESSONS-INDEX.md` before starting any website work, and open the full LESSONS.md entry for each lesson that applies.
- **Copy contact values (URLs, handles, phone, email) from the brief; never retype them.** A retyped Instagram handle was shown to the user with a typo.
- **Ask only on critical matters:** identity that can't be inferred, outward-facing or irreversible actions (production deploys, domains, real form inboxes, spending, deleting), legal or factual claims only the client can confirm, and genuinely conflicting instructions. Batch them into one question round. Decide everything else (design, copy, structure, tooling, QA fixes), log it, and report it at handoff.

## Imagery
- **Never repeat a photo anywhere on the site.** Keep a running allocation list (image → page/section) and grep `<img src` across all pages before handoff. Fill gaps with new stock photos. Only knowingly repeat one (e.g. a listing preview that mirrors the full listing), and tell the user. Near-duplicates count as repeats: two shots from one shoot or of the same view (Macz had groundbreaking shovels and helmets, and two renders of one dining room).
- **No third-party brand logos on images** (presentation boards, signage, renders). They read as endorsements; crop them out or skip the image.
- **Inspect every hero and banner photo at its real crop and breakpoint.** Look for text, license plates, logos or watermarks sitting behind headlines; one hero had a "BMW M4 Coupé" plate behind the title.
- **Never crop the subject.** Cut-out images (cars, products, people) must show the whole subject at every width. Fix the source crop; don't hide it with oversize scaling or negative margins (a Camaro's roof was cut off).
- **Real client photos go in prominent spots; stock photos fill in.** Stock that contradicts the locale or story (foreign plates, palace backdrops, the wrong kind of car) erodes authenticity.
- **Callouts and annotations on photos must point at a part the photo shows.** Check each pin on a % grid over the full-size image before writing its copy; a "chain" callout once sat on the exhaust.
- Unsplash search sits behind a bot check: don't bypass it. Download by known photo ID: `https://images.unsplash.com/<photo-id>?w=1600&q=72&fm=jpg&fit=max`.
- **Cut-outs on dark backgrounds: no white halo.** Pull the edge in past the light rim and recolour it from the interior; check the edge zoomed in on the real background (L-038; `qa.py` checks it).

## Visual identity
- **Glows are allowed** (user, 2026-10-12; this replaces the old no-glow rule): radial halos, colored box-shadow glows and light blooms, on any site. The condition is contrast. Text over or beside a glow still passes 4.5:1 (3:1 for large text), graphics 3:1. A glow never washes out a photo's subject or the text sitting on a photo. `browser_qa.mjs` measures text over glows on screen and errors on a failure. Use them where they serve the identity, not by reflex on every card.
- **Start the palette from the logo** and use the client's own tagline and voice. Weknz went green with a sky/sand logo.
- **Center sticky sub-navs and pill bars:** `width: fit-content; max-width: 100%; margin-inline: auto`.
- **Build the identity from the business's own story:** heritage, owner, real work, location. Don't default to category template patterns: a small label above or below every heading (L-073), icon-tile card rows, a scrolling brand-name marquee, hero stat tiles, three testimonial cards in a row. Cover the logo and ask: could this be any competitor's site?
- **Design from the library when there's no inspiration image** (user, 2026-10-10). Before designing any site, read `<pipeline>/design-library/` (README, `patterns.md`, the closest site entries). Recombine and adapt its patterns to this business; never clone a past site whole. Every finished site gets an entry added there.
- **Keep the positioning true.** A craftsman or builder shop must not read as a discount dealer (e.g. struck-through "was" prices, "most wanted rides" copy).
- **One primary CTA label and style sitewide**, plus the phone number. Everything else is a ghost button or text link. Don't invent cute per-section labels that all go to the same form.
- Give the homepage a closing call-to-action beat; don't end on hours and a newsletter.
- **Headline line-height 1.05 or more** (1.1 for serifs with long descenders). Check every wrapped headline: a .98 heading put the "j" of "project" on the "?" below it (L-051; `qa.py` errors below 1).

## Copy & content
- **Answer the buyer's pre-contact questions on the site:** price or how pricing works, timeline, delivery or logistics, warranty, where to find them, and what happens after they get in touch. Both 2026-10 critiques flagged these as missing.
- **Claims must be unambiguous and consistent.** Read every number as a skeptical buyer: "0% Sales commission" read as 0% financing. Pricing claims agree across pages: "Free quote" contradicted Time & Materials billing. Review headlines quote what the review says.
- **Homepage of about 8 sections; each idea once.** Pages ran 11,700–14,000px tall on phones, with benefits repeated four times and the gallery on three pages.
- **No dead-end features:** a save/bookmark toggle needs a place to view saved items, or it doesn't ship.

## Mobile (check every page at 390px and 1440px for horizontal overflow)
- **Local businesses get a tap-to-call button in the mobile header.** On mobile contact pages, show the phone option before the long form.
- **Badges and pills must not wrap at 360–390px.** Use `white-space: nowrap` and hide secondary info (e.g. the location) on small screens.
- **Icon + text rows** (address, phone, email): `display: inline-flex; align-items: center; gap`, and `flex: none` on the icon so it never drops to its own line.
- **Long unbroken strings** (emails, URLs): add `<wbr>` before the `@` *and* use `overflow-wrap: anywhere` so they don't break mid-word or overflow. Never use `break-word`: it cut emails off in a grid row on the user's phone (L-070).
- **Hours and spec tables:** `white-space: nowrap` on values and a grid that keeps label and value columns aligned.
- Keep the hero CTA above the fold on an 844px-tall phone.

## Forms & data
- **Qualifying selects** (service, vehicle, budget) must start on an empty "Choose…" option. Never submit or prefill defaults the visitor didn't choose; disable empty fields on submit and re-enable them on `pageshow`.
- **Guard every URL-param prefill against null/empty** (a message once read "Hi, I'm interested in the null").
- **Conditional requirements:** whatever reply route the visitor picks becomes required: Phone or Text → phone number, Email → email (L-072: an "Email" choice with an empty email field sent a lead nobody could answer).
- **Anything styled like a control is a real control** (swatches, chips, toggles, steppers, tabs): it does what it suggests, starts with nothing chosen, and its value is carried into the reserve, cart or form. If it isn't a choice, restyle it as plain text (L-042: look-only colour swatches lost the colour on reserve).
- **Every contact form says what happens next** (who replies, how fast) right above the submit button.
- **Never `action="mailto:"`.** It fails silently. Phone fields are `type="tel"` with a pattern. `og:image` is an absolute URL.
- **Generated labels must read as human data.** Never truncate slugs into IDs (e.g. "IC-FERRARI-").
- **Placeholders and demo modes must be listed for the user, never presented as working:** `href="#"` social/legal links, a newsletter that "succeeds" without a backend, form endpoints like `YOUR_FORM_ID`, fake reviews.

## Accessibility & performance
- **Check contrast on every surface a color token appears on**, not just the page background. Grey secondary text and red link text passed on the page background but failed 4.5:1 on raised cards. Small text must be ≥4.5:1 everywhere.
- **Every dark surface flips text *and* graphics to light ink.** That means night sections, photo bands, page heads and the hero, through one shared selector or token, never a single class like `.on-night`. Icons, dividers and strokes need ≥3:1 against what's actually behind them, photos included. A dark-brown logo divider sat invisible on a dark photo band and the user had to circle it (L-031).
- **Text on photos: check it at phone width too.** Left-to-right scrims tuned at 1440 leave phone text over the light end of the photo. Give every text-on-photo band a solid mobile scrim on its base class (L-032).
- **Text on a saturated brand red is pure white.**
- **All animation runs in JavaScript, never CSS** (user, Gadget Zone 2026-10-09). This applies to every site, GSAP or not. CSS only describes states (open/closed, scrolled, shown/hidden); hover colour changes switch instantly. No `transition`, `animation` or `@keyframes`, including inline styles; `qa.py` errors on them. UI motion uses the template's `main.js` `morph()` (Web Animations API, from the current look to the new CSS state); GSAP sites may do it in `motion.js` instead.
- **Animate only `transform` and `opacity`**, never `height`, `inset` or `width`. A shrinking sticky header keeps a fixed-height bar, slides up with `translateY`, scales the logo with `scale()`, and fades in a `::before` backdrop.
- **Parallax default: 50% scroll speed.** When the user asks for parallax, apply it to every full-bleed photo (hero, page heads, photo bands) at 50% unless they name another speed. Use the template's `[data-parallax]` mechanics (`main.js` SPEED = 0.5; CSS sizes band images `max(100%, 50% + 50lvh)`, top-of-page headers 100%). Verify by scrolling at 390 and 1440: no gaps at the frame edges, and recheck the crops.
- **GSAP is opt-in**, at three levels set by `GSAP motion:` in BRIEF.md (or the user asks):
  - `no` (default): no GSAP.
  - `yes`: 1–3 story-driven moments below the fold.
  - `advanced` (user, 2026-10-12): a full award-site motion system with no moment cap, e.g. an intro loader, one morphing canvas scene behind the page, line-by-line text reveals on all copy, smooth wheel scrolling, pinned stories and glows. If a motion reference site is named, copy its effects. The reference build is the music shop sample's Dala pass (SKILL.md › Direction). A fixed scene's shapes that sit near page content are anchored to that content's measured position, not viewport fractions. Check them where each is fully formed at 1280×720, 1440×900, 1920×1080 and 390 (L-079: a particle snare met a metronome only in the user's 1731×860 window). Such a scene defines `window.__motionShapes()` (and `.stops()` for the scroll positions where each shape stands in its place; convention in the template's `motion.js`). `browser_qa.mjs` then sweeps the page with motion on at 1280×720, 1440×900, 1731×860, 1920×1080 and 390×844 and errors on any formed shape over visible text.

  Every level uses the template's self-hosted copy (`site_config.GSAP`, `assets/js/motion.js`) and keeps everything inside a `gsap.matchMedia()` reduced-motion gate. Tween transform/opacity only, never an element `main.js` already moves (`.reveal`, `data-parallax`, header, mobile nav), and no ScrollSmoother unless asked (smooth scrolling on `advanced` uses a `gsap.ticker` wheel smoother). Every level also needs: Lighthouse mobile ≥90, the hero headline visible at load, and text readable over every moving layer at 390 and 1440. `browser_qa.mjs` runs a motion-on pass. The official `gsap-skills` plugin is the API reference; where it conflicts with these rules or the pipeline (npm/CDN installs, ScrollSmoother), the pipeline wins.
- **Entrance animations replay** each time they come back into view, scrolling down or up, and reset only once fully off-screen (user, Gadget Zone 2026-10-09). The template does this by default: `main.js` `REPLAY` for `.reveal`, `motion.js` `inView()` for GSAP moments. Scroll-linked (scrubbed) motion follows the scroll anyway. Exception: lists people scroll back and forth to compare (a product grid) play once; say so at handoff.
- Respect `prefers-reduced-motion` for marquees, reveals and parallax.
- **Speed and local search are part of done.** Aim for Lighthouse mobile ≥90 on every page, with LCP under 2.5s: compress hero images and don't lazy-load above the fold. Self-host web fonts (never link fonts.googleapis.com) and serve phone-sized images: the template build makes WebP `srcset`s, and images in multi-column grids need a `sizes` that matches their columns (L-039). Every local business gets LocalBusiness JSON-LD matching the site's name and phone, unique titles and descriptions (the homepage's naming the town), a share image and a favicon. `browser_qa.mjs` (axe + Lighthouse) and `qa.py` check these.

## Process & tooling (website)
- **Generated sites:** edit the source (`_src/` pages, build script) and rebuild. Never hand-edit generated output.
- **The pipeline tools are shared** (2026-10-13; replaces L-033's copy-back rule). The one copy lives in `<pipeline>/tools/`; each site's `tools/` holds stubs that run it. Fix and extend tools there, never in a site. After changing a check, run `dev/selftest.py` (every planted defect must still be caught).
- **Every site and the pipeline are git repos** (2026-10-13). Commit after each finished phase or round of changes, and commit pipeline changes with the lesson ID. Before a redesign, `git tag previous-<date>`. No pushes or history rewrites; there is no remote. Commit messages use one `-m` per paragraph, never a heredoc (L-027).
- **For scrolled states of fixed headers,** the page's scroll handler can strip test classes. Pin `scrollY` before adding the class.
- **Template tokens don't nest.** A helper reads BIZ itself; never pass `{{TOKEN}}` as a helper argument (the build warns).
- **Preview deploys (Netlify or Cloudflare, which deploys a static-assets Worker since Pages became part of Workers):**
  - Deploy only built files plus a `_headers` file with `X-Robots-Tag: noindex, nofollow`; leave out the source folders.
  - Pick the host with `Deploy host:` in BRIEF.md (`cloudflare` by default, or `netlify`), or override it with `tools/deploy.py --host`.
  - New Netlify sites on a team get "team login" protection (401). `tools/deploy.py` switches it off for the preview site it just created and re-checks; confirm the 200 in its output.
- **Replaced a long-cached file? Give it a new name.** A same-name swap left the user's desktop on the old headshot (L-037; `deploy.py` refuses it now). When the user describes something my screenshots don't show, suspect a stale cache on their device and look at their screenshot before redesigning anything.
- **Before handoff:** one batched desktop+mobile screenshot pass, then an `impeccable critique` / `detect` run. Fix real findings; call out detector false positives instead of chasing them.
