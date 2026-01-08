import time
import timeit
import random
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
# #The algorithm should continuously split the array in half until there are 10,000 groups of just 1 element. 
# #The algorithm should merge the groups and order them as it does. (So if there are the groups [6] and [4] it would 
# #merge them into the group [6, 4] and order it into [4, 6]. It would do the same for the next two groups of one. 
#Then, it should merge the [4, 6] group with the other group and order those. It should do this until the list is completely ordered.
def merge_sort(input_list):
    if len(input_list) > 1:
        #Splits the list in half
        left_list = input_list[:len(input_list)//2]
        right_list = input_list[len(input_list)//2:]
        #Recursively calls the function to continue splitting until there are gorups of 1
        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)
        i = j = k = 0
        result_list = []
        #Sorts the smaller lists
        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                result_list.append(left_list[i])
                i += 1
            elif right_list[j] < left_list[i]:
                result_list.append(right_list[j])
                j+=1
        result_list.extend(left_list[i:])
        result_list.extend(right_list[j: ])

        return result_list
    else:
        return input_list
#Tests function
# print (merge_sort(num_list)[0:100])
# total_time = timeit.timeit(
#     stmt='merge_sort(num_list)',
#     globals=globals(),
#     number=5
# )

# average_time = total_time / 5

# print(f"First 10 of sorted list: {merge_sort(num_list)[:10]}")
# print(f"Average execution time over 5 runs: {average_time:.5f} seconds")
