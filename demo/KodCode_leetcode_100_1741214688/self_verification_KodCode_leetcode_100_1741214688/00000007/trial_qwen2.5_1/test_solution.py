from solution import *

import pytest
from solution import DynamicArray

def test_add_and_find():
    array = DynamicArray([1, 2, 3, 4, 5])
    array.add(2, 3)  # Modify nums[2] to 6
    assert array.find(1, 4) == 6  # The maximum value in the range [1, 4] is 6

def test_add_to_end():
    array = DynamicArray([1, 2, 3])
    array.add(3, 5)  # Extend nums to [1, 2, 3, 5]
    assert array.find(2, 3) == 5  # The maximum value in the range [2, 3] is 5

def test_no_change():
    array = DynamicArray([10, 20, 30, 40, 50])
    assert array.find(1, 3) == 40  # The maximum value in the range [1, 3] is 40

def test_large_range():
    array = DynamicArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    array.add(5, 10)  # Modify nums[5] to 15
    assert array.find(0, 9) == 15  # The maximum value from index 0 to 9 is 15

def test_negative_values():
    array = DynamicArray([-10, -20, -30, -5, -40, -50])
    array.add(2, 25)  # Modify nums[2] to -5
    assert array.find(2, 5) == -5  # The maximum value in the range [2, 5] is -5