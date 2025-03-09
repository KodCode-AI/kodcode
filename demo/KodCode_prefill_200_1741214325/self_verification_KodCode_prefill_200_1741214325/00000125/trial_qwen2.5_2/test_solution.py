from solution import *

`
def test_max_subarray_sum():
    assert max_subarray_sum([1, -2, 3, 10, -4, 7, 2, -5]) == 18
    assert max_subarray_sum([-2, -3, -1]) == -1
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([1]) == 1

def test_edge_cases():
    assert max_subarray_sum([]) == 0, "Should throw ValueError for empty array"
    assert max_subarray_sum(None) == 0, "Should throw ValueError for None"