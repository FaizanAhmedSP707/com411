"""
This program uses a user-defined function along with a nested decision
to allow Beep and Bop to see whether Beep and Bop are in danger
from whatever is hurtling towards them.
"""


def identity():
    print("What lies before us? ")
    # Beep is asking what is in front of him and Bop.
    seen_object = input()
    print()
    # Checking whether the response is 'a large boulder' or not.
    if seen_object == 'a large boulder':
        print("It's time to run!")
    else:
        print("We will be fine.")


# The function call
identity()
