from solution import *

import pytest
from solution import calculate_circle_area

def test_area_with_radius_one():
    assert abs(calculate_circle_area(1) - math.pi) < 1e-9

def test_area_with_radius_zero():
    assert calculate_circle_area(0) == 0

def test_area_with_radius_negative():
    assert abs(calculate_circle_area(-2) - (math.pi * (2 ** 2))) < 1e-9

def test_area_with_large_radius():
    assert abs(calculate_circle_area(5) - (math.pi * (5 ** 2))) < 1e-9

def test_area_with_decimal_radius():
    assert abs(calculate_circle_area(1.5) - (math.pi * (1.5 ** 2))) < 1e-9