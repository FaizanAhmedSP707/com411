"""
| STORY |
Beep is continuing its journey deeper into the forest when it comes across an unusual sight. Beep finds what appears
to be another robot wrapped in cables. It seems this other robot is stuck and needs help.  Beep decides to rescue the
robot.

| Tasks |
We wish to create a program that allows Beep to remove the cables holding the robot.
"""

# Ask the user for number of cables
print("How many cable should I remove?")
number_of_cables_to_remove = int(input())

# A control variable to track the number of removed cables
removed_cables_count = 0


# Remove cables part
print()

while removed_cables_count < number_of_cables_to_remove:
    print("Removed cable.")

    # Increment the control variable for thw while loop
    removed_cables_count += 1
