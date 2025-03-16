from solution import *

import pytest

def test_is_perfect_number():
    assert is_perfect_number(6) == True  # 1+2+3 = 6
    assert is_perfect_number(28) == True  # 1+2+4+7+14 = 28
    assert is_perfect_number(496) == True  # 1+2+4+8+16+31+62+124+248 = 496
    assert is_perfect_number(8128) == True  # 1+2+4+8+16+32+64+127+254+508+1016+2032+4064 = 8128
    assert is_perfect_number(12) == False  # 1+2+3+4+6 = 16
    assert is_perfect_number(10) == False  # 1+2+5 = 8
    assert is_perfect_number(0) == False  # 0 is not a perfect number
    assert is_perfect_number(-28) == False  # Negative numbers are not considered perfect