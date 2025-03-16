from solution import *

from solution import is_sorted_ascending

def test_is_sorted_ascending_positive():
    assert is_sorted_ascending([1, 2, 3, 4, 5]) == True

def test_is_sorted_ascending_with_equal_elements():
    assert is_sorted_ascending([1, 1, 2, 3, 4]) == True

def test_is_sorted_ascending_negative():
    assert is_sorted_ascending([5, 3, 2, 1]) == False

def test_is_sorted_ascending_single_element():
    assert is_sorted_ascending([5]) == True

def test_is_sorted_ascending_empty_list():
    assert is_sorted_ascending([]) == True

def test_is_sorted_ascending_mixed():
    assert is_sorted_ascending([1, 2, 3, 2, 5]) == False