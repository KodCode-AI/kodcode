from solution import *

import pytest

def test_comb_sort_empty_list():
    assert comb_sort([]) == []

def test_comb_sort_single_element():
    assert comb_sort([5]) == [5]

def test_comb_sort_sorted_list():
    assert comb_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_comb_sort_unsorted_list():
    assert comb_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]

def test_comb_sort_large_list():
    large_list = list(range(100000, 0, -1)) + list(range(0, 100000))
    sorted_list = comb_sort(large_list)
    assert sorted_list == list(range(100000))

def test_comb_sort_reversed_list():
    assert comb_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_comb_sort_duplicate_elements():
    assert comb_sort([5, 3, 8, 5, 2, 3]) == [2, 3, 3, 5, 5, 8]