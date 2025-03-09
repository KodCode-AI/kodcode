from solution import *

from solution import result_array

def test_result_array_empty():
    assert result_array([]) == []

def test_result_array_single_element():
    assert result_array([1]) == [0]

def test_result_array_constant_elements():
    assert result_array([1, 1, 1]) == [0, 0, 0]

def test_result_array_increasing_elements():
    assert result_array([1, 2, 3, 4]) == [0, 1, 3, 6]

def test_result_array_decreasing_elements():
    assert result_array([4, 3, 2, 1]) == [6, 3, 1, 0]

def test_result_array_mixed_elements():
    assert result_array([2, 3, 1, 4, 5]) == [0, 1, 0, 3, 6]