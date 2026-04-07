# LEARNING Goal: Boolean Logic with OR Operator
# This script demonstrates the OR operator in conditional statements.
# It teaches: boolean variables, the OR operator, and how conditions are evaluated.
# KEY POINT: The OR operator returns True if EITHER condition is true.

# Assign a string variable for username
user ='Admin'
# Assign a boolean variable for login status
logged_in = True

# Use OR operator: condition is true if user IS 'Admin' OR if user is logged_in
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

# TRY THIS: Change logged_in to False and run again to see the OR operator behavior!