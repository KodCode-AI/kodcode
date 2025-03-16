from solution import *

from solution import find_minimum

def test_find_minimum_non_empty_array():
    assert find_minimum([3, 1, 4, 1, 5, 9]) == 1

def test_find_minimum_single_element_array():
    assert find_minimum([10]) == 10

def test_find_minimum_empty_array():
    assert find_minimum([]) == None

def test_find_minimum_negative_numbers():
    assert find_minimum([-5, -1, -6]) == -6

def test_find_minimum_with_duplicate_minimum():
    assert find_minimum([2, 2, 3, 1, 2]) == 1