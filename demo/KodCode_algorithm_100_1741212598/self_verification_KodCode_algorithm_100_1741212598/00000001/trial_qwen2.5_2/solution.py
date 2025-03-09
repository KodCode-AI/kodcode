def intro_sort(array: list, start: int, end: int, size_threshold: int, max_depth: int) -> list:
    """
    Sorts the array between indices `start` and `end` (inclusive) using Introspective Sort.
    
    :param array: The array to be sorted
    :param start: The starting index of the subarray to sort
    :param end: The ending index of the subarray to sort
    :param size_threshold: The threshold size at which insertion sort is used
    :param max_depth: The maximum depth of recursion before switching to Heap Sort
    :return: The sorted subarray
    """
    depth = 0

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def insertion_sort(arr, low, high):
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i - 1
            while j >= low and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def introsort(arr, low, high, max_depth):
        nonlocal depth
        if high - low < 1:
            return
        if depth >= max_depth:
            heap_sort(arr, low, high)
            return
        depth += 1
        size = high - low
        if size < size_threshold:
            insertion_sort(arr, low, high)
        else:
            pivot_index = partition(arr, low, high)
            introsort(arr, low, pivot_index - 1, max_depth)
            introsort(arr, pivot_index + 1, high, max_depth)
        depth -= 1

    def heap_sort(arr, low, high):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[i] < arr[left]:
                largest = left
            if right < n and arr[largest] < arr[right]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = high - low + 1
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(high - 1, low - 1, -1):
            arr[i], arr[low] = arr[low], arr[i]
            heapify(arr, i, low)

    introsort(array, start, end, max_depth)
    return array