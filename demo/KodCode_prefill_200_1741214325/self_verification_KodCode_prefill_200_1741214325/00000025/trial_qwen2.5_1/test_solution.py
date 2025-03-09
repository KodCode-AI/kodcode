from solution import *

from solution import max_sum_subarray

def test_max_sum_subarray_with_positive_numbers():
    assert max_sum_subarray([1, 2, 3, 4, 5], 2) == 9

def test_max_sum_subarray_with_negative_numbers():
    assert max_sum_subarray([-1, -2, -3, -4, -5], 3) == -6

def test_max_sum_subarray_with_mixed_signs():
    assert max_sum_subarray([1, -1, 5, 2, -3, 4], 3) == 5

def test_max_sum_subarray_with_single_element():
    assert max_sum_subarray([5], 1) == 5

def test_max_sum_subarray_with_invalid_k():
    assert max_sum_subarray([1, 2, 3], 4) is None

def test_max_sum_subarray_with_empty_array():
    assert max_sum_subarray([], 2) is None