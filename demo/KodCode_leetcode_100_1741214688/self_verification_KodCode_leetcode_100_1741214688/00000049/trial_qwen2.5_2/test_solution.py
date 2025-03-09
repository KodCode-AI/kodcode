from solution import *

def test_shortest_subarray_with_at_least_sum():
    assert shortest_subarray_with_at_least_sum([2, 3, 1, 2, 4, 3], 7) == 2
    assert shortest_subarray_with_at_least_sum([1, 4, 4], 4) == 1
    assert shortest_subarray_with_at_least_sum([1, 1, 1, 1, 1, 1, 1, 1], 11) == 0
    assert shortest_subarray_with_at_least_sum([1, 2, 3, 4, 5], 15) == 5
    assert shortest_subarray_with_at_least_sum([5, 6, 7, 8, 9], 40) == 5

# Test for a case where no subarray meets the criteria
def test_no_subarray_meets_criteria():
    assert shortest_subarray_with_at_least_sum([2, 3, 1, 2], 10) == 0

# Additional test cases
def test_mixed_values():
    assert shortest_subarray_with_at_least_sum([1, 2, 3, -4, 5], 5) == 3
    assert shortest_subarray_with_at_least_sum([2, 2, 2, 2, 2], 5) == 2

def test_single_element_non_matches():
    assert shortest_subarray_with_at_least_sum([10], 15) == 0
    assert shortest_subarray_with_at_least_sum([1], 10) == 0