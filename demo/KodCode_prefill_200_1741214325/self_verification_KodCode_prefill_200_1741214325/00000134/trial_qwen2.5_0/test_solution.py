from solution import *

from solution import second_smallest

def test_second_smallest_with_unique_elements():
    assert second_smallest([3, 5, 2, 8, 1, 4]) == 2

def test_second_smallest_with_duplicates():
    assert second_smallest([3, 5, 2, 2, 8, 1, 1, 4]) == 3

def test_second_smallest_with_repeated_elements():
    assert second_smallest([1, 1, 1, 1]) == None

def test_second_smallest_with_one_unique_element():
    assert second_smallest([5]) == None

def test_second_smallest_with_all_duplicates():
    assert second_smallest([10, 10, 10]) == None