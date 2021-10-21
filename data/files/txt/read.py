# This program is to allow Beep and Bop to search the library.


def display_chars(file_path, no_of_chars_to_read):
    print(f"\nThe first {no_of_chars_to_read} are:")
    with open(file_path) as file:
        partial_data = file.read(no_of_chars_to_read)
        print(partial_data)


def display_line(file_path):
    print("\nThe first line is:")
    with open(file_path) as file:
        line_read = file.readline().strip()
        print(line_read)


def display_text(file_path):
    print("\nThe full text is:")
    with open(file_path) as file:
        full_data = file.read()
        print(full_data)


def run():
    display_chars('library.txt', 5)
    display_line('library.txt')
    display_text('library.txt')


if __name__ == '__main__':
    run()
