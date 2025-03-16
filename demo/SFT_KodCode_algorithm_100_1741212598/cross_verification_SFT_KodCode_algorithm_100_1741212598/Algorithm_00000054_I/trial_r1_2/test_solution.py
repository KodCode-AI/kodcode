from solution import *

import pytest

def test_find_peak():
    assert find_peak([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 5
    assert find_peak([1, 10, 9, 8, 7, 6, 5, 4]) == 10
    assert find_peak([1, 9, 8, 7]) == 9
    assert find_peak([1, 2, 3, 4, 5, 6, 7, 0]) == 7
    assert find_peak([1, 2, 3, 4, 3, 2, 1, 0, -1, -2]) == 4
    assert find_peak([1, 2, 2, 1, 0, -1, -2]) == 2
    assert find_peak([1, 1]) == 1
    assert find_peak([1]) == 1
    assert find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10]) == 12
    assert find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9]) == 12
    assert find_peak([]) is None
    assert find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert find_peak([1, 2, 2, 2, 2, 2, 1]) == 2

def test_edge_cases():
    assert find_peak([1]) == 1
    assert find_peak([1, 2]) == 2
    assert find_peak([2, 1]) == 2
    assert find_peak([1, 1]) == 1