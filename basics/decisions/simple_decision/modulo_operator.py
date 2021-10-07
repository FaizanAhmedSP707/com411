# Program to check whether a user-input number is odd or even
print("Please enter a whole number")
user_number = int(input())
print()

# Using a modulo operator in an if..else block for checking
if user_number % 2 == 1:
    print(f"The number {user_number} is an odd number.")
else:
    print(f"The number {user_number} is an even number.")

