def quick_sort_in_place(arr: list) -> None:
    """
    Sorts the given list arr in-place using the quick sort algorithm with an
    in-place partitioning and median-of-three pivot selection to handle edge cases.

    :param arr: A list of integers to be sorted.
    """
    def partition(low, high):
        # Choosing the median of the first, middle, and last elements as the pivot
        mid = (low + high) // 2
        pivot = sorted([arr[low], arr[mid], arr[high]])[1]

        if pivot == arr[low]:
            pivot_index = low
        elif pivot == arr[mid]:
            pivot_index = mid
        else:
            pivot_index = high

        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
        pivot = low

        i = low + 1
        for j in range(low + 1, high + 1):
            if arr[j] < arr[pivot]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
        return i - 1

    def _quick_sort_in_place(low, high):
        if low < high:
            pivot_index = partition(low, high)
            _quick_sort_in_place(low, pivot_index - 1)
            _quick_sort_in_place(pivot_index + 1, high)

    _quick_sort_in_place(0, len(arr) - 1)