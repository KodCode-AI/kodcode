from solution import *

from solution import max_monotonic_group

def test_max_monotonic_group():
    assert max_monotonic_group([5, 4, 3, 2, 1, 2, 3, 4, 5]) == 5
    assert max_monotonic_group([1, 3, 5, 4, 2, 4, 6]) == 4
    assert max_monotonic_group([10, 11, 12, 13, 14, 15]) == 6
    assert max_monotonic_group([15, 14, 13, 12, 11, 10]) == 6
    assert max_monotonic_group([8, 7, 6, 5, 4, 3, 2, 1, 8, 9]) == 5
    assert max_monotonic_group([1]) == 1
    assert max_monotonic_group([2, 2, 2, 2]) == 1
    assert max_monotonic_group([1, 2, 3, 2, 1, 0]) == 3

test_max_monotonic_group()