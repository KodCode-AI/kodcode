from solution import *

import pytest
from solution import KClosestPoints

def test_add_point():
    kcp = KClosestPoints(3)
    kcp.addPoint(1, 2, 0, 0)
    kcp.addPoint(3, 3, 0, 0)
    kcp.addPoint(5, 5, 0, 0)
    kcp.addPoint(7, 7, 0, 0)
    kcp.addPoint(9, 9, 0, 0)
    assert kcp.getKClosestPoints(0, 0) == [[1, 2], [3, 3], [5, 5]]

def test_add_point_with_negative_coordinates():
    kcp = KClosestPoints(3)
    kcp.addPoint(1, 2, -1, -1)
    kcp.addPoint(3, 3, -2, -2)
    kcp.addPoint(5, 5, -3, -3)
    assert kcp.getKClosestPoints(-1, -1) == [[1, 2], [3, 3], [5, 5]]

def test_add_point_with_decreasing_k():
    kcp = KClosestPoints(2)
    kcp.addPoint(1, 1, 0, 0)
    kcp.addPoint(2, 2, 0, 0)
    kcp.addPoint(3, 3, 0, 0)
    assert kcp.getKClosestPoints(0, 0) == [[1, 1], [2, 2]]
    kcp.k = 3
    assert kcp.getKClosestPoints(0, 0) == [[1, 1], [2, 2], [3, 3]]

def test_get_k_closest_points():
    kcp = KClosestPoints(2)
    kcp.addPoint(1, 1, 2, 2)
    kcp.addPoint(3, 3, 2, 2)
    kcp.addPoint(4, 4, 2, 2)
    kcp.addPoint(5, 5, 2, 2)
    assert kcp.getKClosestPoints(2, 2) == [[1, 1], [3, 3]]