# Ernest Banigon portfolio: charcoal and amber, with the work shown in live browser frames
Personal portfolio (web designer & SEO) · own · October 2026 · 1 page + 404 · pipeline build (GSAP) · Source: `Portfolio Site/`
Screens: `../shots/portfolio.webp`, `../shots/portfolio-phone.webp` · Inspiration: none in the library (Ernest picked two references, a dark headphone product page and a "Hi! I'm…" hero, which are described in PROJECT.md › Direction but not saved) · Full page: `Portfolio Site/qa/shots/index-1440-full.png`, `Portfolio Site/qa/shots/index-390-full.png`

## Identity
A designer's own site, where the work is the content. Nine websites are shown as framed browser screens that scroll through the whole homepage, travel posters sit on raised panels like prints on a table, and the person is a cut-out portrait standing in a lit arch. The charcoal page with warm amber reads as calm and premium, so the brightly coloured client screenshots and posters stand out from it instead of fighting a branded background. Mood: warm, nocturnal, editorial, quiet, confident. It avoids looking like a template because the signature device (the browser frame that scrolls through each project) only makes sense for someone who builds websites, the logo is a browser window around "EB", and the hero is a real cut-out portrait rather than a stock "creative" photo.

## Palette
All in `:root` in `assets/css/styles.css`. The whole site is dark; `[data-surface="dark"]` only re-states `--c-band`.

| Token | Hex | Role | Notes (contrast on which surfaces) |
|---|---|---|---|
| `--c-bg` | #1C1C1D | Page, header backdrop, footer, `.browser__play` button | Base surface |
| `--c-panel` | #262627 | Raised panels (`.sheet`): work frames, posters, lightbox, mobile nav | The lightest surface; every text token is measured against it |
| `--c-band` | #222223 | Contact band (`[data-surface="dark"]`) | Only a slight step from the page; the band edge is barely visible (see the 1440 full shot) |
| `--c-ink` | #EFE7DA | Cream headings, ghost-button border/text, skill names | 12.2:1 on panel |
| `--c-text` | #D3CDC3 | Body | 9.5:1 on panel |
| `--c-muted` | #A7A196 | Section intros, captions, process copy, footer, browser-bar labels | 5.8:1 on panel, 6.6:1 on page |
| `--c-brand` / `--c-link` | #F2963A | Amber: primary button, hero greeting and the highlighted words, links, step numerals and rules, focus ring | 6.6:1 on panel; text on amber is `--c-on-brand` #1C1C1D (7.5:1) |
| `--c-stroke` | #77736C | Social icon rings, skills grid lines | 3.4:1 on page (graphics floor 3:1) |
| `--c-line` | #3A3A3C | Hairlines: section rules, browser bar, header shadow line | Decorative only |
| (literal) | #34322F | Hero arch behind the cut-out (`.hero__photo::before`) | Lighter than the page so the black shirt keeps its outline; not a token |
| (literal) | #0E0E0F | Phone-frame bezel (`.work__phone`) | Darker than the page, so the phone reads as a device |
| Ambient glow | rgb(242 150 58 / .3–.42), rgb(214 128 52 / .35–.55), rgb(140 78 32 / .6) | Blurred light pools behind the hero and Skills (`.ambient::before`, `filter: blur(40px)`) | Client-requested exception to the no-glow rule; browser_qa measured text over it |

## Typography
- **Display: Cormorant 500–700** (self-hosted variable woff2, preloaded, `_src/partials/fonts.html`). Used for h1–h3 (weight 600), the process numerals, skill names and the contact email.
  - `h2`: `clamp(2.5rem, 1.8rem + 3vw, 4rem)`, line-height 1.05, tracking -.01em, `text-wrap: balance`.
  - Hero role `.hero__role`: `clamp(3rem, 1.6rem + 5.4vw, 6.25rem)`, line-height **1.1** (raised from .98 after descenders collided, L-051), tracking -.015em. The `<em>` words "Designer" and "SEO" are `font-style: normal` and amber, so the emphasis comes from colour, not italics.
  - Contact `h2`: `clamp(2.75rem, 1.8rem + 4.4vw, 5.25rem)`, line-height 1.1.
  - Contact email: `600 clamp(1.75rem, 1.1rem + 2.8vw, 3.25rem)/1.15`, amber, underlined at `.18em` offset, `overflow-wrap: anywhere`. It works as the closing headline.
  - `h3`: 1.625rem / 1.15 (work names, process steps).
  - Step numerals: `600 2.75rem/1` Cormorant amber with `lining-nums` (2.25rem on phones).
  - Skill names: Cormorant 700, uppercase, tracking .05em, .9375rem on phones and 1.25rem at ≥760. This is the only place the serif is set in caps.
- **Body/UI: Archivo 400–700**, `400 1.0625rem/1.65`. Hero lede 1.1875rem/1.65, max 35rem.
- **Tracked capitals** (`.caps`, nav, `.brand__name`, `.work__meta`, `.browser__bar`): Archivo 600 at .75–.8125rem, tracking .12–.16em, uppercase. The hero greeting "HI! I'M ERNEST" uses the same treatment in amber at `clamp(.875rem, .8rem + .35vw, 1.0625rem)`.
- Buttons: Archivo `600 1rem/1.2`, tracking .02em.

## Homepage anatomy
1. **Header** — sticky, fixed 4.5rem bar, transparent over the hero. Browser-window "EB" logo (amber frame, cream letters, `_src/icons/logo-mark.svg`), the full name in tracked caps, three anchor links (Work / Graphic design / Process) in tracked caps, and an amber "Start a project" button. Once scrolled past 40px, GSAP fades in a charcoal `::before` backdrop with a hairline and scales the logo to .95. Phones: below 900px a burger opens a panel-coloured drop-down; below 600px the header CTA is hidden. There's no tap-to-call, on purpose: this is a portfolio, not a storefront (`LOCAL_BUSINESS = False`).
2. **Hero** (`.hero-wrap` > `.hero`) — 7fr/5fr grid at ≥900px, left aligned. Amber caps greeting, a two-line serif headline "A Web **Designer** & **SEO** Specialist", a one-sentence lede, a primary button plus a ghost button ("See the work"). On the right is a transparent cut-out portrait standing in a #34322F arch (`border-radius: 999px 999px 6px 6px`, inset 14% from the top) so the head rises above the arch. Blurred amber light pools sit low and to the right, and spill 10rem into the next section. **What makes it work:** the arch gives a dark shirt on a dark page an outline without using a box or a white background. Phones: the portrait moves above the text (`order: -1`, 14rem wide, centred), the glow moves up behind it, the buttons split 50/50, and the CTA ends at 834px on an 844px phone.
3. **Client websites** (`#work`) — section head (h2 + muted intro, max 44rem), then a 2-column grid at ≥760px (gap `clamp(2.5rem,5vw,4.5rem) 3rem`) of 4 cards. Each card has a `.sheet` panel holding a browser frame (bar label = the domain in tracked caps, a 16:10 screen) with the homepage's top showing. Below it: the serif name, a one-line description, "WEBSITE DESIGN" meta and an amber underlined "Visit domain ↗". **What makes it work:** hovering, or pressing the "Scroll the page" button, scrolls the full-page screenshot through the frame. Phones: one column; the button is how touch users get the effect.
4. **Concept projects** — a hairline-ruled section (`.section--rule`). Same card, 2 columns × 3 rows of 6. Each frame is labelled "CONCEPT PREVIEW", and a phone screenshot in a #0E0E0F bezel (`.work__phone`, 22% wide) overhangs the bottom-right corner of the panel. The intro states honestly that these are self-initiated previews, not the businesses' official sites. Phones: one column, with the phone frame still overlapping.
5. **Print and graphic design** (`#design`) — ruled section. Six A-ratio posters on panels (padding .35–.6rem), 3 across with 3rem gaps at ≥900px, a muted caption under each, and a click-through to a `<dialog>` lightbox. Phones: a horizontal scroll-snap rail (`grid-auto-columns: min(62%, 15rem)`) that bleeds to the screen edges, which cut about 1,000px of phone height.
6. **Skills** (`#skills`) — a second ambient glow (left and right pools, faded to the page colour at top and bottom). 8 tools in a ruled grid of #77736C cells on a translucent charcoal fill (`rgb(28 28 29 / .62)`), 4 across at ≥760px with the icon stacked over a Cormorant caps name, rows 2rem apart. The icons are custom line drawings, not brand logos. Phones: compact 2-column tiles with the icon beside the name. Weakness: the heading is a bare "Skills" with no intro, and the 2rem row gap breaks the ruled grid into two separate bands.
7. **How a project works** (`#process`) — at ≥1100px a 4fr/8fr grid. On the left are the h2 and a 4:5 stock photo on a panel (a hand sketching wireframes with an orange pen, which echoes the amber). On the right is a 2×2 numbered `<ol>`: each step has a hairline top border with a 3.5rem amber segment, a large amber Cormorant numeral, an h3 and muted copy. Under that, a `<dl>` with Pricing and Timeline in two columns (this answers the buyer's pre-contact questions). Phones: no photo, the numeral sits beside the title (2.25rem column), one column.
8. **Contact band** (`#contact`, closing CTA) — #222223 band, 7fr/5fr at ≥900px. On the left: the huge serif "Have a project in mind?", a muted lede, the email as an amber serif headline-sized link, the phone with an amber icon, a ghost "Copy email address" button (shown only when the clipboard API exists, with a `role="status"` confirmation), a what-happens-next line, and round LinkedIn/Facebook icon buttons. On the right: a square stock photo (notebook "Notes", fountain pen, glasses) on a panel, shown only at ≥900px. There's no form, on purpose: there's no backend, so the contact is a mailto link and the copy button.
9. **Footer** — a hairline-topped bar with © name on the left and the muted email and phone on the right; wraps on phones.

## Other page patterns
- `404.html`: reuses `.hero--404` (min-height 50vh, h1 `clamp(2.75rem, 2rem + 4vw, 4.5rem)`), with one sentence and a text link home. It deliberately doesn't add a second primary button.
- Poster lightbox: a native `<dialog>` (`.lightbox`, max 54rem, `100dvh - 2rem`) with a sticky caption bar and a ghost Close button. The backdrop is `rgb(14 14 15 / .88)`, and clicking it closes the dialog. Each poster is a plain link to its large file, so it still works without JS.

## Signature elements
- **Scrolling browser frames**: a 16:10 `container-type: inline-size` screen whose full-page screenshot translates to `calc(-100% + 62.5cqi)` (62.5cqi = the screen's height). The CSS holds the end state, and GSAP tweens it (7s down, 0.9s back). `assets/css/styles.css` › `.browser`, `.browser__screen`, `.work.is-playing`; `assets/js/motion.js` › "work screens"; markup from `_src/site_config.py` › `_screen()`.
- **Overhanging phone frame** on concept cards: desktop screen plus a phone capture in a bezel that hangs past the panel corner. `styles.css` › `.work__phone`.
- **Cut-out in a lit arch**: a transparent portrait standing on a lighter rounded-top shape, with its head breaking out of the top. `styles.css` › `.hero__photo::before`.
- **Amber words inside a cream serif headline**, with emphasis carried by colour, not italics. `styles.css` › `.hero__role em`.
- **Ambient amber light**: stacked, blurred radial gradients in an isolated z-index -1 layer, faded into the page with a linear gradient. `styles.css` › `.ambient`, `.ambient--skills` (offsets in rem, not %, to keep CLS at 0, L-053).
- **Ruled process steps with an amber lead segment** that draws in order. `styles.css` › `.steps li::after` (`scaleX(var(--draw))`), `.steps li::before` (CSS counter numeral).

## Motion
All motion is GSAP 3.15 (self-hosted; ScrollTrigger + SplitText) in `assets/js/motion.js`, inside `gsap.matchMedia('(prefers-reduced-motion: no-preference)')`. CSS has no transitions at all; it only holds the states. The hero is never hidden at load. Entrance moments use the `inView()` helper: they play when the trigger is 80–90% onto the screen, from either direction, and reset only once fully off-screen, so they replay.
- **Section headings** (`[data-gsap="split"]`, 5 h2s; Skills and the hero are excluded): SplitText splits by words, `yPercent: 45, opacity: 0`, 0.7s `power3.out`, stagger 0.06. There's no line mask, so Cormorant's descenders are never clipped.
- **Process rules**: `--draw` 0→1 on each `li`, 0.6s `power2.inOut`, stagger 0.3 (steps 1 to 4 in sequence).
- **Posters "dealt"**: `y: 56`, rotation cycling -2.5/2/-1.5/2.5/-2/1.5°, fade in, 0.75s `power3.out`, stagger 0.09; they settle square.
- **Work cards**: each card rises separately (`y: 32`, 0.7s `power2.out`), and the second column is delayed 0.1s.
- **Browser scroll-through**: 7s `sine.inOut` down, 0.9s `power2.out` back. Triggered by mouse `pointerenter` or by the `.is-playing` class (set by main.js's button and watched with a MutationObserver).
- **Header**: `--hdr` backdrop opacity and logo scale 1→.95, 0.25s, toggled at 40px of scroll.
- **Mobile menu**: `autoAlpha` + `y: -8`, 0.2s.
- No parallax. `main.js` holds only states and behaviour (nav toggle, `.is-scrolled`, the play button, copy email, the lightbox); its `.reveal` and parallax code are unused template code.

## Reusable components
- **Header**: a fixed-height sticky bar with a GSAP-faded `::before` backdrop and a scaled brand. `styles.css` › `.site-header`, `.site-header::before`, `.brand`.
- **Buttons**: the amber primary (`.btn-primary`, min-height 3.25rem, 3px radius) is the only filled button; the cream-outlined `.btn-ghost` is used for secondary actions. Hover changes opacity instantly. `styles.css` › `.btn`.
- **Raised panel**: `.sheet`, #262627 with a neutral two-layer shadow (`--shadow`) and a 6px radius. The one surface device, used for screens, posters and photos.
- **Work card**: browser frame, serif name, one-line description, meta caps and an amber "Visit ↗" link. `styles.css` › `.work`, `.browser__bar`, `.work__link`.
- **Poster rail → grid**: a scroll-snap rail on phones and a 3-column grid at ≥900px. `styles.css` › `.poster-grid`.
- **Skills grid**: a ruled 4-column cell grid that turns into 2-column inline tiles on phones. `styles.css` › `.skills__grid`, `.skill`.
- **Numbered steps + terms**: `styles.css` › `.steps`, `.terms`.
- **Social icon buttons**: 2.75rem round buttons with #77736C rings that go amber on hover, with the accessible name on the link. `styles.css` › `.social`; `_src/partials/social.html`.
- **Copy-email button**: hidden without the clipboard API, with a `role="status"` message. `assets/js/main.js` › "copy email".
- **Footer**: a single hairline bar. `styles.css` › `.site-footer__bar`.

## How it went
- Lighthouse mobile **99 / 100 / 100 / 100**, LCP 2.0s, CLS 0.00, TBT 1ms (before self-hosting the fonts and the CLS fix it was 78 performance, CLS 0.26, LCP 2.9s). qa.py: 0 errors, 1 justified warning (the radial-gradient glow, which the client asked for). browser_qa: 0 errors, 1 warning (9,945px tall at 390, accepted because it's nine projects each shown once).
- The direction changed once: from a light "proof sheet" to "charcoal and amber" after Ernest picked a reference. Requests he made and got: shortening the greeting to "Hi! I'm Ernest", amber Designer/SEO, the glow, the Skills section in one colour, the portrait above the text on phones, the stock photos filling the empty columns, GSAP, and the browser-window logo (option B, chosen over a magnifying-lens version).
- Mistakes he caught, which became lessons: white halo on the cut-out (**L-038**); an old opaque headshot cached under the same URL (**L-037**: rename long-cached files); the burger not at the right edge because a hidden sibling still matched `+` (**L-036**); a ~120px gap between the poster rail and Skills on phones (**L-041**); descender collisions at line-height .98 that I had wrongly dismissed as a detector false positive (**L-051**). Caught by self or tools: a % offset on the glow causing CLS 0.26 (**L-053**); a misaligned step heading from a stretched grid (**L-054**); tools/ out of sync with the template (**L-052**); Cloudflare host from the brief (**L-035**).
- Open questions: the reply-time promise and quote wording, which sites included SEO work, and a custom domain.

## Reuse guidance
**Fits:** any portfolio or studio whose product is visual work: web or UI designers, agencies, photographers (swap the browser frame for a print sheet), architects, interior or product studios. Also dark, premium single-product or personal brands (audio, watches, coffee roasters, barbers) where photography should glow against charcoal. The panel + neutral shadow + one warm accent system transfers anywhere that needs a quiet stage for colourful content. The scrolling browser frame transfers to any SaaS or agency "see it live" showcase. The ruled numbered process + pricing/timeline `dl` transfers to any service business.
**Keep to this site:** the browser-window "EB" logo, the "Hi! I'm Ernest" greeting with amber role words, the cut-out-in-arch portrait (it relies on his specific waist-up headshot), the amber ambient glow (it was his explicit request; by default the no-glow rule still applies), the Solasta poster set, and the exact charcoal #1C1C1D + amber #F2963A pairing as a whole identity.
