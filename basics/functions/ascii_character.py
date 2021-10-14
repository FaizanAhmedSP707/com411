# This program prints the character represented by a set of decimal numbers: from 32 - 126
print("Program Started!")
print("Please enter an ASCII code: ")
# The abs() function returns the absolute value of a number, so a negative input can be entered as well here.
code = abs(int(input()))

# Now the program checks whether the number given is within the range of 32 to 126.
# This is basically the range for the ASCII characters that can be printed to the screen
if code in range(32, 127):
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is: {character} .")
else:
    # If number is not within range, display an error message
    print("The number you have entered is not within the range of 32 to 126!")

print("Program Ended!")
