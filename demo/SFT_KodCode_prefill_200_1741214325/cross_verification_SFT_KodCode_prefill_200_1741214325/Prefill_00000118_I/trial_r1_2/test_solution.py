from solution import *

from solution import find_min_element

def test_find_min_element_positive_numbers():
    assert find_min_element([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 1

def test_find_min_element_negative_numbers():
    assert find_min_element([-7, -3, -1, -4, -2]) == -7

def test_find_min_element_mixed_sign_numbers():
    assert find_min_element([-1, 0, 1, -2, 2]) == -2

def test_find_min_element_single_element():
    assert find_min_element([42]) == 42

def test_find_min_element_empty_list():
    assert find_min_element([]) == None

def test_find_min_element_with_zeros():
    assert find_min_element([0, 2, 0, 1]) == 0