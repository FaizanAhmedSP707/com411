# This program uses data taken from a csv file to display 2 subplots

import matplotlib.pyplot as plt
import csv
from matplotlib.ticker import MultipleLocator


def read_data():
    # Open the csv file for reading and store the data in a variable
    with open('temps.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        header = next(csv_reader)
        # Handling the headers in the .csv file
        data = {'week1': [], 'week2': []}

        for line in csv_reader:
            """
            For each line taken from the object csv_reader, do the following:
            1) For the key called 'week1'. append the individual values taken to the empty list
            while getting rid of whitespaces, so that a key-value pair is formed. 
            [ KEEPING COLUMN NUMBERS IN MIND --> 0 FOR WEEK 1 ]
            2) For the key called 'week2'. append the individual values taken to the empty list
            while getting rid of whitespaces, so that a key-value pair is formed.
            [ KEEPING COLUMN NUMBERS IN MIND --> 1 FOR WEEK 2 ]  
            """
            data['week1'].append(int(line[0].strip()))
            data['week2'].append(int(line[1].strip()))

    return data


def run():
    # calling the first function
    data = read_data()

    # Setting up 2 axes with 2 rows in a simple column, then plotting the graphs using data passed in
    figure, (axes1, axes2) = plt.subplots(2, 1)
    axes1.plot(range(len(data['week1'])), data['week1'])
    axes2.plot(range(len(data['week2'])), data['week2'])

    # Setting up the way the ticks are to be displayed
    axes1.tick_params(which='both', width=2)
    axes1.tick_params(which='minor', length=4, color='r')
    axes1.tick_params(which='major', length=8)
    axes2.tick_params(which='both', width=2)
    axes2.tick_params(which='minor', length=4, color='r')
    axes2.tick_params(which='major', length=8)

    # Setting up the way the ticks will be placed
    axes1.xaxis.set_minor_locator(MultipleLocator(1))
    axes1.yaxis.set_minor_locator(MultipleLocator(0.5))
    axes1.xaxis.set_major_locator(MultipleLocator(2))
    axes1.yaxis.set_major_locator(MultipleLocator(1))
    axes2.xaxis.set_minor_locator(MultipleLocator(1))
    axes2.xaxis.set_major_locator(MultipleLocator(2))
    axes2.yaxis.set_major_locator(MultipleLocator(2))
    axes2.yaxis.set_minor_locator(MultipleLocator(1))

    # Setting up the labels on both graphs, adjusting the overall display, then displaying it to the screen
    axes1.set_xlabel('Week 1')
    axes1.set_ylabel('Temperature')
    axes2.set_xlabel('Week 2')
    axes2.set_ylabel('Temperature')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    run()
