from solution import *

from solution import factorial

def test_factorial_positive_numbers():
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(1) == 1

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_negative_numbers():
    try:
        factorial(-1)
        assert False, "Expected ValueError for negative input"
    except ValueError as e:
        assert str(e) == "Factorial is not defined for negative numbers"

def test_factorial_large_numbers():
    assert factorial(10) == 3628800