# ExpensiveProgramming
Program using monzo transaction amounts


# How to write a program
To "Name" a program use the notes field for all of your instructions.

Each instruction is a transaction with the same name.

Note: The system uses mod 8 so 65 pence is the equivilent to 1 pence if you're feeling rich

| Minimum Amount (Pennies)  | Brainfuck Equivalent |
| ------------- | ------------- |
| 10  | Delete previous program of the same name |
| 1  | + |
| 2  | - |
| 3  | > |
| 4  | < |
| 5  | \[ |
| 6  | ] |
| 7  | , |
| 8  | . |

# Requirements
Requires the monzo python library https://github.com/muyiwaolu/monzo-python

# Usage
Create a program. Here's an example:

![Example Program](exampls.png?raw=true "Example Program")

Note: The entire program refuses to screenshot for some reason. Will fix later.

Run:

python run.py

# Calculator Script
Included in the calculator folder is a script for working out the cost of running a Brainfuck program in ExpensiveProgramming.

Usage: ```python calculator.py example.bf``` will output ```£2.50```.

# Notes
This has a clear RCE vulnerability but it's funny so I'm keeping it (Also it's unlikely to break your computer)

# Donate
https://monzo.me/dominiczheyuanhall

I accept donations in the form of programs. I will run them please don't murder my poor laptop.
