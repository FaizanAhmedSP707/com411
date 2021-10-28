# A refinement of simple_list.py that Beep and Bop will use to escape the cave

def movements():
    # This function creates a list with directions along with the step to move for each direction
    path = ["Move Forward", 10, "Move Backwards", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    # This function uses print formatting to display each direction with the steps needed to move in that direction
    print("Moving...")
    move_instructions = movements()
    print(f"{move_instructions[0]} for {move_instructions[1]} steps")
    print(f"{move_instructions[2]} for {move_instructions[3]} steps")
    print(f"{move_instructions[4]} for {move_instructions[5]} steps")
    print(f"{move_instructions[6]} for {move_instructions[7]} steps")


if __name__ == '__main__':
    run()
