from solution import *

from solution import bubble_sort

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    assert bubble_sort([5]) == [5]

def test_bubble_sort_positive_numbers():
    assert bubble_sort([34, 12, 24, 9, 5]) == [5, 9, 12, 24, 34]

def test_bubble_sort_negative_numbers():
    assert bubble_sort([34, -34, 12, -12, 24, -24, 9, -9, 5, -5]) == [-34, -24, -12, -9, -5, 5, 9, 12, 24, 34]

def test_bubble_sort_mixed_sign_numbers():
    assert bubble_sort([34, -34, 0, -5, 9, 5, -9, 12, 24, -24, 17, -17]) == [-34, -24, -17, -9, -5, 0, 5, 9, 12, 17, 24, 34]

def test_bubble_sort already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]