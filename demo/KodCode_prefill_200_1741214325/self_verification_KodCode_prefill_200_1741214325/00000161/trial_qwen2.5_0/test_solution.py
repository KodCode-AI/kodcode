from solution import *

import pytest
from solution import generate_combinations

def test_empty_list():
    assert generate_combinations([]) == [(),]

def test_single_element_list():
    assert generate_combinations([1]) == [(), (1,)]

def test_two_elements_list():
    assert generate_combinations([1, 2]) == [(), (1,), (2,), (1, 2)]

def test_three_elements_list():
    assert generate_combinations([1, 2, 3]) == [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

def test_with_duplicates():
    assert generate_combinations([1, 2, 1]) == [(), (1,), (2,), (1, 1), (1, 2), (2, 1)]