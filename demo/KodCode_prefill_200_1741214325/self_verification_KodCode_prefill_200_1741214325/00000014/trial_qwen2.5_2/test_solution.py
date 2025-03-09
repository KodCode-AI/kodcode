from solution import *

import pytest

def test_product_of_list_elements():
    assert product_of_list_elements([1, 2, 3, 4]) == [1, 1, 2, 6]
    assert product_of_list_elements([4, 3, 2, 1]) == [1, 4, 12, 24]
    assert product_of_list_elements([0, 2, 3]) == [1, 0, 0]
    assert product_of_list_elements([]) == []
    assert product_of_list_elements([5]) == []
    assert product_of_list_elements([1, 0, 2, 3]) == [1, 0, 0, 0]