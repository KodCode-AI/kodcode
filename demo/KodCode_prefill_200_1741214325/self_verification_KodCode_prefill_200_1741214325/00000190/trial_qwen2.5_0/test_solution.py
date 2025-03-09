from solution import *

from solution import is_perfect_square

def test_perfect_squares():
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(16) == True
    assert is_perfect_square(25) == True

def test_non_perfect_squares():
    assert is_perfect_square(2) == False
    assert is_perfect_square(3) == False
    assert is_perfect_square(5) == False
    assert is_perfect_square(17) == False

def test_zero():
    assert is_perfect_square(0) == True

def test_negative_numbers():
    assert is_perfect_square(-1) == False
    assert is_perfect_square(-4) == False
    assert is_perfect_square(-16) == False