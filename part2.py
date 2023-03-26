from timsort import tim_sort
from part1 import merge_sort
from part1 import insertion_sort
import matplotlib.pyplot as plt
import random
import time


# Generate test data
data = []
for i in range(1, 100001, 1000):
    data.append([random.randint(-100000, 100000) for j in range(i)])

# Test different values of k
averageTimes = []
for k in range(10, 300, 10):
    print(f"Testing k = {k}")
    total_time = 0
    for arr in data:
        start = time.time()
        tim_sort(arr, k)
        end = time.time()
        total_time += end - start
    avg_time = total_time / len(data)
    averageTimes.append((avg_time))
    print(f"Average time taken: {avg_time:.6f} seconds")

# Plot the data
plt.plot(range(10, 300, 10), averageTimes)
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Tim sort vs K')
plt.legend()
# plt.show()
plt.savefig('my_plot3.png')
plt.close()
def largeArguments():
    avg_merge = []
    avg_insertion = []
    avg_timsort = []
    for n in range(10, 1010, 10):
        merge_times = []
        insertion_times = []
        tim_sort_times = []
        for i in range(10):
            arr = [random.randint(0, 1000) for _ in range(n)]
            start = time.time()
            merge_sort(arr)
            end = time.time()
            merge_times.append(end - start)
            start = time.time()
            insertion_sort(arr)
            end = time.time()
            insertion_times.append(end - start)
            start = time.time()
            tim_sort(arr, 30)
            end = time.time()
            tim_sort_times.append(end - start)

        avg_merge.append(sum(merge_times) / len(merge_times))
        avg_insertion.append(sum(insertion_times) / len(insertion_times))
        avg_timsort.append(sum(tim_sort_times) / len(tim_sort_times))

    # Plot the data
    plt.plot(range(10, 1010, 10), avg_insertion, label='Insertion Sort')
    plt.plot(range(10, 1010, 10), avg_merge, label='Merge Sort')
    plt.plot(range(10, 1010, 10), avg_timsort, label='Tim Sort')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Insertion Sort vs Merge Sort vs Tim Sort')
    plt.legend()
    #plt.show()
    plt.savefig('timVSother.png')

largeArguments()