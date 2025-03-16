from solution import *

from solution import max_distinct_elements_in_subarray

def test_max_distinct_elements_in_subarray():
    assert max_distinct_elements_in_subarray([1, 2, 1, 3, 4, 3], 3) == 3
    assert max_distinct_elements_in_subarray([1, 2, 1, 3, 4, 3, 5], 3) == 3
    assert max_distinct_elements_in_subarray([1, 2, 1, 3, 4, 3, 5], 4) == 4
    assert max_distinct_elements_in_subarray([1, 2, 1, 3, 4, 3, 5], 7) == 5
    assert max_distinct_elements_in_subarray([1, 1, 2, 2, 3, 3], 3) == 2
    assert max_distinct_elements_in_subarray([1, 2, 3, 4, 5, 6], 1) == 1
    assert max_distinct_elements_in_subarray([], 3) == 0
    assert max_distinct_elements_in_subarray([1, 2, 3, 4, 5, 6], 0) == 0