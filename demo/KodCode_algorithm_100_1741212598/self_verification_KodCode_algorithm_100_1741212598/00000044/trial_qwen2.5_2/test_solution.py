from solution import *

`python
import pytest

def test_comb_sort_empty_list():
    assert comb_sort([]) == []

def test_comb_sort_single_element():
    assert comb_sort([5]) == [5]

def test_comb_sort_positive_numbers():
    assert comb_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]

def test_comb_sort_negative_numbers():
    assert comb_sort([-5, -3, -8, -4, -2]) == [-8, -5, -4, -3, -2]

def test_comb_sort_mixed_sign_and_duplicates():
    assert comb_sort([5, 5, 3, 8, 4, 2, -2, -2]) == [-2, -2, 2, 3, 4, 5, 5, 8]

def test_comb_sort_large_random_list():
    import random
    data = [random.randint(-1000000, 1000000) for _ in range(100000)]
    sorted_data = sorted(data)
    assert comb_sort(data) == sorted_data

def test_comb_sort_already_sorted_list():
    assert comb_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_comb_sort_reversed_list():
    assert comb_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]