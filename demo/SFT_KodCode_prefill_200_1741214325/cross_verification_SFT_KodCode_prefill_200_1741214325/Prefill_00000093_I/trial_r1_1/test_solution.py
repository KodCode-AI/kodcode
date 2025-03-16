from solution import *

import pytest

def test_find_smallest_number_with_positive_numbers():
    arr = [4, 2, 9, 7, 5, 6]
    assert find_smallest_number(arr) == 2

def test_find_smallest_number_with_negative_numbers():
    arr = [-5, -2, -6, -1, -3]
    assert find_smallest_number(arr) == -6

def test_find_smallest_number_with_mixed_sign_numbers():
    arr = [2, -3, 5, -1, 0, -4]
    assert find_smallest_number(arr) == -4

def test_find_smallest_number_with_single_element():
    arr = [7]
    assert find_smallest_number(arr) == 7

def test_find_smallest_number_with_empty_array():
    arr = []
    assert find_smallest_number(arr) is None

def test_find_smallest_number_with_duplicate_numbers():
    arr = [3, 3, 3, 3, 3]
    assert find_smallest_number(arr) == 3