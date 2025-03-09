from solution import *

from solution import find_max

def test_find_max_with_positive_numbers():
    assert find_max([2, 3, 1]) == 3

def test_find_max_with_negative_numbers():
    assert find_max([-1, -5, -3]) == -1

def test_find_max_with_mixed_sign_numbers():
    assert find_max([-1, 0, 5, 3, -2]) == 5

def test_find_max_with_single_element():
    assert find_max([42]) == 42

def test_find_max_empty_list():
    with pytest.raises(ValueError):
        find_max([])

def test_find_max_with_floats():
    assert find_max([1.5, 2.3, 0.7]) == 2.3