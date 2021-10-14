# This program determines the ASCII code for a single character
print("Program Started!")
print("Please enter a standard character:")
user_input = input()

# Checking whether the length of the user-input string is 1 or more
if len(user_input) == 1:
    value = ord(user_input)
    print(f"The ASCII code for {user_input} is: {value} .")
else:
    print("Please enter a single character!")
print("Program Ended!")
