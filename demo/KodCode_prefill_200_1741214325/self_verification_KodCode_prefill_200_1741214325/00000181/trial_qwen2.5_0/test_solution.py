from solution import *

from solution import fibonacci_up_to

def test_fibonacci_up_to_zero():
    assert fibonacci_up_to(0) == []

def test_fibonacci_up_to_one():
    assert fibonacci_up_to(1) == [0]

def test_fibonacci_up_to_five():
    assert fibonacci_up_to(5) == [0, 1, 1, 2, 3]

def test_fibonacci_up_to_ten():
    assert fibonacci_up_to(10) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_up_to_large_limit():
    assert fibonacci_up_to(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]