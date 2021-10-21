# The purpose of this program is to display information about the current working directory.

import os
# This imports the required module which is used to find out the current working directory (cwd).


def cwd():
    # Using a variable to store the current working directory
    path = os.getcwd()
    print(f"The current working directory is {path}")
    # This part will print out the files that are in the current working directory
    print("The directory contains the following files:")
    for file in os.listdir(path):
        print(file)


def run():
    print("Processing")
    cwd()


# The function call to the 2nd function which will call the 1st function
run()
