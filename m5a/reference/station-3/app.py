"""Station 3: Practice, GET and POST. This file replaces the text menu in menu.py.

It is the only file that knows about Flask, requests, or HTML.
dataman/logic.py and dataman/store.py did not change.

Run:  python -m flask --app app run --debug --host=0.0.0.0
"""
from flask import Flask, render_template, request

from dataman.logic import PracticeSession, Problem, curator_report
from dataman.store import JsonFileStore

app = Flask(__name__)

STORE = JsonFileStore()     # one store for the whole program, made once
PROBLEM = Problem("P1", "7 x 8", 56)
SESSION = "maya-1"


@app.route("/")
def home():
    return "DataMan is running on the web."


@app.route("/practice", methods=["GET", "POST"])
def practice():
    session = PracticeSession(STORE, SESSION, PROBLEM)
    msg = None
    if request.method == "POST":
        raw = request.form.get("answer", "")
        try:
            answer = int(raw)
        except ValueError:
            answer = None
        if session.is_finished():
            msg = "This session is finished. Choose report."
        elif answer is None:
            msg = "Enter a whole number."
        else:
            out = session.submit(answer)
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
