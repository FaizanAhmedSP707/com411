"""
This time, Beep finds himself in a deep forest
He will use the following program to decide whether to continue
going deeper into the forest or find a way out
"""
print("What did I hear?")
heard = input()
print()
print("What did I see?")
seen = input()
print()

# Checking what Beep heard and saw to output a different message
if heard == 'grrr' and seen == 'two red eyes':
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")
