from solution import *

import pytest
from solution import is_perfect_square

def test_is_perfect_square_positive_perfect_square():
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(9) == True
    assert is_perfect_square(16) == True
    assert is_perfect_square(25) == True

def test_is_perfect_square_negative_number():
    assert is_perfect_square(-4) == False

def test_is_perfect_square_non_perfect_square():
    assert is_perfect_square(2) == False
    assert is_perfect_square(3) == False
    assert is_perfect_square(5) == False
    assert is_perfect_square(6) == False
    assert is_perfect_square(7) == False

def test_is_perfect_square_zero():
    assert is_perfect_square(0) == True

def test_is_perfect_square_large_number():
    assert is_perfect_square(15625) == True
    assert is_perfect_square(15626) == False