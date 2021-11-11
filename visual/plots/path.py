# A program that displays the path that Beep and Bop are taking trough Robo City
import matplotlib.pyplot as plt


def coordinate():
    # This function asks the user to input an x-value and a y-value and then returns it.
    user_x_input = int(input("Please enter an x value (integer): "))
    user_y_input = int(input("Please enter a y value (integer): "))
    return user_x_input, user_y_input
    # The above statement returns the two values as a tuple


def path():
    # Creates 2 empty lists and then appends to them using the user-input data, finally returns the 2 lists
    print("\nRetrieving path...")
    x_values = []
    y_values = []

    for count in range(4):
        # using a loop statement to append the values given in by the user to the 2 empty lists
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return [x_values, y_values]


def run():
    return_values = path()
    plt.plot(return_values[0], return_values[1], 'ro--')
    # 'ro--' plots out a red dashed line with circles as markers
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.show()


if __name__ == '__main__':
    # execute file when run directly
    run()
