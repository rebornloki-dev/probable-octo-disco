# LEARNING Goal: The NOT Operator for Boolean Logic
# This script demonstrates the NOT operator, which inverts a boolean value.
# It teaches: boolean negation, making conditions more readable, and control flow.

# Assign a username
user ='Admin'
# Assign a boolean value for login status
logged_in = False

# The 'not' operator inverts the boolean: 'not False' becomes True
if not logged_in:
    print('Please Log In')
else:
    print('Welcome Admin')

# TRY THIS: Change logged_in to True and run again to see the NOT operator behavior!