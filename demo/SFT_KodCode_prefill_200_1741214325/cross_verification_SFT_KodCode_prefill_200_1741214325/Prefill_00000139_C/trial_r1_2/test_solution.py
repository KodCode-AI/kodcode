from solution import *

from solution import max_subarray_kadane

def test_max_subarray_kadane():
    assert max_subarray_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "Test Case 1 Failed"
    assert max_subarray_kadane([1]) == 1, "Test Case 2 Failed"
    assert max_subarray_kadane([-1, -2, -3, -4]) == -1, "Test Case 3 Failed"
    assert max_subarray_kadane([5, 4, -1, 7, 8]) == 23, "Test Case 4 Failed"