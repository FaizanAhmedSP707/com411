"""
| STORY |
Bop is now fully charged and performing a diagnostic test to ensure all its systems are functioning as expected.
Bop begins by performing a simple calculation.

| Tasks |
We wish to create a program to help Bop calculate the sum of the first 100 numbers.
"""

# Display a start message
print("Calculating the sum of the first 100 numbers...")

# A control variable for the while loop
number_count = 1

# Variable to calculate the sum of the first 100 numbers
totals = 0

# Start of the while loop
while number_count <= 100:
    totals = totals + number_count
    number_count += 1

# Display the final result
print(f"...Done! The answer is {totals}")
