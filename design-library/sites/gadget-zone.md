# Gadget Zone: a dark neon tech store built around the repair bench behind the counter
Electronics / gadget retail (single showroom, Muntinlupa PH) · sample · October 2026 · 6 pages + 404 (Home, Shop, Categories, Deals, About, Contact) · pipeline build · Source: `Concept Websites/Gadget Zone Website/`
Screens: `../shots/gadget-zone.webp`, `../shots/gadget-zone-phone.webp` · Inspiration: `../inspiration/gadget-zone-reference.webp` · Full page: `Portfolio Screenshots/Gadget Zone Website.png`

## Identity
The brief asked for the reference's dark neon tech-store look "as close as possible". What stops it being any gadget shop is one story: the owner started as a phone-repair stall in 2016, so every unit is switched on to try, bench-checked in front of the buyer, set up at pickup, and serviced on the same bench under warranty. That story drives the H1 ("The latest gadgets, *bench-checked.*"), the "Bench-checked" stamp on every product card, the four-step "How a unit leaves our bench" sequence, circuit-trace dividers with solder nodes, and a reserve list that ends in a quote/hold request instead of a fake checkout. Mood: nocturnal, electric, precise, hands-on, honest. The neon comes only from thin gradient strokes and photography. There are no blurred glows.

## From the inspiration image
- **The reference** (a "NEXORA" Dribbble-style shot) showed a navy-black UI with a pink→violet→blue palette, a hero product on a neon ring and pedestal, a "Shop Now" gradient button, a three-item trust row, a 7-icon category strip with a chevron at the foot of the hero panel, a product detail card (thumb column, stars, price + struck price, colour swatches, qty stepper, gradient "Add to cart", trust row), a giant "TECH STORE DESIGN" title between gradient rules, and three phone checkout mockups.
- **Taken:** the palette, rounded navy panels (`--grad-panel`), the ring + pedestal (as SVG strokes), the trust row, the category strip (kept as a real `<nav>`), the product detail card layout (it became the Home spotlight), and the gradient-rule title (it became divider b).
- **Changed on purpose:**
  - "Sign In" was dropped because there are no accounts.
  - The cart is a reserve list that ends on the contact form.
  - There are no stars or reviews counts, and no struck prices outside Deals.
  - The swatches are real radios with nothing chosen by default.
  - "Add to cart" became a muted `.btn-reserve`, so "Get a quote" stays the only filled CTA.
  - The hero product is a circular photo crop inside the ring, not a cut-out standing on the pedestal. The critique flagged this as a P2 shortfall against the reference.
  - The checkout mockups were not used.

## Palette
All tokens are in `assets/css/styles.css` `:root`. The whole site is one dark surface, so one light-ink set covers text and graphics (L-031). Contrast was measured with the project's contrast.py.

| Token | Hex | Role | Notes (contrast on which surfaces) |
|---|---|---|---|
| `--c-bg` | #0a0918 | page background, form field fill | — |
| `--c-surface` | #121029 | cards, footer, step tiles, mobile nav | — |
| `--c-raised` | #1b1839 | quotes, reserve box, hover fills | — |
| `--c-raised2` | #252150 | reserve button, active pill, toast | — |
| `--c-text` | #f5f3ff | body/headings | 17.98 bg · 16.92 surface · 15.49 raised · 13.56 raised2 |
| `--c-muted` | #b9b4dc | secondary copy, nav links | 9.97 / 9.39 / 8.59 / 7.52 |
| `--c-pink` | #ff6ad5 | gradient-text start, solder nodes, brand "ZONE", timeline years, deal "why" | 7.77 / 7.31 / 6.69 / 5.86 |
| `--c-violet` (= `--c-brand`) | #b69cff | links, focus ring, step numerals, icons | 8.63 / 8.12 / 7.43 / 6.51 |
| `--c-blue` | #6aa8ff | waveform divider, minirow icons, gradient end | 8.13 / 7.65 / 7.00 / 6.13 |
| `--c-green` | #5ee49b | "In stock", "Bench-checked" stamp, checklist ticks | 12.25 / 11.53 / 10.55 / 9.24 |
| `--c-line` | #2c2860 | 1px card borders | decorative |
| `--c-line-strong` | #5b54a3 | input/pill/qty strokes | 3.04 on bg, 2.86 on surface (UI strokes only) |
| `--c-trace` | #8a80f0 | circuit-trace divider stroke | graphic |
| `--grad-cta` | #c026d3 → #6d28d9 (100deg) | the one filled button | white text 4.71 → 7.10 |
| `--grad-ink` | #ff6ad5 → #b69cff 55% → #6aa8ff (95deg) | `.grad-text`, ghost-button borders, step bars | — |
| `--grad-cool` | #8fd0ff → #6aa8ff | `.grad-text--cool` (first half of rule titles) | — |
| `--grad-panel` | #17143d → #0e0c25 60% → #120f2e (160deg) | hero, spotlight and page-head panels | — |
| closing panel | #3b1166 → #1d1650 → #102a63 (120deg) | `.closing__panel` only | body text #e4e0ff |
| badges | #6d28d9 / #c026d3 fill | `.badge--pick`/`--new`, `.badge--off`, reserve count | white text |

## Typography
- **Display:** Outfit 600/700 (self-hosted; it was picked because the reference uses a round geometric face, and its 0 is narrower than its O). Headings use `line-height: 1.1; letter-spacing: -.01em; text-wrap: balance`.
  - h1 `clamp(2.4rem, 6vw, 4.1rem)`; inner-page h1 `clamp(2.2rem, 5vw, 3.4rem)` at `max-width: 18ch`.
  - h2 `clamp(1.8rem, 3.6vw, 2.6rem)`; h3 1.2rem/600.
  - Rule titles: `clamp(1.8rem, 4.4vw, 3.2rem)`, uppercase, +.01em tracking.
- **Body:** DM Sans 400/500/700, 1rem/1.6. The hero lead is 1.08rem in muted ink, max 34rem.
- **Numerals:** prices use DM Sans 700 with `tabular-nums` (`.price` 1.3rem, `--lg` 1.8rem, `--xl` `clamp(2rem, 4vw, 2.6rem)`). Step numerals "01–04" are Outfit 700 at 2.4rem in violet. Timeline years are Outfit 700 at 1.3rem in pink.
- **Treatments:**
  - The second half of a headline uses gradient text (`.grad-text`, e.g. "bench‑checked." with a non-breaking hyphen).
  - Rule titles split one heading into a cool-blue half and a pink→blue half.
  - The wordmark is uppercase Outfit 700 with "ZONE" in pink.
  - The large quote uses Outfit 500 at `clamp(1.25rem, 2.4vw, 1.6rem)/1.35`.
- **Weakness:** the build maps all three weights of each family to one woff2 file per family (`_src/partials/fonts.html`). It works only because the files are variable fonts. The ₱ sign falls back to the system font, since only the latin subset is loaded.

## Homepage anatomy
1. **Header:** sticky, with a fixed 4.5rem bar. From the left: a gradient-stroke bolt logo plus the wordmark. Nav on the right: 6 links (active = 2px pink underline at .45em offset), then search and reserve-bag icon buttons (2.75rem round, pink count bubble), the phone with its number, and the "Get a quote" gradient button. The scrolled state fades in a ::before backdrop at rgb(10 9 24/.94) and scales the logo to .94. Below 1180px a burger opens a dropdown panel. Below 600px the number text and the CTA hide and the phone stays as an icon (tap-to-call).
2. **Hero panel:** a rounded 24px `--grad-panel` box. Inside, a `1.08fr .92fr` grid from 900px:
   - Left: H1, lead (the client's tagline plus "try any unit on our table in Poblacion"), the gradient CTA plus a "Browse the shop →" ghost button, and a 3-column trust row (outlined 2.25rem icon tiles, bold line plus muted sub-line).
   - Right: the **neon portal**, a `min(100%, 30rem)` SVG ring (solid 3px gradient circle plus a dashed `2 10` orbit that turns once a minute) around a circular photo of headphones in blue light, over an SVG pedestal of two ellipses.
   - The **category strip** sits at the foot of the panel: 7 icon links in a bordered 16px-radius bar, plus a chevron cell.
   - Phone: the content stacks and the portal falls below the fold. The strip becomes a 4×2 grid with an 8th "Categories" cell.
3. **Divider a, circuit trace:** a full-width SVG path with 14px jogs and four pink solder nodes. It uses `preserveAspectRatio="xMidYMid slice"` at a fixed 40px height, so phones see the detailed middle at full stroke weight.
4. **Spotlight product ("Pick of the month", Orbit Watch 2):** a panel with a `1.05fr 1fr` grid.
   - Gallery: a 5.5rem thumb column next to a square main image. The 3 thumbs are crops of one photo (whole / face / strap), panned with GSAP.
   - Info: badge, H2, sub-line, green "In stock: 6 at the counter, mixed colours", the ₱6,990 XL price, a 4-item check list with local detail ("runs along the Alabang–Zapote road"), a **real radio** colour picker (pill swatches, nothing chosen; reserving asks for a colour first), a qty stepper, "Add to reserve list", and a 3-item minirow (hold 2 days / payment methods / installments).
   - Phone (<480px): thumbs move under the main image in a row of three.
5. **Bench process under divider b, the gradient-rule title:** "HOW A UNIT LEAVES OUR BENCH" between two gradient hairlines (flex, lines `flex: 1`). Below are 4 `.step` tiles (4 columns ≥1000, 2 columns ≥640, 1 below). Each has a numeral, an h3 and muted copy, and a 2px `--grad-ink` bar on its top edge that fills like a charge meter. On phones a gradient rail with pink nodes runs down the left edge.
6. **Deals band:** a full-bleed photo (`store-interior.jpg`) under a scrim, solid rgb(10 9 24/.84) on phones (L-032) and a left-to-right gradient from 900px. Content: H2 "Open-box and last-season stock, up to 28% off" (computed from the data), the reason for the discount, and a ghost "See the deals". **Weakness:** the photo is warm and soft, off-palette, and reads as a shopper's arm rather than a store.
7. **"Who walks through our door":** a `1fr 1.1fr` grid. Left is a `<dl>` customer profile (students, Alabang office crews, families, small offices). Right holds two quote cards, a large one in Outfit and a smaller one. This replaces the usual three-testimonial row.
8. **Visit, under divider c, an audio waveform:** a blue SVG flatline with a spike in the middle. Then a `1.2fr 1fr` grid: "Come in and hold it first" (parking, the weekend hold) with a directions link, and an `<address>` card with an icon row and a `.hours` grid.
9. **Closing CTA with divider d, the device-notch edge:** a centred panel on a violet→navy→blue gradient. Its `clip-path` cuts 28px chamfered corners and a 14px phone "notch" into the top-centre edge. The split-text H2 asks "Five laptops for the office, or one phone by Friday?", followed by a reply promise, the primary CTA and a ghost "Call 0929 123 4567".
10. **Footer, with divider e, a charge meter:** an SVG battery outline on a hairline whose three pink bars fill in order. Below it a 4-column `auto-fit minmax(13rem, 1fr)` grid: brand and story line with socials, Visit or call, Hours, Pages. A legal line carries the sample-site disclaimer.

Phone: the page is about 7,280px tall at 390. The hero CTA and the trust row sit above the fold, and the portal starts just under it.

## Other page patterns
- **Page head (all inner pages):** a `.page-head__panel` gradient panel with breadcrumbs, a two-line H1 whose second half is gradient text, and a muted lead (max 40rem). **Weakness:** at 1440 the right half of the panel is empty navy. There's no image or graphic, so every inner page opens on the same blank box.
- **Shop (`_src/pages/shop.html`):** a centred pill search (max 32rem), a centred filter `.pillbar` (the active pill gets a gradient border on raised2; on phones it's a 2-column grid rather than a sideways scroller), and a live count. `.grid-products` runs 1/2/3/4 columns at 0/560/820/1100px. Product card: 4:3 photo, meta row (category plus a green shield "Bench-checked" stamp), name, blurb, spec checks, a price and Reserve row above a hairline, and an "Ask about this one" link that pre-fills the contact form. A dashed note at the end points to the spotlight and Deals so nothing is duplicated.
- **Deals:** horizontal cards (`.9fr 1.1fr` at 900px+), each with a pink "N% off" sticker badge, the reason in pink ("Open-box display unit"), price, struck "was" price, and a "3 left" outlined chip. A "How the deals work" terms list with pink markers follows, under its own circuit-trace variant.
- **Categories:** 7 alternating 1:1 rows (even rows flip the media), each with a 3:2 lifestyle photo, an outlined line-icon tile, an H2, copy, and a `.cat__facts` grid: On the shelf / Price range (computed, plus "deals from ₱X") / At the counter.
- **About:** an owner story beside a 4:5 photo, then a 2016→Today timeline drawn as a circuit trace (gradient rail plus pink nodes), then "What the bench check covers" (a green-tick checklist beside a 3:2 repair photo), a waveform divider, and "Things we won't do" (3 cards: no upsell, no extended warranty, no grey-market stock). That anti-promise section is the most distinctive copy on the site.
- **Contact:** a `1fr 1.7fr` grid.
  - Left: a sticky quick card listing the call button first (ghost style), then email, address and hours. On phones it comes before the form.
  - Right: the reserve list (items, remove ×, total), then the form (Web3Forms; Phone/Text preference makes phone required; next-steps line above submit).
  - Below: 6 `<details>` FAQs under a rule-title-style H2 "Before you come in". The + rotates to × with GSAP.

## Signature elements
- **Neon portal:** gradient SVG ring, dashed orbit, a circular photo frame and an elliptical pedestal, all strokes with no blur. `assets/css/styles.css` › `.portal`, `.portal__ring`, `.portal__frame`, `.portal__base`; markup in `_src/pages/home.html`.
- **Five unique dividers, each one meaning something:** circuit trace (`.divider--trace`), gradient-rule title (`.rule-title`, `.rule-title__line--r`), audio waveform (`.divider--wave`), device-notch clip-path (`.closing__panel`), and footer charge meter (`.divider--charge`, `_src/partials/footer.html`).
- **Charge-meter step tiles:** a gradient top bar driven by `--bar` (scaleX), which turns into a circuit rail with solder nodes on phones (`.steps::before`, `.step::after`). See `styles.css` › `.step::before`.
- **"Bench-checked" stamp** on every product card. `styles.css` › `.stamp`; generated in `_src/site_config.py` › `h_products`.
- **Reserve list instead of a cart:** the header bag with its count goes to contact.html#reserve, where a list carries colour and qty into the message. `styles.css` › `.reserve`, `.tool-btn__count`, `.btn-reserve`.
- **Split-colour rule titles:** a cool half plus a hot half in one heading (`.grad-text--cool` + `.grad-text`).

## Motion
All motion is JavaScript. CSS holds states only, and qa.py errors on `transition`, `animation` and `@keyframes`. The site has GSAP self-hosted (ScrollTrigger, SplitText, DrawSVGPlugin, Flip) in `assets/js/motion.js`, everything inside a `gsap.matchMedia()` reduced-motion gate. Triggers are sorted into page order with `ScrollTrigger.sort()` on `refreshInit` (L-050).
- **Hero depth (scrub 0.5, hero top→bottom):** the image scales 1→1.18 inside the portal, the ring rotates 50° via `svgOrigin '200 200'` (never rotate the SVG box, L-046), and the pedestal moves y 28 and fades to opacity .4. The dashed orbit turns 360° every 60s.
- **Bench sequence:**
  - Desktop ≥1000×640: the section pins at `center center` for `+=900`, scrub .6. Each step goes from opacity .7 to 1 and y 16 to 0 while its `--bar` fills 0→1, with a .4 beat at the end. The dim level is .7, not .3, so the text still passes contrast (L-047).
  - Below 1000px: each step scrubs from `top 85%` to `top 50%`.
  - Below 640px: the shared `trace()` helper draws the rail and pops nodes from the rail's own progress (`back.out(3)`, .35s; L-049).
- **Dividers draw themselves:** paths and rects use drawSVG over 1.1s `power2.inOut`, the nodes pop with a .12 stagger, and the battery bars fill with scaleX at .25s and a .2 stagger.
- **Closing headline:** SplitText words rise with yPercent 110, .8s `power3.out`, stagger .035.
- **Shop:** `ScrollTrigger.batch` rows rise y 28 over .6s and play only once (people compare products). Filtering uses Flip over .55s `power2.inOut`; entering cards scale in from .92 and leaving cards fade out.
- **Other pages:** About's timeline trace scrubs (`top 80%`→`bottom 55%`) and the checklist ticks draw with a .22 stagger. On Categories the icons draw over .9s and photos scrub from 1.12→1 to `center center`. On Deals the % badge slaps on from scale 1.9 and −16° with `back.out(2.2)` and no fade. Contact and the 404 stay calm.
- **UI:** `.reveal` fade-ups (y 16, .6s) replay on re-entry via `inView()`. The header gets `--hdr` and a logo scale of .94 at 40px (.25s). The mobile nav and the toast each animate over .2–.25s. The spotlight crop pans as x/y/scale around a `0 0` origin (.45s). The FAQ icon tweens `--faq` (.2s). Mouse hover lifts are 2px on buttons and chips and 4px on cards (.18s).

## Reusable components
- **Header:** sticky with a fixed height, and a scrolled backdrop on `::before` driven by an opacity var. See `.site-header`, `.header-call`, `.tool-btn`.
- **Buttons:**
  - Primary `.btn-primary` is the `--grad-cta` fill.
  - Ghost `.btn-ghost` is a gradient border made with the `padding-box`/`border-box` double-background trick (on a band or panel it must repeat that surface's colour).
  - `.btn-call` is the same trick on a surface, and `.btn-reserve` is a muted fill.
- **Panels:** `.panel` (`--grad-panel`, 1px `--c-line`, 24px radius).
- **Product card:** `.product`, plus `.stamp`, `.badge--new`, `.product__buy`.
- **Deal card:** `.deal`, plus `.badge--off`, `.was`, `.deal__left`.
- **Category strip:** `.catnav`, 7 columns that become 4 columns with an extra cell.
- **Spec readout:** `.specs-list` (violet check icons) and `.specs`/`.hours` (a `max-content 1fr` grid with nowrap values).
- **Swatches:** `.swatch` with a hidden radio and `:has(input:checked)` pink border, plus the `.swatches.is-invalid` hint.
- **Qty stepper:** `.qty`, `.qty__btn` (2.75rem targets).
- **Pills:** `.pillbar`, `.pill[aria-pressed]`; the search is `.search` (pill input with an inset icon).
- **Forms:** `.form`, `.field` (bg-coloured inputs with a line-strong border), `.form__next`, `.form__status[data-kind]`.
- **FAQ:** `.faq details` with a + to × pseudo.
- **Timeline trace:** `.timeline` (rail ::before, nodes li::before).
- **Footer:** `.site-footer`, an auto-fit 13rem grid; `.social` uses 2.75rem outlined squares.
- **Toast:** `.toast`, fixed bottom-centre, neutral shadow.

## How it went
- **Critique:** impeccable dual-agent homepage critique scored 27/40 with one P1 (look-only colour swatches lost the colour on reserve). The user chose "Make them selectable" (L-042). The re-critique scored 30/40 with no P0/P1.
- **Finish review fixes:**
  - deal % rounding (L-044, computed with `deal_off()`/`MAX_OFF` plus an assert);
  - a mis-tagged headset;
  - a step that duplicated About;
  - a side stripe on `.who`;
  - extra filled buttons (contact call, active chip).
- **Lighthouse mobile at handoff:** 100 performance on every page, accessibility 100 (Shop 99), LCP 1.7–1.9s.
- **The user drove the motion:**
  - GSAP opt-in;
  - "more advanced animations, on mobile too";
  - "test it on every page";
  - "if I scroll up, the animations never happen again", which led to replaying entrances, now the template default;
  - "use JavaScript for animations rather than CSS", now a global rule with a qa.py check.
- **Lessons born here:**
  - L-042: controls must behave like controls.
  - L-043: phone card side-columns cropped product photos to slivers.
  - L-044: computed figures, rounded down.
  - L-045: browser_qa fixes.
  - L-046: rotate inside the SVG.
  - L-047: dimmed animation states must pass contrast.
  - L-049: followers share one timeline (`trace()`).
  - L-050: ScrollTriggers in page order after a pin.
- **Left as known weaknesses:**
  - the hero is a circle crop, not a cut-out;
  - the deals band photo is off-palette;
  - several product and category photos are bright or white-ground rather than dark and moody;
  - the desktop category chevron reads like a carousel arrow;
  - page-head panels are empty on the right at desktop;
  - shop pills take about 220px at 390.

## Reuse guidance
**Fits:**
- Electronics and phone shops, computer/repair shops, gaming cafés, audio/hi-fi, camera stores, drone or e-bike dealers: any retailer with a hands-on service angle.
- The dark-panel and gradient-stroke system also fits tech services (IT support, smart-home installers) and nightlife or esports brands.
- **Transferable patterns:**
  - Dividers that each carry meaning (a trace, waveform, notch or battery drawn from the trade's own objects).
  - Step tiles with a charge-meter bar that becomes a rail on phones.
  - A reserve or quote list instead of a fake cart.
  - A spotlight "detail card" whose thumbs are crops of one photo.
  - The split-colour rule title.
  - A "things we won't do" section.
  - Ghost buttons made with the gradient-border double background.
  - Neon from strokes, not glows.

**Keep to this site:**
- The exact pink/violet/blue palette on #0a0918 together with the portal ring and pedestal: that combination is the reference's (NEXORA) look and would read as a copy.
- The bench story, its "Bench-checked" stamp and the 01–04 bench copy.
- The Muntinlupa/Alabang customer profile and the closing question.
- The battery footer divider as a literal drawing.
- On another site, take the method (dividers drawn from the trade's own objects), not these specific SVGs.
