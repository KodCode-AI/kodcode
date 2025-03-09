from solution import *

from solution import fibonacci

def test_fibonacci_zero():
    assert fibonacci(0) is None

def test_fibonacci_one():
    assert fibonacci(1) == 0

def test_fibonacci_two():
    assert fibonacci(2) == 1

def test_fibonacci_three():
    assert fibonacci(3) == 1

def test_fibonacci_four():
    assert fibonacci(4) == 2

def test_fibonacci_five():
    assert fibonacci(5) == 3

def test_fibonacci_six():
    assert fibonacci(6) == 5

def test_fibonacci_large_number():
    assert fibonacci(10) == 34

def test_fibonacci_invalid_input():
    try:
        fibonacci(-1)
    except ValueError as e:
        assert str(e) == "n must be a positive integer"
    else:
        assert False, "ValueError was expected"