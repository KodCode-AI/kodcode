from solution import *

from solution import selection_sort

def test_selection_sort_sorted_array():
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_selection_sort_reversed_array():
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_selection_sort_duplicate_elements():
    assert selection_sort([4, 2, 2, 1, 3]) == [1, 2, 2, 3, 4]

def test_selection_sort_with_negative_numbers():
    assert selection_sort([3, -1, -2, 6, 4]) == [-2, -1, 3, 4, 6]

def test_selection_sort_empty_list():
    assert selection_sort([]) == []

def test_selection_sort_single_element_list():
    assert selection_sort([5]) == [5]