# Aakriti Architects: a dusk-lit studio in one dark framed card, the firm's name carved across the sky
Kind: website homepage · Subject: architecture and interiors studio · Learned: 2026-10-10 · Image: `../inspiration/architect-reference.webp` · Original: `../inspiration/originals/architect-reference.png`

## What it is
A one-page concept for an architecture and interiors studio, sold through dusk renders of lit modern houses and warm interiors. The whole page sits inside a rounded dark card floating over a blurred dusk photo, so it reads as a luxury object rather than a web page. Mood: dark, warm, luxurious, calm, editorial.

## Layout anatomy
1. **Header** — inside the hero card: monogram + spaced-caps wordmark left, centred pill nav (active item a white pill), a white "Consultation" pill CTA with a dark arrow disc, then three round outline icon buttons (phone, Instagram, map) right.
2. **Hero** — full-width rounded card, ~26% of the page: a dusk photo of a lit house over water; the firm name in giant translucent white caps (~20vw, ~15% opacity) fills the sky behind the roofline; a tracked-caps subline under it; a two-line sentence-case tagline bottom-left with a small sub; a centred white pill "View Projects" with an arrow disc at the bottom; three frosted glass stat tiles stacked bottom-right; "SINCE 2000 ——" lower left.
3. **About split** — dark panel: serif two-line headline ("Inspired by purpose. Driven by detail."), a paragraph, three small line-icon values in a row, a ghost pill link; right, a large rounded interior photo with a frosted "Since 2000" badge overlapping its lower-left edge.
4. **Services** — heading left (1/4), six dark rounded tiles right, each a thin gold line icon, a serif title, a short line and a round arrow button.
5. **Selected projects** — heading left, ghost pill "Explore all projects" right, then four equal rounded photo cards in a row, full bleed to the card edge.
6. **Featured project** — text left (serif headline, paragraph, a dotted spec list: location, type, area, ghost "View Project"), a wide rounded photo right (~65%).
7. **Testimonial** — heading left; a raised rounded panel with prev/next arrows, a quote mark, the quote, a star rating with "Rating on Google", and a round portrait plus name.
8. **Closing** — a rounded panel: serif headline "Let's create something extraordinary together.", contact columns with line icons (phone, email, address), and a small rounded photo with a white "Book Consultation" pill laid over it.
9. **Footer** — a single thin row: monogram + wordmark, ©, legal links, round social icons.
Phone: the hero card goes full width with the giant name shrinking to one line, the stat tiles drop under the CTA, splits stack photo-first, the service tiles become a 2-column grid and the project row a swipe rail.

## Palette
| Hex | Role | Notes |
|---|---|---|
| #141413 | page / deepest surface | near-black, warm |
| #1F1F1D | panel surface | the sections inside the card |
| #282725 | raised tiles and cards | services tiles, testimonial panel |
| #3F3E3D | hairlines, outline buttons | 1px rules between sections |
| #F2EEE8 | ink | warm off-white headings |
| #B6B1B1 | muted text | body copy on dark |
| #C9A46A | accent | thin gold line icons, monogram (sampled by eye; the photos carry the warmth) |
| #FFFFFF | primary CTA fill | white pills with a black arrow disc |

## Typography
- Display: a high-contrast transitional serif, regular weight, sentence case, two-line headlines at ~2.4× body (close: Cormorant Garamond 500, Playfair Display 400).
- Hero name: a wide geometric sans in caps at giant size and low opacity (close: Montserrat 600, Jost 500).
- Body: a clean neo-grotesque at small sizes in muted grey (close: Inter, Jost 400).
- Labels: tiny tracked caps (≈.3em) for section labels and the "INTERIORS & ARCHITECTURE" subline.
- Numerals: the stats use the sans at a light weight.

## Signature ideas
- The page as one dark rounded card floating over a blurred dusk photo.
- The firm's name carved across the sky of the hero photo in giant translucent caps, with the roofline in front.
- White pill buttons with a dark round arrow disc: one button shape used everywhere.
- Frosted glass badges overlapping photo edges ("Since 2000").
- Everything rounded (24px cards, full pills), thin 1px rules, generous dark space between panels.
- Dusk lighting in every photo: warm interior light against a cool sky ties the set together.

## Patterns to borrow
- hero | Name across the sky | the business name in caps at ~18–22vw, `color: rgb(255 255 255 / .16)`, set behind the photo's subject (the photo's top layer is a cut-out of the building, or the text sits only over the sky) with the real H1 small and bottom-left.
- hero | Framed hero card | the hero is a rounded (24–28px) photo card inset by the page gutter, header inside its top edge, copy and CTA aligned to the bottom.
- cta | Pill with arrow disc | `border-radius: 999px` button with a trailing 2em circle holding an arrow, white on dark (the disc inverts); ghost version = 1px outline pill.
- detail | Frosted badge on a photo edge | a small rounded panel with `backdrop-filter: blur(12px)` and a translucent dark fill, overlapping the lower-left corner of a photo by ~10%, holding a date or one fact.
- section | Heading-left rail | each section is a 1:3 grid: the heading and one link on the left, the content (tiles, cards) on the right; a 1px rule between sections.
- gallery | Four-up project row | four equal rounded photo cards in one row under a heading and a ghost "all projects" pill; a swipe rail on phones.
- section | Featured project with spec list | text column with a short spec list (location · type · area) beside a ~65% wide rounded photo.
- cta | Closing panel with photo CTA | a rounded panel: headline + contact columns left, a small photo on the right with the primary pill laid over it.
- color | Warm near-black stack | three dark surfaces (#141413 / #1F1F1D / #282725) separated by 1px #3F3E3D rules, warm off-white ink and one thin gold accent for line work only.

## Don't copy
- The Aakriti name, monogram and renders; its copy ("Designing spaces. Elevating lives.").
- **Breaks our rules, adapt instead:** the hero stat tiles (25+ / 250+) and the "Since 2000" stat badge (hero stat tiles, L-015; numbers only if true); the row of six icon tiles for services (icon-tile row, L-015: use a ruled list or photo-led rows); tracked-caps labels over every section (eyebrow ratio, L-015); the testimonial carousel with a star rating (invent nothing for a real firm; carousels hide content); the giant translucent name is decorative text at ~1.3:1, so it must be `aria-hidden` and never carry information.
- Muted grey body text on #282725 tiles is near the 4.5:1 floor: check it on every raised surface.

## Fits
Architects, interior designers, design-build firms, high-end builders, luxury real estate, boutique hotels and resorts, furniture makers with a showroom; anything sold on dusk-lit photography and calm luxury.
