# A program to help Beep and Bop decide which steps to take for the falling steps problem

def likelihood():
    # Creates a tuple with the possibilities of the steps falling and returns the minimum value
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run():
    # Uses print formatting to show the returned minimum possibility of the step falling
    min_value = likelihood()
    print(f"Minimum likelihood of falling: {min_value}%")


if __name__ == '__main__':
    run()
