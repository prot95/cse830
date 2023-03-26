def tim_sort(arr, k):
    def insertion_sort(arr, start, end):
        for i in range(start + 1, end + 1):
            key = arr[i]
            j = i - 1
            while j >= start and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge(arr, start, mid, end):
        if arr[mid] <= arr[mid + 1]:
            return

        i = start
        j = mid + 1
        aux = arr[start:end+1]

        for k in range(start, end + 1):
            if i > mid:
                arr[k] = aux[j-start]
                j += 1
            elif j > end:
                arr[k] = aux[i-start]
                i += 1
            elif aux[i-start] <= aux[j-start]:
                arr[k] = aux[i-start]
                i += 1
            else:
                arr[k] = aux[j-start]
                j += 1

    def tim_sort_util(arr, start, end, k):
        if end - start + 1 <= k:
            insertion_sort(arr, start, end)
            return

        mid = start + (end - start) // 2
        tim_sort_util(arr, start, mid, k)
        tim_sort_util(arr, mid + 1, end, k)
        merge(arr, start, mid, end)

    tim_sort_util(arr, 0, len(arr) - 1, k)
