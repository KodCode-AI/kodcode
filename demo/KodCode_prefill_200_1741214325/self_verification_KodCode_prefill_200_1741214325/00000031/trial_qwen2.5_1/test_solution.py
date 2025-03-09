from solution import *

from solution import find_closest_element

def test_closest_element_positive():
    assert find_closest_element([4, 3, 2, 5, 1], 3) == 3  # Array and target value

def test_closest_element_large_positive_number():
    assert find_closest_element([10, 20, 30, 60, 40, 50], 45) == 40  # Large positive numbers

def test_closest_element_zero():
    assert find_closest_element([0, -1, 2, 1, -1], -2) == -1  # Including zero and negative values

def test_closest_element_negative():
    assert find_closest_element([-2, -1, -5, -4, 0], -3) == -2  # Array and negative target value

def test_closest_element_one_element():
    assert find_closest_element([5], 5) == 5  # Single element array

def test_closest_element_sorted_array():
    assert find_closest_element([1, 2, 3, 4, 5], 3) == 3  # Sorted array

def test_closest_element_unsorted_array():
    assert find_closest_element([5, 3, 1, 2, 4], 3) == 3  # Unsorted array with target 3