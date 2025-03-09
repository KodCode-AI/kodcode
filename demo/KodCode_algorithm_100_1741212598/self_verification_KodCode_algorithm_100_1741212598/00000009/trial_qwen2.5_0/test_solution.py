from solution import *

pytest
from solution import find_min_difference

def test_find_min_difference_positive_numbers():
    assert find_min_difference([1, 2, 3, 4, 5]) == 1
    assert find_min_difference([5, 5, 5, 5, 5]) == 5
    assert find_min_difference([5, 5, 5, 5]) == 0
    assert find_min_difference([3]) == 3

def test_find_min_difference_empty_or_single_element():
    assert find_min_difference([]) == 0
    assert find_min_difference([1]) == 1

def test_find_min_difference_mixed_sign():
    assert find_min_difference([-1, -5, 5, 1]) == 0
    assert find_min_difference([9, 9, 9, 9, 9]) == 9
    assert find_min_difference([1, 5, 10, 3]) == 0
    assert find_min_difference([-1, 0, 1]) == 0
    assert find_min_difference(range(10, 0, -1)) == 1
    assert find_min_difference([-1]) == 1
    assert find_min_difference([0, 0, 0, 1, 2, -4]) == 2

def test_find_min_difference_negative_numbers():
    assert find_min_difference([-1, -5, -10, -3]) == 3