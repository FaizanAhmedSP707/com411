# A variation of index_list.py that Beep and Bop will use to escape the cave.

def directions():
    # Creates a list with directions to use in the 2nd function
    direction_list = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction_list


def menu():
    # This function prints out each direction that can be taken in a sort of menu.
    print("Please select a direction:")
    move_direction = directions()
    for index in range(len(move_direction)):
        print(f"{index}: {move_direction[index]}")


def run():
    # Calling menu for execute
    menu()


if __name__ == '__main__':
    # If the file is run directly, this will execute
    run()
