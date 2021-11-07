# A program to help Beep and Bop decipher the patterns in the book.
# All instances below of pattern are local to their respective functions, so there is no clash

def short_pattern():
    # Creating a dictionary which has a short sequence of characters repeating.
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern


def medium_pattern():
    # Creating a dictionary which has a medium sequence of characters repeating.
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern


def long_pattern():
    # Creating a dictionary which has a long sequence of characters repeating.
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern


def run():
    # Creates a new dictionary using the values returned from the first 3 functions.
    print("Analysing patterns...")
    patterns = {"short sequence": short_pattern(), "medium sequence": medium_pattern(), "long sequence": long_pattern()}

    for key, value in patterns.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    run()
