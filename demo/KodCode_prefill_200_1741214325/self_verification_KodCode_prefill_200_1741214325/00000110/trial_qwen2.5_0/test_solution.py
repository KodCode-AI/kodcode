from solution import *

from solution import find_median

def test_find_median_single_element():
    assert find_median([3]) == 3

def test_find_median_sorted_odd():
    assert find_median([1, 3, 5]) == 3

def test_find_median_unsorted_odd():
    assert find_median([5, 1, 3]) == 3

def test_find_median_sorted_even():
    assert find_median([1, 2, 3, 4]) == 2.5

def test_find_median_unsorted_even():
    assert find_median([3, 1, 2, 4]) == 2.5

def test_find_median_empty_list():
    assert find_median([]) is None

def test_find_median_negatives():
    assert find_median([-5, -4, -2, 1, 3]) == -2.0

def test_find_median_SINGLE_ELEMENT():
    assert find_median([9]) == 9