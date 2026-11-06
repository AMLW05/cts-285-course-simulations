"""Verify the Module 5A reference stations.

Usage:  python verify.py <path-to-template-checkout>

For each station: copy the template, rename app.py to menu.py, add the
station's app.py and templates, run the template tests, then call every
route the station has with Flask's test client. Exit 1 on any failure.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def check(cond, what):
    if not cond:
        raise AssertionError(what)


def post(client, url, **data):
    return client.post(url, data=data)


def text(resp):
    return resp.get_data(as_text=True)


# ---- route checks, one function per route ----

def t_home_string(c):
    r = c.get("/")
    check(r.status_code == 200, "home status")
    check(text(r) == "DataMan is running on the web.", "home text")


def t_home_page(c):
    r = c.get("/")
    check(r.status_code == 200, "home status")
    t = text(r)
    for path in ("/practice", "/report", "/bank"):
        check(f'href="{path}"' in t, f"home link {path}")


def t_report(c, back):
    r = c.get("/report")
    check(r.status_code == 200 and "not attempted" in text(r), "empty report")
    check("No attempts yet." in text(r), "empty report list")
    check(('Back to menu' in text(r)) == back, "report back link")


def t_report_label(c, label):
    check(label in text(c.get("/report")), f"report label {label}")


def t_practice_post_inline(c, back):
    """Stations 3-5: POST renders the page with a message."""
    r = c.get("/practice")
    check(r.status_code == 200 and "Try 1: 7 x 8" in text(r), "practice GET")
    check(('Back to menu' in text(r)) == back, "practice back link")
    r = post(c, "/practice", answer="abc")
    check(r.status_code == 200 and "Enter a whole number." in text(r), "invalid")
    check("Try 1:" in text(r), "invalid did not spend a try")
    r = post(c, "/practice", answer="")
    check("Enter a whole number." in text(r), "empty invalid")
    for bad in ("--56", "\u00b2"):
        r = post(c, "/practice", answer=bad)
        check(r.status_code == 200 and "Enter a whole number." in text(r),
              f"invalid {bad!r} gives feedback, not an error")
    r = post(c, "/practice", answer="55")
    check(r.status_code == 200 and "Not yet. Try again." in text(r), "wrong 1")
    check("Try 2:" in text(r), "now try 2")
    r = post(c, "/practice", answer="54")
    check("The answer is 56." in text(r), "reveal")
    check("This session is finished." in text(r), "finished page")
    check("<form" not in text(r), "no form when finished")
    r = post(c, "/practice", answer="56")
    check("This session is finished. Choose report." in text(r), "finished POST")
    t_report_label(c, "two misses")
    check("answered 55 -> wrong" in text(c.get("/report")), "attempt row")


def t_bank_inline(c, back):
    r = c.get("/bank")
    check(r.status_code == 200 and "Set holds 0:" in text(r), "bank GET")
    check(('Back to menu' in text(r)) == back, "bank back link")
    for n in range(1, 11):
        r = post(c, "/bank", problem_id=f"P{n}")
        check(r.status_code == 200, "bank POST status")
        check(f"Added. Set holds {n}." in text(r), f"add {n}")
    r = post(c, "/bank", problem_id="P11")
    check("Refused: set-1 already holds 10 problems" in text(r), "11th refused")
    check("Set holds 10:" in text(r), "still 10")


def t_practice_redirect(c):
    r = c.get("/practice")
    check(r.status_code == 200 and "Back to menu" in text(r), "practice GET")
    r = post(c, "/practice", answer="abc")
    check(r.status_code == 302 and r.headers["Location"].endswith("/practice"),
          "invalid redirects")
    r = c.get("/practice")
    check("Enter a whole number." in text(r), "flash shown")
    r = c.get("/practice")
    check("Enter a whole number." not in text(r), "flash not repeated")
    check("Try 1:" in text(r), "still try 1")
    for bad in ("--56", "\u00b2"):
        r = post(c, "/practice", answer=bad)
        check(r.status_code == 302, f"invalid {bad!r} redirects, not an error")
        check("Enter a whole number." in text(c.get("/practice")), f"invalid {bad!r} flashed")
    r = post(c, "/practice", answer="55")
    check(r.status_code == 302, "wrong redirects")
    check("Not yet. Try again." in text(c.get("/practice")), "wrong flash")
    r = c.get("/practice")
    check("Not yet. Try again." not in text(r), "refresh does not repeat")
    check("Try 2:" in text(r), "only one try spent")
    r = post(c, "/practice", answer="54")
    check(r.status_code == 302, "reveal redirects")
    t = text(c.get("/practice"))
    check("The answer is 56." in t and "This session is finished." in t, "reveal")
    r = post(c, "/practice", answer="56")
    check(r.status_code == 302, "finished POST redirects")
    check("This session is finished. Choose report." in text(c.get("/practice")),
          "finished flash")
    t_report_label(c, "two misses")


def t_bank_redirect(c):
    r = c.get("/bank")
    check(r.status_code == 200 and "Back to menu" in text(r), "bank GET")
    for n in range(1, 11):
        r = post(c, "/bank", problem_id=f"P{n}")
        check(r.status_code == 302 and r.headers["Location"].endswith("/bank"),
              "add redirects")
        t = text(c.get("/bank"))
        check(f"Added. Set holds {n}." in t, f"add {n}")
        check(f"Added. Set holds {n}." not in text(c.get("/bank")),
              "flash not repeated")
    r = post(c, "/bank", problem_id="P11")
    check(r.status_code == 302, "refusal redirects")
    check("Refused: set-1 already holds 10 problems" in text(c.get("/bank")),
          "11th refused")
    check("Set holds 10:" in text(c.get("/bank")), "still 10")


STATIONS = {
    1: [t_home_string],
    2: [t_home_string, lambda c: t_report(c, False)],
    3: [t_home_string, lambda c: t_report(c, False),
        lambda c: t_practice_post_inline(c, False)],
    4: [t_home_string, lambda c: t_report(c, False),
        lambda c: t_practice_post_inline(c, False),
        lambda c: t_bank_inline(c, False)],
    5: [t_home_page, lambda c: t_report(c, True),
        lambda c: t_practice_post_inline(c, True),
        lambda c: t_bank_inline(c, True)],
    6: [t_home_page, lambda c: t_report(c, True), t_practice_redirect,
        t_bank_redirect],
}


def run_station(n, template):
    work = Path(tempfile.mkdtemp(prefix=f"m5a-station-{n}-"))
    try:
        shutil.copytree(template, work, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns(".git", "__pycache__",
                                                      "dataman_store.json"))
        (work / "app.py").rename(work / "menu.py")
        src = HERE / f"station-{n}"
        shutil.copy(src / "app.py", work / "app.py")
        if (src / "templates").is_dir():
            shutil.copytree(src / "templates", work / "templates")
        r = subprocess.run([sys.executable, "-m", "pytest", "-q", "tests"],
                           cwd=work, capture_output=True, text=True)
        check(r.returncode == 0, "template tests failed:\n" + r.stdout + r.stderr)
        store = work / "dataman_store.json"
        if store.exists():
            store.unlink()
        # Import the station's app fresh, with cwd in the temp dir.
        old_cwd = os.getcwd()
        old_path = list(sys.path)
        for name in [m for m in sys.modules
                     if m == "app" or m == "dataman" or m.startswith("dataman.")]:
            del sys.modules[name]
        os.chdir(work)
        sys.path.insert(0, str(work))
        try:
            import app as station_app
            check(Path(station_app.__file__).resolve().parent == work.resolve(),
                  "imported the wrong app.py")
            for fn in STATIONS[n]:
                client = station_app.app.test_client()
                if fn in (t_home_string, t_home_page):
                    fn(client)
                    continue
                # Each route check starts from an empty store.
                station_app.STORE.__init__()
                if store.exists():
                    store.unlink()
                station_app.STORE.__init__()
                fn(client)
        finally:
            os.chdir(old_cwd)
            sys.path[:] = old_path
            for name in [m for m in sys.modules
                         if m == "app" or m == "dataman" or m.startswith("dataman.")]:
                del sys.modules[name]
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main():
    if len(sys.argv) != 2:
        print("Usage: python verify.py <path-to-template-checkout>")
        return 2
    template = Path(sys.argv[1]).resolve()
    if not (template / "dataman" / "logic.py").exists():
        print(f"Not a template checkout: {template}")
        return 2
    failed = 0
    for n in sorted(STATIONS):
        try:
            run_station(n, template)
            print(f"station-{n}: PASS")
        except Exception as err:  # report every station, not just the first
            failed += 1
            print(f"station-{n}: FAIL\n{err}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
