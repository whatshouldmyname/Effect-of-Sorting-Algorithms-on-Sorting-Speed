import random
import time
import timeit

#The algorithm should traverse through the list, and insert the next value into its correct position in the sorted part of the list.
#It should start from the second list element, and compare it with the first. If the second is less than the first, it should swap their positions.
#It should move to the next element and move it to its correct position, then continue like this for the rest of the list.

       


def insertion(displaced_positions):
    n = len(displaced_positions)
    for i in range(1, n):
        # = the value at the current position
        current_value = displaced_positions[i]
        # sets up the position before the current one so it can be called later
        number_before = i - 1
        #determine if the value before is greater than the current value
        while number_before >= 0 and current_value < displaced_positions[number_before]:
            #shifts the larger value up one position
            displaced_positions[number_before + 1] = displaced_positions[number_before]
            #undoes one to the position to keep checking previous values
            number_before -= 1
        #changes the current value to the correct position
        displaced_positions[number_before + 1] = current_value

