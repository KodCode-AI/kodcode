from solution import *

from solution import multiply_by_three

def test_multiply_by_three_positive_numbers():
    assert multiply_by_three(4) == 12

def test_multiply_by_three_zero():
    assert multiply_by_three(0) == 0

def test_multiply_by_three_negative_numbers():
    assert multiply_by_three(-3) == -9

def test_multiply_by_three DECIMAL():
    assert multiply_by_three(2.5) == 7.5