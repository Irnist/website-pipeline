"""Self-test for the shared QA tools: every check must fire on a planted defect and stay quiet on a clean site.

    python dev/selftest.py                 qa.py only (~10s)
    python dev/selftest.py --browser       + browser_qa.mjs on one page (no Lighthouse, ~1 min)
    python dev/selftest.py --site "<finished site>"    another clean base (default: Gadget Zone)

Copies the base site twice into <workspace>/_temp/selftest/ (the original is only read): `clean` must report 0
errors, `broken` gets every defect below and must report each one. Checks have gone silent before without anyone
noticing: browser QA reported 0 errors while motion.js had crashed (L-048), and the L-071 check missed `this`
in ScrollTrigger callbacks; a false positive (the data-todo attribute read as TODO) padded every handoff.
When you add a check, add its defect here (SKILL.md › Handoff › Lessons). Exit 1 if anything fails.
"""
import re
import runpy
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
PIPELINE = Path(__file__).resolve().parent.parent
WORKSPACE = PIPELINE.parent.parent
WORK = WORKSPACE / "_temp" / "selftest"
BASE = WORKSPACE / "Concept Websites" / "Gadget Zone Website"
SKIP = shutil.ignore_patterns("qa", ".git", ".wrangler", ".netlify", "node_modules", "__pycache__")

# Planted into one qa-only page of `broken` (before </main>). (expected report line regex, why)
QA_MARKUP = """
<h1>Selftest second h1</h1>
<img src="assets/img/selftest-missing.webp">
<img alt="Selftest image without src">
<img src="https://images.example.org/selftest.jpg" alt="Hotlinked">
<a href="#">Selftest dead link</a>
<a class="btn" href="{cta_href}">Selftest other label</a>
<select name="selftest_budget"><option>Under 1k</option><option>1k and up</option></select>
<select name="selftest_pick"><option value="">Choose…</option><option value="a" selected>A</option></select>
<select name="selftest_reply" data-requires-phone="Phone call"><option value="">Choose…</option><option>Phone call</option><option>Email</option></select>
<form action="mailto:selftest@example.org"><input name="name"><input name="phone" type="text"><textarea name="message"></textarea><button>Send</button></form>
<a href="tel:+15550109876">Selftest other phone</a>
<p>Write to selftest@example.org any time.</p>
<p>Hi, I'm interested in the null</p>
<div class="marquee">Selftest marquee</div>
<div style="transition: opacity .3s">Selftest inline transition</div>
<p data-gsap="split">Selftest split paragraph</p>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
"""
QA_EXPECT = [
    (r"2 <h1> elements", "exactly one h1"),
    (r"image without alt attribute: assets/img/selftest-missing", "alt text"),
    (r"missing image file assets/img/selftest-missing", "missing image"),
    (r"<img> without src", "img src"),
    (r"hotlinked image https://images\.example\.org", "hotlinked image"),
    (r"dead/placeholder link", "placeholder link (handoff list)"),
    (r"button 'Selftest other label' goes to the primary CTA", "one CTA label (L-014)"),
    (r"select 'selftest_budget' must start on an empty", "Choose… first (L-010)"),
    (r"select 'selftest_pick' preselects", "no preselected choice (L-010)"),
    (r"select 'selftest_reply' offers Email but has no data-requires-email", "reply route required (L-072)"),
    (r"form posts to mailto:", "never mailto"),
    (r"form has no 'what happens next' line", "next-steps line (L-012)"),
    (r"phone field 'phone' is type=\"text\"", "tel fields"),
    (r"tel:\+15550109876 differs from BIZ PHONE", "one phone number (NAP)"),
    (r"email `selftest@example\.org` without <wbr>", "email wrapping (L-070)"),
    (r"visible text contains null", "unguarded prefill"),
    (r"marquee/ticker element", "no marquee (L-015)"),
    (r"inline CSS motion `transition", "JS-only motion, inline"),
    (r"data-gsap=\"split\" on a <p>", "split headings only (L-062)"),
    (r"GSAP from a CDN", "self-hosted GSAP"),
]
CSS = """
/* selftest */
.selftest-a { transition: transform .2s }
@keyframes selftest-spin { to { transform: rotate(1turn) } }
.selftest-b { line-height: .9 }
.selftest-c { overflow-wrap: break-word }
@media (max-width: 599px) { .selftest-row { grid-template-columns: 1fr 1fr } }
.selftest-row { display: grid; grid-template-columns: 1fr }
"""
CSS_EXPECT = [
    (r"`\.selftest-row` sets grid-template-columns in `@media", "breakpoint override after its base rule (L-063)"),
    (r"CSS motion `transition: transform \.2s", "JS-only motion, stylesheet"),
    (r"CSS motion `@keyframes selftest-spin", "no @keyframes"),
    (r"line-height \.9 on `\.selftest-b`", "headline line-height (L-051)"),
    (r"`\.selftest-c` uses overflow-wrap: break-word", "overflow-wrap anywhere (L-070)"),
]
MOTION = """
/* selftest: dead code that only the static checks read */
if (false) {
  gsap.to('.selftest', { width: 10, overwrite: true });
  ScrollTrigger.create({ onUpdate() { return this.progress; } });
  ScrollSmoother.create({});
}
"""
MOTION_EXPECT = [
    (r"motion\.js sets width", "transform/opacity only"),
    (r"reads this\.progress/direction/isActive as a property", "ScrollTrigger `this` (L-071)"),
    (r"overwrite: true", "overwrite auto (L-068)"),
    (r"uses ScrollSmoother", "no ScrollSmoother unless asked"),
]
BARE_PAGE = ('<!doctype html><html lang="en"><head><title></title></head><body>'
             '<header><a href="index.html">Home</a></header><main><p>Selftest bare page.</p></main></body></html>')
BARE_EXPECT = [
    (r"selftest-bare\.html: no tap-to-call", "header tap-to-call"),
    (r"selftest-bare\.html: missing viewport meta", "viewport meta"),
    (r"selftest-bare\.html: empty <title>", "title"),
    (r"selftest-bare\.html: empty meta description", "meta description"),
]
OTHER_EXPECT = [
    (r"audio-devices\.html: <html> has no lang", "html lang"),
    (r"index\.html: JSON-LD doesn't parse", "JSON-LD parses"),
    (r"same <title> on", "unique titles"),
    (r"robots\.txt blocks the whole site", "robots.txt"),
    (r"Google Fonts CSS linked", "self-hosted fonts (L-039)"),
    (r"image used 2x", "no repeated photo"),
    (r"near-duplicate images .*selftest-near-dup\.jpg", "no near-duplicate photo (L-029)"),
    (r"BRIEF\.md links https://instagram\.com/selftestbrief but the site links", "contact links copied from the brief (L-025)"),
    (r"control character", "mangled escapes (L-027)"),
    (r"hard-coded user path", "relative paths (L-055)"),
    (r"tools/ holds full copies of shared pipeline tools \(deploy\.py\)", "shared tools (L-052)"),
]
# Planted into dist/selftest.html (a copy of about.html) for the browser pass
BROWSER_MARKUP = """
<div style="width: 2400px; height: 4px; background: #888"></div>
<p style="color: #8a8a8a; background: #9a9a9a; padding: 8px">Selftest low-contrast text</p>
<img src="assets/img/selftest-broken.webp" alt="Broken on purpose" width="200" height="100">
<button type="button" class="selftest-nameless"></button>
<p id="selftest-shape-text" style="font-size: 20px">Selftest text under a scene shape</p>
<script>window.__motionShapes = () => { const r = document.getElementById('selftest-shape-text').getBoundingClientRect();
  return [{ name: 'selftest-planted', x: r.left, y: r.top, w: r.width, h: r.height, formed: true }]; };</script>
<script>throw new Error('selftest planted error');</script>
"""
# Planted into the clean copy's dist/about.html: scene shapes the sweep must not report (L-079): one over text on
# an opaque card (a scene behind the page can't show through), one over text while still forming
CLEAN_SHAPES = """
<div style="background: #111; padding: 8px"><p id="selftest-card-text">Selftest text on an opaque card</p></div>
<p id="selftest-forming-text">Selftest text under a shape still forming</p>
<script>window.__motionShapes = () => [['selftest-card', true], ['selftest-forming', false]].map(([name, formed]) => {
  const r = document.getElementById(name + '-text').getBoundingClientRect();
  return { name, x: r.left, y: r.top, w: r.width, h: r.height, formed }; });</script>
"""
BROWSER_EXPECT = [
    (r"horizontal overflow at", "no sideways scroll"),
    (r"contrast [\d.]+:1 < 4\.5:1", "text contrast"),
    (r"broken image: assets/img/selftest-broken\.webp", "broken images"),
    (r"button-name", "axe: buttons have names"),
    (r"uncaught JavaScript error.*selftest planted error", "page JS errors (L-048)"),
    (r'scene shape "selftest-planted" lies over text: at 1280×720.*at 390×844', "scene shape over text, every window size (L-079)"),
]
CLEAN_BROWSER_EXPECT = [
    (r"\*\*0 errors", "clean page has 0 errors"),
    (r"^(?![\s\S]*scene shape)(?![\s\S]*no shape was ever reported formed)",
     "scene sweep skips text on an opaque card and shapes still forming (L-079)"),
]


def edit(path, old, new):
    text = path.read_text(encoding="utf-8")
    if text.count(old) < 1:
        sys.exit(f"selftest: can't plant into {path.name}: {old[:40]!r} not found (pick another --site)")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def plant(site):
    dist = site / "dist"
    cfg = runpy.run_path(str(site / "_src" / "site_config.py"))
    cta_href = cfg["PRIMARY_CTA"][1]
    pages = sorted(p.name for p in dist.glob("*.html"))
    qa_page = next(p for p in pages if p not in ("index.html", "404.html", "contact.html", "audio-devices.html"))
    edit(dist / qa_page, "</main>", QA_MARKUP.format(cta_href=cta_href) + "</main>")
    edit(dist / qa_page, "</head>", '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter">'
                                    "</head>")
    home = (dist / "index.html").read_text(encoding="utf-8")
    photo = next(s for s in re.findall(r'<img[^>]+src="(assets/img/[^"]+)"', home)
                 if not re.search(r"logo|icon|favicon|\.svg$", s, re.I))
    other = next(p for p in pages if p not in ("index.html", "404.html", qa_page))
    edit(dist / other, "</main>", f'<img src="{photo}" alt="Selftest repeat">' + "</main>")
    # the same photo re-exported smaller under another name (L-029)
    from PIL import Image
    with Image.open(dist / photo) as im:
        im.convert("RGB").resize((max(1, im.width // 3), max(1, im.height // 3))).save(
            dist / "assets" / "selftest-near-dup.jpg", quality=55)
    edit(dist / qa_page, "</main>", '<img src="assets/selftest-near-dup.jpg" alt="Selftest near duplicate"></main>')
    # the brief names one Instagram URL, the site links a retyped one (L-025)
    brief = site / "BRIEF.md"
    text = brief.read_text(encoding="utf-8") if brief.exists() else ""
    brief.write_text(re.sub(r"^Links.*$", "", text, flags=re.M) + "\nLinks: https://instagram.com/selftestbrief\n",
                     encoding="utf-8")
    edit(dist / qa_page, "</main>", '<a href="https://www.instagram.com/selftestbreif/">Instagram</a></main>')
    edit(dist / "audio-devices.html" if "audio-devices.html" in pages else dist / other, '<html lang="en">', "<html>")
    edit(dist / "index.html", 'type="application/ld+json">', 'type="application/ld+json">{,')
    title = re.search(r"<title>(.*?)</title>", home, re.S).group(0)
    edit(dist / "404.html", re.search(r"<title>.*?</title>", (dist / "404.html").read_text(encoding="utf-8"),
                                      re.S).group(0), title)
    (dist / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    (dist / "selftest-bare.html").write_text(BARE_PAGE, encoding="utf-8")
    with open(dist / "assets" / "css" / "styles.css", "a", encoding="utf-8") as f:
        f.write(CSS)
    with open(dist / "assets" / "js" / "motion.js", "a", encoding="utf-8") as f:
        f.write(MOTION)
    (site / "assets" / "js" / "selftest-src.js").write_text(
        "const mangled = 'svg\x08';\nconst path = 'C:/Users/someone/site';\n", encoding="utf-8")
    (site / "tools" / "deploy.py").write_bytes((PIPELINE / "tools" / "deploy.py").read_bytes())
    about = (dist / "about.html").read_text(encoding="utf-8")
    (dist / "selftest.html").write_text(about.replace("</main>", BROWSER_MARKUP + "</main>", 1), encoding="utf-8")


def run(site, cmd):
    r = subprocess.run(cmd, cwd=site, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return (r.stdout + r.stderr).strip().splitlines()[-1:] or [""]


def report(site, name):
    path = site / "qa" / name
    return path.read_text(encoding="utf-8") if path.exists() else ""


def check(text, expectations, label):
    failed = 0
    for pattern, why in expectations:
        ok = re.search(pattern, text) is not None
        failed += not ok
        print(f"  {'ok  ' if ok else 'MISS'} {why}{'' if ok else f'   (no line matching /{pattern}/ in {label})'}")
    return failed


def main():
    args = sys.argv[1:]
    base = Path(args[args.index("--site") + 1]) if "--site" in args else BASE
    base = base if base.is_absolute() else WORKSPACE / base
    shutil.rmtree(WORK, ignore_errors=True)
    clean, broken = WORK / "clean", WORK / "broken"
    for d in (clean, broken):
        shutil.copytree(base, d, ignore=SKIP)
    # quiet case: the data-todo attribute name is not placeholder text (it once listed `todo` on every page)
    edit(clean / "dist" / "index.html", "</main>", '<span data-todo-note hidden></span></main>')
    plant(broken)

    failed = 0
    print(f"base: {base.name}\n\nclean copy, qa.py: {run(clean, [sys.executable, 'tools/qa.py'])[0]}")
    text = report(clean, "report.md")
    errors = re.search(r"\*\*(\d+) errors", text)
    quiet = [(r"\*\*0 errors", "clean site has 0 errors"),
             (r"^(?![\s\S]*placeholder text `todo`)", "data-todo attribute isn't read as TODO text")]
    failed += check(text, quiet, "clean qa/report.md")
    if errors and errors.group(1) != "0":
        print("  (the base isn't clean: fix it or pick another --site, or every result below is suspect)")

    print(f"\nbroken copy, qa.py: {run(broken, [sys.executable, 'tools/qa.py'])[0]}")
    text = report(broken, "report.md")
    failed += check(text, QA_EXPECT + CSS_EXPECT + MOTION_EXPECT + BARE_EXPECT + OTHER_EXPECT, "qa/report.md")

    # The pipeline itself: the lessons index matches LESSONS.md, and every Python tool can print any name (L-018)
    print("\npipeline:")
    stale = subprocess.run([sys.executable, str(PIPELINE / "dev" / "lessons_index.py"), "--check"],
                           capture_output=True, text=True).returncode
    no_utf8 = [p.relative_to(PIPELINE).as_posix() for p in sorted([*(PIPELINE / "tools").glob("*.py"),
               *(PIPELINE / "dev").glob("*.py"), *(PIPELINE / "brief-form").glob("*.py")])
               if "stdout.reconfigure" not in p.read_text(encoding="utf-8", errors="replace")]
    pipeline = [(not stale, "LESSONS-INDEX.md is current (else: python dev/lessons_index.py)"),
                (not no_utf8, f"Python tools set UTF-8 stdout (L-018){': missing in ' + ', '.join(no_utf8) if no_utf8 else ''}")]
    for ok, why in pipeline:
        failed += not ok
        print(f"  {'ok  ' if ok else 'MISS'} {why}")

    if "--browser" in args:
        edit(clean / "dist" / "about.html", "</main>", CLEAN_SHAPES + "</main>")
        print(f"\nclean copy, browser_qa.mjs about.html: "
              f"{run(clean, ['node', 'tools/browser_qa.mjs', 'about.html', '--no-lighthouse'])[0]}")
        failed += check(report(clean, "browser-report.md"), CLEAN_BROWSER_EXPECT, "clean qa/browser-report.md")
        print(f"\nbroken copy, browser_qa.mjs selftest.html: "
              f"{run(broken, ['node', 'tools/browser_qa.mjs', 'selftest.html', '--no-lighthouse'])[0]}")
        failed += check(report(broken, "browser-report.md"), BROWSER_EXPECT, "qa/browser-report.md")

    total = 2 + len(pipeline) + len(QA_EXPECT + CSS_EXPECT + MOTION_EXPECT + BARE_EXPECT + OTHER_EXPECT) + (
        len(CLEAN_BROWSER_EXPECT + BROWSER_EXPECT) if "--browser" in args else 0)
    print(f"\nselftest: {total - failed}/{total} passed" + ("" if "--browser" in args else " (add --browser for the browser checks)"))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
