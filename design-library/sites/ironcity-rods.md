# IronCity Rods & Customs: a night-garage showroom in black, charcoal and signal red, with condensed all-caps headlines
Custom car / hot-rod restoration shop · sample · October 2026 · 8 pages (home, about, services, builds, inventory, service areas, FAQ, contact) · hand-built (own `_src/build.py` generator, pre-pipeline) · Source: `Concept Websites/Iron City Website/`
Screens: `../shots/ironcity.webp`, `../shots/ironcity-phone.webp` · Inspiration: none in the library (the CSS says the hero finder was "adapted from the reference's search bar", but that reference wasn't kept) · Full page: `Portfolio Screenshots/IronCity Website.png`

## Identity
A restoration shop at night: near-black floors, charcoal cards, and one loud brand red (the logo's `#E30709`) used like a shop's signal light. Teko's condensed caps read as stencilled garage lettering. It suits a Punta Gorda, FL shop whose owner brought 25+ years of Pennsylvania ("Iron City") metalwork south and whose clients ship cars in from Quebec and California. Mood: muscular, nocturnal, precise, workshop-proud, collector-grade. What lifts it above a template: the inset "framed" page (12px gutter with 28px radius round the hero and footer), the real shop-floor bento of teardowns and chassis, and the "ship your car to us" caretaker banner. Weaknesses of the same kind are listed under How it went: a make-name marquee, an eyebrow over every heading, and icon-tile rows.

## Palette
| Token | Hex | Role | Notes (contrast on which surfaces) |
|---|---|---|---|
| `--black` | `#0d0c0c` | Deepest ink, hero base `#090808` | Background only |
| `--bg` | `#171616` | Page background | `--text` 16.5:1 |
| `--bg-raised` | `#1f1e1e` | Process section, steps, features, FAQ TOC | `--dim` 6.7:1 |
| `--charcoal` / `--surface` | `#2f2e2e` | Cards, footer card, form card, hours | `--muted` 6.6:1, `--dim` 5.5:1 |
| `--surface-2` | `#3a3939` | Hover surface | `--muted` 5.6:1 |
| `--red` | `#e30709` | Logo red: buttons, `.accent` headline words, tags, footer top rule | White on red 4.9:1. As text it's 3.7:1 on `--bg` (display sizes only) and **2.8:1 on charcoal (fails)**. Never use it for small text. |
| `--red-deep` | `#b90002` | Button hover | White 6.9:1 |
| `--red-ink` | `#ff6466` | Red *text* on dark (links, numerals, icons) | 6.3:1 on `--bg`, 4.7:1 on charcoal. This is the fix for red-on-dark body text. |
| `--text` | `#f5f4f4` | Headings and body | — |
| `--muted` | `#b8b4b4` | Lead and secondary copy | 8.8:1 `--bg`, 6.6:1 charcoal |
| `--dim` | `#a8a4a4` | Labels, captions, meta | 5.5:1 on charcoal (lowest surface) |
| `--line` / `--line-strong` | `rgba(255,255,255,.10/.18)` | Hairlines and card borders | Decorative |
| stars | `#ffb21e` | Rating stars, award icons | Graphic |
| success | `#5fd38a` | Form success | — |

## Typography
- **Display: Teko 500/600**, uppercase, `letter-spacing: .01em`, **`line-height: .88`** (`.display, .h1, .h2, .h3`). `.h1` `clamp(3.6rem, 9.2vw, 8.6rem)`; `.h2` `clamp(2.7rem, 5.4vw, 4.8rem)`; `.h3` `clamp(1.8rem, 2.6vw, 2.3rem)`/.95; inner `.page-hero .h1` `clamp(3.4rem, 8vw, 7.4rem)`. A red `.accent` span carries the second clause of most headlines ("Built right. / **The first time.**").
- **Body: Work Sans 400–700**, 1rem/1.6. `.lead` `clamp(1.02rem, 1.3vw, 1.15rem)` in `--muted`, max 58ch.
- **Labels:** `.eyebrow` .78rem/600, `.18em` tracking, caps, preceded by a 26×2px red rule. Finder and spec labels are .7–.74rem caps with .14em tracking.
- **Numerals:** Teko does the work: `.price` 2rem, `.stat` `clamp(4rem, 6vw, 5.4rem)`/.8, `.stats strong` `clamp(3rem, 5vw, 4.4rem)`, outlined process numbers `.step__num` 5.2rem with `-webkit-text-stroke: 1.5px`.
- Fonts load from fonts.googleapis.com. This is against the current rules; self-host instead.

## Homepage anatomy
1. **Framed hero**: a full-bleed photo inside the 12px frame (`min-height: min(100svh − 24px, 940px)`), content bottom-aligned. Left-to-right scrim from `rgba(8,7,7,.92)` to transparent at 72%, plus a bottom scrim. It holds a glass rating badge (stars · 5.0 on Google · BBB), a two-line Teko H1 with a red second line, and a lead. The bottom row is a 3-select **build finder** (Service / Vehicle / Budget + "Get a Quote", `grid-template-columns: repeat(3, minmax(0,1fr)) auto`, blur 16px glass) beside a light **locator card** (red pin tile, "View on the map", address). Phone: the photo is clamped to a 470px top band at `object-position: 86% 55%`, a solid gradient takes over below, and the finder stacks to one column. The badge goes `nowrap` and hides its location under 560px.
2. **Make strip**: 12 make names in Teko 2–2.9rem `#8f8b8b`, separated by red 9px rotated squares, on a 38s CSS marquee. Reduced motion wraps it centred (that's what the screenshot shows). *Template pattern; don't copy (L-015).*
3. **What we offer**: a `1fr 1.05fr` split. Left: eyebrow, H2 "Full-service restoration / under one roof", lead, then a `.numbered` list (01–03 in red-ink Teko, hairline rows) and a red button. Right: an asymmetric tile cluster (`1.15fr 1fr`): a tall photo tile (3/4.1, top scrim, "Show-quality builds"), a red stat tile ("25+" over a bleed photo), and a dark "Coast to coast" tile. Phone: one column.
4. **Cars for sale rail**: section-head with a "View all inventory" button. Filter chips (`aria-pressed`, the pressed one goes white-on-black). A horizontal scroll-snap rail (`grid-auto-columns: clamp(268px, 24%, 312px)`) of `.car-card`s: photo with tag and save button, title, location · type, a 3-up icon spec row (miles / engine / trans), a Teko price, and "View details" opening a `<dialog>` with a spec table. Prev/next square buttons (the next one red).
5. **How it works**: a `--bg-raised` band with a 4-column `.steps` grid (2 columns at 1024px, 1 at 560px). Outlined red numerals 01–04, an icon chip top-right, a Teko H3, short copy. Hover tints the border red.
6. **Recent builds bento**: `repeat(4, 1fr)`, `grid-auto-rows: clamp(180px, 19vw, 260px)`, with the first tile spanning 2×2. Real shop photos (teardown, chassis, interior), each with a red caps tag and a Teko title over a bottom scrim. 2 columns at 860px, 1 column at 240px rows at 520px.
7. **Ship-your-car banner**: a rounded charcoal gradient card (`120deg, #2f2e2e → #120f0f`), `1fr 1.2fr`. Copy, a pill list of regions (Quebec / Washington State / California / East Coast) and a button sit on the left. A '69 Camaro cut-out with `mix-blend-mode: lighten` sits on the right, so the black studio background disappears into the card. Phone: the car moves above the copy.
8. **Reviews**: section-head with a `.rating-card` (red "5.0" Teko block + stars + "Leave a review"). Three quote cards with initials avatars and the car model plus town as the attribution ("1967 Chevelle SS · Port Charlotte, FL"). One column at 960px.
9. **Visit (closing beat)**: `1fr 1.05fr`. H2 "Start your build with us **today**", lead, "Contact us", and an hours card (`dl` grid, caps labels, nowrap values). Right: a Google map iframe darkened with `filter: grayscale(1) invert(.92) contrast(.88)`, a light address chip on top, and red-icon contact chips for email and phone below.

Then the footer card.

## Other page patterns
- **Inner page hero** (`.page-hero`): framed photo, 440–620px tall, bottom-aligned, breadcrumb, and a big Teko H1 with a red second line ("Find your / **dream car**"). Used on every inner page.
- **Services** (`services.html`): a sticky centred pill sub-nav (`.service-nav`, `width: fit-content; margin-inline: auto`, active pill red, scroll-spy via `[data-spy]`). Then five `.service-block`s alternating `.split` / `.split--flip`, each with a red-ink numeral, H2, a two-column check `.service-list` and a photo. A red-tinted `.callout` (icon tile · text · button).
- **Inventory** (`inventory.html`): a `.filter-bar` (search plus 3 selects in one glass bar, `1.4fr repeat(3, 1fr)`), a results meta line, an `auto-fill minmax(270px, 1fr)` card grid, a dashed empty state, and the car `<dialog>` (`1.15fr 1fr`, 2-column `.spec-table` with 1px gap lines).
- **Builds** (`builds.html`): chip-filtered `.gallery` (`auto-fill minmax(290px, 1fr)`, 4/3.2 shots) opening a `<dialog>` lightbox with prev/next and keyboard support. `.case` studies: a 2-column media/body card alternating sides, a pill meta row, and a `dl` of Challenge / Solution in red-ink Teko.
- **About** (`about.html`): a story `.split` with a red `.split__badge` ("25+ Years of experience") pinned to the photo corner, a 4-up `.stats` strip (hairline-divided, red-ink `em` suffixes such as "25+" and "5.0★"), `.features` cards and a 4-up `.awards` row.
- **FAQ** (`faq.html`): a `280px 1fr` layout with a sticky TOC (scroll-spy) and `<details>` cards whose + icon rotates 45° and turns red when open. The TOC becomes a horizontal scroller under 900px.
- **Contact** (`contact.html`): a `1.35fr 1fr` form card plus an `.info-stack` of 4 red-icon info cards. Radio pills (`:has(input:checked)` red tint). `.form-call` shows "Prefer to talk? Call…" above the form on phones only. A success panel replaces the form.
- **CTA band** (`_src/build.py` › `cta()`): a framed photo under a red-to-black vertical scrim (`rgba(150,0,2,.88) → rgba(20,8,8,.82)`), centred H2, and a white button plus a phone ghost button. Used on inner pages.

## Signature elements
- **The frame.** The hero, page heads and CTA band sit 12px (8px on phones) inside the viewport with a 28px radius, and the fixed header floats in the same inset: `assets/css/styles.css` › `.frame`, `--frame-gap`, `.site-header`.
- **Red second line.** Every headline splits into a white statement and a red payoff in a `.accent` span: `_src/pages/*.html` › `<span class="accent">`.
- **Hero finder plus locator.** A glass 3-select qualifier bar that pre-fills the contact form, beside a light address card: `styles.css` › `.finder`, `.locator`; `_src/pages/home.html`.
- **Blend-mode cut-out.** A black-studio car photo dropped onto a dark gradient card with `mix-blend-mode: lighten`, so no masking is needed: `styles.css` › `.banner__img`.
- **Outlined Teko numerals** for process steps: `styles.css` › `.step__num` (`color: transparent; -webkit-text-stroke`).
- **Dark-inverted map.** A Google embed recoloured to the theme by a CSS filter, with a light address chip: `styles.css` › `.map iframe`, `.map__chip`.

## Motion
All of it is CSS transitions plus a small vanilla `assets/js/main.js` (no GSAP). This predates the "all animation in JS" rule, so treat it as a list of *what* moves, not *how*.
- **Header:** the bar never resizes. `.is-scrolled` (scrollY > 24) slides it up with `translateY`, fades in a blurred `::before` backdrop and scales the logo 64→54px (`--logo-scale: .84375`) at 280ms `cubic-bezier(.22,1,.36,1)`. This is the source of the CLAUDE.md shrinking-header rule.
- **Reveals:** `.reveal` fades and rises 28px over 700ms, with stagger set by an inline `--d` (60–240ms). The IntersectionObserver plays once (`rootMargin -8%`, threshold .08), so it doesn't replay the way the current template does.
- **Hovers:** cards lift 4px and their images scale 1.05–1.06 over 0.9–1.2s; arrows nudge 4px; the nav underline grows with `scaleX`.
- **Other:** the 38s make marquee (pauses on hover, wraps under reduced motion); dialogs enter with a 260ms `@keyframes dialog-in`; the rail scrolls smoothly from its buttons. There's no parallax.

## Reusable components
- **Header:** fixed and inset, logo · centred nav with a red `scaleX` underline · phone · red quote button. Under 1180px it switches to a call square plus a menu square, and under 560px the call square turns solid red. `styles.css` › `.site-header`, `.header-call`, `.mobile-menu` (full-screen, Teko 2.6rem links).
- **Buttons:** `.btn` (red, 50px, radius 10px, arrow nudge), `.btn--ghost`, `.btn--light`, `.btn--sm`; `.link-arrow` in red-ink; `.icon-btn` 48px squares.
- **Chips:** `.chip[aria-pressed]` filter pills; `.banner__pills` / `.case__meta` are static pills.
- **Cards:** `.car-card` (padded 10px, inset media, 3-up `.specs`, Teko `.price`), `.tile--photo` / `.tile--red` / `.tile--dark`, `.review`, `.info-card`, `.area`, `.region`.
- **Gallery:** `.bento` (4-column, first tile 2×2) and `.shot` (tag + Teko title over a scrim).
- **Rating:** `.hero__badge` (glass pill) and `.rating-card` (red score block).
- **Forms:** `.finder` (glass select bar), `.form-card` / `.form-grid` / `.field` (52px fields, red-ink focus ring), `.radio-row`, `.form-success`.
- **Hours:** `.hours` (`dl` with `auto auto` columns and nowrap values).
- **Footer:** a charcoal `.footer-card` with a 3px red top border, 4-column grid (`1.5fr .8fr .9fr 1.4fr`): brand + address / Menu / Fast Links / a Teko newsletter. `.socials` circles turn red on hover.

## How it went
- **Critique:** impeccable, 2026-10-06, **28/40 ("Good")**, report at `Concept Websites/Iron City Website/.impeccable/critique/2026-10-06T12-52-55Z__index-html.md`. Verdict: "Well crafted but category-interchangeable", reading as a dark exotic-car dealer template. The Iron City steel heritage, Anthony, the real shop-floor photos and the phased-budget promise "have no visual form".
- **P1s:**
  - No tap-to-call on mobile. Fixed since: the red `.header-call` under 560px and `.form-call` above the form.
  - Generic dealer identity. Only partly fixed.
  - The hero finder sent default answers. Fixed since with empty "Choose…" options, though "Not sure yet" remains as a budget option.
- **Contrast:** P3 contrast fixes were applied (`--dim` #918d8d to #a8a4a4, `--red-ink` #ff4a4c to #ff6466). The page now ends on the Visit block, not a CTA band.
- **User corrections:** the red glows (halos) and the "Free quote" vs Time & Materials pricing contradiction. The site's original lessons became the CLAUDE.md rules (L-000): repeated photos, a plate behind hero text, cropped cut-outs, glows, discount positioning, CTA sprawl, mobile wrapping, select defaults, the "null" prefill, contrast on raised cards, layout-property animation, and the Netlify 401.
- **Lessons tied to this design:**
  - L-003: two names for one page ("Exotic Inventory" and "Cars For Sale" in the footer); the outline "04" looked broken; a 10-car grid left 2 orphans.
  - L-004: save/bookmark toggles with nowhere to view saved cars; a newsletter whose demo "succeeds".
  - L-006: a studio Jaguar E-Type hero and discounted modern Mustangs on a classic-craft shop; the red headline collided with the red car.
  - L-007: struck-through "was" prices (still in `_src/build.py` › `CARS` `was=` and `.price s`) read as a discount dealer.
  - L-008: transit insurance, storage and deposits unanswered.
  - L-009: 9 sections, ~11,700px on a phone.
  - L-010: the finder's budget list still offers "Not sure yet" as an answer.
  - L-012: no next-steps line above the submit button.
  - L-013: red glows.
  - L-014: ~20 CTA labels, ~7 solid-red buttons on the homepage.
  - L-015 / L-016: the make marquee, 30 of 66 headings under a kicker, 50 icon-led cards.
- **Against the current rules,** the shipped code also has headline `line-height: .88` (rule: ≥1.05, L-051), Google-hosted fonts, a relative `og:image`, and CSS transitions/keyframes instead of JS motion.

## Reuse guidance
- **Fits:** auto restoration, custom fabrication, motorcycle and performance shops, tattoo studios, boxing gyms, barbers and craft workshops. Any dark, masculine, "built by hand" trade with one strong logo colour. Transferable: the inset frame and floating header, the two-tone headline (statement plus coloured payoff), the `--red` / `--red-ink` split (one hue for fills, a lighter one for text on dark), the blend-mode cut-out banner, the shop-floor bento with a 2×2 lead tile, the qualifier finder (with empty "Choose…" defaults), the darkened map with a light chip, and a mobile call button that turns solid when the quote button hides.
- **Keep to this site:** the exact black/charcoal/`#E30709` + Teko combination (it is IronCity's logo), "Built right. The first time.", and the hot-rod make vocabulary. Don't copy at all: the make marquee, eyebrows over every heading, icon-tile feature rows, the struck-through prices, the save toggles, `line-height: .88`, and the per-section CTA labels.
