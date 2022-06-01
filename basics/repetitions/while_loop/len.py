"""
| STORY |
Beep has fully charged the battery of the robot.  Beep attempts to speak to the robot and notices that each time
it says a word, the robot responds with "Bop".

| Tasks |
We wish to create a program to help the robot communicate with Beep.
"""

# Ask the user to for a phrase
print("Please enter a phrase:")
user_phrase = input()

# Control variable to track the number of time the newly discovered bot says 'Bop'
number_of_bops = 0


# Display Bops
print()

while number_of_bops < len(user_phrase):
    print("Bop ", end="")
    number_of_bops += 1
