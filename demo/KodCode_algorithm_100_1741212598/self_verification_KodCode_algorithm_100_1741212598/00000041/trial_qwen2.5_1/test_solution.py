from solution import *

def quick_sort_in_place(arr: list) -> None:
    """
    Sorts the given list arr in-place using the quick sort algorithm.
    Implements in-place sorting and uses the median-of-three pivot selection to improve performance.
    :param arr: A list of integers to be sorted.
    """
    def _quick_sort_in_place(left, right):
        if left >= right:
            return
        pivot_idx = partition(left, right)
        _quick_sort_in_place(left, pivot_idx - 1)
        _quick_sort_in_place(pivot_idx + 1, right)

    def partition(left, right):
        mid = (left + right) // 2
        candidates = [left, mid, right]
        candidates.sort(key=lambda i: arr[i])
        pivot = arr[candidates[1]]
        pivot_idx = candidates[1]
        
        arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]  # Move pivot to the first position
        i = left + 1
        for j in range(left + 1, right + 1):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[left], arr[i - 1] = arr[i - 1], arr[left]  # Move pivot to its final position
        return i - 1

    _quick_sort_in_place(0, len(arr) - 1)

def test_quick_sort_in_place():
    # Test with normal array
    arr = [10, 5, 2, 3, 7, 6, 8, 4, 9, 1]
    quick_sort_in_place(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test with empty array
    arr = []
    quick_sort_in_place(arr)
    assert arr == []

    # Test with a single element
    arr = [5]
    quick_sort_in_place(arr)
    assert arr == [5]

    # Test with reverse sorted array
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    quick_sort_in_place(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test with almost sorted array
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quick_sort_in_place(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test with an array with negative numbers
    arr = [5, -1, 9, -2, 6, -3, 7]
    quick_sort_in_place(arr)
    assert arr == [-3, -2, -1, 5, 6, 7, 9]

test_quick_sort_in_place()