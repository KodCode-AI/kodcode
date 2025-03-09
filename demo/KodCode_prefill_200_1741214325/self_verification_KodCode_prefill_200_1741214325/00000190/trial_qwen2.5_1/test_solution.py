from solution import *

import unittest

def is_perfect_square(n):
    """Checks if a given number n is a perfect square."""
    if n < 0:
        return False
    root = math.isqrt(n)
    return n == root * root

def test_is_perfect_square_positive_numbers():
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(16) == True
    assert is_perfect_square(25) == True

def test_is_perfect_square_zero():
    assert is_perfect_square(0) == True

def test_is_perfect_square_negative_numbers():
    assert is_perfect_square(-1) == False
    assert is_perfect_square(-16) == False

def test_is_perfect_square_non_perfect_squares():
    assert is_perfect_square(2) == False
    assert is_perfect_square(5) == False
    assert is_perfect_square(10) == False
    assert is_perfect_square(15) == False

def test_is_perfect_square_large_numbers():
    assert is_perfect_square(1681) == True
    assert is_perfect_square(676) == True
    assert is_perfect_square(315186841) == True

if __name__ == "__main__":
    unittest.main()