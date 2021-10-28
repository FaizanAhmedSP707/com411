# A variation of iterate_list.py that Beep and Bop will use to escape the cave.

def directions():
    # Creates a list with directions to use in the 2nd function
    direction_list  = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction_list


def menu():
    """
    This function uses a loop to display the directions to be moved, takes in user input,
    and then returns the direction from the list corresponding to the user input
    """

    print("Please select a direction:")
    move_direction = directions()
    for index in range(len(move_direction)):
        print(f"{index}: {move_direction[index]}")
    user_input = int(input())
    return move_direction[user_input]


def run():
    # Uses a list to append the value returned from the function menu and then prints it out
    route = []
    print("Working out escape route...")
    for count in range(5):
        route.append(menu())
    print(f"Escape route: {route}")


if __name__ == '__main__':
    run()
