# The purpose of this program is to help extract values from the csv file created previously: 'bots.csv'
import csv


def extract(file_path):
    # Print an opening message
    print("Extracting...", end="")

    # Opening the csv file for reading first
    with open(file_path) as csv_file:
        # Storing the contents of the file into a variable
        csv_reader = csv.reader(csv_file)

        # Ignore the headings, need to get only the values
        next(csv_reader)

        # Setting up a variable and assigning to it an empty string
        names = ""

        # For each remaining line in the file,
        # read in the values and extract the name of the robot.
        # Then add the extracted name with a new line character to the variable 'names'.
        for values in csv_reader:

            # A really fancy way of adding in stuff to a variable!!!
            names += f"{values[1]}\n"

    # After complete processing, display the following messages
    print("Done!")
    print(f"The extracted names are as follows:\n{names}")


def run():
    # Calling the first function with the actual file name passed in
    extract("bots.csv")


if __name__ == '__main__':
    run()
