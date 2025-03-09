from solution import *

import pytest

def test_wiggle_sort_positive_numbers():
    assert wiggle_sort([3, 5, 2, 1, 6, 4]) == [3, 5, 1, 6, 2, 4]
    assert wiggle_sort([1, 3, 2, 2, 3, 1]) == [1, 3, 1, 3, 2, 2]

def test_wiggle_sort_negative_numbers():
    assert wiggle_sort([-4, -2, -3, -5, 1, 2]) == [-4, -2, -5, 1, -3, 2]

def test_wiggle_sort_mixed_sign_numbers():
    assert wiggle_sort([1, 5, 1, 1, 6, 4]) == [1, 5, 1, 6, 1, 4]

def test_wiggle_sort_single_element():
    assert wiggle_sort([1]) == [1]

def test_wiggle_sort_empty_list():
    assert wiggle_sort([]) == []