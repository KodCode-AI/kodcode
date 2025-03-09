from solution import *

from solution import remove_duplicates_preserve_order

def test_remove_duplicates_with_duplicates():
    assert remove_duplicates_preserve_order([1, 2, 3, 2, 1, 5, 6, 5, 5, 3]) == [1, 2, 3, 5, 6]

def test_remove_duplicates_empty_list():
    assert remove_duplicates_preserve_order([]) == []

def test_remove_duplicates_single_element():
    assert remove_duplicates_preserve_order([42]) == [42]

def test_remove_duplicates_no_duplicates():
    assert remove_duplicates_preserve_order([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

def test_remove_duplicates_with_negatives():
    assert remove_duplicates_preserve_order([-1, -4, -1, -3, 0, -3, 2, -1, 2]) == [-1, -4, -3, 0, 2]