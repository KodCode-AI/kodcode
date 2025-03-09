from solution import *

import pytest

def test_find_smallest_path():
    grid1 = [[1,2,3],[4,5,6],[7,8,9]]
    k1 = 3
    assert find_smallest_path(grid1, k1) == '147'
    
    grid2 = [[5,9,3],[4,1,6],[7,8,2]]
    k2 = 1
    assert find_smallest_path(grid2, k2) == '1'
    
    grid3 = [[5,3],[4,4]]
    k3 = 2
    assert find_smallest_path(grid3, k3) == '34'
    
    grid4 = [[1,1,1],[1,1,1],[1,1,1]]
    k4 = 3
    assert find_smallest_path(grid4, k4) == '111'
    
    grid5 = [[10,1,12],[11,2,13],[12,3,14]]
    k5 = 5
    assert find_smallest_path(grid5, k5) == '11213'

def test_find_smallest_path_edge_cases():
    grid6 = [[]]
    k6 = 0
    assert find_smallest_path(grid6, k6) == ''
    
    grid7 = [[1]]
    k7 = 1
    assert find_smallest_path(grid7, k7) == '1'

pytest.main()