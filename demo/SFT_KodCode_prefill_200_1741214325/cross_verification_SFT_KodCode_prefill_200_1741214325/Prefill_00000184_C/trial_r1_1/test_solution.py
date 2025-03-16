from solution import *

from solution import quicksort

def test_quicksort_empty_list():
    assert quicksort([]) == []

def test_quicksort_single_element():
    assert quicksort([5]) == [5]

def test_quicksort_sorted_list():
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    assert quicksort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]

def test_quicksort_large_random_list():
    import random
    arr = [random.randint(0, 100000) for _ in range(1000)]
    sorted_arr = sorted(arr)
    assert quicksort(arr) == sorted_arr

def test_quicksort_with_duplicates():
    assert quicksort([4, 2, 4, 8, 3, 2]) == [2, 2, 3, 4, 4, 8]