def setstring(*args, tape: list) -> list:
    tape[int(args[1])] = args[0]
    return tape

def reset(*args, tape: list) -> list:
    tape[int(args[0])] = 0
    return tape

pearcom = {
    "set": setstring,
    "resetint": reset
}
