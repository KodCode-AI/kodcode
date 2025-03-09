from solution import *

from solution import max_subarray_sum

def test_max_subarray_sum_positive():
    assert max_subarray_sum([1, 2, 3, -4, 5], 2) == 6

def test_max_subarray_sum_negative():
    assert max_subarray_sum([-1, -2, -3, 4, 5], 3) == -6

def test_max_subarray_sum_no_negative():
    assert max_subarray_sum([1, 2, 3], 2) == 0

def test_max_subarray_sum_single_element():
    assert max_subarray_sum([1], 1) == 1

def test_max_subarray_sum_k_larger_than_nums():
    assert max_subarray_sum([1, 2, 3], 4) == 0

def test_max_subarray_sum_all_negative():
    assert max_subarray_sum([-5, -3, -10, -1], 2) == -6

def test_max_subarray_sum_mixed():
    assert max_subarray_sum([10, -5, 20, -10, -30, 50], 3) == 55