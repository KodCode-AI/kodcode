from solution import *

import random

def quick_sort_in_place(arr: list) -> None:
    """
    Sorts the given list arr in-place using the quick sort algorithm with an
    in-place partitioning and median-of-three pivot selection to handle edge cases.
    
    :param arr: A list of integers to be sorted.
    """
    def partition(low, high):
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

def test_quick_sort_in_place():
    # Test with a list of positive integers
    arr = [random.randint(1, 100) for _ in range(10)]
    quick_sort_in_place(arr)
    assert arr == sorted(arr)

    # Test with a list of negative integers
    arr = [-x for x in arr]
    quick_sort_in_place(arr)
    assert arr == sorted(arr, reverse=True)

    # Test with a list of mixed integers
    arr = [random.randint(-100, 100) for _ in range(10)]
    quick_sort_in_place(arr)
    assert arr == sorted(arr)

    # Test with an empty list
    arr = []
    quick_sort_in_place(arr)
    assert arr == []

    # Test with a single-element list
    arr = [5]
    quick_sort_in_place(arr)
    assert arr == [5]

    # Test with a nearly sorted list
    arr = [x for x in range(1, 10)]
    arr[0], arr[1] = arr[1], arr[0]  # swap first two elements
    quick_sort_in_place(arr)
    assert arr == list(range(1, 10))

    # Test with a large list of unique elements
    arr = list(range(1, 10001))
    random.shuffle(arr)
    quick_sort_in_place(arr)
    assert arr == list(range(1, 10001))

    # Test with a large list of repeated elements
    arr = [x % 100 for x in range(1, 5001)]
    quick_sort_in_place(arr)
    assert arr == sorted(arr)

test_quick_sort_in_place()