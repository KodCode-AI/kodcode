from solution import *

pytest
from solution import check_opposite_signs

def test_opposite_signs():
    assert check_opposite_signs(1, -1) == True
    assert check_opposite_signs(100, 200) == False
    assert check_opposite_signs(-100, -200) == False
    assert check_opposite_signs(0, 1) == True
    assert check_opposite_signs(-1, 0) == False
    assert check_opposite_signs(0, -1) == True
    assert check_opposite_signs(-1, -1) == False
    assert check_opposite_signs(0x80000000, -0x80000000) == True
    assert check_opposite_signs(-0x80000000, 0x80000000) == True
    assert check_opposite_signs(0x7fffffff, -0x80000000) == True
    assert check_opposite_signs(-0x7fffffff, 0x7fffffff) == False

def test_zero():
    assert check_opposite_signs(0, 0) == False
    assert check_opposite_signs(-0, 0) == True
    assert check_opposite_signs(0, -0) == True
    assert check_opposite_signs(-0, -0) == False