# LEARNING Goal: Conditional Logic (if/elif/else)
# This script demonstrates temperature-based conditional statements.
# It teaches: nested conditions, comparison operators (>, <=), and control flow.

temp = int(input("What is the temperature in Celsius? "))

# Check if temperature is hot (greater than 30°C)
if temp >30 :
    print("It's a hot day")
# Check if temperature is warm (greater than 20°C)
elif temp >20 :
    print("It's a nice day")
# Check if temperature is cool (greater than 10°C)
elif temp >10 :
    print("Its a bit cold")
# If none of the above conditions are true
else :
    print("You should probably stay indoors")