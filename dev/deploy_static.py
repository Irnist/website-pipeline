"""Deploy an older hand-built site (no _src/build.py, no dist/) as a noindex Cloudflare preview.

    python dev/deploy_static.py "<site folder>"

Stages only the published files (top-level *.html, favicon/robots, assets/) into
<site>/.pipeline/stage with a noindex _headers file, then deploys that folder as a
static-assets Worker named <folder>-preview, the same way the shared tools/deploy.py does
(L-026: never let wrangler autoconfig run in the site folder). Source folders (_src,
Media, .impeccable, client-assets, qa) are never staged.
"""
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

NPX = shutil.which("npx") or "npx"  # mise shims npx without a .cmd; resolve it like tools/deploy.py
TOP_FILES = ("favicon.ico", "robots.txt", "site.webmanifest", "manifest.json")


def wrangler(root, *args):
    return subprocess.run([NPX, "-y", "wrangler", *args], cwd=root, capture_output=True,
                          text=True, encoding="utf-8", errors="replace")


def check(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (pipeline deploy check)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.headers.get("X-Robots-Tag", "")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("X-Robots-Tag", "")
    except (urllib.error.URLError, OSError):
        return 0, ""


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = Path(sys.argv[1]).resolve()
    if (root / "_src" / "build.py").exists() and (root / "tools" / "deploy.py").exists():
        sys.exit("this site has tools/deploy.py: use that instead")
    pipe = root / ".pipeline"
    stage = pipe / "stage"
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)
    pages = sorted(root.glob("*.html"))
    if not pages:
        sys.exit(f"no *.html in {root}")
    for p in pages:
        shutil.copy2(p, stage / p.name)
    for name in TOP_FILES:
        if (root / name).exists():
            shutil.copy2(root / name, stage / name)
    shutil.copytree(root / "assets", stage / "assets")
    (stage / "_headers").write_text("/*\n  X-Robots-Tag: noindex, nofollow\n", encoding="utf-8")

    # Every local src/href in the pages must resolve inside the stage.
    missing = set()
    for p in pages:
        for ref in re.findall(r'(?:src|href)="([^"#?]+)', p.read_text(encoding="utf-8", errors="replace")):
            if re.match(r"[a-z][a-z0-9+.-]*:|//", ref) or ref.endswith("/"):  # any scheme (viber:, sms:...)
                continue
            if not (stage / ref).exists():
                missing.add(f"{p.name}: {ref}")
    if missing:
        print("! references not in the stage (check before trusting the preview):")
        for m in sorted(missing):
            print("   ", m)

    who = wrangler(root, "whoami")
    if "You are logged in" not in who.stdout + who.stderr:
        sys.exit("Wrangler is not logged in. Ask the user to run:  ! npx wrangler login")
    state_file = pipe / "cloudflare.json"
    state = json.loads(state_file.read_text(encoding="utf-8")) if state_file.exists() else {}
    name = state.get("worker_name")
    if not name:
        base = re.sub(r"[^a-z0-9]+", "-", root.name.lower()).strip("-")[:40] + "-preview"
        for attempt in range(4):
            name = base if attempt == 0 else f"{base}-{attempt + 1}"
            if wrangler(root, "deployments", "list", "--name", name, "--json").returncode != 0:
                break  # no Worker by that name: free to create
        else:
            sys.exit("could not find a free Worker name")
    config = pipe / "wrangler.jsonc"
    config.write_text(json.dumps({"name": name, "compatibility_date": "2026-09-01", "workers_dev": True,
                                  "preview_urls": False, "assets": {"directory": "stage"}}, indent=2),
                      encoding="utf-8")
    res = wrangler(root, "deploy", "--config", str(config), "--message", "pipeline preview")
    if res.returncode != 0:
        sys.exit(f"deploy failed:\n{res.stdout[-1500:]}\n{res.stderr[-1500:]}")
    m = re.search(r"https://[a-z0-9.-]+\.workers\.dev", res.stdout + res.stderr)
    if not m:
        sys.exit(f"deployed, but no workers.dev URL in the output:\n{res.stdout[-1500:]}")
    url = m.group(0)
    state_file.write_text(json.dumps({"worker_name": name, "url": url}, indent=2), encoding="utf-8")
    print(f"deployed: {url}")

    deadline = time.time() + 180
    code, robots = check(url)
    while code in (0, 404, 522, 525, 526) and time.time() < deadline:
        time.sleep(10)
        code, robots = check(url)
    if code != 200:
        sys.exit(f"! public check returned {code or 'no response'}")
    if "noindex" not in robots.lower():
        sys.exit("! X-Robots-Tag noindex missing on the live site")
    print("public access OK (200), X-Robots-Tag: noindex present")


if __name__ == "__main__":
    main()
