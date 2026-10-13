---
name: website
description: End-to-end client website pipeline (intake → direction → build → QA → preview deploy → handoff) that runs on autopilot and only stops for critical questions. Use when the user runs /website, asks to start/build/continue a client website, or runs it inside a folder created by the "New Website" launcher. Args - free-text business info to start, or one of - status | qa | deploy | handoff.
---

# Website pipeline

You run a client website from raw input to a deployed preview with as little user input as possible. The user's global CLAUDE.md website rules apply to every step. The tools in `tools/` enforce most of them mechanically, so run them instead of re-checking by eye.

## Workspace

Everything lives in one workspace, `C:\Users\Administrator\Desktop\Claude Workspace` (`<workspace>`). Paths below are relative to it; in scripts, derive them from the script's own location (`Path(__file__)`), never a hard-coded Desktop path.

| What | Where |
|---|---|
| Pipeline (`<pipeline>`) | `Workflow and Pipeline/website-pipeline/` (`~/.claude/skills/website` is a junction to it) |
| Sample sites | `Concept Websites/<Name> Website/` |
| The owner's portfolio | `Portfolio Site/` |
| Portfolio screenshots | `Portfolio Screenshots/`: finished-site screenshots only, nothing else |
| Scratch files (test scripts, test screenshots, backups, planted defects) | `_temp/`, never the system temp folder, a project or the template |

## 0. Where am I?

Decide the entry point from the folder state and the args:

| State | Action |
|---|---|
| No `_src/build.py` in cwd | Scaffold: `powershell -NoProfile -ExecutionPolicy Bypass -File "<pipeline>/scaffold.ps1" -Target "<cwd>" -NoLaunch`, then go to Intake. If cwd holds unrelated files, stop and ask (this is a critical question). |
| `PROJECT.md` has every phase ticked (a finished site reopened by the same name) and the args are empty or new-site intake, not a phase arg or a change request | Ask first, before running or changing anything (the user, 2026-10-10, L-057). Use one AskUserQuestion: "<Name> is already finished (preview <URL>). Redesign it?" with **No, leave it** and **Yes, redesign it**. **No:** stop and do nothing, not even a tool sync, QA or deploy. **Yes:** start it exactly like a new site; never redesign on your own from the old brief (L-058). (1) Move everything except `client-assets/` to `<workspace>/_temp/<Name>-previous-<date>/` (an archive, never a delete), including the old `BRIEF.md`. (2) Scaffold again, copy the template's blank `BRIEF.md` in and set its `Business name:` line. (3) Open the brief form, `python "<pipeline>/brief-form/brief_form.py" "<project>"`, as a background command, tell the user the window is open, and wait. Do no direction, library learning, stock search or design work meanwhile. (4) Exit 0 ("Start building"): run the normal new-site process from Intake on the new brief. Exit 3 (closed): stop and say the brief is saved. At handoff, replace the site's design-library entry instead of adding a second one. |
| `PROJECT.md` has unchecked phases | Resume at the first unchecked phase. Say one line about where you're resuming. |
| Resuming or changing any existing project | First sync `tools/` with `template/tools/` (L-052): copy each newer template tool, or port its new checks into a customised copy (keep project-only scripts). `qa.py` warns while one is stale. Also bring in template features the request needs (e.g. GSAP: `h_gsap` in build.py, `{{fn:gsap}}`, `tools/vendor/`, `motion.js`). |
| Arg `status` | Print the phase checklist plus open placeholders. Do nothing else. |
| Arg `learn` | Learn the design images and DESIGN.md files dropped into `<pipeline>/design-library/inspiration/`: follow `design-library/LEARN.md`, then report one line per reference. Do nothing else. |
| Arg `qa` / `deploy` / `handoff` | Run only that phase. |

Free-text args are intake material (business name, phone, links, notes). Treat them the same as `BRIEF.md`.

## Mode: sample or client

`BRIEF.md` › `Project type` sets the mode. It defaults to **sample**, meaning a portfolio piece. An explicit instruction in the args wins.

| | sample (portfolio) | client (real business) |
|---|---|---|
| Missing facts | When the brief is thin, invent a plausible, consistent fictional business: name, story, services, hours. Use 555-01xx phone numbers and `example.com` emails so nothing reaches a real person. | Never invent. Use placeholders and `data-todo`. |
| Reviews, stats, credentials | Fine for a **fictional** business; list them as fictional at handoff. If the sample uses a **real** business, use only real public facts: no invented reviews, claims or prices about real people or companies. | Only what the client supplies. |
| Questions | Almost none: only deleting files, spending money, contacting the real world (real inboxes, real phone numbers), and critical design critiques (#5). | The full question policy below. |
| Forms | Demo mode is fine. | A real endpoint is needed; ask if it's missing. |
| Deploy | noindex preview | noindex preview; production only on request |
| Handoff extra | Portfolio screenshot (see Handoff) | Placeholder list written for the client |

## Operating rules

- **Autopilot.** Move phase to phase without asking "shall I continue?". After each phase, tick it in `PROJECT.md` › Status. That makes the run resumable after compaction or a new session.
- **Questions follow the policy below. Everything else is a decision:** make it, add one line to `PROJECT.md` › Decisions (what + why), and keep going.
- **Client mode: never fabricate client facts.** That covers testimonials, review counts, years in business, licenses, certifications, prices, guarantees, awards and team names. If the material isn't in the inputs, write the copy so it doesn't need the fact. If it's genuinely needed, mark the element with `data-todo="what's needed"` so QA lists it for handoff. Sample mode follows the Mode table.
- **Log every mistake the moment it happens** in `PROJECT.md` › Mistakes. Don't wait for handoff; context may be compacted before then. A mistake is anything the user corrects, any first-draft error that QA, a critique or the reviewer flags (log one entry per type, not per instance), and any wrong assumption or misused tool. Each entry records what happened, who caught it, the root cause, the fix, and how to prevent it.
- **Source of truth:** edit `_src/` (pages, partials, `site_config.py`) and `assets/`, then run `python _src/build.py`. Never edit `dist/`.
- **Scripted edits (L-027):** single changes use Edit. Several replacements at once go in a Python script written with Write (into `<workspace>/_temp`), never a shell heredoc. The script exits unless each match count is exactly 1, and checks every file before writing any of them. Afterwards, `py_compile` any edited `.py` and rebuild.
- **Context hygiene:** run tools and read their *reports* (`qa/*.md`), not raw output. Query long reports, logs and listings through context-mode (`ctx_execute_file` / `ctx_batch_execute` with a question such as "errors and warnings only") instead of reading them whole. Look at screenshots with the Read tool. Never dump whole HTML files into the conversation.

## Question policy (critical matters only)

Ask **only** when one of these is true. This is client mode; in sample mode only #2 and #5 apply, and a noindex preview never needs asking.

1. **Identity unknowable.** You can't tell from any input or public source what the business does, where it is, or who it serves. A wrong guess would mean rewriting the site.
2. **Outward-facing or irreversible.** Production deploys, custom domains, connecting a form to a real inbox, anything that spends money, deleting user files. A noindex preview deploy is pre-authorized when `BRIEF.md` says `Deploy preview: yes`.
3. **Legal or factual claims** the site would make that only the client can confirm (licensing, pricing, warranties). Default to leaving them out. Ask only if the brief makes them central.
4. **Conflicting instructions** between the brief, the user's messages and CLAUDE.md, where both readings are plausible.
5. **Critical design critique.** An impeccable critique or the finish reviewer reports a P0 (Blocking) or P1 (Major) issue. Follow the critique gate below. This is the only question allowed mid-build.

How to ask:
- **One batch, at the end of Intake.** Use a single AskUserQuestion with 1–4 questions. Put the recommended answer first, marked "(Recommended)". Never ask mid-build, except at the critique gate (#5). If a blocker turns up later, use a clearly marked placeholder, log it under Deferred questions, and surface it at handoff.
- **Never ask about:** palette, fonts, layout, copy tone, page list, which stock photos, section order, tech stack, file names, or whether to fix a QA finding. Decide those. The only exception is a P0/P1 critique finding (#5).
- **If nothing is critical, ask nothing.** Say "No blocking questions; proceeding" and continue.

### Critique gate (impeccable findings)

Use impeccable's own severity scale (P0 Blocking, P1 Major, P2 Minor, P3 Polish). Rate each finding-reviewer item on the same scale.

- **P2/P3 (minor): don't fix them; proceed.** Log one line per finding in `PROJECT.md` › Decisions: "skipped: minor (P2/P3), <finding>".
- **P0/P1 (critical): stop and ask before changing anything.** Use one AskUserQuestion batch with up to 4 questions. Write one question per finding, or group them by class if there are more than 4. Each question says what's wrong and where (page, section, screenshot file). It offers 2–3 concrete fix options, with the recommended one first and marked "(Recommended)", plus "Leave as is". Then apply the user's choice to the whole class sitewide (L-016), rebuild, and log the choice in Decisions.
- **Re-check:** re-run the same critique once after applying the choices. Any new P0/P1 goes through the gate again; minor findings are skipped as above.
- **Not part of the gate:** objective rule violations that `qa.py`, `browser_qa.mjs`, LESSONS.md or CLAUDE.md already forbid, such as contrast below 4.5:1, overflow, a repeated photo, a glow that drops the text over it below contrast (glows themselves are allowed), a cropped subject, or a select prefilled with a default. Fix those automatically whatever severity the critique gives them, because they are defects, not design choices. `impeccable detect` flags count as minor unless they hit one of these rules. Note known false positives (L-000) as before.

## Phases

### 1 · Intake

0. Read `<pipeline>/LESSONS.md`. Every lesson in it applies from the first draft. Copy the ones most relevant to this project into `PROJECT.md` › Mistakes › "Watch for".
1. Read `BRIEF.md`, the args, and everything in `client-assets/`. **Open every photo** with Read and catalogue it in `PROJECT.md` › Assets. Record the subject, its quality, any problems (plates, logos, clutter, crop), and the best slot for it (hero/feature/gallery/skip). Third-party brand logos on an image (boards, signage, renders) read as endorsements: mark it "crop before use" or skip (L-028). Note which photos come from the same shoot or show the same view (L-029).
2. If links were given (existing site, Google Business Profile, Facebook), fetch them and extract facts: services, service area, hours, story, owner, years, real projects. Cite the source next to each fact in `PROJECT.md` › Facts.
   - Save captions, reviews and owner quotes **verbatim** to a sources file (e.g. `client-assets/sources.md`). Copy quotes from it; never retype or paraphrase one from memory (L-007).
   - Record each project's **credit line** (designed by / built by / year) in Facts. A project the business only built is never "designed by" it.
3. Optimize client photos: `python tools/optimize_images.py` (client-assets → `assets/img/client/`, EXIF-rotated, max 2000px).
4. Fill `_src/site_config.py`: BIZ, HOURS, SERVICES, PRIMARY_CTA, PAGES, FORM_ENDPOINT, SEO. Unknown contact values stay `""`. The build leaves them as visible `{{TOKEN}}` placeholders and QA reports them.
   - **Contact form.** Copy `Form endpoint:` from the brief into `FORM_ENDPOINT`: blank = demo mode; `netlify` = Netlify Forms (only with `Deploy host: netlify`; qa.py errors otherwise); `web3forms:<access key>` = Web3Forms on any host (the inbox owner makes the key at web3forms.com); or a Formspree-style URL. `{{fn:form_fields}}` adds the matching hidden fields and spam trap. Never pick or wire a real inbox yourself: a blank brief stays in demo mode and goes on the handoff list. In client mode, which inbox gets the messages is an ask. Copy `Online booking link:` into `BOOKING_URL`; `{{fn:booking}}` shows it on the contact page beside the call button.
   - **GSAP motion.** Optional, off by default. Only when the brief says `GSAP motion: yes` or `advanced` (or the user asks), set `GSAP` to the plugins the planned motion needs, e.g. `["ScrollTrigger", "SplitText"]`. Leave it `[]` for `no`: the site keeps the template's lightweight reveals and parallax and ships no GSAP.
   - **Local SEO.** `SEO` feeds the homepage's LocalBusiness JSON-LD: the most specific true schema.org `TYPE`, plus region, postal code, country and areas served. Copy the Google Business Profile link (and any Yelp-type listing) from the brief into `SAME_AS`; social URLs in BIZ are picked up automatically. Write HOURS as `("Mon–Fri", "8:00 AM – 6:00 PM")` so the build can read them; it warns about any row it can't.
5. Apply the question policy. Ask the batch if needed. Write the answers into Facts.

### 2 · Direction

0. **Read the design library first.** If `python "<pipeline>/dev/learn_prep.py" --check` prints more than 0, the user has dropped new reference images or DESIGN.md files: learn them first (`design-library/LEARN.md`). Then read `<pipeline>/design-library/README.md`, then `patterns.md` and the one or two site entries closest to this business. It records every past site's layout, palette, type and motion, what the user praised or corrected, and the inspiration images they supplied. When the brief has no inspiration image, the library sets the quality bar and the pattern vocabulary.
   - Combine patterns from different entries and adapt them to this business's story.
   - Never clone a past site's homepage order, palette or type pairing whole: the competitor test applies to our own past work too.
   - If the brief does come with an inspiration image, save a copy as `design-library/inspiration/<slug>-*.webp` and note in Direction what you took from it and what you changed.
   - If the brief names a DESIGN.md (a design-system file, e.g. from Refero Styles, in `client-assets/` or already in the library), copy one from `client-assets/` into `design-library/inspiration/` and learn it first (`learn_prep.py` files it in `inspiration/design-md/`). Then build from its reference entry: take its type scale, spacing, radii, component styling and motion feel, but keep the palette from the client's logo and the identity from this business's story. Swap any face that can't be self-hosted for the entry's alternative, and port its motion to `morph()` / `motion.js` (no CSS transitions). Note in Direction what was taken and what was changed, and run the competitor test against the source brand too: the site must not read as that brand's.
1. Invoke the `ui-ux-pro-max:ui-ux-pro-max` skill to design the visual direction, with `PROJECT.md` as the brief. Search its data for this business's category: style, palette and reasoning profile, font pairing, UX guidelines. Treat the results as **candidates to adapt, not a template to apply**. The rules below override anything it suggests. Keep `impeccable` for critique and review only (step 4.1 and section 5), so the design is judged by a different skill than the one that made it.
   - **Start from the brand's own assets.** Sample the logo's colours and use the client's own tagline and voice. Log any departure in Decisions (L-005).
   - Build the identity from **this** business's story: heritage, owner, real work, place. Never reuse a previous site's or a template's structure.
   - Run the competitor test: cover the logo and ask whether this could be any competitor's site. If yes, push further.
   - No eyebrow labels over most headings, no icon-tile rows, no marquee. `qa.py` blocks all three (L-015).
   - Check the display font's figures before using it for numbers (step numerals, stats, dates). Some display faces draw 0 like O and 1 like I; set numerals in the body face with `tabular-nums` if so (L-003).
2. Write the direction into `PROJECT.md` › Direction: what ui-ux-pro-max suggested and what was kept, changed or rejected (and why), then the concept, type pairing, palette with every text/surface pair's contrast ratio, imagery rules, motion rules, and the signature elements that make it this business.
   - **GSAP on:** plan 1–3 signature moments from this business's story (a restoration told as a pinned sequence, a project gallery that slides sideways, a headline that sets the tone). Use the moments named under `Must have`; otherwise pick them. Never animate every section. ui-ux-pro-max's GSAP presets are candidates, like its other data. Write each moment, its page and section, and its reduced-motion and phone fallback in Direction.
   - **GSAP advanced** (`GSAP motion: advanced`): a full motion system instead of 1–3 moments, at the level of an award-site build. Reference: the music shop sample's Dala pass (design-library `patterns.md` › Advanced motion system). If the brief names a motion reference site under Style references, study it in a browser first and list each of its effects in Direction as copied, adapted or skipped (and why). Otherwise plan from this vocabulary, built around the business's own objects and rhythm:
     - an intro loader once per session (sessionStorage);
     - one persistent canvas scene behind the page that morphs per section (`data-stage` keys);
     - masked line-by-line reveals on headings and body copy;
     - smooth wheel scrolling on fine pointers via `gsap.ticker` (not ScrollSmoother, which isn't vendored);
     - pinned or scrubbed story sections;
     - sticky blurred sub-navs with a scroll-spy;
     - glows (allowed, see the contrast rule).
     The house rules still hold, with no exceptions:
     - JS only, transform/opacity only;
     - every effect gated on reduced motion, with a still fallback;
     - the hero headline visible at load;
     - Lighthouse mobile ≥90 and LCP <2.5s;
     - text readable over every moving layer. Sweep every scene state at 390 and 1440 with its section's text on screen, and dim the scene on phones where text runs full width.
     - After any SplitText re-split, refresh every ScrollTrigger (L-076).
3. Set the tokens and fonts in `assets/css/styles.css`. The template's CSS holds rule-encoded *mechanics* (header, forms, nowrap utilities). Restyle freely, but keep those behaviours.
   - **Self-host web fonts (L-039).** Never link fonts.googleapis.com: its CSS and font files cost two render-blocking round trips (~1.7s of mobile LCP on Macz). Run `python tools/self_host_fonts.py "<css2 URL>" --preload "Body:400"` (preload only the body face, plus the display face if headlines are the LCP) and set `FONTS = (Path(__file__).parent / "partials" / "fonts.html").read_text(encoding="utf-8")` in `site_config.py`. `qa.py` warns on a Google Fonts link.
4. Only if `BRIEF.md` says `Pause for direction review: yes`: build the homepage, screenshot it, and stop for review. Otherwise continue.

### 3 · Content & imagery

1. Finalise the sitemap in `PAGES`. Local service businesses usually get Home, Services, About, Service Areas or Work, FAQ, Contact and 404. Fit it to what the business actually has; don't pad.
   - The homepage has about 8 sections.
   - Each idea appears once on the site. Never repeat a section (gallery, benefits) across pages (L-009).
2. Write the copy from Facts. Use concrete specifics, the client's own wording where available, and no filler superlatives. Keep the positioning true to the business: a craftsman isn't a discount dealer.
   - **Buyer questions (L-008).** List in `PROJECT.md` what a buyer needs before contacting: price range or how pricing works, timeline or lead time, delivery or logistics, warranty, where to find them, and what happens after contact. Answer each on the site (FAQ, service pages, near the form). Client mode marks unknowns with `data-todo`.
   - Set `NEXT_STEPS` (who replies, how fast, what happens next). In client mode the client confirms it, because it's a promise.
   - **Titles and descriptions.** Each page gets its own `title` (up to ~60 characters) and `desc` (70–160 characters). The homepage's pair names the town (`CITY`): local searches match on it. `qa.py` checks all three.
   - **Fact allocation (L-009).** Before writing, list in `PROJECT.md` which page is the home of each fact, quote and project story. Other pages link to it instead of retelling it. `qa.py` warns when 8+ identical words appear in the `<main>` of two or more pages; list deliberate repeats (e.g. `NEXT_STEPS` on the form and in an FAQ) in `ALLOW_REPEAT_TEXT`.
   - **Honesty pass (L-007).** Read every number and claim as a skeptical buyer. "0% commission" must not read as financing. Pricing and process claims must agree across pages. Review headlines quote the review. Every quote matches the sources file word for word. Every "we designed/built X" matches that project's credit line. Cut any process promise that isn't in Facts.
3. **Images:** client photos go in the prominent spots first. Record in the allocation what each photo literally *shows* (product type and material, era, locale) and whether it matches what the business sells (L-006). Fill gaps with stock: `python tools/fetch_stock.py <unsplash-photo-id|pexels:ID|image-url>:<name> ...`. That writes `assets/img/stock/` and `CREDITS.csv`. Unsplash search sits behind a bot check: find IDs another way (WebSearch, Pexels), never bypass it. **Open every downloaded image** and reject any with the wrong locale, the wrong product (wicker for a poly-furniture maker), plates, logos, or text where a headline will sit. Write each `alt` only after opening that photo, from what it shows, and rewrite any alt drafted for a planned shot (L-074). Never bury a real client photo under a heavy overlay; fix text contrast with placement or a local scrim. If `BRIEF.md` says `AI image prompts: yes`, write `client-assets/image-prompts.md` instead: one style brief, then one prompt per missing slot, each with its target filename.
4. Plan the image allocation (image → page/section) in `PROJECT.md` before building. Never repeat a photo. Near-duplicates (same shoot, same view) count as repeats unless they're shown together as one set (L-029).
5. **Share image and favicon.** Make `assets/img/og.jpg` (1200×630, a crop of the hero with no text near the edges) and set `SEO["OG_IMAGE"]`. It's used only for link previews, so it doesn't count as a repeat. Make `public/favicon.svg` from the logo; the build warns while it's missing.

### 4 · Build

1. Build the **homepage first**: `python _src/build.py`, then `node tools/browser_qa.mjs index.html`. Look at `qa/shots/index-390-fold.png` and `index-1440-fold.png`. Run `impeccable critique` on it and put the findings through the critique gate (P0/P1 → ask; P2/P3 → skip). The homepage sets the system for every other page.
2. Build the remaining pages in the established system. When a grid mixes wide or tall items, set their row and column spans so every row fills (L-003). Give the homepage a closing CTA beat. Use one primary CTA label and style sitewide, plus the phone number. Everything else is a ghost button or a text link.
3. Rebuild after every batch of edits. The build warns about unresolved tokens, missing images and empty BIZ values; fix or log each one.
   - **All animation is JavaScript (the user's standard, 2026-10-09), GSAP or not.** CSS only describes states (open/closed, scrolled, shown/hidden, hover colours, which switch instantly); `qa.py` errors on any CSS `transition`, `animation` or `@keyframes`, including inline styles. For UI motion (a menu, a toast, an accordion icon, a hover lift), toggle the state inside `main.js`'s `morph([{ el, props }], change)`. It animates from the current look to the new CSS state with the Web Animations API, handles interruption, and does nothing extra under reduced motion. Keep to transform and opacity. GSAP sites may instead do all of it in `motion.js` (Gadget Zone).
4. **GSAP moments (only when `GSAP` is set).** Write them in `assets/js/motion.js`. The build loads it after `main.js` and the self-hosted GSAP files from `tools/vendor/gsap/` (v3.15, standard no-charge licence; never a CDN). It has four ready recipes, each optional (add the attribute to use it):
   - `data-gsap="split"` on a heading: words rise out of a line mask.
   - `data-gsap="h-scroll"` with a `data-gsap-track` row: a pinned sideways gallery that stays a swipe row on phones.
   - `data-gsap="trace"` on a list (timeline, process, build log): a line draws down it and a node pops (GSAP tweens `--node`) at each item; a static trace without motion. For a project's own trace (nodes on `::after`, other breakpoints), call the `trace()` helper rather than rebuilding it: it keeps every node in sync with the line (L-049).
   - `data-gsap="sticker"` on a badge: it slaps on big and tilted, with no fade. Keep it inside an `overflow: clip` card or away from the screen edge, because it waits at 1.9×.

   Rules (`qa.py` and the `browser_qa.mjs` motion pass check them):
   - Everything sits inside the `gsap.matchMedia()` reduced-motion gate, and the page must read fully without it.
   - Tween only transform and opacity (`x`, `y`, `xPercent`, `yPercent`, `scale`, `rotation`, `opacity`/`autoAlpha`).
   - Never target an element with `.reveal` or `data-parallax`, because `main.js` already moves it. Animate a child or wrapper instead. Exception: when the user wants all motion in JavaScript, the project hands the reveals to `motion.js`: its `main.js` adds `.gsap-motion` to `<html>` (when motion.js is on the page) and skips its own reveals, the reveal CSS is scoped to `.js:not(.gsap-motion)`, and the motion pass then accepts tweens on `.reveal`. Copy it from Gadget Zone, the worked example: header, mobile nav, toast, hover lifts and FAQ icon in GSAP; CSS keeps only the states.
   - Don't tween an element `main.js` `morph()` animates (the header, the mobile nav, `.reveal`); animate a child instead.
   - The hero headline and image are visible at load (LCP); signature moments sit below the fold.
   - Text an animation holds dimmed or "unlit" still passes contrast in that state: compute the lowest opacity that keeps it at 4.5:1 and carry the rest with non-text cues (L-047). Lighthouse runs with motion on and errors on any contrast failure.
   - Rotate or scale shapes inside an SVG (`svgOrigin`), never a full-width box: its corners overflow phones (L-046).
   - Tween and timeline callbacks read their tween as `this` (`onUpdate() { this.progress() }`), never the outer `const`: a fromTo renders, and calls onUpdate, before the const is assigned, and that one throw stops every moment on the page (L-048). **ScrollTrigger callbacks are different:** they don't bind `this`, so use their argument (`onUpdate(self) { self.progress }`); `qa.py` errors on `this.progress` read as a property (L-071). After building a scroll moment, scroll through it with motion on and assert the state it should change (a class, a value), not just that nothing throws.
   - Entrance moments replay whenever they come back into view (the user's standard): give a play-on-entry tween or timeline `paused: true, scrollTrigger: inView(el, 0.85)`, never `once: true`. Scrubbed moments follow the scroll anyway. Only a list people compare by scrolling back and forth (a product grid) plays once.
   - Keep motion.js's `refreshInit` → `ScrollTrigger.sort()` line: triggers are measured in page order, so one written before a pin above it still accounts for the pin's scroll (L-050).
   - The official GreenSock `gsap-skills` plugin is installed as the API reference (tweens, timelines, ScrollTrigger, plugins). Where it disagrees with this pipeline, this pipeline wins: the vendored files instead of npm or a CDN, no ScrollSmoother, `will-change` only where it's measured to help. Check its claims against the vendored source when they matter: it has `refreshPriority` backwards for 3.15.
   - Pinned sections clip their overflow, and nothing stays invisible once the page has scrolled past it.
   - No ScrollSmoother unless the user asks: it takes over scrolling and breaks `main.js` parallax.
5. **Image sizes (L-039).** The build gives every local photo WebP copies (480–2000px, in `.pipeline/img-cache`, named by content hash) and a `srcset`. `sizes` defaults to `100vw`, or `max(100vw, 90vh)` on `data-parallax` photos (cover-cropped, so drawn wider than the screen on phones). Give images in multi-column grids a `sizes` that matches their columns, e.g. `sizes="(min-width: 900px) 50vw, 100vw"`; a render helper can add it to every image it emits. `browser_qa.mjs` warns when a pick is blurry (smaller than the drawn width) or wastes bytes (over 2x), with a hint. Opt a tag out with `data-no-srcset`. Cut-outs and logos (transparent PNGs) are left alone; give header logos a small copy (~4x their drawn width) under a new file name.

### 5 · QA loop (repeat until clean, max 3 rounds)

1. `python _src/build.py && python tools/qa.py`, then read `qa/report.md`. These are rule checks: duplicate images, repeated wording across pages, placeholders, select defaults, CTA labels, tap-to-call, animation properties, h1/meta. They also cover local SEO: LocalBusiness JSON-LD that matches BIZ name and phone, one phone number sitewide, unique titles and descriptions of search-friendly length, the town in the homepage title or description, `<html lang>`, robots.txt never blocking the site, and a share image once DOMAIN is set.
2. `node tools/browser_qa.mjs`, then read `qa/browser-report.md`. It covers:
   - overflow at 360/390/1440;
   - real rendered contrast on every surface (L-031/L-032): CSS colours for text on plain surfaces, and screen pixels for every single-colour SVG icon or divider (an error below 3:1) and for text on photos (a warning: busy photos are estimates) or on glows and gradients (an error: glows are allowed only where the text over them passes, including `::before`/`::after` glows and box-shadow halos within reach);
   - hero CTA above the fold at 390×844;
   - wrapping pills, dropped icons, broken or upscaled images, and the mobile tap-to-call;
   - **axe-core** WCAG 2.2 A/AA rules: accessible names, labels, ARIA, landmarks, target size;
   - **Lighthouse mobile** on every page, with a score table at the top of the report. Errors: performance below 80, accessibility or SEO below 90, best practices below 70, LCP over 4s, CLS over 0.25, TBT over 600ms. Warnings: performance or best practices below 90, accessibility below 95, SEO below 100, LCP over 2.5s, CLS over 0.1, TBT over 200ms (`FLOORS` in `tools/lighthouse.mjs`). Usual fixes: self-hosted fonts (`tools/self_host_fonts.py`), a tighter `sizes` on the LCP image (read the LCP element and its file in `qa/lighthouse/<page>.json`), `fetchpriority="high"` on the hero image, no `loading="lazy"` above the fold, and small copies of logos. The "efficient cache lifetimes" hint comes from the local test server, which ignores `_headers`; skip it.
   - **srcset picks:** a warning when an image's chosen file is blurry or over 2x its drawn width (see Build 5).
   - **GSAP motion pass** (GSAP pages only, 390 and 1440, reported as "motion on"). The main pass emulates reduced motion, so this pass reloads with motion on and checks five things: tweened properties, clashes with `.reveal`/`data-parallax`, a hero hidden at load, horizontal overflow while scrolling through pins, and content still invisible after the whole page has scrolled. It also errors on ScrollTrigger starts that disagree with the layout (triggers created out of page order, L-050). Every pass, motion on or not, also errors on any uncaught JavaScript error (L-048). Screenshots stay reduced-motion, which shows the fallback. Judge the moments themselves by scrolling the page in a browser.

   Lighthouse adds ~30s a page; use `--no-lighthouse` for quick re-checks while iterating, but the last QA round runs it. Runs are sequential by design; never run two at once.
3. **Visual pass:** open the `-fold` screenshots for every page at 390 and 1440, and skim the `-full` ones. Work through `.pipeline/VISUAL-REVIEW.md`. That covers the things a script can't judge: text or plates behind headlines, cropped subjects, story-fit, template smell.
4. Run `impeccable critique` and `impeccable detect` across the site, and put the findings through the critique gate.
   - P0/P1: ask, then apply the user's choice to the **whole class** of the problem sitewide, not just the instance named. Re-run QA and the critique to confirm (L-016).
   - P2/P3: skip and log, per the gate.
   - For a detector false positive, note why in Decisions instead of chasing it. Known false positives (L-000):
     - cramped-padding on full-bleed bands;
     - broken-image on JS-filled images;
     - hover-state contrast;
     - body `overflow-x`;
     - wide-tracking on small caps;
     - dark-glow on neutral elevation shadows.
5. For a final fresh-eyes pass, spawn the `impeccable:impeccable-finish-reviewer` agent against the direction in `PROJECT.md`. Rate each issue it returns P0–P3 and put them through the critique gate.

### 6 · Preview deploy

- Only if pre-authorized in `BRIEF.md` or by the user's answer. Otherwise make it one question at handoff.
- `python tools/deploy.py` builds the site, deploys only `dist/` with a noindex `_headers` file, then checks that the URL returns 200 publicly with `X-Robots-Tag: noindex`.
- The host comes from `BRIEF.md` › `Deploy host:` (`cloudflare`, the default, or `netlify`). `--host netlify|cloudflare` overrides it. With no `Deploy host:` line, a site that already has `.pipeline/netlify.json` stays on Netlify so its preview URL doesn't move. Each host keeps its own state (`.pipeline/netlify.json` or `.pipeline/cloudflare.json`).
- Cloudflare Pages is now part of Workers, so `cloudflare` deploys `dist/` as a static-assets Worker at `<folder>-preview.<account>.workers.dev`, using a config `deploy.py` writes to `.pipeline/wrangler.jsonc` (L-026). Never run bare `wrangler deploy` or `wrangler pages` in the site folder: autoconfig writes a broken `wrangler.jsonc`.
- If the CLI isn't logged in, ask the user to run `! npx netlify-cli login` or `! npx wrangler login` once, then retry. If a Cloudflare login spans several accounts, they also need `CLOUDFLARE_ACCOUNT_ID` set.
- If `deploy.py` warns that wrangler auto-registered the account's workers.dev subdomain, tell the user the name and that they can rename it (dashboard → Workers & Pages → Settings → Subdomain).
- A fresh `*.workers.dev` name can take a minute or two to resolve; `deploy.py` retries for up to 3 minutes before failing.
- A Netlify 401 means team login protection is on. `deploy.py` switches it off for the preview site it just created and re-checks (L-019). Only if that fails, tell the user the setting: Site configuration → Access & security → Visitor access.
- Older hand-built sites (no `_src/build.py`, no `dist/`; e.g. IronCity, Weknz, HVAC): `python "<pipeline>/dev/deploy_static.py" "<site folder>"` stages only the top-level HTML, `assets/` and favicon into `.pipeline/stage` with a noindex `_headers`, then deploys and checks it the same way.
- A public, indexable site on Cloudflare (not a preview), e.g. the owner's own portfolio: use a classic Pages project for a clean `<project>.pages.dev` address. Create it once with `--force`, then deploy without it, and retry the check through the first-minute 522 (L-035; see `<workspace>/Portfolio Site/tools/deploy_live.py`). Always deploy to the host BRIEF.md names.
- Production launch or a custom domain is always a separate, explicit request.

### 7 · Handoff

Write `HANDOFF.md`, then give the user a short summary in chat:
- The preview URL, plus the paths to the 390 and 1440 homepage screenshots.
- The Lighthouse score table from `qa/browser-report.md`. It's a selling point next to competitors' sites; never claim scores that weren't measured.
- **Placeholders, never presented as working:** every `data-todo`, empty BIZ token, demo-mode form (`FORM_ENDPOINT` empty; with Netlify Forms, also whether deploy.py found the form registered and whether notifications still need switching on), `href="#"` social or legal link, and sample data. `qa/report.md` lists them; copy that list.
- Deferred questions, plus the 3–5 decisions most worth a second look.
- Stock photo credits, and any image knowingly repeated (with the reason).
- **Sample mode:** a list of everything fictional. Also copy `qa/shots/index-1440-full.png` to `<workspace>/Portfolio Screenshots/<Name> Website.png`. That folder holds only these finished-site screenshots. Never overwrite an existing file there; add ` (2)` to the name instead.

**Lessons (every project, before the summary).** This is how mistakes stop repeating:
1. Go through each entry in `PROJECT.md` › Mistakes.
   - **Already in `<pipeline>/LESSONS.md`:** add this project to its *Seen* line. A lesson seen twice means its prevention failed, so upgrade its enforcement one level.
   - **New:** add an `L-###` entry.
2. Enforce each new or upgraded lesson as strongly as it allows:
   - **check:** if it's machine-checkable, add it to `<pipeline>/template/tools/` (`qa.py` or `browser_qa.mjs`) and to this project's `tools/`. Prove it three ways: it fires on a planted defect, it stays quiet on the clean template, and it stays quiet on real markup (`python <pipeline>/dev/qa_real_site.py "<a finished past site>" <scratch dir> "<CTA label>" <CTA href>`; judge every hit). (L-017)
   - **rule:** add or sharpen a one-line rule in the matching section of `~/.claude/CLAUDE.md`.
   - **step:** for process mistakes, edit this SKILL.md or `.pipeline/VISUAL-REVIEW.md`.
3. In the chat summary, say how many mistakes were logged and what became a check, rule or step.

**Design library (every project).** Record the finished site so future builds can learn from it:
- Write `<pipeline>/design-library/sites/<slug>.md` in the entry format from the library README. Work from PROJECT.md › Direction and the shipped CSS and pages, not from memory.
- Save the homepage strip (top of `qa/shots/index-1440-full.png`, 960 wide, at most 2400 tall) and the 390 fold to `design-library/shots/<slug>.webp` and `<slug>-phone.webp`.
- Add the site's row to the README index, and add any new patterns to `patterns.md`.
- Include what the user praised or corrected, and the critique scores. Weak spots are worth recording too.

Tick the last phase. The site is done when every phase is ticked, both QA reports have zero errors, and the handoff lists every placeholder.
