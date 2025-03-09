from solution import *

from solution import sum_of_evens

def test_sum_of_evens_empty_list():
    assert sum_of_evens([]) == 0

def test_sum_of_evens_single_odd_element():
    assert sum_of_evens([3]) == 0

def test_sum_of_evens_single_even_element():
    assert sum_of_evens([2]) == 2

def test_sum_of_evens_multiple_elements():
    assert sum_of_evens([1, 2, 3, 4, 5, 6]) == 12

def test_sum_of_evens_with_odds():
    assert sum_of_evens([1, 3, 5, 7]) == 0

def test_sum_of_evens_with_negatives_and_zerors():
    assert sum_of_evens([-4, -3, -2, -1, 0]) == -4