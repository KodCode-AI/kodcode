from solution import *

from solution import count_unique_elements

def test_count_unique_elements():
    assert count_unique_elements([1, 2, 3, 2, 4]) == 4

def test_count_unique_elements_empty_list():
    assert count_unique_elements([]) == 0

def test_count_unique_elements_duplicates():
    assert count_unique_elements([1, 2, 2, 3, 3, 3]) == 2

def test_count_unique_elements_single_unique_element():
    assert count_unique_elements([1, 1, 1, 1, 1]) == 1

def test_count_unique_elements_all_unique():
    assert count_unique_elements([1, 2, 3, 4, 5]) == 5