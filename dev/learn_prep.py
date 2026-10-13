"""Prepare design references dropped into design-library/inspiration/ for learning (design-library/LEARN.md).

    python learn_prep.py            ingest new drops, then list everything still to learn (crops + palettes)
    python learn_prep.py --check    print only the number of references waiting (drops + pending), change nothing
    python learn_prep.py --lib <design-library folder>   work on another copy (tests)

Ingest: a drop is any image in inspiration/ that isn't already a lowercase-slug .webp. It becomes
inspiration/<slug>.webp (at most 1400 wide) and the original moves to inspiration/originals/. A drop can also be a
design-system Markdown file (e.g. a Refero Styles DESIGN.md) under any .md name: it moves to
inspiration/design-md/<slug>.md, so the next download can't collide with it. A generic name (DESIGN.md) takes its slug
from the file's title instead. A reference is pending until references/<slug>.md exists (or a site entry cites it).
For each pending image this prints viewing crops (<workspace>/_temp/learn/<slug>/, regenerated if missing) and its
sampled palette; for each pending DESIGN.md, its headings and the colours it names.
"""
import argparse
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
PIPELINE = Path(__file__).resolve().parent.parent          # <workspace>/Workflow and Pipeline/website-pipeline
WS = PIPELINE.parent.parent                                 # <workspace>
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp"}
DOC_EXT = {".md"}
DOC_DIR = "design-md"                                       # inspiration/design-md/<slug>.md
GENERIC = {"design", "design-md", "design-system", "readme", "style", "styles", "untitled", "reference"}
VIEW_W, SLICE_H, OVERLAP = 1200, 1500, 80


def slugify(name, taken):
    base = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:60] or "reference"
    slug, n = base, 2
    while slug in taken:
        slug, n = f"{base}-{n}", n + 1
    return slug


SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def drops(lib):
    """Images in inspiration/ not yet in the library's own form (<slug>.webp), plus any .md dropped there."""
    insp = lib / "inspiration"
    if not insp.is_dir():
        return []
    return sorted(p for p in insp.iterdir() if p.is_file() and (
        p.suffix.lower() in DOC_EXT
        or (p.suffix.lower() in IMAGE_EXT and not (p.suffix == ".webp" and SLUG.fullmatch(p.stem)))))


def learned(lib, slug, ext=".webp"):
    """Learned = has a reference entry, or is an older site inspiration file that a site entry already covers."""
    if (lib / "references" / f"{slug}.md").exists():
        return True
    cite = f"{slug}.webp" if ext == ".webp" else f"{DOC_DIR}/{slug}.md"
    return any(cite in p.read_text(encoding="utf-8") for p in (lib / "sites").glob("*.md"))


def doc_title(text):
    """The design system's own name: front-matter name/title, else the first # heading."""
    m = re.match(r"---\s*\n(.*?)\n---", text, re.S)
    if m:
        t = re.search(r"^(?:name|title):\s*['\"]?(.+?)['\"]?\s*$", m.group(1), re.M)
        if t:
            return t.group(1)
    t = re.search(r"^#\s+(.+)$", text, re.M)
    return t.group(1) if t else ""


def ingest_doc(lib, src, taken):
    """Move a dropped .md to inspiration/design-md/<slug>.md. Never overwrites: a taken slug gets -2, -3..."""
    try:
        text = src.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeDecodeError) as e:  # locked, half-copied or not text: leave it for the next run
        print(f"- skipped {src.name}: {e}")
        return
    name = src.stem
    # "DESIGN (1).md" is a browser's second download of DESIGN.md: still generic.
    if re.sub(r"-\d+$", "", re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")) in GENERIC and doc_title(text):
        name = doc_title(text)
    slug = slugify(name, taken)
    taken.add(slug)
    (lib / "inspiration" / DOC_DIR).mkdir(parents=True, exist_ok=True)
    dest = lib / "inspiration" / DOC_DIR / f"{slug}.md"
    shutil.move(str(src), str(dest))
    print(f"- ingested {src.name} -> inspiration/{DOC_DIR}/{slug}.md")


def ingest(lib):
    insp = lib / "inspiration"
    (insp / "originals").mkdir(parents=True, exist_ok=True)
    todo = drops(lib)
    # Names already in the library: its own <slug>.webp and design-md/<slug>.md files, and every reference entry.
    # A drop named like one gets a -2 suffix, never overwrites it (a test drop "macz-reference-1.jpg" once replaced
    # macz-reference-1.webp).
    taken = ({p.stem for p in insp.glob("*.webp") if SLUG.fullmatch(p.stem)}
             | {p.stem for p in (insp / DOC_DIR).glob("*.md")}
             | {p.stem for p in (lib / "references").glob("*.md")})
    for src in todo:
        if src.suffix.lower() in DOC_EXT:
            ingest_doc(lib, src, taken)
            continue
        slug = slugify(src.stem, taken)
        taken.add(slug)
        # Move the original aside first: on Windows "Hero.webp" and "hero.webp" are the same file.
        kept, n = insp / "originals" / f"{slug}{src.suffix.lower()}", 2
        while kept.exists():
            kept, n = insp / "originals" / f"{slug}-{n}{src.suffix.lower()}", n + 1
        shutil.move(str(src), str(kept))
        try:
            with Image.open(kept) as im:
                im.seek(0)
                im = im.convert("RGB")
                if im.width > 1400:
                    im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
                im.save(insp / f"{slug}.webp", "WEBP", quality=82, method=6)
        except Exception as e:  # unreadable or half-copied: put it back for the next run
            shutil.move(str(kept), str(src))
            print(f"- skipped {src.name}: {e}")
            continue
        print(f"- ingested {src.name} -> inspiration/{slug}.webp (original: inspiration/originals/{kept.name})")


def crops(slug, webp):
    out = WS / "_temp" / "learn" / slug
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.png"):  # always rebuilt: another image may have had this slug before
        old.unlink()
    with Image.open(webp) as im:
        im = im.convert("RGB")
        if im.width > VIEW_W:
            im = im.resize((VIEW_W, round(im.height * VIEW_W / im.width)), Image.LANCZOS)
        if im.height > SLICE_H:  # tall page: a small overview plus readable slices
            im.resize((500, round(im.height * 500 / im.width)), Image.LANCZOS).save(out / "overview.png")
        top, n = 0, 1
        while top < im.height:
            im.crop((0, top, im.width, min(im.height, top + SLICE_H))).save(out / f"part-{n:02}.png")
            if top + SLICE_H >= im.height:
                break
            top, n = top + SLICE_H - OVERLAP, n + 1
    return sorted(out.glob("*.png"))


def palette(webp, k=10):
    with Image.open(webp) as im:
        im = im.convert("RGB")
        im.thumbnail((240, 240))
        q = im.quantize(colors=k, method=Image.Quantize.MEDIANCUT)
        pal, total = q.getpalette(), im.width * im.height
        rows = sorted(q.getcolors(), reverse=True)
    return [(f"#{pal[i*3]:02X}{pal[i*3+1]:02X}{pal[i*3+2]:02X}", c / total) for c, i in rows]


def doc_summary(md):
    """Headings and the hex colours a DESIGN.md names (most used first), to orient the read."""
    text = md.read_text(encoding="utf-8-sig")
    heads = [h.strip() for h in re.findall(r"^#{1,3}\s+(.+)$", text, re.M)]
    hexes = Counter(h.upper() for h in re.findall(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b", text))
    return len(text.splitlines()), heads, [h for h, _ in hexes.most_common(16)]


def pending(lib):
    insp = lib / "inspiration"
    return ([p for p in sorted(insp.glob("*.webp")) if not learned(lib, p.stem)]
            + [p for p in sorted((insp / DOC_DIR).glob("*.md")) if not learned(lib, p.stem, ".md")])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--lib", default=str(PIPELINE / "design-library"))
    a = ap.parse_args()
    lib = Path(a.lib).resolve()
    if a.check:
        print(len(drops(lib)) + len(pending(lib)))
        return
    ingest(lib)
    todo = pending(lib)
    if not todo:
        print("Nothing to learn.")
        return
    print(f"\n{len(todo)} reference(s) to learn:\n")
    for webp in todo:
        if webp.suffix == ".md":
            lines, heads, hexes = doc_summary(webp)
            print(f"## {webp.stem}  (DESIGN.md, {lines} lines)")
            print(f"design.md: {webp}")
            print("sections: " + (" / ".join(heads[:30]) or "(no headings)"))
            print("colours named: " + (", ".join(hexes) or "(none)"))
            print()
            continue
        with Image.open(webp) as im:
            size = f"{im.width}x{im.height}"
        print(f"## {webp.stem}  ({size})")
        print(f"image: {webp}")
        for c in crops(webp.stem, webp):
            print(f"view:  {c}")
        print("palette (share of pixels): " + ", ".join(f"{h} {s:.0%}" for h, s in palette(webp)))
        print()


if __name__ == "__main__":
    main()
