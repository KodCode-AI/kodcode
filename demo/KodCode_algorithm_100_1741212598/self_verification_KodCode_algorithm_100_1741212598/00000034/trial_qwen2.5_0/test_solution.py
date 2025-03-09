from solution import *

from solution import check_opposite_signs

def test_check_opposite_signs_positive_mixed():
    assert check_opposite_signs(1, -1) == True

def test_check_opposite_signs_positive_positive():
    assert check_opposite_signs(100, 200) == False

def test_check_opposite_signs_negative_negative():
    assert check_opposite_signs(-100, -200) == False

def test_check_opposite_signs_zero_non_zero():
    assert check_opposite_signs(0, 1) == True
    assert check_opposite_signs(-1, 0) == False

def test_check_opposite_signs_zero_zero():
    assert check_opposite_signs(0, 0) == False