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
        return f'\nRobot {self.name} is {self.age} years old and my energy is {self.energy}.'

    def __repr__(self):
        # Return a string representation of the object
        return f'\nrobot(name={self.name}, age={self.age}, energy={self.energy}'

    # This is an instance method
    def display(self):
        print(f'\nI am {self.name}')

    def grow(self):
        self.age += 1

    def eat(self, amount):
        # Potential energy that can be gained from eating will be stored in potential_energy
        potential_energy = self.energy + amount

        # Checking if the total potential_energy doesn't exceed the MAX_ENERGY
        if potential_energy > Robot.MAX_ENERGY:
            self.energy = Robot.MAX_ENERGY
            # Return how much energy has been gained over the max energy
            return potential_energy - self.energy
        else:
            self.energy = potential_energy

    def move(self, distance):
        # What amount of energy is lost my moving will be stored here
        potential_energy_lost = self.energy - distance

        # Checking whether the energy doesn't fall below 0:
        if potential_energy_lost < 0:
            self.energy = 0
            # Return the energy lost from moving as a positive integer (really it is a negative number)
            return self.energy - abs(potential_energy_lost)
        else:
            self.energy = potential_energy_lost


if __name__ == '__main__':
    robot = Robot()
    Robot.the_laws()  # Can be called as it's not tied to an instance of the class
    robot.display()
    print(robot)  # uses the magic method __str__ by default
    print(repr(robot))
    print(robot)  # uses the magic method __str__ by default
    robot.grow()
    print(repr(robot))  # Uses the magic method __repr__
    robot.move(10)
    print(repr(robot))  # Uses the magic method __repr__
    robot.eat(5)
    print(repr(robot))  # Uses the magic method __repr__
