# A variation of 'set_from_list.py' to help Beep and Bop record their observations

def observed():
    # Creating an empty list that will be populated by taking input from the user
    observations = []
    # Using a loop to populate the list
    for count in range(5):
        print("Please enter an observation:")
        observations.append(input())

    return observations


def remove_observations(observations):
    # A variable to control the while loop below
    is_running = True

    while is_running:
        # asking the user which observation they wish to remove
        print("Do you wish to remove an observation (yes/no)?")
        user_response = input()

        if user_response == 'yes':
            # if the user wishes to remove an observation, this will execute
            print("What observation do you want to remove?")
            del_observation_instance = input()
            observations.remove(del_observation_instance)
            print("Done!")
        else:
            # Exiting the loop
            is_running = False


def run():
    print("Counting observations...")
    # variable to store the return from the function call
    observe_list = observed()
    remove_observations(observe_list)

    # Populate the set
    observations_set = set()
    for value in observe_list:
        data = (value, observe_list.count(value))
        observations_set.add(data)

    # Display the set
    for data_print in sorted(observations_set):
        print(f"{data_print[0]} observed {data_print[1]} times.")


run()
