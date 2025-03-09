from solution import *

from solution import product_of_list_elements

def test_product_of_list_elements_empty_list():
    assert product_of_list_elements([]) == []

def test_product_of_list_elements_single_element():
    assert product_of_list_elements([1]) == [1]

def test_product_of_list_elements_positive_numbers():
    assert product_of_list_elements([1, 2, 3, 4]) == [1, 1, 2, 6]

def test_product_of_list_elements_mixed_sign_numbers():
    assert product_of_list_elements([1, 2, -2, 4]) == [1, 1, -2, -4]

def test_product_of_list_elements_with_zero():
    assert product_of_list_elements([1, 0, 2]) == [1, 0, 0]