# This program is about creating classes and using them to do different things

class Human:
    # This is a class (CONSTANT) attribute (attribute shared by all objects of the class)
    MAX_ENERGY = 100

    # This is the initialiser method
    def __init__(self, name="Human", age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    # This is an instance method
    def display(self):
        print(f'I am {self.name}')


if __name__ == '__main__':
    human = Human()
    human.display()
