# A program that allows Beep the robot, to know more about the user

# Beep is asking for the user's name
print("What is your name, human?")
name = input()

# Beep is asking for the user's age
print("How old are you, human (in years)?")
age = int(input())

# Beep is asking for the user's height
print("How tall are you (in metres), human?")
height = float(input())

# Beep is asking the user's weight
print("How much do you weigh (in kilograms), human?")
weight = float(input())

BMI = float(weight / (height ** 2))

print("{n}, you are {a} years old and your BMI is {b:2.2f}.".format(n=name, a=age, b=BMI))
