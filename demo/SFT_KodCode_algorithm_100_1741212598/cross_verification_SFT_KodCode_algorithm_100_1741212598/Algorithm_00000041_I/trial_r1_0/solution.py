def quick_sort_in_place(arr: list) -> None:
    """
    Sorts the given list arr in-place using the quick sort algorithm.

    :param arr: A list of integers to be sorted.
    """
    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, low, high):
    """
    Helper function to recursively sort the array in-place.
    """
    if low >= high:
        return  # Base case: nothing to sort

    # Select pivot using median-of-three method
    pivot_index = _select_pivot(arr, low, high)
    # Swap the pivot element to the high position
    if pivot_index != high:
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    # Partition the array around the pivot
    pivot_pos = _partition(arr, low, high)
    
    # Recursively sort the subarrays
    _quick_sort(arr, low, pivot_pos - 1)
    _quick_sort(arr, pivot_pos + 1, high)


def _select_pivot(arr, low, high):
    """
    Selects the pivot as the median of the three elements at indices low, mid, and high.
    """
    mid = (low + high) // 2
    candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    # Sort the candidates based on their values and select the median
    sorted_candidates = sorted(candidates, key=lambda x: x[0])
    return sorted_candidates[1][1]


def _partition(arr, low, high):
    """
    Partitions the array using the Lomuto scheme, with the pivot at arr[high].
    Returns the final position of the pivot.
    """
    pivot = arr[high]
    i = low - 1  # Index for smaller element
    for j in range(low, high + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # The pivot's final position is i + 1
    return i + 1