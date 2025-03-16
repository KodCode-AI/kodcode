from solution import *

from solution import quick_sort

def test_quick_sort_empty_list():
    assert quick_sort([]) == []

def test_quick_sort_single_element():
    assert quick_sort([5]) == [5]

def test_quick_sort_positive_numbers():
    arr = [3, 6, 8, 10, 1, 2, 1]
    assert quick_sort(arr) == [1, 1, 2, 3, 6, 8, 10]

def test_quick_sort_negative_numbers():
    arr = [-3, -6, -8, -10, -1, -2, -1]
    assert quick_sort(arr) == [-10, -8, -6, -3, -2, -1, -1]

def test_quick_sort_mixed_sign_numbers():
    arr = [3, -6, 8, -10, 1, -2, 1]
    assert quick_sort(arr) == [-10, -6, -2, 1, 1, 3, 8]