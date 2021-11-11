# This program is to display the path Beep and Bop are taking through Robo City
import matplotlib.pyplot as plt


def display(x_list, y_list):
    # This function will draw a line plot using the arguments passed in as parameters
    plt.plot(x_list, y_list)
    plt.xlabel('Integers')
    plt.ylabel('Square number')
    plt.show()


def run():
    # This function just creates 2 lists and then calls the 1st function; passing the created lists as actual arguments
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display(x_values, y_values)


if __name__ == '__main__':
    run()


"""
Keeping this stuff for reference
x = [0, 5, 10]
y = [0, 50, 100]

plt.plot(x, y)
plt.show()
"""