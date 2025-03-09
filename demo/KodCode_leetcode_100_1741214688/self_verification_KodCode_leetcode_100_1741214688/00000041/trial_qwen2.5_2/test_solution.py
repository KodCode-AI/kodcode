from solution import *

def test_min_land_bridges():
    assert min_land_bridges([[0,0,0,0,0,0,0,0]], 1) == 1
    assert min_land_bridges([[1,0,0,0,0,1,1,1],[0,0,1,1,1,1,0,0],[0,0,1,0,0,1,0,0]], 2) == 1
    assert min_land_bridges([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]], 0) == 5
    assert min_land_bridges([[1,0],[0,0],[0,1]], 1) == -1
    assert min_land_bridges([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]], 2) == -1

test_min_land_bridges()