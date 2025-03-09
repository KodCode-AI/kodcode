from solution import *

import pytest
from solution import bubble_sort

def test_bubble_sort_positive_numbers():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

def test_bubble_sort_negative_numbers():
    assert bubble_sort([-2, -34, -60, -1, -50]) == [-60, -50, -34, -2, -1]

def test_bubble_sort_mixed_sign_numbers():
    assert bubble_sort([-2, 34, -60, 12, -50, 72]) == [-60, -50, -2, 12, 34, 72]

def test_bubble_sort_single_element():
    assert bubble_sort([5]) == [5]

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_duplicate_elements():
    assert bubble_sort([4, 2, 1, 2, 3, 4]) == [1, 2, 2, 3, 4, 4]