# Dala: constellation floating on black velvet
Kind: design system (DESIGN.md) · Subject: AI knowledge assistant (SaaS) · Learned: 2026-10-12 · Source: `../inspiration/design-md/dala.md`

## What it is
A dark-stage SaaS system: a pure black void, one vivid violet action colour and amber sparks, with monolithic weight-400 headlines at outsized scale and ultra-light body copy. The hero art is a procedural constellation of tiny multicoloured outlined triangles forming an organic shape. Mood: nocturnal, weightless, spacious, sculptural, quiet-confident.

## Layout anatomy
1. Nav: transparent bar on black; logo left, 14px uppercase 600 links (0.025em) in `#9a9a9a` (white when active), one filled violet pill at the far right. No border, no blur.
2. Hero: two-column asymmetric split; left = 78–113px headline, amber uppercase label, 18px/200 body (max ~480px), violet pill; right = the animated particle constellation at massive scale.
3. Following sections: two-column text + visual blocks that zigzag (visual-left/text-right, then the reverse), 60–120px section gaps, max width 1280px. No card grids, no pricing tables, no multi-column feature rows.
4. Team: borderless cards; 24px-radius portrait, 12px uppercase violet role, 27px white name, small grey social glyphs; carousel with ~8px violet dots.
Density: one or two elements per viewport. Phone: the zigzag collapses to a single column, visual after the text; display type scales down.

## Palette
| Hex | Role | Notes |
|---|---|---|
| `#000000` | Void canvas | Every section; no grey panels |
| `#ffffff` | Ink | Headlines, body, icons |
| `#9a9a9a` | Muted ink | Inactive nav, ghost links (7.4:1 on black) |
| `#bdbdbd` | Tertiary ink | Captions, supporting body |
| `#8052ff` | Action fill | The only filled-button colour; white on it is 4.6:1 |
| `#ffb829` | Spark accent | Labels, emphasis, links (12.1:1 on black) |
| `#15846e` | Deep verdant | Logo gradient stop, rare tint |

## Typography
- One family: PP Neue Montreal (commercial). Self-hostable alternatives: **Inter** (named substitute) or **Manrope** / **Hanken Grotesk**; keep `"ss01"` where the face has it.
- Display: weight 400, 113px / 78px / 48px / 42px, line-height 1.1, tracking -0.04em (-4.52px at 113, -3.12px at 78, -1.68px at 42–48).
- Body: 18px weight **200**, line-height 1.5. Small text 15px weight 400.
- Labels and nav: 14px weight 600 uppercase, 0.025em (0.35px). Caption 12px / 1.5.
- Hierarchy by scale, never by weight; headlines are never bold.

## Signature ideas
- Pure black as the material, not a fallback: no cards, borders, shadows or panels.
- Same weight (400) from 15px body to 113px display; scale alone carries hierarchy.
- Ultra-light 200 body copy that feels airy.
- One violet pill per view; everything else is a ghost text link.
- A procedural particle field (outlined triangles, many hues) as the only hero art, with sparse ambient particles across the page.

## Patterns to borrow
hero | particle-field hero | canvas or SVG field of small outlined shapes in 5–6 saturated hues forming one organic silhouette on the right half; sparse drifting particles elsewhere; animated in JS, static under reduced motion
section | zigzag text + visual | two-column 1fr/1fr blocks that alternate sides down the page, 60–120px gaps, no containers
typography | scale-not-weight display | one sans at 400 for everything from body to 113px, -0.04em tracking at 42px+, 1.1 leading
typography | ultra-light body | 18px weight 200 body at 1.5 on black (check contrast and rendering on Windows)
color | void + one action colour + spark | pure black canvas, white ink, one saturated fill used only for the primary pill, a warm second accent for labels and emphasis
cta | single violet pill | 14px uppercase 600 pill, ~45px tall, 24px radius, the only filled control per view; secondary = bare text link
card | borderless team card | 24px-radius portrait, small uppercase coloured role, large regular-weight name, nothing else
nav | transparent caps nav | 14px uppercase 600 links in muted grey, white when current, pill CTA anchoring the right
motion | ambient particle drift | low-density shapes drifting slowly in a canvas behind content (rAF, paused off-screen, off under reduced motion)

## Don't copy
- Dala's palette as a whole (violet #8052ff + amber + verdant) and PP Neue Montreal: our palette comes from the client's logo; the structure is what's lent.
- The brain-shaped constellation (Dala's mark of "collective knowledge"): redraw the particle idea around the client's own object.
- Line-heights 0.81 / 0.90 / 1.00 listed in the source: our floor is 1.05 for headlines.
- "Weight 200 body" can render thin on Windows and low-DPI screens; keep contrast high (white on black) and test it, or use 300.
- Any CSS transition/animation the original uses: port motion to `morph()` / `motion.js`.
- No glows: the particles must stay outlined strokes, no bloom or blur halos.

## Fits
Music, audio and nightlife; tech and creative studios; anything sold at night or on a stage; premium product brands that want a calm, spacious dark look.
