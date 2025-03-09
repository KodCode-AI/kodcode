from solution import *

import pytest
from decimal import Decimal

def test_enhanced_factorial_integers():
    assert enhanced_factorial(5) == "120"
    assert enhanced_factorial(20) == "2432902008176640000"
    assert enhanced_factorial(0) == "1"
    assert enhanced_factorial(10) == "3628800"

def test_enhanced_factorial_floats():
    assert enhanced_factorial(0.5) == "1.128"
    assert enhanced_factorial(3.5) == "11.632"
    assert enhanced_factorial(-0.5) == "1.772"
    assert enhanced_factorial(1.1) == "1.182"

def test_enhanced_factorial_large_numbers():
    assert enhanced_factorial(100) == str(gamma(101))  # Using gamma for large number comparison
    assert enhanced_factorial(1000) == str(gamma(1001))  # Using gamma for large number comparison

def test_enhanced_factorial_zero():
    assert enhanced_factorial(0) == "1"

def test_enhanced_factorial_negative_inputs():
    with pytest.raises(ValueError):
        enhanced_factorial(-1)