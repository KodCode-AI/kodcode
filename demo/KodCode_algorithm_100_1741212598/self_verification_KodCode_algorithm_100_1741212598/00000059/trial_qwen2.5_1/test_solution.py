from solution import *

import pytest

def test_custom_selection_sort_empty_list():
    assert custom_selection_sort([]) == []

def test_custom_selection_sort_only_odd_numbers():
    assert custom_selection_sort([9, 1, 5, 3]) == [9, 1, 5, 3]

def test_custom_selection_sort_only_even_numbers():
    assert custom_selection_sort([4, 2, 8, 6]) == [2, 4, 6, 8]

def test_custom_selection_sort_mixed_numbers():
    assert custom_selection_sort([9, 4, 2, 1, 5, 3]) == [3, 4, 2, 1, 5, 9]
    assert custom_selection_sort([2, 3, 6, 7, 10, 11]) == [2, 3, 6, 7, 10, 11]
    assert custom_selection_sort([13, 12, 11, 10, 9, 8]) == [9, 8, 11, 10, 13, 12]

def test_custom_selection_sort_with_zero():
    assert custom_selection_sort([0, 1, 3, 5]) == [0, 1, 3, 5]
    assert custom_selection_sort([1, 0, 3, 5]) == [0, 1, 3, 5]