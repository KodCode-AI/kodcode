from solution import *

from solution import sum_of_evens

def test_sum_of_evens_with_even_numbers():
    assert sum_of_evens([1, 2, 3, 4, 5, 6]) == 12

def test_sum_of_evens_with_odd_numbers():
    assert sum_of_evens([1, 3, 5, 7]) == 0

def test_sum_of_evens_with_mixed_numbers():
    assert sum_of_evens([10, 23, 45, 68, 90]) == 256

def test_sum_of_evens_with_negative_numbers():
    assert sum_of_evens([-2, -4, -6, -8]) == -20

def test_sum_of_evens_with_empty_list():
    assert sum_of_evens([]) == 0