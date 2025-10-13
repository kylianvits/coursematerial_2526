def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    skipped = 0
    total = 0
    taken = 0
    if grade1 is None:
        skipped += 1
    else:
        taken += 1
        total += grade1
    if grade2 is None:
        skipped += 1
    else:
        taken += 1
        total += grade2
    if grade3 is None:
        skipped += 1
    else:
        taken += 1
        total += grade3
    if grade4 is None:
        skipped += 1
    else:
        taken += 1
        total += grade4
    if grade5 is None:
        skipped += 1
    else:
        taken += 1
        total += grade5
    if skipped > 1:
        return False
    if taken == 0:
        return False
    average = total / taken
    return average >= 12
 