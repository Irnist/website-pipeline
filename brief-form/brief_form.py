"""Brief form: edit a project's BRIEF.md and drop client files into client-assets/ in an app window.

    python brief_form.py "<project folder>"             opens the form in an Edge app window
    python brief_form.py "<project folder>" --no-window  serves only and prints the URL (testing)

Exit codes: 0 = the user clicked "Start building" (scaffold.ps1 then launches Claude),
            3 = the window was closed without starting (the brief is still saved; edits autosave),
            1 = could not start (scaffold.ps1 falls back to Notepad).
BRIEF.md stays the source of truth: values are written back into their own lines, comments kept,
so /website and tools/deploy.py read it exactly as before.
"""
import json
import mimetypes
import os
import re
import secrets
import shutil
import subprocess
import sys
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
EDGE_PATHS = [
    Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Microsoft/Edge/Application/msedge.exe",
    Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Microsoft/Edge/Application/msedge.exe",
]
# The app window's Edge profile is scratch data, so it lives in the workspace's _temp (HERE is
# <workspace>/Workflow and Pipeline/website-pipeline/brief-form once resolve() follows the skills junction).
EDGE_PROFILE = HERE.parents[2] / "_temp" / "brief-form-edge"
MAX_UPLOAD = 200 * 1024 * 1024
HIDDEN_ASSETS = {"readme.txt", ".gitkeep", "desktop.ini", "thumbs.db"}
KEY_LINE = re.compile(r"^(?P<key>[A-Z][^:\n]{0,120}?):(?P<rest>.*)$")
COMMENT = re.compile(r"\s*(<!--.*?-->)\s*$")
COMMENT_COL = 31
# Renamed BRIEF labels: old label -> current one. Older briefs are read under the new name and the
# line is renamed on the next save (instead of a second line being appended at the end).
KEY_ALIASES = {
    "Form endpoint (e.g. Formspree URL; blank = demo mode, listed at handoff)": "Form endpoint",
}


def line_key(m):
    key = m.group("key").strip()
    return KEY_ALIASES.get(key, key)


# ---------------------------------------------------------------- BRIEF.md read / write

def read_brief(path):
    """{key: value}; indented lines under a key are continuation lines (multi-line answers)."""
    values, key = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = KEY_LINE.match(line)
        if m:
            key = line_key(m)
            values[key] = COMMENT.sub("", m.group("rest")).strip()
        elif key and line.startswith("  ") and line.strip():
            values[key] += "\n" + line.strip()
        else:
            key = None
    return values


def format_field(key, value, comment):
    lines = [l.strip() for l in str(value).replace("\r", "").split("\n")]
    lines = [l for l in lines if l] or [""]
    first = f"{key}: {lines[0]}" if lines[0] else f"{key}:"
    if comment:
        first = (first.ljust(COMMENT_COL) if len(first) < COMMENT_COL else first + " ") + comment
    return [first] + ["  " + l for l in lines[1:]]


def write_brief(path, updates):
    raw = path.read_text(encoding="utf-8")
    newline = "\r\n" if "\r\n" in raw else "\n"
    lines, out, i, done = raw.splitlines(), [], 0, set()
    while i < len(lines):
        m = KEY_LINE.match(lines[i])
        key = line_key(m) if m else None
        if key in updates and key not in done:
            c = COMMENT.search(m.group("rest"))
            out += format_field(key, updates[key], c.group(1) if c else "")
            done.add(key)
            i += 1
            while i < len(lines) and lines[i].startswith("  ") and lines[i].strip():
                i += 1  # drop the old continuation lines
            continue
        out.append(lines[i])
        i += 1
    missing = [k for k in updates if k not in done]
    if missing:  # e.g. an older brief without "Deploy host:"
        out.append("")
        for k in missing:
            out += format_field(k, updates[k], "")
    tmp = path.with_suffix(".md.tmp")
    tmp.write_text(newline.join(out) + newline, encoding="utf-8")
    os.replace(tmp, path)


# ---------------------------------------------------------------- client-assets

def safe_name(name):
    name = Path(name.replace("\\", "/")).name
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "", name).strip(" .")
    return name[:150] or "file"


def unique_path(folder, name):
    target = folder / name
    stem, suffix, n = target.stem, target.suffix, 2
    while target.exists():
        target = folder / f"{stem} ({n}){suffix}"
        n += 1
    return target


def list_assets(folder):
    if not folder.exists():
        return []
    items = []
    for p in sorted(folder.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
        if p.is_file() and p.name.lower() not in HIDDEN_ASSETS:
            items.append({"name": p.name, "size": p.stat().st_size,
                          "image": (mimetypes.guess_type(p.name)[0] or "").startswith("image/")})
    return items


def recycle(path):
    """Send to the Recycle Bin rather than deleting outright."""
    ps = ("Add-Type -AssemblyName Microsoft.VisualBasic; "
          "[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile($env:BRIEF_FORM_TARGET, "
          "'OnlyErrorDialogs', 'SendToRecycleBin')")
    res = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True,
                         env={**os.environ, "BRIEF_FORM_TARGET": str(path)})
    return res.returncode == 0 and not path.exists()


# ---------------------------------------------------------------- server

class State:
    def __init__(self, project):
        self.project = project
        self.brief = project / "BRIEF.md"
        self.assets = project / "client-assets"
        self.token = secrets.token_urlsafe(16)
        self.result = None  # "start" | "closed"
        self.last_ping = time.time()
        self.done = threading.Event()

    def finish(self, result):
        if self.result is None:
            self.result = result
        self.done.set()


def make_handler(state):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def send(self, code, body=b"", ctype="application/json", extra=None):
            if isinstance(body, (dict, list)):
                body = json.dumps(body).encode("utf-8")
            elif isinstance(body, str):
                body = body.encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            for k, v in (extra or {}).items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(body)

        def authorised(self, query):
            token = self.headers.get("X-Token") or (query.get("t") or [""])[0]
            return secrets.compare_digest(token, state.token)

        def body(self):
            n = int(self.headers.get("Content-Length") or 0)
            return self.rfile.read(n) if n else b""

        def do_GET(self):
            url = urllib.parse.urlparse(self.path)
            query = urllib.parse.parse_qs(url.query)
            if url.path == "/":
                if not self.authorised(query):
                    return self.send(403, "forbidden", "text/plain")
                html = (HERE / "index.html").read_text(encoding="utf-8").replace("__TOKEN__", state.token)
                return self.send(200, html, "text/html; charset=utf-8")
            if not self.authorised(query):
                return self.send(403, {"error": "forbidden"})
            if url.path == "/api/brief":
                return self.send(200, {"folder": state.project.name, "path": str(state.project),
                                       "fields": read_brief(state.brief), "assets": list_assets(state.assets)})
            if url.path == "/api/ping":
                state.last_ping = time.time()
                return self.send(200, {"ok": True})
            if url.path == "/asset":
                name = safe_name((query.get("name") or [""])[0])
                p = state.assets / name
                if not p.is_file():
                    return self.send(404, {"error": "not found"})
                return self.send(200, p.read_bytes(), mimetypes.guess_type(p.name)[0] or "application/octet-stream")
            self.send(404, {"error": "not found"})

        def do_POST(self):
            url = urllib.parse.urlparse(self.path)
            query = urllib.parse.parse_qs(url.query)
            if not self.authorised(query):
                return self.send(403, {"error": "forbidden"})
            if url.path == "/api/save":
                fields = json.loads(self.body() or b"{}").get("fields", {})
                write_brief(state.brief, {str(k): str(v) for k, v in fields.items()})
                return self.send(200, {"ok": True, "saved": time.strftime("%H:%M")})
            if url.path == "/api/upload":
                size = int(self.headers.get("Content-Length") or 0)
                if size > MAX_UPLOAD:
                    return self.send(413, {"error": "File is over 200 MB"})
                state.assets.mkdir(exist_ok=True)
                target = unique_path(state.assets, safe_name((query.get("name") or ["file"])[0]))
                target.write_bytes(self.body())
                return self.send(200, {"ok": True, "name": target.name, "assets": list_assets(state.assets)})
            if url.path == "/api/remove":
                name = safe_name(json.loads(self.body() or b"{}").get("name", ""))
                p = state.assets / name
                ok = p.is_file() and recycle(p)
                return self.send(200 if ok else 400, {"ok": ok, "assets": list_assets(state.assets)})
            if url.path == "/api/open-folder":
                state.assets.mkdir(exist_ok=True)
                subprocess.Popen(["explorer.exe", str(state.assets)])
                return self.send(200, {"ok": True})
            if url.path == "/api/start":
                fields = json.loads(self.body() or b"{}").get("fields")
                if fields:
                    write_brief(state.brief, {str(k): str(v) for k, v in fields.items()})
                self.send(200, {"ok": True})
                threading.Timer(0.6, state.finish, args=("start",)).start()
                return
            self.send(404, {"error": "not found"})

    return Handler


def find_edge():
    return next((p for p in EDGE_PATHS if p.exists()), None)


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit("usage: brief_form.py <project folder> [--no-window]")
    project = Path(args[0]).resolve()
    if not (project / "BRIEF.md").exists():
        print(f"no BRIEF.md in {project}")
        sys.exit(1)

    state = State(project)
    server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(state))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{server.server_address[1]}/?t={state.token}"

    proc, watch_process = None, False
    if "--no-window" in sys.argv:
        print(url, flush=True)
    else:
        edge = find_edge()
        if edge:
            EDGE_PROFILE.mkdir(parents=True, exist_ok=True)
            proc = subprocess.Popen([str(edge), f"--app={url}", f"--user-data-dir={EDGE_PROFILE}",
                                     "--window-size=1180,900", "--no-first-run", "--no-default-browser-check",
                                     "--disable-features=msEdgeSidebarV2,msHubApps"])
            time.sleep(3)
            # A separate profile gives a process we can wait on. If it handed off to a running
            # instance and exited, fall back to the page's heartbeat.
            watch_process = proc.poll() is None
        else:
            import webbrowser
            webbrowser.open(url)
        print("  Brief form is open. Fill it in, drop in photos, then click Start building.", flush=True)

    try:
        while not state.done.wait(1):
            if watch_process and proc.poll() is not None:
                time.sleep(1.5)  # a Start click may still be finishing
                state.finish("closed")
            elif "--no-window" not in sys.argv and time.time() - state.last_ping > 90:
                # No heartbeat: the window is gone even if Edge lingers in the background.
                # Minimised pages throttle timers to about one a minute, so allow a generous gap.
                state.finish("closed")
    except KeyboardInterrupt:
        state.finish("closed")

    if proc and proc.poll() is None:
        proc.terminate()
    server.shutdown()
    sys.exit(0 if state.result == "start" else 3)


if __name__ == "__main__":
    main()
