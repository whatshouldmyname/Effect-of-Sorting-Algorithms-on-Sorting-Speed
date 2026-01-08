import random
import timeit
#The Quicksort algorithm should work with a “Divide and Conquer” Approach
#It should determine a pivot, which could be the first element, last element, middle element, or any random element. 
#It should then partition the array so that the elements that are less than the pivot element are to the left of it, and the elements that are greater are to the right. 
#The quicksort algorithm would then be run again on each new sublist, with a new pivot, partitioning the lists into smaller and smaller sublists.
#This process will be complete when one of the sublists has one or fewer elements

#Creates number list from 0 to 9999
# num_list = list(range(0, 10000))
# #Takes random sample of 1500 positions to displace
# displaced_positions = random.sample(num_list, 1500)
# #Shuffles the values at the displaced positions
# displaced_positions_list = [num_list[i] for i in displaced_positions]
# random.shuffle(displaced_positions_list)
#Reassigns the shuffled values back to the displaced positions in the original list
# for i, pos in enumerate(displaced_positions):
#     num_list[pos] = displaced_positions_list[i]
# #Tests the list for displacement
# print(num_list[0:100])
# #Lomuto partition algorithm
def partition(input_list, left, right):
    #selects pivot element randomly from the list
    pivot_position = random.randint(left, right)
    #sets the value of the pivot
    pivot = input_list[pivot_position]
    #Moves the pivot to the end
    input_list[pivot_position], input_list[right] = input_list[right], input_list[pivot_position]
    i = left
    #iterates through the list, swapping the values of i and j depending on the values
    for j in range(left, right):
        if input_list[j] <= pivot:
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i+=1
    #moves the pivot back into position
    input_list[i], input_list[right] = input_list[right], input_list[i]
    return i
def quicksort(input_list, left, right):
    #ends the function 
    if left>= right:
        return
    #recursively calls quicksort to use divide and conquer approach
    pivot_index = partition(input_list, left, right)
    quicksort(input_list, left, pivot_index-1)
    quicksort(input_list, pivot_index+1, right)     

# total_time = timeit.timeit(
#     stmt='quicksort(num_list, 0, len(num_list)-1)',
#     globals=globals(),
#     number=5
# )

# average_time = total_time / 5
# print(f"Average execution time over 5 runs: {average_time:.5f} seconds")
