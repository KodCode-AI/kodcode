from solution import *

from solution import min_flips_to_connect

def test_min_flips_to_connect():
    assert min_flips_to_connect([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]) == 2
    assert min_flips_to_connect([[0,0,0],[0,1,1],[0,1,0]]) == -1
    assert min_flips_to_connect([[1,0,0,1],[1,1,1,1],[0,0,0,0],[1,1,0,0]]) == 0
    assert min_flips_to_connect([[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,0,0,1],[1,1,1,1,1]]) == 1
    assert min_flips_to_connect([[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1]]) == 2