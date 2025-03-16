from solution import *

from solution import filter_even_numbers

def test_filter_even_numbers_empty_list():
    assert filter_even_numbers([]) == []

def test_filter_even_numbers_all_even():
    assert filter_even_numbers([2, -4, 0, 6]) == []

def test_filter_even_numbers_all_odd():
    assert filter_even_numbers([-1, 3, 5, 7]) == [-1, 3, 5, 7]

def test_filter_even_numbers_mixed():
    assert filter_even_numbers([-2, -1, 0, 1, 2, 3]) == [-1, 1, 3]