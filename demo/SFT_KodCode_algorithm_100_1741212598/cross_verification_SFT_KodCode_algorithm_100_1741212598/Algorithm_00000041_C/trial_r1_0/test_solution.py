from solution import *

import random

def quick_sort_in_place(arr):
    """
    Sorts the given list arr in-place using the quick sort algorithm with an in-place median-of-three pivot selection.
    """
    def partition(low, high):
        mid = (low + high) // 2
        pivot_candidates = [arr[low], arr[mid], arr[high]]
        pivot_candidates.sort()
        pivot_value = pivot_candidates[1]
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

# Test Cases
def test_quick_sort_in_place():
    arr = [10, 5, 2, 3, 7, 6, 8, 4, 9, 1]
    quick_sort_in_place(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    arr = [1, 2, 3, 4, 5]
    quick_sort_in_place(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    quick_sort_in_place(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr = []
    quick_sort_in_place(arr)
    assert arr == []

    arr = [random.randint(-1000, 1000) for _ in range(10000)]
    quick_sort_in_place(arr)
    assert arr == sorted(arr)

test_quick_sort_in_place()