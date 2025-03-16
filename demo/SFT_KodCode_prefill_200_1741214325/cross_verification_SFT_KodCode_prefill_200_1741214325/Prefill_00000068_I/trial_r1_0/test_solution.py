from solution import *

from solution import quick_sort

def test_quick_sort_empty():
    assert quick_sort([]) == []

def test_quick_sort_single_element():
    assert quick_sort([5]) == [5]

def test_quick_sort_positive_numbers():
    assert quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]

def test_quick_sort_negative_numbers():
    assert quick_sort([-3, -6, -8, -10, -1, -2, -1]) == [-10, -8, -6, -3, -2, -1, -1]

def test_quick_sort_mixed_numbers():
    assert quick_sort([-3, 6, -8, 10, -1, 2, 1, 0]) == [-8, -3, -1, 0, 1, 2, 6, 10]

def test_quick_sort_with_duplicates():
    assert quick_sort([8, 8, 8, 8, 5, 3, 2]) == [2, 3, 5, 8, 8, 8, 8]