# This part  allows Beep to count which of the 3 numbers entered is even or odd
print("Please enter the first whole number: ")
first = int(input())
print("Please enter the second whole number: ")
second = int(input())
print("Please enter the third whole number: ")
third = int(input())
# These 2 variables below are used to check how many are odd/even
odd_count = int()
even_count = int()

# The following 'if..elif..else' block is used to count how many are odd/even
if first % 2 != 0:
    odd_count += 1
elif first % 2 == 0:
    even_count += 1
else:
    print()
    print("Please input a whole number!")
if second % 2 != 0:
    odd_count += 1
elif second % 2 == 0:
    even_count += 1
else:
    print()
    print("Please enter a whole number!")
if third % 2 != 0:
    odd_count += 1
elif third % 2 == 0:
    even_count += 1
else:
    print()
    print("Please enter a whole number!")

print()
print(f"There were {even_count} even and {odd_count} odd numbers.")
