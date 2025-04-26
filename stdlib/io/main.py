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

def In(*args, tape: list) -> list:
    intype = args[0]
    reg = int(args[1])
    prompt = args[2] if len(args) == 3 else None
    
    if intype == "int":
        tape[reg] = int(input("" if prompt == None else prompt))
    elif intype == "float":
        tape[reg] = float(input("" if prompt == None else prompt))
    elif intype == "str":
        tape[reg] = input("" if prompt == None else prompt)
    else:
        print(f"Invalid type: {intype}")
        
    return tape

pearcom = {
    "print": output,
    "printc": outputc,
    "printable": printable,
    "println": println,
    "in": In
}
