"""Station 5: The menu becomes a page. This file replaces the text menu in menu.py.

It is the only file that knows about Flask, requests, or HTML.
dataman/logic.py and dataman/store.py did not change.

Run:  python -m flask --app app run --debug --host=0.0.0.0
"""
from flask import Flask, render_template, request

from dataman.logic import (MemoryBank, PracticeSession, Problem, SetFull,
                           curator_report)
from dataman.store import JsonFileStore

app = Flask(__name__)

STORE = JsonFileStore()     # one store for the whole program, made once
PROBLEM = Problem("P1", "7 x 8", 56)
SESSION = "maya-1"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/practice", methods=["GET", "POST"])
def practice():
    session = PracticeSession(STORE, SESSION, PROBLEM)
    msg = None
    if request.method == "POST":
        raw = request.form.get("answer", "")
        if session.is_finished():
            msg = "This session is finished. Choose report."
        elif not raw.strip().lstrip("-").isdigit():
            msg = "Enter a whole number."
        else:
            out = session.submit(int(raw))
            if out.status == "correct":
                msg = "Correct."
            elif out.status == "retry":
                msg = "Not yet. Try again."
            else:
                msg = f"The answer is {out.revealed_answer}."
    return render_template("practice.html", problem=PROBLEM,
                           try_number=session.next_try(),
                           finished=session.is_finished(), message=msg)


@app.route("/report")
def report():
    rep = curator_report(STORE, SESSION, PROBLEM.id)
    return render_template("report.html", session_id=SESSION, rep=rep)


@app.route("/bank", methods=["GET", "POST"])
def bank():
    memory_bank = MemoryBank(STORE, "set-1")
    msg = None
    if request.method == "POST":
        pid = request.form.get("problem_id", "").strip()
        try:
            memory_bank.add_problem(pid)
            msg = f"Added. Set holds {len(memory_bank.members())}."
        except SetFull as err:
            msg = f"Refused: {err}"
    return render_template("bank.html", members=memory_bank.members(),
                           message=msg)
