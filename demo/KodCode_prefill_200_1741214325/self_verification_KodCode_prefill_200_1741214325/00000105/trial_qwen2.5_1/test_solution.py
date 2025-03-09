from solution import *

import pytest

def test_distance_point_to_line_horizontal_line():
    assert math.isclose(distance_point_to_line((5, 3), (1, 3), (4, 3)), 4)

def test_distance_point_to_line_vertical_line():
    assert math.isclose(distance_point_to_line((3, 5), (3, 1), (3, 4)), 4)

def test_distance_point_to_line_45_degree_line():
    assert math.isclose(distance_point_to_line((0, 0), (0, 2), (2, 0)), 2 * math.sqrt(2))

def test_distance_point_to_line_parallel_to_y_axis():
    assert math.isclose(distance_point_to_line((4, 2), (4, 1), (4, 3)), 1)

def test_distance_point_to_line_parallel_to_x_axis():
    assert math.isclose(distance_point_to_line((2, 5), (1, 5), (3, 5)), 1)