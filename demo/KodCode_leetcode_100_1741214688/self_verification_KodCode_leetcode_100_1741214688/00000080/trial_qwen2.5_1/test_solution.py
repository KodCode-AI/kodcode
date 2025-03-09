from solution import *

import pytest
from solution import KClosestPoints

def test_k_closest_points():
    k = 3
    tx, ty = 0, 0
    points = KClosestPoints(k)

    points.addPoint(1, 1)
    points.addPoint(2, 2)
    points.addPoint(3, 3)
    points.addPoint(-1, -1)

    closest_points = points.getKClosestPoints()
    assert len(closest_points) == k  # Ensure we get exactly k points

    assert abs(closest_points[0][0] - tx) + abs(closest_points[0][1] - ty) == 2  # (1, 1) closest
    assert abs(closest_points[1][0] - tx) + abs(closest_points[1][1] - ty) == 2  # (2, 2) second closest
    assert abs(closest_points[2][0] - tx) + abs(closest_points[2][1] - ty) == 2  # (-1, -1) third closest

    # Ensure the order is maintained based on distance
    assert closest_points[0] < closest_points[1] < closest_points[2]

def test_adding_same_point():
    k = 2
    tx, ty = 0, 0
    points = KClosestPoints(k)

    points.addPoint(1, 1)
    points.addPoint(1, 1)
    
    closest_points = points.getKClosestPoints()
    assert len(closest_points) == k  # Ensure we get exactly k points

    assert all(point == [1, 1] for point in closest_points)

def test_large_number_of_points():
    k = 5
    tx, ty = 0, 0
    points = KClosestPoints(k)

    for x in range(-10, 11):
        for y in range(-10, 11):
            points.addPoint(x, y)

    closest_points = points.getKClosestPoints()
    assert len(closest_points) == k  # Ensure we get exactly k points

    # Verify closest points
    actual_distances = sorted([abs(point[0] - tx) + abs(point[1] - ty) for point in closest_points])
    expected_distance = sorted([abs(i - tx) + abs(j - ty) for i in range(-10, 11) for j in range(-10, 11) if abs((i, j)) < k + 0.5])
    assert actual_distances == expected_distance