# To get an input from the user for which direction should Beep paint in.
print("Towards which direction should I paint (up, down, left or right)? ")
direction = input()

print()
# Using an if...elif...else block to output a relevant message
if direction == 'up':
    print("I am painting in the upward direction!")
elif direction == 'left':
    print("I am painting in the leftward direction!")
elif direction == 'right':
    print("I am painting in the rightward direction!")
else:
    print("I am painting in the downward direction!")

