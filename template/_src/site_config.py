"""Per-project data for the build. Everything business-specific lives here.

Any BIZ key can be used in pages and partials as {{KEY}}. Leave unknown values
as "": the build keeps them as visible {{KEY}} placeholders and QA lists them.
"""

BIZ = {
    "NAME": "",        # exactly as the client writes it
    "TAGLINE": "",
    "PHONE": "",       # display format, e.g. (412) 555-0134
    "EMAIL": "",
    "ADDR1": "",       # street
    "ADDR2": "",       # city, state ZIP
    "CITY": "",        # short locale used in copy and meta, e.g. "Pittsburgh"
    "MAPS_URL": "",    # Google Maps link for the address
    # Shown above the form's submit button: who replies, how fast, what happens next.
    # e.g. "Anthony reads every message and replies within one business day with a few questions and a rough range."
    # Client mode: the client confirms the response time; it's a promise.
    "NEXT_STEPS": "",
}

# (days, hours). Rendered by {{fn:hours}} as an aligned, non-wrapping grid.
HOURS = []

# Service names for the contact form's "Service" select ({{fn:service_options}}).
SERVICES = []

# The one primary CTA sitewide: (label, href). Every other button is ghost or a text link.
PRIMARY_CTA = ("Get a quote", "contact.html")

# Where the contact form goes. No backend code needed for any of these:
#   ""                      demo mode: the form says it isn't connected yet; QA lists it at handoff
#   "netlify"               Netlify Forms (Deploy host: netlify only). Submissions + email alerts in the
#                           Netlify dashboard; deploy.py checks Netlify registered the form.
#   "web3forms:<key>"       Web3Forms (free, any host). The inbox owner gets the key by entering their email at
#                           web3forms.com; messages go to that inbox. The key is public by design.
#   "https://formspree.io/f/abcd1234" (or any URL that takes a FormData POST and answers 2xx)
# A real inbox is the client's call: never wire one up without the user's go-ahead (RULES.md › Ask only).
FORM_ENDPOINT = ""

# Online booking page (Calendly, Cal.com, Google appointment schedule). Shown on the contact page as a text
# link next to the call button by {{fn:booking}}; "" shows nothing.
BOOKING_URL = ""

# GSAP scroll motion (BRIEF.md "GSAP motion: yes"). [] = off: the site ships only main.js. Otherwise the
# GSAP plugins this site uses, e.g. ["ScrollTrigger", "SplitText"]. The build copies gsap core plus these
# from tools/vendor/gsap/ (self-hosted, never a CDN) and loads them, then assets/js/motion.js, after main.js.
# Vendored: ScrollTrigger SplitText Flip DrawSVGPlugin MotionPathPlugin MorphSVGPlugin Observer ScrollToPlugin CustomEase.
# Not ScrollSmoother: it takes over scrolling and breaks main.js parallax; only if the user asks for it.
GSAP = []

# https://www.example.com once the real domain is known; enables canonical links, sitemap.xml,
# og:url/og:image and the JSON-LD url (all need absolute URLs).
DOMAIN = ""

# Local businesses must have a tap-to-call link in the header (checked by tools/qa.py),
# and get schema.org LocalBusiness JSON-LD on the homepage (built from BIZ, HOURS and SEO below).
LOCAL_BUSINESS = True

# Local SEO extras for {{fn:seo}} (head.html). Leave unknowns as "" or []: they're simply left out.
# Facts only in client mode, like everything else (no price range or area the client didn't give).
SEO = {
    "TYPE": "LocalBusiness",  # most specific schema.org type that is true: AutoRepair, HVACBusiness,
                              # HomeAndConstructionBusiness, FurnitureStore, MotorcycleDealer, ...
    "REGION": "",             # state/province, e.g. "PA" or "Metro Manila"
    "POSTAL_CODE": "",
    "COUNTRY": "",            # ISO code, e.g. "US", "PH"
    "PRICE_RANGE": "",        # e.g. "$$"
    "AREA_SERVED": [],        # towns/cities served, e.g. ["Pittsburgh", "Mt. Lebanon"]
    "SAME_AS": [],            # official profiles not already in BIZ (Google Business Profile link, Yelp, ...).
                              # Social URLs in BIZ (Facebook, Instagram, ...) are added automatically.
    "OG_IMAGE": "",           # share image, ~1200x630, e.g. "assets/img/og.jpg"; made absolute with DOMAIN
    "LOGO": "",               # e.g. "assets/img/logo.png" (raster; made absolute with DOMAIN)
}

# Template patterns qa.py blocks, allowed only when the client asked for them: {"marquee": "why"}.
ALLOW_PATTERNS = {}

# Images knowingly used more than once (e.g. listing preview + full listing). Tell the user.
ALLOW_REPEAT_IMAGES = []

# Wording knowingly repeated on several pages (8+ identical words in <main>, flagged by qa.py, L-009),
# e.g. the NEXT_STEPS promise on the contact form and an FAQ. Each idea once; list only what must repeat.
ALLOW_REPEAT_TEXT = []

# Page list, in nav order. nav=None keeps a page out of the menu.
# src is the body file in _src/pages/. Optional keys: body_class, extra_head.
PAGES = [
    dict(file="index.html", src="home.html", nav="Home", title="", desc=""),
    dict(file="contact.html", src="contact.html", nav="Contact", title="Contact", desc=""),
    dict(file="404.html", src="404.html", nav=None, title="Page not found", desc=""),
]

# Project-specific render helpers, used in pages as {{fn:name}} or {{fn:name|arg}}.
# Each takes (page, arg) and returns HTML (which may itself contain tokens).
# Overrides the built-in helpers in build.py with the same name.
HELPERS = {}
