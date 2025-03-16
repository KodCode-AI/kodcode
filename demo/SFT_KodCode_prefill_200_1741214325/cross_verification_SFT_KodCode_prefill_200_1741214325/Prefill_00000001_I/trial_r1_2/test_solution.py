from solution import *

from solution import selection_sort

def test_selection_sort_with_positive_numbers():
    assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]

def test_selection_sort_with_negative_numbers():
    assert selection_sort([-64, -25, -12, -22, -11]) == [-64, -25, -22, -12, -11]

def test_selection_sort_with_mixed_numbers():
    assert selection_sort([-1, 5, -7, 8, 0, 12, 10]) == [-7, -1, 0, 5, 8, 10, 12]

def test_selection_sort_with_single_element():
    assert selection_sort([5]) == [5]

def test_selection_sort_with_empty_list():
    assert selection_sort([]) == []