"""
| STORY |
Beep and Bop are have reached near the top of a mountain when they see the entrance to a cave nearby.
Beep decides to head for the cave.  Bop reluctantly follows.

| Tasks |
We wish to create a program that counts down the distance (in a number of steps) to the cave.
"""

# Display an introductory message that also serves as an input prompt for the distance to the cave
print("How far are we from the cave?")
number_of_steps = int(input())

# Start of displaying the count-down
print()

# Start of the for loop the counts down the number of steps to the cave Beep and Bop wish to enter.
for counter in range(number_of_steps, 0, -1):
    print(f"{counter} steps remaining")

# Ending message
print("\nWe have reached the cave!")
