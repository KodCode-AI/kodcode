from solution import *

import pytest

def test_custom_selection_sort():
    assert custom_selection_sort([]) == []
    assert custom_selection_sort([9, 4, 2, 1, 5, 3]) == [3, 4, 2, 1, 5, 9]
    assert custom_selection_sort([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    assert custom_selection_sort([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    assert custom_selection_sort([3, 6, 1, 7, 2]) == [3, 2, 1, 7, 6]
    assert custom_selection_sort([11, 13, 17, 19, 23]) == [11, 13, 17, 19, 23]

def test_with_single_elements():
    assert custom_selection_sort([2]) == [2]
    assert custom_selection_sort([1]) == [1]

def test_with_mix_of_evens_and_odds():
    assert custom_selection_sort([2, 3, 6, 1, 8, 5]) == [2, 3, 6, 1, 8, 5]
    assert custom_selection_sort([4, 9, 2, 7, 10, 1]) == [2, 9, 4, 7, 10, 1]