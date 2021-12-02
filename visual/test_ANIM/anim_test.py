import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(frame):
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    plt.plot(x[:frame], y[:frame], "go--")
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 12)


fig, ax = plt.subplots(1, 1)
some_animation = animation.FuncAnimation(fig, animate, frames=6, interval=2000, repeat=False)

plt.show()
