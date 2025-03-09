from solution import *

import pytest
from solution import is_perfect_square

def test_perfect_square_positive_numbers():
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(9) == True
    assert is_perfect_square(16) == True
    assert is_perfect_square(25) == True

def test_perfect_square_zero():
    assert is_perfect_square(0) == True

def test_perfect_square_negative_numbers():
    assert is_perfect_square(-1) == False
    assert is_perfect_square(-4) == False
    assert is_perfect_square(-9) == False

def test_perfect_square_non_square_numbers():
    assert is_perfect_square(2) == False
    assert is_perfect_square(3) == False
    assert is_perfect_square(5) == False
    assert is_perfect_square(6) == False
    assert is_perfect_square(7) == False
    assert is_perfect_square(8) == False
    assert is_perfect_square(10) == False

def test_perfect_square_large_numbers():
    assert is_perfect_square(2601) == True
    assert is_perfect_square(44100) == True
    assert is_perfect_square(15241383936) == True