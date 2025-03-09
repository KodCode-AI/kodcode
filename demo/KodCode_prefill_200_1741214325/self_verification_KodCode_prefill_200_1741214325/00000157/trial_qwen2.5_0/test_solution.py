from solution import *

from solution import sum_even_length_sublists

def test_sum_even_length_sublists_even():
    assert sum_even_length_sublists([[1, 2, 3, 4], [5, 6], [7, 8, 9], [10]]) == 30  # 1+2+3+4 + 7+8+9 = 30

def test_sum_even_length_sublists_odd_only():
    assert sum_even_length_sublists([[1, 2, 3], [4, 5, 6]]) == 10  # 4+5+6 = 15

def test_sum_even_length_sublists_empty():
    assert sum_even_length_sublists([[], [1, 2], [3, 4, 5, 6], [7, 8, 9, 10]]) == 30  # 1+2 + 7+8+9+10 = 30

def test_sum_even_length_sublists_all_odd():
    assert sum_even_length_sublists([[1, 2], [3, 4, 5], [6]]) == 6  # 1+2 = 3

def test_sum_even_length_sublists_single_element():
    assert sum_even_length_sublists([[1], [2, 3], [4, 5, 6], [7], []]) == 0  # No even-length sublists