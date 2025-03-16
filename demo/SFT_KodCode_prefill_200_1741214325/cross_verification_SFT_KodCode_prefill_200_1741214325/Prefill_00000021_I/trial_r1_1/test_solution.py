from solution import *

from solution import sum_of_even_numbers

def test_sum_of_even_numbers_empty_list():
    assert sum_of_even_numbers([]) == 0

def test_sum_of_even_numbers_no_even_numbers():
    assert sum_of_even_numbers([1, 3, 5, 7]) == 0

def test_sum_of_even_numbers_single_even_number():
    assert sum_of_even_numbers([2]) == 2

def test_sum_of_even_numbers_multiple_even_numbers():
    assert sum_of_even_numbers([2, 4, 6, 8]) == 20

def test_sum_of_even_numbers_mixed_numbers():
    assert sum_of_even_numbers([1, 2, 3, 4, 5, 6]) == 12