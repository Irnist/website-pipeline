"""Run the template's QA tools over a copy of a finished past site (the original is only read).

Use it to prove a new check has no false positives on real markup (LESSONS L-017).

    python dev/qa_real_site.py "<site folder>" <scratch workdir> "<cta label>" <cta href>
    cd <scratch workdir> && node tools/browser_qa.mjs      (optional, after the qa.py run)
"""
import shutil
import subprocess
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "template"
site, work = Path(sys.argv[1]), Path(sys.argv[2])
label, href = sys.argv[3], sys.argv[4]

shutil.rmtree(work, ignore_errors=True)
(work / "dist").mkdir(parents=True)
for f in site.glob("*.html"):
    shutil.copy2(f, work / "dist" / f.name)
shutil.copytree(site / "assets", work / "dist" / "assets")
(work / "tools").mkdir()
for tool in ("qa.py", "browser_qa.mjs", "lighthouse.mjs"):
    shutil.copy2(TEMPLATE / "tools" / tool, work / "tools" / tool)
shutil.copytree(TEMPLATE / "tools" / "vendor", work / "tools" / "vendor")
for extra in ("_headers", "robots.txt", "sitemap.xml"):
    if (site / extra).exists():
        shutil.copy2(site / extra, work / "dist" / extra)
(work / "_src").mkdir()
(work / "_src" / "site_config.py").write_text(
    f"PRIMARY_CTA = ({label!r}, {href!r})\nLOCAL_BUSINESS = True\nALLOW_REPEAT_IMAGES = []\n", encoding="utf-8")
subprocess.run([sys.executable, "tools/qa.py"], cwd=work)
