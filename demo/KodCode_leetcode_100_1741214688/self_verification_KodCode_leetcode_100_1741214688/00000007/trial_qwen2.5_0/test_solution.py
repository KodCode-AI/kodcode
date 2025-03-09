from solution import *

import pytest

def test_dynamic_array():
    da = DynamicArray([1, 2, 3, 4, 5])
    assert da.find(0, 4) == 5
    da.add(2, 3)
    assert da.find(0, 4) == 8
    da.add(0, 5)
    assert da.find(0, 4) == 10

def test_large_range():
    da = DynamicArray([i for i in range(1000)])
    da.add(999, 1000)
    assert da.find(0, 999) == 1999

def test_empty_array():
    da = DynamicArray([])
    with pytest.raises(IndexError):
        da.find(0, 0)

def test_single_element():
    da = DynamicArray([1])
    assert da.find(0, 0) == 1
    da.add(0, 1)
    assert da.find(0, 0) == 2

def test_one_add_operation():
    da = DynamicArray([1, 2, 3])
    da.add(1, 5)
    assert da.find(0, 2) == 7