# This program will help Beep and Bop cross the bridge

def cross_bridge(bridge_dist_crossed):
    # Local variable to be used with the loop
    step_count = 0
    # Using a loop, along with the passed in parameter to do the needed
    for step_count in range(bridge_dist_crossed):
        # Print this message for each step taken
        print("Crossed step.")
        # Incrementing the step counter
        step_count += 1

    if step_count < 5:
        # Simple check to see whether steps taken are less or more than 5.
        print("We must keep going!")
    else:
        print("The bridge is collapsing!")


cross_bridge(3)
cross_bridge(6)
