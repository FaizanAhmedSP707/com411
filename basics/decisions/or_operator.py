# This program allows Beep to pick what adventure he wants
print("What type of adventure should I have?")
adventure_type = input()
print()

# Checking if the adventure type entered is scary or short.
if adventure_type == 'scary' or adventure_type == 'short':
    print("Entering the dark forest!")
# Checking if the adventure type entered is safe or long.
elif adventure_type == 'safe' or adventure_type == 'long':
    print("Taking the safe route!")
# If the adventure type is anything else, a different message is displayed.
else:
    print("Not sure which route to take.")
