from solution import *

import pytest

def test_shortest_distance_from_point_to_line():
    # Line equation: 3x + 4y - 12 = 0
    assert shortest_distance_from_point_to_line(3, 4, -12, 1, 2) == 2.0
    # Line equation: x - y + 5 = 0
    assert shortest_distance_from_point_to_line(1, -1, 5, 0, 0) == 5.0
    # Line equation: 2x + 0y - 3 = 0
    assert shortest_distance_from_point_to_line(2, 0, -3, 0, 1) == 1.5
    # Line equation: -1x + 1y - 4 = 0
    assert shortest_distance_from_point_to_line(-1, 1, -4, 0, 0) == 4.0

# Edge Cases
def test_point_on_line():
    # Line equation: x + y - 2 = 0
    # Point (1, 1) lies on the line
    assert shortest_distance_from_point_to_line(1, 1, -2, 1, 1) == 0.0

def test_parallel_line():
    # Line equation: 4x - 2y + 10 = 0
    assert shortest_distance_from_point_to_line(4, -2, 10, 0, 0) == 5.0

def test_coincident_line():
    # Line equation: 2x + 4y - 8 = 0
    # Distance remains unchanged even for points satisfying the equation
    assert shortest_distance_from_point_to_line(2, 4, -8, 1, 1.5) == 0.5