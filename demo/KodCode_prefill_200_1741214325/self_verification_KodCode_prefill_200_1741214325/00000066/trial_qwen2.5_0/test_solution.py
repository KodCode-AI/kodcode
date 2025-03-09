from solution import *

``
from solution import max_subarray_sum

def test_max_subarray_sum_positive():
    assert max_subarray_sum([1, 2, 3, -2, 5]) == 9

def test_max_subarray_sum_single_element():
    assert max_subarray_sum([5]) == 5

def test_max_subarray_sum_all_negative():
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_max_subarray_sum混合正负数():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_sum_empty_array():
    assert max_subarray_sum([]) == 0