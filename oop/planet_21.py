# I previously created the class Planet that allowed us to add humans and robots to a planet.
# These were stored in a dictionary.  Now that I have the class Inhabitant, I no longer need a dictionary
# or indeed separate methods for humans and robots.  This is because I can now store a single list of inhabitants.
# We can always check whether an inhabitant is a human or a robot using the function isinstance.

from human_21 import Human
from robot_21 import Robot


class Planet:

    # A special method to initialise an object of the class
    def __init__(self):
        self.inhabitants = []

    def __repr__(self):
        # Return a formal string representation about the current object
        return f'planet(inhabitants={self.inhabitants}'

    def __str__(self):
        # Return an informal string representation about the current object
        return f'This planet has {len(self.inhabitants)} inhabitants.'

    def add_inhabitant(self, inhabitant):
        # Pass in an object that is created from a subclass of the inhabitant class
        self.inhabitants.append(inhabitant)

    def remove_inhabitant(self, inhabitant):
        # Pass in an object that is created from a subclass of the inhabitant class for removal
        self.inhabitants.remove(inhabitant)


if __name__ == '__main__':
    planet = Planet()  # Create a new planet object
    print(repr(planet))
    Prins = Human("Prins")
    planet.add_inhabitant(Prins)
    Darren = Human("Darren")
    planet.add_inhabitant(Darren)
    Omega_223 = Robot("Omega_223")
    planet.add_inhabitant(Omega_223)
    Beta_365 = Robot("Beta_365")
