from solution import *

def test_max_consecutive_ones():
    assert max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert max_consecutive_ones([0, 0, 1, 1, 1, 0, 0], 0) == 3
    assert max_consecutive_ones([1, 1, 1, 1], 2) == 4
    assert max_consecutive_ones([0, 0, 0, 1], 1) == 4
    assert max_consecutive_ones([0, 0, 0, 0], 4) == 4
    assert max_consecutive_ones([1, 0, 0, 1, 1, 0, 1], 2) == 6
    assert max_consecutive_ones([0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1], 3) == 9

test_max_consecutive_ones()