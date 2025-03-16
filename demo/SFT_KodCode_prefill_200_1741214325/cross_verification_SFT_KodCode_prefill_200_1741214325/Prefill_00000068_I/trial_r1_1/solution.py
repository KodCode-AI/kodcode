def quick_sort(arr):
    # Base case: If the array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr.copy()
    else:
        # Select the last element as the pivot
        pivot = arr[-1]
        # Create a list for elements less than or equal to the pivot
        left = [x for x in arr[:-1] if x <= pivot]
        # Create a list for elements greater than the pivot
        right = [x for x in arr[:-1] if x > pivot]
        # Recursively sort the left and right partitions and combine results
        return quick_sort(left) + [pivot] + quick_sort(right)