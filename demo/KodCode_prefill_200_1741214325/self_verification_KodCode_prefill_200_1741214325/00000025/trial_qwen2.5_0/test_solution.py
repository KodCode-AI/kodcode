from solution import *

from solution import max_sum_subarray_of_size_k

def test_max_sum_subarray_of_size_k():
    assert max_sum_subarray_of_size_k([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39
    assert max_sum_subarray_of_size_k([1, 4, -2, -10, 23, 3, 1, 0, 20], 4) == 27
    assert max_sum_subarray_of_size_k([1, -4, 2, -10, 23, 3, 1, 0, 20], 4) == 26
    assert max_sum_subarray_of_size_k([1, 4, -2, -10, 23, 3, 1, 0], 5) == 30
    assert max_sum_subarray_of_size_k([1, 2, 3], 3) == 6
    assert max_sum_subarray_of_size_k([1, 2, 3], 4) == None  # k > length of the array
    assert max_sum_subarray_of_size_k([], 1) == None  # Empty array