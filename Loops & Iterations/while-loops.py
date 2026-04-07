# LEARNING Goal: while loops, infinite loops, and the break statement
# This script demonstrates a while True loop that repeats until manually stopped.
# It also shows how break can interrupt the loop when a condition is met.

x = 0

while True:
    # Uncomment the following lines to use break and stop the loop when x reaches 5
    # if x == 5:
    #     break
    print(x)
    x += 1

# NOTE: As written, this loop is infinite because the break statement is commented out.
# The x variable increases on each iteration, but the loop still runs forever.
# Try uncommenting the break block to see how the loop stops at x == 5.