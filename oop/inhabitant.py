# I previously created the classes Human and Robot. Both of these classes share similar
# functionality and extend from the class Inhabitant.  We can therefore move the common
# attributes (name, age and energy) and methods (eat, grow and move) of these two classes to the class Inhabitant.
# This helps improve code reuse and reduce code duplication.

class Inhabitant:

    # This is a class (CONSTANT) attribute (attribute shared by all objects of the class)
    MAX_ENERGY = 100

    def __init__(self, name="Inhabitant", age=0):
        # The name being passed in as default is'Inhabitant'; can be overwritten!
        self.name = name
        self.age = age
        self.energy = Inhabitant.MAX_ENERGY

    def grow(self):
        # Increase the age by 1
        self.age += 1

    def eat(self, amount_to_eat):
        # --- To change/update the energy of the inhabitant when it gets low ---

        # Potential energy that can be gained from eating will be stored in potential_energy
        potential_energy = self.energy + amount_to_eat

        # Checking if the total potential_energy doesn't exceed the MAX_ENERGY
        if potential_energy > Inhabitant.MAX_ENERGY:
            # Set the object's energy to MAX_ENERGY if exceeding 100
            self.energy = Inhabitant.MAX_ENERGY

            # Return how much energy has been gained over the max energy
            return potential_energy - self.energy
        else:
            # Set the energy of the object to the new energy value and return 0 --> new energy was set!
            self.energy = potential_energy
            return 0

    def move(self, distance):
        # What amount of energy is lost my moving will be stored here
        potential_energy_lost = self.energy - distance

        # Checking whether the energy doesn't fall below 0:
        if potential_energy_lost < 0:
            # Set the object's energy to 0 if falls below 0
            self.energy = 0

            # Return the energy lost from moving as a positive integer (really it is a negative number)
            return self.energy - abs(potential_energy_lost)
        else:
            # Set the energy of the object to the new energy value and return 0 --> new energy was set!
            self.energy = potential_energy_lost
            return 0
