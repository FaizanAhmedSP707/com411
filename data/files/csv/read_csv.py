# The purpose of this program is to display the content of a CSV file.

import csv


def read(file_path):
    # Opening the csv file for reading first
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)

        # To handle the headings present in the CSV file
        headings = next(csv_reader)

        # Display the headings
        print(f"Headings:\n{headings}")

        # Printing the values
        print("Values:")
        for values in csv_reader:
            print(values)


def run():
    # Call to 1st function
    read('bots.csv')


if __name__ == '__main__':
    run()
