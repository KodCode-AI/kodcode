from solution import *

import pytest

def test_factorial_positive_numbers():
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(1) == 1

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_large_number():
    assert factorial(10) == 3628800

def test_factorial_negative_numbers():
    with pytest.raises(ValueError):
        factorial(-1)