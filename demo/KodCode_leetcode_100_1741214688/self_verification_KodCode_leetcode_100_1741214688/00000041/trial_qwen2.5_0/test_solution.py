from solution import *

import pytest

def test_min_land_bridges():
    assert min_land_bridges([[0,0,1,0,0],[0,1,0,1,0],[1,1,0,1,1]], 1) == 1
    assert min_land_bridges([[0,1,1,0],[0,0,0,0],[0,1,1,0]], 0) == 2
    assert min_land_bridges([[1,1,1,0,0],[0,0,1,1,1],[0,0,1,0,0]], 2) == -1
    assert min_land_bridges([[0,0,0,0,0,0,1], [0,0,0,0,0,0,1], [0,0,0,0,0,0,1]], 7) == 0
    assert min_land_bridges([[0,0,0,0,0,0,1], [0,0,0,0,0,0,1], [0,0,0,0,0,0,1]], 6) == -1

pytest.main(['-v', 'min_land_bridges.py'])