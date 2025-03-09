from solution import *

import pytest

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_positive_numbers():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

def test_bubble_sort_negative_numbers():
    assert bubble_sort([-64, -34, -25, -12, -22, -11, -90]) == [-90, -64, -34, -25, -22, -12, -11]

def test_bubble_sort_mixed_numbers():
    assert bubble_sort([-64, 34, -25, 12, -22, 11, 90]) == [-64, -25, -22, -11, 11, 12, 34, 90]

def test_bubble_sort_already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_single_element():
    assert bubble_sort([42]) == [42]