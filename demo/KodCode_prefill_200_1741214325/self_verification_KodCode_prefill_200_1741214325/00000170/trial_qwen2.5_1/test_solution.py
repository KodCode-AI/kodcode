from solution import *

from solution import sum_of_naturals

def test_sum_of_naturals_positive_numbers():
    assert sum_of_naturals(5) == 15

def test_sum_of_naturals_zero():
    assert sum_of_naturals(0) == 0

def test_sum_of_naturals_one():
    assert sum_of_naturals(1) == 1

def test_sum_of_naturals_large_number():
    assert sum_of_naturals(100) == 5050