import random
import time
import timeit


def bubble(displaced_positions):
    #makes the variable n represent the length of the list
    n = len(displaced_positions)
    #will repeat for each element in the list
    for i in range(n):
        #sets up the swapped variable to false at the start of each loop
        swapped = False
        #will compare each element with the next one
        for j in range(0, n-i-1):
            #compares the two elements and sees if the first is greater than the second
            if displaced_positions[j] > displaced_positions[j+1]:
                #swaps the two elements
                displaced_positions[j], displaced_positions[j+1] = displaced_positions[j+1], displaced_positions[j]
                #makes swapped true to indicate a swap has occurred
                swapped = True
        #if no swaps occurred, the list is sorted and the loop can end
        if not swapped:
            break
       
