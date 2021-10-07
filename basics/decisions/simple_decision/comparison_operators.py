# This code allows Beep to identify which of two numbers is smaller, bigger or equal to each other
print("Please enter the first number:")
first = int(input())
print("Please enter the second number:")
second = int(input())

# This code checks which conditions are satisfied to output a relevant message
if first < second:
    print()
    print("The first number is the smallest!")
elif first > second:
    print()
    print("The second number is the smallest!")
else:
    print()
    print("Both are equal!")
