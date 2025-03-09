from solution import *

import pytest

def test_insertion_sort_empty_list():
    assert insertion_sort([]) == []

def test_insertion_sort_sorted_list():
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_insertion_sort_reverse_sorted_list():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_insertion_sort_with_duplicates():
    assert insertion_sort([4, 3, 2, 5, 3, 5]) == [2, 3, 3, 4, 5, 5]

def test_insertion_sort_random_list():
    assert insertion_sort([3, 6, 1, 8, 4]) == [1, 3, 4, 6, 8]

def test_insertion_sort_negative_numbers():
    assert insertion_sort([-5, -2, -3, -1]) == [-5, -3, -2, -1]