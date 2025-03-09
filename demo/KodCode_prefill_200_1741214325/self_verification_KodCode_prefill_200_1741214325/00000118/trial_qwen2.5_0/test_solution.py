from solution import *

from solution import find_minimum

def test_find_minimum_with_positive_numbers():
    assert find_minimum([3, 1, 4, 1, 5, 9]) == 1

def test_find_minimum_with_negative_numbers():
    assert find_minimum([-2, -3, -1, -4]) == -4

def test_find_minimum_with_mixed_numbers():
    assert find_minimum([-5, 0, 5, -1, 10]) == -5

def test_find_minimum_with_empty_list():
    assert find_minimum([]) is None

def test_find_minimum_with_single_element():
    assert find_minimum([42]) == 42