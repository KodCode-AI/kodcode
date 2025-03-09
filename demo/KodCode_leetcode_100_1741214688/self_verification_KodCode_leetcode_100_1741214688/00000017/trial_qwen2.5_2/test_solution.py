from solution import *

def test_max_consecutive_ones():
    assert max_consecutive_ones([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert max_consecutive_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
    assert max_consecutive_ones([0,0,0,1], 0) == 1
    assert max_consecutive_ones([1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1], 2) == 12
    assert max_consecutive_ones([0,0,0,0], 1) == 1