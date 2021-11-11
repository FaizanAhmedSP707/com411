# This program will display the path Beep and Bop are taking through Robo City.
import matplotlib.pyplot as plt


def small():
    # This function will draw a small red square using circles and dashed lines
    red_x_plot = [3, 3, 4, 4, 3]
    red_y_plot = [3, 4, 4, 3, 3]
    plt.plot(red_x_plot, red_y_plot, 'ro:')
    # 'ro:' plots out a red dotted line with circles as markers


def medium():
    # This function will draw a medium green square using squares and dashed lines
    green_x_plot = [2, 2, 5, 5, 2]
    green_y_plot = [2, 5, 5, 2, 2]
    plt.plot(green_x_plot, green_y_plot, 'gs--')
    # 'gs--' plots out a green dashed line with squares as markers


def large():
    # This function will draw a large blue square using crosses and straight lines
    blue_x_plot = [1, 1, 6, 6, 1]
    blue_y_plot = [1, 6, 6, 1, 1]
    plt.plot(blue_x_plot, blue_y_plot, 'bp-')
    # 'bp-' plots out a blue solid line with pentagons as markers


def run():
    # Calls the first 3 functions and then shows all of the plotted in a single window
    small()
    medium()
    large()
    plt.show()


if __name__ == '__main__':
    run()
