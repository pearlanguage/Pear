import sys
import os
import importlib.util
from sys import stdout

def run(lines):
    pc = 0  # Program counter
    tape = [0 for _ in range(1024)]  # Memory
    loaded_packages = {}  # Loaded pear packages
    skip_mode = False  # If we currently skip one for an if statement
    if_stack = []  # Nesting stack for if-end statements

    while pc < len(lines):
        line = lines[pc].strip()
        
        # Skip empty lines
        if not line:
            pc += 1
            continue

        tokens = []
        current_token = ''
        in_string = False  # To track if we are inside a string literal
        for char in line:
            if char == '"' and not in_string:
                in_string = True
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
            elif char == '"' and in_string:
                in_string = False
                # Remove quotes from string literals
                tokens.append(current_token)
                current_token = ''
            elif char == ' ' and not in_string:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
            else:
                current_token += char

        if current_token:  # Append any remaining token after the loop
            tokens.append(current_token)

        # Ensure there are tokens before proceeding
        if not tokens:
            print(f"[pear] Error: Empty command or invalid syntax at line {pc + 1}")
            pc += 1
            continue
        
        cmd = tokens[0]

        # Skip logic for if-statements
        if skip_mode:
            if cmd == "if":
                if_stack.append("if")
            elif cmd == "end":
                if_stack.pop()
                if not if_stack:
                    skip_mode = False
            pc += 1
            continue

        # Internal command's
        if cmd == "insert":
            try:
                num = float(tokens[1])
                out = int(tokens[2])
                tape[out] = num
            except (IndexError, ValueError) as e:
                print(f"[insert] Error on line {pc + 1}: {e}")

        elif cmd == "include":
            try:
                package = tokens[1]
                package_path = os.path.join(package, "main.py")

                spec = importlib.util.spec_from_file_location(f"{package}.main", package_path)
                mod = importlib.util.module_from_spec(spec)
                sys.modules[f"{package}.main"] = mod
                spec.loader.exec_module(mod)

                pearcom = getattr(mod, "pearcom", {})
                if len(tokens) != 3:
                    loaded_packages[package] = pearcom
                else:
                    loaded_packages[tokens[2]] = pearcom
            except Exception as e:
                print(f"[include] Error with loading of '{package}': {e}")

        elif cmd == "add":
            tape[int(tokens[3])] = tape[int(tokens[1])] + tape[int(tokens[2])]
        elif cmd == "sub":
            tape[int(tokens[3])] = tape[int(tokens[1])] - tape[int(tokens[2])]
        elif cmd == "mul":
            tape[int(tokens[3])] = tape[int(tokens[1])] * tape[int(tokens[2])]
        elif cmd == "div":
            tape[int(tokens[3])] = tape[int(tokens[1])] / tape[int(tokens[2])]
        elif cmd == "mod":
            tape[int(tokens[3])] = tape[int(tokens[1])] % tape[int(tokens[2])]
        
        elif cmd == "jump":
            pc = tape[int(tokens[1])]
            continue

        elif cmd == "if":
            try:
                reg = int(tokens[1])
                if tape[reg] != 1:
                    skip_mode = True
                    if_stack = ["if"]
            except Exception as e:
                print(f"[if] Error on line {pc + 1}: {e}")
        elif cmd == "end":
            pass  # handled during skip_mode

        # External package command's
        elif cmd in loaded_packages:
            try:
                subcmd = tokens[1]
                args = tokens[2:]
                pearcom = loaded_packages[cmd]

                if subcmd in pearcom:
                    # If it's a string literal command, pass it without quotes
                    if args and args[0].startswith('"') and args[0].endswith('"'):
                        args[0] = args[0][1:-1]  # Remove the surrounding quotes
                    tape = pearcom[subcmd](*args, tape=tape)
                else:
                    print(f"[{cmd}] Unknown subcommand '{subcmd}'")
            except Exception as e:
                print(f"[{cmd}] Failed while executing '{subcmd}': {e}")

        else:
            print(f"[pear] Unknown command: '{cmd}' at line {pc + 1}")

        pc += 1

# Entry point: read Pear-file from argv[1]
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pear_interpreter.py script.pear")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        run(f.readlines())
