from solution import *

from solution import remove_duplicates_preserve_order

def test_remove_duplicates_preserve_order_with_duplicates():
    assert remove_duplicates_preserve_order([1, 2, 3, 2, 1]) == [1, 2, 3]

def test_remove_duplicates_preserve_order_empty_list():
    assert remove_duplicates_preserve_order([]) == []

def test_remove_duplicates_preserve_order_single_element():
    assert remove_duplicates_preserve_order([5]) == [5]

def test_remove_duplicates_preserve_order_no_duplicates():
    assert remove_duplicates_preserve_order([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_remove_duplicates_preserve_order_with_negative_numbers():
    assert remove_duplicates_preserve_order([-1, -2, -3, -2, -1, 0]) == [-1, -2, -3, 0]

def test_remove_duplicates_preserve_order_with_duplicates_and_zeros():
    assert remove_duplicates_preserve_order([1, 2, 3, 2, 1, 0, 0, 3, 4]) == [1, 2, 3, 0, 4]