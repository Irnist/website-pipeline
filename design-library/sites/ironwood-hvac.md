# Ironwood Heating & Air: a hot-and-cold service brand, navy and orange cut by a skewed stripe, set in Muntinlupa
HVAC / aircon cleaning & repair · sample · October 2026 · 7 pages (Home, About, Services, Service Areas, Pricing & FAQ, Contact, 404) · hand-built (static HTML with an optional `_source/build.py` generator, pre-pipeline) · Source: `Concept Websites/HVAC Website/`
Screens: `../shots/ironwood.webp`, `../shots/ironwood-phone.webp` · Inspiration: `../inspiration/ironwood-hvac-inspiration.webp` · Full page: `Portfolio Screenshots/HVAC Website.png`

## Identity
A conversion-first local trade site that turns the US "HVAC landing page" format into a Metro Manila aircon company. It talks about barangays, TESDA certification, DTI/BIR registration, Viber and Messenger, peso prices, and "Aircon not cooling?" rather than furnaces. The logo mark is a flame over a snowflake, and the palette follows it: navy for trust, orange for heat and action, sky blue for cool, used sparingly. Mood: **dependable, direct, workmanlike, warm, local**. What lifts it above the template is mostly content: every barangay listed, peso "from" prices on the homepage, "We show you photos of what we found", 90-day warranty, a 1-hour reply promise. Visually it stays close to the category template (trust-icon row, icon-badge service cards, brand-name strip, stat badge), and this entry says so plainly below.

## From the inspiration image
The reference ("SummitAir", Tempe AZ) showed: a blue topbar with a promo and contact, a white header with an orange phone pill, a dark hero split by an angled edge into a technician photo, a condensed all-caps headline with orange words, a trust-badge row, a horizontal 3-field quote form under the hero, a "Your local partner" split with a "+13 years" circle badge, a 3×2 service-card grid with "Learn more ↗" links, a black "Brands we service" logo strip, a "Why choose us" icon list, and a map.
**Taken:** almost the whole section order; the topbar, header and phone pill; the angled hero divider (rebuilt as `.hero::after`, a 14px orange stripe skewed −12° with a sky-blue offset shadow line); the condensed caps display face (Anton); the horizontal quote form; the years badge overlapping the about photo; the 3×2 cards with "Learn more ↗"; the dark brands strip.
**Changed on purpose:** the black became brand navy `#0F2A44`. The brand strip uses plain text names plus an "independent service provider" disclaimer, never manufacturer logos. The orange-highlight words in the headline were dropped, so the h1 is all white (the `.hot`/`.cool` spans exist in CSS but are unused). The quote form became a floating white card with labels, icons and a reply-time promise. Pricing and an FAQ were added to the homepage, and the clip-art trust badges became navy icon tiles with two-line text. Section titles are mixed case, not all caps, so long headings stay readable.

## Palette
Tokens in `assets/css/styles.css` › `:root`.

| Token | Hex | Role | Notes (contrast on which surfaces) |
|---|---|---|---|
| `--navy` | `#0F2A44` | Text, hero/CTA/brands/stats backgrounds, secondary button | 13.4:1 on cream; 4.81:1 as text on orange (used for the primary button label) |
| `--navy-900` | `#0A1E31` | Topbar, footer, hero gradient start | Muted text `#C7D3DF` reaches 11.1:1 on it |
| `--navy-700` | `#1A3A5C` | Navy button hover | — |
| `--orange` | `#F26B1D` | Primary CTA fill, card icon badges, hero stripe, display numerals, footer icons | Navy on it 4.81:1 (pass). **White on it only 3.05:1**, so all orange buttons use navy text; keep that. As text on navy it's 4.81:1 (stats, badge numbers, large) |
| `--orange-600` / hover | `#DB5C12` / `#FF7D30` | Hover fill (`.btn:hover` uses `#FF7D30`) | Navy on `#FF7D30` 5.73:1 |
| `--orange-ink` | `#B84A0A` | Orange text on light: brand tag, active nav, `.req`, area pins, team roles | 4.79:1 on cream, 5.22:1 on white |
| `--sky` | `#3BA9E0` | Focus ring, input focus border, the second hero stripe, ticks on navy | 5.53:1 on navy; decorative or focus only on light |
| `--sky-100` | `#E3F2FB` | Tick circles, feature icon tiles, subnav hover, card-media fallback | Background tint only |
| `--cream` | `#F7F5F0` | Page background, input fill | Warm off-white; alternates with `--white` sections |
| `--white` | `#FFFFFF` | Cards, `.section--white`, quote card | — |
| `--text-muted` | `#4A5B6E` | Body copy on light | 6.4:1 on cream, 6.97:1 on white |
| `--text-on-dark-muted` | `#C7D3DF` | Lead text on navy | 9.6:1 on navy |
| `--border` / `--border-strong` | `#E2DED5` / `#CFC9BC` | Card and input borders | Warm greys that match the cream |
| placeholder | `#7A8796` | `.input::placeholder` | **3.36:1 on cream, below 4.5** (weakness) |
| `--error` / `--success` | `#B42318` / `#1E7B4A` | Form states | Tinted panels `#FDECEA` / `#E8F5EE` |

## Typography
- **Display:** Anton 400 (fallbacks Impact, Arial Narrow), via `.display`: uppercase, `letter-spacing: .01em`, `line-height: 1.02`. Hero `.hero__title` `clamp(2.75rem, 6.6vw, 5rem)`; inner `.page-hero h1` `clamp(2.5rem, 6vw, 4.25rem)`; CTA band h2 `clamp(1.9rem, 4vw, 3rem)`.
- **Section titles** override the caps: `.section-title { text-transform: none; letter-spacing: 0 }` at `clamp(2rem, 4.4vw, 3.25rem)`, so "Complete aircon solutions for every property" is condensed mixed case with `text-wrap: balance`. The quote-card title uses the same treatment at `clamp(1.6rem, 3vw, 2.2rem)`.
- **Anton as numerals:** prices (`.price strong` 2.8rem), stats (`clamp(2.4rem, 5vw, 3.4rem)` in orange), the badge "10+" (2.6rem), step counters "01–04" (`.step::before` 2.4rem orange), the 404 "404" (`clamp(6rem, 18vw, 11rem)`), card titles (1.5rem) and footer headings (1.25rem caps).
- **Body:** Manrope 400–800, 1rem / 1.65; `.lead` 1.125rem muted, max 62ch. UI labels (buttons, `.link-arrow`, brand tag, table heads) are Manrope 800, uppercase, tracking .04–.22em. Brand tag "HEATING & AIR" is .66rem at .22em tracking in orange-ink.
- Tabular numerals on the price table (`td.num { font-variant-numeric: tabular-nums }`).
- **Rule clash:** display line-height 1.02 is below the current 1.05 minimum (L-051). Fonts are linked from fonts.googleapis.com, not self-hosted.

## Homepage anatomy
1. **Topbar** (`.topbar`): navy-900 strip, 42px high. Snowflake icon + "Aircon not cooling? **Same-day service across Muntinlupa.** Book now" on the left; email, locality and hours with icons on the right. The promo hides under 1100px, and the whole bar hides under 640px.
2. **Sticky header** (`.site-header`): white at 96% with the backdrop blur on a `::before` (so the fixed mobile drawer isn't trapped). Logo mark + Anton "IRONWOOD" with an orange-ink "HEATING & AIR" tag. Nav has a Services dropdown; the active link gets an orange 3px bottom inset bar. Orange phone pill CTA on the right. On phones: logo + a navy 48px menu square; the phone moves to the bottom bar.
3. **Hero** (`.hero`): full-bleed photo of a Filipino technician spray-cleaning a split-type wall unit. A 100° navy gradient goes from .97 opacity to 0 at 72%, and the skewed orange stripe with a sky shadow sits at `left: 52%`. Copy is left-aligned in a 640px column: Anton caps h1 "Reliable aircon cleaning & repair in Muntinlupa City", muted lead, then an orange "Get a free estimate" button and a ghost phone button. Min height `clamp(560px, 78vh, 720px)`. **What makes it work:** the stripe turns a plain scrim into the brand's "cut" motif and echoes the logo's hot/cold. **Phone:** the photo stacks above the copy at 4:3 (`object-position: 78% 40%`) with a 6px orange bottom border standing in for the stripe; copy sits on solid navy and buttons go full width.
4. **Trust strip** (`.trust__grid`): 4 columns on white (2 at ≤960px, 1 at ≤640px). A 52px navy tile with an orange icon, then a bold line and a muted sub-line: Licensed & insured / DTI & BIR registered; TESDA-certified techs / RAC Servicing NC II; 24/7 emergency; 90-day warranty. The local credentials are what stop it reading as generic.
5. **Quote card** (`.quote`): a white floating card (22px radius, `--shadow-lg`) on cream. The head row pairs the title with "We reply within 1 hour during business hours". The `.form-grid` has 3 columns: name, mobile and service select on row 1, then barangay address (span 1) and "How can we help?" (`.field--wide`, span 2) on row 2. Every input has a leading icon. The submit row says "No spam…" on the left with an orange submit on the right. It drops to 2 columns, then 1. `.quote--lift` (negative top margin to overlap the hero) exists but isn't used on the homepage.
6. **About split** (`.split` + `.media-stack`): 1:1 grid on white. On the left, a team photo (5 uniformed techs on a Manila street, 4/3.4) with the navy `.media-stack__badge` "10+ YEARS KEEPING MUNTINLUPA COOL" overlapping the bottom-right corner, framed by a 4px cream border. On the right, a mixed-case Anton h2, a lead, and a 4-item `.ticklist` (sky-100 tick circles) of concrete promises, then a navy "More about us →". Stacks on phones.
7. **Services** (`.cards`): centred head, then a 3×2 grid of white cards (2 columns ≤960px, 1 ≤640px). Each card has a 4:3 photo, a 56px orange icon tile straddling the photo/body seam (`.card__icon` translateY(-50%) with a 4px white border), an Anton title, muted copy and "Learn more ↗". The whole card is a link via `.link-arrow::after { inset: 0 }`. Hover lifts the card, gives the border an orange tint and zooms the image to 1.04. A centred orange "View all services" follows.
8. **Brands strip** (`.brands`): a thin navy band. The Anton label "Brands we service" sits on the left, then a wrapping list of 12 brand names in Manrope 700 and the small disclaimer "Brand names belong to their owners; we are an independent service provider." Phones stack the label above the list.
9. **Service areas** (`.areas`): 1 : 1.15 grid on cream. On the left, h2 "Every barangay in Muntinlupa City", a "No transport fee" lead, then a 2-column `.area-list` of all 9 barangays with orange-ink pins and hairline separators (it stays 2 columns on phones). On the right, an embedded Google map in a 22px-radius frame with a navy `.map__card` overlay giving the address.
10. **Pricing** (`.price-grid`): 3 cards on white. General Cleaning from ₱800, Home Care Plan ₱2,400/yr (featured: 2px orange border plus a "Best value" pill flag), and Split-Type Installation from ₱5,500. Each has a big Anton price with a small "from/only" prefix and a ticklist. The featured card gets the orange button; the others are outline. "See the full price list" closes the section.
11. **FAQ** (`.faq`): an 860px column of `<details>` cards. The plus icon in a cream circle rotates 45° to an orange ×, and the open card gets an orange border. 4 questions, then "More answers".
12. **CTA band** (`.cta-band`): an abstract navy swoosh image under a 90° navy scrim. Anton caps "Hot room? We'll cool it down today." with "Same-day visits for bookings before 12 noon", an orange call button with the number, and a ghost "Request a quote". Buttons go full width on phones.
13. **Footer** (`.site-footer`): navy-900, 4 columns (1.4/1/1/1.2): brand + blurb + socials; Quick links; Services; Get in touch (mobile and landline, email, address, hours + "Emergency calls 24/7"). Orange icons and Anton caps column heads. 2 columns ≤1100px, 1 ≤640px.
14. **Mobile call bar** (`.mobile-bar`, ≤640px): a fixed 2-column bar with a navy "Call now" and an orange "Free quote". The body gets 72px bottom padding and the bar respects `safe-area-inset-bottom`.

At 14 blocks the homepage is well over the ~8-section guideline. Pricing and the FAQ also appear in full on `pricing.html`.

## Other page patterns
- **Page hero** (`.page-hero`, every inner page): a navy photo band with a 100° scrim, breadcrumbs (white links, "/" separators) and a mixed-voice Anton h1 ("Upfront prices. Straight answers.", "This page got lost in the ducts" on the 404), plus a `.accent` orange word option.
- **Services** (`services.html`): alternating `.service-row` (1 : 1.1 grid, image side flips on even rows, hairline dividers between rows). Each row has an Anton h2, a "From ₱…" line, and a `.chip-list` of what's included (white pills, nowrap, orange-ink icons). After that come a "Smaller jobs, same care" split, the brands strip, and a 4-step `.steps` grid where CSS counters draw orange Anton "01–04".
- **Pricing & FAQ** (`pricing.html`): plan cards, then a full `.price-table` (min-width 560px inside an `overflow-x: auto` wrapper; uppercase muted thead on cream; tabular nums; `.sub` second line per row) with `.fine-print`, then FAQ category chips (`.faq-cats`, anchor jumps) over three grouped `<details>` lists.
- **About** (`about.html`): story split, a navy `.stats` band (4 cells separated by 1px gaps on a 12% white grid background, orange Anton numbers), a 3-up `.team` grid (square photos, orange-ink uppercase roles), and a navy `.values` 4-up of translucent cards ("Four promises on every visit").
- **Service areas** (`service-areas.html`): barangay list + map, a "nearby cities" list (`.area-list--nearby`, lighter weight), and a property-types split.
- **Contact** (`contact.html`): a 1 : 1.4 `.contact-grid`. On the left, `.contact-cards`: phone (with Viber/Messenger `.chat-row` buttons), email, office, and an hours card with a right-aligned `.hours` table. On the right is the quote form, which goes 2 columns from 641px. A "Based in Alabang" map band follows.
- **404**: a 1:1 `.notfound` split with a giant orange Anton "404", an illustration and links back.

## Signature elements
- **Hot/cold skew stripe**: the orange 14px bar skewed −12° with a sky-blue `box-shadow` offset makes a two-tone cut between scrim and photo. On phones it becomes a 6px orange border under the photo. `assets/css/styles.css` › `.hero::after`, `.hero__media` (≤960px).
- **Icon badge straddling the photo seam** on service cards, which ties photo and body together. `styles.css` › `.card__icon`.
- **Overlapping stat badge** with a cream "cut-out" border on the about photo. `styles.css` › `.media-stack__badge`.
- **Anton numerals everywhere numbers matter** (prices, stats, step counters, 404), so the condensed face carries the price-led positioning. `styles.css` › `.price strong`, `.stats strong`, `.step::before`.
- **Locale-true content blocks**: the barangay list with pins next to a map card, the TESDA/DTI trust strip, Viber/Messenger contact, peso pricing. `index.html` › `.areas`, `.trust`; `contact.html` › `.chat-row`.
- **Navy-on-orange primary button**: the button text stays navy because white on this orange fails contrast. `styles.css` › `.btn`.

## Motion
Hand-built before the JS-only motion rule, so it **breaks current pipeline rules**:
- CSS `transition` throughout: `.btn` (.2s, with a translateY(-2px) hover lift), `.card` (.25s lift, 1.04 image zoom over .5s), nav links, the subnav dropdown (opacity/translate .18s), the mobile drawer (`transform .3s`), FAQ chevron rotation, and the header shadow. The easing is `--ease: cubic-bezier(.2,.7,.2,1)`. There's also `@keyframes spin` for the form spinner.
- Reveals: `assets/js/main.js` adds `.is-visible` through an IntersectionObserver (threshold .08, rootMargin −8% bottom) with a 0/70/140ms stagger, and the CSS transition does the 18px rise and fade over .6s. Each reveal **plays once** (`io.unobserve`), with no replay. Reduced motion shows everything at once.
- No parallax, no GSAP. Header gets `.is-scrolled` (shadow only) past 8px.
To reuse in a pipeline build, port the hover lifts and the drawer to `main.js` `morph()` and the reveals to the template's `REPLAY`.

## Reusable components
- **Topbar**: promo + contact meta, hides progressively. `styles.css` › `.topbar`.
- **Header**: sticky white, blur on `::before`, dropdown subnav, orange phone pill, slide-in drawer with backdrop ≤960px. `.site-header`, `.nav`, `.subnav`, `.nav-backdrop`.
- **Buttons**: orange primary with navy ink, navy, ghost (on dark), outline; 48px min height, uppercase 800. `.btn`, `.btn--navy`, `.btn--ghost`, `.btn--outline`. The primary carries an **orange glow shadow** `0 6px 18px -8px rgba(242,107,29,.7)`, which the no-coloured-glow rule now forbids.
- **Text link**: uppercase arrow link whose icon nudges diagonally on hover. `.link-arrow`.
- **Service card**: photo + straddling icon tile + whole-card link. `.card`, `.card__icon`.
- **Price card**: featured variant with an orange border and a pill flag. `.price-card--featured`, `.price-card__flag`.
- **Quote form**: icon-prefixed inputs on cream, sky focus ring `0 0 0 4px rgba(59,169,224,.2)`, inline errors, success/error panels, busy spinner. `.quote`, `.form-grid`, `.control`, `.field.has-error`, `.form-status`.
- **FAQ accordion**: `<details>` cards with a rotating plus. `.faq`.
- **Ticklist**: circle ticks, with a navy-section variant. `.ticklist`.
- **Chips**: nowrap pills with icons. `.chip-list`, `.chip`.
- **CTA band**: photo + scrim + headline + two buttons. `.cta-band`.
- **Footer**: 4 columns on navy-900 with an icon contact list and square socials. `.site-footer`, `.footer-contact`, `.socials`.
- **Mobile call bar**: fixed Call/Quote pair. `.mobile-bar`.

## How it went
- No PROJECT.md, critique scores or LESSONS.md entries exist for this site; it predates the pipeline.
- `Media/meta-ai-prompts-muntinlupa.md` ("v2: set in Muntinlupa") shows a mid-build correction: the first AI images looked like an American suburb (lawns, siding, ground-level condensers, sweaters) and were regenerated for Metro Manila. The hero and team shots were redone. **Three homepage service cards (installation, maintenance, emergency) still show US suburban houses and lawns**, the same authenticity problem the imagery rules warn about.
- Gaps measured against today's rules, worth knowing before you borrow from it:
  - **Photos repeat**: `service-maintenance.webp` appears on 4 pages, `service-emergency.webp` on 3, `service-ac-installation.webp` twice on `services.html`.
  - Google Fonts are linked rather than self-hosted.
  - `og:image` is relative (`assets/img/og-share.jpg`).
  - Display line-height is 1.02 (L-051 wants ≥1.05).
  - All motion is CSS transitions, and reveals don't replay.
  - The primary button has an orange glow.
  - The forms have an empty `data-endpoint`, so `main.js` simulates success (a demo mode).
  - Social links are bare platform URLs, and contact values are placeholders (0917 000 0000).
  - Placeholder text contrast is 3.36:1.
  - The homepage has about 14 blocks.
- Done well, and still the standard:
  - The quote form starts on an empty "Choose a service" option.
  - Every form states the reply time.
  - There's a tap-to-call bar on phones.
  - HVACBusiness JSON-LD is present.
  - The hero image is preloaded with a `srcset`.
  - White-on-orange was deliberately avoided (navy ink).
  - The brand strip uses names, not logos, with a disclaimer.

## Reuse guidance
**Fits:** urgent-need local trades where the visitor wants a number, a price and a time slot fast: aircon/HVAC, plumbing, electrical, pest control, appliance repair, roofing, locksmiths. It suits a dependable, no-nonsense mood more than a premium or craft one. Patterns that transfer: a condensed-caps hero with one diagonal brand stripe, a quote form as a floating card straight after the trust row, an icon badge straddling the photo seam on service cards, an area list beside a map card, homepage "from" prices with one featured plan, and the fixed Call/Quote bar on phones. Any brand whose CTA colour is a mid orange or yellow should use dark button text, as here.
**Keep to this site:** the flame-and-snowflake hot/cold pairing (orange + sky stripe) is Ironwood's identity, so don't copy navy/orange/sky plus the skewed double stripe as a set. The Muntinlupa barangay list, TESDA/DTI credentials and Viber/Messenger contact row are locale facts, not decoration. Also avoid copying the inspiration-derived skeleton whole (topbar, trust icons, 3×2 cards, brand strip, stat badge, FAQ, CTA band): stacked together it reads as a category template and fails the "cover the logo" test. Take one or two of these patterns and build the rest from the next client's own story.
