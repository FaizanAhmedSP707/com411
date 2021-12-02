# The purpose of this program is to display the animation of a circle marker moving
# across the screen

import matplotlib.pyplot as plt
import matplotlib.animation as animation

figure, ax = plt.subplots()


def animate(frame_number):
    global ax

    # Setting the limits of the axis (both x & y) on the axes
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    # Doing the plotting thing
    ax.plot(frame_number, frame_number, "b.")


def run():
    global figure
    simple_animation = animation.FuncAnimation(figure, animate, frames=24, interval=42, repeat=False)
    # The animation needs to be stored in a variable before it can be shown.

    plt.show()


if __name__ == '__main__':
    run()
