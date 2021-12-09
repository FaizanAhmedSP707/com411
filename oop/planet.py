# This program imports the classes from human2.py and robot2.py and
# uses a new class called Plant to populate the planet using
# a list of human and robot objects

from human2 import Human
from robot2 import Robot


class Planet:
    # Initialise a dictionary containing a list of inhabitants for each key
    def __init__(self):
        self.humans = []
        self.robots = []

    def __repr__(self):
        # Return a string representation about the current object
        return f"\nPlanet(humans={self.humans}, robots={self.robots})"

    def __str__(self):
        # Return a readable string about the current object
        return f"\nThis planet has {len(self.humans)} humans and {len(self.robots)} robots."

    def add_human(self, human):
        # An object of the human class will be passed in as a parameter for adding to the list of humans
        self.humans.append(human)

    def remove_human(self, human):
        # An object of the human class will be passed in as a parameter for removal from the humans list
        pop_h_index = self.humans.index(human)
        self.humans.pop(pop_h_index)

    def add_robot(self, robot):
        # An object of the robot class will be passed in as a parameter for adding to the list of robots
        self.robots.append(robot)

    def remove_robot(self, robot):
        # An object of the robot class will be passed in as a parameter for removal from the robots list
        pop_r_index = self.robots.index(robot)
        self.robots.pop(pop_r_index)


if __name__ == '__main__':
    new_planet = Planet()
    print(repr(new_planet))  # Uses the magic method __repr__
    print(new_planet)  # uses the magic method __str__ for the printing of an object by default
    Prins = Human('Prins')
    new_planet.add_human(Prins)
    alpha = Robot("Alpha")
    new_planet.add_robot(alpha)
    print(repr(new_planet))
    Nick = Human("Nick")
    new_planet.add_human(Nick)
    Darren = Human("Darren")
    new_planet.add_human(Darren)
    beta = Robot("Beta")
    new_planet.add_robot(beta)
    print(repr(new_planet))
    Faizan = Human("Faizan")
    new_planet.add_human(Faizan)
    print(repr(new_planet))
    new_planet.remove_human(Faizan)
    print(repr(new_planet))

    # Finally print out the planet object using the __str__ method
    print(new_planet)
