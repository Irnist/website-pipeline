# Nordwood Timberworks 3: a staggered timber collage under a split heading
Kind: website homepage (lower slice, 3 of 4) · Subject: timber kit homes, pergolas and timber accents · Learned: 2026-10-12 · Image: `../inspiration/macz-reference-3.webp` · Original: not kept (dropped with the Macz brief as `reference 3.png`)

## What it is
The collections section of the same timber-kit homepage: a split section head over a six-photo collage whose columns break at different heights, then a centred ghost button and a "Trusted by" partner-logo row. The third of four slices the user gave as inspiration for **Macz Arkitektura** (MZ v1 took the split section head; its collage idea was rebuilt as a per-project mosaic on the Project Gallery; see `../sites/macz-arkitektura.md`). Mood: abundant, warm, crafted, editorial, calm.

## Layout anatomy
1. **Split section head**: a two-line serif H2 on the left (~45%), a three-line small grey lede on the right (~35%), the two aligned at the top; wide gap between.
2. **Staggered collage**: three equal columns, ~4px gaps, square corners, six photos. The outer columns split ~43 / 57 (a shorter photo over a taller one); the middle column splits the other way (~57 / 43), so the horizontal seams never line up and the grid reads as a collage, not a table. All columns end on one baseline.
3. **Centred ghost button**: "EXPLORE COLLECTIONS", rectangular outline, tracked caps.
4. **Trusted by**: a centred serif line ("Trusted by Leading Architects & Builders") over a row of six greyed partner logos.
Phone: the collage likely becomes two columns (keeping the stagger) or one column; the split head stacks H2 over lede.

## Palette
| Hex | Role | Notes |
|---|---|---|
| #E0E0E0 | page | flat neutral grey |
| #2D2B29 | headings | warm charcoal |
| #9C9C9C | lede | ≈2.1:1, fails |
| #717171 | greyed logos | monochrome logo row |
| #594635 / #8E846F | photo timber and stone | the only warm colour on the page |

## Typography
- Display: the soft transitional serif, regular, title case, ~3× body, two lines at ~1.15 (close: Gilda Display 400, Cormorant Garamond 500).
- Lede: the light geometric sans, ~12–13px, grey, 1.7 leading (close: Mulish 300, Jost 300).
- Button: the sans in small caps, tracking ~.15em.
- Trust line: the serif at ~1.4× body, centred.

## Signature ideas
- The stagger: one column breaks the other way, so six equal-width photos feel hand-arranged.
- Every photo shows one timber element (porch, posts, ceiling, shutters, pergola) against white render or snow: a consistent art direction makes the collage cohere.
- The heading and lede split across the width, giving the collage a calm editorial lead-in.

## Patterns to borrow
- section | Split section head | H2 (two lines) in the left ~45%, a short muted lede in the right ~35%, top-aligned with a wide gap; stacks H2 over lede on phones.
- gallery | Staggered three-column collage | `grid-template-columns: repeat(3, 1fr)`, each column its own grid: outer columns `grid-template-rows: 43fr 57fr`, the middle column `57fr 43fr`, a fixed total height (~`clamp(32rem, 62vw, 46rem)`), 4px gaps, square corners, `object-fit: cover`; two columns with the stagger kept on tablets, one column on phones.
- cta | Rectangular ghost caps button | the same thin outline caps button, centred under the collage as the single way into the full gallery.

## Don't copy
- The Nordwood name, logo, renders and copy.
- **Breaks our rules, adapt instead:** the "Trusted by" row of third-party logos (brand logos read as endorsements, and a logo wall is a category template tell; use a text-only list with permission, IW's `.brands`, or skip it); grey lede text at ≈2.1:1; a collage of near-duplicate shots (two porch views from one shoot count as a repeat).
- Collage photos without captions are fine for a mood board but a real portfolio should say which project each one is (MZ added title blocks).

## Fits
Architects and builders, joinery and timber, landscaping and outdoor structures, interior designers, kitchen and cabinet makers, wedding and event venues, any business with a large set of varied project photos.
