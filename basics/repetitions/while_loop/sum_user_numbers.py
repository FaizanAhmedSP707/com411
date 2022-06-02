"""
| STORY |
Bop is continuing to run its diagnostic tests. Bop asks Beep to provide some random numbers so that it can calculate
the sum of the specified numbers.

| Tasks |
We wish to create a program to help Bop retrieve some numbers and calculate their sum.
"""

# Display a starting message
print("How many numbers should I sum up?")
count_of_numbers_to_sum = int(input())

# A control variable for the while loop
summed_number_count = 1

# Display a blank line
print()

# Summing variable for numbers
total_of_numbers = 0

# Start of while loop to add up the number of integer inputs the user makes.
while summed_number_count < count_of_numbers_to_sum + 1:  # +1 is needed for proper display of the below message
    print(f"Please enter number {summed_number_count} of {count_of_numbers_to_sum}:")
    user_number = int(input())  # Get the number from user on each iteration of the while loop
    total_of_numbers += user_number
    summed_number_count += 1

# Display the result after the while loop
print(f"\nThe answer is {total_of_numbers}")
