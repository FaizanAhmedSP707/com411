# The program is to allow Beep to classify his books
print("What type of cover does the book have (hard or soft)?")
cover_type = input()
print()

# This section has a nested if block to show different messages after the first check
if cover_type == 'soft':
    print("Is the book perfect-bound (yes or no) ?")
    bound_type = input()
    print()
    if bound_type == 'yes':
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books.")
else:
    print("Books with hard covers can be more expensive!")
