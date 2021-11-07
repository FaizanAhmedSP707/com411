"""
A variation of 'simple_dict.py' that displays the contents of the dictionary in terms of its
keys, values and key-value pairs
"""


def pattern():
    # Creating a dictionary and populating it with items
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def display_keys(data):
    # This function displays the keys in the dictionary.
    print("Keys:")
    for key in data:
        print(key)
    print('')


def display_values(data):
    # This function displays the values in the dictionary.
    print("Values:")
    for value in data.values():
        print(value)
    print('')


def display_items(data):
    # This function displays the key-value pairs in the dictionary.
    print("Pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")
    print('')


def run():
    data_dict = pattern()
    print(f"Dictionary:\n{data_dict}")
    print('')

    display_keys(data_dict)
    display_values(data_dict)
    display_items(data_dict)


if __name__ == '__main__':
    run()
