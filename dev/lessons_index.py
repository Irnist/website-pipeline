"""Write LESSONS-INDEX.md: one line per lesson in LESSONS.md, so Intake reads ~10KB instead of ~80KB.

    python dev/lessons_index.py            rewrite LESSONS-INDEX.md
    python dev/lessons_index.py --check    exit 1 if LESSONS-INDEX.md is out of date (qa.py and selftest use it)

Each line: ID, area, the mistake's first sentence, and its enforcement level (check / rule / step / log),
read from the entry's own "Enforced by:" line. A lesson whose enforcement names no check is listed again
under "Not machine-checked", the ones most likely to repeat (LESSONS.md › Escalation).
PROJECT.md › Watch for lists lesson IDs from here instead of copying lesson text, so it can't go stale.
"""
import re
import sys
from pathlib import Path

PIPE = Path(__file__).resolve().parent.parent
SRC = PIPE / "LESSONS.md"
OUT = PIPE / "LESSONS-INDEX.md"
LEVELS = ("check", "rule", "step", "log")


def first_sentence(text, limit=150):
    text = re.sub(r"\s+", " ", text).strip()
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def entries(md):
    for m in re.finditer(r"^### (L-\d+) · ([^·\n]+) · ([^·\n]+?)(?: · ([^\n]+))?$(.*?)(?=^### |\Z)", md, re.M | re.S):
        lid, date, project, area, body = m.groups()
        field = lambda name: (re.search(rf"^- {name}: (.*?)(?=^- [A-Z][\w ]+:|\Z)", body, re.M | re.S) or [None, ""])[1]
        mistake = field("Mistakes?") or field("Prevention")
        enforced = field("Enforced by")
        low = enforced.lower()
        levels = [lv for lv in LEVELS if re.search(rf"\b{lv}", low)] or (["check"] if "template fix" in low else ["log"])
        yield {
            "id": lid, "date": date.strip(), "project": project.strip(), "area": (area or "").strip(),
            "mistake": first_sentence(mistake), "levels": levels,
            "superseded": "superseded" in body.lower(),
        }


def render(items):
    out = [
        "# Lessons index",
        "",
        "Generated from LESSONS.md by `dev/lessons_index.py`; don't edit by hand. One line per lesson:",
        "what went wrong and how it's enforced now. Open the full entry in LESSONS.md when one applies.",
        "",
    ]
    for it in items:
        sup = " *(superseded, see entry)*" if it["superseded"] else ""
        out.append(f"- **{it['id']}** {it['area']} · {it['mistake']} — {'+'.join(it['levels'])}{sup}")
    loose = [it for it in items if "check" not in it["levels"] and it["id"] != "L-000"]
    out += ["", f"## Not machine-checked ({len(loose)})", "",
            "Enforced only by a rule, step or log: these rely on reading, so they're the likeliest to repeat.", ""]
    out += [f"- {it['id']} ({'+'.join(it['levels'])}): {it['mistake']}" for it in loose]
    counts = {lv: sum(lv in it["levels"] for it in items) for lv in LEVELS}
    out += ["", "Totals: " + ", ".join(f"{n} {lv}" for lv, n in counts.items()) + f" across {len(items)} lessons.", ""]
    return "\n".join(out)


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    items = list(entries(SRC.read_text(encoding="utf-8")))
    text = render(items)
    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != text:
            sys.exit("LESSONS-INDEX.md is out of date: run python dev/lessons_index.py")
        print("LESSONS-INDEX.md is current")
        return
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {OUT.name}: {len(items)} lessons, {len(text) // 1024}KB")


if __name__ == "__main__":
    main()
