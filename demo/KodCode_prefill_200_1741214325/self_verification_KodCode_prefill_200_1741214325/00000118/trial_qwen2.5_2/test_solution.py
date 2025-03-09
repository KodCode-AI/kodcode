from solution import *

from solution import find_minimum

def test_find_minimum_empty_list():
    assert find_minimum([]) == ValueError

def test_find_minimum_with_positive_numbers():
    assert find_minimum([3, 1, 4, 1, 5, 9]) == 1

def test_find_minimum_with_negative_numbers():
    assert find_minimum([-7, -3, -1, -5, -9]) == -9

def test_find_minimum_with_mixed_sign_numbers():
    assert find_minimum([-2, 3, -1, 4, 1]) == -2

def test_find_minimum_single_element_list():
    assert find_minimum([42]) == 42