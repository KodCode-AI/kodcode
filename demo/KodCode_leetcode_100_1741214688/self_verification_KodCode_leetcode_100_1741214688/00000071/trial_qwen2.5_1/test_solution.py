from solution import *

from solution import max_road_importance
import pytest

def test_max_road_importance_1():
    n = 4
    roads = [[0, 1], [1, 2], [2, 3]]
    assert max_road_importance(n, roads) == 8

def test_max_road_importance_2():
    n = 5
    roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    assert max_road_importance(n, roads) == 11

def test_max_road_importance_3():
    n = 3
    roads = [[0, 1], [1, 2]]
    assert max_road_importance(n, roads) == 4

def test_max_road_importance_4():
    n = 6
    roads = [[0, 1], [1, 2], [2, 3], [1, 4], [2, 5]]
    assert max_road_importance(n, roads) == 13

def test_max_road_importance_5():
    n = 2
    roads = [[0, 1]]
    assert max_road_importance(n, roads) == 4