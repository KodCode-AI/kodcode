from solution import *

from solution import area_of_circle

def test_area_of_circle_positive_radius():
    assert abs(area_of_circle(1) - math.pi) < 1e-9
    assert abs(area_of_circle(2) - (4 * math.pi)) < 1e-9

def test_area_of_circle_zero_radius():
    assert area_of_circle(0) == 0.0

def test_area_of_circle_negative_radius():
    assert abs(area_of_circle(-1) - math.pi) < 1e-9

def test_area_of_circle_large_radius():
    assert abs(area_of_circle(10) - (100 * math.pi)) < 1e-9