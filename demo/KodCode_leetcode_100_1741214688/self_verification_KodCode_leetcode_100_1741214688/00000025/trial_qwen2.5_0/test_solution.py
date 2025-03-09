from solution import *

def test_max_subarray_sum():
    assert max_subarray_sum([1, -1, 1], 3) == 0, "Test case 1 failed"
    assert max_subarray_sum([-1, -2, -3, 4, 2, 3, 1], 3) == 9, "Test case 2 failed"
    assert max_subarray_sum([1, 2, 3, -1, 2, 3], 3) == 6, "Test case 3 failed"
    assert max_subarray_sum([1, 2, 3, 4, 5], 1) == 5, "Test case 4 failed"
    assert max_subarray_sum([1, 2, 3, 4, 5], 5) == 15, "Test case 5 failed"
    assert max_subarray_sum([10, 20, 30, -45, 19, 25], 4) == 35, "Test case 6 failed"

def test_with_empty_or_shorter_than_k():
    assert max_subarray_sum([10, 20, 30], 4) == 0, "Test case 7 failed"
    assert max_subarray_sum([], 1) == 0, "Test case 8 failed"
    assert max_subarray_sum([1, 2, 3, 4, 5, 6], 7) == 0, "Test case 9 failed"

def test_no_negative_numbers_return_zero():
    assert max_subarray_sum([1, 2, 3, 4, 5], 1) == 5, "Test case 10 failed"
    assert max_subarray_sum([1, 2, 3, 4, 5], 3) == 12, "Test case 11 failed"