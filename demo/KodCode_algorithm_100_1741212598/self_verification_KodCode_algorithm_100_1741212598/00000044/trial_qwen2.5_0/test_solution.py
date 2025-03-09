from solution import *

``
import pytest

def test_comb_sort_empty_list():
    assert comb_sort([]) == []

def test_comb_sort_single_element():
    assert comb_sort([5]) == [5]

def test_comb_sort_positive_numbers():
    assert comb_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]

def test_comb_sort_negative_numbers():
    assert comb_sort([-10, -5, -20, 0, 10]) == [-20, -10, -5, 0, 10]

def test_comb_sort_large_list():
    large_list = list(range(100000, 0, -1))
    sorted_list = list(range(1, 100001))
    assert comb_sort(large_list) == sorted_list

def test_comb_sort_with_duplicates():
    assert comb_sort([5, 3, 8, 4, 2, 5, 8, 3, 2, 5]) == [2, 2, 3, 3, 4, 5, 5, 5, 8, 8]

def test_comb_sort_already_sorted():
    assert comb_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_comb_sort_reverse_sorted():
    assert comb_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_comb_sort_random_data():
    random_data = [5, 3, 8, 4, 2, 7, 6, 1, 9, 10]
    sorted_data = sorted(random_data)
    assert comb_sort(random_data) == sorted_data