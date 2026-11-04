"""Station 6: The refresh problem. This file replaces the text menu in menu.py.

It is the only file that knows about Flask, requests, or HTML.
dataman/logic.py and dataman/store.py did not change.

Run:  python -m flask --app app run --debug --host=0.0.0.0
"""
from flask import Flask, flash, redirect, render_template, request, url_for

from dataman.logic import (MemoryBank, PracticeSession, Problem, SetFull,
                           curator_report)
from dataman.store import JsonFileStore

app = Flask(__name__)
app.secret_key = "dev-only-change-me"   # signs flash messages; not a real secret

STORE = JsonFileStore()     # one store for the whole program, made once
PROBLEM = Problem("P1", "7 x 8", 56)
SESSION = "maya-1"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/practice", methods=["GET", "POST"])
def practice():
    session = PracticeSession(STORE, SESSION, PROBLEM)
    if request.method == "POST":
        raw = request.form.get("answer", "")
        try:
            answer = int(raw)
        except ValueError:
            answer = None
        if session.is_finished():
            flash("This session is finished. Choose report.")
        elif answer is None:
            flash("Enter a whole number.")
        else:
            out = session.submit(answer)
            if out.status == "correct":
                flash("Correct.")
            elif out.status == "retry":
                flash("Not yet. Try again.")
            else:
                flash(f"The answer is {out.revealed_answer}.")
        return redirect(url_for("practice"))
    return render_template("practice.html", problem=PROBLEM,
                           try_number=session.next_try(),
                           finished=session.is_finished())


@app.route("/report")
def report():
    rep = curator_report(STORE, SESSION, PROBLEM.id)
    return render_template("report.html", session_id=SESSION, rep=rep)


@app.route("/bank", methods=["GET", "POST"])
def bank():
    memory_bank = MemoryBank(STORE, "set-1")
    if request.method == "POST":
        pid = request.form.get("problem_id", "").strip()
        try:
            memory_bank.add_problem(pid)
            flash(f"Added. Set holds {len(memory_bank.members())}.")
        except SetFull as err:
            flash(f"Refused: {err}")
        return redirect(url_for("bank"))
    return render_template("bank.html", members=memory_bank.members())
