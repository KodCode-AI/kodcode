from solution import *

from solution import sum_two_numbers

def test_sum_two_positive_numbers():
    assert sum_two_numbers(2, 3) == 5

def test_sum_with_zero():
    assert sum_two_numbers(0, 5) == 5
    assert sum_two_numbers(5, 0) == 5

def test_sum_negative_numbers():
    assert sum_two_numbers(-1, -1) == -2

def test_sum_mixed_sign_numbers():
    assert sum_two_numbers(-1, 3) == 2
    assert sum_two_numbers(4, -4) == 0