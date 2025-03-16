from solution import *

def test_find_max_recursive():
    assert find_max_recursive([1, 3, 5, 7, 9], 5) == 9
    assert find_max_recursive([10], 1) == 10
    assert find_max_recursive([5, 3, 8, 6, 2], 5) == 8
    assert find_max_recursive([-1, -3, -2, -5, -7], 5) == -1
    assert find_max_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 10