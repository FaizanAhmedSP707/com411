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
        return f'\nhuman(name={self.name}, age={self.age}, energy={self.energy})'

    # This is an instance method
    def display(self):
        print(f'I am {self.name}')

    def grow(self):
        self.age += 1

    def eat(self, amount):
        # Potential energy that can be gained from eating will be stored in potential_energy
        potential_energy = self.energy + amount

        # Checking if the total potential_energy doesn't exceed the MAX_ENERGY
        if potential_energy > Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY
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
    human = Human()
    human.display()
    print(human)  # uses the magic method __str__ by default
    human.grow()
    print(repr(human))  # Uses the magic method __repr__
    human.move(10)
    print(repr(human))  # Uses the magic method __repr__
    human.eat(5)
    print(repr(human))  # Uses the magic method __repr__
