from solution import *

from solution import count_unique_elements

def test_count_unique_elements_empty_list():
    assert count_unique_elements([]) == 0

def test_count_unique_elements_single_repeating_elements():
    assert count_unique_elements([1, 1, 1, 2, 2, 3]) == 3
    assert count_unique_elements([2, 2, 2, 2]) == 1

def test_count_unique_elements_distinct_elements():
    assert count_unique_elements([10, 20, 30, 40, 50]) == 5

def test_count_unique_elements_mixed_elements():
    assert count_unique_elements([1, 2, 3, 2, 4, 5, 1, 3]) == 3
    assert count_unique_elements([1, 1, 1, 1, 1]) == 1