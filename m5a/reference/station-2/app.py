"""Station 2: Report, a GET page. This file replaces the text menu in menu.py.

It is the only file that knows about Flask, requests, or HTML.
dataman/logic.py and dataman/store.py did not change.

Run:  python -m flask --app app run --debug --host=0.0.0.0
"""
from flask import Flask, render_template

from dataman.logic import Problem, curator_report
from dataman.store import JsonFileStore

app = Flask(__name__)

STORE = JsonFileStore()     # one store for the whole program, made once
PROBLEM = Problem("P1", "7 x 8", 56)
SESSION = "maya-1"


@app.route("/")
def home():
    return "DataMan is running on the web."


@app.route("/report")
def report():
    rep = curator_report(STORE, SESSION, PROBLEM.id)
    return render_template("report.html", session_id=SESSION, rep=rep)
