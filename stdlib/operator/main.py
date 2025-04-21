def lt(*args, tape):
    if tape[int(args[0])] < tape[int(args[1])]:
        tape[int(args[2])] = 1
    else:
        tape[int(args[2])] = 0
    return tape
def gt(*args, tape):
    if tape[int(args[0])] > tape[int(args[1])]:
        tape[int(args[2])] = 1
    else:
        tape[int(args[2])] = 0
    return tape
def eq(*args, tape):
    if tape[int(args[0])] == tape[int(args[1])]:
        tape[int(args[2])] = 1
    else:
        tape[int(args[2])] = 0
    return tape
def Not(*args, tape):
    tape[int(args[1])] = 0 if tape[int(args[0])] == 1 else 1
    return tape
def And(*args, tape):
    tape[int(args[2])] = 1 if tape[int(args[0])] and tape[int(args[1])] else 0
    return tape
def Or(*args, tape):
    tape[int(args[2])] = 1 if tape[int(args[0])] or tape[int(args[1])] else 0
    return tape
pearcom = {
    "lt": lt,
    "gt": gt,
    "eq": eq,
    "not": Not,
    "and": And,
    "or": Or
}
