"""
| Story |

There are many cables but Beep is determined to help the robot trapped in the cables.  Beep must be careful
as some of the cables have live electricity running through them.

| Tasks |
We wish to create a program that allows Beep to avoid live cables.
"""

# Ask the user for the number of cables to avoid
print("How many live cables should I avoid?")
cables_to_avoid = int(input())

# Control variable to track the number of live cables avoided
number_of_cables_avoided = 0

# Avoiding the cables
print()

while number_of_cables_avoided < cables_to_avoid:
    print("Avoiding...", end="")
    number_of_cables_avoided += 1
    print(f"Done! {number_of_cables_avoided} live cables avoided.")  # Display the current number of live cables avoided

# Ending message after the while loop has concluded
print("\nAll live cables have been avoided.")
