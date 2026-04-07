# LEARNING Goal: Nested Loops (Loops within Loops)
# This script demonstrates how to use nested for loops to iterate through multiple sequences.
# It teaches: the for loop structure, nested loops, and how iteration combines multiple sequences.

# Create a list of numbers
nums = [1,2,3,4,5]

# Outer loop: iterate through each number in the list
for num in nums:
    # Inner loop: for each number, iterate through each letter in the string 'abc'
    for letter in 'abc':
        # Print the combination of number and letter
        # This will print: 1 a, 1 b, 1 c, 2 a, 2 b, 2 c, etc.
        print(num,letter)

# TRY THIS: Modify the code to:
# - Change the outer list to different numbers
# - Change the inner string to different letters
# - Print the output in a table format using tabs or formatting