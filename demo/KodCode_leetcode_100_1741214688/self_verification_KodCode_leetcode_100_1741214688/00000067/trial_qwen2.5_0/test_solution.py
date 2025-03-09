from solution import *

import pytest

def test_max_array_value():
    assert max_array_value([1, 2, 3, 4, 5], 4) == 18
    assert max_array_value([4, 3, 2, 6], 2) == 20
    assert max_array_value([1], 1) == 0
    assert max_array_value([10, 10, 10], 2) == 0
    assert max_array_value([1, 1, 1, 1], 2) == 2

def test_case1():
    nums = [2, 3, 1, 5, 4]
    k = 3
    assert max_array_value(nums, k) == 12

def test_case2():
    nums = [1, 2, 3, 4, 5]
    k = 3
    assert max_array_value(nums, k) == 22

def test_case3():
    nums = [10, 5, 5, 10]
    k = 1
    assert max_array_value(nums, k) == 20