from solution import *

from solution import max_subarray_sum

def test_max_subarray_sum_single_element():
    assert max_subarray_sum([1]) == 1

def test_max_subarray_sum_positive_numbers():
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_max_subarray_sum_mixed_negative_and_positive_numbers():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_sum_all_negative_numbers():
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_max_subarray_sum_empty_array():
    assert max_subarray_sum([]) == 0

def test_max_subarray_sum_single_negative_number():
    assert max_subarray_sum([-5]) == -5

def test_max_subarray_sum_alternating_signs():
    assert max_subarray_sum([1, -1, 1, -1, 3]) == 3

def test_max_subarray_sum_with_zero():
    assert max_subarray_sum([0, 1, -1, 2, -3, 4, 0, -4, 5]) == 6