_STATE = {
    "problem": "6 × 7",
    "expected_answer": 42,
    "try_number": 0,
    "status": "new",
}


def load_state():
    return dict(_STATE)


def save_state(new_state):
    _STATE.update(new_state)
