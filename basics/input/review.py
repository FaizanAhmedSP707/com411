# Showing that Beep can wear glasses

print("Please enter a character for the eye.")
eye = input()
print("Please enter the length of the glasses.")
glass_length = int(input())

# The following code is used to basically draw glasses using ascii characters

print(f"-----{' ' * glass_length}-----")
print(f"| {eye} | {'-' * (glass_length - 1)}| {eye} |")
print(f"-----{' ' * glass_length}-----")
