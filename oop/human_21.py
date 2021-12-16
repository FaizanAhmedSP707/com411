# This program is about inheritance; inheriting a base class and extending that class in a new class
# to add new features, thus improving code reuse and reduce code duplication

from inhabitant import Inhabitant


class Human(Inhabitant):
    # Inheriting the Inhabitant class

    def __init__(self, name="Human", age=0):
        # Use the initialiser from the super class to initialise a new human object
        super().__init__(name, age)

    def __repr__(self):
        return f'\nhuman(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f"\nMy name is {self.name} and I am {self.age} years old, and my energy is {self.energy}"

    def display(self):
        print(f"\nI am {self.name}")


if __name__ == '__main__':
    # Creating a human object for testing of code
    new_human = Human()
    print(repr(new_human))
    new_human.move(15)
    print(repr(new_human))
    new_human.eat(7)
    print(repr(new_human))
    new_human.eat(9)
    print(repr(new_human))

    print(new_human)  # Uses the magic method __str__
