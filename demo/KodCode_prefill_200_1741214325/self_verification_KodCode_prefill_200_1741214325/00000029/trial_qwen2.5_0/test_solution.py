from solution import *

from solution import bubble_sort

def test_bubble_sort_empty():
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    assert bubble_sort([5]) == [5]

def test_bubble_sort_already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_descending_order():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_random_numbers():
    assert bubble_sort([34, 12, 24, 9, 5]) == [5, 9, 12, 24, 34]

def test_bubble_sort_with_duplicates():
    assert bubble_sort([2, 4, 1, 2, 3]) == [1, 2, 2, 3, 4]