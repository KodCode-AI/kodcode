from solution import *

from solution import selection_sort

def test_selection_sort_positive_numbers():
    assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]

def test_selection_sort_negative_numbers():
    assert selection_sort([-64, -25, -12, -22, -11]) == [-64, -25, -22, -12, -11]

def test_selection_sort_mixed_numbers():
    assert selection_sort([64, -25, 0, 22, -11, 12]) == [-25, -11, 0, 12, 22, 64]

def test_selection_sort_empty_list():
    assert selection_sort([]) == []

def test_selection_sort_single_element():
    assert selection_sort([5]) == [5]