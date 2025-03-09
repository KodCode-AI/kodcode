from solution import *

from solution import max_subarray_kadane

def test_max_subarray_kadane_positive():
    assert max_subarray_kadane([1, 2, 3, -2, 5]) == 9

def test_max_subarray_kadane_single_negative():
    assert max_subarray_kadane([-1]) == -1

def test_max_subarray_kadane_all_negative():
    assert max_subarray_kadane([-2, -3, -1, -5]) == -1

def test_max_subarray_kadane_random():
    assert max_subarray_kadane([2, 3, -2, 1, -5, 4, -3]) == 6

def test_max_subarray_kadane_mixed():
    assert max_subarray_kadane([5, -2, 3, 4, -1, 2, 1, -5, 4]) == 10

def test_max_subarray_kadane_empty():
    assert max_subarray_kadane([]) == 0