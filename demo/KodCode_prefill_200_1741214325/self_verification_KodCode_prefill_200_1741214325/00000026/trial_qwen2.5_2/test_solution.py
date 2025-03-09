from solution import *

from solution import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive_numbers():
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(3) == 6

def test_factorial_negative_numbers():
    assert factorial(-1) == 1  # This should not happen. Factorial is not defined for negative numbers. But included for completeness.