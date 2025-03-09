from solution import *

from solution import sum_recursive

def test_sum_recursive_empty_list():
    assert sum_recursive([]) == 0

def test_sum_recursive_single_element():
    assert sum_recursive([5]) == 5

def test_sum_recursive_positive_numbers():
    assert sum_recursive([1, 2, 3, 4, 5]) == 15

def test_sum_recursive_mixed_numbers():
    assert sum_recursive([-1, 1, -2, 2, -3, 3]) == 0

def test_sum_recursive_large_list():
    assert sum_recursive(range(1, 101)) == 5050