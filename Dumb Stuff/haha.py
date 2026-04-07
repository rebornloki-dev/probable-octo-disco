# LEARNING Goal: String Input and Simple Conditional Logic
# This script demonstrates basic user input and branching logic.
# It teaches: getting and comparing string input, if/else statements, and simple program flow.

# Get user input asking a yes/no question
anime = input ("Do you like Naruto? yes/no")
# Check if the user answered "yes"
if anime == "yes":
    # Respond if user likes Naruto
    print("You are a ninja now")
else:
    # Respond if user doesn't like Naruto or gave a different answer
    print("Civilian Literally")

# TRY THIS: Add .lower() to handle both "Yes" and "yes": if anime.lower() == "yes"