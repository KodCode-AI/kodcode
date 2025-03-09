from solution import *

def test_find_max_recursive():
    assert find_max_recursive([1, 2, 3, 4, 5], 5) == 5
    assert find_max_recursive([-10, -2, -3, -1], 4) == -1
    assert find_max_recursive([100], 1) == 100
    assert find_max_recursive([5, 3, 8, 20, -1, 0], 6) == 20

def test_single_element():
    assert find_max_recursive([42], 1) == 42

def test_empty_array():
    try:
        find_max_recursive([], 0)
    except ValueError as e:
        assert str(e) == "Array must contain at least one element."
    else:
        assert False, "Expected ValueError for empty array"

def test_all Negative():
    assert find_max_recursive([-5, -10, -3, -4], 4) == -3