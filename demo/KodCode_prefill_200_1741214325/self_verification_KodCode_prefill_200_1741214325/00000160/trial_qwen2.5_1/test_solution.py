from solution import *

from solution import find_second_largest

def test_find_second_largest_with_multiple_elements():
    assert find_second_largest([10, 20, 30, 40, 50]) == 40
    assert find_second_largest([55, 22, 33, 11, 99]) == 55

def test_find_second_largest_with_duplicate_max_values():
    assert find_second_largest([99, 99, 34, 67, 67]) == 67
    assert find_second_largest([88, 88, 88, 88]) is None

def test_find_second_largest_with_one_unique_element():
    assert find_second_largest([100]) is None
    assert find_second_largest([100, 100]) is None

def test_find_second_largest_with_reversed_order():
    assert find_second_largest([5, 4, 3, 2, 1]) == 4
    assert find_second_largest([20, 15, 25, 10]) == 20

def test_find_second_largest_with_negative_numbers():
    assert find_second_largest([-10, -20, -30, -25]) == -25
    assert find_second_largest([-1, -1, -2, -3, -4]) == -2