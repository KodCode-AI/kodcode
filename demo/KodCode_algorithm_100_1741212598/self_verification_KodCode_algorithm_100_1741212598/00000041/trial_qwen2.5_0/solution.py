def quick_sort_in_place(arr: list) -> None:
    """
    Sorts the given list arr in-place using the quick sort algorithm with an in-place median-of-three pivot selection.
    """
    def partition(low, high):
        # Choosing the median of the first, middle, and last elements as the pivot
        mid = (low + high) // 2
        pivot_candidates = [arr[low], arr[mid], arr[high]]
        pivot_candidates.sort()
        pivot_value = pivot_candidates[1]

        # Move the pivot to the end for partitioning
        pivot_index = arr.index(pivot_value)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot_index = high

        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot_value:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[pivot_index] = arr[pivot_index], arr[i + 1]
        return i + 1

    def _quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)

    _quick_sort(0, len(arr) - 1)