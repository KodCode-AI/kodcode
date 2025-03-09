from solution import *

from solution import insertion_sort

def test_insertion_sort_positive_numbers():
    assert insertion_sort([4, 5, 2, 6, 1, 3]) == [1, 2, 3, 4, 5, 6]

def test_insertion_sort_already_sorted():
    assert insertion_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_insertion_sort_negative_numbers():
    assert insertion_sort([-2, -5, -4, -3, -1]) == [-5, -4, -3, -2, -1]

def test_insertion_sort_mixed_sign_numbers():
    assert insertion_sort([-1, 3, -2, 5, 0]) == [-2, -1, 0, 3, 5]

def test_insertion_sort_duplicate_numbers():
    assert insertion_sort([4, 2, 4, 2, 1]) == [1, 2, 2, 4, 4]

def test_insertion_sort_empty_list():
    assert insertion_sort([]) == []

def test_insertion_sort_single_element():
    assert insertion_sort([5]) == [5]