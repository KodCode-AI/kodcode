def quick_sort_in_place(arr: list) -> None:
    """
    Sorts the given list arr in-place using the quick sort algorithm.
    
    :param arr: A list of integers to be sorted.
    """
    def helper(low, high):
        if low < high:
            pivot_index = partition(low, high)
            helper(low, pivot_index - 1)
            helper(pivot_index + 1, high)
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    helper(0, len(arr) - 1)