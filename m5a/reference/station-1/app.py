"""Station 1: Hello, route. This file replaces the text menu in menu.py.

It is the only file that knows about Flask, requests, or HTML.
dataman/logic.py and dataman/store.py did not change.

Run:  python -m flask --app app run --debug --host=0.0.0.0
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "DataMan is running on the web."
