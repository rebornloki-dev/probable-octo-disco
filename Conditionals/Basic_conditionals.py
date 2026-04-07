# LEARNING Goal: String Comparison and if/elif/else Chains
# This script demonstrates how to compare string values using if/elif/else.
# It teaches: string equality checking, the elif (else if) statement, and control flow.

# Store a programming language name in a variable
language ='Java'

# Check if language is Python
if language == 'Python':
    print('Language is Python')
# If not Python, check if it's Java (elif = else if)
elif language =='Java':
    print('Language is Java')
# If not Java, check if it's Lua
elif language == 'Lua':
    print('Language is Lua')
# If none of the above match
else:
    print('No match')

# TRY THIS: Change the language variable to different values and run again!