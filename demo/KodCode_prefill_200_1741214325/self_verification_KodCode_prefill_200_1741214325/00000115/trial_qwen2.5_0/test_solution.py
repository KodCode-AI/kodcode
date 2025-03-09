from solution import *

from solution import find_max

def test_find_max_positive_numbers():
    assert find_max([1, 2, 3, 4, 5]) == 5

def test_find_max_with_negative_numbers():
    assert find_max([-5, -2, -3, -1]) == -1

def test_find_max_mixed_sign_numbers():
    assert find_max([-1, 0, 1, 2, -2, 3]) == 3

def test_find_max_single_element():
    assert find_max([42]) == 42

def test_find_max_empty_list():
    assert find_max([]) == ValueError
    # Importing the exception here for completeness, but it's more common to handle it separately
    # from pytest import raises
    # with raises(ValueError):
    #     find_max([])