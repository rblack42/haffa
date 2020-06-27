import sys

try:
    fname = sys.argv[1]
except:
    print("Usage: python3 path.py data-file")
    sys.exit(1)


commands = []
with open(fname) as fin:
    data = fin.read()
    parts = data.split()

current_code = ""
commands = []
coords = []

for p in parts:
    if p.isalpha():
        new_code = p[0]
        if not current_code == new_code:
            if not current_code == "":
                commands.append(current_code)
                if not (current_code == "z" or current_code == 'Z'):
                    commands.append(coords)
                coords = []
            current_code = new_code
            continue
    else:
        try:
            c1,c2 = p.split('.')
            coords.append([c1,c2])
        except:
            c1 = p
            coords.append([c1])

print(commands)

for c in commands:
    if len(c) > 1:
        print(c[0], c[1:])
    else: print(c[0])

    return "zero"

def one():
    return "one"

def two():
    return "two"

switcher = {
        0: zero,
        1: one,
        2: two
    }


def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()
