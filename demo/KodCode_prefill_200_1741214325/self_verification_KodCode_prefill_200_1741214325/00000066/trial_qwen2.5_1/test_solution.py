from solution import *

def test_max_subarray_sum():
    assert max_subarray_sum([1, 2, 3, -2, 5]) == 9  # [1, 2, 3, -2, 5] -> 9
    assert max_subarray_sum([-1, -2, -3, -4]) == -1  # Single element
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # [4, -1, 2, 1] -> 6
    assert max_subarray_sum([0, -1, 2, -3, 5]) == 5  # Single positive number
    assert max_subarray_sum([-3, -6, -2, -5, -4]) == -2  # All negative numbers
    assert max_subarray_sum([]) == 0  # Empty array