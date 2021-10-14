# This program listens to sounds that Beep hears in the cave and outputs a suitable message
# This program uses a user defined function

def listen():
    # Beep is asking what sound he heard, so enter any sound, like 'rumble' for example
    print("What did I hear?")
    sound = input()
    # Putting an empty line in between for readability
    print()
    print(f"That was a loud {sound}!")


listen()
