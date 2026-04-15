# IB DP CompSci - Imports Exercise

# ---------------------------------------------------------------------------
# PART 1 – STANDARD LIBRARY IMPORTS
# ---------------------------------------------------------------------------

# TODO:
# - Import the math module
# - Print:
#   1) sqrt(81)
#   2) pi rounded to 3 decimal places

# TODO: write your imports here
import math
# TODO: write your prints here
print(math.sqrt(81))
print(round(math.pi, 3))

# ---------------------------------------------------------------------------
# PART 2 – FROM ... IMPORT ...
# ---------------------------------------------------------------------------

# TODO:
# - Import sqrt and floor from math using: from math import ...
# - Use them to:
#   1) compute sqrt(50)
#   2) floor the result

# TODO: write your imports here
from math import sqrt, floor
value = 50
# TODO: compute root
root = sqrt(value)
# TODO: compute floored
floored = floor(root)

print("sqrt(50) =", root)
print("floor(sqrt(50)) =", floored)


# ---------------------------------------------------------------------------
# PART 3 – ALIASES
# ---------------------------------------------------------------------------

# TODO:
# - Import random as rnd
# - Simulate rolling a 6-sided die 10 times
# - Store the results in a list and print it

# TODO: write your imports here
import random as rnd
rolls = []
# TODO: add 10 random ints from 1 to 6
for _ in range(10):
    rolls.append(rnd.randint(1, 6))
print("Rolls:", rolls)


# ---------------------------------------------------------------------------
# PART 4 – IMPORTING YOUR OWN MODULE
# ---------------------------------------------------------------------------

# There is a file in this folder called my_utils.py
# TODO:
# - Import my_utils
# - Use:
#   1) my_utils.shout("hello")
#   2) my_utils.is_even(123)
#   3) my_utils.clamp(200, 0, 100)

# TODO: write your import here
import my_utils
print("Shout:", my_utils.shout("hello"))   # TODO
print("Is even:", my_utils.is_even(123)) # TODO
print("Clamp:", my_utils.clamp(200, 0, 100))   # TODO


# ---------------------------------------------------------------------------
# PART 5 – DEBUGGING IMPORTS (CHALLENGE)
# ---------------------------------------------------------------------------

# TODO:
# - What happens if you create a file named random.py in this folder?
# - Why does that break `import random`?
# - Write your answer as a multi-line string below:
# - Below is an example of a multi-line string:
answer = """
If you create a file named random.py in the same folder as your script,
Python will try to import that file instead of the real built-in random module.
This happens because Python's import system looks in the current directory first.
So 'import random' ends up importing local random.py, which does not contain
the functions (like randint) that the real random module provides.
As a result, your program breaks because you're no longer importing the standard
library module.
TODO: write your explanation here.
"""

print(answer)
