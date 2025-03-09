from solution import *

def test_min_land_bridges():
    assert min_land_bridges([[0,0,0,0,0,0,0,0]], 1) == 1
    assert min_land_bridges([[1,0,1], [0,0,0], [1,0,1]], 2) == 0
    assert min_land_bridges([[1,0,0,0,0,0,1,1], [1,0,1,0,1,1,1,1], [1,0,1,0,1,0,1,0], [1,0,1,0,1,1,1,0]], 2) == -1
    assert min_land_bridges([[1, 0, 1, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 1]], 3) == 2

def test_min_land_bridges_edges():
    assert min_land_bridges([[0]], 0) == 0
    assert min_land_bridges([[1]], 0) == 0
    assert min_land_bridges([[0, 1], [1, 0]], 1) == 0
    assert min_land_bridges([[0, 0], [1, 1]], 1) == 2

def test_min_land_bridges_complex():
    assert min_land_bridges([[1, 1, 0, 0, 0, 1, 1, 1], [0, 1, 1, 0, 1, 1, 0, 1], 
                             [1, 0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 0, 1, 0, 1], 
                             [1, 1, 1, 0, 1, 1, 1, 1]], 0) == -1