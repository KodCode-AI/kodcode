from solution import *

import pytest

def test_find_min_difference():
    assert find_min_difference([1, 2, 3, 4, 5]) == 1
    assert find_min_difference([5, 5, 5, 5, 5]) == 5
    assert find_min_difference([5, 5, 5, 5]) == 0
    assert find_min_difference([3]) == 3
    assert find_min_difference([]) == 0
    assert find_min_difference([1, 2, 3, 4]) == 0
    assert find_min_difference([-1, -5, 5, 1]) == 0
    assert find_min_difference([9, 9, 9, 9, 9]) == 9
    assert find_min_difference([1, 5, 10, 3]) == 1
    assert find_min_difference([-1, 0, 1]) == 0
    assert find_min_difference(range(10, 0, -1)) == 1
    assert find_min_difference([-1]) == 1
    assert find_min_difference([0, 0, 0, 1, 2, -4]) == 2
    assert find_min_difference([-1, -5, -10, -3]) == 3