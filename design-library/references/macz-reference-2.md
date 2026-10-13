# Nordwood Timberworks 2: three timber details captioned like museum labels, then the maker at his bench
Kind: website homepage (middle slice, 2 of 4) · Subject: timber kit homes, pergolas and timber accents · Learned: 2026-10-12 · Image: `../inspiration/macz-reference-2.webp` · Original: not kept (dropped with the Macz brief as `reference 2.png`)

## What it is
The product-and-story middle of the same timber-kit homepage: a centred row of three architectural timber details (posts, brackets, shutters), then an editorial "our story" split with a craftsman in the workshop. The second of four slices the user gave as inspiration for **Macz Arkitektura** (MZ v1, the light "sunrise" design, took its captioned cards and story split from here; see `../sites/macz-arkitektura.md`). Mood: quiet, crafted, orderly, honest, airy.

## Layout anatomy
1. **Centred section head**: serif H2 ("Custom Timber Accents") centred, a two-line grey lede centred under it at ~60ch.
2. **Three captioned images**: three equal landscape photos (~4:3) in one row with a tight ~4px gap, square corners, filling the content width; a centred serif caption under each (Posts & Beams, Overhang Brackets, Shutters), no card chrome. One centred rectangular ghost button ("EXPLORE MORE") below.
3. **Story split**: a near-square workshop photo left (~45% of the width) and, vertically centred on the right, a tiny grey caps eyebrow ("OUR STORY"), a two-line serif H2, a grey paragraph and a ghost "READ MORE" button. Generous space (~100px) above and around.
Phone: the three images likely stack (or become a swipe rail) with captions under each; the story split stacks photo first.

## Palette
| Hex | Role | Notes |
|---|---|---|
| #E0E0E0 | page | flat neutral grey; the two sections differ by a barely visible tone |
| #2D2B29 | headings | warm charcoal, ≈10:1 on the page |
| #9C9C9C | body and lede | ≈2.1:1 on #E0E0E0, fails |
| #A0A0A0 | ghost button border and caps label | 1px outline |
| #76614C | photo timber | amber-brown wood in every photo ties the set together |

## Typography
- Display: the same soft transitional serif as slice 1, regular weight, title case, ~2.6× body for H2, 1.15 leading (close: Gilda Display 400, Cormorant Garamond 500).
- Captions: the serif at ~1.05× body, centred.
- Body: a light geometric sans, ~13px, grey, ~1.7 leading (close: Mulish 300, Jost 300).
- Buttons and eyebrow: the sans in small caps, 500, tracking ~.15em.

## Signature ideas
- Timber is the only colour on the page: every photo is chosen for one warm wood element against white or grey.
- Captions sit under the photos like museum labels, not inside cards.
- Square, near-touching images make the row read as one strip.
- One button style for every "more" link: a thin rectangular outline with tracked caps.
- The craftsman photo makes the story real (a person, the material, the workshop).

## Patterns to borrow
- card | Captioned image card | three equal 4:3 photos with a 4px gap and square corners, a centred serif caption under each, no border or background; the image and caption form one link; one centred ghost button under the row.
- cta | Rectangular ghost caps button | `border: 1px solid var(--outline); border-radius: 2px; padding: .8em 1.6em; font: 500 .72rem/1 sans; letter-spacing: .15em; text-transform: uppercase`; the filled variant uses the one dark action colour. Every "more" link uses it.
- section | Editorial story split | a ~45% near-square photo of the owner or the work in progress left, then H2, one paragraph and a ghost button vertically centred in the right column; stacks photo first.
- color | Material as the only colour | keep the UI neutral (grey/white surfaces, charcoal ink) and pick every photo for one warm material (wood, brass, terracotta) so the photos supply the palette.

## Don't copy
- The Nordwood name, renders and copy.
- **Breaks our rules, adapt instead:** the tracked-caps "OUR STORY" eyebrow (eyebrow over headings, L-015); grey body and lede text at ≈1.7–2.1:1 (darken to ≥4.5:1); "Explore more" and "Read more" ghost buttons are fine, but the primary CTA must stay one label sitewide.
- A stock "craftsman" photo on a real client's site: use the client's own people or skip it.

## Fits
Joiners, timber merchants, cabinetmakers, furniture and door/window makers, restoration carpenters, architects and builders who want to show details and process, any craft business with one hero material.
