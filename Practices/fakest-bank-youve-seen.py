# LEARNING Goal: Dictionaries, Nested Conditionals, and User Input
# This script simulates a simple ATM withdrawal system.
# It teaches: dictionary access with keys, nested if statements, type conversion,
# arithmetic operations, and basic security validation (PIN checking).

# Create a dictionary to represent a bank account
account = {"balance": 1000, "pin": "1234"}

# Get PIN input from user
pin =input("Enter your PIN: ")

# First condition: Check if the PIN matches
if pin == account["pin"]:
    # Get the withdrawal amount from user
    amount =int(input("How much would you like to withdraw? "))
    # Nested condition: Check if there are sufficient funds
    if int(amount) <= account["balance"]:
        # Deduct the amount from account balance
        account["balance"] -= amount
        print(f"Withdrawal successful. Your new balance is {account['balance']}.")
    else:
        # If insufficient funds, print error message
        print("Insufficient funds.")
else:   
    # This happens if the PIN is wrong
    print("ACCOUNT LOCKED. ")