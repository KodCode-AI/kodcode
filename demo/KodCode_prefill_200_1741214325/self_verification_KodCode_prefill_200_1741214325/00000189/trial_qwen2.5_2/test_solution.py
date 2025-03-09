from solution import *

from solution import is_fibonacci

def test_is_fibonacci_small_numbers():
    assert is_fibonacci(0) == True
    assert is_fibonacci(1) == True
    assert is_fibonacci(8) == True
    assert is_fibonacci(13) == True

def test_is_fibonacci_large_numbers():
    assert is_fibonacci(144) == True
    assert is_fibonacci(233) == True
    assert is_fibonacci(89) == True
    assert is_fibonacci(377) == True

def test_is_fibonacci_non_fibonacci_numbers():
    assert is_fibonacci(2) == False
    assert is_fibonacci(4) == False
    assert is_fibonacci(7) == False
    assert is_fibonacci(10) == False