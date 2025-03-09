from solution import *

from solution import sum_of_natural_numbers

def test_sum_of_natural_numbers_with_1():
    assert sum_of_natural_numbers(1) == 1

def test_sum_of_natural_numbers_with_5():
    assert sum_of_natural_numbers(5) == 15

def test_sum_of_natural_numbers_with_10():
    assert sum_of_natural_numbers(10) == 55

def test_sum_of_natural_numbers_with_0():
    assert sum_of_natural_numbers(0) == 0

def test_sum_of_natural_numbers_with_negative_number():
    assert sum_of_natural_numbers(-1) == 0