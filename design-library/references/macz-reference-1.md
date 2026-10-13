# Nordwood Timberworks 1: a hearth-lit living room framed like a print, the headline written on the wall
Kind: website homepage (top slice, 1 of 4) · Subject: timber kit homes, pergolas and timber accents · Learned: 2026-10-12 · Image: `../inspiration/macz-reference-1.webp` · Original: not kept (dropped with the Macz brief as `reference 1.png`)

## What it is
The top of a homepage for a timber-kit maker, selling warm, natural-material living through one calm interior render with a lit fire as its centre. It is the first of four slices of the same page that the user gave as the inspiration for **Macz Arkitektura** (the first, light "sunrise" design, MZ v1; the October dark redesign followed `architect-reference` instead; see `../sites/macz-arkitektura.md`). Mood: calm, warm, natural, soft, gallery-like.

## Layout anatomy
1. **Header inside the hero frame**: small tracked-caps links left (Kits, Products, Collections, Custom), a stacked two-line wordmark with a small plank mark dead centre, search and cart icons right, all in white over the photo; no bar or backdrop.
2. **Framed hero**: a full-width photo card inset ~20px from the page edge with a ~10px radius, ~50% of the slice. A two-line centred serif headline ("Crafting Timeless Homes / with Nature's Touch") sits in the upper third over the plain wall above the fireplace, so the room's focal point (the fire) lands just under it. The bottom of the photo dissolves into the grey page instead of ending on a hard edge.
3. **Stat row**: four centred columns on the page grey, serif numerals (10+, 100+, 20+, 50M) at ~2× body over tiny grey labels; no dividers.
4. **Category tiles**: four tall portrait photo tiles (~3:4.6) in one row with ~4px gaps, square corners, edge to edge within the gutter. Each is a link with a dark translucent bar along the bottom holding a serif label left and a ↗ arrow right (Pergola Kits, Pavillion Kits, Homes, Browse all).
Phone: the hero likely becomes a taller crop with the headline over the wall, the stats a 2×2 grid, the category tiles a 2×2 grid or a swipe rail.

## Palette
| Hex | Role | Notes |
|---|---|---|
| #E0E0E0 | page | flat neutral light grey, no paper warmth |
| #F3EFE8 | headline on photo | warm off-white over a pale wall: weak contrast |
| #4A4643 | stat numerals | warm charcoal |
| #9A9A9A | small labels | ≈2.1:1 on the page, fails |
| #544C46 (≈ .8 alpha) | caption bars | dark warm brown-grey over the photo; white text on it |
| #8E755C / #564635 | photo warmth | timber and fire tones, not UI colours |

## Typography
- Display: a light-to-regular transitional serif with soft bracketed serifs, title case, two centred lines at ~4× body, comfortable ~1.15 leading (close: Gilda Display 400, Cormorant Garamond 500; MZ v1 chose Marcellus).
- Numerals: the same serif, regular, ~2× body.
- Body and labels: a light geometric sans at small sizes in grey (close: Mulish 300, Jost 300).
- Nav: the sans in tiny caps, 500, tracking ~.15em.
- Tile captions: the serif at ~1.1× body in white.

## Signature ideas
- The headline is placed on the empty wall of the photo, so the room composes around the words.
- The hero photo fades into the page at its foot rather than stopping, which softens the frame.
- One focal warm light (the fire, the lamp) inside an otherwise grey, neutral page: the photos carry all the colour.
- Category tiles as tall portrait photos with a slim dark caption bar instead of cards.
- Header and wordmark live inside the photo frame, centred, no bar.

## Patterns to borrow
- hero | Framed hero with header inside | the hero is a ~10–12px-radius photo card inset by the page gutter; caps links left, the centred wordmark, and icon buttons right sit in white inside its top edge with only a top scrim.
- hero | Photo dissolving into the page | the hero image gets `mask-image: linear-gradient(#000 70%, transparent)` (or a bottom `::after` gradient to `var(--page)`) so its last ~25% fades into the page colour; the next section starts on that colour with no rule.
- hero | Headline on the empty wall | choose or crop the hero so a plain area (wall, sky) sits in the upper third; set a centred two-line serif H1 there and keep the focal object just below it; add a soft radial or top scrim if the area is pale.
- gallery | Tall captioned category tiles | four portrait (~3:4.5) photos in one row, 4–6px gaps, square corners; each whole tile is a link with a bottom bar `rgb(40 32 26 / .78)`, serif label left, ↗ right, `min-height: 3rem`; 2×2 on phones.
- nav | Split caps nav with centred wordmark | grid `1fr auto 1fr`: tiny tracked caps links left, the stacked wordmark centred, icon buttons right-aligned; collapses to wordmark + menu + call on phones.

## Don't copy
- The Nordwood name, plank mark, the renders (they read as AI-generated) and the copy.
- **Breaks our rules, adapt instead:** the four-up stat row under the hero (hero stat tiles, L-015; numbers only if true, and "50M total sales" is the kind of ambiguous figure the claims rule warns about); the grey labels at ≈2.1:1 and an off-white headline over a pale wall (contrast: add a scrim, darken muted text to ≥4.5:1); a cart icon on a business that doesn't sell online (dead-end feature).
- "Pavillion" is misspelled in the source; never carry copy across.

## Fits
Timber and joinery shops, kit homes and outdoor structures, cabinetmakers, furniture makers, fireplaces and stoves, interior designers, small builders and architects with calm, natural-material work.
