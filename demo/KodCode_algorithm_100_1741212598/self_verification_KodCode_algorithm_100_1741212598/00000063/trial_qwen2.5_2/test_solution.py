from solution import *

import pytest

def test_rotate_and_project_positive_values():
    assert rotate_and_project(1.0, 2.0, 3.0, 'y', 90.0, 10.0, 10.0) == pytest.approx((7.6923076923076925, 15.384615384615385))

def test_rotate_and_project_zero_values():
    assert rotate_and_project(0.0, 0.0, 1.0, 'z', 0.0, 10.0, 10.0) == pytest.approx((0.0, 0.0))

def test_rotate_and_project_negative_values():
    assert rotate_and_project(-1.0, -2.0, -3.0, 'x', 180.0, 10.0, 10.0) == pytest.approx((2.3076923076923075, 4.615384615384615))

def test_rotate_and_project_invalid_angle():
    with pytest.raises(ValueError, match="Angle must be between 0 and 360 degrees."):
        rotate_and_project(1.0, 2.0, 3.0, 'y', 361.0, 10.0, 10.0)

def test_rotate_and_project_invalid_axis():
    with pytest.raises(ValueError, match="Rotation axis must be 'x', 'y', or 'z'."):
        rotate_and_project(1.0, 2.0, 3.0, 'a', 90.0, 10.0, 10.0)

def test_rotate_and_project_invalid_scale():
    with pytest.raises(ValueError, match="Scale and distance must be between 1 and 1000."):
        rotate_and_project(1.0, 2.0, 3.0, 'y', 90.0, 1001.0, 10.0)

def test_rotate_and_project_invalid_distance():
    with pytest.raises(ValueError, match="Scale and distance must be between 1 and 1000."):
        rotate_and_project(1.0, 2.0, 3.0, 'y', 90.0, 10.0, 0.99)

def test_rotate_and_project_invalid_input_type():
    with pytest.raises(ValueError, match="All input values must be integers or floats."):
        rotate_and_project(1, 2, '3', 'y', 90.0, 10.0, 10.0)