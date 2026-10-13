# Published client sites (real businesses, live)

These four are real, published client sites that the user worked on. They are documented here as a quality and layout reference only. Reuse layout ideas, section rhythm and the quality bar; never reuse their copy, business names, logos, photos, phone numbers, review quotes, warranty terms, discounts or any other claims, not even in a portfolio sample. Sources: full-page desktop captures in `Published Live Websites/<site>/SS 1.png` (2560 px wide, 2x of a 1280 viewport), cropped strips in `design-library/shots/`, and the live HTML/CSS fetched on 2026-10-10. Three of the four (Aurora, Children Matter, Macon) are built on Duda (`irp.cdn-website.com`, `dm-` classes); Parker is WordPress + Elementor from an auto-repair marketing agency. Hex values marked "CSS" were read from the live stylesheets; values marked "approx." were sampled from the screenshot. Where a section looks empty in a capture, it is usually a lazy widget or scroll animation that didn't fire, and it's noted as such.

---

## Aurora Plumbing (auroraplumbing.com, Seattle WA)

Shot: `design-library/shots/aurora-plumbing.webp`

### Identity
A 1960-founded neighbourhood plumbing store that is also a supply counter, parts department and fixtures showroom. The site reads like the business: a little old-fashioned, plain-spoken, loud about phone numbers and discounts, proud of its age. Mood: **heritage, neighbourly, no-nonsense, retail-counter, patriotic navy and red**.

### Palette
- Navy `#1e2964` (CSS, rgb 30,41,100): nav bar, buttons, headings, footer sub-bar
- Pure red `#ff0000` (CSS): "Leave us a Google Review" pill, inline "Reach out" links, FAQ chevrons, the "Celebrating over 60 years" line
- Black `#000000` (approx.): main footer
- Light grey `#eeeeee` / `#f7f7f7` (approx./CSS): service-card fill and FAQ rows
- White page, black body text

### Typography
- Headings: **Poppins 700**, uppercase on most section heads (CSS)
- Body: **Inter** (CSS), about 15–16px, generous line height
- The logo is a wide condensed wordmark in a rounded navy box with "Supply · Installation · Service" underneath; the header treats it like a storefront sign.

### Homepage anatomy
1. **Utility header**: three columns on white. Left: "Come visit today" + underlined address + "View our photo gallery" navy pill. Centre: logo lockup with tagline above ("Modern Ideas, Old Fashioned Values") and "Celebrating over 60 years" in red italics below. Right: "Call us now" + big red phone number, social icons, red "Leave us a Google Review" pill. A plunger-with-sign mascot illustration sits beside the logo. Floating round navy icon buttons (email, map, review) are pinned to the right edge.
2. **Navy nav bar**: full width, centred uppercase links with dropdowns (Interior Plumbing, Sewer & Drain, Showroom, Parts, Company, Blog, Reviews, Gallery, FAQ, Contact).
3. **Hero**: their own street sign photographed against the sky, full bleed, about 410px tall at 1280. Centred uppercase italic headline quoting what customers say ("We hear it all the time…"), then three stacked offer lines (dollar-off coupon, senior and military discounts), then a single navy "Call us today" button.
4. **Intro**: centred H1 "Plumbers in [city]" + H2 "Locally owned since 1960", then two long paragraphs in a narrow column.
5. **Four service cards in a 2×2 grid**: thin navy outline, grey fill, line icon, uppercase title, centred paragraph, navy "Learn more" button. In-home services, Parts department, Fixtures showroom, Sewer & drain.
6. **SEO text block**: "Your plumbing needs covered", three paragraphs.
7. **Stock photo + FAQ accordion**: one wide stock photo (plumber, red gloves), then five grey accordion rows with red circular chevrons, questions in uppercase navy.
8. **"Advantages of hiring professionals"**: paragraph + bolded-lead bullet list + a second stock photo.
9. **Closing CTA paragraph**: "Get reliable products and expert help today" with an inline red phone number and contact link.
10. **Footer**: black. Repeated nav, then three columns: phone/address/card logos/Energy Star badge | dispatch hours and retail hours as aligned two-column tables | trade-association, PHCC and BBB badges. A navy strip below holds the copyright notice. A "Let's Talk!" call popup sits bottom right.

### Signature elements
- **The real street sign as the hero image.** The business's own landmark does the branding; no stock photo could.
- **Customer-quote headline** ("We should have come here first!") instead of a generic promise.
- **Two-sided utility header**: "visit us" on the left and "call us" on the right, with the logo as a storefront sign between them. It suits a business that has both a counter and a service van.
- **Dispatch hours vs. retail hours** shown as two separate mini-tables in the footer. That's a real-world detail most templates miss.
- Trade-membership badges grouped in the footer as quiet proof.

### What works / what's dated
Works: the owned photography in the hero; heritage claims stated plainly and early ("since 1960"); phone number visible in three places above the fold; FAQ answers real buyer questions (cost, fixture choice, water heaters); split hours table.
Dated or weak: centred everything, with long grey paragraphs in a narrow column; the page goes text, cards, text, stock, text, so there's little visual rhythm. Two generic stock plumbers (one in a staged white bathroom) undercut the authentic hero. Pure `#ff0000` clashes with the navy and reads as alarm. Too many competing CTAs: gallery pill, review pill, call button, floating icons, popup. The 2×2 icon-card grid is the template pattern our rules warn against. The coupon lines in the hero are discount-dealer language. Uppercase italic hero type with a text-shadow over a busy sign photo struggles for contrast.

### Reuse guidance
Fits long-established trade businesses with a physical counter or showroom plus field service: plumbing and electrical supply, hardware, HVAC, appliance repair, locksmiths. Borrow the owned-landmark hero, the customer-quote headline, the visit/call split header (modernised: one row, not three stacked columns) and the split hours table. Replace the stock photos with real counter, van and crew shots; use one red accent, not a pure-red alarm colour; and swap the 2×2 cards for a story-led services list.

---

## Children Matter TX (childrenmattertx.org, San Antonio TX)

Shot: `design-library/shots/children-matter.webp`

### Identity
A nonprofit family life centre offering supervised visitation and parent coaching as a homelike alternative to institutional visitation. The site is warm and hopeful but has to stay calm and trustworthy for families in custody situations, courts and donors. Mood: **hopeful, gentle, colourful but disciplined, community-funded, reassuring**.

### Palette
Four brand stripes taken from the logo's hands, used as the CTA system:
- Green `#1c8367` (approx.; CSS has close values): "Sponsor", Godparent panel, testimonial gradient end
- Sky blue `#69c3ec` (CSS): "Donate"
- Red `#d22d2f` (CSS rgb 210,45,47; sampled `#d02c30`): "Volunteer", popup buttons
- Mid blue `#1271b0` (CSS): "Events", quote band, headings
Supporting:
- Off-white page `#f7f7f7` (CSS), white cards with soft large shadows
- Deep indigo `#070134` (approx.): "We Offer" band
- Slate-blue `#5c6f9a` (approx.): carousel cards on the indigo band
- Footer navy `#08486c` (CSS rgb 8,72,108)
- Cream `#f5f0ea` (approx.): Godparent panel
- Testimonial band gradient: pale sky `#b7e2ff` to green `#1f856b` (approx.)

### Typography
- **Poppins** for headings, nav chips and body (in the page HTML; matches the capture). Bold for chips and hero lines, light/regular for card headings like "Children Matter Family Life Center". Roboto is loaded but barely visible.
- The Godparent program has its own rounded logotype with a figure replacing the "u", and a lowercase tagline "protect, rebuild, empower".

### Homepage anatomy
1. **Hero with integrated nav**: full-bleed photo of a child on a bike under a blue-to-red diagonal colour wash, about 390px tall. Logo top left. Top right: small text links (About, Contact, Testimonials, Careers, Referrals) separated by dots, and below them **four solid colour chips** (Sponsor, Donate, Volunteer, Events) as the primary nav. Three-line bold headline right-aligned under the chips: "Protect Children, Rebuild Families, and Empower Caregivers".
2. **Family photo intro**: a rounded-corner family photo offset right on the grey page. The left column is empty in the capture (probably a scroll animation that didn't fire).
3. **Quote band**: full-width mid-blue band with a centred Paulo Coelho quote in light white type.
4. **"Who are we?"**: a centred blue heading, then a **diagonal ribbon of the four brand stripes** running across the section behind a white card. The ribbon ends labelled Sponsor / Donate / Volunteer / Events. The card lists the service as safe, comfortable and homelike, with small icons.
5. **"Children First" card**: a second white card offset right, with a research claim and two icon bullets.
6. **"We Offer" carousel**: deep indigo band with large slate-blue cards (Parent Coaching, Supervised Visitation) in a left/right arrow slider. Green titles, bullet lists, green pill "Learn more" buttons.
7. **"Our Impact"**: a heading and a wide photo or video block, greyed in the capture (likely a lazy video).
8. **Testimonial**: a diagonal sky-to-green gradient band with one large white rounded quote card, a round photo avatar overlapping its corner and a star row.
9. **Godparent donor panel**: a boxed two-tone panel (green left, cream right) with a black-and-white child portrait straddling the seam, the program logotype, a short pitch for monthly giving, then a solid green pill and an outline green pill.
10. **Supporters**: logo wall of local business and county sponsors under a blue heading with a thin rule, then a "Thank you to our generous supporters" line.
11. **Memberships**: transparency seal and nonprofit council badges.
12. **Footer**: navy, three columns (Browse links | contact, mailing address, payment and giving methods (Venmo, Amazon Wishlist, Item donations), state-contract note | hours table with a note on appointment-only days). A white strip below carries the copyright and legal links. A "Thanks for stopping by" popup sits bottom right.

### Signature elements
- **Four colour-coded action chips as the main nav.** Each way to help has its own colour, and the colours come from the logo.
- **The diagonal four-stripe ribbon** that carries those same colours and labels through the "Who are we?" section. It's the brand system turned into a graphic.
- **A named giving program with its own mini-brand** (Godparent). The ask becomes an identity, with primary and secondary pill buttons.
- A **split two-tone panel with a photo straddling the seam**.
- Giving channels beyond money (wishlist, item donations, Venmo) listed in the footer.

### What works / what's dated
Works: the brand colours turn into a navigation and CTA system instead of decoration; the ribbon is ownable; the donor panel is a polished, self-contained block; warm, inclusive family photography; the gentle grey page with white floating cards suits the subject.
Weak: the hero is short and the headline is small for the space. Four saturated chips plus text links plus a popup compete. The sky-blue "Donate" chip with white text fails contrast (about 2:1). The quote band uses a famous-author quote instead of the organisation's own voice. Carousel cards on the indigo band are low contrast (slate on indigo, green titles on slate). The empty or greyed blocks in the capture show reliance on animations and lazy embeds that can leave holes. Sponsor logos of mixed quality (one bright yellow storage sign) break the calm. The page runs about 4,700px at 1280 wide with many single-idea sections.

### Reuse guidance
Fits nonprofits, family services, youth programs, community centres, churches, schools and any organisation with several distinct "ways to help". Borrow the colour-per-action chip system (with contrast-checked colours: darken the light blue or use dark text), the logo-derived stripe motif as a section graphic, and a branded recurring-giving panel. Replace the borrowed quote with the organisation's own words, and make the hero taller with a larger headline.

---

## Macon Supply (maconsupply.net, Billings MT plus branches)

Shot: `design-library/shots/macon-supply.webp`

### Identity
A 50-year construction supply distributor for professional contractors across several states, carrying concrete, forming and roofing products. The site is a straight-talking trade counter: product categories, brands carried, branches, credit application. Mood: **industrial, regional, sturdy, pro-to-pro, heritage badge**.

### Palette
- Royal navy `#093075` (CSS): header, headline text, bottom band
- Brick/crimson red `#a2001a` (CSS `--color_1`): pill buttons, category labels, footer links
- Near-black blueprint `#091827` (approx.): dealer panel background
- White page; black body text
- The logo adds a brighter red script and a blue "50 Years" ribbon.

### Typography
- Headings: **Russo One** (CSS), a squared, techno-industrial display face, used large for the hero and the regional H2
- Body: **Open Sans** (CSS) at 15px
- Nav: Open Sans uppercase, small and spaced

### Homepage anatomy
1. **Navy header**: oval anniversary logo (red script on white with a "50 Years" ribbon) on the left; centred uppercase nav (Products, Manufacturers, Request a Quote, Line Card, Locations, Contact) with two red pills below it ("Now Hiring", "Credit Application"); phone pill, address and social icons on the right.
2. **Hero**: wide photo of crews on rebar, overhead with long shadows, about 310px tall. Russo One headline "…Serving the construction industry since 1976" and one red "Call us today" button.
3. **Overlapping intro card**: a white panel rises into the hero bottom and holds the big navy H2 naming the five states and regions served, then a paragraph listing the branch towns and the size of the catalogue.
4. **Product category grid**: 4-column grid of small square product photos (finishing, chemical buckets, forming panels, roofing, rebar…) with a check-circle icon and a red label under each. Ten categories, so the last row is ragged.
5. **Authorised-dealer split**: a big partner-brand logo on white (left half) beside a dark blueprint-texture panel (right half) with the "only authorised dealer in the state" statement.
6. **Brands-carried logo strip**: one row of about eight manufacturer logos.
7. **Review prompt**: "Click the logos below to read or leave a review" with Yelp and Google logos.
8. **Two review cards**: Facebook and Google quotes in white shadow cards with icon, stars, quote and initial-name.
9. **Media band**: an aggregate-plant photo background holding an embedded YouTube "Small Business Spotlight" video and a live Facebook page feed.
10. **Footer**: navy band, then the logo centred overlapping the band edge, repeated nav, card logos, social icons, a sister-company logo, a legal line, and a "Leave details" popup bottom right.

### Signature elements
- **The intro card overlapping the hero**: the regional-coverage statement sits on a white panel that bites into the photo, so the hero and the "who we serve" answer read as one unit.
- **Region-as-headline**: the H2 is literally the list of states served. For a distributor, coverage is the main buying question, and it's answered in the second beat.
- **Trade-first header actions**: "Credit Application" and "Now Hiring" as header pills. Pro customers need credit accounts; that's a real B2B entry point.
- **Blueprint-texture dealer panel** next to the partner logo.
- An anniversary badge logo carrying the heritage.

### What works / what's dated
Works: Russo One plus navy and crimson feels right for construction without clichés like hazard stripes; the overlapping coverage card; category grid with real product photos is fast to scan; credit application and quote request are surfaced for trade buyers; the brand strip answers "do you carry X?".
Weak: the hero is short and the photo is busy (yellow forms behind white type). Category thumbnails are tiny, and the 10-item grid leaves orphans. The page leans on third-party logos (manufacturers, Yelp, Google, Facebook, YouTube) as its main visuals, so the business's own yard, trucks and staff never appear. The embedded Facebook feed and YouTube box look like 2015 widgets. There's no closing CTA beat before the footer. Light grey review cards and centred small text feel generic.

### Reuse guidance
Fits B2B distributors and trade suppliers: building materials, electrical and plumbing wholesale, equipment rental, landscape supply, ag supply. Borrow the overlapping coverage card, region-as-H2, the square-ish display face on navy, the category grid (bigger tiles, a complete grid), and credit and quote actions in the header. Replace the widget band with real yard, branch and fleet photography, and add a closing "open an account / request a quote" section.

---

## Parker Auto AZ (parkerautoaz.com, Tucson AZ)

Shot: `design-library/shots/parker-auto.webp`

### Identity
An independent auto repair and service centre open since 1995, selling trust: certified techs, a nationwide parts-and-labour warranty, rewards, shuttle and after-hours drop-off. It's the most "modern template" of the four: dark chrome header, electric-blue accents, a techy display font. Mood: **technical, clean, confident, sunbelt-bright, dealership-adjacent**.

### Palette
All from the Elementor global kit (CSS):
- Electric blue `#0096FF`: primary, buttons, eyebrows, icons, diagonal corner block
- Ink navy `#0E111B`: top bar, header, testimonial band, footer
- Text grey `#424649`
- Pale periwinkle `#F0F3FF`: services section background
- Cool greys `#E5EBEE` / `#BAC4C9`; panel navy `#171C2B`

### Typography
- Display: **Bai Jamjuree 700** (CSS), a squarish Thai-Latin grotesk with a tech/automotive edge. Global H1 85px with line-height 1em; H2 52px at 1.2.
- Body: **Sarabun 400** at 16px / 1.6 (CSS)
- Eyebrows: small uppercase blue with letter-spacing, above almost every heading
- Loaded from fonts.googleapis.com (not self-hosted)

### Homepage anatomy
1. **Top bar** (ink): "Book appointment" blue button, address with pin icon, hours with clock icon (two lines), social icons.
2. **Header** (ink): an italic outlined wordmark logo, small uppercase nav with dropdowns, and a big blue phone button on the right.
3. **Hero**: full-bleed photo of **their own street sign and building under palms and blue sky**, darkened; left-aligned eyebrow, a four-line headline combining city, year founded and warranty, an uppercase sub-line, a blue "Book appointment" button and a round phone icon with "Give us a call" and the number.
4. **About split**: left is a photo of their storefront (brand names on the glass) with a white "29+ years of service" stat badge overlapping its top-left and a small inset photo overlapping its bottom-right. Right is an eyebrow, H2, paragraph and a "Our credentials" check-list.
5. **Warranty & rewards band**: a lift-bay photo with a dark overlay, a centred headline, the rewards maths in plain words, and a blue "financing options" button.
6. **"Who we are"**: centred heading, a scrollable text box (fixed height with an inner scrollbar) for SEO copy, and a 5-photo strip of the real shop (exterior, waiting room, staff, building, front desk). A big **blue diagonal triangle** fills the lower-right corner.
7. **Services**: periwinkle section. Left is an eyebrow, H2 and two buttons (All services in blue, All vehicles in ink); right is another scroll box. Then a **vehicle-make logo carousel** with a progress rule, then a 3-column grid of service cards (blue square icon tab overhanging the top-left, uppercase spaced title, excerpt, "Learn more", photo at the bottom of the card).
8. **Why choose us**: left is an eyebrow, H2, paragraphs, parts-brand logos and an 8-item check list (shuttle, after-hours drop-off, financing…); right is an interior photo with an overlapping inset photo.
9. **Contact band**: their building exterior with a dark overlay, a centred headline, paragraph and a "Book appointment" button.
10. **Testimonials**: ink band with eyebrow and heading. The review widget is empty in the capture.
11. **Blog**: "Our latest posts" with a "View all posts" button: one large feature card on the left and two horizontal cards stacked on the right.
12. **Greyscale Google map**, full width.
13. **Footer** (ink): logo, phone, address and hours with blue line icons, follow icons; "Schedule an appointment today" plus a button across the top right; Quick links and a two-column services list.

### Signature elements
- **Owned-building photography throughout**: the hero sign, the storefront with make names on the glass, the waiting room, the front desk and the exterior in the contact band. The shop itself is the brand.
- **Stat badge plus inset photo overlapping a storefront photo**: a layered "collage" about block.
- **Service cards with an overhanging square icon tab** and the photo at the card's foot.
- **Vehicle-make carousel** answering "do you work on my car?".
- **Greyscale map** before the footer, so the map matches the dark/blue system instead of fighting it.
- Warranty and rewards maths written out in plain numbers.

### What works / what's dated
Works: strongest owned imagery of the four; it answers buyer questions (warranty, financing, shuttle, after-hours drop-off, makes serviced, hours in the top bar); one CTA ("Book appointment") repeated consistently plus the phone number; disciplined two-colour system with a real dark/light rhythm; the type pair has character without hurting legibility.
Weak: eyebrow-above-every-heading and "Why Choose Us?" are stock agency-template patterns; scroll-in-a-box text areas are a dated SEO trick and bad on mobile; the hero headline's 1em line height is tight; the diagonal blue triangle is decorative noise; the testimonials band is an empty shell when the widget fails; brand logos (car makes, parts brands) are heavy; the page is long (about 4,240px at 1280) with the credentials list repeated in two sections; Google Fonts are hot-linked.

### Reuse guidance
Fits auto repair, tyre shops, collision centres, motorcycle service, fleet maintenance, HVAC or appliance service with a physical shop. Borrow the owned-building hero, the top utility bar with hours and address, the overlapping stat-badge collage, service cards with an icon tab and photo, a "makes/brands we service" strip, and the greyscale map. Drop the eyebrows, the scroll boxes and the diagonal triangle; self-host the fonts; keep the credentials in one place; and give testimonials a static fallback.
