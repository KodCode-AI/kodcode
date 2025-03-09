from solution import *

from solution import min_flips

def test_min_flips():
    assert min_flips([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]) == 2
    assert min_flips([[0,0,0],[0,1,1],[0,1,0]]) == -1
    assert min_flips([[1,0,0],[0,0,0],[0,0,0]]) == 0
    assert min_flips([[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]) == 1
    assert min_flips([[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,0,0,0]]) == -1
    assert min_flips([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,0]]) == 0
    assert min_flips([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]) == 0