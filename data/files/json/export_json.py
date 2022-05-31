"""
The method dump of the module json can be used to write JSON data to a file.  We simply provide the method dump with the
file path and the JSON string we wish to write to a file. We can also optionally specify the number of spaces to use for
the purposes of indentation.

Tasks:
We wish to create a program to store data to a JSON file
"""
import json


def read(file_path):
    """
    Reads data from the JSON file and saves it to a variable, which is then returned at the end of the function.
    :param file_path: A path to the JSON file, from which data will be read from.
    :return: returns the local variable 'data' at the end which contains all the JSON data.
    """
    print("Reading...", end="")

    with open(file_path) as json_file:
        """
        Open the specified file, retrieve the data within and store it, print an ending message, and then finally
        return the stored data outside to the main function.
        """
        data = json.load(json_file)
    print("Done!")
    return data


def save(file_path, data):
    """
    To save the JSON content exported from another file into a new JSON file.
    :param file_path: the file path to use, in which the exported JSON data will be stored.
    :param data: Variable that holds the exported data (Which is in JSON format)
    :return: Returns nothing.
    """
    print("Exporting...", end="")

    with open(file_path, "w") as json_file_s:
        """
        Create a new JSON file to store the exported data in.
        json.dump() takes by default 2 parameters, the variable containing data in JSON format and the name of the
        file. In this case, the file has an alias of 'json_file_s'. Other optional parameters can be specified,
        such as indent here, which specifies the number of spaces to use for indentation purposes.
        """
        json.dump(data, json_file_s, indent=4)
    print("Done!")


def run():
    # Function calls here to the two functions defined above.
    json_data_storage = read("robocity.json")
    save("exported.json", json_data_storage)


if __name__ == '__main__':
    # Main function call here.
    run()
