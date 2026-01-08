import random
import time
import timeit


def radix(displaced_positions):
    #finds the maximum number in the list 
    max_num = max(displaced_positions)
    #initializes place value
    place = 1
    #will repeat for each place value until you hit the maximum number in the list
    while max_num // place > 0:
        #makes n represent the length of the list
        n = len(displaced_positions)
        #creates a empty list to store the sorted values
        output = [0] * n
        #creates a empty list 10 elements long
        count = [0] * 10
        #will look at the digit at the current place value for each element in the list
        for i in range(n):
            #finds the digit at the current place value and increments the count of that digit
            index = (displaced_positions[i] // place) % 10
            count[index] += 1
        #modifies the count list to contain the actual positions of the digits
        for i in range(1, 10):
            count[i] += count[i - 1]
        #modifies the output list to contain the sorted values
        for i in range(n - 1, -1, -1):
            #finds the digit at the current place value
            index = (displaced_positions[i] // place) % 10
            #places the value in the correct position in the output list
            output[count[index] - 1] = displaced_positions[i]
            #resets the count list for the next iteration
            count[index] -= 1
        #copies the sorted values back to the original list
        for i in range(n):
            displaced_positions[i] = output[i]
        #moves to the next place value
        place *= 10


# #Creates number list from 0 to 9999
# num_list = list(range(0, 10000))
# #Takes random sample of 1500 positions to displace
# displaced_positions = random.sample(num_list, 1500)
# displaced_positions_list = [num_list[i] for i in displaced_positions]
# random.shuffle(displaced_positions_list)


# total_time = timeit.timeit(
#     stmt='radix(displaced_positions)',
#     globals=globals(),
#     number=5
# )

# average_time = total_time / 5

# print(f"First 10 of sorted list: {displaced_positions[:10]}")
# print(f"Average execution time over 5 runs: {average_time:.5f} seconds")
