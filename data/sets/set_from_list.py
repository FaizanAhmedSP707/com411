# A program to help Beep and Bop record how many of type of eah item they saw

def observed():
    # Creating an empty list that will be populated by taking input from the user
    observations = []
    # Using a loop to populate the list
    for count in range(7):
        print("Please enter an observation:")
        observations.append(input())

    return observations


def run():
    print("Counting observations...")
    # variable to store the return from the function call
    c_observations = observed()

    # Populating the set
    observations_set = set()
    for value in c_observations:
        data = (value, c_observations.count(value))
        observations_set.add(data)

    # Display the set
    for data_print in observations_set:
        print(f"{data_print[0]} observed {data_print[1]} times.")


run()
