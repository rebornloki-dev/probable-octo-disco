# LEARNING Goal: Creating a reusable module and exposing functions/variables
# This module defines a helper function and a shared string value.
# It teaches: module-level code execution on import, exported names, and function definitions.

print ('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence.'''
    # Loop through the sequence and return the position of the target value
    for i, value in enumerate(to_search):
        if value == target:
            return i
    # Return -1 when the target is not found
    return -1