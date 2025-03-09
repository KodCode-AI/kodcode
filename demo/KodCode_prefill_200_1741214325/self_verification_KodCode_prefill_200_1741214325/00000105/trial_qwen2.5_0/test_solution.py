from solution import *

from solution import shortest_distance_from_point_to_line

def test_distance_same_point():
    point = (1, 1)
    line = ((1, 1), (3, 3))
    assert shortest_distance_from_point_to_line(point, line) == 0

def test_distance_vertical_line():
    point = (2, 2)
    line = ((1, 1), (1, 4))
    assert shortest_distance_from_point_to_line(point, line) == 1

def test_distance_horizontal_line():
    point = (2, 2)
    line = ((1, 1), (4, 1))
    assert shortest_distance_from_point_to_line(point, line) == 1

def test_distance_diagonal_line():
    point = (1, 1)
    line = ((0, 0), (4, 4))
    assert shortest_distance_from_point_to_line(point, line) == 0

def test_distance_oblique_line():
    point = (3, 0)
    line = ((0, 0), (4, 3))
    expected = 3 / math.sqrt(2)
    assert math.isclose(shortest_distance_from_point_to_line(point, line), expected)

def test_distance_oblique_line2():
    point = (3, 1)
    line = ((0, 0), (4, 3))
    expected = 1 / math.sqrt(2)
    assert math.isclose(shortest_distance_from_point_to_line(point, line), expected)