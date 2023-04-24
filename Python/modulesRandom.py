# random function

import random

var = random.choice(["heads","tails"])
print(f"{var}")

# to import a function from library of random
"""from random import choice"""

number = random.randint(1,10)
print(number)

cards = ["jack","king","queen"]
random.shuffle(cards)

print(cards)