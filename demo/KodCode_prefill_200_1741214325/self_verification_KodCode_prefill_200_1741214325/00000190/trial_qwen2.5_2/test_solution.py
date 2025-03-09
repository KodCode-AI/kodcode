from solution import *

from solution import is_perfect_square

def test_perfect_squares():
    assert is_perfect_square(1) is True  # 1 = 1^2
    assert is_perfect_square(4) is True  # 4 = 2^2
    assert is_perfect_square(9) is True  # 9 = 3^2
    assert is_perfect_square(16) is True # 16 = 4^2
    assert is_perfect_square(25) is True # 25 = 5^2

def test_non_perfect_squares():
    assert is_perfect_square(2) is False  # No integer square root
    assert is_perfect_square(3) is False  # No integer square root
    assert is_perfect_square(5) is False  # No integer square root
    assert is_perfect_square(7) is False  # No integer square root
    assert is_perfect_square(8) is False  # No integer square root

def test_zero_and_negative_numbers():
    assert is_perfect_square(0) is True  # 0 = 0^2
    assert is_perfect_square(-4) is False # Negative numbers cannot be perfect squares