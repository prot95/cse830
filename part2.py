from timsort import tim_sort
import matplotlib.pyplot as plt
import random
import time


# Generate test data
data = []
for i in range(1, 100001, 1000):
    data.append([random.randint(-100000, 100000) for j in range(i)])

# Test different values of k
k_values = [8, 16, 32, 64, 128, 256]
averageTimes = []
for k in k_values:
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
plt.plot(k_values, averageTimes)
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Insertion Sort vs Merge Sort')
plt.legend()
# plt.show()
plt.savefig('my_plot3.png')