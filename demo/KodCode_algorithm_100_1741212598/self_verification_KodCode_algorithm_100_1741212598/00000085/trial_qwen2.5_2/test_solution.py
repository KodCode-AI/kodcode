from solution import *

import pytest

def test_real_quadratic_roots():
    # Roots are not real
    assert real_quadratic_roots(1, 0, 1) == ()
    # One root
    assert real_quadratic_roots(1, -2, 1) == (1.0,)
    # Two roots
    assert real_quadratic_roots(1, -3, 2) == (1.0, 2.0)
    # Duplicate roots
    assert real_quadratic_roots(1, 2, 1) == (-1.0,)
    # Edge case: coefficient 'a' is zero
    with pytest.raises(ValueError) as excinfo:
        real_quadratic_roots(0, 1, 2)
    assert str(excinfo.value) == "Coefficient 'a' must not be zero."

def test_performance():
    # Test with large coefficients
    assert real_quadratic_roots(1000, -2000, 1000) == (1.0, 1.0)
    # Test with small coefficients
    assert real_quadratic_roots(1, -1, -6) == (3.0, -2.0)
    # Test with negative coefficients
    assert real_quadratic_roots(-1, 5, 6) == (-2.0, -3.0)