from solution import *

import pytest

def test_rotate_and_project():
    assert pytest.approx(rotate_and_project(1.0, 2.0, 3.0, 'y', 90.0, 10.0, 10.0)) == (7.6923076923076925, 15.384615384615385)
    assert pytest.approx(rotate_and_project(0.0, 0.0, 1.0, 'z', 45.0, 10.0, 10.0)) == (10.0, 0.0)

def test_invalid_input():
    with pytest.raises(ValueError):
        rotate_and_project('a', 2.0, 3.0, 'y', 90.0, 10.0, 10.0)
    with pytest.raises(ValueError):
        rotate_and_project(1.0, 2.0, 3.0, 'y', 365.0, 10.0, 10.0)
    with pytest.raises(ValueError):
        rotate_and_project(1.0, 2.0, 3.0, 'y', 90.0, 0, 10.0)
    with pytest.raises(ValueError):
        rotate_and_project(1.0, 2.0, 3.0, 'y', 90.0, 1001, 10.0)

def test_rotate_and_project_axis():
    with pytest.raises(ValueError):
        rotate_and_project(1.0, 2.0, 3.0, 'w', 90.0, 10.0, 10.0)