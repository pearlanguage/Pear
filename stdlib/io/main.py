from sys import stdout
stdout.flush()
def output(*args, tape: list) -> list:
    stdout.write(str(tape[int(args[0])]))
    stdout.flush()
    return tape

def outputc(*args, tape: list) -> list:
    try:
        stdout.write(chr(int(tape[int(args[0])])))
        stdout.flush()
    except Exception:
        stdout.write('?')
        stdout.flush()
    return tape

def printable(*args, tape: list) -> list:
    if str(tape[int(args[0])]).isprintable():
        tape[int(args[1])] = 1
    else:
        tape[int(args[1])] = 0
    return tape

def println(*args, tape: list) -> list:
    print(tape[int(args[0])])
    return tape

pearcom = {
    "print": output,
    "printc": outputc,
    "printable": printable,
    "println": println
}
