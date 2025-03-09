from solution import *

from solution import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_positive_numbers():
    assert factorial(5) == 120
    assert factorial(3) == 6

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_large_number():
    assert factorial(10) == 3628800

def test_factorial_negative_number():
    try:
        factorial(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative input"