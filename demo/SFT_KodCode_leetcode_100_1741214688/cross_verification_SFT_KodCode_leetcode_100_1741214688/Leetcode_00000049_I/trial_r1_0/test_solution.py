from solution import *

import pytest

def test_shortest_subarray_with_sum_at_least_target():
    assert shortest_subarray_with_sum_at_least_target([2, 3, 1, 2, 4, 3], 7) == 2
    assert shortest_subarray_with_sum_at_least_target([1, 4, 4], 4) == 1
    assert shortest_subarray_with_sum_at_least_target([1, 1, 1, 1, 1, 1, 1, 1], 11) == 0
    assert shortest_subarray_with_sum_at_least_target([1], 1) == 0
    assert shortest_subarray_with_sum_at_least_target([1, 2, 3, 4, 5], 15) == 5
    assert shortest_subarray_with_sum_at_least_target([1, 2, 3, 4, 5], 16) == 0