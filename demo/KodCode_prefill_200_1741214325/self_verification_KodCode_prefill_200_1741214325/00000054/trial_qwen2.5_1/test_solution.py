from solution import *

import pytest

def test_max_product_subarray_positive():
    assert max_product_subarray([2, 3, -2, 4]) == 6

def test_max_product_subarray_negative():
    assert max_product_subarray([-2, 0, -1]) == 0

def test_max_product_subarray_with_one_negative():
    assert max_product_subarray([0, -1]) == 0

def test_max_product_subarray_all_negative():
    assert max_product_subarray([-2, -3, -1]) == 6

def test_max_product_subarray_single_element():
    assert max_product_subarray([2]) == 2

def test_max_product_subarray_empty():
    assert max_product_subarray([]) == 0

def test_max_product_subarray_mixed():
    assert max_product_subarray([2, -5, -2, -4, 3]) == 24