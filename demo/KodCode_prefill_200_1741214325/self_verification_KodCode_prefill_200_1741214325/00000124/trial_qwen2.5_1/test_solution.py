from solution import *

import pytest

def test_single_number():
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
    assert single_number([0, 1, 0]) == 1
    nums = [7, 3, 5, 3, 7, 5, 1, 1, 6]
    assert single_number(nums) == 6

def test_single_number_against_duplicates():
    assert single_number([2, 2, 2, 3, 3, 3, 4]) == 4
    assert single_number([5, 5, 5, 5, 5, 5, 7]) == 7