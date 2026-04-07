# LEARNING Goal: Understanding References vs. Copies (Mutability)
# This script demonstrates that lists are MUTABLE and how variable references work.
# When you assign tuple_2 = tuple_1, you're creating a REFERENCE, not a copy.
# It teaches: how assignment works with data structures, mutability, and side effects.

# Create a list (mutable data structure)
tuple_1= ['History','Math','Physics','CompSci']
# Assign tuple_2 to reference the SAME list (not a copy)
tuple_2=tuple_1
# Print both - they show the same content
print(tuple_1)
print(tuple_2)
# Modify the first element of tuple_1
tuple_1[0]='Art'
# Notice: tuple_2 ALSO changed! They point to the same list in memory.
print(tuple_1)
print(tuple_2)
# TRY THIS: Use tuple_1[:] or tuple_1.copy() to create a true copy instead of a reference!