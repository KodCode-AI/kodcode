from solution import *

from solution import fibonacci

def test_fibonacci_positive():
    assert fibonacci(5) == [0, 1, 1, 2, 3]

def test_fibonacci_single():
    assert fibonacci(1) == [0]

def test_fibonacci_two():
    assert fibonacci(2) == [0, 1]

def test_fibonacci_zero():
    assert fibonacci(0) == []

def test_fibonacci_negative():
    assert fibonacci(-5) == []