from solution import *

from solution import fibonacci

def test_fibonacci_0():
    assert fibonacci(0) == 0

def test_fibonacci_1():
    assert fibonacci(1) == 1

def test_fibonacci_10():
    assert fibonacci(10) == 55

def test_fibonacci_negative():
    assert fibonacci(-1) == 0

def test_fibonacci_large_value():
    assert fibonacci(50) == 12586269025