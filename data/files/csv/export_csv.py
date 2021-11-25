# The purpose of this program is to export user data as a CSV file

def export(csv_file_path, num_bots_export):
    """
    :param csv_file_path: Pass in the file path for the CSV file that will be written to.
    :param num_bots_export: An integer value to indicate how may bots will be exported to the CSV file
    :return: None, as the file will be written to and then closed
    """

    # Opening message for the function!
    print("Exporting...")

    # Opening the csv file for reading first
    with open(csv_file_path, mode="a") as csv_file_append:

        # For each bot to be exported (see num_bots_export value), do:
        for count in range(num_bots_export):

            # Get the bot's id and store it.
            print("Please enter the id of the bot:")
            bot_id = int(input())

            # Get the bot's name and store it.
            print("Please enter the name of the bot:")
            bot_name = input()

            # # Get the bot's paint and store it.
            print("Please enter the paint scheme(colour) of the bot:")
            bot_paint = input()

            # Store the 3 pieces of data in a single variable, and then write to the file
            data_write = f"\n{bot_id}, {bot_name}, {bot_paint}"
            csv_file_append.write(data_write)
    print("Done!")


def run():
    # Calling the first function with the actual file name passed name,
    # plus the number of bots to be exported
    export("exported_bots.csv", 2)


if __name__ == '__main__':
    run()
