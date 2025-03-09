from solution import *

import pytest

@pytest.fixture
def dynamic_array():
    return DynamicArray([1, 3, 5, 7, 9])

def test_add_and_find(dynamic_array):
    dynamic_array.add(2, 2)
    assert dynamic_array.find(1, 4) == 9

def test_initial(find fixture):
    dynamic_array = find fixture
    assert dynamic_array.find(0, 4) == 9

def test_add_at_start(dynamic_array):
    dynamic_array.add(0, 4)
    assert dynamic_array.find(0, 4) == 13

def test_add_in_middle(dynamic_array):
    dynamic_array.add(2, -3)
    assert dynamic_array.find(0, 4) == 7

def test_large_range(find fixture):
    dynamic_array = find fixture
    dynamic_array.add(0, 5)
    dynamic_array.add(4, -5)
    assert dynamic_array.find(0, 4) == 14

def test_single_element(find fixture):
    dynamic_array = find fixture
    dynamic_array.add(1, 3)
    assert dynamic_array.find(1, 1) == 12