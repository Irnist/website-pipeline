"""Static site build.

    python _src/build.py        -> rebuilds dist/  (never edit dist/ by hand)

Page bodies: _src/pages/*.html. Shared chrome: _src/partials/. Business data,
page list and helpers: _src/site_config.py. Source images: assets/img/.

Template syntax (pages and partials):
    {{KEY}}                     BIZ value, plus derived PHONE_HREF, EMAIL_HTML, YEAR
    {{PAGE.key}}                current page's field (title, desc, file, body_class, ...)
    {{> name}}                  include _src/partials/name.html
    {{i:name}} {{i:name|cls}}   inline SVG from _src/icons/name.svg
    {{fn:name}} {{fn:name|arg}} helper output (built-ins below, or site_config.HELPERS)
"""
import hashlib
import html
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, DIST = ROOT / "_src", ROOT / "dist"
sys.path.insert(0, str(SRC))
import site_config as C  # noqa: E402

try:
    from PIL import Image
except ImportError:  # dimensions are a nicety; the build still works without Pillow
    Image = None

TOKEN = re.compile(r"\{\{\s*(.+?)\s*\}\}")
SOURCE_COMMENT = re.compile(r"<!--.*?-->[ \t]*\n?", re.S)
warnings = []
unresolved = {}  # token -> pages


def warn(msg):
    if msg not in warnings:
        warnings.append(msg)


# ---------------------------------------------------------------- business data
def biz_values():
    v = {k: str(val) for k, val in C.BIZ.items()}
    phone = v.get("PHONE", "")
    digits = re.sub(r"[^\d+]", "", phone)
    v["PHONE_HREF"] = f"tel:{digits}" if digits else ""
    email = v.get("EMAIL", "")
    # <wbr> before @ so long addresses break cleanly on phones
    v["EMAIL_HTML"] = html.escape(email).replace("@", "<wbr>@") if email else ""
    v["EMAIL_HREF"] = f"mailto:{email}" if email else ""
    v["YEAR"] = str(date.today().year)
    v["CTA_LABEL"], v["CTA_HREF"] = C.PRIMARY_CTA
    return v


BIZ = biz_values()


# ---------------------------------------------------------------- built-in helpers
def h_nav(page, arg=None):
    items = []
    for p in C.PAGES:
        if not p.get("nav"):
            continue
        current = ' aria-current="page"' if p["file"] == page["file"] else ""
        items.append(f'<li><a href="{p["file"]}"{current}>{html.escape(p["nav"])}</a></li>')
    return "<ul>" + "".join(items) + "</ul>"


def h_cta(page, arg=None):
    cls = f"btn btn-primary {arg}" if arg else "btn btn-primary"
    label, href = C.PRIMARY_CTA
    return f'<a class="{cls}" href="{href}">{html.escape(label)}</a>'


def h_hours(page, arg=None):
    if not C.HOURS:
        warn("HOURS is empty (footer/contact show nothing)")
        return ""
    rows = "".join(f"<dt>{html.escape(d)}</dt><dd>{html.escape(t)}</dd>" for d, t in C.HOURS)
    return f'<dl class="hours">{rows}</dl>'


def h_service_options(page, arg=None):
    if not C.SERVICES:
        warn("SERVICES is empty (contact form service select has no options)")
    return "".join(f'<option value="{html.escape(s)}">{html.escape(s)}</option>' for s in C.SERVICES)


WEB3FORMS = "https://api.web3forms.com/submit"


def form_backend():
    """FORM_ENDPOINT -> (backend, endpoint, key). "" demo | "netlify" | "web3forms:<access key>" | any POST URL
    that takes FormData and answers 2xx (Formspree, Getform, a Worker...)."""
    ep = (C.FORM_ENDPOINT or "").strip()
    if not ep:
        return "demo", "", ""
    if ep.lower() == "netlify":
        return "netlify", "/", ""
    if ep.lower().startswith("web3forms:"):
        return "web3forms", WEB3FORMS, ep.split(":", 1)[1].strip()
    return "url", ep, ""


def h_form_attrs(page, arg=None):
    backend, ep, _ = form_backend()
    if backend == "demo":
        warn("FORM_ENDPOINT is empty: forms run in demo mode (list at handoff)")
        return 'method="post" data-endpoint="" data-backend="demo"'
    if backend == "netlify":
        # Netlify finds the form in the deployed HTML by name + data-netlify; JS posts it url-encoded to /
        name = html.escape(arg or "contact")
        return (f'name="{name}" method="post" data-netlify="true" netlify-honeypot="bot-field" '
                f'data-endpoint="/" data-backend="netlify"')
    return f'action="{html.escape(ep)}" method="post" data-endpoint="{html.escape(ep)}" data-backend="{backend}"'


def h_form_fields(page, arg=None):
    """Hidden fields for the form backend, plus its spam trap (a visually hidden field people never fill;
    main.js drops a submission that fills it). Place it inside the <form>."""
    backend, _, key = form_backend()
    trap = {"netlify": "bot-field", "web3forms": "botcheck"}.get(backend, "_gotcha")
    out = [f'<input type="text" name="{trap}" class="sr-only" tabindex="-1" autocomplete="off" aria-hidden="true" data-trap>']
    if backend == "netlify":
        out.append(f'<input type="hidden" name="form-name" value="{html.escape(arg or "contact")}">')
    elif backend == "web3forms":
        if not key:
            warn("FORM_ENDPOINT 'web3forms:' has no access key after the colon")
        site = f"{C.BIZ['NAME']} website" if C.BIZ.get("NAME") else "website"
        out += [f'<input type="hidden" name="access_key" value="{html.escape(key)}">',
                f'<input type="hidden" name="subject" value="New message from the {html.escape(site)}">',
                f'<input type="hidden" name="from_name" value="{html.escape(site[0].upper() + site[1:])}">']
    return "".join(out)


def h_booking(page, arg=None):
    """A text link to an online booking page (Calendly, Cal.com, Google appointment schedule) when BOOKING_URL is set.
    A link, not a button: the primary CTA stays the one solid button (RULES.md › one primary CTA)."""
    url = getattr(C, "BOOKING_URL", "")
    if not url:
        return ""
    label = html.escape(arg or "Or pick a time online")
    return f'<p class="contact__booking"><a href="{html.escape(url)}" rel="noopener">{label} <span aria-hidden="true">↗</span></a></p>'


def h_canonical(page, arg=None):
    if not C.DOMAIN:
        return ""
    path = "" if page["file"] == "index.html" else page["file"]
    return f'<link rel="canonical" href="{C.DOMAIN.rstrip("/")}/{path}">'


# ---------------------------------------------------------------- local SEO
SEO = getattr(C, "SEO", {})
WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
DAY_ABBR = {d[:3].lower(): i for i, d in enumerate(WEEK)}
# profiles that count as sameAs when they appear as BIZ values (a Maps *search* link is not a profile)
PROFILE = re.compile(r"^https?://(www\.|m\.)?(facebook|instagram|tiktok|youtube|linkedin|x|twitter|yelp|pinterest)\.com/"
                     r"|^https?://(g\.page|business\.google\.com)/", re.I)


def absolute(path):
    """DOMAIN-absolute URL for a site path, or "" while DOMAIN is unknown."""
    if not path or not C.DOMAIN:
        return path if path.startswith(("http://", "https://")) else ""
    return path if path.startswith(("http://", "https://")) else f"{C.DOMAIN.rstrip('/')}/{path.lstrip('/')}"


def parse_days(label):
    """'Mon–Fri', 'Monday - Sunday', 'Sat & Sun', 'Weekdays', 'Every day' -> [day indexes], or None."""
    s = re.sub(r"[–—]|\b(to|through|thru)\b", "-", label.lower())
    if re.search(r"\b(every ?day|daily|7 days|all week)\b", s):
        return list(range(7))
    out = []
    for part in re.split(r",|&|/|\band\b", s):
        part = part.strip()
        if not part:
            continue
        if re.fullmatch(r"weekdays?", part):
            out += range(5)
            continue
        if re.fullmatch(r"weekends?", part):
            out += [5, 6]
            continue
        ends = [e.strip()[:3] for e in part.split("-")]
        if len(ends) > 2 or any(e not in DAY_ABBR for e in ends) or not all(
                re.fullmatch(r"[a-z]+\.?", e.strip()) for e in part.split("-")):
            return None
        a, b = DAY_ABBR[ends[0]], DAY_ABBR[ends[-1]]
        out += [d % 7 for d in range(a, b + 1 if b >= a else b + 8)]
    return sorted(set(out)) or None


def parse_time(t, meridiem=None):
    """'8', '8am', '8:30 a.m.', '18:00', 'noon' -> (hour, minute, had_am_pm) or None."""
    t = t.strip().lower().replace(".", "")
    if t in ("noon", "midday"):
        return 12, 0, True
    if t == "midnight":
        return 0, 0, True
    m = re.fullmatch(r"(\d{1,2})(?::(\d{2}))?\s*(am|pm)?", t)
    if not m:
        return None
    h, mi, ap = int(m.group(1)), int(m.group(2) or 0), m.group(3) or meridiem
    if ap:
        if h > 12:
            return None
        h = (h % 12) + (12 if ap == "pm" else 0)
    if h > 23 or mi > 59:
        return None
    return h, mi, bool(m.group(3))


def parse_hours(text):
    """'8:00 AM – 7:00 PM', '9-5pm', 'Open 24 hours', 'Closed' -> [(opens, closes)], [] when closed, or None."""
    s = text.lower().replace("–", "-").replace("—", "-")
    if re.search(r"24\s*(hours|hrs|h)\b|24/7", s):
        return [("00:00", "23:59")]
    if re.fullmatch(r"\s*closed\s*", s):
        return []
    spans = []
    for part in re.split(r",|&|\band\b", s):
        ends = re.split(r"\s*(?:-|\bto\b)\s*", part.strip())
        if len(ends) != 2:
            return None
        end = parse_time(ends[1])
        if not end:
            return None
        start = parse_time(ends[0])
        if start and not start[2] and end[2]:  # "8-5pm": the start takes pm only if that keeps it before the end
            pm = parse_time(ends[0], "pm")
            start = pm if pm and (pm[0], pm[1]) < (end[0], end[1]) else parse_time(ends[0], "am")
        if not start or (not start[2] and not end[2] and (end[0], end[1]) <= (start[0], start[1])):
            return None  # "9-5" with no am/pm: ambiguous, so don't guess
        spans.append((f"{start[0]:02d}:{start[1]:02d}", f"{end[0]:02d}:{end[1]:02d}"))
    return spans or None


def opening_hours():
    """HOURS as schema.org openingHoursSpecification. A row whose label isn't a day ('Last service job') is
    skipped; a day row whose hours can't be read drops the whole spec, so the schema never claims 'closed'."""
    specs = []
    for days, hours in C.HOURS:
        idx = parse_days(days)
        if idx is None:
            warn(f"JSON-LD: HOURS row '{days}' isn't a day range; left out of openingHours")
            continue
        spans = parse_hours(hours)
        if spans is None:
            warn(f"JSON-LD: can't read hours '{hours}' for '{days}'; openingHours left out (write e.g. '8:00 AM – 6:00 PM')")
            return []
        for opens, closes in spans:
            specs.append({"@type": "OpeningHoursSpecification", "dayOfWeek": [WEEK[i] for i in idx],
                          "opens": opens, "closes": closes})
    return specs


def local_business(page):
    biz = C.BIZ
    ld = {"@context": "https://schema.org", "@type": SEO.get("TYPE") or "LocalBusiness", "name": biz.get("NAME", "")}
    address = {k: v for k, v in {
        "@type": "PostalAddress", "streetAddress": biz.get("ADDR1", ""),
        "addressLocality": biz.get("CITY", ""), "addressRegion": SEO.get("REGION", ""),
        "postalCode": SEO.get("POSTAL_CODE", ""), "addressCountry": SEO.get("COUNTRY", ""),
    }.items() if v}
    same_as = list(dict.fromkeys([v for v in biz.values() if isinstance(v, str) and PROFILE.match(v)]
                                 + list(SEO.get("SAME_AS", []))))
    fields = {
        "url": absolute("/") if C.DOMAIN else "",
        "description": page.get("desc", ""),
        "telephone": biz.get("PHONE", ""),
        "email": biz.get("EMAIL", ""),
        "address": address if len(address) > 1 else None,
        "hasMap": biz.get("MAPS_URL", ""),
        "image": absolute(SEO.get("OG_IMAGE", "")),
        "logo": absolute(SEO.get("LOGO", "")),
        "priceRange": SEO.get("PRICE_RANGE", ""),
        "areaServed": [{"@type": "City", "name": a} for a in SEO.get("AREA_SERVED", [])],
        "sameAs": same_as,
        "openingHoursSpecification": opening_hours() if C.HOURS else [],
    }
    ld.update({k: v for k, v in fields.items() if v})
    data = json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{data}\n</script>'


def h_seo(page, arg=None):
    """Social meta (og:site_name/url/image, twitter:card) and, on the homepage, LocalBusiness JSON-LD."""
    out = [f'<meta property="og:site_name" content="{html.escape(C.BIZ["NAME"])}">'] if C.BIZ.get("NAME") else []
    if C.DOMAIN:
        path = "" if page["file"] == "index.html" else page["file"]
        out.append(f'<meta property="og:url" content="{html.escape(absolute(path) or absolute("/"))}">')
    og = SEO.get("OG_IMAGE", "")
    if og and not (ROOT / og.split("?")[0]).exists() and not og.startswith("http"):
        warn(f"SEO OG_IMAGE not found: {og}")
    elif og and C.DOMAIN:
        out.append(f'<meta property="og:image" content="{html.escape(absolute(og))}">')
        out.append('<meta name="twitter:card" content="summary_large_image">')
    if page["file"] == "index.html" and getattr(C, "LOCAL_BUSINESS", False):
        out.append(local_business(page))
    return "\n".join(out)


def h_favicon(page, arg=None):
    for name, kind in (("favicon.svg", "image/svg+xml"), ("favicon.png", "image/png"), ("favicon.ico", "image/x-icon")):
        if (ROOT / "public" / name).exists():
            return f'<link rel="icon" href="{name}" type="{kind}">'
    warn("no favicon: add public/favicon.svg made from the logo (browsers request /favicon.ico and log a 404)")
    return ""


GSAP_VENDOR = ROOT / "tools" / "vendor" / "gsap"


def gsap_plugins():
    """site_config.GSAP, minus names that aren't vendored (warned). [] = GSAP off."""
    plugins = []
    for name in getattr(C, "GSAP", []):
        if (GSAP_VENDOR / f"{name}.min.js").exists():
            plugins.append(name)
        else:
            warn(f"GSAP plugin '{name}' isn't in tools/vendor/gsap/ (left out); copy it from the gsap npm package's dist/")
    return plugins


def h_gsap(page, arg=None):
    """Script tags for GSAP core, the plugins in site_config.GSAP, then motion.js. Deferred scripts run in
    document order, so this goes after main.js in layout.html. Empty when GSAP is off."""
    if not getattr(C, "GSAP", []):
        return ""
    srcs = [f"assets/js/vendor/gsap/{n}.min.js" for n in ["gsap", *gsap_plugins()]] + ["assets/js/motion.js"]
    return "\n".join(f'<script src="{s}" defer></script>' for s in srcs)


HELPERS = {
    "nav": h_nav, "cta": h_cta, "hours": h_hours, "service_options": h_service_options,
    "form_attrs": h_form_attrs, "form_fields": h_form_fields, "booking": h_booking,
    "canonical": h_canonical, "seo": h_seo, "favicon": h_favicon, "gsap": h_gsap,
    **C.HELPERS,
}


# ---------------------------------------------------------------- rendering
def icon(name, cls=""):
    p = SRC / "icons" / f"{name}.svg"
    if not p.exists():
        warn(f"missing icon: _src/icons/{name}.svg")
        return ""
    attrs = f' class="icon{" " + cls if cls else ""}" aria-hidden="true" focusable="false"'
    return re.sub(r"<svg\b", "<svg" + attrs, p.read_text(encoding="utf-8").strip(), count=1)


def render(text, page, depth=0):
    if depth > 8:
        warn("include/helper nesting deeper than 8: check for a loop")
        return text
    # Source notes stay in the source: a token named in a comment would otherwise be expanded and ship
    # (the contact page's notes once shipped a second copy of the form's hidden fields).
    text = SOURCE_COMMENT.sub("", text)

    def sub(m):
        t = m.group(1)
        if t.startswith(">"):
            p = SRC / "partials" / f"{t[1:].strip()}.html"
            if not p.exists():
                warn(f"missing partial: {p.relative_to(ROOT)}")
                return m.group(0)
            return render(p.read_text(encoding="utf-8"), page, depth + 1)
        if t.startswith("i:"):
            name, _, cls = t[2:].partition("|")
            return icon(name.strip(), cls.strip())
        if t.startswith("fn:"):
            name, _, arg = t[3:].partition("|")
            if "{{" in arg:  # the token regex stops at the first }}, so a nested token truncates the call
                warn(f"token nested inside helper args (tokens don't nest; let the helper read BIZ): {{{{{t}}}}}")
                return m.group(0)
            fn = HELPERS.get(name.strip())
            if not fn:
                warn(f"unknown helper: {name.strip()}")
                return m.group(0)
            return render(fn(page, arg.strip() or None), page, depth + 1)
        if t.startswith("PAGE."):
            return str(page.get(t[5:], ""))
        if t in BIZ:
            if BIZ[t] == "":
                warn(f"BIZ value empty, left as placeholder: {{{{{t}}}}}")
                return m.group(0)
            return BIZ[t]
        return m.group(0)  # reported as unresolved below

    return TOKEN.sub(sub, text)


IMG_TAG = re.compile(r"<img\b[^>]*>", re.I)

# Responsive images: every local photo wider than the smallest step gets WebP copies at these widths
# (never wider than the source) and a srcset, so phones download phone-sized files (Lighthouse "image
# delivery", LCP). src keeps the original as the fallback. Opt out per tag with data-no-srcset.
# Copies are cached in .pipeline/img-cache and named by content hash, so a changed photo gets a new URL.
SRCSET_WIDTHS = (480, 800, 1200, 1400, 1600, 2000)  # 1400: Lighthouse's phone (412px @1.75x) wants ~1300 for heroes
WEBP_QUALITY = 74
IMG_CACHE = ROOT / ".pipeline" / "img-cache"
variants_made = {}  # source path -> [(width, site path)]


def webp_variants(path, site_path):
    """[(width, site path)] for the WebP copies of a local image, made on first use; [] to leave it alone."""
    if path in variants_made:
        return variants_made[path]
    out = []
    try:
        with Image.open(path) as im:
            alpha = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
            if alpha or im.width <= SRCSET_WIDTHS[0] or path.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
                variants_made[path] = []  # cut-outs and logos stay as they are (qa.py checks their edges)
                return []
            digest = hashlib.sha1(path.read_bytes()).hexdigest()[:8]
            widths = [w for w in SRCSET_WIDTHS if w < im.width] + [min(im.width, SRCSET_WIDTHS[-1])]
            rel = Path(site_path).parent / "_w"
            IMG_CACHE.mkdir(parents=True, exist_ok=True)
            for w in dict.fromkeys(widths):
                name = f"{path.stem}-{digest}-{w}.webp"
                cached = IMG_CACHE / name
                # An interrupted build once left a 0-byte cached WebP that every later build reused (L-059):
                # write to a temp name and rename, and treat an empty cache file as missing.
                if not cached.exists() or cached.stat().st_size == 0:
                    h = round(im.height * w / im.width)
                    tmp = cached.with_suffix(".tmp")
                    im.convert("RGB").resize((w, h), Image.LANCZOS).save(tmp, "WEBP", quality=WEBP_QUALITY, method=6)
                    tmp.replace(cached)
                target = DIST / rel / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(cached, target)
                out.append((w, (rel / name).as_posix()))
    except Exception as e:  # noqa: BLE001  (an unreadable image keeps its plain src)
        warn(f"srcset skipped for {site_path}: {e}")
        out = []
    variants_made[path] = out
    return out


def add_dims(markup, page_file):
    """Add width/height to <img> tags that lack them (prevents layout shift), plus a WebP srcset."""
    def fix(m):
        tag = m.group(0)
        src = re.search(r'\ssrc="([^"]+)"', tag)
        if not src or src.group(1).startswith(("http:", "https:", "data:")):
            return tag
        path = ROOT / src.group(1).split("?")[0]
        if not path.exists():
            warn(f"missing image in {page_file}: {src.group(1)}")
            return tag
        if Image is None:
            return tag
        extra = ""
        if " srcset=" not in tag and "data-no-srcset" not in tag:
            variants = webp_variants(path, src.group(1).split("?")[0])
            if variants:
                extra += ' srcset="' + ", ".join(f"{p} {w}w" for w, p in variants) + '"'
                if " sizes=" not in tag:
                    # Parallax photos are cover-cropped in frames up to ~a screen tall, so on phones they're drawn
                    # wider than the screen (Macz: 461-836px at 360x780/390x844 = 59-107vh; 90vh keeps every pick within
                    # 0.95-2x of the drawn width). Everything else defaults to
                    # 100vw; browser_qa.mjs flags any image whose pick is blurry or 2x too big, with a sizes hint.
                    extra += ' sizes="max(100vw, 90vh)"' if "data-parallax" in tag else ' sizes="100vw"'
        if " width=" not in tag:
            try:
                with Image.open(path) as im:
                    extra += f' width="{im.width}" height="{im.height}"'
            except Exception:
                pass
        return tag[:-1].rstrip("/").rstrip() + extra + ">" if extra else tag

    return IMG_TAG.sub(fix, markup)


def build_page(page, layout):
    page = dict(page)
    name = C.BIZ.get("NAME") or "{{NAME}}"
    title = page.get("title") or ""
    page["full_title"] = title if page["file"] == "index.html" and title else (
        f"{title} | {name}" if title else name)
    for key in ("title", "desc"):
        if not page.get(key) and page["file"] != "404.html":
            warn(f"{page['file']}: empty meta {key}")
    src = SRC / "pages" / page["src"]
    if not src.exists():
        warn(f"missing page source: {src.relative_to(ROOT)}")
        return None
    page["body"] = render(src.read_text(encoding="utf-8"), page)
    out = add_dims(render(layout, page), page["file"])
    for t in dict.fromkeys(TOKEN.findall(out)):
        unresolved.setdefault(t, []).append(page["file"])
    return out


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    keep = shutil.ignore_patterns(".keep")
    shutil.copytree(ROOT / "assets", DIST / "assets", ignore=keep)
    public = ROOT / "public"
    if public.exists():
        shutil.copytree(public, DIST, dirs_exist_ok=True, ignore=keep)
    if (ROOT / "_headers").exists():
        shutil.copy2(ROOT / "_headers", DIST / "_headers")

    layout = (SRC / "partials" / "layout.html").read_text(encoding="utf-8")
    # GSAP (optional): ship core + the chosen plugins + motion.js only when site_config.GSAP lists plugins
    if getattr(C, "GSAP", []):
        vendor = DIST / "assets" / "js" / "vendor" / "gsap"
        vendor.mkdir(parents=True, exist_ok=True)
        for name in ["gsap", *gsap_plugins()]:
            if (GSAP_VENDOR / f"{name}.min.js").exists():
                shutil.copy2(GSAP_VENDOR / f"{name}.min.js", vendor)
            else:
                warn("tools/vendor/gsap/gsap.min.js missing: copy tools/vendor/gsap/ from the pipeline template")
        if not (ROOT / "assets" / "js" / "motion.js").exists():
            warn("GSAP is on but assets/js/motion.js is missing: copy it from the pipeline template")
        if "fn:gsap" not in layout:
            warn("GSAP is on but layout.html has no {{fn:gsap}} after main.js: no GSAP scripts load")
    else:
        (DIST / "assets" / "js" / "motion.js").unlink(missing_ok=True)
    built = []
    for page in C.PAGES:
        out = build_page(page, layout)
        if out is not None:
            (DIST / page["file"]).write_text(out, encoding="utf-8")
            built.append(page["file"])

    if C.DOMAIN:
        base = C.DOMAIN.rstrip("/")
        urls = "".join(
            f"<url><loc>{base}/{'' if f == 'index.html' else f}</loc></url>"
            for f in built if f != "404.html")
        (DIST / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>'
            f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>',
            encoding="utf-8")
    # robots.txt never blocks the site: previews stay out of search through the X-Robots-Tag header in
    # _headers, and a crawler blocked by robots.txt can't see that noindex. public/robots.txt overrides this.
    if not (DIST / "robots.txt").exists():
        lines = ["User-agent: *", "Allow: /"]
        if C.DOMAIN:
            lines += ["", f"Sitemap: {C.DOMAIN.rstrip('/')}/sitemap.xml"]
        (DIST / "robots.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    if getattr(C, "LOCAL_BUSINESS", False) and not getattr(C, "SEO", None):
        warn("site_config.py has no SEO dict: copy it from the pipeline template (LocalBusiness JSON-LD needs it)")

    for t, pages in unresolved.items():
        if BIZ.get(t) != "":  # empty BIZ values were already reported once
            warn(f"unresolved {{{{{t}}}}} in {', '.join(pages)}")
    print(f"built {len(built)} pages -> dist/")
    for w in warnings:
        print("  !", w)


if __name__ == "__main__":
    main()
