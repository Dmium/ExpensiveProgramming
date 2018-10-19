import sys

if len(sys.argv) == 1:
    print("No file name supplied.")
    sys.exit()

with open(sys.argv[1]) as f:
    input_string = f.read()

values = {
    "+": 1,
    "-": 2,
    ">": 3,
    "<": 4,
    "[": 5,
    "]": 6,
    ",": 7,
    ".": 8
}

total = 0

command_characters = (char for char in input_string if char in "+-><[],.")

for character in command_characters:
    total += values[character]

if total < 100:
    print(str(total) + "p")
else:
    print("£" + str(total)[:-2] + "." + str(total)[-2:])
