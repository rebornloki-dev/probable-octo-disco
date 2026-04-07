# LEARNING Goal: Understanding Tuples (Immutable Data Structures)
# This script attempts to modify a tuple to demonstrate that tuples are IMMUTABLE.
# It teaches: the difference between tuples () and lists [], immutability, and error handling.

# Create a tuple (immutable: cannot be changed after creation)
tuple_1= ('History','Math','Physics','CompSci')
# Create a reference to the same tuple
tuple_2= tuple_1
# Print both tuples (they contain the same data)
print(tuple_1)
print(tuple_2)
# TRY TO modify the first element of the tuple
# WARNING: This will cause a TypeError because tuples are immutable!
tuple_1[0]='Art' 
print(tuple_1)
print(tuple_2)

# NOTE: If you run this, Python will throw an error: "'tuple' object does not support item assignment"
# Compare this to Sets & Tuples/learning_sets.py where we modify a list - that works!
