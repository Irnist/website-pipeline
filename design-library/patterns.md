# Pattern catalogue

Reusable ideas from every site in the library, grouped by what they are. Each line gives the pattern, what it does, where it came from and where its code is. Paths are relative to each site's source folder (see the site's entry); `styles.css` means `assets/css/styles.css`.

Sites: **PF** portfolio · **GZ** Gadget Zone · **MZ** Macz Arkitektura v1, the light "sunrise" design (archived in `_temp/Macz Arkitektura-previous-2026-10-10/`; the live Macz is the 2026-10 dark redesign, `sites/macz-arkitektura.md`, which built every "ref: architect-reference" pattern below: shell, name in the sky, pill with disc, rails, four-up row, glass badge, closing panel) · **MS** a music-shop sample, archived (built every "ref: dala" pattern below) · **TT** Trevor Travis Motors · **IW** Ironwood HVAC · **IC** IronCity Rods · **WK** Weknz Patio · **live:** a published client site (layout idea only).

## Designing without a reference

This is the recipe behind the strongest sites (PF, GZ, MZ, TT). Their best ideas all came from the business itself, not from the category:

1. **Find the trade's own object** and make it the visual language: GZ's repair bench (circuit traces, charge meters, "Bench-checked" stamps), TT's parts book (FIG. plates, numbered callouts, dot leaders), MZ's drawing set (title-block captions), PF's browser (work shown in live, scrolling frames), MS's metronome (the logo, the count-in steps, the 404), IW's flame and snowflake (a hot/cold stripe). Write it as one sentence: "<business> as <its own object>."
2. **Take one signature device from that object** and use it in 3–5 places, no more: a caption style, a divider, a numbering system, a frame. It is what passes the competitor test.
3. **Palette from the logo,** then assign roles: page, raised surface, ink, muted ink, one action colour. A fill colour and a text colour for the accent are different tokens (IC `--red` / `--red-ink`). Make every band redefine its own `--fg` / `--muted` / `--btn-*` so one button works on every surface (TT surface role tokens).
4. **Type by role:** a display face with character from the trade (condensed caps for industrial, a serif for craft and architecture, a friendly serif for a family shop), a calm body face, and numerals set in tabular figures. Check the display face's 0 and 1 (MZ sets numerals in Jost).
5. **Homepage rhythm of about 8 beats:** hero (promise plus primary CTA) → proof that's specific to this business → offer (services, products or work) → how it works → story or people → buyer answers (price, timing, area) → visit or contact → closing CTA band. Alternate surfaces (light, raised, dark, photo) so each beat reads as its own band.
6. **Motion: 1–3 moments that tell the story** (PF rules drawn in sequence, GZ's pinned bench steps, TT's highlighter swipe). Everything else is still.

## Heroes

- **Name across the sky** (ref: architect-reference): the business name in caps at ~18–22vw and ~16% white, behind the photo's building (cut-out layer on top, or over the sky only), `aria-hidden`; the real H1 stays small, bottom-left. `references/architect-reference.md`.
- **Annotated product plate** (TT): ink hero; caps headline and CTA pair on the left, a framed photo with numbered callout discs on the right, keyed to a "what we checked" list. `styles.css` › `.hero__grid`, `.pin`, `.key`.
- **Cut-out in a lit arch** (PF): transparent portrait on a slightly lighter rounded-top arch; the head rises past the arch so dark clothing keeps its outline. Stacks above the text on phones. `.hero__photo::before`.
- **Neon portal** (GZ): circular photo frame inside a gradient SVG ring with a dashed orbit and an elliptical pedestal, strokes only, no glow. `.portal`, `.portal__ring`, `.portal__base`.
- **Photo hero with wave hand-off** (MZ): full-bleed 50% parallax photo, header scrim plus bottom scrim, a low centred serif H1, and an SVG wave in the page colour that closes it. `.hero`, `.hero__wave`.
- **Skew-stripe hero** (IW): navy scrim fading to clear at 72% over a technician photo, cut by a −12° orange stripe with a sky-blue offset line. On phones it becomes an orange bottom rule. `.hero::after`.
- **Framed full-bleed hero** (IC): photo inset 12px with a 28px radius, copy aligned to the bottom, left and bottom scrims; the header floats in the same inset. `.frame`, `.hero`. Also ref: architect-reference (`references/architect-reference.md`), ref: macz-reference-1 (~10px radius, caps links / centred wordmark / icons inside the frame; `references/macz-reference-1.md`).
- **Photo dissolving into the page** (ref: macz-reference-1): the hero image gets `mask-image: linear-gradient(#000 70%, transparent)` (or a bottom gradient to `var(--page)`), so its last quarter fades into the page colour and the next section starts with no rule. `references/macz-reference-1.md`.
- **Headline on the empty wall** (ref: macz-reference-1): crop the hero so a plain area (wall, sky) fills the upper third, set a centred two-line serif H1 there, and keep the focal object (a lit fire) just below it; add a soft scrim if the area is pale. `references/macz-reference-1.md`.
- **Whole site in a shell over a glowing backdrop** (Macz redesign; ref: architect-reference): one rounded near-black card holds every panel, with up to 72px gutters (`min(100% - 2 * clamp(0px, 4vw, 72px), 90rem)`). Behind it is a fixed `body::before` night-city photo, pre-blurred to 720px and duotoned in the brand's warm hue. A B&W backdrop reads as grey fog. Keep `body` transparent (L-060); edge to edge under 600px. `sites/macz-arkitektura.md` › Signature elements.
- **Graded stock exterior + phone art direction** (Macz redesign): an overcast house photo graded to dusk (dilated sky mask, gradient sky, warm windows) so the name sits in a dark sky. `<picture>` gives phones a portrait crop when the landscape file would show under a third of its width.
- **Split real-photo hero with live status** (WK): the business's own lot photo with an honest caption, plus an open/closed pill; the CTA is "visit". `.hero__photo`, `.hero__status`.
- **Owned-landmark hero** (live: Aurora, Parker): the business's own sign or building instead of stock. A **customer-quote headline** (Aurora) beats a generic promise.
- **Overlapping coverage card** (live: Macon): a white card rises into the bottom of the hero, and its heading is the list of regions served.
- **Particle-field hero** (ref: dala): a JS canvas/SVG field of small outlined shapes in 5–6 saturated hues forming one organic silhouette on the right half, sparse drifting particles elsewhere; static under reduced motion. `references/dala.md`.
- **Beat-keyed particle cone** (MS, built from ref: dala): the field redrawn as the trade's own object, a speaker cone of ~1,400 outlined triangles (700 on phones) on 13 quantized rings that pulse to the business's rhythm (120 BPM; a ripple runs outward each beat, full strength on the downbeat) and part around the pointer. The canvas is 118% wide with a −12% margin so it bleeds off the right edge; GSAP sinks it (yPercent 14, scale .9, opacity .35) as the hero leaves. Draw one path per colour and alpha tier (14 strokes a frame, not 1,400). Both reviewers read seven hues plus loose particles as confetti: use 2–3 hues and sharper rings so the object reads. `assets/js/field.js`, `.hero__field`.
- **Inner page head** (MZ): the hero recipe aligned left, a per-page `--band-scrim`, and a `--busy` variant for noisy photos; near-solid on phones. `.page-head`.

## Sections

- **Zigzag text + visual** (ref: dala): two-column 1fr/1fr blocks that alternate sides down the page, 60–120px gaps, no cards, borders or panels. `references/dala.md`.
- **Zigzag category page with a price guide** (MS): a text-only page head with a caps jump row of anchors, then one zigzag per category (24px-radius photo, 4:3 turning square from 900px), each body ending in a dot-leader "from ₱" list generated from one price dict; the last block swaps prices for service rates or a check list. Five or six identical zigzags in a row feel repetitive (critique P2): vary one block's layout. `instruments.html`, `.zig`, `site_config.py` › `h_prices`.
- **Count-in steps** (MS): a 4-step process told as a musical count: a large metronome SVG beside four huge numerals (1–4) with an h3 and one line each; the current count lights amber while the needle swings. Built from the logo, so the process device is the brand's own object. `.countin`, `.counts`, `site_config.py` › `h_metronome`.
- **Two-column buyer Q&A** (MS): six pre-contact questions (price, stock, delivery, warranty, payment, trade-in) as a `<dl>`, large regular-weight questions and short answers, 2 columns from 760px (never 3), no accordion, prices pulled from the same dict as the price lists. `.answers`.
- **Heading-left rail** (ref: architect-reference): each section a 1:3 grid, heading and one link left, content right, 1px rules between sections. `references/architect-reference.md`.
- **Featured project with spec list** (ref: architect-reference): a text column with a short location · type · area list beside a ~65% wide rounded photo. `references/architect-reference.md`.
- **Ruled steps** (TT, MZ, PF): 3–4 columns with a top rule and a huge counter numeral (condensed or serif, in tabular figures). PF draws each rule in sequence; MZ sets it on a night band. TT `.steps`, MZ `.steps`, PF `.steps` + `li::after`.
- **Charge-meter steps** (GZ): tiles with a gradient top bar that fills; on phones they become a vertical rail with nodes. `.step::before`, `.steps::before`.
- **Story split with ruled values** (MZ, ref: macz-reference-2): a 4:5 real photo beside an H2 and hairline 01–03 rows. Use it instead of icon tiles. `.split`, `.values`. The reference's version: a ~45% near-square photo of the maker at work, with H2, one paragraph and a ghost button vertically centred beside it; `references/macz-reference-2.md`.
- **Spec-sheet list** (WK): serif term plus explanation rows under a 2px rule, in place of icon-tile rows. `.spec`, `.themes`.
- **Dot-leader price list** (TT, MS): item, dotted leader (min 2.5rem), nowrap tabular price. Works for menus, rates and inventory previews. MS generates every list and every "from ₱" figure in the copy from one `PRICES` dict, so no number can drift between pages. `.leaders`.
- **Ruled service rows** (MZ, IW): `.8fr / 1.2fr` title and body rows with anchor ids for deep links; IW flips the sides and adds "From ₱" and what's-included chips. MZ `.service-list`, IW `.service-row`.
- **Split section head** (MZ, ref: macz-reference-3): H2 on the left, muted lede on the right, aligned to the bottom. `.section-head--split`. The reference top-aligns a two-line H2 in the left ~45% and the lede in the right ~35%; `references/macz-reference-3.md`.
- **Cards floating on a photo band** (ref: macz-reference-4): a wide interior photo (`aspect-ratio: 2 / 1`) with a centred 2×2 grid (`width: min(60%, 44rem)`) of `rgb(236 234 230 / .9)` panels with a light backdrop blur, each holding one true quote, fact or FAQ; on phones the photo becomes a header crop and the cards stack on a solid surface. `references/macz-reference-4.md`.
- **Stacking terms table** (TT): a money table that becomes per-row blocks with `data-label` captions below 700px. No sideways scroll. `.terms`.
- **Timeline and roster** (TT): a condensed-year timeline, and staff as a ruled roster instead of people cards. `.timeline`, `.roster`.
- **Giant founding year** (WK): "1980" at `clamp(5rem, 13vw, 10rem)` anchors the story. `.story__year`.
- **Plan your visit** (WK): directions, a numbered "what to bring" list, and an hours table with today's row highlighted. `.visit`, `.bring`, `.hours`.
- **Area list and map card** (IW): a two-column list of places with pins beside a map with an address card overlay. `.areas`, `.map__card`. Variants: a darkened map with a light chip (IC `.map`), and a greyscale map before the footer (live: Parker).
- **"Things we won't do"** (GZ): three anti-promise cards, which build trust without fake stats. `about.html` › `.wont__list`.
- **Review themes until real quotes exist** (WK): a score numeral plus summarised themes; the quote grid stays hidden until real reviews arrive. `reviews.html` › `.rating`, `.themes`.
- **Text-only brands strip** (IW): brand names in type with an "independent provider" disclaimer, never logos. `.brands`.
- **Makes we service** (live: Parker): a strip that answers "do you work on mine?".
- **Partner split** (live: Macon): a big partner mark on white beside a dark textured statement panel.

## Galleries

- **Four-up project row** (ref: architect-reference): four equal rounded photo cards under a heading and a ghost "all projects" pill; a swipe rail on phones. `references/architect-reference.md`.
- **Scrolling browser frames** (PF): a 16:10 screen whose full-page capture scrolls on hover or tap (GSAP 7s down, 0.9s back). For any work that is a page. `.browser__screen`, `motion.js`.
- **Project mosaic** (MZ): 3 columns with a wide 2×2 lead item, stacking to 1. `.mosaic .is-wide`.
- **Single portrait beside a title block** (MZ): alternates sides, so there are no lone image rows. `.project--single`, `.project--flip`.
- **Shop-floor bento** (IC): 4 columns with a 2×2 lead tile, a tag and title over a scrim. `.bento`, `.shot`.
- **Category mosaic with a text tile** (WK): a spanning grid that fills every row at every breakpoint, with one text tile in the brand colour. `.mosaic`, `.tile--text`.
- **Poster rail to grid** (PF): a scroll-snap rail that bleeds to the screen edges on phones, 3 columns at 900px and up, and a native `<dialog>` lightbox. `.poster-grid`, `.lightbox`.
- **Real-shop photo strip** (live: Parker): exterior, waiting room, staff and front desk in one row.
- **Tall captioned category tiles** (ref: macz-reference-1): four portrait (~3:4.5) photos in one row, 4–6px gaps, square corners; each whole tile is a link with a bottom bar `rgb(40 32 26 / .78)`, a serif label left and ↗ right; 2×2 on phones. `references/macz-reference-1.md`.
- **Staggered three-column collage** (ref: macz-reference-3): three equal columns, each its own grid; the outer columns `grid-template-rows: 43fr 57fr`, the middle `57fr 43fr`, one fixed total height (~`clamp(32rem, 62vw, 46rem)`), 4px gaps, square corners, `object-fit: cover`, so no seam lines up. Two columns with the stagger on tablets, one on phones. `references/macz-reference-3.md`.

## Cards

- **Listing spread** (TT): callout plate, model, a big tabular price, a nowrap specs `dl`, and a prefilled "Ask about this one" link. `.unit`, `.specs`.
- **Product card with a service stamp** (GZ): 4:3 photo, a "Bench-checked" stamp, specs, a price and Reserve row. `.product`, `.stamp`.
- **Honest deal card** (GZ): a % sticker *with a stated reason* for the discount and an "N left" chip. Don't use it for craft businesses (positioning rule). `.deal`, `.deal__why`.
- **Desktop card with an overhanging phone** (PF): the phone capture hangs past the panel's corner. `.work__phone`.
- **Borderless team card** (ref: dala): a 24px-radius portrait, small uppercase role in the accent, a large regular-weight name, nothing else. `references/dala.md`.
- **Captioned image card** (MZ, ref: macz-reference-2): 4:3 image, serif h3, a line citing a real project; the whole card is the link. `.card`. The reference sets three equal 4:3 photos 4px apart with square corners and a centred serif caption under each, no card chrome, one ghost button under the row; `references/macz-reference-2.md`.
- **Seam-straddling icon badge** (IW): an icon tile half over the photo and half over the body. `.card__icon`. Variants: a seam-straddling portrait (live: Children Matter); a stat badge with an inset collage (IW `.media-stack__badge`, live: Parker).
- **Featured price card** (IW): 3 plans, the featured one with an accent border and a "Best value" pill. `.price-card--featured`.
- **Listing card with a spec dialog** (IC): inset media, 3-up specs, a `<dialog>` with a spec table. `.car-card`, `.car-dialog`.

## CTAs and closings

- **Pill with arrow disc** (ref: architect-reference): one button shape everywhere, a full pill with a trailing round arrow disc; white on dark, ghost = 1px outline pill. `references/architect-reference.md`.
- **Closing panel with photo CTA** (ref: architect-reference): a rounded panel, headline + contact columns left, a small photo right with the primary pill laid over it. `references/architect-reference.md`.
- **Single pill per view** (ref: dala): one 14px uppercase 600 filled pill (~45px tall, 24px radius) is the only filled control on screen; every secondary action is a bare text link. `references/dala.md`. Built by MS: the call is a caps text link with a muted underline that turns amber on hover (`.btn-ghost span`); a second pill on Contact was the finish reviewer's fix.
- **Rectangular ghost caps button** (ref: macz-reference-2, ref: macz-reference-3): `border: 1px solid var(--outline); border-radius: 2px; padding: .8em 1.6em`, sans 500 at ~.72rem, `letter-spacing: .15em`, uppercase; every "more" link uses it, centred under its row; the filled variant in the one dark action colour is the primary. `references/macz-reference-2.md`.
- **Full-bleed closing field** (TT): an accent-colour band with a huge ink headline and an inverse CTA pair; a slimmer strip on inner pages. `.closing`, `partials/visit-strip.html`.
- **Photo closing band** (MZ): parallax photo, a heavy left scrim, solid below 699px, CTA plus ghost phone button. `.band--cta`.
- **Email as the closing headline** (PF): "Have a project in mind?", then the email at headline size, copy button, next-steps line. Best for one-person businesses. `.contact-band__email`.
- **Notched closing panel** (GZ): a panel with chamfered corners and a clip-path notch taken from the trade's object. `.closing__panel`.
- **Quote band** (MZ): the firm's own line in large serif over a photo. `.band blockquote`.
- **Mobile two-button bar** (IW, WK): a fixed Call + Quote bar under 640px that respects the safe-area inset. IW `.mobile-bar`, WK `.mobile-callbar`.

## Navigation and header

- **Fade-in sticky header** (PF, MZ, IC): a fixed-height bar; a `::before` backdrop fades in and the logo scales to .95 on scroll (transform and opacity only). PF `.site-header::before` + `motion.js`; MZ adds light ink over photos (`.has-hero`).
- **Transparent caps nav** (ref: dala): 14px uppercase 600 links in muted grey, white when current, the pill anchoring the right; no border or blur. `references/dala.md`.
- **Split caps nav with centred wordmark** (ref: macz-reference-1): a `1fr auto 1fr` grid inside the hero frame: tiny tracked caps links left, the stacked wordmark centred, icon buttons right, white over a top scrim; wordmark + call + menu on phones. `references/macz-reference-1.md`.
- **Catalogue-tab nav** (TT): the current page is an accent tab hanging from the header bar. `.site-nav a[aria-current]`.
- **Header call icon button** (TT, MZ): the phone number collapses to a round outlined icon button on phones. `.header-call`.
- **Category strip in the hero panel** (GZ): 7 icon links, a 4×2 grid with a "Categories" cell on phones. `.catnav`.
- **Centred sticky service pills** (IC): a fit-content pill bar with scroll-spy. `.service-nav`.
- **Utility header split** (live: Aurora, Parker): address and hours on one side, phone and booking on the other. **Colour-per-action chips** (live: Children Matter): each logo colour is one action.

## Forms

- **Contact card before the form** (MZ, TT): a sticky call, email and hours card first in the DOM (phone first on mobile), then the form with a next-steps note above submit. MZ `.contact__quick`, TT `.contact`, `.form__next`.
- **Floating quote card** (IW): a white card, a 3-column grid, icon-prefixed inputs, the reply promise in the header. `.quote`, `.control`.
- **Dark band with a paper form card** (WK): a brand-colour band, a paper card, a lock-icon reply-time line. `.quote-band`, `.form-card`.
- **Reserve list instead of a cart** (GZ): a header count links to a list that pre-fills the quote message. `.reserve`.
- **One-line request strip** (ref: macz-reference-4): a slightly raised panel, serif H3 and a one-line sub on the left, one field and one dark filled button on the right in one row from 700px. The reference is a newsletter; use it for a callback or quote request with a real backend, never as a fake signup. `references/macz-reference-4.md`.
- **Hero qualifier finder** (IC): a bar of 3 selects, which must start on an empty "Choose…" option. `.finder`.

## Footers

- **Ink three-column footer** (TT): auto-fit 14rem columns, accent condensed headings, an aligned hours grid, credits in the legal line. `.site-footer`.
- **Four-column night footer** (MZ, IW): brand and divider, contact rows, hours and socials, nav, legal row. MZ `partials/footer.html`.
- **Light four-column footer with serif brand** (ref: macz-reference-4): the footer stays on the page colour; the brand name in the display serif over a short blurb, two link columns under tracked-caps labels, a location column with the address and small square social icons; 2 columns on tablets, 1 on phones. `references/macz-reference-4.md`.
- **Single hairline bar** (PF): name on the left, muted email and phone on the right. For one-page sites. `.site-footer__bar`.
- **Logo horizon stripe** (WK, MZ): an 8px band in the logo's two colours above the footer, or the logo's stroke as a `currentColor` divider that flips on dark. WK `.horizon`, MZ `.horizon`.
- **Split hours tables** (live: Aurora): each service's hours as its own aligned mini-table.

## Typography

- **One variable family by width** (TT): Archivo at 64–72% stretch, weight 800 caps for headings, 100% for body, tabular money.
- **Serif display with sans numerals** (MZ): Marcellus headings, Jost numerals so "01" never reads "OI".
- **Colour-emphasis serif headline** (PF): Cormorant 600 with the key words in the accent through a non-italic `<em>`, under a tracked-caps greeting. `.hero__role em`.
- **Split-colour rule title** (GZ): an uppercase H2 between gradient hairlines. `.rule-title`.
- **Two-tone headline** (IC): a condensed caps statement with an accent payoff line. Use 1.05+ leading, not IC's .88.
- **Condensed numerals for money and steps** (IW): Anton for prices, stats, 01–04 counters and the 404.
- **Outlined numerals** (IC): transparent numerals with an accent text stroke. `.step__num`.
- **Scale, not weight** (ref: dala): one sans at 400 from body to 113px display, -0.04em tracking at 42px+, 1.1 leading; headlines never bold. `references/dala.md`.
- **Ultra-light body** (ref: dala): 18px weight 200 (or 300 on Windows-heavy audiences) at 1.5, white on black. `references/dala.md`.
- **Squared display on navy** (live: Macon, Russo One + Open Sans) and **tech grotesk** (live: Parker, Bai Jamjuree + Sarabun) for industrial and auto trades.

## Colour

- **Warm near-black stack** (ref: architect-reference): `#141413` / `#1F1F1D` / `#282725` surfaces split by 1px `#3F3E3D` rules, warm off-white ink, one thin gold accent for line work only. `references/architect-reference.md`.
- **Charcoal, raised panel and one warm accent** (PF): `#1C1C1D` page, `#262627` panels, cream `#EFE7DA` ink, amber `#F2963A` accent.
- **Void + one action colour + spark** (ref: dala): pure `#000` canvas, white ink, one saturated fill used only for the primary pill, a warm second accent for labels and emphasis. `references/dala.md`. Built by MS (`#000`, violet `#8052ff` pill, amber `#ffb829` spark): with no raised surfaces every token is checked once, on black. Keep the spark for labels that carry an offer, not one under every heading (L-073).
- **Material as the only colour** (ref: macz-reference-2): a neutral UI (grey or white surfaces, charcoal ink) with every photo chosen for one warm material (wood, brass, terracotta), so the photos carry the palette. `references/macz-reference-2.md`.
- **Neutral grey with one espresso action colour** (ref: macz-reference-4): a flat `#E0E0E0`-ish page and panels, warm charcoal `#2D2B29` ink, and one dark brown (`#45392F`-ish) used only for the filled button. Muted greys on that page must still reach 4.5:1 (the reference's don't). `references/macz-reference-4.md`.
- **Surface role tokens** (TT): each band redefines `--fg`, `--muted`, `--rule`, `--btn-bg`, `--btn-fg`. The cleanest way to satisfy "every dark surface flips text and graphics".
- **Fill accent and text accent are separate tokens** (IC): `#e30709` for fills, `#ff6466` for red text on dark.
- **Dark ink on a mid-tone CTA** (IW): navy text on `#F26B1D` (4.81:1) because white on it is only 3.05:1.
- **Logo-seeded tonal roles** (MZ): the accent only as a fill where action happens, never as text on light.
- **Gradient-border ghost button** (GZ): a padding-box/border-box double background. `.btn-ghost`.
- **Two-colour rhythms from the live sites:** ink `#0E111B` + electric `#0096FF` (Parker); navy `#093075` + crimson `#a2001a` (Macon).

## Details

- **Frosted badge on a photo edge** (ref: architect-reference): a small rounded panel with `backdrop-filter: blur(12px)` and a translucent dark fill, overlapping a photo's lower-left corner, holding one true fact. `references/architect-reference.md`.
- **FIG. plate** (TT): a photo at its natural aspect in a 2px frame with an accent "FIG. n" tab and one numbering sequence sitewide. `.plate`, `.fig`, `h_plate`.
- **Linked callouts** (TT): focusable %-positioned discs and key rows highlight each other on hover and focus. `h_cplate`, `main.js`. Check every pin against the full-size photo.
- **Drawing title-block caption** (MZ): a ruled `max-content 1fr` grid with tracked caps labels. `.titleblock`.
- **Trade-object dividers** (GZ): circuit trace with solder nodes, waveform, device-notch clip-path, battery meter. `.divider--trace` and others.
- **Highlighter swipe** (TT): a skewed accent block behind the one number that matters. `.hl`.
- **Live open/closed status** (WK): an `HOURS` map writes into every `[data-open-status]`, with a truthful fallback when JavaScript is off. `main.js` › store hours.
- **Plain-numbers copy** (live: Parker): rewards and warranty maths written out.

## Motion (all JavaScript: `main.js` `morph()` or GSAP `motion.js`)

- **Word-rise headings, no mask** (PF): SplitText words `yPercent: 45` plus a fade, stagger .06, replaying on re-entry. With no line mask, serif descenders aren't clipped.
- **Rules drawn in sequence** (PF): `scaleX(var(--draw))` with a .3 stagger, so the project moves through its stages.
- **Dealt prints** (PF): cards drop in with a ±2.5° tilt and settle square, stagger .09.
- **Shared trace timeline** (GZ): a rail draws with scroll and nodes light from the rail's own progress. `motion.js` › `trace()`.
- **Pinned bench sequence** (GZ): a desktop pin for about 900px; steps light from opacity .7, which still passes contrast.
- **Flip filter grid** (GZ): filter pills reflow cards with GSAP Flip.
- **50% parallax on every full-bleed photo** (MZ): rAF `translateY`; CSS sizes images `max(100%, 50% + 50lvh)`.
- **Transform-only shrinking header** (IC, PF): `translateY` bar, fading backdrop, logo `scale()`.
- **Ambient particle drift** (ref: dala): low-density shapes drifting slowly on a canvas behind content (rAF, paused off-screen, off under reduced motion). `references/dala.md`.
- **Fixed ambient canvas behind every page** (MS): one `position: fixed; inset: 0; z-index: -1` canvas of 26–70 triangles (by screen area) drifting up at 3–10px/s. The page colour goes on `html` and `body` stays transparent, or the canvas is hidden (L-060). One rAF loop drives it and the hero field, stops on `visibilitychange`, and draws one still frame under reduced motion. It cost no Lighthouse points (100 home, TBT 0). Particles show through transparent form fields: give inputs a solid fill. `field.js` › ambient, `.ambient`.
- **Pinned count-in** (MS): desktop (≥900×640) pins the steps for `+=1500`, scrub .6; the scroll plays a bar of four beats: a metronome needle swings ±24° per step (`svgOrigin` inside the SVG, L-046) and the current step lights (numeral amber, opacity 1) while the rest wait at .72 (L-047). Read progress from `onUpdate(self)`, never `this` (L-071). Phones: no pin, the needle scrubs over the list and each step lights at 60%; reduced motion: all lit. `motion.js` › count-in.
- **Logo object keeping time on the 404** (MS): the metronome needle swings on a .5s `sine.inOut` yoyo loop (120 BPM) above "That page lost the beat." A cheap, on-brand 404. `motion.js` › `.notfound`.
- **Hero mark drift** (Macz redesign): the giant aria-hidden name in the sky drifts down (yPercent 35) and fades to .25 as the hero scrolls away. It is scrubbed and never hidden at load, a quiet first GSAP moment. `motion.js` › `.hero__mark`.
- **Split-line quote** (Macz redesign): SplitText line reveal on the quote band. Put it on a heading: SplitText adds an aria-label, which axe prohibits on a `<p>`.

## Advanced motion system (`GSAP motion: advanced`)

The reference build for `advanced` (MS, 2026-10-12, modelled on dala.craftedbygc.com). The site itself is archived and out of the library; these are the parts that carry over.

- **One fixed morphing stage:** a single full-screen `canvas.stage` (z-index -1) behind the home page. Each section carries `data-stage="<shape>"` (plus `data-stage-dim`); motion.js writes each section's scroll-in progress (`top 65%` → `top 35%`, a short window so each shape holds whole even under a short section) into a global, and the canvas eases a morph index over it, moving each particle between two shapes with a per-particle stagger. Perspective F=900, wireframe tetrahedra, about 1,500 particles (900 on phones). Dim every shape but the hero's on phones (about 0.55×). Reduced motion: one still shape in the hero box.
- **Drawing any object from strokes:** describe each shape as strokes in a unit space: `line`, `ellipse` (with an arc range), `face`/`side` (a closed outline at two depths, for thickness), `path` (arc-length parameterised), `rounded` (Chaikin smoothing), `mirror` (draw half, reflect) and `tube` (a centreline with radii). `sample()` spreads the particles along all strokes by length × weight, so a heavier stroke reads as solid. Tag strokes (STRING, STICK, KEY…) so the motion moves only the tagged particles; `pose()` turns, tips and scales the whole shape, then places it in the section's empty side.
- **Placement rule:** put each shape in the empty side of its section and check it at the scroll point where it's fully formed, with the neighbouring sections' windows in mind. Anchor shapes that sit near text to that text's measured position, not to viewport fractions (L-079), and implement `window.__motionShapes()` / `.stops()` so `browser_qa.mjs` can sweep them. The stage sits behind the page, so an opaque photo hides whatever is under it. First-pass misses: a shape ran through a paragraph, a halo covered the closing headline, an object tipped nearly edge-on read as striped terrain, one hid behind the previous section's photo, and one never formed because the next section's morph started too early (L-077).
- **Rendering cost:** one `requestAnimationFrame` loop for every canvas, stopped while the tab is hidden and skipped for canvases off-screen (IntersectionObserver). Draw one path per colour and alpha tier (about 14 strokes a frame, not 1,400), 1px strokes, no blur or glow. Lighthouse mobile stayed at 100 with two canvases running.
- **Intro curtain:** an inline head script sets `.is-intro` before first paint, unless reduced motion is on or sessionStorage says the intro has played. A short count lights, the curtain fades at about .9s while first-screen line reveals restart, and a 3.5s fallback timer removes the class if motion.js never claims it. Re-check every reveal when the curtain lifts (L-081). It cost about 0.5s of LCP.
- **Line reveals on all copy:** SplitText `lines` + `mask: 'lines'` on h1/h2, ledes and body paragraphs (yPercent 105, 1.1s `expo.out`, stagger .08), `aria: 'auto'` on headings and `'none'` on paragraphs. `.line-mask { padding-bottom: .12em; margin-bottom: -.12em }` keeps descenders. Any re-split triggers a debounced `ScrollTrigger.refresh()` (L-076). Text inside a pin gets the pin's length added to its `inView()` end (L-078).
- **Smooth wheel without a library:** about 30 lines on `gsap.ticker`: fine pointers only, lerp scrollY toward a wheel target with `1 - exp(-dt * 7)`, let go if anything else scrolls, and skip ctrl, horizontal and inner-scroller wheels.
- **Jump bar:** a sticky, centred, blurred pill under the header with a scroll-spy in main.js. The current link is the section crossing 40% of the viewport, and the row scrolls sideways to keep it in view.

## Avoid (seen in our own past work)

- Category template tells: a make or brand marquee, an eyebrow over most headings (IC: 30 of 66), many CTA labels (IC: about 20), struck-through "was" prices at a craft shop, icon-tile rows, a 10-block homepage (WK). These are what make a site look like a competitor's.
- Template leftovers after a restyle: WK kept its old structure and colour roles; TT's PRODUCT.md kept "black and yellow".
- Photos repeated across pages (WK, IW), stock that contradicts the place (IW: US suburbs; TT: Thai "local" photos), sponsor logos on product photos (TT).
- A hero photo in a circle when the reference used a cut-out (GZ), and off-palette band photos.
- CSS transitions and keyframes, reveals that play only once, headline leading below 1 (IC .88, TT .88–.95, IW 1.02), Google Fonts links, a fake "sent" form (IW), and a primary button with a coloured glow (IW). Port the idea, not the code.
- A shipped design that drifts from PROJECT.md › Direction without logging it (MZ).
