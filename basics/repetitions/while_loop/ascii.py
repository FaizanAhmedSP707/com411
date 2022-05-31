"""
| STORY |
There are many cables but Beep is determined to help the robot trapped in the cables.  Beep must be careful
as some of the cables have live electricity running through them.

| Tasks |
We wish to create a program that allows Beep to avoid live cables.
"""

# Ask the user for the number of live cables to avoid
print("How many bars should be charged?")
bars_to_charge = int(input())

# Control variable to track the number of live cables avoided
bars_charged = 0


# Display the bars
print()

while bars_charged < bars_to_charge:
    bars_charged += 1
    print(f"Charging : {'█' * bars_charged}")

print("The battery is fully charged.")
