from sortedcontainers import SortedDict
import random
import time
import matplotlib.pyplot as plt

def binary_tree_insertion(dictionary):
    sorted_dict = SortedDict()
    for key, value in dictionary.items():
        sorted_dict[key] = value

def hash_table_insertion(dictionary):
    hash_dict = dict()
    for key, value in dictionary.items():
        hash_dict[key] = value

def binary_tree_deletion(dictionary):
    sorted_dict = SortedDict(dictionary)
    for key in dictionary.keys():
        del sorted_dict[key]

def hash_table_deletion(dictionary):
    hash_dict = dict(dictionary)
    for key in dictionary.keys():
        del hash_dict[key]

def test_data_structure_performance():
    avg_bst_insert, avg_bst_delete = [], []
    avg_hash_insert, avg_hash_delete = [], []
    inputArray = []
    for i in range(1, 8):
        n = 10**i
        dictionary = {random.randint(0, n): random.randint(0, n) for _ in range(n)}
        inputArray.append(n)
        # Test binary tree insertion
        binary_tree_insertion_time = 0
        for _ in range(3):
            start_time = time.perf_counter()
            binary_tree_insertion(dictionary)
            end_time = time.perf_counter()
            binary_tree_insertion_time += end_time - start_time
        binary_tree_insertion_time /= 3
        avg_bst_insert.append(binary_tree_insertion_time)

        # Test hash table insertion
        hash_table_insertion_time = 0
        for _ in range(3):
            start_time = time.perf_counter()
            hash_table_insertion(dictionary)
            end_time = time.perf_counter()
            hash_table_insertion_time += end_time - start_time
        hash_table_insertion_time /= 3
        avg_hash_insert.append(hash_table_insertion_time)

        # Test binary tree deletion
        binary_tree_deletion_time = 0
        for _ in range(3):
            start_time = time.perf_counter()
            binary_tree_deletion(dictionary)
            end_time = time.perf_counter()
            binary_tree_deletion_time += end_time - start_time
        binary_tree_deletion_time /= 3
        avg_bst_delete.append(binary_tree_deletion_time)

        # Test hash table deletion
        hash_table_deletion_time = 0
        for _ in range(3):
            start_time = time.perf_counter()
            hash_table_deletion(dictionary)
            end_time = time.perf_counter()
            hash_table_deletion_time += end_time - start_time
        hash_table_deletion_time /= 3
        avg_hash_delete.append(hash_table_deletion_time)

        print(f"n={n}: Binary Tree Insertion Time={binary_tree_insertion_time:.6f}, Hash Table Insertion Time={hash_table_insertion_time:.6f}, Binary Tree Deletion Time={binary_tree_deletion_time:.6f}, Hash Table Deletion Time={hash_table_deletion_time:.6f}")
        plotGraphs(avg_bst_insert, avg_bst_delete, avg_hash_insert, avg_hash_delete, inputArray)

def plotGraphs(avg_bst_insert, avg_bst_delete, avg_hash_insert, avg_hash_delete, inputArray):
    plt.plot(inputArray, avg_bst_insert, label='BST')
    plt.plot(inputArray, avg_hash_insert, label='Hash Table')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Insertion Time Comparison')
    plt.legend()
    # plt.show()
    plt.savefig('ans3_1.png')
    plt.close()

    plt.plot(inputArray, avg_bst_delete, label='BST')
    plt.plot(inputArray, avg_hash_delete, label='Hash Table')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Deletion Time Comparison')
    plt.legend()
    # plt.show()
    plt.savefig('ans3_2.png')
    plt.close()

if __name__ == "__main__":
    test_data_structure_performance()
