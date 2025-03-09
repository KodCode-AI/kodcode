from solution import *

import pytest

def test_max_monotonic_group():
    assert max_monotonic_group([5, 4, 3, 2, 1, 2, 3, 4, 5]) == 5
    assert max_monotonic_group([1, 3, 5, 4, 2, 4, 6]) == 4
    assert max_monotonic_group([1, 2, 3, 2, 1]) == 5
    assert max_monotonic_group([10]) == 1
    assert max_monotonic_group([1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 7

@pytest.mark.parametrize("heights, expected", [
    ([5, 4, 3, 2, 1, 2, 3, 4, 5], 5),
    ([1, 3, 5, 4, 2, 4, 6], 4),
    ([1, 2, 3, 2, 1], 5),
    ([10], 1),
    ([1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1], 7)
])
def test_max_monotonic_group_parametrized(heights, expected):
    assert max_monotonic_group(heights) == expected