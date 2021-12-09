# This program will populate a universe using a planet object that is inhabited by human and
# robot objects

from planet1 import Planet
from robot2 import Robot
from human2 import Human

import random


class Universe:
    # Initialise an empty list for the planet attribute to store a list of planet objects
    def __init__(self):
        self.planets = []

    def __repr__(self):
        # Return a string representation about the current object
        return f"Universe(planets={self.planets}"

    def __str__(self):
        # Return a readable string about the current object
        return f"The universe contains {len(self.planets)} planets"

    def generate(self):
        """
        This isn't a static method as it works on an object instance that is created
        """
        # Create a new planet
        new_planet = Planet()

        # Populate the planet with a random number of humans and robots using a loop
        for index in range(random.randint(1, 10)):
            human = Human(f"Human{index}")
            new_planet.add_human(human)

        for index in range(random.randint(1, 10)):
            robot = Robot(f"Robot{index}")
            new_planet.add_robot(robot)

        # Add to the list of planets
        self.planets.append(new_planet)


if __name__ == '__main__':
    new_universe = Universe()
    new_universe.generate()
    print(repr(new_universe))  # uses the __repr__ method
    print(new_universe)  # Uses the __str__ method
    print(new_universe.planets)
