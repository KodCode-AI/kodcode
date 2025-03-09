from solution import *

``
import pytest
from solution import find_median

def test_find_median_odd():
    assert find_median([7, 3, 5, 2, 9]) == 5

def test_find_median_even():
    assert find_median([7, 3, 5, 2, 9, 8]) == 6.5

def test_find_median_single_element():
    assert find_median([42]) == 42

def test_find_median_empty_list():
    with pytest.raises(ValueError):
        find_median([])

def test_find_median_duplicate_elements():
    assert find_median([3, 5, 5, 7, 11]) == 5