from solution import *

from solution import max_product_subarray

def test_max_product_subarray_positive_numbers():
    assert max_product_subarray([2, 3, -2, 4]) == 6

def test_max_product_subarray_with_zero():
    assert max_product_subarray([2, 0, -2, 4]) == 8

def test_max_product_subarray_negative_numbers():
    assert max_product_subarray([-2, 0, -1]) == 0

def test_max_product_subarray_mixed_sign_numbers():
    assert max_product_subarray([-2, -3, 7]) == 42

def test_max_product_subarray_single_element():
    assert max_product_subarray([2]) == 2

def test_max_product_subarray_all_negative():
    assert max_product_subarray([-1, -2, -3, -4]) == 24

def test_max_product_subarray_empty_array():
    assert max_product_subarray([]) == 0