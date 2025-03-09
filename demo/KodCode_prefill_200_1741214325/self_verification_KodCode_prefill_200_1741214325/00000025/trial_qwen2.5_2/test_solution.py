from solution import *

from solution import max_sum_subarray

def test_max_sum_subarray_with_positive_numbers():
    assert max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39

def test_max_sum_subarray_with_negative_numbers():
    assert max_sum_subarray([-1, -4, -2, -10, -23, -3, -1, -20], 4) == -8

def test_max_sum_subarray_with_zero():
    assert max_sum_subarray([0, 0, 0, 0], 2) == 0

def test_max_sum_subarray_with_k_larger_than_array():
    assert max_sum_subarray([1, 2, 3], 4) is None

def test_max_sum_subarray_with_small_array():
    assert max_sum_subarray([1], 1) == 1

def test_max_sum_subarray_with_k_equal_to_array_size():
    assert max_sum_subarray([1, 2, 3, 4, 5], 5) == 15