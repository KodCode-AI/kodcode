from solution import *

``
from solution import bubble_sort

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    assert bubble_sort([5]) == [5]

def test_bubble_sort_sorted_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted_list():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_random_list():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

def test_bubble_sort_with_duplicates():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 11, 90, 22]) == [11, 11, 12, 22, 22, 25, 34, 64, 90]