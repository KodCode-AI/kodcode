def quick_sort_in_place(arr: list) -> None:
    """
    Sorts the given list arr in-place using the quick sort algorithm with the median-of-three pivot selection.
    
    :param arr: A list of integers to be sorted.
    """
    def _quick_sort_helper(low, high):
        if low >= high:
            return
        
        # Select the pivot using median of three strategy
        mid = (low + high) // 2
        a, b, c = arr[low], arr[mid], arr[high]
        candidates = [(a, low), (b, mid), (c, high)]
        sorted_candidates = sorted(candidates, key=lambda x: x[0])
        median_value, median_index = sorted_candidates[1]
        
        # Swap the median element with the high element
        arr[median_index], arr[high] = arr[high], arr[median_index]
        
        # Partition the array
        pivot_index = _partition(low, high)
        
        # Recursively sort the sub-arrays
        _quick_sort_helper(low, pivot_index - 1)
        _quick_sort_helper(pivot_index + 1, high)
    
    def _partition(low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i
    
    if len(arr) > 1:
        _quick_sort_helper(0, len(arr) - 1)