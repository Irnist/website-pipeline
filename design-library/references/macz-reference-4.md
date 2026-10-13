# Nordwood Timberworks 4: four voices floating on a warm-lit bedroom, then a quiet grey sign-off
Kind: website homepage (closing slice, 4 of 4) · Subject: timber kit homes, pergolas and timber accents · Learned: 2026-10-12 · Image: `../inspiration/macz-reference-4.webp` · Original: not kept (dropped with the Macz brief as `reference 4.png`)

## What it is
The end of the same timber-kit homepage: a wide interior photo band with four translucent testimonial cards laid over it, a one-line newsletter strip and a light four-column footer. The last of four slices the user gave as inspiration for **Macz Arkitektura** (MZ v1 took the full-bleed photo band for its quote and closing bands but dropped the testimonial cards and newsletter; see `../sites/macz-arkitektura.md`). Mood: serene, warm, trustworthy, understated, soft.

## Layout anatomy
1. **Photo band with floating cards**: a wide bedroom photo (~2:1) inset by a small gutter, square corners, its warm cove-lit timber ceiling and floor-to-ceiling windows framing the centre. A 2×2 grid of light translucent cards sits in the middle ~60% of the band, each holding a short quote in small grey sans, then a round avatar, a serif name and a grey role. The photo shows at the sides and in the gaps between cards.
2. **Newsletter strip**: a slightly raised grey panel; left, a serif H3 ("Get Inspired") with a two-line grey sub; right, an underline-free email field and a dark espresso "SUBSCRIBE" button in tracked caps.
3. **Footer**: four columns on the page grey: the brand name set in serif on two lines with a small grey blurb; "Support" and "Corporate" with tracked-caps labels and tracked-caps grey links; "Location" with the address and four small square-rounded social icons.
Phone: the cards likely stack into one column over a taller crop (or the photo becomes a header above them), the strip stacks heading over field and button, the footer goes to two columns then one.

## Palette
| Hex | Role | Notes |
|---|---|---|
| #E0E0E0 | page and footer | flat neutral grey |
| #DEDEDE | newsletter panel | barely raised from the page |
| #E3E2E1 (≈ .88 alpha) | floating cards | light frosted panels over the photo |
| #45392F | the one filled button | espresso brown, white caps text (sampled #50453B with text) |
| #2D2B29 | headings, names | warm charcoal |
| #7D7D7B | footer labels | ≈3:1 on the page, too low for small text |
| #A9A9A9 | footer links, quote text | ≈1.8:1, fails |
| #6F6456 | photo timber and floor | the warm colour comes from the photo |

## Typography
- Display: the soft transitional serif for "Get Inspired", the footer brand and reviewer names (close: Gilda Display 400, Cormorant Garamond 500).
- Body and quotes: a light geometric sans, ~11–12px, grey, ~1.6 leading (close: Mulish 300, Jost 300).
- Labels, links and button: the sans in caps, 500, tracking ~.15em, ~10–11px.

## Signature ideas
- Cards float over a real room, so the reassurance happens "inside" the kind of space the buyer wants.
- Warm cove lighting and timber in the band photo answer the timber hero at the top of the page.
- One dark espresso fill in the whole page: the only solid button.
- A light footer on the same grey as the page, so the page ends quietly instead of on a dark slab.

## Patterns to borrow
- section | Cards floating on a photo band | a wide interior photo (`aspect-ratio: 2 / 1`, `object-fit: cover`) with a centred 2×2 grid (`width: min(60%, 44rem)`) of panels `background: rgb(236 234 230 / .9); backdrop-filter: blur(6px)`, each holding one true quote, fact or FAQ; on phones the photo becomes a header crop and the cards stack below on a solid surface.
- form | One-line request strip | a slightly raised panel: serif H3 and one-line sub left; one field and one dark filled button right, aligned on one row from 700px; for a callback or quote request where a newsletter has no backend.
- footer | Light four-column footer with serif brand | the footer on the page colour: brand name in the display serif over a short blurb, two link columns with tracked-caps labels, a location column with address and small square social icons; 2 columns at tablet, 1 on phones.
- color | Neutral grey with one espresso action colour | flat `#E0E0E0`-ish page and panels, warm charcoal ink, and one dark brown (`#45392F`-ish) used only for the filled button; all warmth comes from timber in the photos.

## Don't copy
- The Nordwood name, renders, copy and the four named testimonials (stock faces and invented quotes).
- **Breaks our rules, adapt instead:** testimonial cards for a real business (invent nothing; use only real, attributable quotes, or turn the cards into true facts/FAQs); a newsletter that "succeeds" without a backend, and ending the homepage on a newsletter (give it a closing CTA beat instead); `href="#"` legal and social links; grey quote, label and link text at ≈1.8–3:1 (darken to ≥4.5:1, including on the translucent cards over the photo).
- Translucent cards over a busy photo: check contrast on the lightest part of the photo behind each card at 390 and 1440.

## Fits
Builders, joiners, architects and interior designers, boutique hotels and rentals, furniture and bedding makers, any business with one strong interior photo and a handful of real client quotes or facts.
