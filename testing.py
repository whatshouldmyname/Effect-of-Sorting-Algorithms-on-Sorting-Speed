import random
import timeit
import bubble_sort, cycle_sort, insertion_sort, merge_sort, pigeonhole_sort
import quick_sort, radix_sort, selection_sort, tim_sort

def list_generator():
    num_list = list(range(0, 10000))
    displaced_positions = random.sample(num_list, 1500)
    displaced_positions_list = [num_list[i] for i in displaced_positions]
    random.shuffle(displaced_positions_list)
    for i, pos in enumerate(displaced_positions):
        num_list[pos] = displaced_positions_list[i]
    return num_list

def normalize_quick_sort(input_list):
    quick_sort.quicksort(input_list, 0, len(input_list)-1 )
    return input_list

def sort_everything():
    algorithms = [
        bubble_sort.bubble,
        cycle_sort.cycle,
        insertion_sort.insertion,
        merge_sort.merge_sort,
        pigeonhole_sort.pigeon,
        radix_sort.radix,
        selection_sort.selection_sort,
        tim_sort.tim_sort,
        normalize_quick_sort
    ]

    # Generate 3 independent lists
    lists = [list_generator() for _ in range(3)]

    results = {}

    for algorithm in algorithms:
        algo_name = algorithm.__name__
        results[algo_name] = []

        for lst in lists:
            # Time the algorithm on this list, 5 runs
            total_time = timeit.timeit(
                stmt=lambda: algorithm(lst[:]),
                number=5
            )
            avg_time = total_time / 5
            results[algo_name].append(avg_time)

    return results


# Run everything
outputs = sort_everything()

# Print results
for alg, averages in outputs.items():
    print(f"{alg}:")
    for i, avg in enumerate(averages, start=1):
        print(f"  List {i} average: {avg:.5f} seconds")
