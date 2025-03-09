from solution import *

import pytest

def test_rotate_and_project():
    # Test case with rotation around y axis
    assert rotate_and_project(1.0, 2.0, 3.0, 'y', 90.0, 10.0, 10.0) == pytest.approx((7.6923076923076925, 15.384615384615385), abs=1e-6)
    
    # Test case with rotation around x axis
    assert rotate_and_project(1.0, 2.0, 3.0, 'x', 90.0, 10.0, 10.0) == pytest.approx((2.9802322387695317, 17.060701905662994), abs=1e-6)
    
    # Test case with rotation around z axis
    assert rotate_and_project(-1.0, -1.0, 1.0, 'z', 180.0, 1.0, 1.0) == pytest.approx((-1.0, -1.0), abs=1e-6)
    
    # Test case with invalid axis
    with pytest.raises(ValueError):
        rotate_and_project(1.0, 1.0, 1.0, 'w', 90.0, 10.0, 10.0)

    # Test case with invalid angle
    with pytest.raises(ValueError):
        rotate_and_project(1.0, 1.0, 1.0, 'x', -1.0, 10.0, 10.0)
    
    # Test case with invalid scale
    with pytest.raises(ValueError):
        rotate_and_project(1.0, 1.0, 1.0, 'x', 90.0, 0.0, 10.0)
    
    # Test case with invalid distance
    with pytest.raises(ValueError):
        rotate_and_project(1.0, 1.0, 1.0, 'x', 90.0, 10.0, 0.0)
    
    # Test case with non-numeric coordinates
    with pytest.raises(ValueError):
        rotate_and_project('a', 1.0, 1.0, 'x', 90.0, 10.0, 10.0)