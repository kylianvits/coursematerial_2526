def multiple_choice(right_answer, given_answer):
    if right_answer==given_answer:
        return 1
    if right_answer!=given_answer and given_answer is not None:
        return -0.2
    if given_answer is None:
        return 0