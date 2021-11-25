"""
This purpose of this program is to draw a plot using the matplotlib library and then animate it using the animation
module from matplotlib, then finally show the plot
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setting up a figure with a single axes on which the plot will be drawn
figure, ax = plt.subplots()


def animate(frame_number):
    # Print out the frame number on each frame of the animation
    print(f"Frame: {frame_number}")

    # List of x and y values to plot on the axes
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    y = [0, 1, 4, 9, 16, 25, 36, 49, 64]

    # Plot the graph by limiting the dots to the frame number
    plt.plot(x[:frame_number], y[:frame_number], 'r')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 120)
    # Setting the labels for the axis in the plot
    ax.set_xlabel('Integer')
    ax.set_ylabel('Square number of integer')


def run():
    # Reference to global variable to avoid errors
    global figure
    simple_animation = animation.FuncAnimation(figure, animate, frames=10, interval=1000, repeat=False)
    plt.show()


if __name__ == '__main__':
    run()
