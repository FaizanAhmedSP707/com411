# A program that reviews all the concepts taught about if statements and nesting
a = input("Please input the first number: ")
b = input("Please enter the second number: ")
c = input("Please enter the third number: ")
if a == b and b == c:
    print("The numbers are equal")
elif a > b:
    if a > c:
        print("The first number is the largest")
    else:
        if b > c:
            print("The first number is the largest, the second number")