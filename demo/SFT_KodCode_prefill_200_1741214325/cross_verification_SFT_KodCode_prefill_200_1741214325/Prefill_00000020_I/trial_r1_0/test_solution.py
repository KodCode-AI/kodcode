from solution import *

from solution import triangle_area

def test_triangle_area_positive_numbers():
    assert triangle_area(2, 3) == 3.0

def test_triangle_area_with_zero():
    assert triangle_area(0, 5) == 0.0
    assert triangle_area(5, 0) == 0.0

def test_triangle_area_negative_numbers():
    assert triangle_area(-1, -1) == 0.5

def test_triangle_area_mixed_sign_numbers():
    assert triangle_area(-1, 3) == -1.5