# Demonstrate some parts of the random module

import random

def coin_flip():
    # Return either heads, tails, or other?
    # Heads -- (0, 0.5)
    # Tails -- (0.5, 0.999999)
    # Other --- the rest
    result = random.random()

    if result < 0.5:
        return "heads"
    elif result < 0.9999999:
        return "tails"
    else:
        return "other"
    
def main():

    heads = 0
    tails = 0
    others = 0

    for _ in range(1_000_000):
     
     result = coin_flip

    if result == "heads":
        heads = heads + 1 # increment
    elif result == "tails":
        tails += 1 # increment



