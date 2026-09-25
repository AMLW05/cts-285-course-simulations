#!/usr/bin/env python3
"""Run the published CTS-285 command sequence against a Flask starter package.

NOT STUDENT MATERIAL. This is course-QA tooling. See verification/README.md.

It exists to answer the checklists in cts-285_SOURCE issues #127 and #106 with
evidence rather than with assurance. Every command it runs is copied from a
published page, not paraphrased, because the thing under test IS the published
command. Where this file and a Canvas page disagree about a command, the page is
the specification and this file is the defect.

Usage:
    python3 check_starter.py --package <dir>            # M5 checks only
    python3 check_starter.py --package <dir> \
        --suite <test_dataman.py> \
        --variant <data_store-*.py> --variant <...>     # adds the private checks

The package is a directory holding app.py, business_logic.py, data_store.py,
requirements.txt and templates/. It is never modified: every check runs against a
copy in a temporary directory.
"""

import argparse
import hashlib
import os
import platform
import shutil
import signal
import socket
import sqlite3
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

# The published command set, verbatim. m7-persistence-technical-build-gate.md
# "Question 7 - the commands, and there is only one set", and the two lines
# module-05/final-build/05 already teaches.
VENV_CREATE = "python3 -m venv .venv"
VENV_ACTIVATE = "source .venv/bin/activate"
INSTALL = "python -m pip install -r requirements.txt"
RUN = "python -m flask --app app run --debug --host=0.0.0.0"

# Flask's default when the published run command names no port.
PORT = 5000

REQUIRED_FILES = [
    "app.py",
    "business_logic.py",
    "data_store.py",
    "requirements.txt",
    os.path.join("templates", "index.html"),
]

PASS, FAIL, SKIP = "PASS", "FAIL", "SKIP"


class Report:
    def __init__(self):
        self.rows = []

    def add(self, check_id, issue_line, status, detail=""):
        self.rows.append((check_id, issue_line, status, detail))
        marker = {PASS: "PASS", FAIL: "FAIL", SKIP: "skip"}[status]
        print(f"  {marker}  {check_id}")
        if detail:
            for line in str(detail).splitlines():
                print(f"          {line}")

    @property
    def failed(self):
        return any(r[2] == FAIL for r in self.rows)

    def table(self):
        width = max(len(r[0]) for r in self.rows)
        out = ["", "=" * 72, "RESULTS", "=" * 72]
        for check_id, issue_line, status, _ in self.rows:
            out.append(f"{status:<5} {check_id:<{width}}  {issue_line}")
        counts = {s: sum(1 for r in self.rows if r[2] == s) for s in (PASS, FAIL, SKIP)}
        out.append("-" * 72)
        out.append(f"{counts[PASS]} passed, {counts[FAIL]} failed, {counts[SKIP]} skipped")
        return "\n".join(out)


def sh(command, cwd, timeout=300):
    """Run a command through bash so `source` genuinely activates the venv."""
    return subprocess.run(
        ["bash", "-c", command],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def in_venv(command):
    return f"{VENV_ACTIVATE} && {command}"


def stamp():
    print("=" * 72)
    print("ENVIRONMENT")
    print("=" * 72)
    print(f"  python3        {platform.python_version()} ({sys.executable})")
    print(f"  bare `python`  {shutil.which('python') or 'NOT ON PATH'}")
    print(f"  sqlite3        {sqlite3.sqlite_version}")
    print(f"  platform       {platform.platform()}")
    print("")
    print("  THIS IS NOT A GITHUB CODESPACE. Any check below that passes here")
    print("  says the command form is sound, not that it is verified in the")
    print("  environment students will use.")
    print("")


def port_free(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        return s.connect_ex(("127.0.0.1", port)) != 0


def check_shape(package, report):
    missing = [f for f in REQUIRED_FILES if not os.path.exists(os.path.join(package, f))]
    if missing:
        report.add("package-shape", "#127 starter runs", FAIL, f"missing: {', '.join(missing)}")
        return False
    report.add("package-shape", "#127 starter runs", PASS, f"{len(REQUIRED_FILES)} required files present")
    return True


def check_venv_and_install(work, report):
    r = sh(VENV_CREATE, work)
    if r.returncode != 0:
        report.add("venv-create", "#127 venv can be created as taught", FAIL, r.stderr.strip()[:400])
        return False
    report.add("venv-create", "#127 venv can be created as taught", PASS, VENV_CREATE)

    r = sh(in_venv("python -c 'import sys; print(sys.executable)'"), work)
    if r.returncode != 0 or ".venv" not in r.stdout:
        report.add("venv-activate", "#127 venv can be activated as taught", FAIL,
                   f"`python` after activation resolved to: {r.stdout.strip() or r.stderr.strip()}")
        return False
    report.add("venv-activate", "#127 venv can be activated as taught", PASS,
               f"`python` resolves inside the venv: {r.stdout.strip()}")

    r = sh(in_venv(INSTALL), work)
    if r.returncode != 0:
        report.add("install", "#127 requirements.txt installs correctly", FAIL, r.stderr.strip()[:400])
        return False
    report.add("install", "#127 requirements.txt installs correctly", PASS, INSTALL)

    r = sh(in_venv("python -m pip freeze"), work)
    if r.returncode != 0:
        report.add("resolved-versions", "requirements.txt is a range, not a pin", FAIL,
                   f"could not read the resolved set: {r.stderr.strip()[:300]}")
        return True
    resolved = " ".join(sorted(x for x in r.stdout.split() if x))
    report.add("resolved-versions", "requirements.txt is a range, not a pin", PASS, resolved)
    return True


def check_app_over_http(work, report):
    if not port_free(PORT):
        report.add("app-serves", "#127 starter runs", FAIL, f"port {PORT} already in use; cannot run the published command")
        return

    proc = subprocess.Popen(
        ["bash", "-c", in_venv(RUN)],
        cwd=work,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        start_new_session=True,
    )
    try:
        base = f"http://127.0.0.1:{PORT}"
        deadline = time.time() + 30
        body = None
        while time.time() < deadline:
            if proc.poll() is not None:
                break
            try:
                with urllib.request.urlopen(base + "/", timeout=2) as resp:
                    body = resp.read().decode()
                    break
            except (urllib.error.URLError, ConnectionError, OSError):
                time.sleep(0.4)

        if body is None:
            out = proc.stdout.read() if proc.poll() is not None else "(still running, never answered)"
            report.add("app-serves", "#127 starter runs", FAIL, f"no response within 30s\n{out[:400]}")
            return
        report.add("app-serves", "#127 starter runs", PASS, f"{RUN} -> GET / 200")

        if "DataMan Answer Checker" not in body:
            report.add("app-renders", "#127 starter runs", FAIL, "GET / did not render the template heading")
        else:
            report.add("app-renders", "#127 starter runs", PASS, "template rendered")

        def post(answer):
            """Return the body, or None if the route failed.

            A 4xx or 5xx here is the starter being broken, which is the thing this
            harness reports. Letting it raise killed the run before the results
            table printed, so the one failure worth catching was the one that
            produced no report.
            """
            data = urllib.parse.urlencode({"answer": answer}).encode()
            try:
                with urllib.request.urlopen(base + "/answer", data=data, timeout=5) as resp:
                    return resp.read().decode()
            except (urllib.error.URLError, ConnectionError, OSError):
                return None

        first = post("41")
        if first is None:
            report.add("rule-first-try", "two-try rule, manual p.20", FAIL,
                       "POST /answer did not return a response")
            report.add("rule-second-try", "two-try rule, manual p.20", FAIL,
                       "not reached; POST /answer failed")
            return
        if "Try again." in first:
            report.add("rule-first-try", "two-try rule, manual p.20", PASS, "first wrong answer -> Try again.")
        else:
            report.add("rule-first-try", "two-try rule, manual p.20", FAIL, "first wrong answer did not invite a retry")

        second = post("41")
        if second is None:
            report.add("rule-second-try", "two-try rule, manual p.20", FAIL,
                       "POST /answer did not return a response on the second try")
        elif "The correct answer is 42." in second:
            report.add("rule-second-try", "two-try rule, manual p.20", PASS, "second wrong answer -> answer revealed")
        else:
            report.add("rule-second-try", "two-try rule, manual p.20", FAIL, "second wrong answer did not reveal")
    finally:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
            proc.wait(timeout=10)
        except Exception:
            pass


def run_suite(package, suite):
    # The suite path must be absolute before it reaches the child. cwd is set to
    # the suite's own directory, so a RELATIVE --suite -- which is the form this
    # repository's README documents -- would be resolved against that directory
    # and never found. Verified by review, not by this harness, because every run
    # here had passed an absolute path.
    suite = os.path.abspath(suite)
    r = subprocess.run(
        [sys.executable, suite],
        cwd=os.path.dirname(suite) or ".",
        # PYTHONDONTWRITEBYTECODE: without it the suite writes __pycache__ into the
        # package it is pointed at, so a check that claims to leave the starter
        # untouched quietly modifies it. Found by the artefacts turning up staged.
        env={
            **os.environ,
            "PYTHONPATH": os.path.abspath(package),
            "PYTHONDONTWRITEBYTECODE": "1",
        },
        capture_output=True,
        text=True,
        timeout=120,
    )
    return r


def check_suite(package, suite, report):
    # Copy first, as check_variant already does. The suite can write a database or
    # other artefacts beside the module it imports, and the README promises every
    # check runs against a copy. Suppressing bytecode was not enough to make that
    # true; only copying is.
    with tempfile.TemporaryDirectory() as tmp:
        copy = os.path.join(tmp, "pkg")
        shutil.copytree(package, copy)
        r = run_suite(copy, suite)
    tail = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[:200]
    if r.returncode == 0:
        report.add("suite-green", "#106 M6 regression suite runs unchanged", PASS, tail)
    else:
        report.add("suite-green", "#106 M6 regression suite runs unchanged", FAIL, f"exit {r.returncode}: {tail}")


def check_variant(package, suite, variant, report):
    name = os.path.basename(variant)
    with tempfile.TemporaryDirectory() as tmp:
        swapped = os.path.join(tmp, "pkg")
        shutil.copytree(package, swapped)
        shutil.copyfile(variant, os.path.join(swapped, "data_store.py"))
        r = run_suite(swapped, suite)

    failing = [l for l in r.stdout.splitlines() if l.startswith("FAIL")]
    passing = [l for l in r.stdout.splitlines() if l.startswith("PASS")]
    expected = "Storage accepted the write and did not keep it."

    if r.returncode == 0:
        report.add(f"variant:{name}", "#106 variant produces the intended failure", FAIL,
                   "suite passed; the variant did not turn the storage test red")
    elif len(failing) == 1 and len(passing) == 3 and expected in r.stdout:
        report.add(f"variant:{name}", "#106 variant produces the intended failure", PASS,
                   f"3 pure-logic tests green, storage test red\n{failing[0]}")
    else:
        report.add(f"variant:{name}", "#106 variant produces the intended failure", FAIL,
                   f"expected 3 PASS + 1 FAIL carrying the storage message; got "
                   f"{len(passing)} PASS, {len(failing)} FAIL\n{r.stdout.strip()[-400:]}")


def check_sqlite_reference(package, suite, reference, schema, report):
    """#106: the SQLite path initializes, and progress survives a process restart.

    Restart survival is checked across two separate interpreter processes, not two
    calls in one. A module-level dict survives the second; only storage survives
    the first, which is the whole property M7 introduces.
    """
    with tempfile.TemporaryDirectory() as tmp:
        pkg = os.path.join(tmp, "pkg")
        shutil.copytree(package, pkg)
        shutil.copyfile(reference, os.path.join(pkg, "data_store.py"))
        shutil.copyfile(schema, os.path.join(pkg, "schema.sql"))

        env = {**os.environ, "PYTHONPATH": pkg, "PYTHONDONTWRITEBYTECODE": "1"}

        def run(code):
            return subprocess.run([sys.executable, "-c", code], cwd=pkg, env=env,
                                  capture_output=True, text=True, timeout=60)

        r = run("import data_store; data_store.load_state()")
        if r.returncode != 0:
            report.add("sqlite-init", "#106 SQLite path creates/initializes", FAIL,
                       r.stderr.strip()[-400:])
            return
        made = [f for f in os.listdir(pkg) if f.endswith(".db")]
        if not made:
            report.add("sqlite-init", "#106 SQLite path creates/initializes", FAIL,
                       "first storage call created no database file")
            return
        report.add("sqlite-init", "#106 SQLite path creates/initializes", PASS,
                   f"first storage call created {made[0]} from schema.sql")

        r = run("import sqlite3, data_store; data_store.load_state();"
                " c = sqlite3.connect(data_store.DATABASE_FILE);"
                " c.execute(\"INSERT INTO dataman_state (id, problem, expected_answer,"
                " try_number, status) VALUES (2, 'x', 1, 0, 'new')\")")
        if "CHECK constraint failed" in r.stderr:
            report.add("sqlite-one-row", "gate: CHECK (id = 1) is the schema's rule", PASS,
                       "a second row is refused by the database, not by convention")
        else:
            report.add("sqlite-one-row", "gate: CHECK (id = 1) is the schema's rule", FAIL,
                       f"a second row was accepted (exit {r.returncode})")

        # Process one: answer wrong, save, exit.
        r = run("import data_store, business_logic;"
                " o = business_logic.check_answer(data_store.load_state(), '41');"
                " data_store.save_state(o['state'])")
        if r.returncode != 0:
            report.add("sqlite-restart", "#106 progress survives a restart", FAIL,
                       r.stderr.strip()[-400:])
            return

        # Process two: a genuinely new interpreter. Nothing in memory carries over.
        r = run("import data_store; s = data_store.load_state();"
                " print(s['try_number'], s['status'])")
        got = r.stdout.strip()
        if got == "1 retry":
            report.add("sqlite-restart", "#106 progress survives a restart", PASS,
                       "a second process read back try_number=1, status=retry")
        else:
            report.add("sqlite-restart", "#106 progress survives a restart", FAIL,
                       f"expected '1 retry' from a fresh process, got {got!r} "
                       f"{r.stderr.strip()[-200:]}")

        if suite:
            r = run_suite(pkg, suite)
            tail = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]
            if r.returncode == 0:
                report.add("sqlite-suite", "#106 M6 suite unchanged across the swap", PASS, tail)
            else:
                report.add("sqlite-suite", "#106 M6 suite unchanged across the swap", FAIL,
                           f"exit {r.returncode}: {tail}")


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def check_parity(package, other, report):
    """Code parity is a hard failure. README drift is reported, not gated.

    The two READMEs differ on purpose: the distributed copy addresses the student
    in the second person and lists requirements.txt, which the source copy omits.
    That is a provenance question, and the simulations repo's milestone 16 already
    carries it as "provenance headers where exported/support copies intentionally
    differ". Gating on it would make this check red on arrival, which is how a
    check teaches people to ignore it.
    """
    diffs, same = [], 0
    for rel in REQUIRED_FILES:
        a, b = os.path.join(package, rel), os.path.join(other, rel)
        if not os.path.exists(a) or not os.path.exists(b):
            diffs.append(f"{rel}: missing on one side")
            continue
        if sha(a) == sha(b):
            same += 1
        else:
            diffs.append(f"{rel}: {sha(a)} != {sha(b)}")
    if diffs:
        report.add("starter-parity-code", "source-to-distributed parity", FAIL,
                   f"{same} identical; differing:\n" + "\n".join(diffs))
    else:
        report.add("starter-parity-code", "source-to-distributed parity", PASS,
                   f"all {same} code and template files identical")

    a, b = os.path.join(package, "README.md"), os.path.join(other, "README.md")
    missing = [side for side, path in (("package", a), ("other", b)) if not os.path.exists(path)]
    if missing:
        report.add("starter-parity-readme", "reported, not gated", SKIP,
                   f"no README.md on the {' and '.join(missing)} side; nothing compared")
    elif sha(a) != sha(b):
        report.add("starter-parity-readme", "reported, not gated", SKIP,
                   f"the two READMEs differ ({sha(a)} != {sha(b)}); intentional register "
                   f"difference, wants a provenance header")
    else:
        report.add("starter-parity-readme", "reported, not gated", PASS, "READMEs identical")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--package", required=True, help="the Flask starter directory to verify")
    p.add_argument("--suite", help="path to test_dataman.py (private source repo)")
    p.add_argument("--variant", action="append", default=[], help="a controlled failure variant (repeatable)")
    p.add_argument("--parity-against", help="a second starter copy to compare against")
    p.add_argument("--sqlite-reference", help="a SQLite data_store.py to verify (private source repo)")
    p.add_argument("--sqlite-schema", help="the schema.sql it reads")
    args = p.parse_args()

    package = os.path.abspath(args.package)
    report = Report()
    stamp()

    print("CHECKS")
    print("-" * 72)
    if not check_shape(package, report):
        print(report.table())
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        work = os.path.join(tmp, "app")
        shutil.copytree(package, work)
        if check_venv_and_install(work, report):
            check_app_over_http(work, report)

    if args.suite:
        check_suite(package, args.suite, report)
        for variant in args.variant:
            check_variant(package, args.suite, variant, report)
    else:
        report.add("suite-green", "#106 M6 regression suite", SKIP, "no --suite given (lives in the private source repo)")

    if args.sqlite_reference and args.sqlite_schema:
        check_sqlite_reference(package, args.suite, os.path.abspath(args.sqlite_reference),
                               os.path.abspath(args.sqlite_schema), report)
    else:
        report.add("sqlite-restart", "#106 SQLite persistence", SKIP,
                   "no --sqlite-reference given (lives in the private source repo)")

    if args.parity_against:
        check_parity(package, os.path.abspath(args.parity_against), report)
    else:
        report.add("starter-parity-code", "source-to-distributed parity", SKIP, "no --parity-against given")

    print(report.table())
    return 1 if report.failed else 0


if __name__ == "__main__":
    sys.exit(main())
