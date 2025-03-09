from solution import *

from solution import second_smallest

def test_second_smallest_with_duplicates():
    assert second_smallest([3, 5, 2, 2, 8, 1, 1, 4]) == 3

def test_second_smallest_with_single_duplicate():
    assert second_smallest([3, 3, 3, 3]) == None

def test_second_smallest_with_unique_elements():
    assert second_smallest([4, 1, 2, 6, 8, 5]) == 2

def test_second_smallest_with_all_elements_same():
    assert second_smallest([1, 1, 1]) == None

def test_second_smallest_with_empty_list():
    assert second_smallest([]) == None

def test_second_smallest_with_single_element():
    assert second_smallest([5]) == None