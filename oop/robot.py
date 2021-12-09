# This program is about creating classes and using them to do different things

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

    # This is an instance method
    def display(self):
        print(f'I am {self.name}')


if __name__ == '__main__':
    robot = Robot()
    Robot.the_laws()
    robot.display()
