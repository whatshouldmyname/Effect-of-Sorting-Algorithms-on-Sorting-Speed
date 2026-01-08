#The selection algorithm should traverse through the list, finding the minimal value of the list. It should move this value to the position of the first element of the.
#The algorithm should then traverse through the other 9,999 elements and when it finds the minimum value of that, move it two the second position in the newly sorted list.
#It should continue doing this for all the elements, with the sorted portion growing larger and the unsorted portion shrinking as it does. 
import time
import timeit
import random

#Go through the array to find the lowest value.
#Move the lowest value to the front of the unsorted part of the array.
#Go through the array again as many times as there are values in the array
def selection_sort(list):
    #iterates through the list
    for i in range(len(list)-1):
        #sets the minimum to the first value in the unsorted portion (everything before i is sorted)
        min_index = i
        #iterates through unsorted part of the list
        for j in range (i+1, len(list)):
            #Sets the mininum index to the index of the lowest value its found so far in the unsorted list
            if list[j] <  list[min_index]:
                min_index = j
        #Swaps the first element of the unsorted portion with the actual minimum
        list[i], list[min_index] = list[min_index], list[i]
    return list

       
# #Creates number list from 0 to 9999
# num_list = list(range(0, 10000))
# #Takes random sample of 1500 positions to displace
# displaced_positions = random.sample(num_list, 1500)
# #Shuffles the values at the displaced positions
# displaced_positions_list = [num_list[i] for i in displaced_positions]
# random.shuffle(displaced_positions_list)
# #Reassigns the shuffled values back to the displaced positions in the original list
# for i, pos in enumerate(displaced_positions):
#     num_list[pos] = displaced_positions_list[i]
# #Tests the list for displacement
# total_time = timeit.timeit(
#     stmt='selection_sort(num_list)',
#     globals=globals(),
#     number=5
# )

# average_time = total_time / 5

# print(f"First 10 of sorted list: {selection_sort(num_list)[:10]}")
# print(f"Average execution time over 5 runs: {average_time:.5f} seconds")