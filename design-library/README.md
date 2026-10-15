# Design library

Every site we've built, recorded so a new site can reach the same quality without an inspiration image. It's read at the start of the Direction step (SKILL.md › 2.0), and every finished site is added at handoff.

- `patterns.md`: the cross-site catalogue of heroes, sections, galleries, cards, CTAs, nav, footers, forms, type, colour, motion and details. Each pattern names the site it came from and points to its code. It also gives the recipe for designing without a reference, and lists what to avoid.
- `sites/<slug>.md`: one entry per site, covering identity, palette, type, the homepage section by section, signature elements, motion, reusable components, how it went, and reuse guidance.
- `shots/`: each homepage's top strip (960 wide) and phone fold (360 wide). Look at them with Read before borrowing anything.
- `inspiration/`: the reference images the user supplied with each brief. They show the user's taste: what they reached for when they did have a reference. `inspiration/design-md/` holds the design-system files (DESIGN.md) they supplied the same way.

**How to use it.** Find the one or two entries closest to the new business (by trade or mood, not by name), read `patterns.md`, then build this business's own concept and borrow *patterns*, never a whole site. Two past sites in the same trade must still look unrelated: IronCity and Trevor Travis both sell vehicles, and one is a night garage while the other is a parts book. The published client sites are real businesses: borrow layout ideas only, never their copy, names, photos or claims.

## Index

| Site | Trade | Concept (one line) | Mood | Build | Entry |
|---|---|---|---|---|---|
| Ernest Banigon portfolio | Web designer (own) | Charcoal and amber, with the work shown in live browser frames that scroll | warm dark, editorial, personal | pipeline + GSAP | `sites/portfolio-ernest-banigon.md` |
| Gadget Zone | Electronics retail | Dark neon tech store built around the owner's repair bench (circuit traces, charge meters, "Bench-checked" stamps) | electric, playful, trustworthy | pipeline + GSAP | `sites/gadget-zone.md` |
| Macz Arkitektura | Architecture firm | The firm's name carved across a dusk sky, inside one dark framed card; every project captioned like a drawing title block (2026-10 redesign of the light "sunrise" site) | dark, warm, luxurious, exact | pipeline + GSAP | `sites/macz-arkitektura.md` |
| Trevor Travis Motors | Motorcycle dealer + parts | The shop's own parts book: ink FIG. plates with numbered callouts, dot-leader prices, orange closing field | industrial, honest, catalogue | pipeline | `sites/trevor-travis-motors.md` |
| Ironwood Heating & Air | HVAC / aircon | Hot and cold: navy and orange cut by a skewed two-tone stripe | bold, local, reliable | hand-built (pre-pipeline) | `sites/ironwood-hvac.md` |
| IronCity Rods & Customs | Hot-rod / custom cars | Night-garage showroom in black, charcoal and signal red with condensed caps | dark, loud, mechanical | hand-built (pre-pipeline) | `sites/ironcity-rods.md` |
| Weknz Patio Furniture | Furniture showroom | Family showroom on a sunny lawn: cream paper, walnut ink, friendly serif, visit-first | warm, homely, daylight | hand-built (pre-pipeline) | `sites/weknz-patio.md` |
| Aurora Plumbing · Children Matter TX · Macon Supply · Parker Auto AZ | Plumbing · nonprofit · trade supply · auto repair | Real published client sites (layout ideas only) | varied | live, third-party | `sites/published-client-sites.md` |

**Quality ranking (as a bar to aim at).** The pipeline sites (portfolio, Gadget Zone, Macz, Trevor Travis) are the strongest. Each was built from the business's own story, QA'd to 0 errors and scored Lighthouse mobile 90+. The three hand-built sites predate most rules in LESSONS.md, so their entries record what they got wrong as well as what's worth keeping (IronCity reads as a category template; Weknz kept template leftovers). Older sites also used CSS motion and headline line-heights below 1, which today's rules forbid: port those ideas to `morph()` / `motion.js` and 1.05+ leading before reusing them.

## Dropped references

Drop any design image (a website screenshot, mockup, landing page, app screen or poster) into `inspiration/`, with any name and format (PNG, JPG, WebP, GIF, BMP). It's learned the next time you run `/website learn`, or automatically at the start of the next site build. Learning writes `references/<slug>.md`, adds its patterns to `patterns.md`, files the image in `inspiration/` (the original in `inspiration/originals/`) and logs it in `learned.log`. The procedure is `LEARN.md`.

A design-system file works the same way: drop a DESIGN.md from Refero Styles (styles.refero.design) or a similar library into `inspiration/`, under any `.md` name (renaming it after the brand, e.g. `linear.md`, is clearest). It's filed in `inspiration/design-md/`, which leaves the drop folder empty for the next download, and a name that's already taken gets `-2`, so no file is ever overwritten. A file still called `DESIGN.md` is named from its own title. Its entry lends a site structure (type scale, spacing, components, motion feel); the palette still comes from the client's logo.

| Reference | Kind | Concept | Mood | Entry |
|---|---|---|---|---|
| Aakriti Architects | website homepage | A dusk-lit studio in one dark framed card, the firm's name carved across the sky | dark, warm, luxurious, calm | references/architect-reference.md |
| Dala | design system (DESIGN.md) | A constellation floating on black velvet: pure black, one violet pill, weight-400 display, ultra-light body | nocturnal, weightless, spacious | references/dala.md |
| Nordwood Timberworks 1 | website homepage (slice 1/4) | A hearth-lit living room framed like a print, the headline written on the wall | calm, warm, natural, soft | references/macz-reference-1.md |
| Nordwood Timberworks 2 | website homepage (slice 2/4) | Three timber details captioned like museum labels, then the maker at his bench | quiet, crafted, orderly, airy | references/macz-reference-2.md |
| Nordwood Timberworks 3 | website homepage (slice 3/4) | A staggered timber collage under a split heading | abundant, warm, editorial, calm | references/macz-reference-3.md |
| Nordwood Timberworks 4 | website homepage (slice 4/4) | Four voices floating on a warm-lit bedroom, then a quiet grey sign-off | serene, warm, understated, soft | references/macz-reference-4.md |

## Entry format (for new entries at handoff)

```
# <Site name>: <one-line design concept>
<Trade> · <sample|client|own> · <month year> · <pages> · <pipeline build | hand-built> · Source: `<workspace-relative path>`
Screens: `../shots/<slug>.webp`, `../shots/<slug>-phone.webp` · Inspiration: `../inspiration/<file>` (or none) · Full page: `Portfolio Screenshots/<file>`

## Identity              story, 3–5 mood words, what stops it looking like a template
## From the inspiration image   (if any) what was taken, what was changed
## Palette               | Token | Hex | Role | Contrast notes |
## Typography            faces, weights, clamp() sizes, line-heights, tracking, numerals
## Homepage anatomy      numbered sections: layout, content, the detail that makes it work, phone behaviour
## Other page patterns
## Signature elements    3–6, each with a file › selector pointer
## Motion
## Reusable components   header, buttons, cards, forms, footer: one line + pointer each
## How it went           critique scores, Lighthouse, what the user praised or corrected, L-### lessons
## Reuse guidance        Fits: … · Keep to this site: …
```

Then add a row to the index above, put the screenshots in `shots/`, and add the site's new patterns to `patterns.md`.
