# The code below is used by Beep to find his spare battery by using many nested if statements
print("Where should I look?")
location = input()

# Beep is going to check in the bedroom
if location == 'in the bedroom':
    print("Where in the bedroom should I look?")
    bedroom_spot = input()
    if bedroom_spot == 'under the bed':
        print("Found some shoes but no battery.")
    else:
        print("Found some mess but no battery.")
# Beep is going to look in the bathroom
elif location == 'in the bathroom':
    print("Where in the bathroom should I look?")
    bathroom_spot = input()
    if bathroom_spot == 'in the bathtub':
        print("Found a rubber duck but no battery.")
    else:
        print("Found a wet surface but no battery.")
# Beep is going to look in the lab
elif location == 'in the lab':
    print("Where in the lab should I look?")
    lab_spot = input()
    if lab_spot == 'on the table':
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery")
# If Beep has to check in any other location
else:
    print("I do not know where that is but I will keep looking.")
