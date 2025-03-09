from solution import *

from solution import find_second_maximum

def test_find_second_maximum_with_long_list():
    assert find_second_maximum([10, 5, 2, 8, 5, 11, 13]) == 11

def test_find_second_maximum_with_repeated_max():
    assert find_second_maximum([10, 10, 10, 10]) == None

def test_find_second_maximum_single_element():
    assert find_second_maximum([5]) == None

def test_find_second_maximum_empty_list():
    assert find_second_maximum([]) == None

def test_find_second_maximum_with_negative_numbers():
    assert find_second_maximum([-10, -5, -6, -1, -3]) == -5

def test_find_second_maximum_with_mixed_numbers():
    assert find_second_maximum([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 2

def test_find_second_maximum_with_two_elements():
    assert find_second_maximum([5, 5]) == None

def test_find_second_maximum_with_descending_order():
    assert find_second_maximum([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9

def test_find_second_maximum_with_all_equal_elements():
    assert find_second_maximum([2, 2, 2, 2, 2]) == None