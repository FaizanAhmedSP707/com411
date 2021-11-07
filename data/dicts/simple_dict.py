# A program that will help Beep and Bop decipher the pattern

def pattern():
    # Creating a dictionary and populating it with items
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def run():
    # Storing the return of the 1st function and then displaying it
    dict_display = pattern()
    print(dict_display)


if __name__ == '__main__':
    run()
