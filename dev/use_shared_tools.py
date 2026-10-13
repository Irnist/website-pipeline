"""Switch a site from its own copies of the pipeline tools to stubs that run the shared copy (L-052).

    python dev/use_shared_tools.py "<site folder>" [...]     (relative paths resolve against the workspace)

Each full copy of a shared tool in <site>/tools/ is replaced by the template's stub, missing ones get a stub
(pipeline sites only: those with _src/site_config.py), and the old vendored axe-core is removed (the shared browser_qa brings
its own). Site-only scripts (e.g. the portfolio's capture_work.mjs) are left alone. Needs the site under git
with tools/ committed, so the old copies stay in history; commit the result afterwards.
"""
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
PIPELINE = Path(__file__).resolve().parent.parent
WORKSPACE = PIPELINE.parent.parent
SHARED = sorted(f.name for f in (PIPELINE / "tools").iterdir() if f.suffix in (".py", ".mjs"))
STUBS = PIPELINE / "template" / "tools"
MARK = "pipeline-tool-stub"


def migrate(site):
    tools = site / "tools"
    if not (site / ".git").exists():
        return print(f"skip {site.name}: not a git repo, so the old copies would be lost (git init + commit first)")
    dirty = subprocess.run(["git", "status", "--porcelain", "--", "tools"], cwd=site,
                           capture_output=True, text=True).stdout.strip()
    if dirty:
        return print(f"skip {site.name}: uncommitted changes in tools/ (commit them first):\n{dirty}")
    if not (site / "_src" / "site_config.py").exists():
        # IronCity has a _src/build.py from before the pipeline: it writes pages to the root, with no dist/
        return print(f"skip {site.name}: no _src/site_config.py (built before the pipeline; the tools don't apply)")
    tools.mkdir(exist_ok=True)
    changed = []
    for name in SHARED:
        mine = tools / name
        if mine.exists() and MARK in mine.read_text(encoding="utf-8", errors="replace"):
            continue
        mine.write_bytes((STUBS / name).read_bytes())
        changed.append(name)
    for old in ("axe.min.js", "axe-core.LICENSE.txt"):
        if (tools / "vendor" / old).exists():
            (tools / "vendor" / old).unlink()
            changed.append(f"vendor/{old} (removed)")
    print(f"{site.name}: {', '.join(changed) if changed else 'already on the shared tools'}")


for arg in sys.argv[1:] or sys.exit(__doc__):
    path = Path(arg)
    migrate(path if path.is_absolute() else WORKSPACE / path)
