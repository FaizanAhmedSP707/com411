# This program is about updating the class from 'human.py' to add 2 magic methods

class Human:
    # This is a class (CONSTANT) attribute (attribute shared by all objects of the class)
    MAX_ENERGY = 100

    # This is the initialiser method
    def __init__(self, name="Human", age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    # These 2 are magic methods
    def __str__(self):
        # Return a readable string about the current object
        return f'\nMy name is {self.name} and I am {self.age} years old and my energy level is {self.energy}.'

    def __repr__(self):
        # Return a string representation of the object
        return f'\nhuman(name={self.name}, age={self.age})'

    # This is an instance method
    def display(self):
        print(f'I am {self.name}')


if __name__ == '__main__':
    human = Human()
    human.display()
    print(human)  # uses the magic method __str__ by default
    print(repr(human))  # Uses the magic method __repr__
