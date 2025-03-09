from solution import *

import pytest

def test_wiggle_sort():
    assert wiggle_sort([3, 5, 2, 1, 6, 4]) in [[3, 5, 1, 6, 2, 4], [3, 6, 1, 5, 2, 4], [5, 6, 2, 3, 1, 4]]
    assert wiggle_sort([4, 5, 5, 6]) in [[4, 5, 6, 5], [5, 6, 4, 5]]
    assert wiggle_sort([10]) == [10]
    assert wiggle_sort([1, 3, 2, 2, 3, 1]) in [[1, 3, 1, 2, 2, 3], [2, 3, 1, 3, 1, 2]]
    assert wiggle_sort([-2, -5, -4, -7, -3, -6]) in [[-2, -5, -3, -7, -4, -6], [-2, -3, -7, -4, -5, -6]]

@pytest.mark.parametrize("input, output", [
    ([3, 5, 2, 1, 6, 4], [3, 5, 1, 6, 2, 4]),
    ([4, 5, 5, 6], [4, 5, 6, 5]),
    ([10], [10]),
    ([1, 3, 2, 2, 3, 1], [1, 3, 1, 2, 2, 3])
])
def test_wiggle_sort_parametrized(input, output):
    assert wiggle_sort(input) in [[output], [output[1], output[0], *output[2:]]]

def test_wiggle_sort_empty_list():
    assert wiggle_sort([]) == []

def test_wiggle_sort_single_element_list():
    assert wiggle_sort([1]) == [1]