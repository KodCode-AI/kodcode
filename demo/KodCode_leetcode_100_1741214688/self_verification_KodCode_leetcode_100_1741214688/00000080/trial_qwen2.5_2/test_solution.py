from solution import *

import heapq
from solution import KClosestPoints
from typing import List

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def test_k_closest_points():
    tx, ty = 3, 3
    kcp = KClosestPoints(3)
    kcp.addPoint(1, 2)
    kcp.addPoint(2, 1)
    kcp.addPoint(3, 4)
    kcp.addPoint(4, 5)
    result = kcp.getKClosestPoints()
    expected = [[2, 1], [3, 4], [1, 2]]
    assert manhattan_distance((2, 1), (3, 3)) == manhattan_distance(expected[0], (3, 3))
    assert manhattan_distance((3, 4), (3, 3)) == manhattan_distance(expected[1], (3, 3))
    assert manhattan_distance((1, 2), (3, 3)) == manhattan_distance(expected[2], (3, 3))

    kcp = KClosestPoints(2)
    kcp.addPoint(1, 1)
    kcp.addPoint(2, 2)
    kcp.addPoint(3, 3)
    kcp.addPoint(4, 4)
    result = kcp.getKClosestPoints()
    expected = [[1, 1], [2, 2]]
    assert manhattan_distance((1, 1), (3, 3)) == manhattan_distance(expected[0], (3, 3))
    assert manhattan_distance((2, 2), (3, 3)) == manhattan_distance(expected[1], (3, 3))

test_k_closest_points()