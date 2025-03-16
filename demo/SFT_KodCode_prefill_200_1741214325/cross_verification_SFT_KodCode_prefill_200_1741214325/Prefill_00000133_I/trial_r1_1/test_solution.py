from solution import *

from solution import multiply_by_three

def test_multiply_by_three_positive_numbers():
    assert multiply_by_three(2) == 6

def test_multiply_by_three_with_zero():
    assert multiply_by_three(0) == 0

def test_multiply_by_three_negative_numbers():
    assert multiply_by_three(-1) == -3

def test_multiply_by_three_large_number():
    assert multiply_by_three(100) == 300