"""
| STORY |
Beep and Bop have reached the entrance of the cave.  It is very dark inside and both Beep and Bop are finding it
difficult to see.  They decide to activate night vision.  Beep is intrigued by the cave whilst Bop has a bad feeling.

| Tasks |
We wish to create a program that adjusts the light level of Beep and Bop's night vision.
"""

# Display an introductory message that also serves as an input prompt for the level of brightness needed
print("What level of brightness is required? (Please input an even number):")
brightness_level = int(input())

# Adjusting the brightness level
print("\nAdjusting brightness...\n")

# Start of for loop that increases Beep's and Bop's night vision software's brightness level
for brightness in range(2, brightness_level + 1, 2):
    # Using the above range, display asterisk symbols to represent the current light level using the above loop
    print(f"Beep's brightness level: {'*' * brightness}")
    print(f"Bop's brightness level: {'*' * brightness}")
    print()  # put an empty line in between the next round of print messages

# Display the ending message
print("Adjustments complete!")
