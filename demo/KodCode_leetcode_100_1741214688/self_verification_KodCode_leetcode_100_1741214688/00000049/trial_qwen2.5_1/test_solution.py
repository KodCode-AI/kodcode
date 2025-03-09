from solution import *

from solution import shortest_subarray_with_target

def test_shortest_subarray_with_target():
    assert shortest_subarray_with_target([2, 3, 1, 2, 4, 3], 7) == 2
    assert shortest_subarray_with_target([1, 4, 4], 4) == 1
    assert shortest_subarray_with_target([2, 3, 1, 2, 4, 3], 11) == 3
    assert shortest_subarray_with_target([1, 1, 1, 1, 1, 1, 1, 1], 11) == 0
    assert shortest_subarray_with_target([1, 2, 3, 4, 5], 15) == 5
    assert shortest_subarray_with_target([10, 2, -2, -20, 10], -10) == 3
    assert shortest_subarray_with_target([1], 2) == 0
    assert shortest_subarray_with_target([5, 6], 11) == 2

def test_cases_with_small_arrays():
    assert shortest_subarray_with_target([2, 3], 5) == 2
    assert shortest_subarray_with_target([1], 2) == 0
    assert shortest_subarray_with_target([], 2) == 0