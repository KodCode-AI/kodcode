from solution import *

from solution import fibonacci

def test_fibonacci_zero_terms():
    assert fibonacci(0) == []

def test_fibonacci_one_term():
    assert fibonacci(1) == [0]

def test_fibonacci_two_terms():
    assert fibonacci(2) == [0, 1]

def test_fibonacci_five_terms():
    assert fibonacci(5) == [0, 1, 1, 2, 3]

def test_fibonacci_ten_terms():
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]