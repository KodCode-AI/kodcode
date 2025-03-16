from solution import *

import pytest

def test_are_elements_unique_with_unique_elements():
    assert are_elements_unique([1, 2, 3, 4, 5]) == True

def test_are_elements_unique_with_duplicates():
    assert are_elements_unique([1, 2, 3, 3, 5]) == False

def test_are_elements_unique_with_negative_numbers():
    assert are_elements_unique([-1, -2, -3, -4, -5]) == True

def test_are_elements_unique_with_mixed_sign_numbers():
    assert are_elements_unique([0, 1, -1, 2, -2]) == True

def test_are_elements_unique_with_all_same_elements():
    assert are_elements_unique([1, 1, 1, 1, 1]) == False

def test_are_elements_unique_with_empty_list():
    assert are_elements_unique([]) == True

def test_are_elements_unique_with_single_element():
    assert are_elements_unique([42]) == True