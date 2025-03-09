from solution import *

from solution import max_subarray_sum_with_negative

def test_max_subarray_sum_with_negative():
    assert max_subarray_sum_with_negative([4, -2, 5, -1, 2, 3], 3) == 7
    assert max_subarray_sum_with_negative([-1, -2, -3, -4], 2) == -1
    assert max_subarray_sum_with_negative([1, 2, 3, 4, 5], 2) == 9  # No negative numbers in the optimal subarray
    assert max_subarray_sum_with_negative([1, -2, 3, -4, 5], 3) == 2  # Optimal subarray [3, -4, 5]
    assert max_subarray_sum_with_negative([5, 4, -2, 1], 2) == 4  # Optimal subarray [4, -2] or [-2, 1]
    assert max_subarray_sum_with_negative([10, -5, 3, -2, 8], 3) == 8  # Optimal subarray [-5, 3, -2] or [3, -2, 8]
    assert max_subarray_sum_with_negative([1, 2, 3], 4) == 0  # Subarray size exceeds the array length

# Example with no negative numbers
def test_max_subarray_no_negatives():
    assert max_subarray_sum_with_negative([10, 20, 30, 40], 2) == 70

# Example with single element array
def test_max_subarray_single_element():
    assert max_subarray_sum_with_negative([10], 1) == 10