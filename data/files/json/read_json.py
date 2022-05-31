"""
A JSON file is a data file that has the file extension .json. It contains data that is structured using JavaScript
Object Notation.  This is a lightweight format for storing and transferring data.

A JSON file contains key-value pairs (e.g. "name":"Beep"). Each key-value pair is separated by a comma.
Related key-value pairs are enclosed in curly brackets {} and often represent an individual entity e.g. a bot.
Multiple entities can be grouped using square brackets [] and nested within one another.

We can read the data from a JSON file use the module json.
import json --? library name
json.load() --> this method loads the data from the file
(Once the data has been loaded, we can extract the values using the appropriate keys.)

Tasks: To create a program to display the content of a JSON file
"""
import json


def read(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)

        city_name = data["city"]
        print(f"City Name: {city_name}")

        population_size = data["population"]
        print(f"Population Size: {population_size}")

        for bot_data in data["bots"]:
            name = bot_data["name"]
            stats = bot_data["stats"]
            print(f"{name} has the following stats: {stats}")


def run():
    read("robocity.json")  # This is used to get data from a JSON file


if __name__ == '__main__':
    run()
