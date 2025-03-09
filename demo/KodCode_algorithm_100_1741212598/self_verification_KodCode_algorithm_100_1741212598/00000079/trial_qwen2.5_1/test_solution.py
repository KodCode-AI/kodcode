from solution import *

from solution import wiggle_sort

def test_wiggle_sort_with_positive_numbers():
    assert wiggle_sort([3, 5, 2, 1, 6, 4]) == [3, 5, 1, 6, 2, 4]

def test_wiggle_sort_with_negative_numbers():
    assert wiggle_sort([-2, -5, -4, -7, -3]) == [-2, -5, -4, -7, -3]

def test_wiggle_sort_with_mixed_sign_numbers():
    assert wiggle_sort([-2, 5, -3, -2, 3, 3]) == [-2, 5, -3, 3, -2, 3]

def test_wiggle_sort_with_single_element():
    assert wiggle_sort([1]) == [1]

def test_wiggle_sort_with_empty_list():
    assert wiggle_sort([]) == []