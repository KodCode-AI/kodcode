def quicksort(arr):
    def _quicksort(low, high):
        if low < high:
            # Select pivot index as the middle element
            pivot_index = (low + high) // 2
            # Swap pivot with last element
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            # Partition the array
            pivot_position = _partition(low, high)
            # Recursively sort the left and right sub-arrays
            _quicksort(low, pivot_position - 1)
            _quicksort(pivot_position + 1, high)
    
    def _partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # Swap pivot element to its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    _quicksort(0, len(arr) - 1)
    return arr