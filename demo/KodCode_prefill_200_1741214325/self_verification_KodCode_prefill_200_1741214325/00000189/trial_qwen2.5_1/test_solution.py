from solution import *

from solution import is_fibonacci

def test_is_fibonacci_0():
    assert is_fibonacci(0) == True

def test_is_fibonacci_1():
    assert is_fibonacci(1) == True

def test_is_fibonacci_8():
    assert is_fibonacci(8) == True

def test_is_fibonacci_13():
    assert is_fibonacci(13) == True

def test_is_fibonacci_34():
    assert is_fibonacci(34) == True

def test_is_fibonacci_9():
    assert is_fibonacci(9) == False

def test_is_fibonacci_25():
    assert is_fibonacci(25) == False

def test_is_fibonacci_55():
    assert is_fibonacci(55) == True

def test_is_fibonacci_89():
    assert is_fibonacci(89) == True

def test_is_fibonacci_144():
    assert is_fibonacci(144) == True

def test_is_fibonacci_145():
    assert is_fibonacci(145) == False

def test_is_fibonacci_negative():
    assert is_fibonacci(-1) == False