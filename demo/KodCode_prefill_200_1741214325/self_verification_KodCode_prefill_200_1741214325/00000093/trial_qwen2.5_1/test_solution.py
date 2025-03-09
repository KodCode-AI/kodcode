from solution import *

from solution import find_smallest_number

def test_find_smallest_number_positive_integers():
    assert find_smallest_number([3, 1, 4, 1, 5, 9]) == 1

def test_find_smallest_number_single_element():
    assert find_smallest_number([42]) == 42

def test_find_smallest_number_negative_integers():
    assert find_smallest_number([-5, -2, -10, -1]) == -10

def test_find_smallest_number_empty_array():
    with pytest.raises(ValueError):
        find_smallest_number([])

def test_find_smallest_number_mixed_signs():
    assert find_smallest_number([-1, 1, -3, 3, -2, 2]) == -3