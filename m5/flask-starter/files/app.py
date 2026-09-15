from flask import Flask, render_template, request

from business_logic import check_answer
from data_store import load_state, save_state

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    state = load_state()
    return render_template("index.html", state=state, outcome=None)


@app.route("/answer", methods=["POST"])
def answer():
    submitted = request.form.get("answer", "").strip()
    state = load_state()
    outcome = check_answer(state, submitted)
    save_state(outcome["state"])
    return render_template("index.html", state=outcome["state"], outcome=outcome)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
