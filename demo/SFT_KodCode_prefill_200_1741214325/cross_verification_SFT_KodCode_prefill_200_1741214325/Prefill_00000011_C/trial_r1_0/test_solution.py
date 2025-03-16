from solution import *

from solution import max_product_subarray

def test_max_product_subarray_positive_numbers():
    assert max_product_subarray([2, 3, -2, 4]) == 6

def test_max_product_subarray_mixed_sign_numbers():
    assert max_product_subarray([-2, 0, -1]) == 0

def test_max_product_subarray_large_numbers():
    assert max_product_subarray([0, 2]) == 2
    assert max_product_subarray([-1, -2, -3, 0]) == 6

def test_max_product_subarray_single_element():
    assert max_product_subarray([1]) == 1

def test_max_product_subarray_all_negative():
    assert max_product_subarray([-1, -2, -3, -4]) == 24

def test_max_product_subarray_all_positive():
    assert max_product_subarray([1, 2, 3, 4]) == 24

def test_max_product_subarray_with_zero():
    assert max_product_subarray([0, 2, 3, -5]) == 6