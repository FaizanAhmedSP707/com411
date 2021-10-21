# This program will help Beep and Bop to search the library


def search(file_name):
    print("Searching...")
    with open(file_name) as file:
        for line in file:
            print(f"Looked in the {line.strip()}")
    print("...Done!")


def run():
    search('library.txt')


if __name__ == '__main__':
    run()
