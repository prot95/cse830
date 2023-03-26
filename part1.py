import random
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def largeArguments():
    avg_merge = []
    avg_insertion = []

    for n in range(10, 1010, 10):
        merge_times = []
        insertion_times = []
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

        avg_merge.append(sum(merge_times) / len(merge_times))
        avg_insertion.append(sum(insertion_times) / len(insertion_times))
        print(
            f'n={n}, merge={sum(merge_times) / len(merge_times)}, insertion={sum(insertion_times) / len(insertion_times)}')

    # Plot the data
    plt.plot(range(10, 1010, 10), avg_insertion, label='Insertion Sort')
    plt.plot(range(10, 1010, 10), avg_merge, label='Merge Sort')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Insertion Sort vs Merge Sort')
    plt.legend()
    #plt.show()
    plt.savefig('my_plot.png')

def smallArguments():
    avg_merge = []
    avg_insertion = []

    for n in range(10, 100, 5):
        merge_times = []
        insertion_times = []
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

        avg_merge.append(sum(merge_times) / len(merge_times))
        avg_insertion.append(sum(insertion_times) / len(insertion_times))
        print(
            f'n={n}, merge={sum(merge_times) / len(merge_times)}, insertion={sum(insertion_times) / len(insertion_times)}')

    # Plot the data
    plt.plot(range(10, 100, 5), avg_insertion, label='Insertion Sort')
    plt.plot(range(10, 100, 5), avg_merge, label='Merge Sort')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Insertion Sort vs Merge Sort')
    plt.legend()
    # plt.show()
    plt.savefig('my_plot2.png')

if __name__ == '__main__':
    largeArguments()
    smallArguments()


