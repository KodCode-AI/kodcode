from solution import *

from solution import are_elements_unique

def test_are_elements_unique_all_unique():
    assert are_elements_unique([1, 2, 3, 4, 5]) == True

def test_are_elements_unique_with_repeats():
    assert are_elements_unique([1, 2, 3, 3, 4]) == False

def test_are_elements_unique_empty_array():
    assert are_elements_unique([]) == True

def test_are_elements_unique_single_element():
    assert are_elements_unique([1]) == True

def test_are_elements_unique_complex_data_types():
    # Test with non-hashable elements
    assert are_elements_unique([(1, 2), (1, 2), (3, 4)]) == False