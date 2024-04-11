# mid unit activety
# Author: Alex
# 11 April 2024

import random

def generate_number(min_num, max_num):
    """Generate a random number between min_num and max_num."""

    return random.randint(min_num, max_num)
def play_game(secret_number, attempts):
    """Play the number guessing game."""

    print("HI! Welcome! This is a number guessing game!")

    print(f"I'm thinking of a number between {min_num} and {max_num}.")
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))
        if guess == secret_number:
            print("WOW! you managed to guess the correct number congratulations! I did not expect that.")
            break
        elif guess < secret_number:
            print("oh no. Try a higher number.")
        else:
            print("uh no. Try a lower number.")
    else:
        print(f"Unfortunate, you've run out of attempts. The correct number was {secret_number}.")

# Define the range of numbers for the game
min_num = 1
max_num = 100

# Number of attempts allowed for the player
attempts = 10

# Generate a secret number
secret_number = generate_number(min_num, max_num)

# Play the game
play_game(secret_number, attempts)