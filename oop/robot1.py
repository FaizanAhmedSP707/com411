# This program is about updating the class form 'robot.py' to add 2 magic methods

class Robot:
    # This is a class attribute
    laws = "Protect, Obey and Survive"

    # This is a class (CONSTANT) attribute (attribute shared by all objects of the class)
    MAX_ENERGY = 100

    # This is a static method (doesn't need an object created in order to access it)
    @staticmethod
    def the_laws():
        print(Robot.laws)

    # This is the initialiser method
    def __init__(self, name="Robot", age=0, energy=0):
        self.name = name
        self.age = age
        self.energy = energy

    # These 2 are magic methods
    def __str__(self):
        # Return a readable string about the current object
        return f'\nRobot {self.name} is {self.age} years old.'

    def __repr__(self):
        # Return a string representation of the object
        return f'\nhuman(name={self.name}, age={self.age})'

    # This is an instance method
    def display(self):
        print(f'\nI am {self.name}')


if __name__ == '__main__':
    robot = Robot()
    Robot.the_laws()  # Can be called as it's not tied to an instance of the class
    robot.display()
    print(robot)  # uses the magic method __str__ by default
    print(repr(robot))
