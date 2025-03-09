from solution import *

import pytest

def test_simpson_integration():
    # Define a simple function for testing, e.g., f(x) = x^2
    def f(x):
        return x * x

    # Test with a known integral, f(x) = x^2 from 1 to 2
    approx_integral = simpson_integration(f, 1, 2, 4)
    assert approx_integral == pytest.approx(2.3333, abs=1e-4)

def test_invalid_input():
    # Test with invalid input
    with pytest.raises(ValueError):
        simps_integral = simpson_integration(lambda x: x * x, 2, 1, 4)

def test_constant_function():
    # Test with a constant function, e.g., f(x) = 1 from 0 to 10
    def f(x):
        return 1.0

    approx_integral = simpson_integration(f, 0, 10, 2)
    assert approx_integral == pytest.approx(10.0, abs=1e-2)

def test_linear_function():
    # Test with a linear function, e.g., f(x) = x from 0 to 2
    def f(x):
        return x

    approx_integral = simpson_integration(f, 0, 2, 3)
    assert approx_integral == pytest.approx(2.0, abs=1e-3)