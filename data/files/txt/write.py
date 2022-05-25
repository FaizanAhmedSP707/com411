"""
Story: Beep and Bop are still searching through the many ancient books that fill the Robo City Library.
Tasks: We wish to help Beep and Bop search the books.
"""


def search(path_for_file):
    print("Searching...")  # intro message

    sections = ""  # Stores all strings that start with "Section"
    books = "Books:\n"  # Stores all string that don't start with "Section"

    with open(path_for_file) as file:
        for line in file:
            if line.startswith("Section"):
                sections += line
            else:
                books += line

    print("Done!")  # This is done after the lines have finished being copied to the respective variables

    # return single string consisting of sections and books, with two newline characters between them
    return f"{sections}\n\n{books}"


def save(path_to_file, data_string):
    print("Saving...")

    with open(path_to_file, "w") as file:
        file.write(data_string)
    print("Done!")  # After the data has been written to the file


def run():
    data_str = search("books.txt")
    save("sections-books.txt", data_str)


if __name__ == '__main__':
    run()
