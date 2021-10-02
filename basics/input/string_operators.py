# Using some string operators to show Beep's health status

print("Please enter the number of lives.")
lives = int(input())

print("Please enter the energy level.")
energy = int(input())

print("Please the enter shield level.")
shield = int(input())

print("Health has been set.")

print(f"Lives:  {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")
