from solution import *

from solution import max_subarray_sum

def test_max_subarray_sum_positive_numbers():
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_max_subarray_sum_mixed_numbers():
    assert max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7

def test_max_subarray_sum_single_element():
    assert max_subarray_sum([5]) == 5

def test_max_subarray_sum_all_negative():
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_max_subarray_sum_single_negative():
    assert max_subarray_sum([-5]) == -5

def test_max_subarray_sum_empty_array():
    with pytest.raises(ValueError):
        max_subarray_sum([])