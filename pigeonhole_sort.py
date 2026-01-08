import random
import time
import timeit




#the cycle that does the pigeonhole sorting
def pigeon(displaced_positions):
    #finds the maximum and minimum values in the list
    minimum,maximum = min(displaced_positions), max(displaced_positions)
    #finds the size of the range of values
    size = maximum - minimum + 1
    #creates an empty list the size of the range of values
    hole = [0] * size
    #determines how many of each value there are
    for x in displaced_positions:
        #finds the location in the hole list and maps it there
        hole[x - minimum] += 1
        
    i = 0
    #places the values back into the original list in sorted order
    for something in range(size):
        #sorts through the hole list and skips past empty spots
        while hole[something] > 0:
            #undoes the increase from before
            hole[something] -= 1
            #maps the value back to the original list as the original value
            displaced_positions[i] = something + minimum
            #tells the list to move to the next position
            i += 1

      

# #Creates number list from 0 to 9999
# num_list = list(range(0, 10000))
# #Takes random sample of 1500 positions to displace
# displaced_positions = random.sample(num_list, 1500)
# displaced_positions_list = [num_list[i] for i in displaced_positions]
# random.shuffle(displaced_positions_list)



# total_time = timeit.timeit(
#     stmt='pigeon(displaced_positions)',
#     globals=globals(),
#     number=5
# )

# average_time = total_time / 5

