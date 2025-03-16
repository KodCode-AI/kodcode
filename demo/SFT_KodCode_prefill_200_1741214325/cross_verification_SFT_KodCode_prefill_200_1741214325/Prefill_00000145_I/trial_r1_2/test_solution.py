from solution import *

import pytest
from solution import bubble_sort

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    assert bubble_sort([5]) == [5]

def test_bubble_sort_sorted_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted_list():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_unsorted_list():
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bubble_sort_with_negative_numbers():
    assert bubble_sort([-2, -5, -45, 0, 2, -1, 3]) == [-45, -5, -2, -1, 0, 2, 3]

def test_bubble_sort_duplicate_numbers():
    assert bubble_sort([2, 3, 1, 3, 2]) == [1, 2, 2, 3, 3]