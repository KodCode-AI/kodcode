from solution import *

import math
from solution import is_perfect_square

def test_is_perfect_square_positive():
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(25) == True

def test_is_perfect_square_negative():
    assert is_perfect_square(-1) == False
    assert is_perfect_square(-4) == False

def test_is_perfect_square_non_perfect_square():
    assert is_perfect_square(2) == False
    assert is_perfect_square(10) == False
    assert is_perfect_square(15) == False

def test_is_perfect_square_large_number():
    assert is_perfect_square(169) == True
    assert is_perfect_square(180) == False

def test_is_perfect_square_zero():
    assert is_perfect_square(0) == True

def test_is_perfect_square_one():
    assert is_perfect_square(1) == True