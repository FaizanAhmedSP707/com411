# This program is about inheritance; inheriting a base class and extending that class in a new class
# to add new features, thus improving code reuse and reduce code duplication

from inhabitant import Inhabitant


class Robot(Inhabitant):
    # Inheriting the Inhabitant class

    # Class attribute
    laws = "Protect, Obey and Survive"

    # A static method for robots
    @staticmethod
    def the_laws():
        print(Robot.laws)

    def __init__(self, name="Robot", age=0):
        # Use the initialiser from the super class to initialise a new human object
        super().__init__(name, age)

    def __repr__(self):
        return f'\nrobot(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f"\nMy name is {self.name} and I am {self.age} years old, and my energy is {self.energy}"

    def display(self):
        print(f"\nI am {self.name}")


if __name__ == '__main__':
    # Creating a human object for testing of code
    new_robot = Robot()
    Robot.the_laws()  # Get the static method that is available be default
    print(repr(new_robot))
    new_robot.move(35)
    print(repr(new_robot))
    new_robot.eat(17)
    print(repr(new_robot))
    new_robot.eat(12)
    print(repr(new_robot))

    print(new_robot)  # Uses the magic method __str__
