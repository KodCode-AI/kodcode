from solution import *

from solution import max_subarray_sum

def test_max_subarray_sum_positive_numbers():
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_max_subarray_sum_negative_numbers():
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_max_subarray_sum_with_zeros():
    assert max_subarray_sum([0, 0, 1, -1, 0]) == 1

def test_max_subarray_sum_mixed_values():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_sum_single_element():
    assert max_subarray_sum([-7]) == -7

def test_max_subarray_sum_empty_array():
    with pytest.raises(ValueError):
        max_subarray_sum([])