# LEARNING Goal: Object Identity vs. Equality (is operator)
# This script demonstrates the difference between '==' (value equality) and 'is' (identity).
# It teaches: how Python stores objects in memory, variable references, and the id() function.

# Create a list
a = [1, 2, 3]
# Assign b to reference the SAME list object (not a copy)
b = a

# Print the unique memory address (id) of list a
print(id(a))
# Print the unique memory address (id) of list b
print(id(b))
# The 'is' operator checks if both variables point to the SAME object in memory
# This will print True because a and b point to the exact same list
print (a is b)

# TRY THIS: Create c = [1, 2, 3] (a new list) and compare: print(a == c) vs print(a is c)