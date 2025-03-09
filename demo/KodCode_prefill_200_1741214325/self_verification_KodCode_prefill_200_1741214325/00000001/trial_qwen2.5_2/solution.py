def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.
    :param arr: List of integers to be sorted
    :return: Sorted list of integers
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr