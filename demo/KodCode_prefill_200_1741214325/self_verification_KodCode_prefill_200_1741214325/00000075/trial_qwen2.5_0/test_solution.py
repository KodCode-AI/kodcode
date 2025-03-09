from solution import *

from solution import is_perfect_number

def test_is_perfect_number_small():
    assert not is_perfect_number(1)
    assert is_perfect_number(6)  # 1 + 2 + 3 = 6
    assert is_perfect_number(28) # 1 + 2 + 4 + 7 + 14 = 28

def test_is_perfect_number_large():
    assert not is_perfect_number(100)
    assert is_perfect_number(496) # 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = 496
    assert not is_perfect_number(8128) # This is a known perfect number, but not in the range where we expect false negatives

def test_is_perfect_number_negative():
    assert not is_perfect_number(-28)

def test_is_perfect_number_zero():
    assert not is_perfect_number(0)