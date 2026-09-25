# Verification — not student material

**Nothing in this directory is for students.** It is course QA: it runs the commands the Canvas
pages publish and reports whether they work. It is listed here, and in the root `README.md`, for
the same reason `m2/elicitation-vn-spike/` is — so that nobody who finds it has to guess what it is.

It answers two issues in the private source repository with evidence instead of assurance:

- **#127** — verify M5 technical delivery in a student Codespace
- **#106** — verify the M7 persistence workflow end to end in a student Codespace

## Why the checks live here and the answers do not

`check_starter.py` is written once and takes the starter package as an argument, so the public and
private callers run the same code and cannot drift.

What each caller may check is decided by what may be public:

| Caller | Checks | Why |
|---|---|---|
| this repository, in CI | package shape, venv, install, resolved versions, the app over HTTP | every input is already public |
| the private source repository | the above, plus the M6 test suite, both controlled failure variants, the SQLite reference, source-to-distributed parity | students write the M7 SQLite `data_store.py` themselves; a reference implementation published here would publish the answer to graded work |

The private caller fetches this script rather than copying it. This repository is public, so that
needs no credential.

## Running it

```
python3 verification/check_starter.py --package m5/flask-starter/files
```

With the private inputs, from a checkout of the source repository beside this one:

```
python3 verification/check_starter.py \
  --package m5/flask-starter/files \
  --suite      ../cts-285_SOURCE/module-06/exemplars/test_dataman.py \
  --variant    ../cts-285_SOURCE/module-07/student-facing/failure-variants/data_store-write-never-lands.py \
  --variant    ../cts-285_SOURCE/module-07/student-facing/failure-variants/data_store-load-reseeds.py \
  --parity-against ../cts-285_SOURCE/module-05/starter/minimal-flask-app
```

The starter is never modified. Every check runs against a copy in a temporary directory.

## What a pass means, and what it does not

**A pass here is not a Codespaces verification.** The script prints that on every run, above the
results, because the distinction is the whole reason the two issues exist. A pass says the command
form is sound on a clean Linux box with the interpreter named in the environment stamp. It says
nothing about the forwarded port, the Codespaces image's Python version, or whether bare `python`
exists on `PATH` before the virtual environment is activated.

## Two tiers, deliberately

`FAIL` is a broken command or a broken starter. Differences that are intentional — the two starter
READMEs, which read differently on purpose — are reported and do not change the exit status.

A repository-wide gate would be red on arrival from inherited drift, and a check that is red on
arrival is one people learn to ignore. The source repository's `house-style.yml` splits its tiers
the same way and says so in its own header.

## If a check fails

The published page is the specification and this script is the defect, unless the failure is in the
starter itself. Fix the technical direction in place. Neither issue authorises reopening the
instructional sequence: both are labelled *instructional redesign: No*.
