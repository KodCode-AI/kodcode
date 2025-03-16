from solution import *

from solution import count_unique_elements

def test_count_unique_elements_empty_list():
    assert count_unique_elements([]) == 0

def test_count_unique_elements_single_element():
    assert count_unique_elements([1]) == 1

def test_count_unique_elements_duplicate_elements():
    assert count_unique_elements([1, 2, 3, 4, 5]) == 5

def test_count_unique_elements_with_duplicates():
    assert count_unique_elements([1, 2, 2, 3, 4, 4, 5]) == 5

def test_count_unique_elements_same_elements():
    assert count_unique_elements([1, 1, 1, 1, 1]) == 1