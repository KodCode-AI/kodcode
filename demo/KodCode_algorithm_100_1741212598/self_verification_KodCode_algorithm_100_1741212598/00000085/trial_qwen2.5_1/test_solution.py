from solution import *

import pytest

def test_real_quadratic_roots():
    # Test quadratic equation with real roots
    assert real_quadratic_roots(1, -3, 2) == (1.0, 2.0)
    # Test quadratic equation with a double root
    assert real_quadratic_roots(1, 2, 1) == (-1.0, -1.0)
    # Test quadratic equation with real and distinct roots
    assert real_quadratic_roots(1, -5, 6) == (2.0, 3.0)
    # Test quadratic equation with no real roots
    assert real_quadratic_roots(1, 0, 1) == ()
    # Test invalid input when a is zero
    with pytest.raises(ValueError, match="Coefficient 'a' must not be zero."):
        real_quadratic_roots(0, 0, 1)

# Test with zero a but valid b and c
def test_no_exception_on_zero_a_with_valid_bc():
    assert real_quadratic_roots(0, 2, 1) == (-0.5,)

# Test edge cases
def test_with_large_numbers():
    assert real_quadratic_roots(1000, -3001, 2002) == (1.998002, 2.002002)

def test_with_edge_zero():
    # Edge case where coefficients are zero
    assert real_quadratic_roots(0, 0, 0) == ()
    # More negative values
    assert real_quadratic_roots(-1, -2, -1) == (-1.0,)