"""
| STORY |
Beep and Bop are looking for their way out of the dark forest. Beep spots some mountains in the distance and decides
that the best thing to do would be to head to the top of the mountains.  Bop is not so sure.

| Tasks |
We wish to create a program that allows us to display some mountains.
"""

# Display an introductory message that also serves as an input prompt
print("How many mountains should I display?")
user_number_for_mounts = int(input())

# Put some space between the above message and the below output
print("\nDisplaying...\n")

# Display a mountain made up of ASCII codes for the number of mountains submitted by the user
for mountain in range(user_number_for_mounts):
    print("""
             __
            /  \\_
           /^    \\
          /  ^    \\_
        _/ ^ ^     ^\\
       /  ^     ^    \\
    """)

"""
Notes to self: 
--> Using the statement 'print("""""")' allows for printing of a multi-line message without having to type in
    the escape character "\n" at the end of a line.
--> '\\' allows for displaying the backslash character in a string.
"""
