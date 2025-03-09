from solution import *

def test_real_quadratic_roots():
    assert real_quadratic_roots(1, -3, 2) == (1.0, 2.0)
    assert real_quadratic_roots(1, 2, 1) == (-1.0, -1.0)
    assert real_quadratic_roots(1, -5, 6) == (2.0, 3.0)
    assert real_quadratic_roots(1, -5, 7) == ()
    assert real_quadratic_roots(2, -7, 3) == (0.5, 3.0)
    assert real_quadratic_roots(0, 2, 3) == ValueError # Check that it raises an error when a is zero

# Run tests
import pytest
pytest.main([__file__])