from solution import *

def test_generate_fibonacci_with_small_numbers():
    assert generate_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]

def test_generate_fibonacci_with_large_number():
    assert generate_fibonacci(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_generate_fibonacci_with_zero():
    assert generate_fibonacci(0) == [0]

def test_generate_fibonacci_with_negative_number():
    assert generate_fibonacci(-5) == []

def test_generate_fibonacci_with_single_element():
    assert generate_fibonacci(1) == [0, 1]