from solution import *

from solution import find_first_unique

def test_find_first_unique_with_repeated_elements():
    assert find_first_unique([2, 3, 4, 3, 2]) == 2

def test_find_first_unique_with_unique_first_element():
    assert find_first_unique([1, 2, 3, 4]) == 0

def test_find_first_unique_with_duplicates_only():
    assert find_first_unique([1, 1, 2, 2]) == -1

def test_find_first_unique_with_empty_list():
    assert find_first_unique([]) == -1

def test_find_first_unique_with_single_element():
    assert find_first_unique([5]) == 0

def test_find_first_unique_with_mixed_occurrences():
    assert find_first_unique([7, 8, 8, 9, 7]) == 3