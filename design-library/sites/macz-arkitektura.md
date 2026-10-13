# Macz Arkitektura: the firm's name carved across a dusk sky, inside one dark framed card
Architecture / design-and-build firm · sample (real business, public facts only) · October 2026 redesign (replaces the light "sunrise" design, archived in `_temp/Macz Arkitektura-previous-2026-10-10/`) · 6 pages (Home, About Us, Our Services, Project Gallery, Contact Us, 404) · pipeline build, GSAP on · Source: `Concept Websites/Macz Arkitektura Website/`
Screens: `../shots/macz.webp`, `../shots/macz-phone.webp` · Inspiration: `../inspiration/architect-reference.webp` (learned as `../references/architect-reference.md`) · Full page: `Portfolio Screenshots/Macz Arkitektura Website (2).png`

## Identity
A redesign that kept every word of the previous site and moved it into the reference's dark, framed studio layout. The whole site sits in one rounded near-black "shell" floating over a warm amber blur of a night city. Inside it, every section is a rounded panel. The hero carries the firm's name, MACZ, carved huge and translucent across the dusk sky over a whole lit tropical house, with "A R K I T E K T U R A" spaced underneath. The real H1, the firm's sign-off "Details tell stories", sits small at the bottom left.

The logo's sun yellow (#FEC726) and brown (#261A0E) are the only brand colours: a yellow pill with a brown arrow disc is the single CTA shape. The rest is a warm Material-3 dark scheme seeded from that yellow.

The work is still presented as drawings: every project gets a ruled title block, and the owner's bilingual captions are quoted verbatim. Mood: dark, warm, quietly luxurious, exact. It passes the competitor test through:
- the name in the sky;
- the logo's own colours;
- the real renders, boards and groundbreaking photos;
- the Tagalog quotes.

## From the inspiration image
The brief's reference was one long homepage comp, "Aakriti Architects" (`client-assets/architect-reference.webp`). The brief asked to follow it closely.

**Taken:**
- the rounded dark shell over a blurred backdrop;
- the header floating inside the hero card, with a pill nav where the current page is a light pill;
- the round icon buttons and the CTA pill with a trailing arrow disc;
- the giant translucent name across the sky with a spaced sub-name;
- frosted glass fact cards at the bottom right of the hero;
- a frosted badge on the story photo;
- heading-left rails;
- a numbered services tile grid;
- a four-up project row with an "Explore all projects" ghost pill;
- a featured project with a spec list;
- a closing panel with contact columns and a photo carrying the CTA;
- a thin footer.

**Changed on purpose:**
- The hero stat tiles with invented numbers became two true fact cards: the real Facebook figure ("100% recommend us", from 11 reviews, linked) and the Alabang base with its three regions. The testimonial card is folded into the first one.
- The icon tiles became numbered tiles, since qa.py blocks icon-tile rows.
- There are no eyebrow labels.
- The white CTA pill became the logo's sun-yellow pill with brown ink (L-005).
- The reference's cool greys became warm M3 tones.

## Palette
Material 3 dark scheme from seed #FEC726 (`assets/css/styles.css` › `:root`, generated with `materialyoucolor`).

| Token | Hex | Role | Contrast |
|---|---|---|---|
| `--c-page` | #0B0803 | Behind the shell, under the blurred photo | |
| `--c-shell` | #120E05 | The rounded page card | text 14.9 |
| `--c-bg` | #191409 | Panels | text 14.2, muted 10.8, gold 10.8 |
| `--c-surface` | #221D13 | Tiles, form cards, mobile menu | text 13.0, muted 9.8 |
| `--c-raised` | #2E291F | Hover, inputs | text 11.2, muted 8.5 |
| `--c-text` | #ECE1D1 | Body ink; also the light "current page" nav pill (ink #120E05 on it, 14.9) | |
| `--c-muted` | #D2C5AC | Ledes, secondary copy | ≥8.5 on every surface |
| `--c-gold` | #E1C37F | Numerals, title-block labels, links, thin accents | ≥8.5 |
| `--c-line` | #4F4633 | Hairlines between sections and in title blocks | decorative |
| `--c-outline` | #9B8F79 | Field and ghost-button borders | ≥5.3 (≥3:1 needed) |
| `--c-brand` | #FEC726 | Logo sun: CTA fill, process rail and nodes, quote cite | 11.7 on panels |
| `--c-on-brand` | #261A0E | Logo brown: CTA text and the arrow disc | 10.8 on brand |
| Photo text | #FFF / #F1E9DC / #ECE3D4 | Over a dark scrim; `.page-head > .media::after` .42 plus the photo-card gradient; phones get a stronger base scrim (L-032) | |

No glows: the shell has one neutral elevation shadow (0 30px 80px / .45), and so does the mobile menu panel.

## Typography
- **Display: Playfair Display 400** for h1–h4.
  - Sizes: h1 clamp(2.5rem, 6.2vw, 4.5rem)/1.1; h2 clamp(1.9rem, 3.6vw, 2.9rem)/1.12; h3 1.3rem/1.25.
  - Quote band: clamp(2rem, 4.6vw, 3.6rem)/1.15.
  - `text-wrap: balance`, sentence case.
- **Body/UI: Manrope** 400/500/600/700/800. All numerals use Manrope with tabular-nums.
- **The sky mark:** `.hero__name` in Manrope 800, clamp(6.5rem, 27vw, 24rem)/.8, `rgb(255 248 236 / .2)`, `aria-hidden`. It is one all-caps word with no descenders, so the .8 leading is allowed through `ALLOW_PATTERNS["tight-leading"]`. Below it, `.hero__sub` is Manrope 500 with .55em tracking.
- **Caps only for tiny labels:** title-block `dt` (.78rem, 700, .1em, gold) and the quote cite (.82rem, .12em, brand).
- Both families are self-hosted (`_src/partials/fonts.html`); Manrope 400 is preloaded.

## Homepage anatomy
Eight sections (`_src/pages/home.html`), all inside the shell.

1. **Hero photo card:**
   - Pexels 35361412, a whole two-storey tropical house (landscape), colour-graded from overcast to a warm grey dusk with its windows lit (`_temp/macz-redesign/grade_hero.py`: dilated sky mask, then a gradient sky). `min-height: clamp(38rem, 94svh, 54rem)`, 50% parallax, centred crop.
   - Phones get their own portrait crop through `<picture>` (`<source media="(max-width: 899px)">`, 1125×2250 WebPs at 480/800/1125). The landscape file showed only 28% of its width at 390. `.media > picture { display: contents }` lets the frame rules treat the inner `<img>` as a direct child.
   - The header floats inside the card.
   - Bottom left: the H1, a lede, the CTA pill and a ghost phone pill. Bottom right: two `.glass` fact cards, hidden below 900px so the CTA stays above the fold.
2. **Story panel:**
   - A split with the H2 "One team, from the first site visit to the final turnover" and a lede.
   - The 01–03 values as ruled rows and a "More about us" ghost pill.
   - A drafting-hands photo with a frosted `.figure-badge`: "One team, design to turnover".
3. **Services rail:** six numbered `.tile`s (01–06), each linking to its `services.html#id` anchor, with a round arrow `.go` disc. Two columns on phones.
4. **"Recent projects, from BGC to Biñan":**
   - Four `.proj` cards: the NMR board, GIC render, KAC board and FaB pole. Each mirrors the lead image of its gallery entry, a disclosed knowing repeat.
   - Board crops are art-directed with object-position so no clipped title lettering shows.
   - Two columns on phones.
5. **Featured "Now underway: The NMR Project":** the owner's "Not just modern…" lede, a three-row title block, and a "See the NMR renders" ghost pill beside the client dining render at 3/2.
6. **Quote band:**
   - A rounded `.band` with sunlit columns at 50% parallax.
   - `<h2 class="band__quote" data-gsap="split">` "Trends come and go. Timeless design stays."
   - Cited in brand yellow.
7. **Process panel:** "How a Macz project runs", an `ol.steps` with `data-gsap="trace"` (a yellow rail draws down and the nodes light up).
8. **Closing panel:**
   - Left: the H2 "Have a space in mind? Let's talk it through." and a lede.
   - Ruled fact columns: phone, email, address. A fourth, "100% recommend us", shows only below 900px, where the hero fact cards are hidden (each idea once per viewport).
   - Right: a shadowed-steps photo with the CTA pill laid over it.

Then the footer panel.

## Other page patterns
- **Page head:** the hero recipe in a shorter photo card, with the H1 and intro bottom left, `sizes="100vw"`, a .42 darkening layer and parallax. Photos: pencil-on-plan (About), tile-laying (Services), wood-slat facade (Gallery), sun-through-blinds (Contact). The 404 page head has no photo.
- **About:**
  - a split: "Why one team designs and builds" beside the material-samples photo;
  - the MACZimum rail, an owner quote set large;
  - "Where we work": a regions title block with locations of recent projects;
  - a plain closing panel.
- **Services:**
  - seven numbered `.service` cards, each with an anchor id;
  - the fit-out split: a plasterer photo with a three-column `.scope` list;
  - "How pricing works" as a rail with no prices;
  - an FAQ rail of `<details>` with a round +/− disc.
- **Gallery:**
  - NMR: `.project__head` (intro and the Tagalog quote left, full title block right) over a `.mosaic--nmr` 6-column grid. The sofa and piano views of one room span 3 each, then three renders span 2 each.
  - GIC: a `.board` with the render and the three-panel strip at native aspect, capped at 62rem.
  - KAC and FaB: a `.project-pair`, two columns of text, title block and board. FaB shows the pole and the title sheet as a 2-up `.fab-set`.
  - "Smaller projects": two text cards with mini title blocks, plus an Instagram link.
- **Contact:**
  - The quick card comes first in the DOM, so phones get Call before the form. It holds a ghost "Call 0919 123 4567" pill, email, map and hours.
  - The Web3Forms form in a raised card: selects start on "Choose…", phone becomes required for call or text, and the `NEXT_STEPS` note sits in a bordered box above "Send project details".

## Signature elements
- **The name in the sky:** `.hero__mark` / `.hero__name` / `.hero__sub`. It is `aria-hidden`; the real H1 is separate.
- **The shell:** `.shell` (radius 28px, 1px white/.07 rim), `width: min(100% - 2 * clamp(0px, 4vw, 72px), 90rem)` with the same margin, so up to 72px of backdrop shows on wide screens. It sits over `body::before`, a fixed Manila night photo pre-blurred to 720px and warm-duotoned (#0b0803 → #5a3c14 → #e8b058, `glow_backdrop.py`) under a .15–.3 darkening. `body` must stay transparent, or its fill hides the layer (L-060). Below 600px the shell goes edge to edge and the panels keep 16px radii.
- **Sun pill with brown arrow disc:** `.btn-primary::after` uses the `--arrow` data-URI disc. It is the one CTA shape sitewide, and the form submit uses the same shape.
- **Glass:** `.glass` (`--glass` rgb(25 20 9 / .62) plus backdrop blur, `--glass-line` rim) for the hero facts and the photo badge only.
- **Drawing title block** (`.titleblock`): gold tracked labels and hairline rows, on every project and the featured block.

## Motion
- **main.js:**
  - `.reveal` entrances replay on re-entry;
  - 50% parallax on the hero, page heads and the quote band;
  - the header gets a frosted pill backdrop through `::before` once scrolled, with the brand scaled to .92;
  - the mobile menu and FAQ animate through `morph()`.
  - There is no CSS transition or animation anywhere.
- **GSAP** (`assets/js/motion.js`, ScrollTrigger and SplitText, all inside a `matchMedia` reduced-motion gate):
  1. Hero: the MACZ mark drifts down (yPercent 35) and fades to .25 as the hero scrolls away (scrubbed; never hidden at load).
  2. Quote band: the split-line headline (the target is an h2, because SplitText's aria-label is prohibited on a `<p>`).
  3. Process: the steps trace (the rail draws, the nodes light).
- **Reduced motion:** everything is static and visible.

## Reusable components
- **Header** (`.site-header`): sticky, with `margin-bottom: -header-h` so it floats over the first photo card.
  - The pill nav sits inside a translucent capsule.
  - The phone number shows from 1200px; the round call button and the menu button below that.
  - The header CTA is hidden under 600px.
- **Buttons:** `.btn-primary`/`.btn-submit` (the sun pill and disc), `.btn-ghost` (1px outline pill, also used for every phone button), `.go` (round arrow disc). The light `.btn-call` pill was cut as a second primary-looking style.
- **Panels and rails:** `.panel` (rounded section group, hairlines between sections) and `.rail` (sticky heading left at 1:2.2, content right).
- **Cards and photos:** `.tiles`/`.tile` (numbered link tiles), `.proj-row`/`.proj` (four-up photo cards), `.feature` (spec block beside a photo), `.band` (rounded photo band), `.closing` (contact columns and photo CTA; `.closing--plain` for inner pages).
- **Gallery layouts:** `.mosaic--nmr`, `.board`, `.project-pair`, `.fab-set`, `.also`.
- **Forms and FAQ:** `.faq` (`<details>` with a round +/− disc), `.form__next` (a bordered "what happens next" box).

## How it went
- **QA:** qa.py 0/0. Browser QA 0 errors and 9 warnings, all accepted:
  - 8 DPR-1 "blurry" srcset picks on parallax-overscanned page heads;
  - one 2.5s lab LCP (the runs vary ±0.2s).
- **Lighthouse mobile:** index 97, about 98, contact 99, projects 97, services 98; accessibility, best practices and SEO 100 on every page. Once the backdrop actually rendered, it cost the homepage 4 points (93) until it went behind `@media (min-width: 600px)`. Phones never see it, so they don't fetch it.
- **Finish reviewer (impeccable), two P1s, both settled by the user at the critique gate:**
  - The hero, a portrait photo cropped to sky and soffits, didn't show the reference's whole lit house under the name. User chose "New landscape photo": an overcast Pexels house, colour-graded to dusk, with a separate phone crop.
  - The shell filled almost the whole screen, so the backdrop barely read. User chose "Widen and lighten": a 72px gutter and an amber-duotoned backdrop.
  - Fixed automatically as rule violations: the second primary-looking `.btn-call` style (now ghost), and the homepage fact repeats. P2/P3 items were skipped and logged.
- **impeccable detect:** 41, all minor or false positives (cramped-padding on containers, the menu panel shadow, one caps cite).
- **Browser-QA catches during the build:**
  - the About H1 at 2.32:1 on a pale photo (fixed with a page-head darkening layer);
  - the brand in the header at 4.4:1 over the sky (fixed with a stronger top scrim);
  - SplitText on a `<p>` (axe);
  - 9 homepage sections (trust facts folded into the closing);
  - LCP 2.6–2.9s from `sizes="160vw"` page heads.
- **Self-caught:**
  - the phone 2-column project row lost the cascade (L-063);
  - the board previews showed clipped title lettering;
  - the backdrop never rendered under body's fill, so two regrades were judged blind (L-060, now a qa.py check).
- **User-caught (process, L-058):** after "Yes, redesign it" the redesign started from the old brief instead of opening the brief form.
- **Tooling:**
  - an interrupted build left a 0-byte cached WebP (L-059), now written atomically;
  - the first redesign deploy made a second Worker because the archive took `.pipeline/` (L-061). deploy.py now reuses the archived state.
- **Weaknesses left in:**
  - The hero is graded stock, not Macz work (no client photo is wide or sharp enough).
  - The GIC renders are only 689–921px wide.
  - Services card 07 sits alone on the last row at 1440.
  - The homepage is still about 7,600px tall on phones.

## Reuse guidance
**Fits:** architects, interior studios, design-build firms, luxury renovation and joinery, boutique hotels or venues with one strong exterior photo. Moods: dark, warm, editorial, premium.

**Transfers:**
- the framed shell over a blurred backdrop;
- the pill-with-disc single CTA shape;
- glass fact cards that hold only true facts;
- heading-left rails;
- the four-up preview row that mirrors gallery leads (disclose it);
- the title-block spec lists;
- an M3 dark scheme seeded from the logo colour;
- a duotoned blurred backdrop in the brand's own warm hue (a B&W one reads as grey fog);
- `<picture>` art direction when a landscape hero shows under a third of its width on phones;
- colour-grading an overcast stock exterior to dusk when no real dusk shot exists (dilate the sky mask before feathering, or the roofline haloes);
- the hero-mark scroll drift as a quiet GSAP moment.

**Keep to this site:** the MACZ sky mark and the "Details tell stories" voice, the exact sun/brown/warm-black palette, the Tagalog captions, the graded dusk-house hero.

**Don't clone:** the reference's homepage order whole. Recombine it with another entry's patterns.
