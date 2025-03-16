from solution import *

def test_sum_recursive_empty_list():
    assert sum_recursive([]) == 0

def test_sum_recursive_positive_numbers():
    assert sum_recursive([1, 2, 3, 4, 5]) == 15

def test_sum_recursive_with_zeros():
    assert sum_recursive([0, 0, 0, 0]) == 0

def test_sum_recursive_negative_numbers():
    assert sum_recursive([-1, -2, -3, -4, -5]) == -15

def test_sum_recursive_mixed_numbers():
    assert sum_recursive([-1, 1, -2, 2, -3, 3]) == 0

def test_sum_recursive_single_element():
    assert sum_recursive([42]) == 42