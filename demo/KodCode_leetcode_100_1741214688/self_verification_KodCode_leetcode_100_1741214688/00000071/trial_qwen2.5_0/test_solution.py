from solution import *

from solution import max_road_importance

def test_max_road_importance():
    # Example 1
    n = 5
    roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    assert max_road_importance(n, roads) == 43
    
    # Example 2
    n = 4
    roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
    assert max_road_importance(n, roads) == 26
    
    # Example 3
    n = 3
    roads = [[0, 1], [1, 2], [0, 2], [2, 1]]
    assert max_road_importance(n, roads) == 18
    
    # Edge Case: Single City
    n = 1
    roads = []
    assert max_road_importance(n, roads) == 1