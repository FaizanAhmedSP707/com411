# A program that displays some data related to temperatures observed during 1 week

import matplotlib.pyplot as plt


def read_data(file_path):
    # This function takes a file path as a parameter, reads in data from the file to create a plot

    temps = []
    # Need an empty list to store the values taken from the file
    # Now open the file, read it line by line and then append it to the list
    with open(file_path) as file:
        for line in file:
            temps.append(int(line.strip()))
    return temps


def run():
    # Read in the data from the file
    data = read_data('temps.txt')
    # print(data) --> for debugging purposes!!

    # Create a single figure with 2 axes in it, and reserve space for 2 plots to be shown; with 1 row & 2 columns
    fig, (axes1, axes2) = plt.subplots(1, 2)

    # Plot a line graph using the data stored from reading the file, 1st arg creates a list from the length of the data
    axes1.plot(range(len(data)), data)

    # Plot a bar graph using the data stored from reading the file, 1st arg creates a list from the length of the data
    axes2.bar(range(len(data)), data)

    plt.show()


if __name__ == '__main__':
    run()
