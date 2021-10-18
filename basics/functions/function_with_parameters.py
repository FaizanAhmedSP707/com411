# This program is to allow Beep and Bop to climb a ladder to escape and survive

def climb_ladder(steps_remaining, steps_crossed):
    """
    This function will compare whether the remaining number of steps to take is more or less than
    the number of steps crossed and then output a simple message
    """
    if steps_remaining > steps_crossed:
        # If remaining steps are more, then Beep and Bop have to climb more
        print("Still some way to go!")
    else:
        # If remaining steps are less, then Beep and Bop are almost out of danger!
        print("We are almost there!")


climb_ladder(5, 2)
climb_ladder(2, 5)
