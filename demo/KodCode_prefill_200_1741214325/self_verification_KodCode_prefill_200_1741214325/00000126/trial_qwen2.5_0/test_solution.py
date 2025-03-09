from solution import *

from solution import is_sorted_ascending

def test_is_sorted_ascending_with_sorted_list():
    assert is_sorted_ascending([1, 2, 3, 4, 5]) == True

def test_is_sorted_ascending_with_unsorted_list():
    assert is_sorted_ascending([5, 3, 1]) == False

def test_is_sorted_ascending_with_empty_list():
    assert is_sorted_ascending([]) == True

def test_is_sorted_ascending_with_single_element_list():
    assert is_sorted_ascending([42]) == True

def test_is_sorted_ascending_with_consecutive_equal_elements():
    assert is_sorted_ascending([1, 1, 2, 2, 3]) == True

def test_is_sorted_ascending_with_mixed_elements():
    assert is_sorted_ascending([3, 1, 2, 4, 5]) == False