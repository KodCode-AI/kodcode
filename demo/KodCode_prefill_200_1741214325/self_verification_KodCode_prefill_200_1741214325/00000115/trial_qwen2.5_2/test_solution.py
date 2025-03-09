from solution import *

from solution import find_max

def test_find_max_positive_numbers():
    assert find_max([1, 2, 3, 4, 5]) == 5

def test_find_max_with_negative_numbers():
    assert find_max([-5, -2, -6, -1]) == -1

def test_find_max_single_element():
    assert find_max([42]) == 42

def test_find_max_empty_list():
    with pytest.raises(ValueError):
        find_max([])

def test_find_max_mixed_signals():
    assert find_max([-10, 0, 10, 20, -5]) == 20