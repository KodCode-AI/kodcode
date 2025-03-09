from solution import *

from solution import sum_even_sublists

def test_sum_even_sublists_empty_list():
    assert sum_even_sublists([]) == 0

def test_sum_even_sublists_single_element():
    assert sum_even_sublists([[1]]) == 0

def test_sum_even_sublists_all_even_sublists():
    assert sum_even_sublists([[1, 2], [3, 4], [5, 6]]) == 21

def test_sum_even_sublists_odd_and_even_sublists():
    assert sum_even_sublists([[1, 2, 3], [4, 5], [6, 7, 8], [9]]) == 20

def test_sum_even_sublists_nested_even_sublists():
    assert sum_even_sublists([[[1, 2], [3, 4, 5]], [[6, 7], [8]]]) == 24

def test_sum_even_sublists_without_even_sublists():
    assert sum_even_sublists([[1, 2, 3], [4, 5], [6, 7, 8]]) == 0