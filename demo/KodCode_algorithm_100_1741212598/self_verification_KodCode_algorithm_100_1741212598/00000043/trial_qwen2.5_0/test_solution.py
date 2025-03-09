from solution import *

import mpmath
from solution import calculate_pi_efficient

def test_calculate_pi_efficient():
    precision = 50
    expected = str(mpmath.mp/mp.pi)  # Convert mpmath.pi to string with the specified precision
    approximation = calculate_pi_efficient(precision)
    assert len(approximation) - approximation.rstrip('0').rfind('.') - 1 == precision  # Verify the precision
    assert float(approximation) == float(expected)  # Verify the value

def test_calculate_pi_small_precision():
    precision = 10
    expected = str(mpmath.mp.mp.pi)  # Convert mpmath.pi to string with the specified precision
    approximation = calculate_pi_efficient(precision)
    assert len(approximation) - approximation.rstrip('0').rfind('.') - 1 == precision
    assert float(approximation) == float(expected)

def test_calculate_pi_large_precision():
    precision = 100
    expected = str(mpmath.mp/mp.pi)
    approximation = calculate_pi_efficient(precision)
    assert len(approximation) - approximation.rstrip('0').rfind('.') - 1 == precision
    assert float(approximation) == float(expected)