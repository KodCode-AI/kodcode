from solution import *

from solution import are_elements_unique

def test_unique_elements():
    assert are_elements_unique([1, 2, 3, 4, 5]) == True

def test_duplicate_elements():
    assert are_elements_unique([1, 2, 3, 3, 5]) == False

def test_empty_array():
    assert are_elements_unique([]) == True

def test_single_element_array():
    assert are_elements_unique([42]) == True

def test_multiple_duplicates():
    assert are_elements_unique([1, 2, 3, 3, 2, 1]) == False