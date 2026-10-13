# Weknz Patio Furniture: a family showroom on a sunny lawn, in cream paper, walnut ink and a friendly serif
Outdoor / patio furniture showroom (Amish-built poly) · sample · October 2026 · 7 pages (home, about, furniture, reviews, service areas, FAQ, contact) · hand-built (static HTML, pre-pipeline) · Source: `Concept Websites/Weknz Patio Furniture/`
Screens: `../shots/weknz.webp`, `../shots/weknz-phone.webp` · Inspiration: none · Full page: `Portfolio Screenshots/Patio Website.png`

## Identity
This is the visit-first version of a family showroom: "Come sit in it before you buy it." Warm cream pages, walnut-brown ink taken from the logo's wordmark, and Young Serif headlines make it feel like a hand-lettered sign at a Virginia roadside lot, not an e-commerce catalogue. The site's centre of gravity is a live "Closed now · opens today at 10 am" status, the hours table and the real lot photo, which suits a business whose sale happens in person in Shacklefords. Mood: neighbourly, unhurried, sunny, heritage, plain-spoken. Template-breakers: the giant "1980" numeral story block, the ruled spec-sheet "How it's built" list in place of icon tiles, the sky-over-sand "horizon" stripe lifted from the logo's beach, and a reviews section that summarises themes honestly instead of inventing quotes.

Note: the shipped code is the post-critique rebuild. The 2026-10-06 critique scored an earlier, green-dominant version that kept a template ("Lawnx") structure; see How it went.

## Palette
| Token | Hex | Role | Notes (contrast on which surfaces) |
|---|---|---|---|
| `--bg` | `#faf6ec` | Page background (cream) | `--text` 15.1:1 |
| `--paper` | `#fffdf7` | Cards, form card, hours card, swatch band | `--text-muted` 6.5:1 |
| `--sand-100` | `#fbf1da` | `.section--sand` bands (story, reviews), marquee strip, hover fills | `--text-muted` 5.9:1, green-700 4.8:1 |
| `--sand-200` | `#fbe8b8` | "Ideal for" pills | `--walnut-800` text |
| `--sand-300` | `#fcd884` | `.btn--cta` (mobile call bar quote button, footer directions), FAQ open icon, icons on walnut | Walnut-950 on it 13.1:1. As text on walnut-900 it's 11.9:1. |
| `--sand-400` | `#f5c55a` | CTA hover | — |
| `--walnut-900` | `#2b1d13` | `--text` headings; top bar, quote band, footer, mobile call bar, nav toggle | `--on-dark` #f6ecdc 13.9:1, `--on-dark-muted` #d8c6b0 9.8:1 |
| `--walnut-800` | `#3e2a1c` | Big numerals ("1980", "4.6"), 2px rules over spec lists | 12:1 on sand-100 |
| `--walnut-600` | `#6f4a32` | "Family owned · Since 1980" line, breadcrumb links | 7.2:1 on bg |
| `--text-body` | `#47362a` | Body copy | 10.6:1 on bg |
| `--text-muted` | `#6b5a4c` | Secondary copy | 6.1:1 bg, 5.9:1 sand-100 |
| `--green-700` | `#1b7a41` | Primary action (logo palm leaves): primary button, links, H1 second clause, numerals, icons | White on it 5.4:1. As text it's 5.0:1 on bg and 4.8:1 on sand-100 (passes, just). |
| `--green-800` | `#145a32` | Hover | — |
| `--green-500` / `--green-100` | `#249c54` / `#e6f2e4` | Open-status dot / open pill fill | — |
| `--sky-400` / `--sky-200` | `#5cc9ee` / `#bfe9f8` | Logo sky: the `.horizon` stripe and the footer tagline only | Sky-400 on cream is 1.8:1, so it is never used as text. Sky-200 on walnut is 12.6:1. |
| closed / danger | `#9a3412` / `#a3261b` | "Closed" cells and status, errors | 6.8:1 on bg |
| stars | `#b7791f` | Rating stars | 3.4:1 on bg (graphic, ≥3) |
| `--rule` / `--rule-strong` | `#e6dac3` / `#cdbb9c` | Hairlines and dashed hours rules | Decorative |

## Typography
- **Display: Young Serif 400**, `letter-spacing: -0.01em`, `line-height: 1.1`, `text-wrap: balance`. `h1` `clamp(2.4rem, 5.4vw, 4.25rem)`; `h2` `clamp(1.9rem, 3.6vw, 2.75rem)`; inner `.page-hero h1` `clamp(2.2rem, 4.6vw, 3.6rem)`. The serif also sets list headings (`.spec h3` 1.3rem, `.themes h3` 1.35rem, `.area strong` 1.25rem), the marquee items, the footer tagline (1.45rem/1.3) and the "Family owned · Since 1980" line (1.15rem in walnut-600 followed by a 120px rule).
- **Body: Libre Franklin 400/500/600/650/700**, 1.0625rem/1.65, `text-wrap: pretty`. `h3` is Franklin 700, `clamp(1.1rem, 1.6vw, 1.25rem)`/1.3. Buttons use 650.
- **Emphasis:** the H1's second clause is an `<em>` restyled `font-style: normal; color: var(--green-700)` ("…, *built to outlast the weather.*").
- **Numerals:** `.story__year` "1980" `clamp(5rem, 13vw, 10rem)`/.85, `-0.03em`; `.rating__score` "4.6" `clamp(4rem, 9vw, 6.5rem)`; the `.bring` counters are serif 1.6rem in green. Hours and phone use `font-variant-numeric: tabular-nums`.
- No eyebrows over headings in the rebuild. Fonts come from fonts.googleapis.com; self-host them instead.

## Homepage anatomy
1. **Top bar + sticky header**: a 40px walnut bar (address · email · live status · socials), then a cream sticky header that gains a hairline and shadow on scroll. Logo · nav with a "Furniture" disclosure dropdown · a green round phone icon with "Call the showroom / (804) 785-6291". Phone: the bar collapses to the status line only, and the header becomes logo · green call circle · walnut menu square opening a right-hand drawer (`min(380px, 88vw)`).
2. **Hero, split not full-bleed**: `1fr 1.08fr`. Left: the serif "Family owned · Since 1980" line with a trailing rule, a 4-line H1 (second clause green), lead, a primary "Plan your visit" (pin icon) plus a ghost "Request a quote", and a star line "4.6 from 47 Google reviews". Right: the *real* lot photo (branded trailer, gazebo, poly sets) at 4/3.2 with a 22px radius, a live status pill pinned top-left, and a caption: "Our lot in Shacklefords. Every set out here is one you can sit at." Phone: one column with the photo below and its aspect ratio switched to 16/11. A fixed walnut call bar (Call now | Request a quote) sits at the bottom.
3. **Value strip**: a sand-100 band with serif claims (Amish crafted, Made in the USA, No-commission staff…) separated by green palm icons on a 60s marquee, with a **round pause button**. *Still a template pattern (L-015/L-016); replace it with a static list next time.*
4. **Plan your visit**: `1.1fr 1fr`. Left: H2, a serif location line ("Shacklefords, Virginia 23156"), a drive-time sentence, "Get directions" and "Call ahead", then a numbered "what to bring" list (`.bring`: 1 measurements / 2 colour ideas / 3 time to sit). Right: a paper card with a live status pill and an hours table. Today's row is green and bold with " · today" appended; closed days are rust. Phone: stacks.
5. **Heritage story** (sand band): `auto 1fr`. A huge walnut "1980" with "Family owned in Shacklefords" beneath, beside the H2 "A family showroom, not a catalog", two paragraphs, a 3-column `dl` of facts (Family owned / Amish-built / No-commission staff) under a strong rule, and an "Our story →" link.
6. **How it's built** (paper band): `.8fr 1.2fr`. Intro and link on the left. On the right, a spec sheet: a 2px walnut top rule, then rows of serif term | body text (Recycled poly lumber, Color all the way through, Stainless steel hardware, Amish joinery, Soap-and-water care). One column at 560px.
7. **Walk the showroom mosaic**: `repeat(4, 1fr)`, 230px rows. Tile 1 spans 2×2, tile 3 spans 2 rows, tiles 5–6 span 2 columns. Category tiles use real photos with a bottom walnut scrim and label + arrow. The last tile is a walnut text tile ("Furnishing a restaurant or community space?" in sand serif → Commercial furniture). It fills its rows at every breakpoint: 2 columns at 900px, and 160px rows with tiles 1 and 6 full-width at 560px.
8. **Quote band** (walnut): `.9fr 1.1fr`. Left: H2 "Tell us about your space", a check list in sand icons and a light ghost "Rather talk? (804)…". Right: a paper form card (name, phone, email *optional*, "I'm interested in", textarea), a lock-icon reassurance line ("We reply within one business day…") and a green "Send request".
9. **Reviews summary** (sand band): `auto 1fr`. A big "4.6 / 47 Google reviews" numeral, stars, the H2 "What Google reviewers mention most", one paraphrased sentence of themes, "Read them on Google" plus "More on our reviews →".
10. **FAQ preview**: a split with the H2 "Questions before you drive out?" and an "All FAQs" link, beside 4 `<details>` rows (cost, delivery, see before buying, custom colours) with round + icons.

Then the horizon stripe and the footer. The page has 10 blocks including the strip, longer than the ~8-section target.

## Other page patterns
- **Inner page hero** (`.page-hero`, `.page-hero--media`): no photo overlay at all. A cream band with breadcrumb, serif H1 (max 16em) and lead, plus an optional `1.05fr .95fr` rounded photo or **map** (`.map-frame` with a "Loading map of Shacklefords, VA" placeholder in `::before`).
- **Furniture** (`furniture.html`): a jump-link `.chip-nav` of icon chips under the H1. Each category is a `.split` / `.split--reverse` with an H2, a serif `.lead` subtitle in walnut-600, "Ideal for" sand pills (`.ideal`) and a "Request a quote" button that preselects the category (`[data-interest]` in `main.js`). A `.swatches` colour band (`auto-fill minmax(104px, 1fr)`, 5/4 chips with a faint plank texture `repeating-linear-gradient`) lists named colours. These swatches are information, not controls. Keep it that way, or make them real choices (L-042).
- **Reviews** (`reviews.html`): the rating block, then a 2-column `.themes` list (serif headings under a 2px walnut rule). The real-quotes `figure` grid stays `hidden` behind an "ADD REAL REVIEWS HERE" comment until the client supplies reviews. This is the honest pattern for a sample.
- **Service areas** (`service-areas.html`): a map hero, then a 3-column `.areas` ruled list (town · drive time; the home town in green).
- **FAQ** (`faq.html`): a `260px 1fr` layout with a sticky aside (left-ruled jump nav plus a walnut "Still have a question?" help card). Groups: Pricing & delivery, Visiting, Materials & care, Commercial & quotes. The aside turns into pill links under 900px.
- **Contact** (`contact.html`): `.85fr 1.15fr` with a ruled `.info-list` (icon · heading · text rows under a 2px walnut rule) and the form card, then a wide map.
- **Closing invitation** (`.cta-banner`, every inner page): a sand-300 rounded block `1.3fr auto` with "Come sit in it before you buy it." and the buttons.

## Signature elements
- **Live open/closed status.** It computes Eastern Time from a `HOURS` map and writes "Closed now · opens today at 10 am" into every `[data-open-status]` (top bar, hero pill, hours card), with the today row highlighted. The no-JS text is a truthful hours summary. See `assets/js/main.js` › "Store hours", and `assets/css/styles.css` › `.open-status`, `.hero__status`, `.hours tr.is-today`.
- **Giant founding year** as the story's anchor: `styles.css` › `.story__year`.
- **Spec-sheet list instead of icon tiles.** Serif term | plain explanation rows under a heavy rule: `styles.css` › `.spec`; reused as `.themes`, `.areas`, `.info-list`.
- **Logo horizon stripe.** An 8px sky-over-sand band above the footer, quoting the logo's beach: `styles.css` › `.horizon`.
- **Real-photo hero with an honest caption** and a status pill on the photo: `styles.css` › `.hero__photo`, `index.html` hero.
- **Mobile call bar.** A fixed walnut bar with two equal buttons (green Call now | sand Request a quote) and safe-area padding: `styles.css` › `.mobile-callbar`.

## Motion
Restrained, all CSS (predates the JS-only animation rule):
- A single authored entrance: `@keyframes settle` (opacity .35→1, 14px rise, .9s `cubic-bezier(.16,1,.3,1)`) on the hero H1 and photo, with the photo delayed .12s.
- The marquee runs 60s linear with a pause toggle (`.is-paused`) and stops under reduced motion.
- Hovers: tile images scale 1.04 over .8s, arrows nudge 3–4px, the dropdown chevron rotates, the FAQ + rotates 45°, and the drawer slides in `translateX` over .3s.
- The header shadow fades in on scroll.
- There are no scroll reveals and no parallax.

## Reusable components
- **Top bar:** `styles.css` › `.topbar` (walnut, live status, hides socials and extras under 900px).
- **Header:** `.site-header` (sticky cream), `.header-call` (round icon + label/number), `.has-dropdown` / `.dropdown` (click disclosure that closes on a second click of its own button, on an outside click and when focus leaves it), `.nav` drawer + `.nav-backdrop`.
- **Buttons:** `.btn--primary` (green), `.btn--cta` (sand on walnut contexts), `.btn--ghost` (rule-strong outline), `.btn--light` (on walnut), `.link-arrow`.
- **Cards and tiles:** `.visit__card`, `.form-card` (paper, `--shadow`), `.tile` / `.tile--text` (mosaic), `.cta-banner`.
- **Lists:** `.bring` (CSS-counter numbered list), `.spec`, `.themes`, `.areas`, `.info-list`, `.facts` (3-up `dl`), `.checklist`.
- **Badges:** `.open-status` / `.hero__status` (pill with a coloured dot), `.ideal` pills, `.chip` jump links.
- **Forms:** `.field` (48px, 1.5px rule-strong border, green focus ring at 4px/18%), `.opt` "(optional)" label, `.form-reassure` (lock icon + reply-time promise), `.form-status` (success/error panel), `.form-trap` honeypot.
- **Hours:** `.hours` table (dashed rules, right-aligned tabular times, rust "Closed").
- **FAQ:** `.faq details` with a round `.faq__icon`.
- **Footer:** `.site-footer` (walnut, 4 columns `1.5fr 1fr 1.1fr 1.3fr`: logo on a cream plate + serif tagline + sand "Get directions" / Pages / Furniture / Visit & contact with sand icons), `.footer-bottom` with the client's tagline "We rock your weekends." in sky-200 serif.

## How it went
- **Critique:** impeccable, 2026-10-06, **23/36 (Acceptable, 64%)**, report at `Concept Websites/Weknz Patio Furniture/.impeccable/critique/2026-10-06T10-10-33Z__index-html.md`.
  - Verdict: "Template-interchangeable". The Lawnx structure and personality were kept, every section ran pill → h2 → paragraph, and the site was green-dominant though the logo is sky and sand.
  - What worked: the live open/closed status with the today row, the real showroom gallery plus swatch grid, and the plumbing (sticky call bar, validation, skip link, reduced motion, JSON-LD).
- **Fixed in the rebuild that shipped:**
  - Warm walnut/cream/sand palette sourced from the logo.
  - The real tagline now appears in the footer.
  - Eyebrow pills and icon-tile rows are gone, replaced by `.spec` lists.
  - Real lot photo as the hero; a Plan-your-visit block with the address; FAQ answers for cost and delivery.
  - "No-commission staff" in place of the ambiguous "0% Sales commission".
  - A reply-time reassurance line on the form.
- **Lessons tied to this design:**
  - L-003: external-link arrows on internal/tel links; a dropdown that wouldn't close via its button; contradictory no-JS top-bar hours; decorative numerals at 3.3:1.
  - L-005: the palette ignored the logo. This is the origin of "start the palette from the logo".
  - L-006: wicker and wire stock for a poly maker; the lot photo buried under an overlay.
  - L-007: "0%" ambiguity; review headlines that didn't quote the reviews; the unused tagline.
  - L-008: price, delivery, lead time, warranty and address were missing.
  - L-009: 13 sections, ~14,000px on a phone.
  - L-011: a mailto form, letters accepted in the phone field, a relative og:image.
  - L-013: gold glow on `.btn--cta:hover`.
  - L-014: five labels for one action.
  - L-015: the template structure.
- **Still in the shipped code (L-016):**
  - The marquee, which now has a pause button.
  - The "Interested in" select still starts on "Not sure yet" (`index.html`, `contact.html`).
  - Six photos are each used 2–3× across pages (7 photos total).
  - With no endpoint, the form still falls back to opening the email app, with the outcome stated honestly.
  - Green, not sky, remains the action colour, and sky survives only as the stripe and tagline.
  - The hero `@keyframes` and CSS transitions break the JS-only motion rule.

## Reuse guidance
- **Fits:** showroom and walk-in retail (furniture, sheds, hot tubs, nurseries, garden centres, farm stores, antique malls), family businesses with a founding year, and anywhere the sale happens in person. Transferable:
  - The visit-first CTA order.
  - The live open/closed status plus the today-row hours table, with a truthful no-JS fallback.
  - A split hero with a real photo, an honest caption and a status pill.
  - A giant founding-year numeral.
  - Spec-sheet ruled lists instead of icon tiles.
  - A walnut quote band with a paper form card and a reply-time line.
  - A review-themes summary until real quotes exist.
  - A fixed two-button mobile call bar.
  - A logo-derived stripe as the one decorative device.
- **Keep to this site:** the walnut/palm-green/sand/sky palette, the palm icon and horizon stripe (both from the Weknz logo), Young Serif + Libre Franklin as a pair for this brand, "Come sit in it before you buy it.", and "We rock your weekends."
- **Don't copy:** the pausable marquee, the "Not sure yet" default, photo repeats across pages, and the 10-block homepage.
