# LEARNING Goal: Simple Game Logic with Input and Conditionals
# This script creates a basic number guessing game.
# It teaches: user input, type conversion (int()), variables, and if/else statements.

# Store the secret number that the player needs to guess
secret = 7
# Get the player's guess and convert it from string to integer
guess= int(input("Guess the number:"))
# Check if the guess matches the secret number
if guess == secret:
 # Player guessed correctly
 print("You win")
else:
 # Player guessed wrong
 print("Nope")

# TRY THIS: Extend this game by:
# - Allowing multiple guesses in a loop
# - Enabling a random secret number (import random)
# - Giving hints ("Too high!" or "Too low!")