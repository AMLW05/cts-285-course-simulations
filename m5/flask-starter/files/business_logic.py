def check_answer(state, submitted):
    expected = str(state["expected_answer"])
    next_state = dict(state)

    if submitted == expected:
        next_state["status"] = "correct"
        return {
            "message": "Correct.",
            "allow_retry": False,
            "reveal_answer": False,
            "state": next_state,
        }

    next_try = state["try_number"] + 1
    next_state["try_number"] = next_try

    if next_try >= 2:
        next_state["status"] = "revealed"
        return {
            "message": f"The correct answer is {expected}.",
            "allow_retry": False,
            "reveal_answer": True,
            "state": next_state,
        }

    next_state["status"] = "retry"
    return {
        "message": "Try again.",
        "allow_retry": True,
        "reveal_answer": False,
        "state": next_state,
    }
