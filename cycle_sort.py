import random
import time
import timeit

#The algorithm should traverse through the list, and insert the next value into its correct position in the sorted part of the list.
#It should start from the second list element, and compare it with the first. If the second is less than the first, it should swap their positions.
#It should move to the next element and move it to its correct position, then continue like this for the rest of the list.



#Displaces the values in the list at the selected positions
def cycle(displaced_positions):
    global idk_what_this_does
    n = len(displaced_positions)
    #will repeat for each element in the list
    for number in range(0, n -1):
        #gets the digit at the current position
        digit = displaced_positions[number]
        #tells where the digit currently is
        pos = number
        #finds the correct position for the digit
        for i in range(number + 1 , n):
            #moves the digit up one spot if the value at that position is less than the digit
            if displaced_positions[i] < digit:
                pos += 1
        # tells it to continue if the digit is already in the correct position
        if pos == number:
            continue
        #swaps the digit to its correct position and takes out the number that was in that position
        displaced_positions[pos], digit = digit, displaced_positions[pos]
        #this loop basically does the same thing but for each displaced digit until the cycle is complete
        #this is for the sake of efficiency
        #the loop above is more of a failsafe
        while pos != number:
            pos = number
            for i in range(number + 1 , n):
                if displaced_positions[i] < digit:
                    pos += 1
            while digit == displaced_positions[pos]:
                pos += 1
            displaced_positions[pos], digit = digit, displaced_positions[pos]
            

      

# #Creates number list from 0 to 9999
# num_list = list(range(0, 10000))
# #Takes random sample of 1500 positions to displace
# displaced_positions = random.sample(num_list, 1500)
# displaced_positions_list = [num_list[i] for i in displaced_positions]
# random.shuffle(displaced_positions_list)


