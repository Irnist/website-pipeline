# Trevor Travis Motors: the shop's own parts book — ink plates with numbered callouts, dot-leader price lists, an orange closing field
Motorcycle dealer + parts counter (Bayanan, Muntinlupa, PH) · sample · October 2026 · 8 pages (Home, Motorcycles, Parts & Service, Installment, About, Contact + Photo credits, 404) · pipeline build · Source: `Concept Websites/Trevor Travis Motors Website/`
Screens: `../shots/trevor-travis.webp`, `../shots/trevor-travis-phone.webp` · Inspiration: `../inspiration/trevor-travis-inspiration.webp` · Full page: `Portfolio Screenshots/Trevor Travis Motors Website.png`

## Identity
The site is the exploded-diagram parts catalogue that sits on Trevor's counter: every photo is a numbered FIG. plate, bikes carry orange callout discs keyed to an itemised "what we checked" list, and prices run on dot leaders like a parts book. It fits a neighbourhood shop whose pitch is "the same people who run the parts counter checked this bike", and it puts money and paperwork (cash price, 20% down, monthly, OR/CR) in plain pesos, which is what PH riders ask before they call. Mood: workmanlike, printed, honest, dense, warm-industrial. It avoids the category template (glossy cut-out bikes on black, red accents, stat tiles, testimonial cards) by using document devices: FIG. numbering running across the whole site (FIG. 1–19), 2px rules instead of cards, tabular numerals, and a local story (tricycles, National Road, Bayanan terminal) where a template would put "Precision meets power".

## From the inspiration image
- **What it showed:** "Ridenix", a dark moto-dealer template. Charcoal panels with rounded corners, a glossy red sportbike cut-out with diagonal red/white stripes, red CTA buttons, an icon-tile category row, "30+ years / 500+ bikes" stat tiles, inventory cards with spec grids and a red "View Details" bar, a newsletter block and a red footer brand tile.
- **What was taken:** darkness as the brand's ground (the ink header, hero, story, find-us and footer bands); bike-forward imagery; per-bike spec data (year, odometer, engine, owners, papers) as a key part of each listing.
- **What was changed on purpose:**
  - Cut-outs on black became framed photos at their natural aspect.
  - Cards became ruled rows and per-bike `.unit` spreads.
  - The red accent became ember orange. The brief asked for black and yellow; the user then asked for orange "while still looking premium".
  - Icon tiles, stat tiles, the newsletter and the hero slider dots were all dropped.
  - The rounded panels became square, flat fields.
  - PROJECT.md › Direction calls the inspiration the template to *refuse*.

## Palette
Tokens in `assets/css/styles.css` › `:root`. Each surface redefines the roles `--fg --muted --rule --focus --btn-bg --btn-fg --link --link-line` (`.band--orange`, `.band--ink, .on-ink`, `.site-header`, `.site-footer`). Components read only those roles.

| Token | Hex | Role | Notes (contrast on which surfaces) |
|---|---|---|---|
| `--orange` | `#f26a1b` | Closing bands (`.band--orange`), FIG. tab, callout discs, key numerals, current-nav tab, highlighter, primary button on ink, header phone link | Ink on it 6.1:1; as text on ink 6.1, ink-2 5.6, ink-3 4.8. White on it 3.1, so never used. Never used as text on paper or white |
| `--ink` | `#14110f` | Header, hero, dark bands, footer, plate frames, 2px rules; body text on light and orange | 17.0 on paper, 18.8 on white |
| `--ink-2` | `#1f1b18` | Photo well inside a plate; plate fill on ink bands | Orange 5.6, smoke 8.4 |
| `--ink-3` | `#2c2723` | Lit key row on callout hover/focus; scrollbar thumb | Orange 4.8 (bold only), smoke 7.2 |
| `--paper` | `#f6f3ee` | Default page background, `.form__next` panel; text on ink | — |
| `--white` | `#ffffff` | `.band--white` (installment teaser), contact form card, inputs | — |
| `--muted-dark` | `#bdb4a8` | Secondary text on ink: captions, key rows, footer legal | 9.2 on ink |
| `--muted-page` | `#524c45` | Secondary text on paper and white | 7.7 paper, 8.5 white |
| `--muted-orange` | `#3d1a06` | The only secondary text allowed on orange | 5.1 on orange |
| `--orange-deep` | `#a8420c` | Link underlines and input focus ring on light surfaces; never a fill | 5.5 paper, 6.1 white |
| `--line-page` / `--line-dark` | `#d8d1c6` / `#3b3530` | 1px row dividers on light / ink; hairline plate frame on ink bands | decorative only |
| `--c-error` / `--c-ok` | `#9b1c12` / `#1d6b34` | Form status only | 7.4 / 5.9 on paper |

Rules: orange text only on ink; text on orange is ink or cover brown; no grey on orange. Ignore DESIGN.md's "ink on orange 12.2:1". The real ratio is 6.1 (CSS comment and PROJECT.md agree).

## Typography
- **One family:** Archivo variable, self-hosted (`assets/fonts/archivo-normal-latin.woff2` plus a latin-ext subset for ₱), `font-weight 100 900; font-stretch 62% 125%`, fallback Arial Narrow. Hierarchy comes from width and case, never from a second face.
- **Display (hero `.hero__title`):** 800, `font-stretch: 64%`, caps, `clamp(3rem, 1.2rem + 6vw, 5.75rem)`, line-height .88, tracking .005em.
- **Page titles (`.page-head h1`):** `clamp(2.75rem, 1.3rem + 5vw, 5rem)` / .9.
- **Closing headline (`.closing h2`):** `clamp(2.5rem, 1.3rem + 4.6vw, 4.75rem)`.
- **h2:** 800, `--narrow` 66%, caps, `clamp(2.25rem, 1.4rem + 3.4vw, 3.75rem)` / .95, `text-wrap: balance`.
- **h3:** `clamp(1.5rem, 1.2rem + 1vw, 1.875rem)` / 1.
- **Unit names:** `clamp(2rem, 1.4rem + 2.4vw, 3rem)`.
- **Body:** 400, 1.0625rem / 1.6, `font-stretch 100%`, `text-wrap: pretty`, measure 34–42em.
- **Lede (`.lede`):** `clamp(1.125rem, 1.05rem + .35vw, 1.3125rem)` / 1.5.
- **Note:** .9375rem / 1.4.
- **Labels (FIG. tab, MOTORS tag):** 800, stretch 80%, .8125rem, letter-spacing .08em, caps.
- **Nav:** 700, stretch 82%, .9375rem, .03em, caps.
- **Buttons:** 700, stretch 88%, 1.0625rem, sentence case.
- **Numerals:** `.num, .price, .specs dd, .hours dd` get `tabular-nums lining-nums`.
  - `.unit__price`: 800, stretch 72%, `clamp(1.75rem, 1.4rem + 1.4vw, 2.5rem)`.
  - Step counters (`.steps li::before`): 3.5rem, stretch 64%, line-height .8.
  - `.timeline__year`: 1.75rem, stretch 66%.
- **Quote (`.quote p`):** 700, stretch 85%, `clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem)` / 1.2, sentence case.
- **Weakness:** the .88 / .9 / .95 heading leading predates L-051 (headline line-height ≥1.05). `qa.py` would now flag four rules here, including the step-counter `::before`. Caps-only Archivo has no descenders, so it reads fine, but a reuse must opt in through `ALLOW_PATTERNS['tight-leading']` or open the leading up.

## Homepage anatomy
1. **Cover (hero)**
   - Layout: `.band.band--ink.hero`, 2-column grid `minmax(0,1.15fr) minmax(0,1fr)` at 900px+, gap 4rem, vertically centred, top padding tightened to `clamp(2rem,4.5vw,3.5rem)`.
   - Content, left: H1 "Bikes, parts and the papers to ride them.", lede, primary "Visit the shop" plus outlined "Call 0919 123 4567", and an hours meta line.
   - Content, right: FIG. 1, an orange KTM 390 Duke photo at natural aspect (max 34rem, `justify-self: end`) with three orange discs (front disc 16/70, rear tyre 83.5/61, trellis frame 40.5/54) keyed to "Brakes / Tyres / Papers" rows that say what "checked" means.
   - What makes it work: the hero photo is also the product promise, annotated.
   - Phone: one column, CTA pair stacked above the plate; the fold shows the headline, both buttons and the top of the bike.
2. **On the floor this week**
   - Layout: paper `.split.split--top`, 1:1.
   - Content: intro and a "new units at maker's SRP" note on the left; on the right a `.leaders.leaders--lg` dot-leader list of all six pre-owned bikes. Each row has the model as a link, a small "year · type · km" line, and the cash price.
   - What makes it work: the inventory preview is a price list, not a card grid.
3. **Story**
   - Layout: ink `.split--wide-plate` (1:1.3).
   - Content: FIG. 2, a tricycle queue, beside "Started on tricycles, three streets from here" and two paragraphs of owner history, with a `.go` arrow link to About.
4. **Parts counter**
   - Layout: paper `.split--wide-text` (1.25:1).
   - Content: H2 "Call with your model. We'll check the shelf.", a 5-row dot-leader parts list (₱320–₱2,400), a courier note, and a tall FIG. 3 helmet-wall plate (`.plate--tall`, max 26rem, pinned to the right edge).
5. **Installment, worked out in pesos**
   - Layout: `.band--white.band--ruled` (2px ink top rule), split.
   - Content: the plan terms on the left; on the right a dot-leader computation (cash → down → balance → add-on → **monthly**) whose total row carries the orange highlighter swipe on ₱3,405.
   - What makes it work: the only highlighter on the page, and it marks the number the buyer actually wants.
6. **How buying a bike here goes**
   - Layout: paper `.band--ruled`, `.steps` ordered list, 3 columns at 900px+.
   - Content: each step has a 2px ink top rule, a huge condensed counter (1/2/3), an h3 and muted copy.
   - It answers "what happens after I call".
7. **Find us on National Road**
   - Layout: ink `.split--wide-plate.split--flip` (text left, plate right).
   - Content: bold address, two landmark directions ("past the Bayanan tricycle terminal… look for the orange shutter"), an aligned hours grid, a Google Maps link with ↗, and FIG. 4, a real National Road photo.
8. **Closing**
   - Layout: `.band--orange.closing`, grid 1.4fr/1fr aligned to the bottom.
   - Content: a huge "Open every day until 7 PM." on the left; on the right one line plus the CTA pair, here ink button with orange text and the call button outlined in ink.
   - Phone: stacks.

Footer follows (see components). Home height is about 8,400px at 390px.

## Other page patterns
- **Page head (all inner pages):** `.page-head` on paper. Big condensed H1 (`clamp(2.75rem,…,5rem)`), a lede, and a 2px ink bottom rule. No hero photo; the inner pages open like a catalogue chapter.
- **Listing (`_src/pages/motorcycles.html`):**
  - Each bike is an `article.unit`, 2 columns `1.2fr 1fr` at 900px+, with a 1px rule between units.
  - Left: a callout plate (`{{fn:cplate}}`) with 2–3 discs on real features ("CVT: new belt", "Side panel: light scratches, and the price reflects them").
  - Right: the model as h2, a big tabular cash price with a small "cash" tag, a `.specs` dl (Year, Odometer, Engine, Owners, OR/CR, Registered to) in a `max-content 1fr` grid with nowrap values under ~22 characters, a note, and an "Ask about this bike" link that pre-fills the contact form via `?item=&service=`.
  - Honest defects in a callout are the pattern worth copying.
- **Installment (`_src/pages/financing.html`):**
  - Full terms table `.terms`: six bikes × down/12/18/24/36 months, right-aligned tabular figures, highlighter on the Mio M3 12-month cell, which ties back to the home example.
  - Below 700px each row becomes a block: bike name across the top, then a 3-column grid of figures, each labelled via `td::before { content: attr(data-label) }`. No sideways scroll (L-024).
  - Then a "what to bring" ticks list beside FIG. 16, three `.ruled-block` steps, and an ink FAQ split (`.faq details`, chevron drawn with borders).
- **Parts & Service (`_src/pages/parts-service.html`):** six dot-leader lists in a 2-column `.cols` (32 priced rows), a helmets-and-gear split, a service menu with flat rates on ink, and a delivery / returns / guarantee 3-column `.ruled-block` row.
- **About (`_src/pages/about.html`):** "A tricycle driver's son" split; an ink `.timeline` (years 1993–2018 in a 4.5rem condensed column); a `.roster` of staff as a ruled list (10rem name column at 700px+) instead of people cards; one pull quote (`.quote`) from a tricycle operator; `.plates-row` of two plates (1.35fr/1fr).
- **Contact (`_src/pages/contact.html`):**
  - `.contact` grid 1:1.5. The `aside#visit` (address, call button, directions, hours, map, email, socials) comes first in the DOM, so on phones the call option sits before the form.
  - The form is a white card with a 2px ink frame. Selects start on "Choose…". The phone field becomes required for Phone call/Text. Prefill is guarded against null. `.form__next` (who replies, how fast) sits above "Send message". Demo-mode message when there is no endpoint.
- **Inner-page close:** the `_src/partials/visit-strip.html` orange strip, "Come see it on National Road", with address, hours and the CTA pair. Slimmer than the home closing band, so it is not a repeat.

## Signature elements
- **FIG. plates in one sitewide sequence:** photo at natural aspect in a 2px ink frame on an ink-2 well, caption bar led by an orange `FIG. n` tab. Pointers: `assets/css/styles.css` › `.plate`, `.plate__cap`, `.fig`; helper `_src/site_config.py` › `h_plate`. On ink bands the frame drops to `--line-dark` (`.band--ink .plate`).
- **Callout plates:** 2.25rem orange discs placed by `--x/--y` % on the photo, focusable `<button>`s tied to key rows via `aria-describedby`. Hover or focus on either side lights both (disc `scale(1.18)`, row `--ink-3`). Pointers: `.pin`, `.key`, `.key__no`; `_src/site_config.py` › `h_cplate`; `assets/js/main.js` › "plate callouts".
- **Dot-leader price lists:** flex rows with a `::before` 2px dotted leader (`min-width: 2.5rem`, never a stub), nowrap bold tabular price, a 2px `--fg` opening rule and 1px row rules, plus a `.leaders__total` closing 2px rule. Pointer: `.leaders`, `.leaders--lg`.
- **Highlighter swipe:** an orange block skewed −6° and rotated −1° behind the monthly figure only; it draws in with `scaleX` when its `.reveal` parent enters. Pointer: `.hl`, `.hl::before`.
- **Catalogue-tab nav:** at 1180px+ the current page becomes an orange tab hanging from the top of the ink header (square top, 2px-rounded bottom). Pointer: `.site-nav a[aria-current="page"]` inside `@media (min-width: 1180px)`.
- **Surface-role system:** bands swap `--fg/--muted/--rule/--btn-bg/--btn-fg/--link-line`, so one `.btn-primary` is ink-on-orange on light fields and orange-on-ink on dark ones. Pointer: `.band--orange`, `.band--ink, .on-ink`.

## Motion
- **Everything is CSS and predates the 2026-10-09 "all animation in JS" rule.** `qa.py` would now error on these:
  - `@keyframes pin-in`: hero callout discs pop in, scale .4→1 with opacity, .6s, staggered `.35s + i × .14s`.
  - `.reveal`: opacity plus `translateY(1rem)`, .6s `cubic-bezier(.16,1,.3,1)`. Only two on the whole site: the home installment computation and the financing table.
  - The highlighter `scaleX` draw: .7s, .25s delay.
  - Header scrolled state: 3px orange `::before` rule fades in and the wordmark scales to .94 over .25s. The bar height never changes.
  - Nav underline `scaleX` grow: .2s.
  - Mobile menu: fades and slides down .5rem, .2s.
  - Button hover: `translateY(-1px)`, .15s.
  - FAQ chevron rotation and `.go` arrow nudge (3px).
- **Reveals play once:** `main.js` calls `io.unobserve()`, so there is no REPLAY. No parallax and no GSAP.
- **Reduced motion:** reveals and pins are gated by `prefers-reduced-motion: no-preference`, and a global reduce block zeroes durations.
- **To reuse:** port these to `main.js` `morph()` and `REPLAY`.

## Reusable components
- **Header:** sticky fixed-height 4.5rem ink bar (`.site-header`, `.site-header__bar`).
  - Wordmark: condensed caps name plus an orange MOTORS tag (`.brand`, `.brand__tag`).
  - Right side: orange phone link (`.header-call`) and primary CTA (`.header-cta`).
  - Hamburger below 1180px. Below 600px the phone becomes a 2.75rem orange-outlined icon button and the header CTA hides.
- **Buttons:** `.btn-primary`, one label "Visit the shop", is always the inverse of its field. `.btn-call` is outlined in currentColor with a phone icon and the full number, and sits beside the primary everywhere. `.btn-ghost` is for secondary links (404). All have a 2px radius and min-height 3rem.
- **Text link:** `.go`, 700 weight, 2px `--link-line` underline, arrow icon; `.ext` adds ↗ for external links only.
- **Unit / listing spread:** `.unit`, `.unit__price`, `.specs` (`styles.css`).
- **Ruled blocks and steps:** `.ruled-block`, `.steps` (counter via `counter(step)`), `.cols--3`.
- **Timeline and roster:** `.timeline` (4.5rem year column), `.roster` (10rem name column).
- **Terms table that stacks on phones:** `.terms` plus the `@media (max-width: 699px)` block.
- **FAQ:** `.faq details/summary`, with a border-drawn chevron.
- **Form:** `.form`, `.field`, `.field.is-required label::after " (required)"`, a select chevron from two linear-gradients, `.form__next` panel with a 2px ink top rule, `.form__status[data-kind]`, and the `.contact__form` white card with a 2px ink frame.
- **Hours grid:** `.hours` (`max-content 1fr`, nowrap values), rendered by `{{fn:hours}}`.
- **Footer:** ink `.site-footer`, `repeat(auto-fit, minmax(14rem,1fr))` (3 columns at 1440).
  - Columns: brand and icon-row contacts plus socials; "Shop hours"; "Pages".
  - Headings: orange condensed caps (`.site-footer__heading`, 1.125rem, stretch 72%).
  - Legal line: 1px `--line-dark` with a "Photo credits" link (`.site-footer__legal`).
- **Closing bands:** `.band--orange.closing` on home, `.strip` on inner pages.

## How it went
- **Review results:**
  - No numeric critique score. The impeccable-finish-reviewer's verdict was "ship after fixes". Its fixes: callouts on every bike plate, tall plates on the right edge, leaders never a stub, the catalogue-tab nav, and the About staff turned into a roster.
  - Declined: one highlighter per price list. It was kept to the installment computations so it stays meaningful.
  - `impeccable detect`: 35 findings, all false positives (cramped-padding on full-bleed bands; side-tab on the header `::before` rule).
  - QA ended at 0 errors. Lighthouse mobile 97–100 after the 2026-10-08 speed and SEO pass (LCP 1.7–2.6s; Motorcycles had been 4.7s).
- **User direction:**
  - The brief asked for black and yellow. The user then asked to "update the yellow color palette to orange while still looking premium".
  - That moved the hero from an orange field to ink, so orange now owns only the close. The yellow R6 hero was swapped for an orange KTM Duke and its callouts re-pinned.
  - The user also commissioned the speed and local-SEO pass. No other corrections are recorded.
- **Lessons from this site:**
  - L-022: a callout said "chain and sprocket" but pointed at the exhaust. Check pins on a % grid over the full-size photo.
  - L-023: desktop nav wrapped at 1440. Nav is nowrap, labels shortened, "Home" hidden, hamburger below 1180px.
  - L-024: the terms table relied on sideways scroll, and long nowrap spec values overflowed. Stack tables on phones; keep spec values under 22 characters.
  - L-025: a retyped Instagram handle had a typo.
  - Also L-018–L-021 (tooling), L-039 (speed/SEO), and L-007 (an honesty pass caught a ZX-6R "cash only" contradiction).
- **Known weaknesses:**
  - CSS motion and leading under 1 (see above).
  - Nine passages are retold across pages and were never cleaned up (installment terms, the shop story, the address line, directions).
  - The ZX-6R plate shows sponsor livery logos.
  - Several "local" photos are from Thailand (parts shop, workshop bay), and the National Road photo is hazy.
  - PRODUCT.md still says "black and yellow".
  - The contact form is in demo mode.
  - The motion budget is thin: only two reveals on the whole site.

## Reuse guidance
- **Fits:** any trade counter whose value is inspection, specs or itemised prices. Used-car and moto dealers, parts and hardware counters, bike shops, appliance repair, tool rental, machine shops, pre-owned electronics, auto service menus. Also any business where buyers compare money terms: installment tables, rate cards, menus with prices.
  - The FIG.-plate + callout-key pattern transfers wherever a photo can be annotated with "what we checked / what's included": a renovated room, a serviced AC unit, a refurbished laptop.
  - Dot leaders and tabular numerals suit any price list.
  - The surface-role token system (`--fg/--btn-bg/...` per band) is a template-wide win.
- **Keep to this site:** don't copy these as a whole set:
  - the whole parts-book identity (FIG. numbering + orange callouts + highlighter + catalogue tab);
  - the ember-orange-on-warm-ink palette;
  - the Archivo 64% condensed-caps voice;
  - the tricycle/National Road story bands.
  
  Take one device per site and build the rest from that business's own story. Don't reuse the hero copy formula "Bikes, parts and the papers to ride them."
