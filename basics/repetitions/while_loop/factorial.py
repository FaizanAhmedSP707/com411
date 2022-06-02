"""
| STORY |
Bop is continuing to run its diagnostic tests. Bop decides to try a more sophisticated calculation and wishes to
calculate the factorial of a number.

| Tasks |
We wish to create a program to help Bop calculate the factorial of a specified number.
"""

# Display a starting message
print("Please enter a number:")
user_number = int(input())

# For calculating the factorial
counter = 0  # Default value
total = 1  # Stores the answer for the factorial, if the number is 0, 1 should be returned

# Start of while loop to calculate the factorial of the user's entered number
while counter < user_number:
    counter += 1
    total *= counter

# After the while loop is over, print out the answer
print(f"\nThe factorial of the number you have chosen is {total}")
