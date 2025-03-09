from solution import *

from solution import generate_fibonacci

def test_generate_fibonacci_with_10():
    assert generate_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]

def test_generate_fibonacci_with_1():
    assert generate_fibonacci(1) == [0, 1, 1]

def test_generate_fibonacci_with_0():
    assert generate_fibonacci(0) == [0]

def test_generate_fibonacci_with_negative_number():
    assert generate_fibonacci(-1) == [0]

def test_generate_fibonacci_with_large_number():
    assert generate_fibonacci(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]