# This program is to help Beep and Bop find their way out of the cave

def directions():
    # This function creates a list of directions for Beep and Bop to use
    directions_list = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions_list


def run():
    # Calls the first function and prints the list
    print(directions())


if __name__ == '__main__':
    run()
